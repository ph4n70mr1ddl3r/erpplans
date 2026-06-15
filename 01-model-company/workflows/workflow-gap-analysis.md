# Workflow Gap Analysis — BuildRight Depot Corp.

> Methodology and results of the operational workflow gap analysis (Pass 1, Pass 2, Pass 3, Pass 4,
> Pass 5, Pass 6, Pass 7, Pass 8, Pass 9 (all 2026-06-14), Pass 10, and Pass 11 (2026-06-15)).
> Companion document to [value-stream-index.md](value-stream-index.md) and
> [workflow-criticality-classification.md](workflow-criticality-classification.md).

---

## 1. Purpose

Validate that the operational workflow inventory **comprehensively covers the operations of the
model company** (BuildRight Depot Corp. — a Philippine hardware/DIY/home-improvement big-box
retailer: 200 stores, 4 DCs, 35,000 active SKUs, ~800–1,000 vendors, ~PHP 62.3B annual revenue,
5 legal entities) as described in [model-company-profile.md](../model-company-profile.md), and
identify capability gaps not addressed by any existing value stream.

---

## 2. Method

1. **Inventory** the existing value streams, process areas, and workflows grouped by the
   8 operating families (Plan & Source, Make & Move, Sell & Serve, Finance, People, Asset &
   Infrastructure, Governance & Assurance, Technology & Data).
2. **Map** each major operational domain in the model company profile (merchandising, supply
   chain, store operations, POS/ecommerce, finance, HR, assets, governance/compliance, IT/data,
   legal/real-estate) to the value stream(s) that cover it.
3. **Flag gaps** where a domain had no dedicated value stream, only partial coverage, or was a
   known retired value stream (VS-49/50/51/52) not yet re-introduced.
4. **Validate** each candidate gap by keyword search across all PA files to confirm it is not
   already covered (avoiding redundant value streams) and to scope it so the new value stream is
   distinct from adjacent ones. For Pass 10, every candidate gap was confirmed to have its defining
   terms appear in zero or near-zero PA files with no dedicated owner — 'fraud orchestration' (0 PA
   files) and 'fraud management' (1) for VS-125; 'customer golden record' (0) and 'identity
   resolution' (2) for VS-126; 'integrated business planning' (0), 'IBP' (0), and 'sales and
   operations planning' (0) for VS-127; and 'model risk management' (0) and 'algorithmic
   fairness' (0) for VS-128 — each with only incidental single-step references to the broader
   capability scattered
   across multiple adjacent value streams. For Pass 11, every candidate gap was confirmed to be
   either a single workflow within another value stream ripe for elevation (W2683 Philippine
   Competition Law Compliance in VS-76.2, elevated to VS-129 following the Pass-1/Pass-5/Pass-7/
   Pass-8/Pass-10 pattern) or genuinely uncovered with zero (or only one incidental) PA-file
   references for the defining terms ('merger and acquisition'/'divestiture' for VS-130;
   'human rights'/'modern slavery' for VS-131; 'political contribution'/'election compliance'/
   'COMELEC' for VS-132). For prior passes, each candidate gap was confirmed to
   have only incidental single-workflow coverage (or none) in the existing PA files;
   for Pass 7 specifically, 'enterprise architecture' appeared in **zero** PA files, calibration was
   referenced across **50+** PA files with no dedicated owner, dangerous-goods transport was
   confirmed distinct from VS-24.3 fixed-site storage, and performance bonds/surety were confirmed
   sprinkled across VS-46/VS-11/VS-18 as single steps. For Pass 8, every candidate gap was confirmed
   to be either a single workflow within another value stream ripe for elevation (W447 DTI-BPS in
   VS-22.1; W348 Revenue Assurance in VS-21.3; W2943 ABC-Whistleblower in VS-86.3) or genuinely
   uncovered with no dedicated owner and only incidental references (RA 11285 energy-efficiency
   compliance across 14 PA files with zero dedicated headers). For Pass 9, every candidate gap was
   confirmed to be genuinely uncovered with **zero** dedicated PA-file references for the defining
   terms ('candidate experience' / 'career site' / 'talent community' for VS-121; 'global sourcing' /
   'sourcing agent' / 'overseas buying office' for VS-122; 'apprenticeship program' for VS-123;
   'clienteling' for VS-124) and only incidental single-workflow references to the broader capability
   (employer brand in 3 PA files, vocational/TESDA participation in 4, product knowledge in 33 with
   no dedicated owner), each scoped to be distinct from adjacent covered capabilities.
5. **Prioritize** gaps by operational criticality, regulatory exposure, and volume, and select the
   set to fill in each revision pass.

---

## 3. Gaps Identified

