# BuildRight Depot Corp. — Executive Summary

> One-page overview of the model company and its hybrid IT landscape — a unified cloud ERP core with best-of-breed edges and in-house builds — for C-suite stakeholders.

---

## The Company

**BuildRight Depot Corp.** is a model big-box hardware/home improvement retail chain in the Philippines, operating with all its capabilities and systems fully enabled on a hybrid landscape (adopted 2026-09-03): a **unified cloud ERP core** provided by a theoretical software vendor, surrounded by **best-of-breed** edge products and **in-house built** differentiating platforms (see `07-methodology/capability-sourcing-and-engineering-model.md`).

| Parameter | Value |
|---|---|
| Format | Hardware / DIY / Home Improvement Big Box |
| Stores | 200 (nationwide: Luzon, Visayas, Mindanao) |
| Distribution Centers | 4 (Davao, Cebu, Laguna, Clark) |
| HQ | Davao City, Philippines |
| Legal Entities | 5 (Holdings, Depot, Logistics, Digital Commerce, Property Mgmt) |
| Annual Revenue | ~PHP 62.3 Billion |
| Employees | 6,762 |
| Active SKUs | 35,000 |
| POS Terminals | 600 (3 per store) |
| Monthly Transactions | 2.8 million |
| Ecommerce | Yes — BOPIS (Buy Online, Pick Up In Store) + Home Delivery |
| Loyalty Members | ~600,000 |

---



## IT Landscape (Hybrid — Unified Core + Bought Edges + Built Differentiators)

The business runs on a unified cloud ERP **core**, with specialist edges bought best-of-breed and differentiating capabilities built in-house:

| Platform | Provider | Status |
|---|---|---|
| Unified Cloud ERP (financials, P2P, inventory ledger, POS, HR/payroll, approvals) | Theoretical Software Vendor | Fully Operational (core) |
| Best-of-breed WMS / TMS / Store WFM / Field Service | Specialist vendors (registered sourcing decisions) | Fully Operational (edges) |
| Order Orchestration (OMO) · Trade & Project Services (TPS) | Built in-house (SEP paved road) | Fully Operational (differentiators) |
| AI & Agent Platform (AAP) | Built in-house on bought foundation-model APIs (VS-128 governance) | Fully Operational (agentic automation) |

---

## Critical Requirements

The ERP must handle these non-negotiables:

1. **High-volume retail POS** — 2.8M transactions/month, 600 terminals, offline capability (≥ 8 hours), real-time event-driven architecture
2. **Multi-entity Philippine operations** — 5 legal entities with intercompany consolidation, BIR (Bureau of Internal Revenue) compliance (VAT, EWT/Expanded Withholding Tax, income tax), SSS (Social Security System)/PhilHealth (Philippine Health Insurance)/Pag-IBIG (Home Development Mutual Fund) payroll
3. **Complex supply chain** — 4 DCs, import management (LC, customs, landed cost), catch-weight items (lumber, wire), consignment, VMI
4. **Omnichannel with multi-origin fulfillment** — BOPIS + home delivery + ship-from-store + drop-ship with real-time inventory sync across 200 stores; mixed-basket orders from a single POS transaction
5. **Scalability** — must grow to 300+ stores without architectural limits

---

## Key Operational Metrics

| Metric | Target | Rationale |
|---|---|---|
| POS uptime | 99.9% | Revenue stops if registers go down |
| POS offline endurance | ≥ 8 hours | Philippine internet reliability |
| Month-end close | ≤ 5 working days | Financial reporting agility |
| Inventory accuracy | ≥ 97% | Shrinkage control at PHP 62B scale |

---

## Repository Structure

```
erpplans/
├── 01-model-company/       ← Company profile, requirements, and workflows (LIVE)
└── 07-methodology/         ← Technical guidelines & reference specs (partial; further methodology docs pending platform selection — see 07-methodology/README.md)
```

---

## Ongoing Operations & Maintenance

1. Monitor live interfaces and transaction queues across all 200 stores and 4 distribution centers.
2. Maintain compliance with BIR requirements, including e-invoicing and statutory reporting.
3. Review nightly intercompany reconciliations and monthly financial consolidation routines.
4. Periodically audit active workflows against standard operating procedures.

---

*Date: 2026-09-03 (updated counts: 728 requirements, 5,370 workflows across 188 value streams, 6,762 employees — W5515–W5517 capability-sourcing & engineering workflows added in VS-113 by the sourcing-model gap-fill pass, owning the hybrid sourcing machinery end-to-end (W5515 Sourcing Decision Gate Operation & Capability Sourcing Register in PA-113.3, W5516 Best-of-Breed Product Lifecycle Management, Vendor Release Intake & Exit Reserves in PA-113.2, W5517 SEP Paved Road & Engineering Standard Governance for Built Products in PA-113.1 — sourcing model §3–§9); prior 2026-09-03: W5512–W5514 agentic-AI platform lifecycle workflows added in VS-128.3 by the agentic gap-fill pass, owning the sourcing-model §12 agent lifecycle end-to-end (intake/sourcing/registration, shadow & canary evaluation with autonomy-tier ratification, runtime/guardrail/kill-switch telemetry with quarterly re-registration & sunset); W5511 gift-card dormancy/escheat/expired-liability derecognition added in VS-54.3 by the event-custody pass; the IT landscape re-framed by the hybrid capability-sourcing decision — unified ERP core + best-of-breed edges + in-house OMO/TPS differentiators on the SEP paved road — plus the AI & Agent Platform agentic extension, per `07-methodology/capability-sourcing-and-engineering-model.md` and `07-methodology/it-product-operating-model.md`; prior 2026-08-26: post-catalog batch 5 added — W5510 supplier service-fee billing & account deduction for store-rendered services (barcode labels & promotional collaterals), transposing the concessionaire W5507 pattern onto merchandise suppliers and settling via W770 debit memos against AP — joining the 2026-08-24/25/26 thirteen: fringe benefits tax determination & quarterly BIR 1605 filing, unfulfilled-demand & lost-sales capture, concession item catalog/barcode/label governance, concessionaire self-service price change & label-first propagation, concession service-fee billing, restricted-substance & chemical-content product compliance, extreme-heat work interruption & heat-stress management, POSH/Safe Spaces CODI, RA 11165 telecommuting, director education, customer digital accessibility/WCAG, climate physical & transition risk, and employee financial wellness).
*Corrected 2026-08-24 — consistency review #25:* the 2026-06-25 footer below recorded 733 requirements; review #22 (2026-08-24) subsequently removed five exact-duplicate requirement rows (733 → 728; 429 Must / 293 Should / 6 Nice). Original 2026-06-25 note: VS-127 PA-127.4 added — 8 workflows W5489–W5496 — specializing the S&OP/IBP consensus cycle for BuildRight's PH-retail context; total headcount 6,757 → 6,762 with the dedicated S&OP/IBP sub-team in Supply Chain & Logistics; VS-49–VS-52 retired after placeholder-content review; VS-89–VS-192 added across thirty gap-analysis passes — see [CHANGELOG.md](../CHANGELOG.md) and [`workflow-gap-analysis.md`](workflows/workflow-gap-analysis.md) for per-pass detail.*
