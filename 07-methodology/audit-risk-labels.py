#!/usr/bin/env python3
"""
audit-risk-labels.py — risk-label punctuation & mitigation-clause structure guard.

Consistency review #40 (2026-08-29) audited the three surfaces named in the
review #39 close-out:

  * Pain Points mitigation-clause structure — of the 7,066 risk bullets,
    95.8% carry the canonical 'mitigated by …' clause, 31 more carry explicit
    alternative mitigation phrasings, and 265 (3.7%) state the risk without a
    mitigation clause (their mitigations live in the workflow's Controls
    section). That residue is an authored-content enrichment backlog per the
    format guide's 'refine freely during per-workflow review' note, not a
    mechanical defect, and is documented in the CHANGELOG rather than
    fabricated. The structural defect repaired: 50 risk labels used the
    em-dash form '**X risk** — description' instead of the colon form used by
    the 6,800+ majority ('**X risk**: description').
  * Trigger-field prose richness — 85 Trigger values outside the Check-52
    allowlisted files are ultra-short cadence phrases ('Monthly reporting',
    'Quarterly analysis'); thin but honest, single-workflow (no duplication),
    and an enrichment backlog rather than a defect.
  * WORKFLOW-FORMAT-GUIDE example inventory — the ✅/❌ examples' anchors all
    resolve against current state: W2599 exists (VS-73.1), VS-88 is an active
    value stream, and the '~72,000 receipts/yr → ~6,000 discrepancies/yr'
    example matches the canonical DC-only goods-receipt volume (6,000/month).

Guard mode (--guard, validator Check 57): the em-dash risk-label form must not
reappear in PA files.
"""
import argparse, glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(REPO, "01-model-company", "workflows")

EMDASH_RE = re.compile(r"\*\*[^*]*[Rr]isk\*\*\s*—")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guard", action="store_true",
                    help="exit 1 on any em-dash risk label")
    args = ap.parse_args()
    hits = []
    files = sorted(glob.glob(os.path.join(WORKFLOWS, "VS-*", "PA-*.md")))
    for f in files:
        text = open(f, encoding="utf-8").read()
        for m in EMDASH_RE.finditer(text):
            line = text[:m.start()].count("\n") + 1
            hits.append((os.path.relpath(f, REPO), line, m.group(0)))
    for rel, line, lit in hits:
        print(f"em-dash-risk-label: {rel}:{line}: {lit}")
    print(f"audit-risk-labels: {len(hits)} hit(s) across {len(files)} PA files")
    if args.guard:
        sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