| # | Capability gap | Why it matters for BuildRight | Existing (partial) coverage | Decision |
|---|---|---|---|---|
| 1 | **Product Recall & Safety Corrective Action** | 35K SKUs incl. electrical, paint/chemical, power tools, appliances; Consumer Act (RA 7394) + DTI-BPS + FDA recall obligations; ~3–8 recalls/yr | Only the store-level *customer-notification execution* step exists (W776 in VS-09); no end-to-end recall program | **FILLED — VS-89** |
| 2 | **Damage, Claims & Freight Recovery** | ~72K inbound receipts/yr, ~5K store replenishment orders/month, ~42.9K ecommerce orders/month; vendor/carrier/customer damage and shortage across all legs; claim notice windows are short | Retired VS-50 (placeholder) was the home; typhoon damage handled in VS-69; no systematic damage/claims program | **FILLED — VS-90** |
| 3 | **Consumer Data Privacy & Data Protection** | ~600K loyalty members, ~5,200 B2B contacts, ~515K ecommerce orders/yr, CCTV across 200 stores; Data Privacy Act (RA 10173) + NPC, 72-hour breach notification | Employee data privacy only (W647 in VS-19); consumer program (consent, DSAR, PIA/DPIA, breach) absent | **FILLED — VS-91** |
| 4 | **Kitting, Bundling & Build-to-Order Assembly** | Kit/Bundle is an explicit item type (profile §6.4); bundle pricing (§9.3); contractor combo packs, seasonal kits | Retired VS-51 (placeholder); custom *fabrication* heavily covered (VS-09 PA-09.1); build-to-stock kit/bundle operations absent | **FILLED — VS-92** |
| 5 | Workforce Management & Labor Scheduling | 200 stores × 2–3 shifts × 29 staff; DOLE labor-code compliance | **Already covered** — PA-19.3 (Workforce Management, 10 workflows) in VS-19 | No action |
| 6 | Facilities, Equipment & Maintenance Management | 600 POS terminals, paint mixers, cutting equipment, forklifts, HVAC across 205 locations | **Substantially covered** — PA-20.3 (VS-20) + PA-07.2 (VS-07, incl. W47, W579, W1025, W1403) | No action |
| 7 | Dark Store & Micro-Fulfillment | Emerging micro-fulfillment for ecommerce | Retired VS-49 (placeholder); low near-term relevance for PH big-box provincial footprint | **FILLED — VS-93** |
| 8 | Cooperative & Community Enterprise Procurement | Community/cooperative buying programs | Retired VS-52 (placeholder); lower priority than items 1–4 | **FILLED — VS-94** |
| 9 | Marketplace Operator & Third-Party Seller Management | BuildRight operating its own 3P marketplace to expand assortment | **New gap (Pass 2)** — VS-48 retail media and VS-65 marketplace presence (selling on Lazada/Shopee) did not cover BuildRight as marketplace operator | **FILLED — VS-95** |
| 10 | Equipment Leasing & Capital Equipment Finance | B2B lease/lease-to-own for expensive contractor equipment (generators, scaffolding, solar, HVAC) | **New gap (Pass 2)** — VS-12 short-term tool rental and VS-38 consumer credit did not cover B2B multi-year equipment leasing | **FILLED — VS-96** |
| 11 | **Corporate Real Estate & Property Portfolio Management** | BuildRight Property Management Inc. (one of the 5 named legal entities, profile §2) owns ~205 store/DC/office sites and leases them to BuildRight Depot Inc.; PFRS 40 investment-property accounting, landlord-side leasing & CAM, real property tax as owner, portfolio NOI/yield | **New gap (Pass 3)** — only the *lessee* side was covered (VS-20 site selection/CAM-as-tenant, VS-42 lease administration as tenant, VS-35 fixed-asset accounting); the *lessor / property-owner / investor* operating model was entirely uncovered | **FILLED — VS-97** |
| 12 | **Contingent, Contract & Outsourced Workforce Management** | ~10–20% of store/DC labor is non-employee (outsourced security guards, janitorial, promodizers, construction/agency labor); DOLE Department Order 174 labor-only-contracting compliance, worker-misclassification and co-employment risk before the NLRC | **New gap (Pass 3)** — VS-19 covers BuildRight's own employees (incl. directly-hired seasonal W555) and VS-34 covers commercial service contracts at the PO/invoice level, but no dedicated contingent-workforce *program* (DOLE D.O. 174 structuring, four-fold-test classification, contractor onboarding/access/safety, time-vs-invoice reconciliation, spend analytics) | **FILLED — VS-98** |
| 13 | **IT Asset & Technology Lifecycle Management** | 600 POS terminals + RF/handheld scanners + mobile devices + network/Wi-Fi + servers/storage + the full software/SaaS estate across 205+ locations; license true-up/audit exposure (BSA), data-privacy obligations on device disposal (RA 10173), DENR e-waste rules | **New gap (Pass 3)** — VS-35 fixed-asset *accounting* and VS-27 IT *operations/service desk* did not cover the ITAM discipline (hardware/software discovery & CMDB, SAM & license optimization, SaaS portfolio & FinOps, technology refresh, secure retirement with sanitization) | **FILLED — VS-99** |
| 14 | **Legal Operations, Litigation & IP Management** | Active legal matters and outside counsel across the 5-entity group; commercial/contract, labor (NLRC), consumer/DTI, property/lease, tax (BIR), customs (BOC), insurance/subrogation, and IP exposure; the board receives periodic litigation updates (per VS-36.1) | **New gap (Pass 3)** — VS-36 corporate governance, VS-22 compliance/regulatory, and VS-88 records/retention/legal-hold *execution* covered adjacent areas but not the *litigator work* (matter/case management, litigation lifecycle, outside counsel, IP portfolio prosecution & enforcement, settlement/loss-contingency) | **FILLED — VS-100** |
| 15 | **Merchandise Financial Planning, Open-to-Buy & Margin Management** | ~PHP 62.3B revenue, ~PHP 42–45B COGS, 28–32% gross margin, ~40% import component, 6–8x inventory-turn target; the open-to-buy, receipt-budget, markdown-margin, and inventory-investment discipline that governs whether EBITDA (12–14%) and turn targets are met | **New gap (Pass 4)** — VS-01.1 (assortment = *which* products), VS-02 (supply operations = *how much/when* operationally), VS-33.1 (corporate revenue/OPEx budget), and VS-17.4 (finance FP&A) all touched adjacent territory, but no value stream owned the *merchandise-financial* layer (seasonal merchandise plan, OTB, markdown budget, IMU/maintained-margin modeling, turn/GMROI/WOS planning, in-season reforecast, merchandise P&A) | **FILLED — VS-101** |
| 16 | **Compensation, Benefits & Total Rewards Strategy** | 6,715 employees across 5 entities/205 locations, 15–20% turnover, region-varying minimum wages, mandatory 13th-month/statutory benefits, executive-pay governance before the board; pay equity and market competitiveness directly drive attract-and-retain | **New gap (Pass 4)** — VS-19.2 (Payroll & Compensation) executes *payroll processing* only (pay runs, statutory remittance, 13th-month, final pay, garnishments); no value stream owned the *design and governance* of pay/benefits (job architecture, salary structure, market benchmarking, pay equity, benefits/HMO design, retirement, STI/LTI plans) | **FILLED — VS-102** |
| 17 | **HR Shared Services, Employee Experience & People Analytics** | 6,715 employees, ~1,200–1,600 hires and ~1,000–1,340 exits/year, 5 entities, distributed 200-store footprint; a structured HR service-center, EX program, and people-analytics function is essential to service quality, self-service adoption, compliance, and data-driven people decisions | **New gap (Pass 4)** — VS-19 owns the employee *lifecycle* (recruitment, payroll, WFM, learning, separation) and VS-84 owns labor relations, but no value stream owned the *service-delivery* layer (HR helpdesk/case management, ESS/MSS, multi-entity shared services, EX, engagement, DEI, workforce planning, people analytics, HRIS admin) | **FILLED — VS-103** |
| 18 | **Government Affairs, Public Policy & Industry Relations** | A PHP 62.3B retailer operating under Philippine national regulation (BIR tax/e-invoicing, DTI consumer, DOLE labor, BSP payments, DENR environmental, customs/tariff, data privacy) and participating in retail/supply-chain industry associations; 200 stores across regions require consistent national policy engagement and the board expects external-affairs reporting | **New gap (Pass 4)** — VS-76 covers *local* (LGU) permits/tax/relationships, VS-22 executes *permit/license operations* and government-audit response, VS-84.3 covers *labor-specific* policy advocacy/associations (W2893/W2894), VS-14.3 handles PR/crisis-comms, and VS-100 handles litigation; no value stream owned *proactive national corporate government affairs and industry relations* (stakeholder mapping, legislative/regulatory monitoring, advocacy, coalition building, association leadership, public affairs, political/regulatory risk) | **FILLED — VS-104** |
| 19 | **Supply Chain Finance & Working Capital Management** | ~PHP 37B annual procurement spend, ~800–1,000 vendors, 30–60-day standard terms; the supplier-finance / reverse-factoring / dynamic-discounting / cash-conversion-cycle discipline that releases working capital and supports vendor liquidity at PHP 62.3B-revenue scale | **New gap (Pass 5)** — VS-18 (treasury cash) contained a single program-summary workflow W324 “Supply Chain Finance & Dynamic Discounting Program”; VS-15 (P2P) processed the payable and VS-39 handled rebates, but no value stream owned the comprehensive SCF & working-capital program (multi-funder facility, vendor enrollment, dynamic-discounting platform, CCC governance) | **FILLED — VS-105** |
| 20 | **Commodity & Input-Cost Risk Management** | 35K-SKU assortment heavily weighted to commodity-intensive categories (steel/cement/lumber 14%+14%, copper 10%+12%, oil-derived paint/plastics 8%); ~40% import; a 10% commodity swing can move COGS by ~PHP 0.5–1.5B and threatens the 28–32% gross-margin target | **New gap (Pass 5)** — VS-02.3 touched supply-chain disruption risk and VS-18.3 hedged FX only; VS-101 modeled margin; “commodity hedg” appeared in only 1 PA file and no value stream owned the dedicated commodity-exposure / hedging / indexed-pricing / pass-through program | **FILLED — VS-106** |
| 21 | **Strategic Key Account & Enterprise Customer Management** | ~40% of revenue concentrated in ~5,200 B2B accounts; the top ~700 strategic accounts (developers, large enterprises, government, large contractors) materially move the P&L and warrant dedicated relationship/growth management | **New gap (Pass 5)** — VS-11 executed transactional trade/project/wholesale, VS-43 operated the trade loyalty program, VS-46 executed government bidding, and VS-13 served mass support; “key account” appeared across 16 files but no value stream owned the strategic key-account program (tiering, KAP/JBP, account teams, executive sponsorship, account profitability, CLV/churn) | **FILLED — VS-107** |
| 22 | **On-Site Renewable Energy & Prosumer Asset Operations** | ~205 large rooftops (1.6–3.0M sqm) in a high-irradiance, high-tariff market; rooftop solar/storage cuts grid cost, hedges brownouts (links to VS-07/W470), and delivers the ESG decarbonization target (links to VS-25) | **New gap (Pass 5)** — VS-70 sold solar products to customers, VS-35 accounted for fixed assets, and VS-07/VS-20.3 contained single energy/solar-monitoring workflows (W111/W173); no value stream owned BuildRight's own generation/prosumer program (capex, EPC, net-metering, REC, decarbonization accounting) | **FILLED — VS-108** |
| 23 | **Store Remodel, Renovation & Lifecycle Refurbishment Program** | 200-store chain remodels/refurbishes on a ~5–7-year cycle (~30–40 events/year at PHP 8–25M each; ~PHP 300–700M/yr program) — the single largest lever for comp-sales growth, format relevance, and asset-value preservation | **New gap (Pass 6)** — VS-37 covers only *new* store opening/commissioning, VS-59 only closure/decommissioning, VS-20 only *new-build* construction, VS-97 the landlord/owner investment view, and VS-40 only the *capex accounting* of remodel spend (W1811–W2752); the *operational* remodel program (lifecycle scoring, scope/concept/design, phasing around a live trading store, FF&E/signage rollout, technology/POS refresh, merchandise reset, re-opening, post-remodel analytics) was entirely uncovered | **FILLED — VS-109** |
| 24 | **Freight Procurement, Carrier Management & Freight Audit** | Freight is a major cost line (inbound/import, line-haul, last-mile; ~400–600 import TEUs/month, ~5,000 replenishment orders/month, ~80% third-party fleet, ~42.9K ecommerce orders/month); PHP-hundreds-of-millions-to-low-billions of spend with no single owner for carrier contracting/rate/routing-guide/freight-audit/landed-cost | **New gap (Pass 6)** — the freight-financial discipline was sprinkled across VS-02.2 (import freight, W66 inter-island, W249 demurrage), VS-04 (DC), VS-06.1 (outbound), and VS-06.3 (last-mile, incl. the single carrier-rate/freight-audit workflow W1166 and W1371/W1439/W1440); VS-56 covers only the last-mile 3PL *delivery-partner* relationship, VS-87 customs/tariff, and VS-15 AP processing — no value stream owned the end-to-end freight-spend/carrier-relationship/landed-cost program | **FILLED — VS-110** |
| 25 | **Packaging, Pallet & Returnable Transport Item (RTI) Management** | At BuildRight's volume (~72K inbound receipts/yr, ~134M POS line items/yr), packaging/pallets/RTI are a material cost line (PHP 200–500M/yr), a damage/shrink source, a freight-cube driver, and a sustainability/EPR (RA 11898) and single-use-plastic exposure | **New gap (Pass 6)** — referenced incidentally across VS-04 (DC receiving/palletization), VS-05 (merchandise inventory), VS-06 (logistics), VS-32 (reverse), VS-73 (waste), VS-41 (private-label packaging), VS-87 (import/ISPM-15), VS-24.3 (hazmat); no value stream owned the packaging-engineering, pallet/RTI pool, tracking/reconciliation, compliance/EPR, or cost-analytics discipline | **FILLED — VS-111** |
| 26 | **Corporate Project & Program Management Office (PMO)** | PHP 800M–1.2B annual capex plus major transformation programs (ERP/digital, net-zero/renewable, omnichannel, store-format evolution) run dozens of concurrent projects and several multi-project programs requiring portfolio governance, stage-gate discipline, resource/capacity planning, dependency/risk management, and benefits realization | **New gap (Pass 6)** — VS-40 performs only the *financial accounting* of capital projects (request/approval/commitment/CIP/turnover/variance/ROI-review W1811–W2752); VS-33 sets the budget envelope and tracks corporate KPIs; and the delivery-domain VSs (VS-20/VS-37/VS-109/VS-108/VS-27/VS-06) execute their respective project types — no value stream owned the enterprise project-portfolio governance/methodology/program-management/benefits-realization discipline | **FILLED — VS-112** |
| 27 | **Enterprise Architecture, Application Portfolio & Technology Strategy** | A 5-entity, 200-store, PHP 62.3B-revenue retailer on a unified cloud ERP with ~10+ active integration touchpoints (POS, ecommerce, payments, bank, BIR eFPS, statutory, delivery, loyalty, WMS, supplier portal) and an expanding digital perimeter (ecommerce, marketplace, retail media, mobile app, BIR e-invoicing, AI/ML) requires a continuous enterprise-architecture discipline to keep the application landscape coherent, integrated, secure, standards-compliant, and strategy-aligned | **New gap (Pass 7)** — 'enterprise architecture' appeared in **0** PA files; VS-27 operates/secures platforms, VS-28 consumes data, VS-30 evaluates emerging tech/POCs, VS-99 manages hardware/software asset lifecycle — none designs and governs the application landscape, integration architecture, technology standards, solution architecture, or multi-year technology strategy | **FILLED — VS-113** |
| 28 | **Dangerous Goods (DG) & Hazardous Materials Transport, Ecommerce & Regulatory Compliance** | An 8–10%+ DG-intensive assortment (paint/solvents ~2,800 SKUs, adhesives/thinners, aerosols, garden/agro chemicals, cleaning chemicals, fuels/lubricants, gas cylinders, lithium-battery products) moves by import ocean freight (~400–600 TEUs/month), inter-island sea/land, DC-to-store distribution, and ecommerce last-mile (~42,900 orders/month) under multiple regulators (DENR-EMB RA 6969, BFP Fire Code, DOLE OSH, MARINA/Coast Guard, CAB, LTFRB/DOTC) and international modal rules (IMDG/IATA/ADR); non-compliance causes carrier refusal, ecommerce channel blocking, port seizure, fines, and fire/spill/injury risk | **New gap (Pass 7)** — VS-24.3 (HSE) covers only **fixed-site** storage/handling safety; VS-87 covers import customs; VS-89 covers defective-product recall; VS-111 engineers product/transport packaging generally — no value stream owned the DG transport, ecommerce ship-eligibility, DG documentation/carrier-qualification, DENR-EMB hazardous-waste transport manifest, DG site permitting, or DG incident/spill/claim lifecycle | **FILLED — VS-114** |
| 29 | **Calibration, Metrology & Measurement Traceability Management** | Catch-weight and cut-to-length selling (lumber/board-foot, wire/meter, nails bulk, tiles/sq-m) at 600 POS across 2.8M monthly transactions; custom fabrication (pipe/lumber/sheet/wire cutting) and paint mixing/tinting at every store; DC weighbridges/truck scales at 4 DCs; fuel & logistics meters; environmental/process instruments; and test & measurement tools — measurement accuracy directly determines revenue accuracy, inventory accuracy (≥97% target), quality acceptance, and DTI weights & measures / Consumer Act RA 7394 compliance | **New gap (Pass 7)** — calibration/metrology was referenced incidentally across **53** PA files (VS-08 POS scales, VS-09 cutting/paint, VS-04 DC scales, VS-07 store equipment, VS-31 quality instruments, VS-12 rental tools, VS-61 fuel, VS-23 system calibration) with **no dedicated owner** and **zero** PA with 'calibration' or 'metrology' in its title — no value stream owned the program, standards/traceability, scheduling, records, or compliance discipline | **FILLED — VS-115** |
| 30 | **Performance Bond, Surety & Bank Guarantee Management** | ~10% B2G + ~30% B2B/project revenue under RA 9184 (Government Procurement Reform Act) and large enterprise contracts require bid bonds, performance bonds (5–30%), payment bonds, warranty bonds, and retention — secured by surety bonds or bank guarantees/LCs/cash that encumber on the order of **PHP 5M–50M+** of credit facility simultaneously and tie up capacity that otherwise supports operations | **New gap (Pass 7)** — VS-46 (B2G) references the bond as one bid step, VS-11 (B2B/project) references tender/performance bonds in bidding, VS-18 (Treasury) manages the bank/facility — no value stream owned the surety facility strategy, bond application/issuance/tracking/encumbrance lifecycle, counter-indemnity/collateral, release/closeout, claim/default response, or surety analytics | **FILLED — VS-116** |
| 31 | **DTI-BPS Product Standards Certification & PS Mark/ICC Compliance** | ~44% of the 35,000-SKU assortment by category mix is DTI-BPS-regulated (steel/cement/PVC ~14%, tiles ~12%, electrical ~10%, paint/coatings ~8%) and ~40% is imported; RA 4109 and DTI-BPS DAOs make PS Mark / ICC / SOC certification a legal prerequisite to sale, with ~10–15 regulated import shipments/month, market-surveillance exposure, and per-unit ICC-sticker obligations | **New gap (Pass 8)** — only the single import-clearance workflow **W447** in VS-22.1 existed; VS-87 clears customs, VS-31 runs internal QC, VS-89 recalls defective product — no value stream owned the full PS-Mark-license / vendor-certification / accredited-testing / ICC-sticker / market-surveillance / vendor-recovery program | **FILLED — VS-117** |
| 32 | **Revenue Assurance, Pricing Integrity & Leakage Management** | ~PHP 62.3B revenue / 2.8M monthly POS transactions across 600 terminals / ~42,900 ecommerce orders/month / ~600K loyalty members / gift-card / marketplace-3P / catch-weight selling; retail revenue leakage benchmarks 1–3% of gross revenue = **PHP 0.6B–1.9B/yr** at risk from pricing, promo/loyalty/gift-card, refund/reversal, catch-weight/weighing, discount-stacking, VAT/tax, payment/MDR, and settlement leakage | **New gap (Pass 8)** — only the single monthly-audit workflow **W348** in VS-21.3 existed; VS-23 addresses inventory shrink (a different vector), VS-17.4 reports revenue, VS-08 executes the transaction — no value stream owned the continuous, all-channel revenue-assurance / leakage-detection / recovery program | **FILLED — VS-118** |
| 33 | **Whistleblower, Ethics & Corporate Integrity (Speak-Up) Program** | 6,715 employees + ~10–20% contingent labor across 200 stores/4 DCs/5 entities; ~800–1,000 vendors; ~10% B2G + ~30% B2B revenue (ABC exposure); cash/data handling at scale — an enterprise speak-up channel, independent investigation, and whistleblower protection is a governance expectation (board audit/risk oversight, ISO 37001/37301) | **New gap (Pass 8)** — only the single ABC-specific workflow **W2943** in VS-86.3 existed; VS-21 audits controls, VS-100 manages litigation, VS-23 investigates theft, VS-84 handles grievances, VS-103 runs HR cases — no value stream owned the multi-channel intake / triage / investigation / retaliation-protection / culture / analytics program across **all** violation types | **FILLED — VS-119** |
| 34 | **Energy Efficiency, Conservation & RA 11285 Compliance Program** | ~205 large energy-consuming sites (200 stores at 8,000–15,000 sqm + 4 DCs + HQ) are RA 11285 (Energy Efficiency & Conservation Act, 2019) designated establishments with statutory obligations: designate an Energy Efficiency Officer, conduct mandatory energy audits (Type-1 every 3 yrs / Type-2 annually), prepare and submit an Energy Conservation Plan and annual reporting to DOE; energy is a material cost line and decarbonization lever | **New gap (Pass 8)** — referenced incidentally across 14 PA files (W692/W1543 energy consumption in VS-25.1, W701/W1563 in VS-20.3, W111 utility bill, VS-108 own-generation) with **zero** dedicated workflow headers; VS-25 reports the footprint, VS-108 generates clean energy, VS-34 buys transactionally — no value stream owned the RA 11285 compliance program / ISO 50001 EnMS / ECM pipeline / M&V / energy-procurement-retail-competition discipline | **FILLED — VS-120** |
| 35 | **Talent Acquisition, Employer Brand & Candidate Experience** | ~1,200–1,600 hires/yr at 15–20% turnover across a 5-entity, 205-location, ~6,715-employee group competing for scarce corporate *and* trade-knowledgeable frontline talent in the Philippine market; the strategic candidate-side discipline (EVP, career site, candidate experience, sourcing-channel strategy, talent community, campus/vocational feeder, candidate NPS, TA operations) directly drives time-to-fill, cost-per-hire, offer-acceptance, and early-attrition | **New gap (Pass 9)** — VS-19.1 executes recruitment *transaction* processing only (W15/W179/W715/W682) and VS-103.2 owns the *employee* experience; 'candidate experience', 'career site', and 'talent community' each appeared in **zero** PA files and 'employer brand' only incidentally (3 PA files) — no value stream owned the *attraction and candidate-side* discipline | **FILLED — VS-121** |
| 36 | **Global Sourcing, Import Buying & Sourcing Agent Management** | ~40% of COGS imported (~PHP 17–18B/yr), ~400 international vendors across China/Taiwan/Indonesia/Malaysia/Japan/Europe, ~400–600 import TEUs/month, ~PHP 1.4B/month import value, commodity-intensive assortment; the strategic source-side discipline (source-market/country strategy, sourcing-model decision, sourcing-agent/overseas-buying-office governance, import vendor development, consolidated container buying, total-landed-cost sourcing) materially drives COGS, availability, and supply-base resilience | **New gap (Pass 9)** — VS-02.2 executes operational import/customs, VS-03 executes transactional vendor/PO, VS-87 customs compliance, VS-31/VS-41 quality/factory audit; 'global sourcing', 'sourcing agent', and 'overseas buying office' each appeared in **zero** PA files — no value stream owned the *strategic source-side* discipline | **FILLED — VS-122** |
| 37 | **Skilled-Trade Apprenticeship, Vocational Education & Capability Pipeline** | BuildRight's differentiation is knowledgeable trade staff (lumber/tile/plumbing/electrical/paint/tools) plus fabrication/estimation/installation specialists, in a Philippine market where trade certification runs through the TESDA (RA 7796) NC/COC framework and such talent is scarce; a structured apprenticeship/vocational capability pipeline is the primary lever on service quality, attach, and the credible "home-building partner" positioning | **New gap (Pass 9)** — VS-19.4 runs general employee L&D/competency, VS-12.3 W1556 is a single TESDA school career-day *participation* workflow, VS-43.3 trains trade *customers*; 'apprenticeship program' appeared in **zero** PA files and 'vocational' only incidentally (4) — no value stream owned BuildRight's *own* structured apprenticeship and vocational feeder | **FILLED — VS-123** |
| 38 | **Sales Enablement, Product Knowledge Mastery & Clienteling** | ~5,800 store staff serving 2.8M monthly POS transactions, ~PHP 1,800 ATV, ~40% B2B/trade revenue, ~600K loyalty members; associate selling effectiveness (product-knowledge mastery, consultative selling, clienteling/customer-360 at POS, attachment/linked/category selling, trade-pro consultative selling) is the single largest controllable lever on basket size, conversion, attach, and trade-pro capture | **New gap (Pass 9)** — product knowledge referenced across ~33 PA files and product training ~13 with **no dedicated owner**; 'clienteling' appeared in **zero** PA files and 'sales enablement'/'selling skills' in 2/1 — VS-19.4 owns general L&D, VS-13 loyalty/CRM, VS-07 daily store execution, VS-09 in-store services — no value stream owned the *associate selling-effectiveness* discipline | **FILLED — VS-124** |
| 39 | **Cross-Channel Fraud Management & Payment Fraud Protection** | ~PHP 62.3B revenue / 2.8M monthly POS transactions across 600 terminals / ~42,900 ecommerce orders/month (COD-heavy) / ~600K loyalty members / gift-card balances / ~5,200 trade accounts; retail fraud benchmarks 0.5–1.5% of gross revenue = **PHP 0.3B–0.9B/yr** at risk across payment fraud, return/refund abuse, promo/coupon/loyalty abuse, gift-card fraud, account takeover, first-party/friendly fraud, chargebacks, employee/internal collusion, and trade-account/application fraud | **New gap (Pass 10)** — fraud detection referenced across ~17 PA files and specific fraud types handled as single steps within VS-32 (return), VS-58 (coupon), VS-80 (payment/chargeback), VS-13.2 (loyalty), VS-23 (physical shrink), VS-118 (pricing leakage), VS-86 (AML) — 'fraud orchestration' appeared in **zero** PA files and 'fraud management' in one — no value stream owned the *cross-channel fraud program* (detection rules/ML, case management, investigation, recovery, chargeback representment, internal-fraud, regulatory/law-enforcement, analytics) | **FILLED — VS-125** |
| 40 | **Customer Data Platform, Single Customer View & Identity Resolution** | ~600K loyalty members + ~5,200 trade accounts + ~200 corporate accounts + ~515K ecommerce orders/yr + 2.8M monthly POS transactions + clienteling/personalization ambition; the inability to resolve a single customer across cash/loyalty/ecommerce/trade/app touchpoints blocks personalization, loyalty accuracy, retention, CLV decisions, and consent-compliant marketing under RA 10173 | **New gap (Pass 10)** — 'CDP' referenced across ~23 PA files and 'customer data platform' ~12 with no dedicated owner; 'customer golden record' appeared in **zero** PA files and 'identity resolution' in two — sprinkled across VS-13 (loyalty), VS-29 (master data), VS-107 (key account), VS-10 (ecommerce), VS-75 (app) — no value stream owned the *CDP platform and single-customer-view discipline* | **FILLED — VS-126** |
| 41 | **Sales & Operations Planning (S&OP) & Integrated Business Planning (IBP)** | 35K SKUs across 200 stores + 4 DCs, ~40% imports with 45–90-day lead times (demand errors compound over long lead times), heavy Philippine seasonality (rainy-season, ber-months, summer), 6–8x inventory-turn target, ~PHP 42–45B COGS; the monthly cross-functional consensus demand-supply cycle that balances forecast, supply constraints, inventory, and the financial plan | **New gap (Pass 10)** — 'S&OP' referenced across ~20 PA files and 'demand planning/forecasting' ~24–31 with no dedicated owner; 'integrated business planning', 'IBP', and 'sales and operations planning' each appeared in **zero** PA files — sprinkled as single steps inside VS-02 (operational supply), VS-101 (merchandise financial plan), VS-33 (corporate strategy), VS-106 (commodity) — no value stream owned the *S&OP/IBP consensus-planning process* | **FILLED — VS-127** |
| 42 | **AI/ML Governance & Responsible AI** | Rapidly expanding AI/ML footprint — fraud detection (VS-125), demand forecasting (VS-127), personalization/recommendation (VS-126), pricing/markdown, inventory optimization, LP analytics, customer-service chatbots, document/OCR automation, and generative-AI assistants across the PHP 62.3B-revenue, 5-entity, ~6,715-employee operation; uncontrolled models cause revenue loss (bad forecast/price), customer harm (unfair bias, wrongful fraud decline, privacy breach), and regulatory/reputational exposure under RA 10173 automated-decision rights and emerging PH AI rules | **New gap (Pass 10)** — 'AI governance' referenced in ~3 PA files, 'responsible AI' in 1, and the defining terms 'model risk management' and 'algorithmic fairness' in **zero** PA files each — AI/ML is engineered inside VS-30.2 and used by VS-125/VS-126/VS-127/VS-28/VS-113 — no value stream owned the *AI-governance and responsible-AI discipline* (model inventory/risk, fairness/bias, explainability, AI privacy/consent, safety/robustness, human oversight, GenAI governance, ISO 42001/NIST AI RMF) | **FILLED — VS-128** |
| 43 | **Competition & Antitrust Compliance (RA 10667 / PCC)** | A dominant-share, 200-store, ~PHP 62.3B-revenue retailer with pervasive pricing (VS-57), trade/resale-pricing and RPM exposure with ~800–1,000 vendors (VS-03/VS-11/VS-43/VS-82), association/coalition conduct (VS-104), buyer-power in procurement, marketplace/retail-media platform conduct (VS-95/VS-48), and an M&A pipeline (VS-130) — each a distinct antitrust vector under RA 10667 and PCC guidance, with fines up to PHP 250M (first offense) and private damages exposure | **New gap (Pass 11)** — only the single workflow **W2683** (Philippine Competition Law Compliance) in VS-76.2 existed, with scattered antitrust guardrail references in VS-104/VS-46/VS-71.3/VS-100.3/VS-119 — no value stream owned the end-to-end competition-compliance program (market-power assessment, pricing/conduct controls, RPM/clause controls, association protocol, merger notification, PCC engagement/investigation/leniency, penalty/remediation) | **FILLED — VS-129** |
| 44 | **Corporate Development, Mergers, Acquisitions, Divestiture & Strategic Transactions** | A growth-stage, 5-entity, 200-store retailer growing 10–15 stores/year whose path includes acquiring competitor chains/banners, specialty/service businesses, JVs (property/digital/fintech), and divesting/carving out non-strategic assets — the inorganic-growth lifecycle (target sourcing, valuation, DD, SPA, regulatory clearance incl. PCC, Day-1, PMI/synergy, carve-out/TSA, divestiture) carries PHP-hundreds-of-millions-to-low-billions per major transaction and a 60–70% integration-failure rate | **New gap (Pass 11)** — 'merger and acquisition' and corporate-transaction 'divestiture' each appeared in **zero** PA files (the only 'divestiture' references were conflict-of-interest divestiture) — VS-33 sets strategy, VS-37 opens stores, VS-40 accounts for capex, VS-112 runs PMO, VS-100.3 provides legal advisory, VS-129 handles PCC clearance — no value stream owned the *M&A transaction lifecycle* | **FILLED — VS-130** |
| 45 | **Human Rights, Modern Slavery & Responsible Supply Chain Due Diligence** | A commodity-intensive, ~40%-import assortment (tools/electronics, paint/chemicals, lumber, tiles, PPE, garden/agro) sourced from China/Taiwan/Indonesia/Malaysia/Japan/Europe, sold to international B2B customers subject to UK MSA/German LkSG/EU CSDDD/US UFLPA — exposing BuildRight to forced/modern-slavery labor, child labor, unsafe conditions, irresponsible recruitment, conflict-minerals, and land-rights risk across its own operations and supply chain | **New gap (Pass 11)** — 'human rights' and 'modern slavery' each appeared in only **one** PA file (an ESG *reporting topic* in VS-25.2 and an audit *risk* in VS-21.3) — VS-25.2 touches environmental/diversity sourcing, VS-03 runs vendor ops, VS-122 executes import sourcing, VS-31/VS-117 address product quality/standards, VS-119 internal ethics — no value stream owned the *human-rights due-diligence program* | **FILLED — VS-131** |
| 46 | **Corporate Political Engagement, Election Compliance & Public Affairs Governance** | A PHP 62.3B, 5-entity, 200-store, multi-region retailer with substantial B2G sales (VS-46), LGU relationships (VS-76), industry advocacy (VS-104), and board/investor transparency expectations — operating under the Omnibus Election Code, RA 9006/COMELEC (corporate political contributions largely prohibited, with criminal liability), RA 3019 anti-graft, and RA 6713 | **New gap (Pass 11)** — 'political contribution', 'election compliance', and 'COMELEC' each appeared in **zero** PA files — VS-104 manages govt-affairs *relationships*, VS-86 addresses *bribery*, VS-119 handles *misconduct*, VS-46 executes *B2G sales*, VS-14.3 manages *comms* — no value stream owned the *political-activity governance/compliance/discipline* | **FILLED — VS-132** |

