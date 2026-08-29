#!/usr/bin/env python3
"""
audit-semantic-anchors.py — semantic-sample anchor guard (validator Check 62).

Consistency review #44 (2026-08-29) performed the bounded semantic-correctness
sample audit: 40 workflows randomly drawn (seed 44), stratified 5-per-family
across the 8 value-stream families, audited in full — step-sequence logic,
per-step Duration plausibility vs the described activity, RACI role
feasibility vs the org chart, and statutory statements inside step prose.
36 of 40 verified semantically sound, including every statutory base checked
(DOLE 174 labor-only-contracting, RA 4136 PDL/restriction codes, DENR CCO
2013-24 lead-in-paint at 90 ppm, TRAIN-law payroll tables, point-of-sale VAT
recognition) and the volume chains (W1627's 280/store × 200 = 56,000/month and
2 min × 56,000 ≈ 22,400 h/yr; W31's 35,000 × 204 = 7.2M SKU-locations and
140,000 SKU-DC; W614's §1.1-anchored feed volumes). Four defects repaired:

  * W264 — Participants counts 'Category Manager (6), Buyer (8)' were stale
    vs the §13.1 register (5 Category Managers, 10 Buyers incl. Senior);
  * W1777 — the in-house-installment interest VAT basis 'as a financial
    service' was wrong (financial-service interest is VAT-exempt under the
    NIRC; the 12% holds because the interest forms part of the gross selling
    price);
  * W253 — '~10,000 new loyalty enrollments/month' was impossible against
    the data-volumes §1.1 customer-registration anchor (~150/day ≈ 4,500/
    month, of which loyalty sign-ups are the bulk);
  * W449 — the Controls section's operational line was a mis-paste of the
    regularization-risk prose, not a control; replaced with the actual
    DOLE-174 audit control.

Guard mode (--guard): the four repaired literals must not reappear, and any
Participants-field parenthetical count for a §13.1-anchored merchandising
role must equal the register (Category Managers 5, Buyers 10, Merchandise
Planners 5, Pricing Analysts 4).

Consistency review #49 (2026-08-29) lifted coverage toward the corpus-wide
bar: a corpus-wide statutory-citation census (110 distinct forms) plus a
200-workflow stratified batch (seed 5050, excluding the 481 already
audited; see semantic-audit-coverage.txt) brought full-read coverage to
681 of 5,363 workflows. Repairs: 4 "RR No./Revenue Regulation(s) No.
19-2020" spelling variants and 17 bare "RR 19-2020" transfer-pricing
mis-citations → RR 02-2013 (house TP canon); "RA 9160 as amended by
RA 10121" → RA 10365 and RA 11521 (AMLA amendments; RA 10121 is the
DRRM Act, whose two live DRRM usages are correct); W269's RACI R-column
realigned to the prose actors (five steps); W2141's quarterly
warranty-partner review given an internal Accountable (CFO, not the
external Insurance Partner); 11 "BFS"/"BFSR" spots → BPS / DTI-BPS (the
Bureau of Philippine Standards' acronym is and was BPS — including the
inverted "(BFS, formerly BPS)" note — and "DOE Bureau of Fire Standards
and Regulations" does not exist; VS-175 anchors cylinder re-qualification
to DTI-BPS per RA 11592). Each retired literal above is teeth-verified.
"""
import argparse, glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(REPO, "01-model-company", "workflows")

RETIRED_LITERALS = [
    "Category Manager (6), Buyer (8)",
    "subject to VAT (12%) as a financial service",
    "~10,000 new loyalty enrollments/month",
    "operational: regularization of thousands of workers",
    "| Participants (field) |",
    "200 stores × ~5,000 replenishment orders/month",
    "**Absb-erosion risk**",
    "(DOLE DO 174 Compliance)",
    "DTI DAO 2",
    "RR 19-2020",
    "No. 19-2020",
    "RA 11199",
    "per DAO 198",
    "amended by RA 10121",
    "DTI/BFS",
    "BFS/DTI",
    "DENR/BFS",
    "(BFS, formerly BPS)",
    "PS Mark from BFS",
    "BFS may cite",
    "/BFSR",
    "Bureau of Fire Standards",
    "to HR. | Store Manager | HR Admin |",
    "in the system. | Security Guard |",
    "attendance profile. | Vendor Account Mgr |",
    "their payroll. | Store Manager | HR Admin |",
    "upon offboarding. | HR Admin | HR Director |",
    "| VP Merchandising | Insurance Partner |",
]
CLIP_RE = re.compile(r'auto-\w+ of "(logies|logy[^"s/]|countant)')
FOOTPRINT_CLIP_RE = re.compile(r'auto-\w+ of "print([^"]*)" \(replaces manual Step (\d+)\)')
ROLE_COUNTS = [("Category Manager", 5), ("Buyers", 10), ("Buyer", 10),
               ("Merchandise Planners", 5), ("Pricing Analysts", 4)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guard", action="store_true")
    args = ap.parse_args()
    hits = []
    files = sorted(glob.glob(os.path.join(WORKFLOWS, "VS-*", "PA-*.md")))
    for f in files:
        text = open(f, encoding="utf-8").read()
        rel = os.path.relpath(f, REPO)
        for lit in RETIRED_LITERALS:
            if lit in text:
                hits.append(("retired-literal", rel,
                             text[:text.find(lit)].count("\n") + 1, lit))
        for m in CLIP_RE.finditer(text):
            hits.append(("clipped-keyword", rel,
                         text[:m.start()].count("\n") + 1,
                         f'automation keyword clip "{m.group(1)}"'))
        for m in FOOTPRINT_CLIP_RE.finditer(text):
            stepn = m.group(2)
            blk = text[text.rfind("## W", 0, m.start()):]
            sm = re.search(r"^\| " + stepn + r" \| (.+?) \|", blk, re.M)
            if sm and "footprint" in sm.group(1).lower():
                hits.append(("clipped-keyword", rel,
                             text[:m.start()].count("\n") + 1,
                             f'footprint clip "print{m.group(1)[:30]}"'))
        for m in re.finditer(r"^\| \*\*Participants\*\* \| (.+?) \|$", text, re.M):
            row = m.group(1)
            for role, n in ROLE_COUNTS:
                pm = re.search(re.escape(role) + r"\s*\((\d+)\)", row)
                if pm and int(pm.group(1)) != n:
                    hits.append(("participant-count", rel,
                                 text[:m.start()].count("\n") + 1,
                                 f"{role} count {pm.group(1)} != register {n}"))
    for kind, rel, line, detail in hits:
        print(f"{kind}: {rel}:{line}: {detail}")
    print(f"audit-semantic-anchors: {len(hits)} hit(s) across {len(files)} PA files")
    if args.guard:
        sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
