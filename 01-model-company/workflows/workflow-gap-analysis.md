# Workflow Gap Analysis — BuildRight Depot Corp.

> Methodology and results of the operational workflow gap analysis (Pass 1, Pass 2, and Pass 3,
> all 2026-06-14).
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
   distinct from adjacent ones.
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

### Family subtotal impact (cumulative after Pass 1 + Pass 2 + Pass 3)

| Family | After Pass 2 | After Pass 3 (current) |
|---|---|---|
| Plan & Source | 308 | 308 |
| Make & Move | 307 | 307 |
| Sell & Serve | 1,098 | 1,098 |
| Finance | 411 | 411 |
| People | 122 | **146** (+24) |
| Asset & Infrastructure | 104 | **128** (+24) |
| Governance & Assurance | 528 | **552** (+24) |
| Technology & Data | 158 | **182** (+24) |
| **Grand total** | **3,036** | **3,132** (+96) |
| Value streams | 92 | **96** (+4) |
| Process areas | 280 | **292** (+12) |

The 96 new workflows added in Pass 3 are currently **unclassified** (counted in the 1,965-workflow
unclassified total) and will be tier-assigned in a follow-up criticality review, exactly as the
Pass 1 (VS-89–VS-92) and Pass 2 (VS-93–VS-96) batches were handled. Several Pass 3 workflows are
anticipated Tier 1 (intercompany rent transfer-pricing benchmarking and PFRS 40 fair-value
measurement, DOLE D.O. 174 labor-only-contracting compliance and misclassification defense,
software license compliance-audit response, lease/investment-property impairment, and litigation
loss-contingency accrual under PFRS/IAS 37).

---

## 5. Validation

`07-methodology/validate-repo.sh` passes with **0 errors** after the additions:

- Grand total (3,132) matches actual PA workflow header count (3,132). ✅
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
- No further capability gaps are currently outstanding against the model company profile.
  Future business-model changes (e.g., used-material marketplace, customer construction-loan
  brokerage, captive insurance underwriting) may be re-evaluated in a future revision.

---

*Date: 2026-06-14 · Back to [Workflow Index](README.md) · [Value Stream Index](value-stream-index.md)*