### Candidate gaps considered but rejected (adequate coverage)

- **Strategic sourcing / RFP** — covered by VS-03 vendor management.
- **Loyalty / coalition partnerships** — covered by VS-13.
- **Tax compliance** — covered by VS-79 / VS-87.
- **Anti-counterfeit / product authentication** — covered by VS-71.
- **Trade credit / AR risk** — covered by VS-16 / VS-68.
- **Treasury / FX / intercompany** — covered by VS-18 / VS-72.
- **Energy & utilities management** — covered by VS-25.1 (W692/W1543) and VS-20.3 (W701/W1563).
- **B2B self-service portal** — covered (W936 portal referenced throughout VS-11/VS-16).
- **NPI / range / product lifecycle** — covered by VS-01.1 (assortment planning & product lifecycle).
- **Affiliate / influencer / referral marketing** — covered by VS-14.2 (W1351/W142/W1184/W1558).
- **In-store concessionaire / kiosk / vending** — covered by VS-07.1 (W177).
- **Performance management / succession** — covered by VS-19.1 (W72/W178).
- **Software development lifecycle (SDLC)** — covered by VS-27.1 (W132).
- **Data governance / stewardship** — covered by VS-28.2 (W1177).
- **DIY how-to content / knowledge library** — covered by VS-09.1 (W1136) + VS-01.3 (W1346).
- **Refurbishment / open-box / liquidation** — covered by VS-32.3 (W1640) + VS-05.3 (W220).
- **Disaster/BCP / insurance** — covered by VS-26.
- **Field service / installation dispatch** — covered across VS-12 / VS-66 / VS-70 / VS-06 / VS-74.
- **Visual merchandising / display execution** — substantially covered across VS-55 (planogram/space, incl. W2168 cross-merchandising, W2177 endcap compliance, W2180 visual-standards audit, W2187 seasonal display rotation) and VS-62 (sample/display lifecycle, incl. W2347 vendor-funded display).
- **Corporate communications / PR / crisis comms** — covered by VS-14.3 (W134/W143/W1562).
- **Contact center / call-center operations** — covered by VS-13.1 (W258 omnichannel ticketing, W259 call-center daily ops, W597 escalation SLA, W1550 VOC).
- **Import trade finance / LC / freight forwarder** — covered by VS-02.2 (W144/W191/W249/W464/W1233/W1264) and VS-87.
- **Talent management / succession** — covered by VS-19.1 (W72/W178) and the EX/DEI workflows now in VS-103.
- **Property / facility maintenance (landlord-side)** — covered by VS-20.3 and VS-97.2.
- **IT change & release management** — covered by VS-27.1 (service management, W132 SDLC).
- **Continuous improvement / operations excellence** — covered across VS-30 (innovation/automation) and VS-21 (audit).

