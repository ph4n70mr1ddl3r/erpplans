#!/usr/bin/env python3
"""
add-expansion-anchors.py — One-time extension of internal-controls-matrix.md with
"Expansion & Legacy-Block Domain Controls" (C18–C25): one anchor control per value
stream whose workflows had ZERO coverage in the controls register.

The v8 register extension (2026-06-27) added one anchor control per gap-analysis value
stream (VS-89–VS-192, CTL-68–171) but left 68 value streams across the Core
(VS-02/06/08/11/12/14/21/23–26/28/30/31), Expansion (VS-32–48, VS-53–78) and Statutory
(VS-79–88) blocks with no register row citing any of their workflows — the honest backlog
tracked by validator Check 21 ("the Expansion block is outside the register"). This pass
extends the register to full value-stream coverage: CTL-172–CTL-239, one anchor per
uncovered value stream, grouped by family in the same house style as C10–C17.

Verification built in: every W-reference must resolve to a real workflow header (Check 7's
rule) and every Req Ref must exist in erp-requirements.md (733 IDs). Running
07-methodology/backfill-controls.py afterwards injects the CTL-XX references into the
mapped workflows' Controls sections.

Usage:
    python3 07-methodology/add-expansion-anchors.py --dry-run   # print planned block
    python3 07-methodology/add-expansion-anchors.py             # write changes
"""
import re
import sys

REPO = __file__.rsplit("/07-methodology/", 1)[0]
MATRIX = f"{REPO}/01-model-company/internal-controls-matrix.md"
REQS = f"{REPO}/01-model-company/erp-requirements.md"

