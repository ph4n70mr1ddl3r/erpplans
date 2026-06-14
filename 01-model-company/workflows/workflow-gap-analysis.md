# Workflow Gap Analysis — BuildRight Depot Corp.

> Methodology and results of the 2026-06-14 operational workflow gap analysis.
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

1. **Inventory** the existing 88 value streams (268 process areas, 2,940 workflows) grouped by the
   8 operating families (Plan & Source, Make & Move, Sell & Serve, Finance, People, Asset &
   Infrastructure, Governance & Assurance, Technology & Data).
2. **Map** each major operational domain in the model company profile (merchandising, supply
   chain, store operations, POS/ecommerce, finance, HR, assets, governance/compliance, IT/data)
   to the value stream(s) that cover it.
3. **Flag gaps** where a domain had no dedicated value stream, only partial coverage, or was a
   known retired value stream (VS-49/50/51/52) not yet re-introduced.
4. **Validate** each candidate gap by keyword search across all PA files to confirm it is not
   already covered (avoiding redundant value streams) and to scope it so the new value stream is
   distinct from adjacent ones.
5. **Prioritize** gaps by operational criticality, regulatory exposure, and volume, and select the
   set to fill in this revision.

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
| 9 | Marketplace Operator & Third-Party Seller Management | BuildRight operating its own 3P marketplace to expand assortment | **New gap (2026-06-14)** — VS-48 retail media and VS-65 marketplace presence (selling on Lazada/Shopee) did not cover BuildRight as marketplace operator | **FILLED — VS-95** |
| 10 | Equipment Leasing & Capital Equipment Finance | B2B lease/lease-to-own for expensive contractor equipment (generators, scaffolding, solar, HVAC) | **New gap (2026-06-14)** — VS-12 short-term tool rental and VS-38 consumer credit did not cover B2B multi-year equipment leasing | **FILLED — VS-96** |

### Candidate gaps considered but rejected (adequate coverage)

- **Strategic sourcing / RFP** — covered by VS-03 vendor management.
- **Loyalty / coalition partnerships** — covered by VS-13.
- **Tax compliance** — covered by VS-79 / VS-87.
- **Anti-counterfeit / product authentication** — covered by VS-71.
- **Trade credit / AR risk** — covered by VS-16 / VS-68.
- **Treasury / FX / intercompany** — covered by VS-18 / VS-72.

---

## 4. New Value Streams Added (2026-06-14)

**Pass 1** (initial gap analysis, W2993–W3088): four value streams, 12 process areas, 96 workflows:

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-89](VS-89-product-recall-safety-corrective-action/README.md) | Product Recall & Safety Corrective Action Management | Governance & Assurance | 3 | 24 | W2993–W3016 |
| [VS-90](VS-90-damage-claims-freight-recovery/README.md) | Damage, Claims & Freight Recovery Management | Make & Move | 3 | 24 | W3017–W3040 |
| [VS-91](VS-91-consumer-data-privacy-protection/README.md) | Consumer Data Privacy & Data Protection Program | Governance & Assurance | 3 | 24 | W3041–W3064 |
| [VS-92](VS-92-kitting-bundling-build-to-order-assembly/README.md) | Kitting, Bundling & Build-to-Order Assembly Operations | Make & Move | 3 | 24 | W3065–W3088 |

**Pass 2** (this revision, W3089–W3184): four value streams, 12 process areas, 96 workflows,
distributed across four families:

| VS | Value Stream | Family | Process Areas | Workflows | W-range |
|---|---|---|---|---|---|
| [VS-93](VS-93-dark-store-micro-fulfillment/README.md) | Dark Store & Micro-Fulfillment Operations | Make & Move | 3 | 24 | W3089–W3112 |
| [VS-94](VS-94-cooperative-community-enterprise-procurement/README.md) | Cooperative & Community Enterprise Procurement | Plan & Source | 3 | 24 | W3113–W3136 |
| [VS-95](VS-95-marketplace-operator-third-party-seller/README.md) | Marketplace Operator & Third-Party Seller Management | Sell & Serve | 3 | 24 | W3137–W3160 |
| [VS-96](VS-96-equipment-leasing-capital-equipment-finance/README.md) | Equipment Leasing & Capital Equipment Finance | Finance | 3 | 24 | W3161–W3184 |

### Family subtotal impact (cumulative after Pass 1 + Pass 2)

| Family | Before Pass 1 | After Pass 1 | After Pass 2 (current) |
|---|---|---|---|
| Plan & Source | 260 | 260 | **308** (+48) |
| Make & Move | 235 | 283 | **307** (+24) |
| Sell & Serve | 1,050 | 1,074 | **1,098** (+24) |
| Finance | 363 | 387 | **411** (+24) |
| Governance & Assurance | 480 | 528 | 528 |
| **Grand total** | **2,844** | **2,940** | **3,036** (+96) |
| Value streams | 84 | 88 | **92** (+4) |
| Process areas | 256 | 268 | **280** (+12) |

The 96 new workflows added in Pass 2 are currently **unclassified** (counted in the unclassified
 total) and will be tier-assigned in a follow-up criticality review. Several are anticipated
 Tier 1 (marketplace seller KYB/payout, lease credit underwriting and Truth-in-Lending disclosure,
 dark-store dispatch SLA for ecommerce promise, cooperative fair-trade pricing).

---

## 5. Validation

`07-methodology/validate-repo.sh` passes with **0 errors** after the additions:

- Grand total (3,036) matches actual PA workflow header count (3,036). ✅
- All 1,167 classified workflow IDs resolve to a header. ✅
- No dangling workflow references in cross-reference docs. ✅
- No placeholder/skeleton workflow content. ✅
- All cross-document counts reconciled (README, executive-summary, value-stream-index,
  workflows/README, criticality classification, dependency map, touchpoint map,
  requirement-workflow-matrix). ✅

---

## 6. Remaining (deferred) gaps

- **Dark Store & Micro-Fulfillment (former VS-49)** and **Cooperative/Community Procurement (former
  VS-52)** — **filled** in this revision by VS-93 and VS-94 respectively. No retired-number gaps
  remain. The retired VS numbers (49, 50, 51, 52) stay unused.
- **Marketplace Operator & Third-Party Seller Management** and **Equipment Leasing & Capital
  Equipment Finance** — **filled** in this revision by VS-95 and VS-96 respectively (new gaps
  identified and filled in the same pass).
- No further capability gaps are currently outstanding against the model company profile.
  Future business-model changes (e.g., used-material marketplace, customer construction-loan
  brokerage, captive insurance underwriting) may be re-evaluated in a future revision.

---

*Date: 2026-06-14 · Back to [Workflow Index](README.md) · [Value Stream Index](value-stream-index.md)*