### Candidate gaps considered but rejected in Pass 6 (adequate coverage)

- **Lumber yard / bulk building materials operations** — covered by VS-07.1 (W1281 Lumber Yard Daily Operations & Inventory Management, W951 bulk material breaking, W1243 lumber grading) and W1488 bulk delivery.
- **Corporate travel, expense & P-card management** — covered by VS-34.3 Expense Monitoring & Control (W1686 Travel & Business Entertainment Expense Management + the corporate-card issuance/audit workflows).
- **Print, signage & POSM production & distribution** — covered by VS-14.1 Campaign Planning & Execution (W1270 Seasonal Promotional Catalog Production/Printing/Store Distribution, W1522 Monthly Flyer & Promotional Catalog, plus the in-store POS-material production/distribution step and W1313 vendor-supplied POP lifecycle).
- **Energy & utilities procurement & contract management** — covered by W111 (utility bill/consumption across ~205 accounts, in VS-07.2/VS-20.3), VS-108 (own generation), and VS-34 (procurement); explicitly noted as covered above.
- **Store fixtures / FF&E procurement** — absorbed into the new VS-109 remodel program (W3481) and VS-37 store opening, with VS-34/VS-03 for transactional procurement.

### Capabilities elevated from single workflows to dedicated value streams (Pass 5)

