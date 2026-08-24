#!/usr/bin/env python3
"""
fix-vs-wrefs.py — One-time repairer for workflow references written in the VS
namespace inside workflow-catalog files (companion to validator Check 35).

Consistency review #21 found that no check validated `VS-<n>` tokens themselves:
Checks 19/20 resolve link TARGETS, Checks 6/7/33 validate only `W…` tokens, so a
citation like "(links to VS-469 DTI)" — where 469 is not a value stream at all but
is exactly the number of workflow W469 (Customer Complaint DTI Escalation) — shipped
silently across the catalog. Twenty-four distinct phantom `VS-<n>` numbers (87
instances in 25 PA files) were found; every target was verified to exist and to
match its surrounding gloss before inclusion:

  VS-228  -> W228   Sales Commission Calculation (Trade & Project Sales)
                    ("trade commissions", "incentives")
  VS-245  -> W245   Vendor Performance Chargebacks & Penalties Management
                    ("compliance chargebacks")
  VS-254  -> W254   Location Master Lifecycle & Hierarchy Management
                    ("location (master)")
  VS-256  -> W256   Enterprise Document Retention & Archiving Policy
                    ("Document Registry", "document archiving")
  VS-277  -> W277   Freight Bill Audit & Payment (FBAP) Reconciliation
                    ("Logistics Finance")
  VS-279  -> W279   Product Substitution Rules & Governance
                    ("substitute SKU mapping / substitute master")
  VS-287  -> W287   Vendor Master Data Governance & Deduplication
                    ("vendor master")
  VS-289  -> W289   Pricing Master Governance (Base Prices & Matrices)
                    ("pricing master")
  VS-292  -> W292   Employee Master Data Governance & Cross-Entity Lifecycle
                    ("employee master") — except the special case below
  VS-295  -> W295   Payment Terms & Settlement Rule Master Governance
                    ("payment-terms master / term-master")
  VS-330  -> W330   In-Store Emergency Response Protocol
                    ("incident protocol", paired with W471)
  VS-337  -> W337   Payroll & Statutory Compliance Audit
  VS-399  -> W399   Fixed Asset Master Data Governance ("asset register")
  VS-400  -> W400   Equipment & Asset Maintenance (EAM) Master Governance
                    ("asset/PM register")
  VS-402  -> W402   Contract & Agreement Master Governance ("contract master")
  VS-469  -> W469   Customer Complaint DTI Escalation & Consumer Adjudication
                    Management ("DTI escalation", "Consumer Act complaint")
  VS-908  -> W908   Store-Level Barangay & Local Fiesta Merchandising Calendar
                    Management
  VS-1099 -> W1099  Store-Level Vendor-Sponsored Product Training Academy &
                    Staff Certification Program ("vendor training")
  VS-1250 -> W1250  Store Foot Traffic Analytics, Conversion Rate Monitoring &
                    Sales Floor Productivity Insights ("footfall")
  VS-1493 -> W1493  Store-Level Contractor Lounge & Trade Amenities Management,
                    Satisfaction Survey & Retention ("contractor/pro experience")
  VS-1511 -> W1511  Store-Level Community Engagement, Barangay Relations &
                    Local Partnership Management
  VS-3796 -> W3796  Import Vendor Negotiation, FOB Pricing & Cost-Reduction
                    Management ("FOB cost reduction flows to margin")
  VS-4398 -> W4398  Customer Safety Signage, Wayfinding & Barrier Management
                    ("safety/wayfinding")

  Special case (context-specific target, applied before the generic map):
    PA-106.2 "VS-292 service/non-stock master" -> W296 Service & Non-Stock Item
    Master Governance — the gloss names W296, not the employee master W292.

Idempotent: re-running on repaired files is a no-op. --check reports only and exits
non-zero when pending repairs remain.

Usage:
    python3 07-methodology/fix-vs-wrefs.py --dry-run
    python3 07-methodology/fix-vs-wrefs.py
"""
import argparse
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(REPO, "01-model-company", "workflows")

