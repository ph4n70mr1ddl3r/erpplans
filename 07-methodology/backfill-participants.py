#!/usr/bin/env python3
"""
backfill-participants.py — Derive the missing `| **Participants** |` field row from Steps.

A generation artifact shipped the gap-analysis-batch value streams VS-53–VS-63 (plus single
workflows in VS-86/87/99/189) without the required Participants field row, even though every
affected workflow carries a fully-authored Steps table naming its Responsible/Accountable
roles. This closes that gap mechanically on the honest-draft principle used by
`backfill-time-estimate.py`: the values come from content already authored in the workflow
(its own per-step Role (R) / Role (A) columns); nothing is invented.

Derivation rule, per workflow block:
  1. Collect every role token from the Steps table's Role (R) and Role (A) columns, splitting
     compound "A / B" cells; drop blanks, em-dashes and system actors (System, POS System,
     Ecommerce System, CRM, Automated) — Participants lists the people/teams involved
     (customers, vendors and agencies included), matching the register style of e.g. VS-73.
  2. Normalize a small set of abbreviation variants to the house form used elsewhere in the
     same file family (Category Mgr -> Category Manager, ...).
  3. Drop the Owner row's own components (Participants is "all OTHER roles involved").
  4. De-duplicate preserving first-appearance order; insert `| **Participants** | A, B, C |`
     immediately after the `| **Owner** | ... |` row.

Idempotent: a workflow that already has a Participants row is never touched; a workflow whose
steps yield no human roles is skipped and reported (needs human authoring).

Usage:
    python3 07-methodology/backfill-participants.py           # write changes
    python3 07-methodology/backfill-participants.py --check   # report only, exit 1 if pending
"""
import argparse, glob, os, re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(REPO, "01-model-company", "workflows")

SYSTEM_ACTORS = {
    "System", "Systems", "POS System", "Ecommerce System", "Ecommerce Platform",
    "ERP", "ERP System", "CRM", "CDP", "OMS", "WMS", "Automated", "Various",
    "HQ Function", "—", "-",
}
# Abbreviation variants -> house form (only exact-token matches are rewritten).
NORMALIZE = {
    "Category Mgr": "Category Manager",
    "Logistics Mgr": "Logistics Manager",
    "Store Ops Dir": "Store Ops Director",
    "Regional Ops Mgr": "Regional Ops Manager",
    "Logistics Coord": "Logistics Coordinator",
    "Merch Coordinator": "Merchandising Coordinator",
    "Merch Coordinator": "Merchandising Coordinator",
    "VP Merch": "VP Merchandising",
    "Merch Planner": "Merchandising Planner",
    "Customer Service Dir": "Customer Service Director",
    "Vendor Coord": "Vendor Coordinator",
    "Ecom Logistics Coord": "Ecom Logistics Coordinator",
    "Ecom Quality Coord": "Ecom Quality Coordinator",
    "VP Legal": "VP Legal & Compliance",
}

STEP_ROW_RE = re.compile(
    r'^\| (?:\d+[a-z]?|[A-Z]{1,3}-\d+) \|.*?\|([^|]*)\|([^|]*)\|[^|]*\|$', re.M)
OWNER_RE = re.compile(r'^\| \*\*Owner\*\* \| (.*?) \|$', re.M)
HAS_PART_RE = re.compile(r'^\| \*\*Participants\*\*', re.M)
WF_RE = re.compile(r"^## (W\d+[A-Z]?)\..*?(?=^## W|\Z)", re.M | re.S)


def derive_participants(block):
    """Return the derived Participants value or None if no human roles are found."""
    owner = OWNER_RE.search(block)
    owner_tokens = set()
    if owner:
        owner_tokens = {t.strip() for t in owner.group(1).split('/') if t.strip()}
    seen, ordered = set(), []
    for m in STEP_ROW_RE.finditer(block):
        for cell in (m.group(1), m.group(2)):
            for tok in (t.strip() for t in cell.split('/')):
                if not tok or tok in SYSTEM_ACTORS:
                    continue
                tok = NORMALIZE.get(tok, tok)
                if tok in SYSTEM_ACTORS or tok in owner_tokens or tok in seen:
                    continue
                seen.add(tok)
                ordered.append(tok)
    return ", ".join(ordered) if ordered else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true',
                    help='report pending changes without writing; exit 1 if any pending')
    args = ap.parse_args()

    files = sorted(glob.glob(os.path.join(WORKFLOWS, 'VS-*', 'PA-*.md')))
    filled, skipped = 0, []
    for f in files:
        text = open(f, encoding='utf-8').read()
        out, changed = [], False
        pos = 0
        for m in WF_RE.finditer(text):
            block = m.group(0)
            if not HAS_PART_RE.search(block):
                participants = derive_participants(block)
                if participants:
                    om = OWNER_RE.search(block)
                    if om:
                        row = om.group(0)
                        new_block = block.replace(
                            row, row + f"\n| **Participants** | {participants} |", 1)
                        out.append((m.start(), m.end(), new_block))
                        filled += 1
                        changed = True
                        continue
                skipped.append((os.path.relpath(f, REPO), re.match(r'## (W\d+[A-Z]?)', block).group(1)))
        if changed:
            # apply replacements back-to-front
            new_text = text
            for s, e, nb in reversed(out):
                new_text = new_text[:s] + nb + new_text[e:]
            if not args.check:
                open(f, 'w', encoding='utf-8').write(new_text)
    print(f"PA files scanned: {len(files)}")
    print(f"Participants rows {'pending' if args.check else 'backfilled'}: {filled}")
    if skipped:
        print(f"Skipped (no human roles derivable — needs human): {len(skipped)}")
        for f, w in skipped:
            print(f"  {f}: {w}")
    if args.check:
        raise SystemExit(1 if filled else 0)


if __name__ == '__main__':
    main()
