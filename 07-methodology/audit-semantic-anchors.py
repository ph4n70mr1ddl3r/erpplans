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

Consistency review #50 (2026-08-29) added the general keyword-quote integrity
rules after the 104-workflow batch-7 read exposed the clip family at its true
extent: every `System … of "QUOTE" (replaces manual Step N)` bullet must quote
text that (a) actually appears in the referenced step's Activity cell
(containment — catches the 50 review #45/#47 '-logy' mis-repairs that wrote
"technology" where the step word was Metrology/methodology/typology/toxicology/
genealogy/apology) and (b) appears at a word boundary in at least one
occurrence (catches the 884 mid-word clips: account(s)/discount(s)→count(s),
profile→file, catalog→log, center→enter, analogous→logous, … — the class the
exact-literal clip regexes had only piecemeal covered). Hand-authored
noun-phrase summary bullets (adjudicated, semantically sound vintage style)
are allowlisted per (file, workflow).
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
    # review #50 batch-7 repairs
    "1 LP analyst per region (~10–12 LP analysts chain-wide)",
    "Supply Chain team (31 at HQ)",
    "(personnel safety logs)",
    "~20–30 RFQs per month",
    "× 10 groups = 5 hours/day",
    "~5–10 tonnes of recyclable material per store/month",
    # review #51 batch-8 repairs
    "- operational: as evidence",
    "- operational: (eFPS) experiences frequent downtime",
    "- operational: is not always accessible or up-to-date",
    "NOLCO carryforward period is 3 years for small taxpayers",
    "Labor Code Article 294",
    "130% for rest days and holidays",
    "PHP 500K–20M; represents ~5–8% of total revenue",
    "SALSBAC",
    "archived accounting data (W15.3)",
    "~100–150 new hires",
    "~200 new hires/month",
    "~15–25 new hires/month",
    "1.5 hours × 4,500 employees",
    "- **Total: ~140–160 hours/year**",
    "(18 regular holidays",
    # review #52 batch-9 repairs
    "Store staff (6,000)",
    "~35-person Finance team",
    "instead of 0.00236, a small rounding error",
    "- operational: and physical reality",
    "| IT Auditor | BPO | 2 days |",
    "~500–800 qualifying transactions/day",
    "(10th and 25th of following month)",
    "per W1324 (DOLE DO 174 compliance)",
    "notice per DO 174 requirements",
    "~1.2–1.5 GWh/store",
    "175,000–220,000 tonnes",
    "~1M loyalty members",
    "~1–2 per store/month",
    "D.O. 53-04",
    # review #53 batch-10 repairs
    "General Affiliate Notice",
    "(GIS, AFS, GAN",
    "10-20 per store per day",
    "2,000-4,000 orders/day",
    "- operational: to file public financial statements",
    "~150–250 exceptions/week",
    "30-person Supply Chain team",
    "~84,000 returns/month",
    "~84,000 product returns per month",
    "(double the chain average)",
    "~55 license expirations/year",
    "55% of revenue from ~600,000 loyalty members",
    "per RA 9275",
    "RA 9275 refrigerant",
    "ODS/RA 9275",
    "transfer-prricing",
    # review #54 batch-11 repairs
    "30 staff × 200 stores",
    "~600–800 separations/year",
    "~50–70 separations/month",
    "≈ 550–730 hours/year",
    "~200–300 new vendor assessments/year",
    "DIY segment (55% of revenue)",
    "~60 stores in typhoon-prone Visayas",
    # review #55 batch-12 repairs
    "~200–400 customer complaints per store per month",
    "~2,800 in-store return refunds",
    "~5,000–6,000 refund transactions/month",
    "~50–80 off-cycle payments/month",
    "~800–1,000 active contracts",
    "~5–10 active sabbaticals",
    "assuming 5-10 active programs",
    "~15–20 active 3PL contracts",
    "(15–20 providers × 2–3 hours",
    "15–20 × 3–5 hours = 45–100 hours",
    "~3,000–4,400 SKU-location",
    "~PHP 3–5M in fixtures/equipment",
    "~12 categories × tens of attributes",
    # review #56 batch-13 repairs
    "~20–40/DC/month",
    "~1,825 hazmat receiving events",
    "= ~304 hours/year",
    "= ~520 hours/year",
    "1601-E,",
    "(~25,000–50,000 total)",
    "per DOLE 174",
    "(DOLE Department Order 174) distinguishes",
    "~150 DC staff on duty per shift",
    "~2–3 hours/day at 30–40 selections",
    "= ~2,000 store-hours/month",
    "~5 hours/month on daily reconciliation",
    "~12,000–15,000 store-hours/year",
    "5-day standard onboarding",
    "~250–450 hours/year",
    "~15 min/day per store on pallet sorting",
    "~250–350 component structures/year",
    "~20–30 component structures/month",
    "× 3 hours = ~60 hours/quarter",
    "~15–20 days/quarter",
    "~400–500 deliveries/day",
    "**~360 hours/year**",
    "revertion",
    "ERB",
]
CLIP_RE = re.compile(r'auto-\w+ of "(logies|logy[^"s/]|countant)')
FOOTPRINT_CLIP_RE = re.compile(r'auto-\w+ of "print([^"]*)" \(replaces manual Step (\d+)\)')
ROLE_COUNTS = [("Category Manager", 5), ("Buyers", 10), ("Buyer", 10),
               ("Merchandise Planners", 5), ("Pricing Analysts", 4)]

