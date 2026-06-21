#!/usr/bin/env python3
"""
backfill-controls.py — Normalize `### Controls` formatting and backfill CTL-XX references.

Two related fixes applied in one pass over every PA file:

  1. Blank-line normalization. A prior generation run (`add-automation-controls.py`) wrote
     `### Controls` bodies with no separating blank line before the following `###` header,
     so the two sections render glued together. This ensures exactly one blank line between
     a Controls body and the next `###` / `##` / `---` / EOF. (3,235 sections were affected.)

  2. CTL-XX backfill. `internal-controls-matrix.md` maps each of the 67 controls to the
     workflows that exercise it (its `Workflows` column). This script reverses that into a
     workflow -> controls index and, for any workflow whose `### Controls` body cites NO
     CTL-XX today but IS mapped in the matrix, prepends the mapped control(s) as a properly
     formatted bullet `- CTL-XX (objective); ...`. Existing content is never removed or
     rewritten — this only ADDS references where a real mapping exists.

Both transforms are idempotent: re-running on an already-fixed file is a no-op.

Scope note: the 67-control register was authored against the Core workflows (W1-W942), so
only ~60 workflows currently have a matrix mapping. The gap-analysis block (W2993+) is not
yet covered by the register; extending the register is a separate, manual effort tracked by
validator Check 21. This tool will pick up any new mappings automatically as the register grows.

Usage:
    python3 07-methodology/backfill-controls.py           # write changes
    python3 07-methodology/backfill-controls.py --check   # report only, exit non-zero if changes pending
"""
import argparse, glob, os, re, sys
from collections import defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(REPO, "01-model-company", "workflows")
MATRIX = os.path.join(REPO, "01-model-company", "internal-controls-matrix.md")

CONTROLS_HEADER = "### Controls"
NEXT_BOUNDARY = r"(?=^### |^---|^## |\Z)"


def build_workflow_to_controls():
    """Parse internal-controls-matrix.md into {workflow_base_id: [(ctl_id, objective), ...]}."""
    ctl_obj = {}                     # CTL-XX -> objective string
    ctl_wfs = defaultdict(set)       # CTL-XX -> {workflow ids}
    for line in open(MATRIX, encoding="utf-8"):
        m = re.match(r"^\|\s*(CTL-\d+)\s*\|\s*(.+?)\s*\|\s*[PD]\s*\|", line)
        if not m:
            continue
        cid, obj = m.group(1), m.group(2).strip().rstrip(";").strip()
        ctl_obj[cid] = obj
        for tok in re.findall(r"W\d+[A-Z]?(?:\.\d+[a-z]?)?", line):
            base = re.match(r"(W\d+[A-Z]?)", tok).group(1)
            ctl_wfs[cid].add(base)
    wf_to_ctl = defaultdict(list)
    for cid, wfs in ctl_wfs.items():
        for wf in sorted(wfs):
            wf_to_ctl[wf].append((cid, ctl_obj[cid]))
    return wf_to_ctl


def controls_bullet(wf_id, wf_to_ctl):
    """Build the '- CTL-XX (objective); ...' bullet for a workflow, or '' if no mapping."""
    refs = wf_to_ctl.get(wf_id)
    if not refs:
        return ""
    # De-dup by ctl id (a control mapped via multiple sub-step tokens lists once)
    seen, parts = set(), []
    for cid, obj in refs:
        if cid in seen:
            continue
        seen.add(cid)
        # Keep objectives short and lowercase-initial for inline parenthetical flow
        o = obj[:90].rstrip(".") + "."
        parts.append(f"{cid} ({o[0].lower() + o[1:]})")
    return "- " + "; ".join(parts)


def transform_file(path, wf_to_ctl):
    """Apply both fixes to one PA file. Returns (changed, backfilled_count)."""
    text = open(path, encoding="utf-8", errors="replace").read()
    original = text
    backfilled = 0

    # Split into workflow blocks on '## W' headers so we know each Controls section's owner.
    parts = re.split(r"(?=^## W\d+[A-Z]?\. )", text, flags=re.MULTILINE)
    if len(parts) <= 1:
        return False, 0

    # Map from block start offset -> workflow id, by re-scanning the original text.
    wf_at = {}  # char offset -> workflow base id
    for m in re.finditer(r"^## (W\d+[A-Z]?)\.", text, re.MULTILINE):
        wf_at[m.start()] = m.group(1)

    out = []
    cursor = 0
    for part in parts:
        # Find where this part sits in the original to resolve its workflow id.
        # parts[0] is the preamble (before the first '## W'); subsequent parts each start
        # with the '## W' header that re.split kept via the lookahead.
        block_start = text.find(part, cursor)
        if block_start == -1:
            out.append(part)  # safety; shouldn't happen
            continue
        # Resolve workflow id: nearest header at or before block_start that is a '## W'
        wf_id = None
        for off in wf_at:
            if off <= block_start and off >= (cursor - 1):
                wf_id = wf_at[off]
        cursor = block_start + len(part)

        if wf_id is None:
            out.append(part)
            continue

        out.append(_fix_block(part, wf_id, wf_to_ctl))

    new_text = "".join(out)
    if new_text != original:
        # Count how many Controls sections in THIS file got a CTL bullet added.
        backfilled = _count_backfilled(original, new_text)
        if not args_check:
            open(path, "w", encoding="utf-8").write(new_text)
        return True, backfilled
    return False, 0


def _fix_block(block, wf_id, wf_to_ctl):
    """Within one workflow block, fix each `### Controls` section."""
    pattern = re.compile(
        r"(^### Controls\n)(.*?)" + NEXT_BOUNDARY,
        re.MULTILINE | re.DOTALL,
    )

    def repl(m):
        header = m.group(1)
        body = m.group(2)
        # --- Fix 2: CTL backfill (only if no CTL-XX cited and a mapping exists) ---
        if "CTL-" not in body:
            bullet = controls_bullet(wf_id, wf_to_ctl)
            if bullet:
                body = bullet + "\n" + body.lstrip("\n")
                _backfill_counter[0] += 1
        # --- Fix 1: blank-line normalization before the next header ---
        # Strip trailing blank lines, then ensure exactly one trailing newline so the
        # following '###'/'##'/'---'/EOF is preceded by a blank line.
        body = body.rstrip("\n") + "\n\n"
        return header + body

    return pattern.sub(repl, block)


def _count_backfilled(original, new_text):
    """Heuristic: difference in 'CTL-' occurrence count, clamped to >= 0."""
    before = original.count("\n- CTL-")
    after = new_text.count("\n- CTL-")
    return max(0, after - before)


_backfill_counter = [0]
args_check = False


def main():
    global args_check
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="report pending changes without writing; exit 1 if any pending")
    args = ap.parse_args()
    args_check = args.check

    wf_to_ctl = build_workflow_to_controls()
    files = sorted(glob.glob(os.path.join(WORKFLOWS, "VS-*", "PA-*.md")))

    changed_files = 0
    total_backfilled = 0
    for f in files:
        changed, n = transform_file(f, wf_to_ctl)
        if changed:
            changed_files += 1
            total_backfilled += n

    print(f"PA files scanned: {len(files)}")
    print(f"PA files with changes: {changed_files}")
    print(f"Controls sections backfilled with CTL-XX refs: {_backfill_counter[0]}")
    if args.check:
        sys.exit(1 if changed_files else 0)


if __name__ == "__main__":
    main()