Pass 5 specifically targeted capabilities that existed only as a single workflow within another value stream (or were conflated with an adjacent covered one) and elevated each to its own end-to-end program — the same pattern used in Pass 1 (VS-89 Product Recall was elevated from the single customer-notification workflow W776 in VS-09):

- **Supply chain finance / dynamic discounting** — *previously* the single workflow W324 in VS-18 PA-18.1; now the dedicated **VS-105** program.
- **Commodity hedging / input-cost risk** — *previously* a single incidental reference; now the dedicated **VS-106** program.
- **Strategic / key account management** — *previously* sprinkled across VS-11/VS-43/VS-46/VS-13; now the dedicated **VS-107** program.
- **Own-generation / prosumer solar** — *previously* the single monitoring workflows W111 (energy) and W173 (solar) in VS-07/VS-20.3; now the dedicated **VS-108** program.

---

## 4. New Value Streams Added

**Pass 1** (W2993–W3088): four value streams, 12 process areas, 96 workflows:

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-89](VS-89-product-recall-safety-corrective-action/README.md) | Product Recall & Safety Corrective Action Management | Governance & Assurance | 3 | 24 | W2993–W3016 |
| [VS-90](VS-90-damage-claims-freight-recovery/README.md) | Damage, Claims & Freight Recovery Management | Make & Move | 3 | 24 | W3017–W3040 |
| [VS-91](VS-91-consumer-data-privacy-protection/README.md) | Consumer Data Privacy & Data Protection Program | Governance & Assurance | 3 | 24 | W3041–W3064 |
| [VS-92](VS-92-kitting-bundling-build-to-order-assembly/README.md) | Kitting, Bundling & Build-to-Order Assembly Operations | Make & Move | 3 | 24 | W3065–W3088 |

**Pass 2** (W3089–W3184): four value streams, 12 process areas, 96 workflows:

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-93](VS-93-dark-store-micro-fulfillment/README.md) | Dark Store & Micro-Fulfillment Operations | Make & Move | 3 | 24 | W3089–W3112 |
| [VS-94](VS-94-cooperative-community-enterprise-procurement/README.md) | Cooperative & Community Enterprise Procurement | Plan & Source | 3 | 24 | W3113–W3136 |
| [VS-95](VS-95-marketplace-operator-third-party-seller/README.md) | Marketplace Operator & Third-Party Seller Management | Sell & Serve | 3 | 24 | W3137–W3160 |
| [VS-96](VS-96-equipment-leasing-capital-equipment-finance/README.md) | Equipment Leasing & Capital Equipment Finance | Finance | 3 | 24 | W3161–W3184 |

**Pass 3** (W3185–W3280): four value streams, 12 process areas, 96 workflows, deliberately
distributed across the four previously-thinnest operating families (Asset & Infrastructure,
People, Technology & Data each had only 3–4 value streams; Governance & Assurance is the natural
home for legal operations):

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-97](VS-97-corporate-real-estate-property-portfolio/README.md) | Corporate Real Estate & Property Portfolio Management | Asset & Infrastructure | 3 | 24 | W3185–W3208 |
| [VS-98](VS-98-contingent-contract-outsourced-workforce/README.md) | Contingent, Contract & Outsourced Workforce Management | People | 3 | 24 | W3209–W3232 |
| [VS-99](VS-99-it-asset-technology-lifecycle-management/README.md) | IT Asset & Technology Lifecycle Management | Technology & Data | 3 | 24 | W3233–W3256 |
| [VS-100](VS-100-legal-operations-litigation-ip-management/README.md) | Legal Operations, Litigation & IP Management | Governance & Assurance | 3 | 24 | W3257–W3280 |

**Pass 4** (W3281–W3376): four value streams, 12 process areas, 96 workflows, deliberately
distributed to strengthen the three thinnest operating families (People +2; Plan & Source +1;
Governance & Assurance +1). Each gap had been previously overlooked because it was conflated with
an adjacent covered capability:

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-101](VS-101-merchandise-financial-planning-otb-margin-management/README.md) | Merchandise Financial Planning, OTB & Margin Management | Plan & Source | 3 | 24 | W3281–W3304 |
| [VS-102](VS-102-compensation-benefits-total-rewards/README.md) | Compensation, Benefits & Total Rewards Strategy | People | 3 | 24 | W3305–W3328 |
| [VS-103](VS-103-hr-shared-services-employee-experience-people-analytics/README.md) | HR Shared Services, Employee Experience & People Analytics | People | 3 | 24 | W3329–W3352 |
| [VS-104](VS-104-government-affairs-public-policy-industry-relations/README.md) | Government Affairs, Public Policy & Industry Relations | Governance & Assurance | 3 | 24 | W3353–W3376 |

**Pass 5** (W3377–W3472): four value streams, 12 process areas, 96 workflows. Each gap had been
previously overlooked because it was either (a) conflated with an adjacent covered capability or
(b) addressed only as a single workflow within another value stream (the same pattern used in
Pass 1, where VS-89 Product Recall was elevated from the single customer-notification workflow
W776 in VS-09):

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-105](VS-105-supply-chain-finance-working-capital-management/README.md) | Supply Chain Finance & Working Capital Management | Finance | 3 | 24 | W3377–W3400 |
| [VS-106](VS-106-commodity-input-cost-risk-management/README.md) | Commodity & Input-Cost Risk Management | Plan & Source | 3 | 24 | W3401–W3424 |
| [VS-107](VS-107-strategic-key-account-enterprise-customer-management/README.md) | Strategic Key Account & Enterprise Customer Management | Sell & Serve | 3 | 24 | W3425–W3448 |
| [VS-108](VS-108-onsite-renewable-energy-prosumer-asset-operations/README.md) | On-Site Renewable Energy & Prosumer Asset Operations | Asset & Infrastructure | 3 | 24 | W3449–W3472 |

**Pass 6** (W3473–W3568): four value streams, 12 process areas, 96 workflows, deliberately
concentrated in the two thinnest-by-workflow operating families (Make & Move and Asset &
Infrastructure). Each gap had been overlooked because it was either (a) genuinely uncovered by any
value stream, (b) sprinkled across multiple value streams without a single owner, or (c) conflated
with an adjacent covered capability:

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-109](VS-109-store-remodel-renovation-lifecycle-refurbishment/README.md) | Store Remodel, Renovation & Lifecycle Refurbishment Program | Asset & Infrastructure | 3 | 24 | W3473–W3496 |
| [VS-110](VS-110-freight-procurement-carrier-management-and-freight-audit/README.md) | Freight Procurement, Carrier Management & Freight Audit | Make & Move | 3 | 24 | W3497–W3520 |
| [VS-111](VS-111-packaging-pallet-and-returnable-transport-item-management/README.md) | Packaging, Pallet & Returnable Transport Item (RTI) Management | Make & Move | 3 | 24 | W3521–W3544 |
| [VS-112](VS-112-corporate-project-and-program-management-office/README.md) | Corporate Project & Program Management Office (PMO) | Asset & Infrastructure | 3 | 24 | W3545–W3568 |

**Pass 7** (W3569–W3664): four value streams, 12 process areas, 96 workflows, deliberately
strengthening the thinnest family by workflow count (**Technology & Data** +48) and adding to three
families total (Governance & Assurance, Finance, and Technology & Data). Each gap had been
previously overlooked because it was (a) genuinely uncovered by every value stream, (b) referenced
across many PA files with no dedicated owner, (c) conflated with a fixed-site HSE capability, or
(d) reduced to single steps within B2G/B2B/treasury value streams:

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-113](VS-113-enterprise-architecture-application-portfolio-and-technology-strategy/README.md) | Enterprise Architecture, Application Portfolio & Technology Strategy | Technology & Data | 3 | 24 | W3569–W3592 |
| [VS-114](VS-114-dangerous-goods-hazmat-transport-ecommerce-regulatory-compliance/README.md) | Dangerous Goods (DG) & Hazmat Transport, Ecommerce & Regulatory Compliance | Governance & Assurance | 3 | 24 | W3593–W3616 |
| [VS-115](VS-115-calibration-metrology-and-measurement-traceability-management/README.md) | Calibration, Metrology & Measurement Traceability Management | Technology & Data | 3 | 24 | W3617–W3640 |
| [VS-116](VS-116-performance-bond-surety-and-bank-guarantee-management/README.md) | Performance Bond, Surety & Bank Guarantee Management | Finance | 3 | 24 | W3641–W3664 |