BULLET_RE = re.compile(r'- System [^"]*?of "([^"]+)" \(replaces manual Step (\d+)([a-z]?)\)\.')
STEP_RE = re.compile(r"^\|\s*(\d+)([a-z]?)\s*\|")

# Hand-authored noun-phrase summary bullets (vintage generator style): the quote
# is a descriptive noun phrase, not a verbatim step span — adjudicated sound.
QUOTE_STYLE_ALLOWLIST = {
    ("PA-116.2-bond-application-issuance-tracking-and-encumbrance-management.md", "W3655"),
    ("PA-117.3-market-surveillance-compliance-monitoring-and-certification-analytics.md", "W3687"),
    ("PA-17.3-tax-and-statutory.md", "W590"),
    ("PA-17.3-tax-and-statutory.md", "W1503"),
    ("PA-18.1-cash-positioning-and-forecasting.md", "W234"),
    ("PA-18.1-cash-positioning-and-forecasting.md", "W323"),
    ("PA-15.1-invoice-processing-and-matching.md", "W461"),
    ("PA-38.3-financing-reconciliation-settlement.md", "W1785"),
    ("PA-40.2-project-cost-tracking.md", "W1826"),
    ("PA-46.1-government-registration-qualification.md", "W1950"),
    ("PA-26.3-insurance-claims-and-policy-management.md", "W860"),
    ("PA-10.1-ecommerce-platform-operations.md", "W1185"),
}


def steps_header_hits(lines):
    """Structural rule (review #51): a steps table header row must not directly
    follow a field-table row — the W4762 signature (missing '### Steps' or any
    phase header between the field table and the steps table)."""
    out = []
    for i, l in enumerate(lines):
        if re.match(r"^\| # \| Activity \|", l):
            prev = next((x for x in lines[:i][::-1] if x.strip()), "")
            if prev.startswith("| **") and "**" in prev:
                out.append((i + 1, "steps table follows field row with no section header"))
    return out


def quote_integrity_hits(fname, lines):
    """Containment + word-boundary check for step-quoting automation bullets."""
    out = []
    cur = None
    steps = {}
    in_steps = False
    for i, l in enumerate(lines, 1):
        if re.match(r"^### Steps\b", l):
            in_steps = True
            continue
        m = re.match(r"^#{2,3} (W\d+[A-Z]?)[. ]", l)
        if m:
            cur = m.group(1)
            in_steps = False
            continue
        if l.startswith("#"):
            # named h3 sub-sections (e.g. '### Vendor Rebate Dispute Resolution')
            # end the current workflow's step scope
            cur = None
            in_steps = False
            continue
        if in_steps:
            sm = STEP_RE.match(l)
            if sm and cur:
                steps[(cur, sm.group(1), sm.group(2))] = l
        bm = BULLET_RE.search(l)
        if bm and cur:
            if (fname, cur) in QUOTE_STYLE_ALLOWLIST:
                continue
            quote, snum, sltr = bm.group(1), bm.group(2), bm.group(3)
            st = steps.get((cur, snum, sltr), "")
            if not st:
                continue
            stn = re.sub(r"\*\*", "", st)
            stw = re.sub(r"\s+", " ", stn)
            q = quote.rstrip("…").rstrip()

            def contained(s):
                s2 = re.sub(r"\s+", " ", s)
                return bool(s) and (s in stn or s.lower() in stn.lower()
                                    or s2 in stw or s2.lower() in stw.lower())

            if not contained(q):
                if not ("…" in quote and contained(quote.split("…")[0].rstrip())):
                    out.append((i, f'quote not in Step {snum}{sltr}: "{q[:60]}"'))
                    continue
            # word-boundary: at least one occurrence must not sit inside a word
            hay, needle = (stn, q) if q in stn else (stn.lower(), q.lower())
            ok = False
            for mm in re.finditer(re.escape(needle), hay):
                s, e = mm.start(), mm.end()
                if (s == 0 or not hay[s - 1].isalnum()) and (e >= len(hay) or not hay[e].isalnum()):
                    ok = True
                    break
            if not ok:
                out.append((i, f'mid-word clip in Step {snum}{sltr}: "{q[:60]}"'))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guard", action="store_true")
    args = ap.parse_args()
    hits = []
    files = sorted(glob.glob(os.path.join(WORKFLOWS, "VS-*", "PA-*.md")))
    for f in files:
        text = open(f, encoding="utf-8").read()
        rel = os.path.relpath(f, REPO)
        fname = os.path.basename(f)
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
        for line, detail in quote_integrity_hits(fname, text.splitlines()):
            hits.append(("quote-integrity", rel, line, detail))
        for line, detail in steps_header_hits(text.splitlines()):
            hits.append(("steps-header", rel, line, detail))
    for kind, rel, line, detail in hits:
        print(f"{kind}: {rel}:{line}: {detail}")
    print(f"audit-semantic-anchors: {len(hits)} hit(s) across {len(files)} PA files")
    if args.guard:
        sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
