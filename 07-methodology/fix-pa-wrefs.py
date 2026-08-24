#!/usr/bin/env python3
"""
fix-pa-wrefs.py — One-time repairer for dangling & misdirected cross-references
inside PA-file workflow bodies (companion to validator Check 33).

Consistency review #20 found that Checks 6/7 validate workflow references only in the
four cross-reference docs (matrix, controls matrix, dependency map, touchpoint map) —
never inside the 569 PA files themselves. Eighteen dangling tokens survived there,
plus two references that resolve but point at the wrong workflow, plus six hand-written
"links to VS-X" bullets citing CTL ids whose register rows belong to unrelated process
areas. All repaired via the explicit remap table below (each target verified to exist):

  Dangling workflow references (token -> replacement, occurrences):
    W01    -> W1        (3x) zero-padded citation of the PA-01.1 assortment workflow
    W03.4  -> VS-03.4   (4x) PA reference written in the W namespace (vendor portal)
    W03.1  -> VS-03.1   (1x) same, vendor sourcing
    W03.2  -> VS-03.2   (1x) same, PO cycle
    W03    -> W698      (1x) "request updated SDS from vendor" -> the SDS Lifecycle
                        Management workflow (VS-24 PA-24.3), not receiving W3
    W05.2  -> W22       (2x) "(Stock Transfers)" gloss matches W22 exactly
    W413   -> W14       (4x) IC-elimination citations -> W14, whose steps 8-9 own
                        elimination entries and consolidation verification
    W1593  -> W706      (1x) phantom id -> VS-03's Supplier Performance Scorecard & QBR
    W6796  -> W796      (1x) digit-insertion typo of the same file's DC Workforce
                        Scheduling, Labor Planning & Productivity Tracking workflow

  Resolves-but-misdirected workflow reference:
    W2347  -> W2469     (1x) cited as "VS-67 ... vendor scorecard" but W2347 is
                        VS-62's Vendor-Funded Display Program; the cross-functional
                        scorecard feed workflow is W2469 (VS-67 PA-67.2)

  Misdirected CTL citations in hand-written "links to VS-X" bullets
  (ctl id -> correct register row, occurrences):
    CTL-357 -> CTL-349  (2x) "board governance - links to VS-36" -> PA-36.1 control
    CTL-357 -> CTL-304  (2x) "board governance & MCG compliance - links to VS-21"
                        -> PA-21.1 audit control (Board Audit Committee reporting)
    CTL-335 -> CTL-304  (1x) "major-capex/post-implementation audit - links to VS-21"
    CTL-689 -> CTL-614  (1x) "AI/ML governance - links to VS-128" -> PA-128.1 control

Idempotent: re-running on repaired files is a no-op. --check reports only and exits
non-zero when pending repairs remain.

Usage:
    python3 07-methodology/fix-pa-wrefs.py --dry-run
    python3 07-methodology/fix-pa-wrefs.py
"""
import argparse
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(REPO, "01-model-company", "workflows")
MATRIX = os.path.join(REPO, "01-model-company", "internal-controls-matrix.md")

