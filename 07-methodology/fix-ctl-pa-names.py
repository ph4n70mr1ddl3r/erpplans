#!/usr/bin/env python3
"""
fix-ctl-pa-names.py — One-time canonicalizer of the CTL-240–808 process-area operating
controls' objective names (companion to validator Check 34).

Background: add-pa-controls.py derived each PA control's objective name from the PA file
slug via humanize() (title-cased hyphen-split), and backfill-controls.py truncated the
result to 90 characters mid-word when mirroring it into PA-file Controls bullets. Both
generators ran before fix-pa-names.py established the value-stream-index bullet as the
canonical PA name (review #18), so all three surfaces drifted apart:

  - proper nouns mangled: "S&OP"->"Sandop", "DENR"->"Denr", "ERP"->"Erp", "DC"->"Dc",
    "B2B"->"B2b", "CIP"->"Cip", "FP&A"->"Fpanda", "DG"->"Dg", "AI"->"Ai";
  - words dropped: "Vendor Quality Management & Audit"->"Vendor Quality Audit",
    "Annual Business Planning & Budgeting"->"Annual Business Planning";
  - "&"/","/"-" punctuation stripped: "Store Waste Segregation & Collection"->
    "Store Waste Segregation Collection";
  - 145 PA-body parentheticals truncated mid-word at 90 chars (e.g. "...Modeling
    Registrati.").

This script rewrites, from the canonical index names:
  1. every internal-controls-matrix.md row
       "| CTL-NNN | Ensure controlled execution — <name> (PA-XX.Y) | ..."
     -> name := canonical index name of PA-XX.Y;
  2. every PA-file Controls bullet parenthetical
       "CTL-NNN (ensure controlled execution — <anything>.)"
     -> "CTL-NNN (ensure controlled execution — <canonical name> (PA-XX.Y).)"
     using the CTL->PA mapping from the matrix (so cross-PA citations keep their own PA).

Hand-written contextual CTL glosses (e.g. "CTL-06 (vendor certification)") are untouched —
only the machine-generated "ensure controlled execution" class is rewritten. Idempotent;
--check reports only and exits non-zero when changes remain.

Usage:
    python3 07-methodology/fix-ctl-pa-names.py --dry-run
    python3 07-methodology/fix-ctl-pa-names.py
"""
import argparse
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(REPO, "01-model-company", "workflows")
INDEX = os.path.join(WORKFLOWS, "value-stream-index.md")
MATRIX = os.path.join(REPO, "01-model-company", "internal-controls-matrix.md")

MATRIX_ROW = re.compile(r"^(\| CTL-\d{3} \| )Ensure controlled execution — .+? \(PA-(\d{2,3}\.\d)\)( \| .*)$")
BODY_BULLET = re.compile(r"(CTL-\d{3}) \(ensure controlled execution — .*?\.\)")


def canonical_pa_names():
    """PA-XX.Y -> canonical name, from the value-stream-index bullets (canonical source)."""
    names = {}
    text = open(INDEX, encoding="utf-8").read()
    for m in re.finditer(r"- \*\*(PA-\d{2,3}\.\d)\*\* \[([^\]]+)\]\(", text):
        names[m.group(1)] = m.group(2)
    return names


def ctl_to_pa():
    """CTL-NNN -> PA-XX.Y for the PA operating controls (CTL-240–808), from the matrix."""
    mapping = {}
    for line in open(MATRIX, encoding="utf-8"):
        m = MATRIX_ROW.match(line.rstrip("\n"))
        if m:
            mapping[m.group(1) if False else re.match(r"\| (CTL-\d{3})", line).group(1)] = "PA-" + m.group(2)
    return mapping


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    dry = args.dry_run or args.check

    canon = canonical_pa_names()
    if len(canon) != 569:
        print(f"ABORT: expected 569 canonical PA names, found {len(canon)}", file=sys.stderr)
        sys.exit(2)

    # Pass 1: matrix rows.
    matrix_text = open(MATRIX, encoding="utf-8").read()
    rows_changed = 0
    out_lines = []
    for line in matrix_text.splitlines(keepends=True):
        m = MATRIX_ROW.match(line.rstrip("\n"))
        if m:
            pa = "PA-" + m.group(2)
            if pa not in canon:
                print(f"ABORT: matrix row cites unknown PA {pa}", file=sys.stderr)
                sys.exit(2)
            new = f"{m.group(1)}Ensure controlled execution — {canon[pa]} ({pa}){m.group(3)}\n"
            if new != line:
                rows_changed += 1
                line = new
        out_lines.append(line)
    new_matrix = "".join(out_lines)

    ctl_map = {}
    for line in new_matrix.splitlines():
        m = MATRIX_ROW.match(line)
        if m:
            ctl_map[re.match(r"\| (CTL-\d{3})", line).group(1)] = "PA-" + m.group(2)
    if len(ctl_map) != 569:
        print(f"ABORT: expected 569 PA-control rows, found {len(ctl_map)}", file=sys.stderr)
        sys.exit(2)

    # Pass 2: PA-file bullets.
    bullets_changed = 0
    files_changed = 0
    for vs in sorted(os.listdir(WORKFLOWS)):
        d = os.path.join(WORKFLOWS, vs)
        if not vs.startswith("VS-") or not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if not (f.startswith("PA-") and f.endswith(".md")):
                continue
            p = os.path.join(d, f)
            text = open(p, encoding="utf-8").read()

            def repl(m):
                nonlocal bullets_changed
                ctl = m.group(1)
                pa = ctl_map.get(ctl)
                if pa is None:      # not a PA operating control; leave untouched
                    return m.group(0)
                want = f"{ctl} (ensure controlled execution — {canon[pa]} ({pa}).)"
                if m.group(0) != want:
                    bullets_changed += 1
                return want

            new_text = BODY_BULLET.sub(repl, text)
            if new_text != text:
                files_changed += 1
                if not dry:
                    open(p, "w", encoding="utf-8").write(new_text)

    print(f"matrix objective rows canonicalized: {rows_changed}/569")
    print(f"PA-body parentheticals canonicalized: {bullets_changed} across {files_changed} files")
    if not dry and rows_changed:
        open(MATRIX, "w", encoding="utf-8").write(new_matrix)
    if dry and (rows_changed or bullets_changed):
        sys.exit(1)


if __name__ == "__main__":
    main()
