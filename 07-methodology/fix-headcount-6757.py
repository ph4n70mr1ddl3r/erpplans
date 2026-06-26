#!/usr/bin/env python3
"""
fix-headcount-6757.py — Propagate the 2026-06-25 headcount change (6,757 -> 6,762)
into the workflow catalog body.

Context: the 2026-06-25 S&OP/IBP change moved total company headcount 6,757 -> 6,762
(+5 in Supply Chain & Logistics) and HQ 357 -> 362. The summary documents were updated
but the per-workflow prose was not, leaving ~97 workflow files still citing "6,757" as
the current workforce. This script replaces stale *current-figure* occurrences of
"6,757" with "6,762" across 01-model-company/workflows/ (PA files + READMEs + the
cross-reference docs that live there).

SAFE per-occurrence replacement — only current-figure prose is touched:
  - Skips any occurrence whose surrounding window contains an arrow ('->' or the
    Unicode '->'), so legitimate historical change-notes like "6,715 -> 6,757",
    "6,757 -> 6,762", or "total 6,757 -> 6,762" are preserved verbatim.
  - Skips workflow-gap-analysis.md entirely (canonical historical record).
  - Word-boundary match so '6,757' inside a larger number is never touched.
  - Idempotent: a file already at 6,762 (no stale 6,757) is a no-op.

Companion to the 2026-06-26 CHANGELOG entry. Does NOT touch the per-VS '357' HQ
references or technical-guidelines.md (those are fixed by hand in the same pass);
this script focuses solely on the 6,757 total-headcount figure.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WF_DIR = os.path.join(ROOT, "01-model-company", "workflows")
SKIP_FILES = {"workflow-gap-analysis.md"}  # canonical historical record
OLD = "6,757"
NEW = "6,762"
ARROW_WINDOW = 25  # chars each side to inspect for an arrow (historical context)

# Match 6,757 not embedded in a longer number (digit boundary on both sides).
PAT = re.compile(r"(?<!\d)6,757(?!\d)")


def is_historical(line: str, idx: int) -> bool:
    """True if this occurrence sits inside a 'X -> Y' change-note (skip it)."""
    lo = max(0, idx - ARROW_WINDOW)
    hi = min(len(line), idx + len(OLD) + ARROW_WINDOW)
    window = line[lo:hi]
    return ("->" in window) or ("\u2192" in window)  # ASCII '-'+'>' or Unicode '→'


def process(path: str):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    orig = text
    replaced = 0
    skipped = 0

    def repl(m):
        nonlocal replaced, skipped
        if is_historical(text, m.start()):
            skipped += 1
            return m.group(0)
        replaced += 1
        return NEW

    new_text = PAT.sub(repl, text)
    if new_text != orig:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new_text)
    return replaced, skipped


def main():
    if not os.path.isdir(WF_DIR):
        print(f"ERROR: workflows dir not found: {WF_DIR}", file=sys.stderr)
        return 2
    tot_rep = tot_skip = tot_files = 0
    details = []
    for dirpath, _dirs, files in os.walk(WF_DIR):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            if fn in SKIP_FILES:
                continue
            path = os.path.join(dirpath, fn)
            rep, skip = process(path)
            if rep or skip:
                rel = os.path.relpath(path, ROOT)
                details.append((rel, rep, skip))
                tot_files += 1 if rep else 0
            tot_rep += rep
            tot_skip += skip
    print(f"Files changed:           {tot_files}")
    print(f"Occurrences replaced:    {tot_rep}   ({OLD} -> {NEW})")
    print(f"Historical refs skipped: {tot_skip}   (arrow-context '->' / '->')")
    print("\nPer-file (changed files only):")
    for rel, rep, skip in sorted(details):
        if rep:
            print(f"  {rep:3d} replaced, {skip} skipped  {rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
