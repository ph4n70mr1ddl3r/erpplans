#!/usr/bin/env python3
"""
fix-controls-bullets.py — Repair Controls-section rendering defects + mangled bold labels.

Consistency review #27 found a defect cluster no prior check could see (all 42 checks
validate counts/IDs/anchors/tables — none validated *list hygiene* inside analysis
sections):

  1. Dangling `operational:` continuation lines. The original
     `add-automation-controls.py` generator emitted CTL bullets with a `- ` prefix but
     `operational:` items without one, so 3,349 Controls sections rendered with the
     operational controls as a stray paragraph glued to the bullet list. Fixed by
     prefixing `- ` (the generator's own item format — see its `generate_controls`).

  2. Unbalanced parentheses. The generator's pain-point extraction regex
     (`mitigated by (.+?)(?:[.;]|$)`) truncated captures at the first period of
     "e.g."/"vs."/"No." and swallowed closing parens at `; operational:` joins,
     leaving 78 Controls lines with unbalanced parens. The unambiguous majority
     pattern — `X (links to VS-NN; operational:` — is repaired mechanically by
     re-inserting `)` before the `; operational:` boundary (and at end-of-line when a
     line still ends with an open paren and never went negative).

  3. Generator junk segments. 35 lines carried fragments of *pain-point descriptions*
     (not controls) — bold labels (`operational: reliability**:`), truncated
     "(e.g., …" tails, and quoted script lines. These are repaired surgically below
     from each workflow's own intact Pain Points (genuine mitigations kept verbatim,
     junk dropped) — each replacement was verified against the source pain-point text.

  4. Mangled bold labels in Pain Points bullets: `- **Label": text` (11 lines, the
     `**` closed with a stray `"` instead) → `- **Label**: text`.

  5. One Pain Points bullet written as a table row (PA-137.2) → normal bullet.

All transforms are content-preserving except (3), where junk fragments mislabelled as
controls are dropped/repaired per the source pain points. Guarded by validator Check 43.
Idempotent: re-running on already-fixed files is a no-op.

Usage:
    python3 07-methodology/fix-controls-bullets.py           # write changes
    python3 07-methodology/fix-controls-bullets.py --check   # report only, exit 1 if pending
"""
import argparse, glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MC = os.path.join(REPO, "01-model-company")
WF = os.path.join(MC, "workflows")

