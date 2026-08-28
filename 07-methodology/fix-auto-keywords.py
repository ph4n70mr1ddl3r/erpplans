#!/usr/bin/env python3
"""
fix-auto-keywords.py — Repair glitched keywords in the defragmented
`### Automation Opportunity` bullets.

`defragment-automation.py` (2026-06-21) repaired add-automation-controls.py's
mid-phrase fragments into the honest form

    - System auto-<verb> of "<keyword>" (replaces manual Step N).

but its keyword extractor left four glitch classes, repaired here against each
bullet's own referenced step text:

  * mid-word clips        — 'auto-log of "logy"' where the step says
                            "technology"/"Logistics"…; the bullet is re-quoted
                            with the full in-step word containing the clip;
  * entity-name captures  — 'auto-log of "Logistics Inc."' where the step names
                            a BuildRight legal entity; flagged --manual for
                            hand repair (the honest object is step-specific);
  * punctuation artifacts — trailing ',', ';' or spaces inside the quotes;
  * nested quotes         — 'of "generates "Sold Consignment Report"…"' —
                            re-quoted with the inner quoted phrase.

Also normalizes case-variant keywords ('Review' → 'review'; the dominant form
is lowercase) — 'Logistics Inc.'-style captures are excluded from that rule.

Idempotent; reports every edit. PA files only; bullets outside the canonical
form are untouched.

The tool also normalizes 41 cell-bounded RACI role-title variants to their
dominant forms (plurals, abbreviation spellings, OHS Officer -> HSE Officer,
and the org-chart ghost 'VP Communications' -> Marketing Comms Manager);
--check is the zero-false-positive guard enforced by validator Check 53.
"""
import argparse, glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(REPO, "01-model-company", "workflows")

BULLET = re.compile(r'- System auto-(\w+) of "([^"]*)" \(replaces manual Step (\d+)\)\.')
CASE_NORMALIZE = {"Review": "review", "Check": "check", "Documentation": "documentation",
                  "Tracking": "tracking", "Request": "request", "Assignment": "assignment",
                  "Counts": "counts", "Documents": "documents", "Reports": "reports",
                  "Logs": "logs", "Reviews": "reviews", "Checks": "checks"}


def step_activity(block, n):
    m = re.search(r"^\| " + re.escape(n) + r" \| (.+?) \|", block, re.M)
    return m.group(1) if m else ""


def fix_keyword(kw, verb, block, stepn, notes):
    orig = kw
    # nested quotes: keep the first inner quoted phrase
    if '"' in kw[1:-1] or "“" in kw:
        m2 = re.search(r"[\"“]([^\"”]{3,80})[\"”]", kw)
        if m2:
            kw = m2.group(1)
    kw = kw.rstrip(",;").strip()
    if kw in CASE_NORMALIZE:
        kw = CASE_NORMALIZE[kw]
    if kw == "logy":
        act = step_activity(block, stepn)
        m3 = re.search(r"\b\w*logy\w*\b", act, re.I)
        if m3:
            kw = m3.group(0).lower()
            notes.append(f"clip repaired from step word: '{orig}' -> '{kw}'")
        elif "technology" in act.lower():
            kw = "technology"
            notes.append(f"clip repaired via step 'technology': '{orig}' -> '{kw}'")
        else:
            notes.append(f"MANUAL: '{orig}' (no in-step logy word)")
    elif re.search(r"\bLogistics,? Inc\.\b", kw) and len(kw) < 30:
        notes.append(f"MANUAL entity-name capture: '{orig}'")
    return kw


