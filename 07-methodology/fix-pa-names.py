#!/usr/bin/env python3
"""
fix-pa-names.py — Canonicalize process-area names across the three places they appear.

Consistency review #18 (2026-06-28) found 38 name drifts no prior check could see: a
process area's name is stated in three places — the PA file's H1 (`# PA-XX.Y — Name`),
its VS README 'Process Areas' table row, and the value-stream-index.md PA bullet — and
38 of the 569 triplets had drifted apart (mostly Expansion-block files whose H1s were
shortened at generation time: 'Coupon & Voucher Creation' vs the canonical
'Coupon & Voucher Creation & Distribution'; plus 'and'→'&', ':'→'—', and one VS README
outlier, PA-69.1, where H1 and index agreed but the README row had been truncated).

Canonical source: the value-stream-index.md PA bullet (the master index; it agreed with
the VS README in 37 of the 38 cases and with the H1 in the PA-69.1 case — majority rule).
The script rewrites:
  - every PA file H1 to `# PA-XX.Y — <canonical name>`; and
  - every VS README row name to the canonical name (and its link text/path).
Idempotent: re-running on aligned files is a no-op.

Usage:
    python3 07-methodology/fix-pa-names.py           # write changes
    python3 07-methodology/fix-pa-names.py --check   # report only, exit 1 if pending
"""
import argparse, glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(REPO, "01-model-company", "workflows")
INDEX = os.path.join(WORKFLOWS, "value-stream-index.md")

IDX_BULLET = re.compile(r"^- \*\*(PA-\d+\.\d+)\*\* \[([^\]]+)\]\(([^)]+)\) — (\d+) workflows", re.MULTILINE)
# VS README 'Process Areas' row: | [PA-XX.Y](file.md) | Name | N |
README_ROW = re.compile(r"^\| \[(PA-\d+\.\d+)\]\(([^)]+)\) \| ([^|]+?) \| (\d+) \|$", re.MULTILINE)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="report only; exit 1 if pending")
    args = ap.parse_args()

    idx_text = open(INDEX, encoding="utf-8").read()
    canonical = {m.group(1): (m.group(2), m.group(3)) for m in IDX_BULLET.finditer(idx_text)}
    if len(canonical) != 569:
        print(f"FATAL: expected 569 index PA bullets, found {len(canonical)}")
        sys.exit(2)

    total, files = 0, 0
    for vsdir in sorted(glob.glob(os.path.join(WORKFLOWS, "VS-*"))):
        readme_path = os.path.join(vsdir, "README.md")
        readme = open(readme_path, encoding="utf-8").read()
        readme_changed = False
        rows = {m.group(1): m for m in README_ROW.finditer(readme)}
        pa_files = {re.match(r"(PA-\d+\.\d+)-", os.path.basename(p)).group(1): p
                    for p in glob.glob(os.path.join(vsdir, "PA-*.md"))}
        for pid, path in sorted(pa_files.items()):
            if pid not in canonical:
                continue
            cname, clink = canonical[pid]
            want_h1 = f"# {pid} — {cname}"
            text = open(path, encoding="utf-8").read()
            h1 = text.split("\n", 1)[0]
            changed = False
            if h1 != want_h1:
                text = text.replace(h1, want_h1, 1)
                changed = True
                print(f"{'PENDING' if args.check else 'FIXED'} H1  {os.path.relpath(path, REPO)}:\n"
                      f"        - {h1}\n        + {want_h1}")
            # VS README row: link path + display name must match canonical
            m = rows.get(pid)
            if m and (m.group(2) != os.path.basename(path) or m.group(3).strip() != cname):
                new_row = f"| [{pid}]({os.path.basename(path)}) | {cname} | {m.group(4)} |"
                if not args.check:
                    readme = readme.replace(m.group(0) + "\n", new_row + "\n", 1)
                readme_changed = True
                print(f"{'PENDING' if args.check else 'FIXED'} ROW {os.path.basename(vsdir)}/README.md {pid}:\n"
                      f"        - {m.group(3).strip()!r} / link {m.group(2)!r}\n"
                      f"        + {cname!r} / link {os.path.basename(path)!r}")
            n = 1 if changed else 0
            n += 1 if (m and (m.group(2) != os.path.basename(path) or m.group(3).strip() != cname)) else 0
            if n:
                files += 1
                total += n
                if changed and not args.check:
                    open(path, "w", encoding="utf-8").write(text)
        if readme_changed and not args.check:
            open(readme_path, "w", encoding="utf-8").write(readme)

    verb = "pending" if args.check else "applied"
    print(f"\n{total} name alignment(s) {verb} across {files} location(s).")
    if args.check and total:
        sys.exit(1)


if __name__ == "__main__":
    main()