**Pass 8** (W3665–W3760): four value streams, 12 process areas, 96 workflows. Three of the four
are elevations of a single workflow within another value stream to a dedicated end-to-end program
(the same pattern used in Pass 1, Pass 5, and Pass 7), and the fourth is a genuinely-uncovered
statutory program referenced only incidentally across multiple value streams. Each gap had been
previously overlooked because it was (a) reduced to a single workflow (W447 DTI-BPS in VS-22.1;
W348 Revenue Assurance in VS-21.3; W2943 ABC-Whistleblower in VS-86.3), or (b) genuinely uncovered
with only incidental references and no dedicated owner (RA 11285 energy-efficiency compliance
across 14 PA files with zero dedicated headers):

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-117](VS-117-dti-bps-product-standards-certification-ps-mark-icc-compliance/README.md) | DTI-BPS Product Standards Certification & PS Mark/ICC Compliance | Governance & Assurance | 3 | 24 | W3665–W3688 |
| [VS-118](VS-118-revenue-assurance-pricing-integrity-and-leakage-management/README.md) | Revenue Assurance, Pricing Integrity & Leakage Management | Finance | 3 | 24 | W3689–W3712 |
| [VS-119](VS-119-whistleblower-ethics-and-corporate-integrity-speak-up-program/README.md) | Whistleblower, Ethics & Corporate Integrity (Speak-Up) Program | Governance & Assurance | 3 | 24 | W3713–W3736 |
| [VS-120](VS-120-energy-efficiency-conservation-and-ra-11285-compliance-program/README.md) | Energy Efficiency, Conservation & RA 11285 Compliance Program | Asset & Infrastructure | 3 | 24 | W3737–W3760 |

**Pass 9** (W3761–W3856): four value streams, 12 process areas, 96 workflows, deliberately
strengthening the thinnest family by workflow count (**People** +48, the thinnest at 194 workflows)
while also filling one genuine gap each in **Plan & Source** and **Sell & Serve**. Each gap had been
previously overlooked because it was genuinely uncovered with **zero** PA-file references for its
defining terms and only incidental single-workflow references to the broader capability:

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-121](VS-121-talent-acquisition-employer-brand-candidate-experience/README.md) | Talent Acquisition, Employer Brand & Candidate Experience | People | 3 | 24 | W3761–W3784 |
| [VS-122](VS-122-global-sourcing-import-buying-sourcing-agent-management/README.md) | Global Sourcing, Import Buying & Sourcing Agent Management | Plan & Source | 3 | 24 | W3785–W3808 |
| [VS-123](VS-123-skilled-trade-apprenticeship-vocational-education-capability-pipeline/README.md) | Skilled-Trade Apprenticeship, Vocational Education & Capability Pipeline | People | 3 | 24 | W3809–W3832 |
| [VS-124](VS-124-sales-enablement-product-knowledge-clienteling/README.md) | Sales Enablement, Product Knowledge Mastery & Clienteling | Sell & Serve | 3 | 24 | W3833–W3856 |

**Pass 10** (W3857–W3952): four value streams, 12 process areas, 96 workflows, distributed across
four families (Finance, Technology & Data, Plan & Source). Each gap had been
previously overlooked because it was genuinely unowned as a program — its defining terms appeared
in zero or near-zero PA files with only incidental single-step references to the broader capability
scattered across multiple adjacent value streams:

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-125](VS-125-cross-channel-fraud-management-payment-fraud-protection/README.md) | Cross-Channel Fraud Management & Payment Fraud Protection | Finance | 3 | 24 | W3857–W3880 |
| [VS-126](VS-126-customer-data-platform-single-customer-view-identity-resolution/README.md) | Customer Data Platform, Single Customer View & Identity Resolution | Technology & Data | 3 | 24 | W3881–W3904 |
| [VS-127](VS-127-sales-operations-planning-integrated-business-planning/README.md) | Sales & Operations Planning (S&OP) & Integrated Business Planning | Plan & Source | 3 | 24 | W3905–W3928 |
| [VS-128](VS-128-ai-ml-governance-responsible-ai/README.md) | AI/ML Governance & Responsible AI | Technology & Data | 3 | 24 | W3929–W3952 |

**Pass 11** (W3953–W4048): four value streams, 12 process areas, 96 workflows, adding one value stream to **Plan & Source** (the supply-chain-DD discipline) and three to **Governance & Assurance** (competition law, corporate development/M&A, and political engagement). Each gap had been previously overlooked because it was either reduced to a single workflow within another value stream (VS-129 elevating the single W2683 competition-law workflow in VS-76.2, following the same Pass-1/Pass-5/Pass-7/Pass-8/Pass-10 single-workflow-elevation pattern) or genuinely uncovered with no dedicated owner (VS-130 M&A/divestiture, VS-131 human-rights/responsible-supply-chain DD, VS-132 political engagement/election compliance — each with zero or only one incidental PA-file reference for its defining terms):

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-129](VS-129-competition-and-antitrust-compliance/README.md) | Competition & Antitrust Compliance (RA 10667 / PCC) | Governance & Assurance | 3 | 24 | W3953–W3976 |
| [VS-130](VS-130-corporate-development-ma-divestiture/README.md) | Corporate Development, Mergers, Acquisitions, Divestiture & Strategic Transactions | Governance & Assurance | 3 | 24 | W3977–W4000 |
| [VS-131](VS-131-human-rights-responsible-supply-chain-due-diligence/README.md) | Human Rights, Modern Slavery & Responsible Supply Chain Due Diligence | Plan & Source | 3 | 24 | W4001–W4024 |
| [VS-132](VS-132-corporate-political-engagement-election-compliance/README.md) | Corporate Political Engagement, Election Compliance & Public Affairs Governance | Governance & Assurance | 3 | 24 | W4025–W4048 |

### Family subtotal impact (cumulative after Pass 1 + Pass 2 + Pass 3 + Pass 4 + Pass 5 + Pass 6 + Pass 7 + Pass 8 + Pass 9 + Pass 10 + Pass 11)

| Family | After Pass 3 | After Pass 4 | After Pass 5 | After Pass 6 | After Pass 7 | After Pass 8 | After Pass 9 | After Pass 10 | After Pass 11 (current) |
|---|---|---|---|---|---|---|---|---|---|
| Plan & Source | 308 | 332 | 356 | 356 | 356 | 356 | 380 | 404 | **428** (+24) |
| Make & Move | 307 | 307 | 307 | 355 | 355 | 355 | 355 | 355 | 355 |
| Sell & Serve | 1,098 | 1,098 | 1,122 | 1,122 | 1,122 | 1,122 | 1,146 | 1,146 | 1,146 |
| Finance | 411 | 411 | 435 | 435 | 459 | 483 | 483 | 507 | 507 |
| People | 146 | 194 | 194 | 194 | 194 | 194 | 242 | 242 | 242 |
| Asset & Infrastructure | 128 | 128 | 152 | 200 | 200 | 224 | 224 | 224 | 224 |
| Governance & Assurance | 552 | 576 | 576 | 576 | 600 | 648 | 648 | 648 | **720** (+72) |
| Technology & Data | 182 | 182 | 182 | 182 | 230 | 230 | 230 | 278 | 278 |
| **Grand total** | **3,132** | **3,228** | **3,324** | **3,420** | **3,516** | **3,612** | **3,708** | **3,804** | **3,900** (+96) |
| Value streams | 96 | 100 | 104 | 108 | 112 | 116 | 120 | 124 | **128** (+4) |
| Process areas | 292 | 304 | 316 | 328 | 340 | 352 | 356 | 368 | **388** (+12) |

Pass 4 deliberately strengthened the three thinnest operating families: **People** (the
thinnest at 4 value streams) received +2, and **Plan & Source** and **Governance & Assurance** each
received +1. Pass 5 added one value stream to each of four families (Plan & Source, Sell & Serve,
Finance, and Asset & Infrastructure — the last being the thinnest by value-stream count), targeting
capabilities that existed only as single workflows within another value stream (SCF / commodity
hedging / key account / own-generation) or were conflated with an adjacent covered one. Pass 6
concentrated both new value streams in each of the two thinnest families by *workflow count* —
**Make & Move** (307 → 355, +48 via VS-110 Freight + VS-111 Packaging/RTI) and **Asset &
Infrastructure** (152 → 200, +48 via VS-109 Remodel + VS-112 PMO) — targeting capabilities that were
genuinely uncovered (remodel execution, packaging/pallet/RTI engineering), sprinkled across
multiple value streams (freight-spend/carrier), or conflated with the financial-accounting view
of an asset (capex accounting vs project-portfolio governance).

Pass 7 deliberately strengthened the thinnest family by workflow count — **Technology & Data**
(182 → 230, +48 via VS-113 Enterprise Architecture + VS-115 Calibration/Metrology) — and added one
value stream each to **Governance & Assurance** (576 → 600 via VS-114 DG/Hazmat Compliance) and
**Finance** (435 → 459 via VS-116 Surety/Bank Guarantee). Each gap had been previously overlooked
because it was genuinely uncovered by every value stream ('enterprise architecture' appeared in
zero PA files), referenced across many PA files with no dedicated owner (calibration/metrology
across 53 files), conflated with a fixed-site HSE capability (DG transport/ecommerce/regulatory vs
VS-24.3 storage safety), or reduced to single steps within B2G/B2B/treasury value streams
(performance bonds/surety in VS-46/VS-11/VS-18).

Pass 8 added one value stream each to **Finance** (459 → 483 via VS-118 Revenue Assurance),
**Asset & Infrastructure** (200 → 224 via VS-120 Energy Efficiency/RA 11285), and two to
**Governance & Assurance** (600 → 648 via VS-117 DTI-BPS Certification + VS-119 Ethics/Speak-Up).
This pass concentrates in Governance & Assurance and Finance because the remaining genuinely-
uncovered capabilities — after the thinner families (People, Technology & Data, Make & Move) were
substantially strengthened in Passes 4–7 — are statutory product-certification, revenue-leakage
protection, corporate-ethics/speak-up, and energy-efficiency compliance programs that naturally
live in those two families. Three of the four gaps (VS-117 elevating W447, VS-118 elevating W348,
VS-119 extending W2943) follow the Pass-1/Pass-5/Pass-7 pattern of elevating a single workflow to
a dedicated end-to-end program; the fourth (VS-120) is a genuinely-uncovered statutory program.

