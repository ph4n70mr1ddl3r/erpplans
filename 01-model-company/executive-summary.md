# BuildRight Depot Corp. — Executive Summary

> One-page overview of the model company and monolithic ERP system architecture for C-suite stakeholders.

---

## The Company

**BuildRight Depot Corp.** is a model big-box hardware/home improvement retail chain in the Philippines, operating with all its capabilities and systems running under an optimized, monolithic model ERP platform provided by a theoretical software vendor.

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



## Monolithic ERP System

BuildRight is supported by a single, fully optimized monolithic ERP system running the entire business end-to-end:

| Platform | Provider | Status |
|---|---|---|
| Model Monolithic ERP | Theoretical Software Vendor | Fully Operational |

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
└── 07-methodology/         ← Operational guidelines and technical specifications (COMPLETE)
```

---

## Ongoing Operations & Maintenance

1. Monitor live interfaces and transaction queues across all 200 stores and 4 distribution centers.
2. Maintain compliance with BIR requirements, including e-invoicing and statutory reporting.
3. Review nightly intercompany reconciliations and monthly financial consolidation routines.
4. Periodically audit active workflows against standard operating procedures.

---

*Date: 2026-06-15 (updated counts: 733 requirements, 3,996 workflows across 132 value streams; VS-49/50/51/52 retired after placeholder-content review; VS-89/90/91/92 added via first gap-analysis pass — Product Recall, Damage & Claims, Consumer Data Privacy, Kitting & Bundling; VS-93/94/95/96 added via second gap-analysis pass — Dark Store & Micro-Fulfillment, Cooperative & Community Enterprise Procurement, Marketplace Operator & Third-Party Seller, Equipment Leasing & Capital Equipment Finance; VS-97/98/99/100 added via third gap-analysis pass — Corporate Real Estate & Property Portfolio, Contingent & Outsourced Workforce, IT Asset & Technology Lifecycle, Legal Operations/Litigation & IP; VS-101/102/103/104 added via fourth gap-analysis pass — Merchandise Financial Planning/OTB/Margin Management, Compensation/Benefits/Total Rewards, HR Shared Services/EX/People Analytics, Government Affairs/Public Policy/Industry Relations; VS-105/106/107/108 added via fifth gap-analysis pass — Supply Chain Finance & Working Capital Management, Commodity & Input-Cost Risk Management, Strategic Key Account & Enterprise Customer Management, On-Site Renewable Energy & Prosumer Asset Operations; VS-109/110/111/112 added via sixth gap-analysis pass — Store Remodel/Renovation/Lifecycle Refurbishment, Freight Procurement/Carrier Management/Freight Audit, Packaging/Pallet/RTI Management, Corporate Project & Program Management Office (PMO); VS-113/114/115/116 added via seventh gap-analysis pass — Enterprise Architecture/Application Portfolio/Technology Strategy, Dangerous Goods & Hazmat Transport/Ecommerce/Regulatory Compliance, Calibration/Metrology/Measurement Traceability Management, Performance Bond/Surety/Bank Guarantee Management; VS-117/118/119/120 added via eighth gap-analysis pass — DTI-BPS Product Standards Certification/PS Mark/ICC Compliance, Revenue Assurance/Pricing Integrity/Leakage Management, Whistleblower/Ethics & Corporate Integrity (Speak-Up) Program, Energy Efficiency/Conservation & RA 11285 Compliance Program; VS-121/122/123/124 added via ninth gap-analysis pass — Talent Acquisition/Employer Brand & Candidate Experience, Global Sourcing/Import Buying & Sourcing Agent Management, Skilled-Trade Apprenticeship/Vocational Education & Capability Pipeline, Sales Enablement/Product Knowledge Mastery & Clienteling; VS-125/126/127/128 added via tenth gap-analysis pass — Cross-Channel Fraud Management/Payment Fraud Protection, Customer Data Platform/Single Customer View & Identity Resolution, Sales & Operations Planning (S&OP)/Integrated Business Planning, AI/ML Governance & Responsible AI; VS-129/130/131/132 added via eleventh gap-analysis pass — Competition & Antitrust Compliance/RA 10667/PCC, Corporate Development/Mergers & Acquisitions/Divestiture & Strategic Transactions, Human Rights/Modern Slavery & Responsible Supply Chain Due Diligence, Corporate Political Engagement/Election Compliance & Public Affairs Governance; VS-133/134/135/136 added via twelfth gap-analysis pass — Operational Excellence/Process Mining/Continuous Improvement, Organizational Change Management/Digital Adoption/Transformation Enablement, Technology Business Management/IT Financial Management/Cloud FinOps, Supply Chain Network Design/Multi-Echelon Inventory Optimization/Flow Engineering)*
