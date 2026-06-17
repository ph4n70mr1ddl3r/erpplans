#!/usr/bin/env python3
"""classify-workflows.py — Keyword-driven criticality proposal for unclassified workflows.

Companion to `validate-repo.sh`. The authoritative criticality register
(`01-model-company/workflows/workflow-criticality-classification.md`) is hand-maintained.
This script proposes a Tier 1 / Tier 2 / Tier 3 assignment for every workflow that is NOT
already in that register, using conservative keyword rules over the workflow name, its PA
file title, and its value-stream family. Output is written to a SEPARATE file
(`workflow-criticality-proposed.md`) so the confirmed register stays authoritative and the
proposal is clearly reviewable / reversible.

Methodology (see `workflow-criticality-classification.md` "Classification Rules"):
  - Tier 1 = revenue-critical / core transactional / legal-compliance / hard dependency
  - Tier 2 = standard support / cost control / governance / soft dependency  (SAFE DEFAULT)
  - Tier 3 = advanced analytics / AI / optimization / automation / enhancement only

Rules are evaluated in priority order: Tier 1 first (specific statutory/core terms), then
Tier 3 (specific advanced-tech terms), then Tier 2 (default). Family overrides adjust
whole value streams where the family context is decisive (e.g. VS-79 BIR tax → mostly
Tier 1; VS-128 AI *governance* → Tier 1/2, not Tier 3). Every assignment is a proposal
pending human review — the tier boundaries are deliberately conservative to minimise
false promotions.

Usage:
    python3 07-methodology/classify-workflows.py [--write]
        Without --write, prints a summary only. With --write, (re)generates
        01-model-company/workflows/workflow-criticality-proposed.md.
"""
import argparse, glob, os, re, sys
from collections import defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WF   = os.path.join(REPO, "01-model-company", "workflows")
CC   = os.path.join(WF, "workflow-criticality-classification.md")
OUT  = os.path.join(WF, "workflow-criticality-proposed.md")

# ----------------------------------------------------------------------------
# Tier 1 — high-confidence statutory / core-transactional / hard-dependency
# ----------------------------------------------------------------------------
T1_PATTERNS = [
    # Statutory & tax
    r"\bbir\b", r"efps", r"e-invoic", r"\beis\b", r"electronic invoic", r"withholding",
    r"\bvat\b", r"tax filing", r"tax remitt", r"statutory", r"alphalist", r"tax return",
    r"tax cred", r"tax reconcil", r"tax audit", r"corporate income tax", r"input tax",
    r"output tax", r"book of accounts", r"2307", r"creditable withholding",
    # AML / sanctions / ABC
    r"\baml\b", r"\bkyc\b", r"\bkyb\b", r"sanctions", r"\bstr\b", r"\bsar\b",
    r"suspicious transaction", r"beneficial owner", r"\bpep\b", r"politically exposed",
    r"anti-financial", r"anti-corrupt", r"anti-bribery", r"bribery",
    # Data privacy statutory
    r"breach notif", r"data breach", r"\bdsar\b", r"data subject access", r"data subject request",
    r"npc notif", r"72-hour",
    # Product recall / stop-sale
    r"product recall", r"stop-sale", r"stop sale", r"market withdrawal", r"recall notif",
    r"recall execution", r"corrective action", r"safety recall",
    # Regulatory permits / licenses / registration (operational, go-live blocking)
    r"license to operate", r"\blto\b", r"business permit", r"permit renewal", r"permit to operate",
    r"branch registration", r"cas registration", r"accreditation", r"fire safety inspection",
    r"fsic", r"height clearance", r"sanitary permit", r"health permit",
    # Payment / settlement / cash integrity
    r"settlement", r"reconcil", r"cash office", r"bank deposit", r"deposit preparation",
    r"acquirer settlement", r"payment settlement", r"bank reconcil", r"cash reconcil",
    r"card terminal", r"tender reconcil", r"payment reconcil", r"vault", r"cash-in-transit",
    r"armored",
    # Core finance ops
    r"invoice process", r"\bap\b", r"accounts payable", r"3-way match", r"vendor invoice",
    r"vendor payment", r"\bar\b", r"accounts receivable", r"credit limit", r"dunning",
    r"collection", r"month-end close", r"year-end close", r"financial close", r"gl posting",
    r"general ledger", r"intercompany", r"consolidat", r"product costing", r"landed cost",
    # Payroll / labor statutory
    r"payroll", r"garnishment", r"\bsss\b", r"philhealth", r"pag-ibig", r"13th month",
    r"thirteenth month", r"final pay", r"separation pay", r"wage",
    # POS mandatory compliance
    r"senior citizen", r"\bpwd\b", r"solo parent", r"mandatory discount", r"vat-exempt",
    r"price freeze", r"emergency price",
    # Core inventory / warehouse / logistics
    r"warehouse receiving", r"\breceipt\b", r"goods receipt", r"putaway", r"replenish",
    r"\bpick\b", r"\bpack\b", r"dispatch", r"outbound", r"physical inventory", r"cycle count",
    r"inventory adjust", r"stock transfer", r"inter-dc", r"store-to-store",
    # Core procurement
    r"purchase order", r"\bpo\b cycle", r"vendor onboard", r"special order", r"auto-replenish",
    r"\bpo\b approval",
    # Core POS / selling
    r"\bpos\b", r"checkout", r"transaction process", r"in-store sell", r"\btilt\b",
    r"cash tender", r"refund process", r"void process", r"shift handover", r"store open",
    r"store clos", r"end-of-day", r"end of day", r"offline pos", r"z-report",
    # Core ecommerce fulfillment
    r"bopis", r"home delivery", r"order fulfill", r"order rout", r"click.?and.?collect",
    r"ship.?from.?store", r"drop.?ship", r"smart locker",
    # Import / customs core
    r"\bcustoms\b", r"brokerage", r"port operation", r"container", r"\bbl\b", r"bill of lading",
    r"import clearance", r"duty deferr", r"bonded warehouse",
    # Safety / emergency / BCP
    r"safety incident", r"emergency response", r"evacuat", r"spill response", r"fire response",
    r"incident report", r"incident management", r"crisis response", r"business continuity",
    r"disaster recovery", r"failover", r"\bbcp\b", r"\bdr\b", r"hot site", r"cold site",
    # Core supply chain
    r"demand forecast", r"s&op", r"supply plan", r"inventory plan",
    # Quality
    r"incoming quality", r"quality inspection", r"quality control",
    # Foundational master data (core entities)
    r"item master", r"customer master", r"vendor master", r"location master", r"financial master",
    r"\bcoa\b", r"cost center", r"pricing master", r"barcode", r"\bgtin\b", r"unit of measure",
    r"\buom\b", r"fiscal calendar", r"posting period", r"bank master",
    # Pricing execution
    r"price change execution", r"regular price change", r"price execution",
]

