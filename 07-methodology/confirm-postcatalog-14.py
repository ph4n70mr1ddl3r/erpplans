#!/usr/bin/env python3
"""
confirm-postcatalog-14.py — One-time post-catalog confirmation pass (W5497–W5510).

Promotes the fourteen post-catalog workflow-level gap fills (W5497–W5510, added
2026-08-24/26) from the keyword-proposal register into the confirmed register
(workflow-criticality-classification.md), applying the calibrated confirmation
rules workflow-by-workflow — the same standard as the 2026-06-28 Full-Coverage
Confirmation Pass (confirm-all-workflows.py), but with human adjudications
recorded below instead of regex-only calibration:

    statutory / regulatory execution      -> Tier 1
    analytics / scorecard / optimization  -> Tier 3
    standard operational support          -> Tier 2 (safe default)

Adjudications (proposed -> confirmed):
  ADOPT     W5497 T1  CODI statutory machinery (RA 7877/RA 11313), statutory
            investigation clock, DOLE reporting interfaces.
  PROMOTE   W5498 T2->T1  RA 11165 written-telecommuting-agreement mandate,
            no-less-favorable-treatment duty, DOLE labor-standards inspection
            readiness, PD 626 telework EC claims — statutory execution.
  ADOPT     W5499 T2  director education program (training/program-support class).
  ADOPT     W5500 T2  WCAG accessibility program — compliance program with RA 7277
            exposure but no statutory filing/execution duty.
  PROMOTE   W5501 T2->T3  hazard-exposure modeling, scenario definition/quantification,
            KRIs and dashboards feeding W122's governance — analytics class.
  ADOPT     W5502 T2  wellness/education program.
  PROMOTE   W5503 T2->T1  DENR CCO 2013-24 90-ppm lead cap enforced through
            item-master/goods-receipt gates, DENR EMB market-surveillance response
            deadlines, stop-sale machinery — regulatory execution (VS-117 class).
  PROMOTE   W5504 T2->T1  RA 11058/DO 252-25 foreseeable-risk duty executed as a
            threshold work-interruption protocol on PAGASA advisories; sibling
            precedent W576 (typhoon protocol) and W140 (incident management) are T1.
  ADOPT     W5505 T1  core-transactional barcode/price-label integrity for items
            ringing on BuildRight POS (RA 7394 posted-tag regime).
  ADOPT     W5506 T2  approval/propagation operations.
  DEMOTE    W5507 T1->T2  service-fee billing & cost recovery — AR billing/dispute
            operations (W1614 chargeback pattern); the `barcode` keyword that
            proposed T1 is incidental to the fee schedule.
  ADOPT     W5508 T1  quarterly BIR Form 1605 FBT filing (20 filings/year) —
            statutory execution.
  DEMOTE    W5509 T1->T3  substitution analytics & replenishment feedback core;
            capture is instrumentation for the analytics — T3 class.
  DEMOTE    W5510 T1->T2  AP-side supplier service-fee billing & debit-memo cycle
            (W5507's mirror); `barcode` keyword incidental.

Net: 6 -> Tier 1 / 6 -> Tier 2 / 2 -> Tier 3 (14 total). Register arithmetic:
5,372 -> 5,386 rows; 5,349 -> 5,363 unique; T1 1,375 -> 1,381, T2 3,243 -> 3,249,
T3 754 -> 756. The proposal register is regenerated empty (0 unclassified) via
classify-workflows.py, and every downstream current-state figure spot is re-pointed
(register Summary/intro/coverage, workflows/README Quick Stats + nav row, root-README
coverage rows + tree rows, WORKFLOW-FORMAT-GUIDE anchors, dependency-map intro +
v4.16 footer note, gap-analysis current-state clause).

Every replacement below must match exactly once (asserted); idempotence is NOT
provided — this is a one-time pass.

Usage:
    python3 07-methodology/confirm-postcatalog-14.py --dry-run
    python3 07-methodology/confirm-postcatalog-14.py
"""
import argparse
import re
import subprocess
import sys

REPO = __file__.rsplit("/07-methodology/", 1)[0]
WF = f"{REPO}/01-model-company/workflows"
CLS = f"{WF}/workflow-criticality-classification.md"
PROP = f"{WF}/workflow-criticality-proposed.md"