# Hand-authored anchor controls: (vs, type, objective, activity, owner, workflows, req_refs)
# Workflows were chosen as each VS's control-critical points (reconciliations, statutory
# filings, verifications), preferring workflows whose Controls sections are still pure
# boilerplate (Check 21 metric c) where the control genuinely lands there.
CONTROLS = [
    # --- C18. Plan & Source ---
    (2,  "D", "Ensure demand-plan integrity & replenishment authorization",
     "Monthly S&OP consensus sign-off with forecast-accuracy (MAPE/bias) tracking; store auto-replenishment overrides logged with reason codes and reviewed weekly; seasonal and disaster pre-positioning plans approved before stock commitment",
     "VP Supply Chain", ["W133", "W596", "W835", "W1533", "W1355"], ["SCP-001", "SCP-002"]),
    (41, "P", "Prevent non-compliant private-label products from reaching shelf",
     "Factory qualification audit and first-article approval before first PO; product and packaging specification sign-off per SKU; regulatory testing/certification renewals tracked with listing blocked on lapse; packaging & labeling compliance audited per production batch",
     "Quality Assurance Manager", ["W1831", "W1832", "W1840"], ["PUR-022", "GOV-015"]),
    (45, "D", "Ensure consignment & VMI settlement integrity",
     "Consignment stock physically counted and reconciled to vendor settlement monthly; non-valuated receipts proven-up at settlement; VMI auto-confirmations matched to agreed min/max parameters; multi-entity consignment settlements cross-checked between entities",
     "Category Manager", ["W1926", "W1930", "W1937", "W1948"], ["INV-009", "FIN-018"]),
    (57, "D", "Ensure competitor-price data integrity & price-match governance",
     "Scraped competitor prices validated for like-for-like SKU/UOM before any match decision; intelligence-driven price changes retain the standard approval workflow and audit trail; rapid-response repricing executed within DTI price-change tag rules",
     "Pricing Analyst", ["W2214", "W2215", "W2219", "W2222"], ["POS-006", "MDM-005"]),
    (64, "D", "Ensure markdown & clearance pricing compliance",
     "Markdown triggers execute from sell-through/aging rules with approval thresholds; clearance price overrides require delegated authority; clearance events reconciled financially post-event; vendor markdown allowances claimed against executed markdowns",
     "Merchandising Planner", ["W2390", "W2391", "W2394", "W2395", "W2397"], ["GOV-029", "POS-041"]),
    (67, "D", "Ensure vendor scorecard data quality & performance action",
     "Scorecard KPIs computed from system data with a data-quality audit; strategic vendors reviewed quarterly with documented actions; performance improvement plans tracked to closure; vendor financial-health alerts tied to exposure review",
     "Procurement Manager", ["W2454", "W2459", "W2462", "W2463", "W2465"], ["PUR-008", "MDM-004"]),
    # --- C19. Make & Move ---
    (6,  "D", "Ensure fleet compliance & freight-cost integrity",
     "Route/dispatch adheres to LGU truck-ban ordinances and LTFRB weight limits; fuel consumption reconciled per vehicle against route logs; carrier freight bills audited to contracted rates; 3PL SLA reviews documented with penalties applied",
     "Logistics Manager", ["W196", "W431", "W1315", "W198", "W1166", "W1207"], ["GOV-007", "LOG-001"]),
    (32, "D", "Ensure returns integrity & refund-fraud prevention",
     "Receipt-less returns bounded by policy limits with ID tracking; refunds/credits issued to original tender with exception approval; return disposition matched to vendor claim recovery; return-fraud patterns monitored and flagged",
     "DC Returns Coordinator", ["W1622", "W1625", "W1627", "W1628", "W1630"], ["POS-007", "POS-019"]),
    (56, "D", "Ensure 3PL delivery-partner compliance & performance",
     "Partner screening with driver/vehicle compliance verification before engagement; delivery quality inspected at handover; real-time tracking with SLA compliance monitored on a scorecard and rate-card enforcement at billing",
     "Logistics Manager", ["W2190", "W2192", "W2196", "W2198", "W2199"], ["ECOM-012", "PUR-008"]),
    (61, "D", "Ensure fleet fuel-cost accuracy & fraud prevention",
     "Fuel-card transactions matched per vehicle/driver with exception flags on off-pattern consumption; fuel-efficiency variances investigated; RFID toll accounts reconciled to statements",
     "Fleet Supervisor", ["W2310", "W2311", "W2312", "W2313", "W2319"], ["FIN-064", "GOV-007"]),
    (74, "D", "Ensure jobsite delivery accuracy & site reconciliation",
     "Phased deliveries matched to the approved project schedule with on-site verification and receipt sign-off; damaged/refused material claims documented at placement; project close-out reconciles delivered vs. estimated materials with variance analysis",
     "Logistics Coordinator", ["W2622", "W2625", "W2703", "W2708", "W2709"], ["ECOM-011", "ECOM-004"]),
    (81, "D", "Ensure CIT custody-chain & cash-in-transit integrity",
     "Dual-control skim and CIT handover with seal numbers recorded; GPS-tracked in-transit monitoring with route-adherence alerts; vault counts reconciled to store-declared deposits; counterfeit notes authenticated at deposit",
     "CIT Operations Manager", ["W2801", "W2802", "W2810", "W2811", "W2812", "W2806"], ["POS-009", "IC-005"]),
    # --- C20. Sell & Serve ---
    (8,  "D", "Ensure POS settlement & tender reconciliation completeness",
     "Daily multi-tender reconciliation of POS captures to acquirer/e-wallet settlements with variance triage; cashier over/short tracked with threshold escalation; near-real-time sync completeness reconciled nightly; catch-weight pricing verified against calibrated scales",
     "Store Manager", ["W1425", "W1301", "W1354", "W272", "W525", "W1305"], ["POS-009", "FIN-009"]),
    (11, "D", "Ensure B2B billing & receivable milestone integrity",
     "Project progress billing tied to verified milestones with retention release only on sign-off; contract price-book pricing enforced at order entry with deviation approval; statements auto-issued and disputes resolved within SLA",
     "B2B Sales Manager", ["W163", "W1426", "W1134", "W1117", "W1022"], ["CRM-008", "POS-010"]),
    (12, "D", "Ensure installation quality & warranty registration",
     "Installer/service-partner quality audited with scorecards; punch-list closure and customer walk-through sign-off required before job close; completion certificates register warranty automatically; rework tracked to root cause",
     "Store Manager", ["W213", "W1171", "W1254", "W795"], ["SRV-001", "POS-019"]),
    (14, "D", "Ensure marketing spend & loyalty-fraud control",
     "Campaign spend tracked to budget with ROI attribution; co-op/vendor funds reconciled to agreements; loyalty-fraud patterns monitored with accounts flagged and points frozen on confirmation",
     "Digital Marketing Manager", ["W83", "W677", "W104", "W496", "W565"], ["CRM-001", "CRM-007"]),
    (37, "P", "Prevent premature store go-live",
     "Go-live gated by systems-verification checklist, permit completeness, safety/compliance training validation and cash-float setup sign-off; handover from project to operations documented with an open-issues register",
     "VP Store Operations", ["W1742", "W1751", "W1752", "W1754", "W1760"], ["SCP-012", "POS-085"]),
    (43, "D", "Ensure trade-program benefit & master-data integrity",
     "Tier benefits, early-payment discounts and referral incentives computed from system data with quarterly business reviews documented; account master data quality audited; annual recertification enforced with lapse handling",
     "Account Manager", ["W1879", "W1885", "W1889", "W1890", "W1900"], ["CRM-001", "CRM-008"]),
    (44, "P", "Protect research-participant data & insight validity",
     "Panel/survey data collected under documented consent with RA 10173 safeguards; mystery-shop scoring calibrated and double-blind; competitive intelligence gathered ethically with no competitively-sensitive price coordination",
     "Market Research Analyst", ["W1902", "W1908", "W1911", "W1917"], ["NFR-010", "MDM-032"]),
    (46, "D", "Ensure B2G procurement compliance & collection",
     "PhilGEPS registration kept current; bids governed by procurement-law modes with documented quotations/awards; BIR-compliant billing issued and government collections followed up per aging schedule",
     "Trade Account Manager", ["W1950", "W1959", "W1960", "W1966", "W1967"], ["CRM-009", "PUR-031"]),
    (47, "D", "Ensure subscription billing & dunning integrity",
     "Recurring billing reconciled to active entitlements; failed payments enter dunning with retry rules; cancellations pro-rated per policy; SKU/enrollment-flow changes gated by configuration sign-off",
     "VP Store Operations", ["W1976", "W1982", "W1983", "W1984", "W1986"], ["CRM-024", "SRV-001"]),
    (48, "D", "Ensure retail-media billing & placement delivery",
     "Campaign placements audited against contracted inventory; vendor co-op funding reconciled to agreements; AR collections managed with campaign suspension on delinquency; sales-lift attribution methodology documented and consistent",
     "Marketing Manager", ["W1998", "W2000", "W2010", "W2015", "W2017"], ["FIN-019", "CRM-007"]),
    (53, "D", "Ensure warranty registration & claim integrity",
     "Warranty capture validated at checkout against item/serial master; claims adjudicated against terms with vendor cost recovery where applicable; registration completeness audited for data quality",
     "Customer Service Manager", ["W2118", "W2119", "W2120", "W2123", "W2126"], ["POS-019", "MDM-015"]),
    (55, "D", "Ensure planogram & price-tag compliance",
     "Planogram version control with store acknowledgement; compliance audited via on-site and photo-based remote checks; shelf-label price accuracy audited against the active price file",
     "Merchandising Planner", ["W2170", "W2174", "W2175", "W2176"], ["MDM-023", "MDM-005"]),
    (58, "P", "Prevent coupon & promo-code abuse",
     "Coupon configuration enforces stacking, limit and eligibility rules; redemption validated at tender; vendor-funded programs reconciled to funding agreements; fraud patterns monitored with deactivation controls",
     "Marketing Analyst", ["W2238", "W2241", "W2244", "W2246", "W2247"], ["POS-014", "ECOM-010"]),
    (60, "D", "Ensure omnichannel order-routing accuracy",
     "Routing-engine decisions logged with ATP basis; split/mixed-basket fulfillment orders reconciled to a single financial order; routing exceptions worked to closure within SLA; drop-ship vendor confirmations matched to orders",
     "Ecommerce Operations Manager", ["W2287", "W2288", "W2289", "W2291", "W2294"], ["ECOM-003", "ECOM-005"]),
    (62, "D", "Ensure sample & display asset accountability",
     "Sample inventory tracked with monthly condition inspection; damaged replacements charged or written off with approval; display assets reconciled at seasonal refresh; sample-to-order conversion measured",
     "Merchandising Coordinator", ["W2337", "W2341", "W2342", "W2343"], ["GOV-028", "POS-081"]),
    (63, "D", "Ensure store-communication task closure",
     "HQ directives acknowledged with compliance visible on a dashboard by store; task completion quality audited; emergency communication protocol tested on schedule",
     "Store Operations Director", ["W2359", "W2360", "W2366", "W2368", "W2371"], ["POS-069", "HR-041"]),
    (65, "D", "Ensure marketplace order & settlement reconciliation",
     "Marketplace orders downloaded and processed with inventory allocation per channel strategy; settlements reconciled to platform statements with fee and chargeback validation; listing prices synchronized to the price file",
     "Ecommerce Director", ["W2408", "W2409", "W2412", "W2414"], ["ECOM-013", "ECOM-026"]),
    (66, "D", "Ensure design-service quotation & change-order control",
     "Quotations derived from the standard rate card with approval thresholds; customer approval captured before execution; change orders priced and signed before work proceeds; project status tracked through quality inspection",
     "Project Consultant", ["W2432", "W2434", "W2435", "W2442", "W2448"], ["POS-054", "SRV-001"]),
    (70, "D", "Ensure solar program compliance & delivery",
     "Staff certification tracked before selling/consulting; installation materials staged and delivered with sign-off; net-metering activation documented per LGU/DOE rules; promotional ROI and savings claims validated",
     "Solar Program Manager", ["W2528", "W2530", "W2539", "W2540"], ["MDM-027", "SRV-001"]),
    (75, "P", "Protect mobile-app customer data & release quality",
     "App releases gated by security/privacy review (RA 10173) and performance SLOs; push-notification consent honored with preference management; catalog/price sync integrity monitored with reconciliation alerts",
     "Digital Product Manager", ["W2647", "W2650", "W2651", "W2652"], ["NFR-010", "NFR-032"]),
    (77, "D", "Ensure project staging & price-lock integrity",
     "Phased staging triggers only from approved project schedules; price-lock/escalation terms enforced at invoicing; on-site material receipt verified; consumption-vs-estimate variance analyzed at close-out",
     "Trade Sales Manager", ["W2697", "W2702", "W2703", "W2709", "W2710"], ["ECOM-011", "ECOM-004"]),
    (78, "D", "Ensure green-product claim substantiation",
     "Green certifications verified before product listing and before any marketing claim; BERDE/LEED project documentation support accurate and retained; regulatory changes monitored for continuing claim validity",
     "Sustainability Coordinator", ["W2718", "W2724", "W2736", "W2738"], ["ESG-009", "GOV-008"]),
    (82, "D", "Ensure MSME micro-wholesale credit & order integrity",
     "KYC onboarding completed before first credit order; route-seller and app/WhatsApp orders validated with credit check at capture; cluster/group-buy orders reconciled to deliveries; micro-wholesale pricing governed per segment",
     "MSME Sales Manager", ["W2825", "W2829", "W2830", "W2833", "W2834"], ["PUR-023", "CRM-008"]),
    # --- C21. Finance ---
    (34, "P", "Prevent unauthorized non-merchandise spend",
     "Purchase requisitions follow the approval matrix with service contracts renegotiated before auto-renewal; expense cards reconciled monthly against policy limits; SLA performance documented as a condition of payment",
     "Procurement Manager", ["W1675", "W1676", "W1678", "W1685", "W1686"], ["FIN-064", "HR-016"]),
    (38, "D", "Ensure consumer-financing settlement & compliance",
     "Financier settlements reconciled daily to POS originations with exception handling; MDR fees tracked and reported; BSP regulatory monitoring documented; installment VAT/WHT computed per rule",
     "Treasury Manager", ["W1777", "W1782", "W1783", "W1784", "W1785"], ["FIN-045", "CRM-008"]),
    (39, "D", "Ensure vendor rebate accuracy & recognition",
     "Rebate accruals estimated per agreement terms and trued-up to vendor statements; volume thresholds tracked automatically; income recognized as earned per PFRS; markdown allowances and damage claims recovered",
     "VP Merchandising", ["W1787", "W1788", "W1789", "W1792", "W1804"], ["FIN-019", "PUR-020"]),
    (40, "P", "Ensure capex authorization & commitment control",
     "Capex requests follow the tiered approval matrix with business-case evaluation; commitments tracked against budget with revisions re-approved; partial turnovers capitalized with supporting documentation",
     "FP&A Manager", ["W1812", "W1813", "W1814", "W1815", "W1821", "W2749"], ["FIN-016", "FIN-055"]),
    (54, "D", "Ensure stored-value float & liability integrity",
     "Gift-card issuance/redemption tracked to serial with daily float counts and variance escalation; breakage recognized per policy; compliance terms monitored; corporate bulk issuance documented against PO",
     "Gift Card Program Manager", ["W2142", "W2143", "W2145", "W2148", "W2150"], ["POS-015", "CRM-001"]),
    (68, "D", "Ensure trade-credit exposure control",
     "New accounts scored and limits approved per the authority matrix; real-time limit monitoring blocks over-limit orders with override logging; periodic reviews with bureau-data refresh; insurance coverage assessed against exposure",
     "Credit Manager", ["W2478", "W2480", "W2484", "W2486", "W2487"], ["CRM-003", "CRM-008"]),
    (72, "D", "Ensure shared-services chargeback integrity",
     "Cost pools identified and compiled monthly per documented allocation basis; chargebacks reconciled to cost pools with variance management; IC invoices generated and settled on schedule; pool audits documented",
     "Financial Controller", ["W2574", "W2575", "W2576", "W2579", "W2580", "W2583"], ["IC-001", "IC-005"]),
    (79, "D", "Ensure BIR tax compliance & filing integrity",
     "VAT ledgers reconciled to GL before 2550M/Q filings via eFPS with e-payment validation; EIS transmission completeness reconciled daily; EWT computations calendar-tracked through the 1601 series; VAT-exempt/zero-rated sales supported by certificates; POS/CAS accreditation current",
     "Tax Manager", ["W2753", "W2755", "W2756", "W2757", "W2760", "W2761"], ["FIN-006", "FIN-007"]),
    (80, "D", "Ensure card/e-wallet settlement & chargeback control",
     "Daily settlement files ingested and posted to GL with settlement-to-capture reconciliation and exception triage; terminal batch closes validated; chargeback evidence compiled within scheme windows; MID/MCC hierarchy mapped to entities",
     "Payment Operations Manager", ["W2777", "W2784", "W2785", "W2786", "W2787", "W2788"], ["POS-049", "FIN-009"]),
    # --- C22. People ---
    (83, "D", "Ensure occupational-health record & claim compliance",
     "Work-relatedness determinations documented for EC claims with SSS/PhilHealth coordination; DOLE annual medical report and OHS statistics compiled; medical records kept confidential under consent per RA 10173; clinic pharmacy stock reconciled",
     "Occupational Health Manager", ["W2850", "W2852", "W2853", "W2855", "W2856", "W2863"], ["HSE-005", "GOV-043"]),
    (84, "D", "Ensure labor-relations statutory compliance",
     "CBA negotiation, drafting, ratification and DOLE registration followed with economic costing before sign-off; union dues check-off only on written authorization; grievances tracked through the steps with documentation; LMC governance recorded",
     "Labor Relations Director", ["W2874", "W2876", "W2877", "W2879", "W2881"], ["HR-014", "GOV-040"]),
    # --- C23. Asset & Infrastructure ---
    (20, "D", "Ensure facility compliance & lease-cost integrity",
     "LGU permit/RPT inspections current per site; CAM reconciliations reviewed and challenged with documentation; preventive maintenance executed with inspection records; construction turnover accepted against snag lists",
     "Facilities Manager", ["W430", "W1183", "W240", "W117", "W1295"], ["GOV-006", "GOV-003"]),
    (35, "D", "Ensure fixed-asset register accuracy",
     "Asset tags applied at capitalization with annual wall-to-wall verification and rolling spot checks; transfers and disposals documented with approval; register reconciled to GL and the insurance schedule",
     "Fixed Asset Accountant", ["W1690", "W1692", "W1697", "W1703", "W1706", "W1707"], ["FIN-011", "MDM-027"]),
    (42, "D", "Ensure lease-administration & PFRS 16 integrity",
     "Key dates tracked with renewal/option notices served on time; rent, CAM and percentage-rent reconciled to lease terms; abatements enforced; PFRS 16 month-end processing and disclosures reviewed",
     "VP Real Estate", ["W1855", "W1862", "W1864", "W1865", "W1872"], ["FIN-052", "GOV-003"]),
    (59, "D", "Ensure controlled store-closure execution",
     "Closure board-approved with regulatory/LGU deregistration completed; inventory liquidated with variance review; fixed assets recovered or disposed with approval; lease termination documented; employee separation executed per PH labor law",
     "Store Closure Project Manager", ["W2264", "W2269", "W2270", "W2271", "W2272"], ["POS-086", "PROP-001"]),
    # --- C24. Technology & Data ---
    (28, "D", "Ensure BI data governance & reporting integrity",
     "ETL jobs monitored with exception handling and data-quality gates before dashboard refresh; self-service access provisioned by role with training; executive reporting package reconciled to source systems before distribution",
     "BI Analytics Manager", ["W879", "W880", "W881", "W882", "W885"], ["RPT-001", "NFR-038"]),
    (30, "D", "Ensure responsible AI/ML & pilot governance",
     "AI/ML models governed with bias audit and ethical review before deployment; demand-forecast model accuracy monitored with retraining triggers; innovation pilots stage-gated with KPI review before scale-up",
     "IT Innovation Lead", ["W203", "W689", "W690", "W1206"], ["INV-025", "NFR-035"]),
    # --- C25. Governance & Assurance ---
    (21, "D", "Ensure audit-plan execution & remediation",
     "Risk-based audit plan executed with documented fieldwork; issues tracked to corrective-action closure with board reporting; specialized audits (ABC, capex, rebate, revenue assurance) performed per plan",
     "Internal Audit Manager", ["W121", "W159", "W333", "W344", "W346", "W348"], ["GOV-002", "NFR-007"]),
    (23, "D", "Ensure shrinkage detection & case governance",
     "Exception-based monitoring across cash handling, refunds, BOPIS staging and consignment stock; investigations documented in case management; organized-retail-crime coordination with law enforcement; recoveries accounted",
     "Regional LP Manager", ["W837", "W839", "W841", "W842", "W1248", "W1249"], ["POS-050", "GOV-020"]),
    (24, "D", "Ensure OHS compliance & incident management",
     "Safety certifications and training tracked with expiry alerts; workplace inspections scheduled and closed on time; incidents investigated with WAIR/AMR statutory reporting; hazmat spill response drilled",
     "Safety Officer", ["W140", "W141", "W238", "W436", "W655", "W758"], ["GOV-004", "GOV-034"]),
    (25, "D", "Ensure ESG data integrity & disclosure",
     "GHG, water and energy metrics collected with documented methodology and evidence retained; sustainable-sourcing claims verified including chain-of-custody; disclosures reviewed for accuracy before publication",
     "Sustainability Lead", ["W192", "W195", "W693", "W1262", "W1529"], ["ESG-008", "ESG-006"]),
    (26, "D", "Ensure BCP readiness & insurance recovery",
     "BIA maintained with RTO/RPO targets; tabletop and DR-failover tests executed with results documented; damage and business-interruption claims documented, filed and recovered to GL",
     "IT Director", ["W853", "W858", "W860", "W864", "W1204", "W1322"], ["BCP-003", "NFR-013"]),
    (31, "D", "Ensure supplier quality & product-safety verification",
     "Vendor quality audits scheduled with VCAR closure tracked; first-article inspection before listing; electrical-safety and standards certification verified per SKU; import pre-shipment verification documented",
     "Quality Manager", ["W1602", "W1606", "W1609", "W1610", "W1611", "W1612"], ["PUR-017", "PUR-024"]),
    (33, "D", "Ensure strategy-to-budget alignment",
     "Annual targets cascade to store/department operating plans with board budget approval; mid-year recalibration documented; weekly KPI flash reconciled to financial systems",
     "CFO", ["W1647", "W1648", "W1650", "W1651", "W1654"], ["FIN-015", "RPT-001"]),
    (36, "D", "Ensure corporate-governance compliance",
     "Board materials distributed with minutes approved and resolutions authenticated; SEC annual filings current; related-party transactions identified and disclosed; whistleblower channel operated with independence",
     "Corporate Secretary", ["W1715", "W1716", "W1717", "W1718", "W1720", "W1733"], ["GOV-001", "GOV-038"]),
    (69, "D", "Ensure typhoon-response protocol execution",
     "Pre-positioning and readiness checklists executed before landfall; emergency pricing freeze activated per RA 7581 with DTI compliance; post-event damage assessments documented for insurance claims; employee welfare and deployment tracked",
     "Store Manager", ["W2502", "W2503", "W2507", "W2508", "W2515"], ["GOV-030", "GOV-011"]),
    (71, "D", "Ensure anti-counterfeit program integrity",
     "High-risk SKUs serialized with authentication verified at receiving and key control points; seizures documented with law-enforcement/regulatory reporting; marketplace takedowns tracked; customer restitution processed",
     "Loss Prevention Manager", ["W2550", "W2554", "W2558", "W2561", "W2562", "W2563"], ["INV-008", "POS-050"]),
    (73, "D", "Ensure store-waste regulatory compliance",
     "Waste segregated at store with hazardous streams (paint/chemical/e-waste) disposed only via DENR-accredited handlers with manifests; recycling revenue reconciled to the waste ledger; reduction targets tracked",
     "Sustainability Coordinator", ["W2598", "W2599", "W2603", "W2605", "W2606"], ["ESG-008", "GOV-008"]),
    (76, "D", "Ensure multi-LGU license compliance",
     "Permit/license renewal calendar with expiry alerts escalating ahead of lapse; fire-safety, sanitary and signage permits current per site; regulatory changes impact-assessed; compliance dashboard maintained",
     "Legal Compliance Officer", ["W2670", "W2672", "W2675", "W2677", "W2680"], ["NFR-017", "REG-002"]),
    (85, "D", "Ensure mandatory-discount & VAT-exemption compliance",
     "SC/PWD/solo-parent ID validation at POS with purchase-book recording; discount computation and stacking rules configured per RA 9994/10754/8972 and reviewed on change; abuse monitoring; zero-rated/exempt sales supported by certificates",
     "Tax Accountant", ["W2897", "W2898", "W2899", "W2900", "W2905", "W2906"], ["POS-014a", "FIN-006"]),
    (86, "D", "Ensure AML/KYC & sanctions compliance",
     "Customers risk-tiered with KYC due-diligence documentation and periodic refresh; sanctions/watchlist screening at onboarding and on list updates; covered transactions (≥PHP 500K single-day cash) detected with CTRs filed; STRs filed with AMLC within statutory windows",
     "MLRO / Compliance Officer", ["W2921", "W2924", "W2926", "W2929", "W2931", "W2932"], ["COM-009", "NFR-010"]),
    (87, "D", "Ensure customs classification & valuation compliance",
     "HS/AHTN classifications assigned per SKU with advance rulings sought where material; customs value captures assists and royalties; rules-of-origin documented for FTA preference claims; classification discrepancies reconciled",
     "Trade Compliance Specialist", ["W2945", "W2946", "W2947", "W2948", "W2949", "W2952"], ["SCP-015", "FIN-013"]),
    (88, "D", "Ensure records-retention & legal-hold compliance",
     "Retention schedule by record class (BIR/SEC/DOLE/NPC) enforced with event-driven clock management; legal holds issued and released with defined scope; disposition only after review and approval with certificates of destruction; e-invoice/receipt archives BIR-compliant",
     "Records Manager", ["W2975", "W2977", "W2978", "W2979", "W2980"], ["DOC-005", "POS-037"]),
]

