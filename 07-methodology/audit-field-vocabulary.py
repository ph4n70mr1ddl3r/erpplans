#!/usr/bin/env python3
"""
audit-field-vocabulary.py — Pain-Points risk-label, Frequency-cadence, and
Owner-role vocabulary guard.

Consistency review #37 (2026-08-29) audited the three surfaces named in the
review #36 close-out:

  * Pain Points risk taxonomy — the 4,836 distinct bolded **X risk**: labels
    (6,959 bullets) cluster cleanly into domain-specific labels; sixteen
    near-miss variant pairs were adjudicated and thirteen normalized
    (Blindspot → Blind-spot; Cannibalisation → Cannibalization; the hybrid
    Cannibalization-miss → Missed-cannibalization; Cost-leak → Cost-leakage;
    Metrics-gaming → Metric-gaming; Operations → Operational;
    Re-occurrence → Recurrence; Record-gap → Records-gap; Reputation →
    Reputational; the unhyphenated "Scope creep risk" → "Scope-creep risk";
    and three capitalized 'Risk' tails → lowercase). Distinct concepts were
    kept (Capability-shortfall ≠ Capacity-shortfall; CDR-reconciliation;
    Hidden-PL-cost; Reputational/ESG; Tax-mis-classification).
  * Frequency cadence vocabulary — 3,117 distinct leading terms spell-check
    clean (no continous/quaterly/montly-class misspellings exist); the only
    variant was 17 unhyphenated "ad hoc" → "ad-hoc" (dominant 320×).
  * Owner-field role vocabulary vs the profile — top roles cohere with §13.1
    and §3.3 (Category Manager 72, Pricing Analyst 32, Merchandise Planner
    28…); the org-chart spelling is HSE, so 'EHS Manager' → 'HSE Manager',
    and the two PA-07.1 store-opening rows now read Compliance Officer in
    both role cell and prose. The bare 'Compliance Manager' title was
    adjudicated a plausible Legal & Compliance team title and kept
    (qualified forms — Product/EPR/Trade/Tax/HR Compliance Manager — are
    distinct roles; 'CSR Manager' in PA-14.3 is Corporate Social
    Responsibility, not customer service).

Guard mode (--guard, validator Check 54): none of the retired literals below
may reappear in PA files or the workflow summary docs.
"""
import argparse, glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(REPO, "01-model-company", "workflows")

RETIRED_LITERALS = [
    "**Blindspot risk**", "**Cannibalisation risk**",
    "**Cannibalization-miss risk**", "**Cost-leak risk**",
    "**Metrics-gaming risk**", "**Operations risk**",
    "**Re-occurrence risk**", "**Record-gap risk**",
    "**Reputation risk**", "**Scope creep risk**",
    "**Audit Risk**", "**Closure Risk**", "**Regularization Risk**",
    "EHS Manager",
]


def check_file(path, hits):
    text = open(path, encoding="utf-8").read()
    rel = os.path.relpath(path, REPO)
    for lit in RETIRED_LITERALS:
        if lit in text:
            line = text[:text.find(lit)].count("\n") + 1
            hits.append(("retired-literal", rel, line, lit))
    for m in re.finditer(r"\bad hoc\b", text):
        line = text[:m.start()].count("\n") + 1
        hits.append(("cadence-variant", rel, line, "ad hoc"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guard", action="store_true",
                    help="exit 1 on any retired vocabulary literal")
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
    print(f"audit-field-vocabulary: {len(hits)} hit(s) across {len(files)} files")
    if args.guard:
        sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
