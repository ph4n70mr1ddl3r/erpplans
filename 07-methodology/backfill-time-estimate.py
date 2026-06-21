#!/usr/bin/env python3
"""
backfill-time-estimate.py — Mechanically derive the `### Time Estimate` section where absent.

WORKFLOW-FORMAT-GUIDE.md lists Time Estimate as a required field for every workflow. A
2026-06-21 scan (validator Check 22) found **410 workflows** missing it — a generation
artifact concentrated in VS-27/37/38/39/40 and a few others, where whole batches shipped
with the field omitted despite having fully-written Steps tables with per-step Durations.

This tool fills that gap mechanically and honestly. For each workflow missing Time Estimate
it parses the Steps table's Duration column and emits a draft roll-up of the form:

    ### Time Estimate
    - Step 1: <duration>
    - Step 2: <duration>
    - ...
    - *Draft roll-up from per-step Durations (mechanically derived). Annualize per the
      workflow's Frequency/Volume where the total drives headcount; refine with the
      workflow-specific context (the house style is per-step ranges + an annual figure).*

This is NOT fabrication: every value comes from the workflow's own authored step Durations
(already workflow-specific), and the output is explicitly labelled a draft pending human
annualization. It does not invent throughput math (receipts/year, etc.) — that is domain
content requiring human judgement, deliberately left out (same honest-draft principle as
the Automation/Controls fields).

Scope rule (conservative): a workflow's Time Estimate is generated ONLY IF the section is
absent AND a Steps table with >=1 parseable Duration exists. Workflows also missing Steps
(16 cases — genuine structural defects needing manual fixing) are skipped, as are workflows
whose Durations don't parse (rare; reported).

Idempotent: re-running on an already-filled file is a no-op (the `### Time Estimate`
section is then present).

Usage:
    python3 07-methodology/backfill-time-estimate.py           # write changes
    python3 07-methodology/backfill-time-estimate.py --check   # report only, exit 1 if pending
"""
import argparse, glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(REPO, "01-model-company", "workflows")

# A workflow block split. Keeps the '## W' header on each block.
BLOCK_SPLIT = re.compile(r"(?=^## W\d+[A-Z]?\. )", re.MULTILINE)

# Steps table row: | # | Activity | Role (R) | Role (A) | Duration |
# Step number may be '1', '2', '1a', '3.1' etc. Tolerate trailing pipes / spaces.
STEP_ROW = re.compile(
    r"^\|\s*(\d+[a-z]?(?:\.\d+)?)\s*\|\s*(.+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|"
)

TE_PRESENT = re.compile(r"^### Time Estimate\s*$", re.MULTILINE)
TE_TABLE_PRESENT = re.compile(r"^\| \*\*Time Estimate\*\*", re.MULTILINE)


def parse_steps_table(block):
    """Return [(step_num, duration), ...] from the Steps table, or [] if absent/unparseable."""
    m = re.search(r"^### Steps\s*\n(.*?)(?=^### |^---|^## |\Z)", block, re.MULTILINE | re.DOTALL)
    if not m:
        return []
    out = []
    for line in m.group(1).split("\n"):
        rm = STEP_ROW.match(line)
        if rm:
            num, activity, r, a, dur = rm.groups()
            # skip header/separator rows (Activity wouldn't match a real step, but guard)
            if activity.lower() in ("activity", "---") or set(activity) <= {"-"}:
                continue
            out.append((num, dur.strip()))
    return out


def has_time_estimate(block):
    return bool(TE_PRESENT.search(block) or TE_TABLE_PRESENT.search(block))


def build_time_estimate(steps):
    """Build the draft Time Estimate body from per-step Durations."""
    lines = ["### Time Estimate"]
    for num, dur in steps:
        if dur:
            lines.append(f"- Step {num}: {dur}")
        else:
            lines.append(f"- Step {num}: (duration not specified)")
    lines.append(
        "- *Draft roll-up from per-step Durations (mechanically derived by "
        "`07-methodology/backfill-time-estimate.py`). Annualize per the workflow's "
        "Frequency/Volume where the total drives headcount; refine to the per-step range "
        "+ annual figure house style shown in WORKFLOW-FORMAT-GUIDE.md.*"
    )
    return "\n".join(lines) + "\n"


def transform_file(path, write=True):
    """Return (sections_added, workflows_skipped_no_steps)."""
    text = open(path, encoding="utf-8", errors="replace").read()
    original = text

    blocks = BLOCK_SPLIT.split(text)
    if len(blocks) <= 1:
        return 0, 0

    added = 0
    skipped_no_steps = 0
    new_blocks = [blocks[0]]
    for block in blocks[1:]:
        if has_time_estimate(block):
            new_blocks.append(block)
            continue
        steps = parse_steps_table(block)
        if not steps:
            skipped_no_steps += 1
            new_blocks.append(block)
            continue
        te_body = build_time_estimate(steps)
        # Insert at the END of the workflow body: immediately before the '---' separator
        # that delimits this workflow from the next (middle blocks end with '\n---'; the
        # last block in a file ends with '\n---\n\n*Workflow Count...*'). Use rfind to
        # locate the LAST '\n---' in the block — that is always the workflow separator
        # (never an internal table-row rule, which is '\n|---|'). This keeps Time
        # Estimate inside the workflow body and before the file footer, so Check 16
        # (PA-footer format) is unaffected.
        sep = block.rfind("\n---")
        if sep == -1:
            # No separator (malformed); append at end as a safe fallback.
            new_block = block.rstrip("\n") + "\n\n" + te_body
        else:
            new_block = block[:sep].rstrip("\n") + "\n\n" + te_body + "\n" + block[sep:]
        new_blocks.append(new_block)
        added += 1

    new_text = "".join(new_blocks)
    if added and new_text != original:
        if write:
            open(path, "w", encoding="utf-8").write(new_text)
    return added, skipped_no_steps


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="report pending changes without writing; exit 1 if any pending")
    args = ap.parse_args()

    files = sorted(glob.glob(os.path.join(WORKFLOWS, "VS-*", "PA-*.md")))
    total_added = 0
    total_skipped = 0
    files_changed = 0
    for f in files:
        added, skipped = transform_file(f, write=not args.check)
        if added:
            files_changed += 1
            total_added += added
        total_skipped += skipped

    print(f"PA files scanned: {len(files)}")
    print(f"PA files with a Time Estimate added: {files_changed}")
    print(f"Time Estimate sections added: {total_added}")
    print(f"Workflows skipped (also missing Steps — manual fix needed): {total_skipped}")
    if args.check:
        sys.exit(1 if total_added else 0)


if __name__ == "__main__":
    main()