# ── (3) Surgical repairs: (relative path, exact current line) → replacement line.
# A value of None deletes the line (generator junk; the workflow's pain points carry
# no mitigation to keep — verified case by case during review #27).
SURGICAL = {
    # VS-02.2 W1233 — pain-point description fragment, no mitigation in source pains
    ("workflows/VS-02-supply-planning/PA-02.2-import-and-customs-operations.md",
     "operational: downtime** — the BOC e2m system experiences periodic downtime"): None,
    # VS-04.3 W270 — description fragment (drivers exchange RTPs without recording)
    ("workflows/VS-04-dc-warehouse/PA-04.3-dc-operations-management.md",
     "operational: recording) during receiving, bypassing the formal RTP logging process"): None,
    # VS-05.3 W1189 — "(90 days vs." truncated at "vs."; completed from source pain 2
    ("workflows/VS-05-inventory-lifecycle/PA-05.3-inventory-disposition-and-optimization.md",
     "operational: automated POS block in Step 5 and graduated markdown in Step 3 to ensure stock sells before expiry; operational: using conservative shelf life settings (90 days vs; operational: smaller, more frequent orders and vendor-managed inventory (W20) for high-volume cement brands"):
     "operational: automated POS block in Step 5 and graduated markdown in Step 3 to ensure stock sells before expiry; operational: using conservative shelf life settings (90 days vs. 120 days) and palletized covered storage; operational: smaller, more frequent orders and vendor-managed inventory (W20) for high-volume cement brands",
    # VS-07.1 W278 — genuine mitigation, stray ")"
    ("workflows/VS-07-store-operations/PA-07.1-store-daily-management.md",
     "operational: dual-sign and CCTV)"):
     "operational: dual-sign and CCTV",
    # VS-07.1 W1121 — label+description fragment; real mitigation is the backup measures
    ("workflows/VS-07-store-operations/PA-07.1-store-daily-management.md",
     "operational: reliability**: If the PA system fails during an emergency, lives are at risk"):
     "operational: battery backup and manual megaphone as mandatory backup measures",
    # VS-07.4 W601 — junk middle segment dropped (both genuine mitigations kept)
    ("workflows/VS-07-store-operations/PA-07.4-store-staffing-and-people.md",
     "operational: backup RFID badge scanning; operational: downtime**: biometric failure requires manual punch entry with supervisor confirmation per W561; operational: real-time overtime budget tracking in Step 4"):
     "operational: backup RFID badge scanning; operational: real-time overtime budget tracking in Step 4",
    # VS-08.1 W523 — description fragment; source mitigation is post-promo verification
    ("workflows/VS-08-pos-checkout/PA-08.1-transaction-processing.md",
     "operational: bug or config error) causes incorrect pricing on day after promo ends"):
     "operational: post-promo verification of promo deactivation",
    # VS-08.1 W552 — "(e" truncated "(e.g., skip every other transaction…)"
    ("workflows/VS-08-pos-checkout/PA-08.1-transaction-processing.md",
     "operational: prompt only once per transaction, easy \"No Thanks\" option, and configurable prompt frequency (e; operational: cashier training (W518) and analytics visibility; operational: system-enforced GL routing for donation line items"):
     "operational: prompt only once per transaction, easy \"No Thanks\" option, and configurable prompt frequency (e.g., skip every other transaction for same customer); operational: cashier training (W518) and analytics visibility; operational: system-enforced GL routing for donation line items",
    # VS-08.2 W543 — "(W543" truncated "(W543.3) as evidence"
    ("workflows/VS-08-pos-checkout/PA-08.2-payment-and-cash-management.md",
     "operational: item master governance (W252) with consignment flag validation at SKU creation; operational: real-time consignment inventory deduction and vendor recall processing per W29; operational: transaction-level sell-through data (W543"):
     "operational: item master governance (W252) with consignment flag validation at SKU creation; operational: real-time consignment inventory deduction and vendor recall processing per W29; operational: transaction-level sell-through data (W543.3) as evidence",
    # VS-08.3 W519 — both segments are pain-description fragments
    ("workflows/VS-08-pos-checkout/PA-08.3-pos-compliance-and-controls.md",
     "operational: should learn to reduce false positives over time (e; operational: does not aggregate across terminals and locations in real-time"): None,
    # VS-08.3 W520 — quoted script fragment; source mitigation is the spot-audit program
    ("workflows/VS-08-pos-checkout/PA-08.3-pos-compliance-and-controls.md",
     "operational: by law to verify age for these products\"); operational: accepts DOB entry in good faith"):
     "operational: quarterly spot-audits and verification rate monitoring",
    # VS-09.1 W1027 — control-design rule; paren completed from source pain 3
    ("workflows/VS-09-in-store-services/PA-09.1-custom-fabrication-and-processing.md",
     "operational: on-hand > 3 units) and include \"subject to availability\" disclaimer"):
     "operational: buffer-discount display rule (show \"available\" only if on-hand > 3 units) and \"subject to availability\" disclaimer",
    # VS-10.1 W923 — "(partners below 4" truncated "(partners below 4.0/5.0 for 2 consecutive quarters placed on probation)"
    ("workflows/VS-10-ecommerce-digital/PA-10.1-ecommerce-platform-operations.md",
     "operational: competitive pricing (benchmark against independent installers), convenience messaging, and \"protect your warranty\" communication; operational: delivery tracking integration, automated reminders per W708, and rescheduling via customer service per W258; operational: W213 quality audit program, customer satisfaction survey, and partner scorecard with minimum rating threshold (partners below 4"):
     "operational: competitive pricing (benchmark against independent installers), convenience messaging, and \"protect your warranty\" communication; operational: delivery tracking integration, automated reminders per W708, and rescheduling via customer service per W258; operational: W213 quality audit program, customer satisfaction survey, and partner scorecard with minimum rating threshold (partners below 4.0/5.0 for 2 consecutive quarters placed on probation)",
    # VS-11.3 W598 — "(e" truncated "(e.g., deposit, LOI) for large quotations…"
    ("workflows/VS-11-trade-project-wholesale/PA-11.3-wholesale-operations.md",
     "operational: W85 landed cost tracking, monthly price list review, and clear minimum margin floors with approval gates; operational: dedicated government procurement specialist per W78 and pre-bid pricing analysis; operational: requiring reseller commitment indicators (e"):
     "operational: W85 landed cost tracking, monthly price list review, and clear minimum margin floors with approval gates; operational: dedicated government procurement specialist per W78 and pre-bid pricing analysis; operational: requiring reseller commitment indicators (e.g., deposit, LOI) for large quotations and conversion-rate tracking by Sales Rep",
    # VS-13.1 W258 — description fragment (pains carry no mitigations)
    ("workflows/VS-13-customer-experience/PA-13.1-customer-support-and-complaints.md",
     "operational: handoff friction**: Escalated tickets requiring store action (e"): None,
    # VS-18.3 W319 — both segments are pain-description fragments
    ("workflows/VS-18-treasury-cash/PA-18.3-fx-and-investments.md",
     "operational: Fixing Rate) or PHIBOR + spread, rising benchmark rates increase interest expense; operational: document can trigger a technical default even when financial covenants are met"): None,
    # VS-19.3 W34 — description fragments (pains carry no mitigations)
    ("workflows/VS-19-hire-to-retire/PA-19.3-workforce-management.md",
     "operational: approval creates audit gaps in time & attendance and can lead to under-staffed shifts; operational: skill coverage (e"): None,
    # VS-19.5 W977 — second segment is description tail "(mandatory at 65)"
    ("workflows/VS-19-hire-to-retire/PA-19.5-separation-and-benefits.md",
     "operational: conservative investment policy and annual board review; operational: at 65)"):
     "operational: conservative investment policy and annual board review",
    # VS-20.3 W701 — description fragment ("system loss charge components")
    ("workflows/VS-20-real-estate-construction/PA-20.3-facility-maintenance-and-equipment.md",
     "operational: loss charge components)"): None,
    # VS-21.2 W1330 — "(e" truncated "(e.g., Yolanda-level typhoon, actual competitor entries…)"
    ("workflows/VS-21-internal-audit-risk/PA-21.2-enterprise-risk-management.md",
     "operational: linking to annual strategic planning cycle when Exec Team is already in planning mode; operational: using historically grounded scenarios (e; operational: Board Risk Committee oversight and quarterly tracking via W122"):
     "operational: linking to annual strategic planning cycle when Exec Team is already in planning mode; operational: using historically grounded scenarios (e.g., Yolanda-level typhoon, actual competitor entries in other ASEAN markets); operational: Board Risk Committee oversight and quarterly tracking via W122",
    # VS-22.2 W961 — quoted script fragment (pains carry no mitigations)
    ("workflows/VS-22-compliance-regulatory/PA-22.2-government-audit-and-inspection-response.md",
     "operational: to record your ID for our records, sir/ma'am\") without mentioning AMLC"): None,
    # VS-22.3 W114 — label+description fragment (pains carry no mitigations)
    ("workflows/VS-22-compliance-regulatory/PA-22.3-regulatory-change-management.md",
     "operational: reporting tension**: SEC sustainability reporting requirements (MC No"): None,
    # VS-22.3 W1219 — label+description fragments
    ("workflows/VS-22-compliance-regulatory/PA-22.3-regulatory-change-management.md",
     "operational: instability** — BIR EIS platform has experienced outages during peak implementation periods; operational: must handle peak volumes (weekend and holiday spikes at 2–3× average)"): None,
    # VS-23.1 W1475 — description fragment; source mitigation is the loophole closure
    ("workflows/VS-23-loss-prevention/PA-23.1-exception-monitoring-and-investigation.md",
     "operational: can circumvent controls (e"):
     "operational: system controls that close technical loopholes (e.g., coupon stacking restrictions and usage limits)",
    # VS-23.3 W1338 — junk middle segment dropped (both genuine mitigations kept)
    ("workflows/VS-23-loss-prevention/PA-23.3-shrinkage-reduction.md",
     "operational: requiring multiple converging indicators before investigation and LP Manager assessment; operational: errors); operational: HR-led process with VP Legal oversight"):
     "operational: requiring multiple converging indicators before investigation and LP Manager assessment; operational: HR-led process with VP Legal oversight",
    # VS-27.1 W1408 — description fragment (pain carries no mitigation)
    ("workflows/VS-27-it-operations-security/PA-27.1-service-management.md",
     "operational: outages) may retain elevated permissions after the emergency resolves"): None,
    # VS-27.3 W1205 — junk trailing segment dropped (both genuine mitigations kept)
    ("workflows/VS-27-it-operations-security/PA-27.3-cybersecurity-and-privacy.md",
     "operational: standardized POS image deployment, remote configuration management, and automated compliance checking; operational: POS software that encrypts all cached card data and auto-purges after sync; operational: per POS requirements) means terminals cache data locally during network outages"):
     "operational: standardized POS image deployment, remote configuration management, and automated compliance checking; operational: POS software that encrypts all cached card data and auto-purges after sync",
    # VS-28.2 W1177 — description fragment "(e.g., mandatory customer phone number at POS)"
    ("workflows/VS-28-data-analytics-bi/PA-28.2-data-engineering-and-quality.md",
     "operational: customer phone number at POS)"): None,
    # VS-29.1 W310 — description fragment
    ("workflows/VS-29-master-data/PA-29.1-foundational-masters.md",
     "operational: needs the specific barangay), causing data quality degradation in the customer master"): None,
    # VS-100.3 — stray ** artifacts + swallowed ")" (both genuine mitigations kept)
    ("workflows/VS-100-legal-operations-litigation-ip-management/PA-100.3-corporate-legal-advisory-contracts-risk-governance.md",
     "operational: review SLA and clause standards**; operational: annual refresh and regulatory monitoring (links to VS-22"):
     "operational: review SLA and clause standards; operational: annual refresh and regulatory monitoring (links to VS-22)",
    ("workflows/VS-100-legal-operations-litigation-ip-management/PA-100.3-corporate-legal-advisory-contracts-risk-governance.md",
     "operational: anti-retaliation policy and monitoring (per VS-22; operational: trained investigators and counsel oversight**"):
     "operational: anti-retaliation policy and monitoring (per VS-22); operational: trained investigators and counsel oversight",
    ("workflows/VS-100-legal-operations-litigation-ip-management/PA-100.3-corporate-legal-advisory-contracts-risk-governance.md",
     "operational: security controls (links to VS-27; operational: training and adoption metrics**"):
     "operational: security controls (links to VS-27); operational: training and adoption metrics",
    # VS-115.3 W3638 — junk middle segment dropped (both genuine mitigations kept)
    ("workflows/VS-115-calibration-metrology-and-measurement-traceability-management/PA-115.3-weights-and-measures-compliance-and-analytics.md",
     "operational: MSA and Gage R&R; operational: risk**: Measurement variation larger than tolerance produces wrong decisions; operational: periodic re-validation"):
     "operational: MSA and Gage R&R; operational: periodic re-validation",
    # VS-118.2 W3697 — junk middle segment dropped (both genuine mitigations kept)
    ("workflows/VS-118-revenue-assurance-pricing-integrity-and-leakage-management/PA-118.2-pricing-promotion-loyalty-and-payment-integrity-monitoring.md",
     "operational: price-integrity monitoring; operational: mismatch risk**: Customer charged wrong price (under or over); operational: override analytics and thresholds"):
     "operational: price-integrity monitoring; operational: override analytics and thresholds",
    # VS-119.2 W3727 — junk middle segment dropped (both genuine mitigations kept)
    ("workflows/VS-119-whistleblower-ethics-and-corporate-integrity-speak-up-program/PA-119.2-investigation-case-management-and-retaliation-protection.md",
     "operational: reporting-obligation assessment; operational: report not filed timely (e; operational: disclosure control"):
     "operational: reporting-obligation assessment; operational: disclosure control",

    # ── second batch: lines that were already bulleted before pass 1 ran ──
    # VS-11.2 W1149 — description fragment with label (pains carry no mitigations)
    ("workflows/VS-11-trade-project-wholesale/PA-11.2-project-sales-and-b2b.md",
     "- operational: complexity**: Multi-store consolidated billing requires sophisticated ERP capability"): None,
    # VS-21.3 W358 — description fragment with label
    ("workflows/VS-21-internal-audit-risk/PA-21.3-specialized-audit-domains.md",
     "- operational: Downtime** — Non-functional cameras during critical incidents"): None,
    # VS-22.1 W1489 — first segment is a description fragment; rebuilt from pain 1/4
    ("workflows/VS-22-compliance-regulatory/PA-22.1-regulatory-permits-and-licenses.md",
     "- operational: downtime**: the BIR e-invoicing system experiences periodic downtime; operational: updates must be deployed quickly across 600 terminals"):
     "- operational: good-faith queued transmission with immediate retransmission upon BIR system recovery; operational: rapid deployment of BIR format updates across 600 terminals",
    # VS-71.1 W2551 — junk trailing segment dropped (genuine mitigation kept)
    ("workflows/VS-71-anti-counterfeit-authentication/PA-71.1-product-authentication-serialization.md",
     "- operational: unique per-unit codes and geographic scan anomaly detection; operational: downtime**: Authentication platform unavailability prevents customer verification"):
     "- operational: unique per-unit codes and geographic scan anomaly detection",
    # VS-100.1 W3257 — stray trailing "**" removed
    ("workflows/VS-100-legal-operations-litigation-ip-management/PA-100.1-legal-matter-case-outside-counsel-management.md",
     "- operational: docket/calendar discipline and triage SLA; operational: conflicts check (W3275)**"):
     "- operational: docket/calendar discipline and triage SLA; operational: conflicts check (W3275)",
}

