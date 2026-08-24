#!/usr/bin/env python3
"""
fix-table-structure.py — one-time markdown table-structure repairer
(companion to validator Check 29)

A 2026-06-28 whole-repo review (consistency review #17) found 18 table defects the
validator did not cover: Check 13's column-count guard scans only the summary docs
(root README, 01-model-company/*.md, workflows/*.md, 07-methodology/*.md) and only
compares DATA rows against the header — it never verified the delimiter (separator)
row, and never scanned the 569 PA files. GFM requires the delimiter row to match the
header row's cell count or the table is not recognized at all (the whole block
renders as plain paragraph text on GitHub), so these were live rendering defects:

  Class 1 — delimiter row MISSING columns (9 sites): 5-column Steps tables
    ('| # | Activity | Role (R) | Role (A) | Duration |') whose delimiter row had
    only 4 cells (VS-09 x3, VS-11, VS-13, VS-20, VS-29 x2), plus a 2-column
    Field/Detail table with a 1-cell delimiter (VS-28). Generator artifacts.
  Class 2 — delimiter row with EXCESS columns (7 sites): 2-column Field/Detail
    tables whose delimiter had 4–5 cells (VS-105 x5, VS-133, VS-170) — a 5-column
    steps-delimiter template pasted under a 2-column field header.
  Class 3 — stray 1-cell data row '| **Steps** |' inside a 2-column Field/Detail
    table (VS-162 PA-162.3): an empty-Detail row that pads to a spurious blank row.
  Class 4 — DOUBLED delimiter line (VS-29 PA-29.2): two consecutive 4-cell
    delimiter rows under one 5-column header.

This script repairs all four classes idempotently:
  - rewrites a mismatched delimiter row to the header's cell count, preserving any
    per-cell alignment colons when the cell survives;
  - collapses doubled delimiter lines to a single (corrected) delimiter;
  - deletes a data row that is exactly '| **Steps** |' (the empty-Detail artifact);
  - any OTHER data-row/column mismatch is only REPORTED (never auto-edited) — those
    need per-case judgment (a long cell may simply need an escaped '\\|').

Code-fence aware (tables inside ``` blocks are ignored) and escaped-pipe aware
('\\|' is a literal, not a cell separator), matching Check 29's detector semantics.

Run from anywhere: paths are resolved from the repository root (script's parent).
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SEP_RE = re.compile(r'^\|[\s:|-]+\|\s*$')
STRAY_STEPS_RE = re.compile(r'^\| \*\*Steps\*\* \|$')


def ncells(line: str) -> int:
    """Number of table cells, treating escaped '\\|' as a literal (not a separator)."""
    return re.sub(r'\\\|', '', line).count('|') - 1


def rewrite_delim(line: str, want: int) -> str:
    """Rewrite a delimiter row to `want` cells, preserving per-cell alignment colons."""
    cells = [c.strip() for c in line.strip().strip('|').split('|')]
    out = []
    for i in range(want):
        if i < len(cells):
            body = cells[i].replace('-', '') or '-'
            out.append(f'{body:-<3}')
        else:
            out.append('---')
    return '|' + '|'.join(out) + '|'


def fix_file(path: Path, log: list) -> bool:
    text = path.read_text(encoding='utf-8')
    lines = text.split('\n')
    changed = False
    fence = False
    i = 0
    while i < len(lines):
        if lines[i].startswith('```'):
            fence = not fence
            i += 1
            continue
        if fence or not lines[i].startswith('|'):
            i += 1
            continue
        # candidate header: a pipe row whose next line is a delimiter row
        if i + 1 < len(lines) and not SEP_RE.match(lines[i]) and SEP_RE.match(lines[i + 1]):
            hdr = ncells(lines[i])
            sep = lines[i + 1]
            if ncells(sep) != hdr:
                lines[i + 1] = rewrite_delim(sep, hdr)
                log.append(f"{path.relative_to(ROOT)}:{i + 2} delimiter {ncells(sep)} -> {hdr} cells")
                changed = True
            j = i + 2
            # collapse any immediately-following duplicate delimiter lines
            while j < len(lines) and SEP_RE.match(lines[j]):
                log.append(f"{path.relative_to(ROOT)}:{j + 1} duplicate delimiter line removed")
                del lines[j]
                changed = True
            # data rows: only the empty-Detail '| **Steps** |' artifact is auto-fixed
            while j < len(lines) and lines[j].startswith('|') and not SEP_RE.match(lines[j]):
                if STRAY_STEPS_RE.match(lines[j]) and hdr == 2:
                    log.append(f"{path.relative_to(ROOT)}:{j + 1} stray '| **Steps** |' row removed")
                    del lines[j]
                    changed = True
                    continue
                if ncells(lines[j]) != hdr:
                    log.append(f"{path.relative_to(ROOT)}:{j + 1} REPORT-ONLY data row has "
                               f"{ncells(lines[j])} cells vs header {hdr}: {lines[j][:60]!r}")
                j += 1
            i = j
            continue
        i += 1
    if changed:
        path.write_text('\n'.join(lines), encoding='utf-8')
    return changed


def main() -> int:
    log: list = []
    fixed = 0
    for path in sorted(ROOT.rglob('*.md')):
        if '__pycache__' in str(path) or '.git' in path.parts:
            continue
        if fix_file(path, log):
            fixed += 1
    for entry in log:
        print(entry)
    print(f"\n{fixed} file(s) modified; {len([e for e in log if 'REPORT-ONLY' not in e])} fix(es) applied; "
          f"{len([e for e in log if 'REPORT-ONLY' in e])} report-only finding(s).")
    return 0


if __name__ == '__main__':
    sys.exit(main())
