# Workflow Gap Analysis — BuildRight Depot Corp.

> Methodology and results of the operational workflow gap analysis (Pass 1, Pass 2, Pass 3, Pass 4,
> and Pass 5, all 2026-06-14).
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
   distinct from adjacent ones. For Pass 4 and Pass 5, every candidate gap was confirmed to have
   only incidental single-workflow coverage (or none) in the existing PA files.
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

### Family subtotal impact (cumulative after Pass 1 + Pass 2 + Pass 3 + Pass 4 + Pass 5)

| Family | After Pass 3 | After Pass 4 | After Pass 5 (current) |
|---|---|---|---|
| Plan & Source | 308 | 332 | **356** (+24) |
| Make & Move | 307 | 307 | 307 |
| Sell & Serve | 1,098 | 1,098 | **1,122** (+24) |
| Finance | 411 | 411 | **435** (+24) |
| People | 146 | 194 | 194 |
| Asset & Infrastructure | 128 | 128 | **152** (+24) |
| Governance & Assurance | 552 | 576 | 576 |
| Technology & Data | 182 | 182 | 182 |
| **Grand total** | **3,132** | **3,228** | **3,324** (+96) |
| Value streams | 96 | 100 | **104** (+4) |
| Process areas | 292 | 304 | **316** (+12) |

Pass 4 deliberately strengthened the three thinnest operating families: **People** (the
thinnest at 4 value streams) received +2, and **Plan & Source** and **Governance & Assurance** each
received +1. Pass 5 added one value stream to each of four families (Plan & Source, Sell & Serve,
Finance, and Asset & Infrastructure — the last being the thinnest by value-stream count), targeting
capabilities that existed only as single workflows within another value stream (SCF / commodity
hedging / key account / own-generation) or were conflated with an adjacent covered one.

The 96 new workflows added in Pass 4 and the 96 added in Pass 5 are currently **unclassified**
(counted in the 2,157-workflow unclassified total) and will be tier-assigned in a follow-up
criticality review, exactly as the Pass 1 (VS-89–VS-92), Pass 2 (VS-93–VS-96), and Pass 3
(VS-97–VS-100) batches were handled. Several Pass 4 workflows are anticipated Tier 1
(open-to-buy/markdown-budget governance and merchandise P&A control, pay-equity analysis and
minimum-wage compliance, multi-entity statutory-benefits remittance governance, and
political-activity/anti-bribery compliance in government affairs), as are several Pass 5 workflows
(SCF facility/covenant governance and hedge-accounting controls, commodity hedge authority/SoD
and PFRS 9 hedge documentation, strategic-account credit-concentration disclosure and
anti-bribery controls, and renewable-asset net-metering/REC accounting and PFRS 16 treatment).

---

## 5. Validation

`07-methodology/validate-repo.sh` passes with **0 errors** after the additions:

- Grand total (3,324) matches actual PA workflow header count (3,324). ✅
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
- No further capability gaps are currently outstanding against the model company profile.
  Future business-model changes (e.g., used-material marketplace, customer construction-loan
  brokerage, captive insurance underwriting) may be re-evaluated in a future revision.

---

*Date: 2026-06-14 · Back to [Workflow Index](README.md) · [Value Stream Index](value-stream-index.md)*