The 96 new workflows added in Pass 8 are currently **unclassified** (counted in the 2,445-workflow
unclassified total) and will be tier-assigned in a follow-up criticality review, exactly as the
Pass 1 (VS-89–VS-92), Pass 2 (VS-93–VS-96), Pass 3 (VS-97–VS-100), Pass 4 (VS-101–VS-104),
Pass 5 (VS-105–VS-108), Pass 6 (VS-109–VS-112), and Pass 7 (VS-113–VS-116) batches were handled.
Several Pass 8 workflows are anticipated Tier 1 (DTI-BPS regulated-product gating/ICC-sticker/
market-surveillance controls, revenue-assurance pricing/promo/loyalty/refund/settlement integrity
and leakage-recovery controls, speak-up confidentiality/retaliation-protection/investigation-
independence controls, and RA 11285 designated-establishment/audit/reporting controls).

Pass 9 deliberately strengthened the thinnest family by workflow count — **People** (194 → 242,
+48 via VS-121 Talent Acquisition/Employer Brand & Candidate Experience + VS-123 Skilled-Trade
Apprenticeship/Vocational Education & Capability Pipeline) — and added one value stream each to
**Plan & Source** (356 → 380 via VS-122 Global Sourcing/Import Buying & Sourcing Agent Management)
and **Sell & Serve** (1,122 → 1,146 via VS-124 Sales Enablement/Product Knowledge Mastery &
Clienteling). Each gap had been previously overlooked because it was genuinely uncovered — the
defining terms 'candidate experience'/'career site'/'talent community', 'global sourcing'/'sourcing
agent'/'overseas buying office', 'apprenticeship program', and 'clienteling' each appeared in **zero**
PA files — with only incidental single-workflow references to the broader capability (employer
brand in 3 PA files, vocational/TESDA participation in 4, product knowledge in 33 with no dedicated
owner). After Passes 1–8 had filled the genuinely-uncovered *operational* and *statutory*
capabilities across Make & Move, Asset & Infrastructure, Technology & Data, Finance, and
Governance & Assurance, the remaining genuinely-uncovered capabilities are the *strategic
people-attraction and selling-effectiveness* disciplines that naturally live in People, Plan &
Source, and Sell & Serve. None of the four follows the single-workflow-elevation pattern; all four
are genuinely-uncovered strategic disciplines with no dedicated owner.

The 96 new workflows added in Pass 9 are currently **unclassified** (counted in the 2,541-workflow
unclassified total) and will be tier-assigned in a follow-up criticality review, exactly as the
Pass 1–Pass 8 batches were handled. Several Pass 9 workflows are anticipated Tier 1 (candidate
consent/RA 10173 and equal-opportunity controls in VS-121, sourcing sanctions/ABC and
import-vendor trade-compliance gating controls in VS-122, TESDA/DOLE apprenticeship-compliance
and trade-safety controls in VS-123, and clienteling RA 10173/associate-fairness and selling-
quality controls in VS-124).

