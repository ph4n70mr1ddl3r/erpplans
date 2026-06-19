# BuildRight Depot Corp. — Executive Summary

> One-page overview of the model company and unified cloud ERP system architecture for C-suite stakeholders.

---

## The Company

**BuildRight Depot Corp.** is a model big-box hardware/home improvement retail chain in the Philippines, operating with all its capabilities and systems running under an optimized, unified cloud ERP platform provided by a theoretical software vendor.

| Parameter | Value |
|---|---|
| Format | Hardware / DIY / Home Improvement Big Box |
| Stores | 200 (nationwide: Luzon, Visayas, Mindanao) |
| Distribution Centers | 4 (Davao, Cebu, Laguna, Clark) |
| HQ | Davao City, Philippines |
| Legal Entities | 5 (Holdings, Depot, Logistics, Digital Commerce, Property Mgmt) |
| Annual Revenue | ~PHP 62.3 Billion |
| Employees | 6,715 |
| Active SKUs | 35,000 |
| POS Terminals | 600 (3 per store) |
| Monthly Transactions | 2.8 million |
| Ecommerce | Yes — BOPIS (Buy Online, Pick Up In Store) + Home Delivery |
| Loyalty Members | ~600,000 |

---



## Unified Cloud ERP System

BuildRight is supported by a single, fully optimized unified cloud ERP system running the entire business end-to-end:

| Platform | Provider | Status |
|---|---|---|
| Unified Cloud ERP | Theoretical Software Vendor | Fully Operational |

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

*Date: 2026-06-20 (updated counts: 733 requirements, 4,956 workflows across 172 value streams; VS-49–VS-52 retired after placeholder-content review; VS-89–VS-176 added across twenty-four gap-analysis passes — see [CHANGELOG.md](../CHANGELOG.md) and [`workflow-gap-analysis.md`](workflows/workflow-gap-analysis.md) for per-pass detail).*