ROLE_VARIANTS = [
    ("Account Managers", "Account Manager"), ("Sponsors", "Sponsor"),
    ("Store Associates", "Store Associate"), ("Approvers", "Approver"),
    ("Cashiers", "Cashier"), ("Contractors", "Contractor"), ("Pickers", "Picker"),
    ("DC Managers", "DC Manager"), ("Dept. Supervisors", "Dept. Supervisor"),
    ("Drivers", "Driver"), ("Supervisors", "Supervisor"),
    ("Dept Supervisors", "Dept Supervisor"),
    ("Marketing Comm Manager", "Marketing Comms Manager"),
    ("Property Mgmt", "Property Mgr"), ("Gov Affairs", "Govt Affairs"),
    ("Service Center Mgr", "Service Center Manager"), ("BCM Manager", "BC Manager"),
    ("Digital Commerce Mgr", "Digital Commerce Manager"),
    ("HR Training Mgr", "HR Training Manager"), ("Real Estate Mgr", "Real Estate Manager"),
    ("Sustainability Mgr", "Sustainability Manager"),
    ("Merchandising Mgr", "Merchandising Manager"),
    ("External Adviser", "External Advisor"), ("OHS Officer", "HSE Officer"),
    ("Department Leads", "Department Heads"), ("HR Payroll Specialist", "Payroll Specialist"),
    ("HR Labor Relations", "Labor Relations"),
    ("Supply Chain Planner (HQ)", "Supply Chain Planner"),
    ("VP Communications", "Marketing Comms Manager"), ("Legal Lead", "Legal Head"),
    ("All participants", "All Participants"), ("All staff", "All Staff"),
    ("All store staff", "All Store Staff"), ("Customer-Service Rep", "Customer Service Rep"),
    ("external counsel", "External Counsel"), ("First-aider", "First Aider"),
    ("HR EX", "HR-EX"), ("HR L&D", "HR-L&D"),
    ("Human Rights DD", "Human-Rights DD"),
    ("Treasury analyst", "Treasury Analyst"), ("Treasury specialist", "Treasury Specialist"),
]

RETIRED_KEYWORDS = ["logy", "Logistics Inc.", "Logistics, Inc."]


def check_file(path, hits):
    """Guard mode: retired keyword glitches and cell-bounded role variants."""
    text = open(path, encoding="utf-8").read()
    rel = os.path.relpath(path, REPO)
    for kw in RETIRED_KEYWORDS:
        if f'of "{kw}"' in text:
            line = text[:text.find(f'of "{kw}"')].count("\n") + 1
            hits.append(("retired-keyword", rel, line, kw))
    for m in re.finditer(r'auto-\w+ of "([^"\n]*)"', text):
        q = m.group(1)
        if q != q.strip() or q.rstrip(",;") != q or '"' in q[1:-1]:
            line = text[:m.start()].count("\n") + 1
            hits.append(("glitched-keyword", rel, line, f"'{q[:60]}'"))
    for var, canon in ROLE_VARIANTS:
        pat = re.compile(r"(?<=\| )" + re.escape(var) + r"(?=[ /|])|(?<=/ )" +
                         re.escape(var) + r"(?=[ /|])")
        for m in pat.finditer(text):
            line = text[:m.start()].count("\n") + 1
            hits.append(("role-variant", rel, line, f"'{var}' -> '{canon}'"))
            break


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="guard mode: exit 1 on retired keyword glitches or "
                         "cell-bounded role-title variants")
    args = ap.parse_args()
    if args.check:
        hits = []
        files = sorted(glob.glob(os.path.join(WORKFLOWS, "VS-*", "PA-*.md")))
        for f in files:
            check_file(f, hits)
        for kind, rel, line, detail in hits:
            print(f"{kind}: {rel}:{line}: {detail}")
        print(f"fix-auto-keywords --check: {len(hits)} hit(s) across {len(files)} PA files")
        sys.exit(1 if hits else 0)
    total_edits = 0
    manual = []
    for f in sorted(glob.glob(os.path.join(WORKFLOWS, "VS-*", "PA-*.md"))):
        text = open(f, encoding="utf-8").read()
        out = []
        edits = 0
        pos = 0
        result = []
        for bm in re.finditer(r"(^## W\d+[A-Z]?\. )(.*)$", text, re.M):
            start = bm.start()
            end = None
            nxt = re.search(r"^## W\d+[A-Z]?\. ", text[start + 1:], re.M)
            end = start + 1 + nxt.start() if nxt else len(text)
            result.append((start, end))
        for start, end in result:
            block = text[start:end]
            notes = []
            new_block = BULLET.sub(
                lambda m: f'- System auto-{m.group(1)} of "{fix_keyword(m.group(2), m.group(1), block, m.group(3), notes)}" (replaces manual Step {m.group(3)}).',
                block)
            if notes:
                edits += 1
                for note in notes:
                    if note.startswith("MANUAL"):
                        manual.append((os.path.relpath(f, REPO), note))
                    else:
                        print(f"{os.path.relpath(f, REPO)}: {note}")
            out.append(text[pos:start])
            out.append(new_block)
            pos = end
        out.append(text[pos:])
        new_text = "".join(out)
        if new_text != text:
            open(f, "w", encoding="utf-8").write(new_text)
            total_edits += 1
    print(f"\nfiles edited: {total_edits}; manual follow-ups: {len(manual)}")
    for rel, note in manual:
        print(f"  {rel}: {note}")


if __name__ == "__main__":
    main()
