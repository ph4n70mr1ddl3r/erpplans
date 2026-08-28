#!/usr/bin/env python3
"""
audit-operational-controls.py — Controls-section operational-prose variant guard.

Consistency review #39 (2026-08-29) audited the three surfaces named in the
review #38 close-out:

  * Controls-section operational-control prose — the 5,153 'operational:'
    sentences cluster into the intentional add-pa-controls.py templates
    ('<Role> review and approval gate' ×~1,100 across 300+ roles, plus the two
    Check-21-known boilerplate strings). The variant forms the review
    normalized (~20 spots): hyphenated 'review-and-approval gate' → 'review
    and approval gate'; 'review & approval' → 'review and approval';
    'review and approvals'; 'VP for Merchandising/Store Operations' → the
    house 'VP Merchandising'/'VP Store Operations'; the redundant '(CSR)'
    gloss and '(HQ)' qualifiers inside gate sentences. Role look-alikes in the
    near-miss tail (CEO vs CMO, AP vs AR Supervisor…) are genuinely distinct
    roles; the three 'Marketing — <role>' department-scoped composites are
    kept as informative.
  * System Touchpoints module-family naming vs the 36-module register — the
    semantic mapping coheres (subsystem names by design, per the review #35
    adjudication); the only hyphenated family-name hits inside ST sections
    ('master-data-quality monitoring', 'loss-prevention CCTV') are
    grammatically correct compound modifiers, not inconsistencies. Clean.
  * cross-PA 'links to VS-x' citation density — 44,041 citations across all
    569 PAs, median 57 per PA, minimum 2, maximum 259, zero PAs without
    cross-VS citations. Healthy; nothing repaired.

Guard mode (--guard, validator Check 56): the retired variant literals below
must not reappear in PA files.
"""
import argparse, glob, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(REPO, "01-model-company", "workflows")

RETIRED_LITERALS = [
    "review-and-approval gate",
    "review & approval",
    "review and approvals gate",
    "VP for Merchandising review and approval gate",
    "VP for Store Operations review and approval gate",
    "Customer Service Representative (CSR) review and approval gate",
    "(HQ) review and approval gate",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guard", action="store_true",
                    help="exit 1 on any retired operational-prose literal")
    args = ap.parse_args()
    hits = []
    files = sorted(glob.glob(os.path.join(WORKFLOWS, "VS-*", "PA-*.md")))
    for f in files:
        text = open(f, encoding="utf-8").read()
        for lit in RETIRED_LITERALS:
            if lit in text:
                line = text[:text.find(lit)].count("\n") + 1
                hits.append((os.path.relpath(f, REPO), line, lit))
    for rel, line, lit in hits:
        print(f"retired-literal: {rel}:{line}: {lit}")
    print(f"audit-operational-controls: {len(hits)} hit(s) across {len(files)} PA files")
    if args.guard:
        sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