# Context-specific repair applied first (old text is unique within its file).
SPECIAL_CASES = [
    ("VS-106-commodity-input-cost-risk-management/"
     "PA-106.2-procurement-hedging-forward-buying-and-indexed-pricing.md",
     "VS-292 service/non-stock master", "W296 service/non-stock master"),
]

# Generic namespace repair: every phantom `VS-<n>` token maps to workflow `W<n>`.
# No active value stream carries any of these numbers, so the token itself is
# unambiguous; each target was gloss-verified (see module docstring).
GENERIC = {
    "VS-228": "W228", "VS-245": "W245", "VS-254": "W254", "VS-256": "W256",
    "VS-277": "W277", "VS-279": "W279", "VS-287": "W287", "VS-289": "W289",
    "VS-292": "W292", "VS-295": "W295", "VS-330": "W330", "VS-337": "W337",
    "VS-399": "W399", "VS-400": "W400", "VS-402": "W402", "VS-469": "W469",
    "VS-908": "W908", "VS-1099": "W1099", "VS-1250": "W1250",
    "VS-1493": "W1493", "VS-1511": "W1511", "VS-3796": "W3796",
    "VS-4398": "W4398", "VS-5493": "W5493",
}

# Workflow ids that must exist as '## W<id>.' / '### W<id>.' headers (repair targets).
W_TARGETS = sorted(set(GENERIC.values()) | {"W296"})


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


def catalog_files():
    out = []
    for vs in sorted(os.listdir(WORKFLOWS)):
        d = os.path.join(WORKFLOWS, vs)
        if not vs.startswith("VS-") or not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if f.endswith(".md"):
                out.append(os.path.join(vs, f))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="report only; exit 1 if changes pending")
    ap.add_argument("--check", action="store_true", help="alias for --dry-run")
    args = ap.parse_args()
    dry = args.dry_run or args.check

    wids = defined_workflow_ids()
    missing_w = [w for w in W_TARGETS if w not in wids]
    if missing_w:
        print(f"ABORT: repair targets not defined on disk: {missing_w}", file=sys.stderr)
        sys.exit(2)

    pending = 0

    # Pass 1: context-specific repairs (exact-text).
    for rel, old, new in SPECIAL_CASES:
        path = os.path.join(WORKFLOWS, rel)
        text = open(path, encoding="utf-8").read()
        n = text.count(old)
        if n == 0:
            if new not in text:
                print(f"WARN: special-case pattern not found (already repaired?): {rel}: {old}")
            continue
        pending += n
        print(f"{'WOULD FIX' if dry else 'FIX'} {rel}: '{old}' -> '{new}' (x{n})")
        if not dry:
            open(path, "w", encoding="utf-8").write(text.replace(old, new))

    # Pass 2: generic token remap across the catalog.
    tok_re = re.compile(r"\b(" + "|".join(sorted(GENERIC, key=len, reverse=True)) + r")\b")
    for rel in catalog_files():
        path = os.path.join(WORKFLOWS, rel)
        text = open(path, encoding="utf-8").read()
        hits = tok_re.findall(text)
        if not hits:
            continue
        counts = {}
        for h in hits:
            counts[h] = counts.get(h, 0) + 1
        pending += len(hits)
        detail = ", ".join(f"{k}->{GENERIC[k]} x{v}" for k, v in sorted(counts.items()))
        print(f"{'WOULD FIX' if dry else 'FIX'} {rel}: {detail}")
        if not dry:
            open(path, "w", encoding="utf-8").write(tok_re.sub(lambda m: GENERIC[m.group(0)], text))

    print(f"\n{pending} repair(s) {'pending' if dry else 'applied'}.")
    if dry and pending:
        sys.exit(1)


if __name__ == "__main__":
    main()
