#!/usr/bin/env python3
"""
audit-st-touchpoints.py — System-Touchpoints vocabulary & Trigger-duplication guard.

Consistency review #35 (2026-08-29) audited the two surfaces the review #34
close-out named:

  * System Touchpoints module-name consistency — the 15,988 ST bullets across
    the 569 PA files spell-check cleanly against the ST vocabulary (no
    misspellings of module names survive the review #33 house-spelling sweeps),
    and the 36 canonical modules of workflow-system-touchpoint-map.md are
    families whose subsystem names in PA prose (AP module, WMS, PIM, BI …)
    cohere. What the sweep DID find: eight rogue spelling/hyphenation variants
    of dominant house forms, since normalized (ageing → aging incl. the W995
    title/TOC-anchor/classification-register cascade; drilldown → drill-down;
    pick-up → pickup; put-away → putaway; time-stamp(ed) → timestamp(ed);
    charge-back(s) → chargeback(s); anti-counterfeiting → anti-counterfeit;
    adjectival self-serve → self-service). Forms that are TITLE-canonical are
    deliberately untouched (W258 "Omni-channel …", W1238/W1491 "Material
    Take-Off …", W3657 "… Closeout", the paired check-in/check-out noun form).
  * Trigger-field duplication across sibling workflows — every same-PA
    byte-identical Trigger pair was adjudicated: all eleven clusters are
    legitimate shared-event/shared-cadence triggers (parallel M&A due-diligence
    streams on LOI signing, annual-audit-plan children, month-close siblings,
    kickoff-triggered project streams), so the surface ships clean with the
    clusters allowlisted and any NEW same-PA duplicate an error.

Guard mode (--guard, used by validator Check 52):
  1. retired-literal — the eight normalized variants must not reappear in
     PA files or the workflow summary docs;
  2. duplicate-trigger — same-PA byte-identical (case-insensitive) Trigger
     values are errors unless the (file, trigger) pair is on the adjudicated
     allowlist below.
"""
import argparse, glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(REPO, "01-model-company", "workflows")

RETIRED_LITERALS = [
    "ageing", "Ageing",
    "drilldown", "drilldowns",
    "pick-up", "put-away", "time-stamp",
    "charge-back", "anti-counterfeiting", "self-serve",
]

# adjudicated legitimate shared-trigger clusters (file basename, lowercased
# trigger text) — parallel streams of one program / same-cycle children
TRIGGER_ALLOWLIST = {
    ("PA-130.2-transaction-due-diligence-valuation-and-deal-structuring.md",
     "loi/exclusivity"),
    ("PA-130.3-integration-carveout-divestiture-and-postmerger-performance.md",
     "post-close integration"),
    ("PA-183.3-dts-tax-incentive-compliance-and-reporting.md",
     "monthly calendar close"),
    ("PA-21.1-audit-planning-and-execution.md", "annual audit plan"),
    ("PA-21.3-specialized-audit-domains.md", "annual audit plan"),
    ("PA-33.1-annual-business-planning.md", "annual budget process (w1646)"),
    ("PA-37.1-new-store-project-planning.md", "project kickoff (w1737)"),
    ("PA-59.1-store-closure-decision-planning.md", "closure approved"),
    ("PA-60.3-fulfillment-performance-analytics.md", "monthly"),
    ("PA-60.3-fulfillment-performance-analytics.md", "quarterly"),
    ("PA-61.2-toll-route-cost.md", "monthly review"),
    ("PA-61.3-fleet-total-cost-analytics.md", "quarterly"),
    ("PA-64.3-post-season-analysis-learning.md", "post-season"),
    ("PA-69.1-typhoon-preparedness-early-warning.md",
     "pagasa signal no. 1 in store region"),
    ("PA-75.3-digital-engagement-analytics-optimization.md",
     "monthly analytics"),
    ("PA-82.2-micro-wholesale-order-fulfillment-delivery.md",
     "delivery completion"),
    ("PA-85.3-tax-credit-recovery-registry-audit.md", "monthly close"),
    ("PA-86.1-kyc-cdd-pep-sanctions-screening.md",
     "onboarding or periodic screening"),
}

TRIGGER_RE = re.compile(r"^\| \*\*Trigger\*\* \| (.+?) \|$", re.M)
WID_RE = re.compile(r"^## (W\d+[A-Z]?)\.", re.M)


def check_file(path, hits):
    text = open(path, encoding="utf-8").read()
    rel = os.path.relpath(path, REPO)
    base = os.path.basename(path)
    for lit in RETIRED_LITERALS:
        for m in re.finditer(re.escape(lit), text):
            # 'charge-back' inside 'charge-backs' is covered by the literal
            line = text[:m.start()].count("\n") + 1
            hits.append(("retired-literal", rel, line, lit))
            break  # one report per literal per file is enough for the guard
    if base.startswith("PA-"):
        seen = {}
        for m in TRIGGER_RE.finditer(text):
            wids = WID_RE.findall(text[:m.start()])
            wid = wids[-1] if wids else "?"
            key = m.group(1).strip().lower()
            if key in seen and (base, key) not in TRIGGER_ALLOWLIST:
                line = text[:m.start()].count("\n") + 1
                hits.append(("duplicate-trigger", rel, line,
                             f"{seen[key]} == {wid}: '{m.group(1).strip()[:80]}'"))
            elif key not in seen:
                seen[key] = wid


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guard", action="store_true",
                    help="exit 1 on any hit (validator mode)")
    args = ap.parse_args()
    hits = []
    files = sorted(glob.glob(os.path.join(WORKFLOWS, "VS-*", "PA-*.md")))
    files += [os.path.join(WORKFLOWS, x) for x in [
        "README.md", "value-stream-index.md", "WORKFLOW-FORMAT-GUIDE.md",
        "workflow-criticality-classification.md",
        "workflow-criticality-proposed.md", "workflow-dependency-map.md",
        "workflow-system-touchpoint-map.md", "workflow-gap-analysis.md"]]
    files = [f for f in files if os.path.exists(f)]
    for f in files:
        check_file(f, hits)
    for kind, rel, line, detail in hits:
        print(f"{kind}: {rel}:{line}: {detail}")
    print(f"audit-st-touchpoints: {len(hits)} hit(s) across {len(files)} files")
    if args.guard:
        sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