DATE = "2026-09-02"

TITLES = {
    "W5497": "POSH / Safe Spaces Compliance Program — CODI Committee, Statutory Investigation & Reporting (RA 7877 / RA 11313)",
    "W5498": "Telecommuting & Flexible / Hybrid Work Arrangement Program (RA 11165)",
    "W5499": "Director Induction, Onboarding & Continuing Board Education Program",
    "W5500": "Customer Digital Accessibility Program — WCAG 2.1 AA Compliance for Web, App & Digital Channels",
    "W5501": "Climate Physical & Transition Risk Assessment, Scenario Analysis & Resilience Response Planning",
    "W5502": "Employee Financial Wellness Program — Literacy Education, Salary-Linked Lender Governance & Debt-Stress Support",
    "W5503": "Restricted-Substance & Chemical-Content Product Compliance — Lead-in-Paint (DENR CCO), Formaldehyde Emission & VOC Limits",
    "W5504": "Extreme-Heat Work Interruption & Occupational Heat-Stress Management (DOLE Heat-Index Advisory Response)",
    "W5505": "Concession Item Catalog, Barcode & Price-Label Onboarding & Governance",
    "W5506": "Concessionaire Self-Service Price Change Request, Approval & Store-Level Propagation",
    "W5507": "Concession Service-Fee Billing & Cost Recovery for Labels, Barcode Changes & Admin Services",
    "W5508": "Fringe Benefits Tax (FBT) Determination, Valuation & Quarterly BIR Form 1605 Filing",
    "W5509": "Unfulfilled-Demand & Lost-Sales Capture, Substitution Analytics & Replenishment Feedback",
    "W5510": "Supplier Service-Fee Billing & Account Deduction for Store-Rendered Services (Barcode Labels & Promotional Collaterals)",
}
VSNAME = {
    "W5497": "Labor Relations & Collective Bargaining", "W5498": "Hire-to-Retire",
    "W5499": "Corporate Governance", "W5500": "Ecommerce & Digital Channels",
    "W5501": "Internal Audit & Risk", "W5502": "Occupational Health & Employee Wellness",
    "W5503": "Quality Management & Product Compliance", "W5504": "Health, Safety & Environment",
    "W5505": "Store Operations", "W5506": "Store Operations", "W5507": "Store Operations",
    "W5508": "Tax Management & BIR Reporting", "W5509": "Supply Planning",
    "W5510": "Procure-to-Pay",
}
FAMILY = {
    "W5497": "People", "W5498": "People", "W5499": "Governance & Assurance",
    "W5500": "Sell & Serve", "W5501": "Governance & Assurance", "W5502": "People",
    "W5503": "Governance & Assurance", "W5504": "Governance & Assurance",
    "W5505": "Sell & Serve", "W5506": "Sell & Serve", "W5507": "Sell & Serve",
    "W5508": "Finance", "W5509": "Plan & Source", "W5510": "Finance",
}
TIER = {"W5497": 1, "W5498": 1, "W5499": 2, "W5500": 2, "W5501": 3, "W5502": 2,
        "W5503": 1, "W5504": 1, "W5505": 1, "W5506": 2, "W5507": 2, "W5508": 1,
        "W5509": 3, "W5510": 2}

TIER_ROWS = {1: [], 2: [], 3: []}
for w in sorted(TIER):
    TIER_ROWS[TIER[w]].append(f"| {w} | {TITLES[w]} | {VSNAME[w]} |")


def sub_once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        sys.exit(f"ABORT: replacement '{label}' matched {n} times (expected 1)")
    return text.replace(old, new)