BOUNDARY = "; operational:"


def balance_parens(line):
    """Insert ')' at '; operational:' boundaries (and at EOL) where depth > 0.

    Returns the repaired line, or None if the line ever goes negative (extra ')')
    — those cases are owned by the surgical table. Safe only when every inserted
    ')' follows an unclosed '(' opened earlier in the line.
    """
    depth = 0
    out = []
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth < 0:
                return None  # extra closer — surgical territory
        if line.startswith(BOUNDARY, i) and depth > 0:
            out.append(")")
            depth -= 1
            out.append(BOUNDARY)
            i += len(BOUNDARY)
            continue
        out.append(ch)
        i += 1
    if depth > 0:
        out.append(")")
        depth -= 1
    return "".join(out) if depth == 0 else None


def fix_file(path, rel, write):
    lines = open(path, encoding="utf-8").readlines()
    changed = 0
    in_controls = False
    out = []
    for line in lines:
        s = line.rstrip("\n")
        stripped = s.strip()

        # ── (5) Pain-Points bullet written as a table row (PA-137.2) ──
        if stripped.startswith("| **Stale-SDS risk**:") and "expiry tracking" in stripped:
            s = "- " + stripped.lstrip("| ").rstrip(" |")
            changed += 1

        # ── (4) mangled bold labels: '- **Label":' → '- **Label**:' ──
        m = re.match(r"^(\s*-\s*\*\*[^*]+)\"(:\s)", s)
        if m and s.count("**") % 2 == 1:
            s = re.sub(r"^(\s*-\s*\*\*[^*]+)\"(:\s)", r"\1**\2", s)
            changed += 1

        if s == "### Controls":
            in_controls = True
            out.append(line)
            continue
        if in_controls and (s.startswith("#") or s.startswith("---") or stripped == ""):
            in_controls = False
            out.append(line)
            continue
        if in_controls:
            # ── (3) surgical replacements / drops (also matches already-bulleted
            #    variants: normalize the leading '- ' before lookup) ──
            probe = s[2:] if s.startswith("- ") else s
            key = (rel, probe)
            if key in SURGICAL:
                new = SURGICAL[key]
                if new is None:
                    changed += 1
                    continue  # drop the junk line entirely
                s = new
                changed += 1
            # ── (1) bullet-prefix dangling operational: lines ──
            if s.startswith("operational:") and not s.startswith("- "):
                s = "- " + s
                changed += 1
            # ── (2b) stray '**' artifacts never legitimately appear inside a
            #    Controls bullet (they are pain-point bold leakage); strip them ──
            if s.startswith("- ") and "**" in s:
                s = s.replace("**", "")
                changed += 1
            # ── (2) paren balance at '; operational:' boundaries / EOL ──
            if s.startswith("- ") and s.count("(") != s.count(")"):
                b = balance_parens(s)
                if b is not None:
                    s = b
                    changed += 1
        out.append(line if s + "\n" == line else s + "\n")
    if write and changed:
        open(path, "w", encoding="utf-8").writelines(out)
    return changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="report only; exit 1 if changes pending")
    args = ap.parse_args()

    total = 0
    files = sorted(glob.glob(os.path.join(WF, "VS-*", "PA-*.md")))
    for path in files:
        rel = os.path.relpath(path, MC)
        total += fix_file(path, rel, write=not args.check)
    print(f"{'PENDING' if args.check else 'APPLIED'} repairs: {total} across {len(files)} PA files")
    if args.check and total:
        sys.exit(1)


if __name__ == "__main__":
    main()