FAMILIES = [
    ("C18", "Plan & Source", [2, 41, 45, 57, 64, 67]),
    ("C19", "Make & Move", [6, 32, 56, 61, 74, 81]),
    ("C20", "Sell & Serve", [8, 11, 12, 14, 37, 43, 44, 46, 47, 48, 53, 55, 58, 60, 62, 63, 65, 66, 70, 75, 77, 78, 82]),
    ("C21", "Finance", [34, 38, 39, 40, 54, 68, 72, 79, 80]),
    ("C22", "People", [83, 84]),
    ("C23", "Asset & Infrastructure", [20, 35, 42, 59]),
    ("C24", "Technology & Data", [28, 30]),
    ("C25", "Governance & Assurance", [21, 23, 24, 25, 26, 31, 33, 36, 69, 71, 73, 76, 85, 86, 87, 88]),
]


def main():
    dry = "--dry-run" in sys.argv
    import glob, os
    # --- verification: workflows and reqs exist ---
    all_w = set()
    for f in glob.glob(f"{REPO}/01-model-company/workflows/VS-*/PA-*.md"):
        for h in re.findall(r"^#{2,3} (W\d+[A-Z]?)\.", open(f).read(), re.M):
            all_w.add(h)
    all_req = set(re.findall(r"^\| ([A-Z]+-\d+[a-z]?) \|", open(REQS).read(), re.M))
    by_vs = {c[0]: c for c in CONTROLS}
    errs = []
    for cid, (vs, typ, obj, act, owner, wfs, reqs) in by_vs.items():
        for w in wfs:
            if w not in all_w:
                errs.append(f"VS-{vs}: workflow {w} does not resolve to a header")
        for r in reqs:
            if r not in all_req:
                errs.append(f"VS-{vs}: requirement {r} not found in erp-requirements.md")
    listed = [c[0] for c in CONTROLS]
    UNCOVERED = [2,6,8,11,12,14,20,21,23,24,25,26,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88]
    if sorted(listed) != UNCOVERED:
        errs.append("CONTROLS does not cover exactly the 68 uncovered VS")
    for _cid, _fam, vss in FAMILIES:
        for v in vss:
            if v not in by_vs:
                errs.append(f"family lists VS-{v} with no control")
    if errs:
        print("VERIFICATION FAILED:")
        for e in errs:
            print("  " + e)
        sys.exit(1)

    # --- build the block ---
    ctl = 172
    lines = []
    per_family = {f[1]: [0, 0] for f in FAMILIES}
    for cid, fam, vss in FAMILIES:
        lines.append(f"## {cid}. Expansion & Legacy-Block Domain Controls — {fam}")
        lines.append("")
        lines.append("One anchor control per value stream whose workflows previously had no coverage in the")
        lines.append("register (Core VS-02–VS-31, Expansion VS-32–VS-48/VS-53–VS-78, Statutory VS-79–VS-88); each is")
        lines.append("exercised at the specific workflows listed and backfilled into those workflows' Controls")
        lines.append("sections by `07-methodology/backfill-controls.py`.")
        lines.append("")
        lines.append("| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |")
        lines.append("|---|---|---|---|---|---|---|")
        for vs in sorted(vss):
            _vs, typ, obj, act, owner, wfs, reqs = by_vs[vs]
            per_family[fam][0 if typ == "P" else 1] += 1
            lines.append(f"| CTL-{ctl} | {obj} | {typ} | {act} | {owner} | {', '.join(wfs)} | {', '.join(reqs)} |")
            ctl += 1
        lines.append("")
    block = "\n".join(lines)
    n = ctl - 172
    nP = sum(v[0] for v in per_family.values())
    nD = sum(v[1] for v in per_family.values())

    if dry:
        print(block)
        print(f"# {n} controls ({nP} P / {nD} D), CTL-172–CTL-{ctl-1}")
        return

    txt = open(MATRIX).read()
    anchor = "## Controls Summary by Category"
    assert anchor in txt and "CTL-239" not in txt
    txt = txt.replace(anchor, block + anchor, 1)

    # --- extend the summary table ---
    fam_label = {"Plan & Source": "Expansion & Legacy — Plan & Source"}
    for cid, fam, vss in FAMILIES:
        p, d = per_family[fam]
        label = f"Expansion & Legacy — {fam}"
        old = "| **Total** | **50** | **121** | **171** |"
        txt = txt.replace(old,
                          f"| {label} | {p} | {d} | {p + d} |\n" + old, 1)
    # the 8 rows were inserted in family order above the Total row -> reorder check:
    # inserted sequentially each immediately before Total, so they end up in insertion order. Good.
    txt = txt.replace("| **Total** | **50** | **121** | **171** |",
                      f"| **Total** | **{50 + nP}** | **{121 + nD}** | **{171 + n}** |", 1)

    open(MATRIX, "w").write(txt)
    print(f"inserted {n} controls (CTL-172–CTL-{ctl-1}; {nP} P / {nD} D); total now {171 + n}")


if __name__ == "__main__":
    main()