Pass 10 added value streams to three families — **Finance** (483 → 507 via VS-125 Fraud
Management), **Technology & Data** (230 → 278 via VS-126 Customer Data Platform + VS-128 AI/ML
Governance, strengthening the thinnest-by-workflow family), and **Plan & Source** (380 → 404 via
VS-127 S&OP/IBP). Each gap had been previously overlooked because the capability was genuinely
unowned as a program — its defining terms appeared in zero or near-zero PA files ('fraud
orchestration', 'customer golden record', 'integrated business planning'/'IBP', and 'model risk
management'/'algorithmic fairness' respectively) with only incidental single-step references to the
broader capability scattered across multiple adjacent value streams (VS-23/VS-32/VS-58/VS-80/VS-13.2/
VS-118/VS-86 for fraud; VS-13/VS-29/VS-107/VS-10/VS-75 for the customer view; VS-02/VS-101/VS-33/
VS-106 for planning; VS-30.2/VS-27.3/VS-91/VS-113/VS-21 for AI). None of the four follows the
single-workflow-elevation pattern of Passes 1/5/7/8; all four are genuinely-unowned programs.

The 96 new workflows added in Pass 10 are currently **unclassified** (counted in the 2,637-workflow
unclassified total) and will be tier-assigned in a follow-up criticality review, exactly as the
Pass 1–Pass 9 batches were handled. Several Pass 10 workflows are anticipated Tier 1 (chargeback
representment/recovery and deduction-authorization/SoD controls in VS-125, identity-resolution/
consent-at-activation/DSAR controls in VS-126, demand-consensus/single-number-plan controls in
VS-127, and model-validation/fairness-testing/human-oversight/GenAI controls in VS-128).

---

## 5. Validation

`07-methodology/validate-repo.sh` passes with **0 errors** after the additions:

- Grand total (3,900) matches actual PA workflow header count (3,900). ✅
- All 1,167 classified workflow IDs resolve to a header. ✅
- No dangling workflow references in cross-reference docs. ✅
- No placeholder/skeleton workflow content. ✅
- All cross-document counts reconciled (README, executive-summary, value-stream-index,
  workflows/README, criticality classification, dependency map, touchpoint map,
  requirement-workflow-matrix). ✅

---

## 6. Remaining (deferred) gaps

- **Dark Store & Micro-Fulfillment (former VS-49)** and **Cooperative/Community Procurement (former
  VS-52)** — **filled** by VS-93 and VS-94 (Pass 2). No retired-number gaps remain. The retired VS
  numbers (49, 50, 51, 52) stay unused.
- **Marketplace Operator & Third-Party Seller Management** and **Equipment Leasing & Capital
  Equipment Finance** — **filled** by VS-95 and VS-96 (Pass 2).
- **Corporate Real Estate & Property Portfolio**, **Contingent & Outsourced Workforce**, **IT
  Asset & Technology Lifecycle**, and **Legal Operations/Litigation & IP** — **filled** by VS-97,
  VS-98, VS-99, and VS-100 (Pass 3); these four gaps had been previously overlooked because each
  was conflated with an adjacent covered capability (lease administration, employee HR, fixed-asset
  accounting, and corporate-governance/compliance/records respectively).
- **Merchandise Financial Planning/OTB**, **Compensation/Benefits/Total Rewards**, **HR Shared
  Services/EX/People Analytics**, and **Government Affairs/Industry Relations** — **filled** by
  VS-101, VS-102, VS-103, and VS-104 (Pass 4); as with Pass 3, each had been conflated with an
  adjacent covered capability (assortment/supply/corporate-budget, payroll processing, the
  employee lifecycle, and LGU/regulatory/labor-advocacy respectively).
- **Supply Chain Finance & Working Capital**, **Commodity & Input-Cost Risk**, **Strategic Key
  Account & Enterprise Customer**, and **On-Site Renewable Energy & Prosumer** — **filled** by
  VS-105, VS-106, VS-107, and VS-108 (Pass 5); each had existed only as a single workflow within
  another value stream (W324 SCF in VS-18, the incidental commodity-hedging reference, the
  sprinkled key-account mentions across VS-11/VS-43/VS-46, and the W111/W173 energy/solar
  monitoring workflows) or was conflated with an adjacent covered capability.
- **Store Remodel/Renovation/Lifecycle Refurbishment**, **Freight Procurement/Carrier
  Management/Freight Audit**, **Packaging/Pallet/RTI Management**, and **Corporate Project &
  Program Management Office (PMO)** — **filled** by VS-109, VS-110, VS-111, and VS-112 (Pass 6);
  each had been genuinely uncovered (remodel execution, packaging/pallet/RTI engineering), sprinkled
  across multiple value streams (freight-spend/carrier across VS-02.2/VS-04/VS-06.1/VS-06.3), or
  conflated with the financial-accounting view of an asset (capex accounting in VS-40 vs
  project-portfolio governance).
- **Enterprise Architecture/Application Portfolio/Technology Strategy**, **Dangerous Goods/Hazmat
  Transport/Ecommerce/Regulatory Compliance**, **Calibration/Metrology/Measurement Traceability**, and
  **Performance Bond/Surety/Bank Guarantee Management** — **filled** by VS-113, VS-114, VS-115, and
  VS-116 (Pass 7); each had been genuinely uncovered by every value stream ('enterprise architecture'
  in zero PA files), referenced across many PA files with no dedicated owner (calibration/metrology
  across 53 files), conflated with a fixed-site HSE capability (DG transport vs VS-24.3 storage), or
  reduced to single steps within B2G/B2B/treasury value streams (performance bonds/surety).
- **DTI-BPS Product Standards Certification & PS Mark/ICC Compliance**, **Revenue Assurance/Pricing
  Integrity/Leakage Management**, **Whistleblower/Ethics & Corporate Integrity (Speak-Up) Program**,
  and **Energy Efficiency & Conservation & RA 11285 Compliance** — **filled** by VS-117, VS-118,
  VS-119, and VS-120 (Pass 8); three were elevations of a single workflow to a dedicated program
  (W447 DTI-BPS in VS-22.1, W348 Revenue Assurance in VS-21.3, W2943 ABC-Whistleblower in VS-86.3)
  and one was genuinely uncovered with only incidental references (RA 11285 energy-efficiency
  compliance across 14 PA files with zero dedicated headers).
- **Talent Acquisition/Employer Brand & Candidate Experience**, **Global Sourcing/Import Buying &
  Sourcing Agent Management**, **Skilled-Trade Apprenticeship/Vocational Education & Capability
  Pipeline**, and **Sales Enablement/Product Knowledge Mastery & Clienteling** — **filled** by
  VS-121, VS-122, VS-123, and VS-124 (Pass 9); all four were genuinely uncovered strategic
  disciplines whose defining terms ('candidate experience'/'career site'/'talent community',
  'global sourcing'/'sourcing agent'/'overseas buying office', 'apprenticeship program', and
  'clienteling') each appeared in zero PA files, with only incidental single-workflow references to
  the broader capability (employer brand in 3 files, vocational/TESDA participation in 4, product
  knowledge in 33 with no dedicated owner).
- **Cross-Channel Fraud Management & Payment Fraud Protection**, **Customer Data Platform/Single
  Customer View & Identity Resolution**, **Sales & Operations Planning (S&OP) & Integrated Business
  Planning**, and **AI/ML Governance & Responsible AI** — **filled** by VS-125, VS-126, VS-127, and
  VS-128 (Pass 10); all four were genuinely-unowned programs whose defining terms ('fraud
  orchestration', 'customer golden record', 'integrated business planning'/'IBP', and 'model risk
  management'/'algorithmic fairness') appeared in zero or near-zero PA files, with only incidental
  single-step references to the broader capability scattered across multiple adjacent value
  streams.
- **Competition & Antitrust Compliance (RA 10667/PCC)**, **Corporate Development/M&A/Divestiture**,
  **Human Rights/Responsible Supply Chain DD**, and **Corporate Political Engagement/Election
  Compliance** — **filled** by VS-129, VS-130, VS-131, and VS-132 (Pass 11); one was an elevation
  of a single workflow (W2683 competition-law compliance in VS-76.2 → VS-129) and three were
  genuinely uncovered disciplines whose defining terms ('merger and acquisition'/'divestiture',
  'human rights'/'modern slavery', 'political contribution'/'election compliance'/'COMELEC') each
  appeared in zero (or only one incidental) PA file.
- No further capability gaps are currently outstanding against the model company profile.
  Future business-model changes (e.g., used-material marketplace, customer construction-loan
  brokerage, captive insurance underwriting) may be re-evaluated in a future revision.

### Candidate gaps considered but rejected in Pass 7 (adequate coverage)

- **Tax controversy / BIR audit defense / CTA appeal** — covered by W77 (BIR Audit Response) in
  VS-22, with a detailed LOA → investigation → FAN → protest → CTA-appeal lifecycle (separate from
  VS-79 tax filing).
- **Real Property Tax (RPT) assessment, payment & appeal** — covered by W119 (RPT Management) in
  VS-79 and referenced across VS-97/VS-42/VS-76 as owner/lessor/LGU.
- **Insurance claims management & subrogation** — covered by the dedicated PA-26.3 (Insurance
  Claims and Policy Management) in VS-26, including adjuster, settlement, and subrogation.
- **Special / custom / made-to-order lifecycle** — covered by W744 (Store-Level Special Order
  Follow-Up), W545 (special orders), and W38 (special order fulfillment) across VS-09/VS-11.
- **Merchandise allocation / initial distribution** — covered for new stores (VS-37 allocation
  planning) and cross-dock (VS-04); replenishment allocation in VS-02.
- **Loyalty points liability / breakage / reward economics** — covered by VS-13 (loyalty) and
  VS-17.4 (W1405 PFRS 15 deferred-revenue allocation, breakage accounting).
- **Market development funds / co-op advertising / vendor-funded marketing** — covered by W513
  (co-op advertising) in VS-39 and VS-14 marketing.
- **Trade show / exhibition / industry-event representation** — covered by W1899 (Trade Show
  Participation & Industry Event Representation) in VS-43.3 and W1292 (Builder's Expo) in VS-07.1.
- **Fire & life-safety systems management** — covered across VS-24 (HSE), VS-20.3 (facilities),
  and VS-07.2 (store facility/safety), including BFP FSIC and suppression inspections.
- **Data platform / data engineering / analytics operations** — covered by VS-28.2 (Data
  Engineering and Quality) and VS-27.2 (Infrastructure and Platform).
- **Management accounting / cost center / profitability analytics** — covered by VS-17.4 FP&A
  (W1405 Store-Level P&L/Contribution Margin, W85 Product Costing & Margin Analysis Review) and
  VS-33.2 corporate performance management (W1655/W1656 store/category performance review).
- **Performance/capacity of PA 53-file 'calibration' mentions** — *considered as elevation*
  (like Pass 5 elevated W324 SCF) but elevated here to a dedicated value stream (VS-115) because the
  references had no owning PA and spanned revenue, quality, compliance, and HSE impact.

### Candidate gaps considered but rejected in Pass 9 (adequate coverage)

- **In-store events / DIY workshops / community engagement** — covered comprehensively by PA-12.3
  (Workshops & Events, 10 workflows: W147/W906/W1289/W1377/W1378/W1379/W1556/W1557 incl. instructor
  recruitment, registration/waitlist, vendor demo days, TESDA/school career-day participation, and
  seasonal workshop series with conversion-funnel management).
- **Supplier ESG / sustainable sourcing / responsible procurement** — covered by VS-25.2 (W195
  Sustainable Sourcing & Ethical Vendor Audit, W1176 Green Procurement & Sustainable Vendor
  Certification, W1480 Supplier Diversity), VS-78 green-building product curation, and source-side
  audits in VS-122.2/VS-31/VS-41; three dedicated workflows within ESG plus the new global-sourcing
  source-side governance make this substantially covered.
- **Organizational design / capability framework / strategic workforce planning** — covered by
  VS-103.3 (People Analytics, Workforce Planning & HR Technology) for workforce planning and
  VS-102.1 (Job Architecture, Pay Structure & Market Benchmarking) for job architecture/org-design
  inputs, with VS-33.1 corporate planning linkage; the *strategic* org-design layer is owned across
  these rather than as a standalone value stream.
- **B2B punchout / hosted catalog / procurement integration** — covered by W1242 (E-Commerce B2B
  Corporate Punchout Catalog & Procurement Integration, cXML/OCI) in VS-10.1 plus VS-11 trade/B2B
  and VS-65 marketplace integration.
- **Vendor EDI / ASN / B2B integration** — covered by VS-03.4 (Vendor Portal & Collaboration),
  VS-110.2 (Freight Execution/Routing Guide/Visibility), VS-15.1 (Invoice Processing & Matching),
  and the integration architecture in VS-113; EDI/ASN is a system-of-record integration discipline
  distributed across these rather than a standalone operational value stream.
- **Insurance program / risk financing / total cost of risk** — covered by PA-26.3 (Insurance
  Claims & Policy Management, incl. W862 annual renewal and W1565 annual portfolio review/coverage-
  gap analysis/market benchmarking) in VS-26.
- **Construction-site / jobsite HSE (DOLE D.O. 13)** — covered by W789 (Construction Safety
  Management & DOLE DO 13 Compliance) in VS-20.2 for BuildRight construction projects, with field
  safety for dispatched crews in VS-12.1/VS-24.
- **Open innovation / R&D / corporate venture / pilot-to-scale** — covered by VS-30.1 (Emerging
  Technology & PoC, incl. W691 scouting/evaluation and W690 digital-transformation portfolio) and
  VS-30.2 (AI/ML & Automation); emerging tech is owned there rather than as a standalone value
  stream.
- **Clienteling-adjacent: personalization / recommendation engine / customer 360** — covered by
  W200 (AI personalization/recommendation) in VS-30.2, VS-13.3 (Customer Data & CRM), and the new
  VS-124 clienteling tool (W3844); the *data/ML* layer is owned across these, while VS-124 owns the
  *associate-side selling* discipline that was the genuine gap.

### Candidate gaps considered but rejected in Pass 8 (adequate coverage)

- **Product Information Management (PIM) / Digital Asset Management (DAM) / product-content
  production** — covered by PA-01.3 (Product Information & Content: W50 PIM, W1346 multilingual
  localization, W1345 barcode/GS1, W1465 SDS, W1466 seasonal content staging), VS-10 (ecommerce),
  and VS-48 (retail media). The 'content factory' (photo studio, syndication to marketplaces) is
  substantially covered across VS-01.3/VS-10/VS-65.
- **Vendor compliance / routing guide / ASN / inbound appointment / compliance chargeback** —
  covered by VS-110.2 (Freight Execution, Routing Guide & Visibility), W1168 (DSD Receiving & Vendor
  Compliance), VS-04 (DC receiving), VS-03 (vendor mgmt), and VS-67 (vendor scorecard).
- **Fleet asset lifecycle / telematics / vehicle management** — covered comprehensively by VS-06
  (W199 telematics, W799 vehicle acquisition/registration/disposal, W1348 preventive maintenance,
  W1349 tires, W197 driver, W653 accident) and VS-61 (W2310–W2333 fleet cost/TCO).
- **Organized retail crime (ORC) / refund & return fraud / loyalty-points / gift-card fraud** —
  covered comprehensively by VS-23 (W840/W1542/W1337 ORC, W841/W1336 refund fraud, W1475 coupon
  abuse, W1476 gift-card fraud, W1338 employee theft).
- **Product liability / consumer-safety incident / customer-injury claims** — covered by W185
  (Product Liability & Consumer Safety Incident Management) in VS-22.3, W863 (Third-Party Liability
  & Customer Incident Insurance Response) and W1566 (Store-Level Slip-and-Fall/Customer-Injury
  Claims) in VS-26.3, VS-100 (legal/litigation), and VS-89 (recall).
- **B2B project job costing / progress billing / retention money** — covered by VS-11 (W165
  Project Retention & Milestone Billing, W918 Project Budget & Cost-Variance, W1134 Retention
  Release, W1288/W1426 Progress Billing & Milestone Collection, W1024 Material Escrow).
- **Diversity, Equity, Inclusion & Belonging (DEIB)** — covered by dedicated workflows W3343
  (VS-103.2) and W719 (VS-19.1).
- **Carbon / GHG / Scope 1-2-3 / net-zero accounting** — covered by W192 (GHG Tracking in
  VS-25.1) and W3466 (GHG Reduction & Scope 2 Attribution in VS-108.3), within the ESG (VS-25) and
  renewable (VS-108) programs.
- **Pricing / markdown / price optimization** — covered by VS-01.2 (Pricing & Promotions),
  VS-57 (Competitive Price Intelligence), and VS-101 (Merchandise Financial Planning/OTB/Margin).
- **Energy & utilities consumption management / procurement** — covered by W111 (utility bill),
  VS-25.1 (environmental monitoring), VS-108 (own generation); the *RA 11285 statutory
  compliance / ISO-50001 / ECM program* dimension is now filled by VS-120.
- **Tool / equipment repair & service center** — covered by VS-12 (Installation & Repair Services).
- **AI / model-risk governance / responsible AI** — covered by VS-30.2 (AI/ML & Automation) and
  VS-113 (Enterprise Architecture); emerging and not yet a standalone operational program for the
  current model company.

---

*Date: 2026-06-15 · Back to [Workflow Index](README.md) · [Value Stream Index](value-stream-index.md)*