# ----------------------------------------------------------------------------
# Tier 3 — high-confidence advanced analytics / AI / optimization / automation
# ----------------------------------------------------------------------------
T3_PATTERNS = [
    r"\bai[-/ ]?ml\b", r"\bml\b model", r"machine learning", r"deep learning",
    r"predictive analytic", r"prescriptive", r"optimization", r"optimisation",
    r"\brpa\b", r"robotic process", r"computer vision", r"natural language",
    r"telematics", r"\biot\b", r"sensor network", r"predictive maintenance",
    r"3d render", r"3d design", r"augmented reality", r"\bar\b experience", r"virtual reality",
    r"digital twin", r"shelf monitor", r"autonomous", r"smart safe",
    r"innovation", r"proof of concept", r"\bpoc\b", r"emerging tech", r"emerging technology",
    r"retail media", r"carbon offset", r"ghg emissions", r"scope [123]", r"decarboniz",
    r"sustainability report", r"esg report", r"circular economy", r"life.?cycle assessment",
    r"\blca\b", r"social media", r"influencer", r"referral program", r"brand ambassador",
    r"benchmark", r"maturity model", r"maturity assessment", r"advanced analytic",
]

# Value-stream family overrides. (vsnum_min, vsnum_max) -> tier, applied ONLY when no
# name keyword matched, to nudge whole families that are contextually decisive.
FAMILY_DEFAULTS = {
    (79, 79): 1,   # VS-79 Tax Management & BIR Statutory Reporting
    (85, 85): 1,   # VS-85 Mandatory Discount & Tax Credit Recovery
    (89, 89): 1,   # VS-89 Product Recall & Safety Corrective Action
    (91, 91): 1,   # VS-91 Consumer Data Privacy & Data Protection (statutory core)
    (114, 114): 1, # VS-114 Dangerous Goods / Hazmat transport compliance
    (117, 117): 1, # VS-117 DTI-BPS Product Standards / PS Mark / ICC compliance
    (118, 118): 1, # VS-118 Revenue Assurance & Pricing Integrity (revenue leakage)
    (125, 125): 1, # VS-125 Cross-Channel Fraud Management (revenue/crime)
    # Default-to-Tier-2 families are left to the global default (no entry needed).
}

# Workflows in VS-128 (AI Governance) and VS-30 (Innovation) should NOT be blanket-Tier-3:
# governance/policy = Tier 1, platform engineering = Tier 2. Leave to name rules + default.
SPECIAL_VS = {128: "ai-gov", 30: "innovation", 28: "analytics", 25: "esg"}


def family_tier(vsnum):
    for (lo, hi), t in FAMILY_DEFAULTS.items():
        if lo <= vsnum <= hi:
            return t
    return None