# (file, old_text, new_text) — old_text strings are unique within their file.
REPAIRS = [
    # --- dangling W references -------------------------------------------------
    ("VS-01-merchandise-strategy/PA-01.1-assortment-planning-and-product-lifecycle.md",
     "W220 (SLOB), W01 (assortment planning)", "W220 (SLOB), W1 (assortment planning)"),
    ("VS-28-data-analytics-bi/PA-28.3-advanced-analytics.md",
     "bundle creation per W01", "bundle creation per W1"),
    ("VS-28-data-analytics-bi/PA-28.3-advanced-analytics.md",
     "Integration with W01 (assortment planning)", "Integration with W1 (assortment planning)"),
    ("VS-30-innovation-digital/PA-30.3-document-and-knowledge-management.md",
     "part of vendor portal per W03.4", "part of vendor portal per VS-03.4"),
    ("VS-30-innovation-digital/PA-30.3-document-and-knowledge-management.md",
     "W03.4 (vendor portal)", "VS-03.4 (vendor portal)"),
    ("VS-03-vendor-management/PA-03.3-vendor-performance-and-contracts.md",
     "vendor portal enhancements per W03.4", "vendor portal enhancements per VS-03.4"),
    ("VS-03-vendor-management/PA-03.3-vendor-performance-and-contracts.md",
     "shared via portal per W03.4", "shared via portal per VS-03.4"),
    ("VS-03-vendor-management/PA-03.3-vendor-performance-and-contracts.md",
     "W03.4 (vendor portal), W03.1 (vendor sourcing), W03.2 (PO cycle)",
     "VS-03.4 (vendor portal), VS-03.1 (vendor sourcing), VS-03.2 (PO cycle)"),
    ("VS-04-dc-warehouse/PA-04.3-dc-operations-management.md",
     "request updated SDS from vendor per W03", "request updated SDS from vendor per W698"),
    ("VS-04-dc-warehouse/PA-04.3-dc-operations-management.md",
     "per W6796 (DC Workforce Productivity Tracking)", "per W796 (DC Workforce Productivity Tracking)"),
    ("VS-37-store-opening-commissioning/PA-37.3-grand-opening-post-opening.md",
     "initiate transfer per W05.2 (Stock Transfers)", "initiate transfer per W22 (Stock Transfers)"),
    ("VS-37-store-opening-commissioning/PA-37.3-grand-opening-post-opening.md",
     "Inter-store transfer initiation per W05.2 for excess stock",
     "Inter-store transfer initiation per W22 for excess stock"),
    ("VS-17-record-to-report/PA-17.2-consolidation-and-intercompany.md",
     "IC elimination entries for consolidated reporting per W413",
     "IC elimination entries for consolidated reporting per W14"),
    ("VS-17-record-to-report/PA-17.2-consolidation-and-intercompany.md",
     "eliminated in consolidated trial balance per W413",
     "eliminated in consolidated trial balance per W14"),
    ("VS-17-record-to-report/PA-17.2-consolidation-and-intercompany.md",
     "IC elimination automation (W413)", "IC elimination automation (W14)"),
    ("VS-17-record-to-report/PA-17.2-consolidation-and-intercompany.md",
     "Consolidated reporting with IC elimination (W413)", "Consolidated reporting with IC elimination (W14)"),
    # --- resolves-but-misdirected W reference ----------------------------------
    ("VS-137-product-information-management-and-digital-asset-management/"
     "PA-137.1-product-information-model-attribute-taxonomy-and-governance.md",
     "links to VS-03 scorecard W1593", "links to VS-03 scorecard W706"),
    ("VS-137-product-information-management-and-digital-asset-management/"
     "PA-137.1-product-information-model-attribute-taxonomy-and-governance.md",
     "vendor scorecard (VS-67 W2347/VS-03)", "vendor scorecard (VS-67 W2469/VS-03)"),
    # --- misdirected hand-written CTL citations --------------------------------
    ("VS-59-store-closure-decommissioning/PA-59.1-store-closure-decision-planning.md",
     "CTL-357 (board governance — links to VS-36)", "CTL-349 (board governance — links to VS-36)"),
    ("VS-59-store-closure-decommissioning/PA-59.1-store-closure-decision-planning.md",
     "CTL-335 (major-capex/post-implementation audit — links to VS-21)",
     "CTL-304 (major-capex/post-implementation audit — links to VS-21)"),
    ("VS-59-store-closure-decommissioning/PA-59.3-staff-redeployment-post-closure.md",
     "CTL-357 (board governance — links to VS-36)", "CTL-349 (board governance — links to VS-36)"),
    ("VS-72-cross-entity-shared-services/PA-72.3-shared-services-performance-analytics.md",
     "CTL-357 (board governance & MCG compliance — links to VS-21)",
     "CTL-304 (board governance & MCG compliance — links to VS-21)"),
    ("VS-76-multi-region-lgu-compliance/PA-76.3-lgu-relationship-regulatory-analytics.md",
     "CTL-357 (board governance & MCG compliance audit — links to VS-21)",
     "CTL-304 (board governance & MCG compliance audit — links to VS-21)"),
    ("VS-60-omnichannel-order-routing/PA-60.3-fulfillment-performance-analytics.md",
     "CTL-689 (AI/ML governance — links to VS-128)", "CTL-614 (AI/ML governance — links to VS-128)"),
]

# Workflow ids that must exist as '## W<id>.' / '### W<id>.' headers (repair targets).
W_TARGETS = ["W1", "W22", "W14", "W698", "W706", "W796", "W2469"]
# CTL ids that must exist as register rows (repair targets).
CTL_TARGETS = ["CTL-349", "CTL-304", "CTL-614"]


def defined_workflow_ids():
    ids = set()
    for vs in sorted(os.listdir(WORKFLOWS)):
        d = os.path.join(WORKFLOWS, vs)
        if not vs.startswith("VS-") or not os.path.isdir(d):
            continue
        for f in os.listdir(d):
            if f.startswith("PA-") and f.endswith(".md"):
                for line in open(os.path.join(d, f), encoding="utf-8"):
                    m = re.match(r"^#{2,3} (W\d+[A-Z]?)\.", line)
                    if m:
                        ids.add(m.group(1))
    return ids


def defined_ctl_ids():
    ids = set(re.findall(r"\b(CTL-\d{2,3})\b", open(MATRIX, encoding="utf-8").read()))
    return ids


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="report only; exit 1 if changes pending")
    ap.add_argument("--check", action="store_true", help="alias for --dry-run")
    args = ap.parse_args()
    dry = args.dry_run or args.check

    wids = defined_workflow_ids()
    missing_w = [w for w in W_TARGETS if w not in wids]
    ctls = defined_ctl_ids()
    missing_ctl = [c for c in CTL_TARGETS if c not in ctls]
    if missing_w or missing_ctl:
        print(f"ABORT: repair targets not defined on disk: {missing_w} {missing_ctl}", file=sys.stderr)
        sys.exit(2)

    pending = 0
    for rel, old, new in REPAIRS:
        path = os.path.join(WORKFLOWS, rel)
        text = open(path, encoding="utf-8").read()
        n = text.count(old)
        if n == 0:
            if new not in text:
                print(f"WARN: pattern not found (already repaired?): {rel}: {old[:60]}")
            continue
        if text.count(new) and n > 1:
            print(f"WARN: ambiguous repair skipped: {rel}: {old[:60]} (x{n})")
            continue
        pending += n
        print(f"{'WOULD FIX' if dry else 'FIX'} {rel}: '{old[:58]}' -> '{new[:58]}' (x{n})")
        if not dry:
            open(path, "w", encoding="utf-8").write(text.replace(old, new))

    print(f"\n{pending} repair(s) {'pending' if dry else 'applied'}.")
    if dry and pending:
        sys.exit(1)


if __name__ == "__main__":
    main()