def build_tier_subsection(tier):
    rows = TIER_ROWS[tier]
    intro = {
        1: ("#### Post-Catalog Confirmation (2026-09-02)\n\n"
            "Six post-catalog workflows confirmed **Tier 1** — statutory / regulatory execution "
            "(W5497 CODI machinery per RA 7877/RA 11313; W5508 quarterly BIR 1605 FBT filing) or "
            "core-transactional checkout integrity (W5505 barcode/price-label governance per the "
            "RA 7394 posted-tag regime), including three promotions from the keyword-proposed "
            "Tier 2 on statutory-execution grounds (W5498 RA 11165 agreement mandate + DOLE "
            "inspection readiness; W5503 DENR CCO lead-cap gates + agency response deadlines; "
            "W5504 RA 11058/DO 252-25 threshold work-interruption duty — W576/W140 sibling "
            "precedent). Rows in family order (People, Governance & Assurance, Sell & Serve, Finance):\n"),
        2: ("#### Post-Catalog Confirmation (2026-09-02)\n\n"
            "Six post-catalog workflows confirmed **Tier 2** — standard operational support: four "
            "adopted at the keyword-proposed tier (W5499 director education, W5500 WCAG "
            "accessibility program, W5502 financial wellness, W5506 price-change "
            "approval/propagation) and two demoted from the keyword-proposed Tier 1 because the "
            "`barcode` core-transactional keyword is incidental to their billing/recovery core "
            "(W5507 concession service-fee billing; W5510 supplier service-fee billing & account "
            "deduction — the W1614 chargeback-pattern class). Rows in family order "
            "(Governance & Assurance, Sell & Serve, People, Finance):\n"),
        3: ("#### Post-Catalog Confirmation (2026-09-02)\n\n"
            "Two post-catalog workflows confirmed **Tier 3** — analytics/optimization class: "
            "W5501 promoted from the keyword-proposed Tier 2 (hazard-exposure modeling, scenario "
            "definition/quantification, KRIs feeding W122's governance) and W5509 demoted from the "
            "keyword-proposed Tier 1 (substitution analytics & replenishment-feedback core; the "
            "capture layer is instrumentation). Rows in family order (Governance & Assurance, "
            "Plan & Source):\n"),
    }[tier]
    table = "| ID | Workflow | Value Stream |\n|---|---|---|\n" + "\n".join(rows) + "\n"
    return "\n" + intro + "\n" + table


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    # ---------------- 1. workflow-criticality-classification.md ----------------
    cls = open(CLS, encoding="utf-8").read()

    # 1a. Intro banner -> full-coverage form (Check 18's full-coverage frame)
    old_intro = """> Classifies operational workflows into criticality tiers (the confirmed register holds 5,372
> rows, of which 23 are `###` parent/summary sub-workflows double-counted against a `##` parent,
> covering 5,349 unique workflows). The 2026-06-28 Full-Coverage Confirmation Pass had promoted every
> then-existing keyword-proposed workflow into the confirmed register (unclassified 2,596 → 0).
> An additional 14 workflows (5,363 total − 5,349 classified) — W5497–W5510, added 2026-08-24/26 as
> post-catalog workflow-level gap fills — are unclassified; each carries a keyword-driven proposed
> tier in
> [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md)
> (`07-methodology/classify-workflows.py` re-derives it from the register on every run) pending a
> confirmation pass."""
    new_intro = """> Classifies all 5,363 unique operational workflows into criticality tiers (the confirmed
> register holds 5,386 rows, of which 23 are `###` parent/summary sub-workflows double-counted
> against a `##` parent). Zero workflows remain unclassified: the 2026-06-28 Full-Coverage
> Confirmation Pass promoted every then-existing keyword-proposed workflow (unclassified
> 2,596 → 0), and the fourteen post-catalog workflows W5497–W5510 (added 2026-08-24/26) were
> confirmed on 2026-09-02 by the post-catalog confirmation pass
> (`07-methodology/confirm-postcatalog-14.py`; 6 → Tier 1, 6 → Tier 2, 2 → Tier 3).
> [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) is empty and is
> re-derived from the register on every run of
> `07-methodology/classify-workflows.py` whenever new workflows ship unclassified."""
    cls = sub_once(cls, old_intro, new_intro, "intro banner")

    # 1b. Tier headings + body sentences + Additions headings
    for old, new, label in [
        ("## Tier 1: Core Operations (1,375 Workflows)", "## Tier 1: Core Operations (1,381 Workflows)", "T1 heading"),
        ("## Tier 2: Standard Support (3,243 Workflows)", "## Tier 2: Standard Support (3,249 Workflows)", "T2 heading"),
        ("## Tier 3: Advanced Optimization (754 Workflows)", "## Tier 3: Advanced Optimization (756 Workflows)", "T3 heading"),
        ("These 1,375 workflows are foundational", "These 1,381 workflows are foundational", "T1 body"),
        ("These 3,243 workflows are needed", "These 3,249 workflows are needed", "T2 body"),
        ("These 754 workflows deliver advanced capabilities", "These 756 workflows deliver advanced capabilities", "T3 body"),
        ("### Tier 1 Additions (401 Workflows)", "### Tier 1 Additions (407 Workflows)", "T1 Additions heading"),
        ("### Tier 2 Additions (488 Workflows)", "### Tier 2 Additions (494 Workflows)", "T2 Additions heading"),
        ("### Tier 3 Additions (128 Workflows)", "### Tier 3 Additions (130 Workflows)", "T3 Additions heading"),
    ]:
        cls = sub_once(cls, old, new, label)

    # 1c. Summary — confirmed table, note, proposed mirror, coverage table, Domain Breakdown
    cls = sub_once(cls,
        "| Phase 1 | Go-Live Critical (Tier 1) | 1,375 | 25.6% |",
        "| Phase 1 | Go-Live Critical (Tier 1) | 1,381 | 25.6% |", "Summary T1 row")
    cls = sub_once(cls,
        "| Phase 2 | Operational Excellence (Tier 2) | 3,243 | 60.4% |",
        "| Phase 2 | Operational Excellence (Tier 2) | 3,249 | 60.3% |", "Summary T2 row")
    cls = sub_once(cls,
        "| Phase 3 | Innovation & Optimization (Tier 3) | 754 | 14.0% |",
        "| Phase 3 | Innovation & Optimization (Tier 3) | 756 | 14.0% |", "Summary T3 row")
    cls = sub_once(cls,
        "| **Confirmed Total** | | **5,372** | 100% |",
        "| **Confirmed Total** | | **5,386** | 100% |", "Summary Confirmed Total")
    cls = sub_once(cls,
        "> own classification row; the remaining 5,349 are canonical `##` workflows.",
        "> own classification row; the remaining 5,363 are canonical `##` workflows.",
        "Summary confirmed note")
    cls = sub_once(cls,
        """The register reached full coverage on 2026-06-28 (every then-existing keyword-proposed workflow
promoted by the Full-Coverage Confirmation Pass). On 2026-08-24/26, fourteen post-catalog workflow-level
gap fills (W5497–W5510) shipped unclassified and repopulated the proposal register;
[`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) is regenerated by
[`07-methodology/classify-workflows.py`](../../07-methodology/classify-workflows.py).

| Phase | Label | Proposed Count |
|---|---|---|
| Phase 1 | Go-Live Critical (Tier 1) — proposed | 6 |
| Phase 2 | Operational Excellence (Tier 2) — proposed | 8 |
| Phase 3 | Innovation & Optimization (Tier 3) — proposed | 0 |
| **Proposed Total** | | **14** |""",
        """The register reached full coverage on 2026-06-28 (every then-existing keyword-proposed workflow
promoted by the Full-Coverage Confirmation Pass) and holds full coverage again since 2026-09-02,
when the fourteen post-catalog workflow-level gap fills (W5497–W5510, added 2026-08-24/26) were
confirmed by the post-catalog confirmation pass — 6 → Tier 1, 6 → Tier 2, 2 → Tier 3, with three
statutory-execution promotions (W5498/W5503/W5504), one analytics promotion (W5501), two analytics/
billing-core demotions to Tier 3 (W5509) and Tier 2 (W5507/W5510), and eight adoptions at the
keyword-proposed tier. [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) is
empty and is regenerated by
[`07-methodology/classify-workflows.py`](../../07-methodology/classify-workflows.py)
whenever new workflows ship unclassified.

| Phase | Label | Proposed Count |
|---|---|---|
| Phase 1 | Go-Live Critical (Tier 1) — proposed | 0 |
| Phase 2 | Operational Excellence (Tier 2) — proposed | 0 |
| Phase 3 | Innovation & Optimization (Tier 3) — proposed | 0 |
| **Proposed Total** | | **0** |""",
        "proposed-summary block")
    cls = sub_once(cls,
        "| Confirmed (hand-reviewed) | 5,372 rows (5,349 unique `##` workflows) |",
        "| Confirmed (hand-reviewed) | 5,386 rows (5,363 unique `##` workflows) |",
        "coverage Confirmed row")
    cls = sub_once(cls,
        "| Proposed (keyword, pending review) | 14 |",
        "| Proposed (keyword, pending review) | 0 |", "coverage Proposed row")
    cls = sub_once(cls,
        "| **Grand Total** | **5,363** unique `##` workflows (5,349 confirmed + 14 unclassified) |",
        "| **Grand Total** | **5,363** unique `##` workflows (5,363 confirmed + 0 unclassified) |",
        "coverage Grand Total row")
    cls = sub_once(cls,
        "breakdown of the 5,372 classified register rows (5,349 unique workflows)",
        "breakdown of the 5,386 classified register rows (5,363 unique workflows)",
        "Domain Breakdown prose")

    # 1d. Dated confirmation note after the batch-5 addition note
    batch5_anchor = "warrants explicit confirmation review)."
    note = ("\n\n> **2026-09-02 confirmation (post-catalog pass):** The fourteen post-catalog workflows "
            "W5497–W5510 were confirmed by the post-catalog confirmation pass "
            "(`07-methodology/confirm-postcatalog-14.py`), applying the calibrated rules "
            "workflow-by-workflow: **6 → Tier 1** (W5497 CODI statutory machinery; W5498 *promoted* "
            "on the RA 11165 written-agreement mandate, no-less-favorable-treatment duty and DOLE "
            "labor-standards inspection readiness; W5503 *promoted* on the DENR CCO 2013-24 90-ppm "
            "lead-cap item/goods-receipt gates, DENR EMB market-surveillance response deadlines and "
            "stop-sale machinery; W5504 *promoted* on the RA 11058/DO 252-25 foreseeable-risk duty "
            "executed as a threshold work-interruption protocol — the W576/W140 Tier-1 sibling "
            "precedent; W5505 core-transactional barcode/price-label integrity under the RA 7394 "
            "posted-tag regime; W5508 quarterly BIR 1605 FBT filing), **6 → Tier 2** (W5499/W5500/"
            "W5502/W5506 adopted at the proposed tier; W5507/W5510 *demoted* — service-fee billing "
            "and account-deduction recovery operations where the `barcode` keyword is incidental to "
            "the fee schedule), and **2 → Tier 3** (W5501 *promoted* — scenario analysis/modeling "
            "feeding W122; W5509 *demoted* — substitution-analytics core). Register 5,372 → 5,386 "
            "rows (5,349 → 5,363 unique); the proposal register is regenerated empty.")
    cls = sub_once(cls, batch5_anchor, batch5_anchor + note, "confirmation note")

    # 1e. Per-tier Additions subsections (insert at each Additions section tail):
    # Tier 1 and Tier 2 insert before the next tier's Additions heading; Tier 3 before
    # the first heading of level <= 3 that follows its section.
    cls = sub_once(cls, "\n### Tier 2 Additions (494 Workflows)",
                   build_tier_subsection(1) + "\n### Tier 2 Additions (494 Workflows)",
                   "T1 subsection insert")
    cls = sub_once(cls, "\n### Tier 3 Additions (130 Workflows)",
                   build_tier_subsection(2) + "\n### Tier 3 Additions (130 Workflows)",
                   "T2 subsection insert")
    m = re.search(r"^### Tier 3 Additions \(130 Workflows\)$", cls, re.M)
    if not m:
        sys.exit("ABORT: cannot locate Tier 3 Additions heading for insert")
    tail_start = m.end()
    nxt = re.search(r"^#{1,3} (?!Tier 3 Additions).+$", cls[tail_start:], re.M)
    if not nxt:
        sys.exit("ABORT: cannot locate the section following Tier 3 Additions")
    cut = tail_start + nxt.start()
    cls = cls[:cut] + build_tier_subsection(3).rstrip("\n") + "\n" + cls[cut:]

    # 1f. v7.42 footer note (newest *Date: note first, above v7.41)
    v742 = ("*Date: 2026-09-02 | Workflow Criticality Classification v7.42 — post-catalog confirmation "
            "pass: the fourteen post-catalog workflows W5497–W5510 (added 2026-08-24/26) confirmed "
            "6 → Tier 1 / 6 → Tier 2 / 2 → Tier 3 by `07-methodology/confirm-postcatalog-14.py` "
            "(adjudications in the dated confirmation note above; three statutory-execution promotions "
            "W5498/W5503/W5504, one analytics promotion W5501, demotions W5509 → T3 and W5507/W5510 → T2, "
            "eight adoptions). Register 5,372 → 5,386 rows (5,349 → 5,363 unique; T1 1,375 → 1,381, "
            "T2 3,243 → 3,249, T3 754 → 756); proposed register regenerated empty (0 unclassified); "
            "downstream figures re-pointed (workflows/README Quick Stats + nav row, root-README coverage "
            "rows + tree rows, WORKFLOW-FORMAT-GUIDE anchors, dependency-map intro + v4.16 footer, "
            "gap-analysis current-state clause). `validate-repo.sh`: 0 errors / 0 warnings across 63 checks.*\n")
    anchor = "*Date: 2026-08-28 | Workflow Criticality Classification v7.41"
    cls = sub_once(cls, anchor, v742 + anchor, "v7.42 footer note")

    # ---------------- 2. workflows/README.md ----------------
    wfr = open(f"{WF}/README.md", encoding="utf-8").read()
    wfr = sub_once(wfr, "| Classified (Tier 1) | 1,375 |", "| Classified (Tier 1) | 1,381 |", "QS T1")
    wfr = sub_once(wfr, "| Classified (Tier 2) | 3,243 |", "| Classified (Tier 2) | 3,249 |", "QS T2")
    wfr = sub_once(wfr, "| Classified (Tier 3) | 754 |", "| Classified (Tier 3) | 756 |", "QS T3")
    wfr = sub_once(wfr,
        "| Classified total | 5,372 rows = 5,349 unique workflows + 23 parent/summary sub-workflow rows (full coverage confirmed 2026-06-28; the 14 post-catalog workflows W5497–W5510, added 2026-08-24/26, ship unclassified with keyword-driven proposed tiers) |",
        "| Classified total | 5,386 rows = 5,363 unique workflows + 23 parent/summary sub-workflow rows (full coverage: confirmed 2026-06-28 by the Full-Coverage Confirmation Pass and re-achieved 2026-09-02 when the 14 post-catalog workflows W5497–W5510 were confirmed 6 T1 / 6 T2 / 2 T3) |",
        "QS classified total")
    wfr = sub_once(wfr,
        "| [workflow-criticality-proposed.md](workflow-criticality-proposed.md) | Keyword-driven tier proposal register for workflows outside the confirmed register — holds the 14 unclassified post-catalog workflows (W5497–W5510, added 2026-08-24/26) pending confirmation; regenerates automatically whenever new workflows ship unclassified |",
        "| [workflow-criticality-proposed.md](workflow-criticality-proposed.md) | Keyword-driven tier proposal register for workflows outside the confirmed register — currently empty (0 unclassified since the 2026-09-02 post-catalog confirmation of W5497–W5510); regenerates automatically whenever new workflows ship unclassified |",
        "nav proposed row")

    # ---------------- 3. root README.md ----------------
    root = open(f"{REPO}/README.md", encoding="utf-8").read()
    root = sub_once(root,
        "│   │   ├── workflow-criticality-classification.md  Tier 1/2/3 confirmed priorities (5,372 rows)",
        "│   │   ├── workflow-criticality-classification.md  Tier 1/2/3 confirmed priorities (5,386 rows)",
        "root tree classification row")
    root = sub_once(root,
        "│   │   ├── workflow-criticality-proposed.md    Keyword-driven tier proposal register for unclassified workflows (14 post-catalog workflows W5497–W5510 added 2026-08-24/26)",
        "│   │   ├── workflow-criticality-proposed.md    Keyword-driven tier proposal register for unclassified workflows (currently empty — 0 unclassified; regenerates via classify-workflows.py)",
        "root tree proposed row")
    root = sub_once(root,
        "| Workflows | 5,363 fully specified across 188 value streams (5,349 confirmed-classified + 14 post-catalog additions W5497–W5510 with keyword-proposed tiers) | `workflows/value-stream-index.md` |",
        "| Workflows | 5,363 fully specified across 188 value streams (all 5,363 confirmed-classified — the 14 post-catalog additions W5497–W5510 were confirmed 2026-09-02) | `workflows/value-stream-index.md` |",
        "root coverage Workflows row")
    root = sub_once(root,
        "| Criticality classification | **5,349 of 5,363 workflows classified** — the confirmed register holds 5,372 rows incl. 23 `###` parent/summary sub-workflows; the 2026-06-28 Full-Coverage Confirmation Pass promoted the remaining keyword-proposed workflows (unclassified 2,596 → 0; 65 → Tier 1 statutory, 179 → Tier 3 analytics, 3 demoted to Tier 2, remainder adopted); the fourteen post-catalog workflows W5497–W5510 (added 2026-08-24/26: POSH/Safe Spaces CODI, RA 11165 telecommuting, director education, customer digital accessibility/WCAG, climate risk assessment, employee financial wellness, restricted-substance & chemical-content product compliance, extreme-heat work interruption & occupational heat-stress management, concession item catalog/barcode/price-label governance, concessionaire self-service price change & propagation, concession service-fee billing & cost recovery, fringe benefits tax determination & quarterly BIR 1605 filing, unfulfilled-demand & lost-sales capture, supplier service-fee billing & account deduction for store-rendered services) carry keyword-driven proposed tiers in `workflow-criticality-proposed.md` pending a confirmation pass | `workflows/workflow-criticality-classification.md` |",
        "| Criticality classification | **5,363 of 5,363 workflows classified (full coverage)** — the confirmed register holds 5,386 rows incl. 23 `###` parent/summary sub-workflows; the 2026-06-28 Full-Coverage Confirmation Pass promoted the remaining keyword-proposed workflows (unclassified 2,596 → 0; 65 → Tier 1 statutory, 179 → Tier 3 analytics, 3 demoted to Tier 2, remainder adopted), and the fourteen post-catalog workflows W5497–W5510 (added 2026-08-24/26: POSH/Safe Spaces CODI, RA 11165 telecommuting, director education, customer digital accessibility/WCAG, climate risk assessment, employee financial wellness, restricted-substance & chemical-content product compliance, extreme-heat work interruption & occupational heat-stress management, concession item catalog/barcode/price-label governance, concessionaire self-service price change & propagation, concession service-fee billing & cost recovery, fringe benefits tax determination & quarterly BIR 1605 filing, unfulfilled-demand & lost-sales capture, supplier service-fee billing & account deduction for store-rendered services) were confirmed 2026-09-02 by the post-catalog confirmation pass — 6 → Tier 1, 6 → Tier 2, 2 → Tier 3; `workflow-criticality-proposed.md` is empty | `workflows/workflow-criticality-classification.md` |",
        "root coverage classification row")

    # ---------------- 4. WORKFLOW-FORMAT-GUIDE.md ----------------
    fg = open(f"{WF}/WORKFLOW-FORMAT-GUIDE.md", encoding="utf-8").read()
    fg = sub_once(fg,
        "├── workflow-criticality-classification.md  Tier 1/2/3 priorities (5,372 confirmed rows; 14 post-catalog workflows keyword-proposed)",
        "├── workflow-criticality-classification.md  Tier 1/2/3 priorities (5,386 confirmed rows; 0 post-catalog workflows keyword-proposed)",
        "format-guide layout classification row")
    fg = sub_once(fg,
        "├── workflow-criticality-proposed.md      Keyword-driven tier proposal register (holds the 14 unclassified post-catalog workflows W5497–W5510; regenerates via classify-workflows.py)",
        "├── workflow-criticality-proposed.md      Keyword-driven tier proposal register (currently empty — 0 unclassified; regenerates via classify-workflows.py)",
        "format-guide layout proposed row")
    fg = sub_once(fg,
        "| [workflow-criticality-proposed.md](workflow-criticality-proposed.md) | Keyword-driven tier proposal register for unclassified workflows (companion; holds the 14 unclassified post-catalog workflows W5497–W5510 added 2026-08-24/26, pending confirmation) |",
        "| [workflow-criticality-proposed.md](workflow-criticality-proposed.md) | Keyword-driven tier proposal register for unclassified workflows (companion; currently empty — 0 unclassified since the 2026-09-02 post-catalog confirmation) |",
        "format-guide related-docs proposed row")

    # ---------------- 5. workflow-dependency-map.md ----------------
    dep = open(f"{WF}/workflow-dependency-map.md", encoding="utf-8").read()
    dep = sub_once(dep,
        """> Directed dependency graph of classified operational workflows, showing prerequisite
> relationships for system functions. Of 5,363 total workflows, 5,349 are classified into
> criticality tiers (the confirmed register holds 5,372 rows, incl. 23 `###` parent/summary
> sub-workflows); 14 (W5497–W5510, added 2026-08-24/26 as post-catalog workflow-level gap fills in
> existing core/statutory value streams) are unclassified with keyword-driven proposed tiers
> pending a confirmation pass (see
> [`workflow-criticality-classification.md`](workflow-criticality-classification.md)).""",
        """> Directed dependency graph of classified operational workflows, showing prerequisite
> relationships for system functions. All 5,363 workflows are classified into
> criticality tiers (the confirmed register holds 5,386 rows, incl. 23 `###` parent/summary
> sub-workflows) — the fourteen post-catalog additions W5497–W5510 (added 2026-08-24/26) were
> confirmed 2026-09-02 by the post-catalog confirmation pass; their step-level edge
> incorporation into §1–§7 proceeds as edges are curated (see
> [`workflow-criticality-classification.md`](workflow-criticality-classification.md)).""",
        "dep-map intro")
    v416 = ("*Date: 2026-09-02 | Workflow Dependency Map v4.16 — post-catalog confirmation pass: the "
            "fourteen post-catalog workflows W5497–W5510 were confirmed into the criticality register "
            "(6 → Tier 1 / 6 → Tier 2 / 2 → Tier 3; see the classification v7.42 note), so the intro "
            "now declares full classification (5,363 of 5,363; register 5,386 rows) and drops the "
            "pending-confirmation clause. No edge, block-size, or anchor-count changes; step-level edge "
            "incorporation of the fourteen into §1–§7 proceeds as edges are curated. Prior ")
    dep = sub_once(dep, "*Date: 2026-08-28 | Workflow Dependency Map v4.15",
                   v416 + "*Date: 2026-08-28 | Workflow Dependency Map v4.15", "dep-map v4.16 footer")

    # ---------------- 6. workflow-gap-analysis.md current-state clause ----------------
    ga = open(f"{WF}/workflow-gap-analysis.md", encoding="utf-8").read()
    ga = sub_once(ga,
        "**188 value streams · 569 process areas · 5,363 workflows** (the fourteen post-catalog workflows\n> ship unclassified with keyword-driven proposed tiers pending a confirmation pass).",
        "**188 value streams · 569 process areas · 5,363 workflows** (the fourteen post-catalog workflows\n> were confirmed 2026-09-02 by the post-catalog confirmation pass — full classification coverage).",
        "gap-analysis current-state clause")

    if args.dry_run:
        print("dry-run: all replacements matched exactly once; no files written")
        return

    open(CLS, "w", encoding="utf-8").write(cls)
    open(f"{WF}/README.md", "w", encoding="utf-8").write(wfr)
    open(f"{REPO}/README.md", "w", encoding="utf-8").write(root)
    open(f"{WF}/WORKFLOW-FORMAT-GUIDE.md", "w", encoding="utf-8").write(fg)
    open(f"{WF}/workflow-dependency-map.md", "w", encoding="utf-8").write(dep)
    open(f"{WF}/workflow-gap-analysis.md", "w", encoding="utf-8").write(ga)
    print("wrote: classification, workflows/README, root README, format-guide, dependency-map, gap-analysis")

    # ---------------- 7. regenerate the proposal register (empty) ----------------
    r = subprocess.run([sys.executable, f"{REPO}/07-methodology/classify-workflows.py", "--write"],
                       capture_output=True, text=True)
    print(r.stdout.strip())
    if r.returncode != 0:
        sys.exit(f"classify-workflows.py failed: {r.stderr}")
    prop = open(PROP, encoding="utf-8").read()
    m = re.search(r"\*\*Workflow coverage:\*\* (\d+) unclassified workflows · Tier 1: (\d+) · Tier 2: (\d+) · Tier 3: (\d+)", prop)
    if not m or any(int(g) != 0 for g in m.groups()):
        sys.exit(f"ABORT: regenerated proposal register is not empty: {m.groups() if m else 'unparseable'}")
    print("proposal register regenerated empty (0 unclassified)")
    print("done: 14 workflows promoted; register 5,386 rows / 5,363 unique; T1 1,381 / T2 3,249 / T3 756")


if __name__ == "__main__":
    main()