def classify(name, vsnum, pa_title):
    # Classify on the workflow NAME only. The PA filename/title is deliberately NOT
    # included: it is a broad category label (e.g. '...-settlement') whose keywords
    # would leak into every workflow in that PA and produce false Tier-1 matches.
    blob = name.lower()
    # VS-128 AI governance: regulatory/risk framework = Tier 1; ops/analytics = Tier 2.
    if vsnum == 128:
        if re.search(r"govern|policy|risk|framework|registry|inventory|oversight|compliance|"
                     r"fairness|explainab|privacy|safety|audit|approval|accountab|three lines",
                     blob):
            return 1
        return 2
    # Tier 1 explicit
    for pat in T1_PATTERNS:
        if re.search(pat, blob):
            return 1
    # Tier 3 explicit
    for pat in T3_PATTERNS:
        if re.search(pat, blob):
            return 3
    # Family default
    ft = family_tier(vsnum)
    if ft is not None:
        return ft
    # Safe default
    return 2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    # Confirmed/classified set
    cc = open(CC, encoding="utf-8").read()
    classified = set(re.findall(r"^\| (W\d+[A-Z]?) \|", cc, re.M))

    # VS family name lookup
    vs_name = {}
    idx = open(os.path.join(WF, "value-stream-index.md"), encoding="utf-8").read()
    for m in re.finditer(r"\[VS-(\d+)\]\([^)]*\)\s*\|\s*(.+?)\s*\|", idx):
        vs_name[int(m.group(1))] = m.group(2)

    # Walk PA files
    items = []  # (wnum, name, vsnum, pa)
    for pa in sorted(glob.glob(os.path.join(WF, "VS-*", "PA-*.md"))):
        vs_slug = os.path.basename(os.path.dirname(pa))
        mvsn = re.match(r"VS-(\d+)-", vs_slug)
        vsnum = int(mvsn.group(1)) if mvsn else 0
        txt = open(pa, encoding="utf-8").read()
        for m in re.finditer(r"^## (W\d+[A-Z]?)\.\s*(.+?)$", txt, re.M):
            wnum, name = m.group(1), m.group(2).strip()
            if wnum in classified:
                continue
            pa_title = os.path.basename(pa)
            tier = classify(name, vsnum, pa_title)
            items.append((tier, wnum, name, vsnum, pa_title))

    # De-dup (a W-number should appear once; keep first)
    seen = set(); dedup = []
    for it in items:
        if it[1] in seen:
            continue
        seen.add(it[1]); dedup.append(it)

    counts = {1: 0, 2: 0, 3: 0}
    by_tier = defaultdict(list)
    for tier, wnum, name, vsnum, pa in sorted(dedup, key=lambda x: x[1]):
        counts[tier] += 1
        by_tier[tier].append((wnum, name, vsnum))

    total = sum(counts.values())
    print(f"Proposed classification for {total} unclassified workflows:")
    print(f"  Tier 1 (core/statutory): {counts[1]}")
    print(f"  Tier 2 (standard support): {counts[2]}")
    print(f"  Tier 3 (advanced/opt):   {counts[3]}")

    if not args.write:
        print("\n(dry-run; pass --write to generate workflow-criticality-proposed.md)")
        return

    lines = []
    lines.append("# Proposed Criticality Classification (keyword-driven, Pass 14)")
    lines.append("")
    lines.append("> **Proposal — pending human review.** Auto-generated by "
                 "[`07-methodology/classify-workflows.py`](../../07-methodology/classify-workflows.py). "
                 "This file proposes a Tier 1/2/3 assignment for every workflow NOT already in the "
                 "authoritative [`workflow-criticality-classification.md`](workflow-criticality-classification.md). "
                 "Rules are deliberately conservative: Tier 1 is assigned only on high-confidence "
                 "statutory / core-transactional keywords (or a family override for wholly-statutory "
                 "value streams); Tier 3 only on high-confidence advanced-tech keywords; everything "
                 "else defaults to Tier 2 (the documented safe default for unclassified workflows). "
                 "On review, promote/demote rows by moving them into the confirmed register.")
    lines.append("")
    lines.append(f"**Workflow coverage:** {total} unclassified workflows · "
                 f"Tier 1: {counts[1]} · Tier 2: {counts[2]} · Tier 3: {counts[3]}")
    lines.append("")
    for tier, label in [(1, "Tier 1 — Core / statutory / revenue-critical (proposed)"),
                        (2, "Tier 2 — Standard support / cost control (proposed)"),
                        (3, "Tier 3 — Advanced / optimization / automation (proposed)")]:
        lines.append(f"## {label}")
        lines.append("")
        lines.append("| ID | Workflow | Value Stream |")
        lines.append("|---|---|---|")
        # group by VS for reviewability
        rows = sorted(by_tier[tier], key=lambda x: (x[2], x[0]))
        for wnum, name, vsnum in rows:
            vn = vs_name.get(vsnum, f"VS-{vsnum}")
            name_clean = name.replace("|", "\\|")
            lines.append(f"| {wnum} | {name_clean} | [VS-{vsnum}](VS-{vsnum}-{vn}) |")
        lines.append("")
    open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"\nWrote {OUT}")

if __name__ == "__main__":
    main()
