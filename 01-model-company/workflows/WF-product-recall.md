# Product Recall Management Workflows

> Workflows governing end-to-end product recall and safety compliance for BuildRight Depot Corp., covering recall risk assessment, customer notification, inventory quarantine, regulatory reporting, vendor recovery, and recall effectiveness verification. As a hardware/DIY retailer selling paints, chemicals, electrical equipment, power tools, and construction materials across 200 stores, BuildRight must maintain robust recall capabilities to comply with the Consumer Act (RA 7394), DTI regulations, FDA requirements (for regulated products), and DENR mandates (for hazardous materials).

Back to [Workflow Index](README.md)

---

## Workflows in This Domain

| Workflow | Name | Criticality |
|---|---|---|
| W873 | Product Safety Incident Triage & Recall Risk Assessment | Tier 1 |
| W874 | Product Recall Customer Notification Campaign Execution | Tier 1 |
| W875 | Product Recall Inventory Quarantine, Hold & Disposition | Tier 1 |
| W876 | Product Recall Regulatory Reporting & DTI/BIR/FDA Compliance | Tier 1 |
| W877 | Product Recall Vendor Recovery & Cost Reimbursement | Tier 2 |
| W878 | Product Recall Effectiveness Audit & Close-Out | Tier 2 |

---

## W873. Product Safety Incident Triage & Recall Risk Assessment

| Field | Detail |
|---|---|
| **Trigger** | Customer complaint involving injury or safety hazard, vendor recall notification, DTI/FDA safety advisory, or media report of product safety issue |
| **Frequency** | Estimated 20–30 safety incident triages per year; 3–5 escalate to formal recall assessment |
| **Volume** | Each triage involves 1–5 reported incidents; recall assessment may cover 1–50 SKUs across 200 stores |
| **Owner** | Quality & Compliance Manager |
| **Participants** | Merchandising Manager, Procurement Manager, Legal Counsel, LP Director, Store Operations Director, External Regulatory Consultant |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Log safety incident — capture: product details (SKU, batch/lot, manufacturer), incident description, customer injury/impact, date and store location, and source of report (customer, vendor, regulator, media) | Customer Service / Store Manager | Quality Manager | 30 min |
| 2 | Conduct immediate risk triage — classify severity: (a) Critical — serious injury or death risk, immediate action required, (b) High — injury risk with product in widespread distribution, (c) Medium — quality issue without safety risk, (d) Low — cosmetic or minor defect. For Critical: escalate to VP Operations within 1 hour | Quality Manager | VP Operations | 1 hour |
| 3 | Gather product and incident evidence — collect: (a) affected product sample from store/DC, (b) batch/lot traceability data from inventory system, (c) customer photos/medical report (if injury), (d) vendor communication regarding defect, (e) regulatory advisory (if applicable) | Quality Manager | LP Director | 4 hours |
| 4 | Convene Recall Assessment Committee — for Critical/High classifications: assemble Quality, Legal, Merchandising, Procurement, and Store Operations; present incident evidence; determine: (a) voluntary recall warranted, (b) mandatory recall (DTI-directed), (c) product hold pending investigation, (d) no action (document and monitor) | Quality Manager | VP Operations | 2 hours |
| 5 | Define recall scope — if recall warranted: (a) identify all affected SKUs and batch/lot numbers, (b) determine affected stores/DCs with current inventory, (c) identify all customers who purchased affected product (POS/loyalty data), (d) estimate inventory in customer hands, (e) define remedy (refund, replacement, repair) | Quality Manager | Merchandising Manager | 4–8 hours |
| 6 | Issue internal product hold — immediately block affected SKUs at POS (cannot be sold), ecommerce (remove from catalog), and warehouse (quarantine); notify all Store Managers via urgent communication | IT Operations / Merchandising | VP Operations | 1 hour |
| 7 | Prepare recall decision document — document risk assessment findings, recall scope, recommended action, financial impact estimate, and regulatory reporting requirements; obtain VP Operations and Legal sign-off | Quality Manager | VP Operations | 2 hours |

### System Touchpoints
- **CRM/Customer Service** — incident logging, customer complaint tracking
- **Inventory Module** — batch/lot traceability, store-level inventory lookup, product hold
- **POS System** — SKU blocking, sale prevention for recalled items
- **Ecommerce Platform** — product removal, customer notification
- **ERP LP Module** — incident evidence management
- **BI Dashboard** — product distribution analysis, customer purchase history

### Pain Points / Risks
- Batch/lot traceability may be incomplete — not all vendors provide lot-level data
- Customer identification depends on loyalty membership — cash customers without receipts are unreachable
- Time pressure for Critical recalls — every hour of delay increases customer exposure risk
- Media attention escalates quickly — social media amplifies product safety incidents
- Financial impact can be significant — recall costs include inventory loss, logistics, customer refunds, and brand damage
- International vendors may resist recall acknowledgment — jurisdictional complexity

### Staffing Implication
- Quality & Compliance Manager: recall assessment is a core responsibility
- Recall Assessment Committee: assembled per event (5–7 members)
- Legal Counsel: available within 2 hours for Critical events
- External regulatory consultant: on retainer for DTI/FDA liaison

### Time Estimate
- Per triage (no recall): 4–6 person-hours
- Per recall assessment: 20–40 person-hours over 1–3 days
- **Annual estimate: 25 triages × 5 hours + 4 recalls × 30 hours = 245 person-hours/year**

---

## W874. Product Recall Customer Notification Campaign Execution

| Field | Detail |
|---|---|
| **Trigger** | Recall decision approved (W873); regulatory authority mandates public notification |
| **Frequency** | 3–5 recall notification campaigns per year |
| **Volume** | Each campaign may need to reach 100–50,000 customers depending on product distribution |
| **Owner** | Corporate Communications / Quality Manager |
| **Participants** | Marketing Manager, CRM Manager, Store Manager, Legal Counsel, Customer Service Team, External PR Agency |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Identify affected customers — extract purchase history from POS/loyalty database: (a) loyalty members who purchased affected SKU within recall period, (b) customers who used registered credit card, (c) B2B/trade account customers, (d) ecommerce customers; generate notification list with contact details | CRM Manager | Quality Manager | 2–4 hours |
| 2 | Draft customer notification — prepare multi-channel messaging: (a) SMS (concise: product, risk, action), (b) email (detailed: product description, batch/lot, risk explanation, remedy instructions, contact number), (c) in-store signage (poster at entrance and affected department), (d) social media post (public advisory), (e) newspaper ad (for mandatory recalls); Legal reviews all messaging | Corporate Communications | Legal Counsel | 2–3 hours |
| 3 | Execute notification campaign — send SMS/email to identified customers; deploy in-store signage to all stores with affected inventory; post social media advisory; schedule newspaper ad if required | Corporate Communications | VP Operations | 2 hours (digital); 1–2 days (physical) |
| 4 | Activate customer service response — brief Customer Service team on recall details, remedy options (refund, replacement, disposal instruction), and escalation path; establish dedicated recall hotline; prepare FAQ document | Customer Service Manager | Quality Manager | 2 hours |
| 5 | Monitor customer response — track: (a) notification delivery rate (SMS/email), (b) customer contact volume (calls, emails, store visits), (c) product return rate, (d) customer sentiment (social media); report daily to Quality Manager | CRM Manager | Corporate Communications | 30 min daily during active recall |
| 6 | Weekly recall status communication — issue weekly update to customers (if recall duration > 2 weeks): return statistics, safety reminder, and extended remedy deadline; coordinate with DTI if mandatory recall | Corporate Communications | Quality Manager | 1 hour weekly |

### System Touchpoints
- **CRM/Loyalty System** — customer purchase history extraction, notification list generation
- **Communication Platform** — SMS blast, email campaign, social media posting
- **POS System** — return processing for recalled items (no-receipt return with recall code)
- **Customer Service Platform** — recall hotline, ticket categorization, FAQ management
- **ERP Document Management** — notification templates, recall signage assets
- **Social Media Management** — post scheduling, sentiment monitoring, response management

### Pain Points / Risks
- Customer notification reach is limited — only ~40% of transactions are linked to identifiable customers (loyalty or card)
- SMS blast may be filtered as spam — delivery rate target: 85%
- Customer frustration if recalled product is a critical construction material — may need urgent replacement coordination
- Social media backlash if recall is perceived as too slow or insufficient
- Multi-language notifications may be needed — English and Filipino minimum; regional languages for major markets
- Newspaper ad cost for mandatory recalls can be PHP 200,000–500,000 per publication

### Staffing Implication
- Corporate Communications Manager: lead for all notification campaigns
- CRM Manager: customer data extraction and notification execution
- Customer Service: additional staffing during active recalls (+2 agents)
- External PR Agency: for high-profile recall media management

### Time Estimate
- Per campaign: 15–30 person-hours over 1–4 weeks
- **Annual estimate: 4 campaigns × 22 hours = 88 person-hours/year**

---

## W875. Product Recall Inventory Quarantine, Hold & Disposition

| Field | Detail |
|---|---|
| **Trigger** | Recall decision approved (W873); product hold issued |
| **Frequency** | 3–5 recall events per year requiring inventory quarantine |
| **Volume** | Each recall may involve 1–50 SKUs across 200 stores + 4 DCs; inventory at risk: PHP 100,000–10,000,000 per event |
| **Owner** | Inventory Manager / Warehouse Manager |
| **Participants** | Store Manager, DC Manager, Quality Manager, Procurement Manager, Finance Controller, LP Officer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Activate inventory quarantine — system-wide hold on affected SKUs: (a) POS blocked from sale (error message: "Item recalled — do not sell"), (b) ecommerce removed from catalog, (c) WMS quarantine flag on DC inventory, (d) in-transit shipments intercepted and redirected | Inventory Manager | Quality Manager | 1 hour |
| 2 | Store-level physical quarantine — Store Manager isolates all affected inventory: (a) remove from sales floor and backroom, (b) tag with "RECALL — DO NOT SELL" label, (c) move to designated quarantine area, (d) count and record quantities, (e) photograph for documentation | Store Manager | LP Officer | 2–4 hours per store |
| 3 | DC-level quarantine — DC Manager segregates affected inventory: (a) quarantine zone in warehouse, (b) update WMS location to "RECALL HOLD", (c) verify batch/lot numbers against recall scope, (d) count and record; prevent any outbound picks | DC Manager | Warehouse Manager | 4–8 hours per DC |
| 4 | Determine disposition — based on recall type: (a) Return to Vendor — vendor accepts return and credits BuildRight, (b) Destroy On-Site — certified destruction with documentation (for hazardous or contaminated products), (c) Destroy via Licensed Facility — for regulated products requiring certified destruction, (d) Corrective Action — manufacturer provides repair kit or replacement stock | Quality Manager | Procurement Manager | 4 hours |
| 5 | Execute disposition — (a) Return: coordinate reverse logistics, ship to vendor-designated location, obtain receipt, (b) Destroy: engage licensed waste disposal contractor (for hazmat), conduct destruction with witness, certificate of destruction, (c) Corrective: receive manufacturer repair/replacement, inspect, and release to saleable inventory | Inventory Manager | Quality Manager | 1–2 weeks (elapsed) |
| 6 | Financial impact recording — write off destroyed inventory, record vendor credit memo for returns, post transportation and disposal costs, and update insurance claim if applicable | Finance Controller | Finance VP | 2–4 hours |
| 7 | Release quarantine — after disposition complete, update inventory system: remove hold for non-affected batches, adjust on-hand quantities, and release any substituted stock | Inventory Manager | Quality Manager | 1 hour |

### System Touchpoints
- **Inventory Module** — product hold/quarantine, batch/lot tracking, quantity adjustment
- **POS System** — sale blocking for recalled SKUs
- **WMS** — quarantine zone management, location update, pick prevention
- **Ecommerce Platform** — catalog removal, inventory sync hold
- **Finance Module** — inventory write-off, vendor credit memo, disposal cost recording
- **ERP LP Module** — quarantine documentation, destruction witness logging

### Pain Points / Risks
- Physical quarantine compliance at 200 stores is difficult to verify — some recalled items may remain on shelf
- Hazmat destruction requires DENR-licensed contractor — limited availability in provincial areas
- Return-to-vendor logistics cost may exceed inventory value for low-cost items — write-off more economical
- Batch/lot tracking gaps mean some affected inventory may not be identified — over-quarantine wastes good stock
- In-transit inventory requires carrier intercept — additional cost and complexity
- POS blocking must be instantaneous — any gap allows potential sale of recalled product

### Staffing Implication
- Inventory Manager: quarantine management (4–8 hours per recall)
- Store Managers: 2–4 hours per store per recall (200 stores × 3 hours = 600 hours per recall)
- DC Managers: 4–8 hours per DC per recall
- LP Officers: verification of store quarantine compliance

### Time Estimate
- Per recall: 700–800 person-hours chain-wide (mostly store-level physical quarantine)
- **Annual estimate: 4 recalls × 750 hours = 3,000 person-hours/year**

---

## W876. Product Recall Regulatory Reporting & DTI/BIR/FDA Compliance

| Field | Detail |
|---|---|
| **Trigger** | Recall decision approved (W873); mandatory reporting requirements triggered |
| **Frequency** | 3–5 regulatory reporting events per year |
| **Volume** | Each event requires submissions to 1–3 regulatory bodies |
| **Owner** | Quality Manager / Compliance Officer |
| **Participants** | Legal Counsel, Procurement Manager, Corporate Communications, External Regulatory Consultant |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Identify regulatory reporting requirements — determine which agencies require notification: (a) DTI — Consumer Act (RA 7394) mandatory recall reporting for consumer products, (b) FDA — for regulated products (paints, chemicals, electrical), (c) DENR — for hazardous materials, (d) BIR — for inventory write-off documentation, (e) DOH — if public health risk; note reporting deadlines (DTI: within 24 hours of recall decision) | Compliance Officer | Legal Counsel | 1 hour |
| 2 | Prepare regulatory submission — compile: (a) product identification and batch/lot details, (b) defect description and risk assessment, (c) number of affected units in market, (d) recall scope and remedy, (e) customer notification plan, (f) timeline of events, (g) corrective action plan; format per agency requirements | Quality Manager | Compliance Officer | 4–8 hours |
| 3 | Submit regulatory notification — file reports with required agencies within mandated timeframes; DTI typically requires formal letter + supporting documents; FDA may require online portal submission; obtain acknowledgment receipts | Compliance Officer | Legal Counsel | 2 hours |
| 4 | Respond to regulatory queries — agencies may request additional information, on-site inspection, or product sample submission; coordinate with Quality Manager and Legal for responses | Compliance Officer | Quality Manager | Variable |
| 5 | Submit progress reports — for ongoing recalls: file weekly/monthly progress reports to agencies showing: units recovered, customer notification reach, remaining inventory, and estimated completion date | Compliance Officer | Quality Manager | 2 hours per report |
| 6 | File final recall report — upon recall completion: submit comprehensive close-out report with total units recovered, disposition method, effectiveness assessment, and corrective actions implemented; obtain agency clearance | Quality Manager | Compliance Officer | 4 hours |

### System Touchpoints
- **ERP Compliance Module** — regulatory submission tracking, deadline management
- **Document Management** — regulatory templates, submission archive, acknowledgment receipts
- **Inventory Module** — recovery statistics, disposition documentation
- **CRM System** — customer notification reach metrics
- **BI Dashboard** — recall progress metrics for regulatory reporting

### Pain Points / Risks
- DTI 24-hour reporting deadline is tight — pre-approved templates needed for rapid submission
- FDA jurisdiction over hardware products (paints, chemicals) is complex — requires specialized knowledge
- Regulatory inspectors may visit stores to verify recall compliance — 200-store verification is logistically challenging
- BIR inventory write-off documentation requires specific format — non-compliance risks tax deduction denial
- Multiple agency submissions create administrative burden — Compliance Officer may be overwhelmed during concurrent recalls

### Staffing Implication
- Compliance Officer: regulatory reporting is core responsibility
- Quality Manager: technical content for submissions
- Legal Counsel: review all regulatory submissions before filing
- External regulatory consultant: for FDA and DENR submissions

### Time Estimate
- Per reporting event: 12–20 person-hours over 1–4 weeks
- **Annual estimate: 4 events × 16 hours = 64 person-hours/year**

---

## W877. Product Recall Vendor Recovery & Cost Reimbursement

| Field | Detail |
|---|---|
| **Trigger** | Recall disposition complete (W875); financial impact quantified |
| **Frequency** | 3–5 vendor recovery processes per year |
| **Volume** | Average recovery claim: PHP 200,000–5,000,000 depending on product and recall scope |
| **Owner** | Procurement Manager / Finance Controller |
| **Participants** | Quality Manager, Finance Controller, Legal Counsel, Vendor Account Manager, Insurance Coordinator |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Compile recall cost documentation — aggregate all costs: (a) inventory value at cost (destroyed or returned), (b) reverse logistics (return shipping, disposal), (c) customer refund cost, (d) customer service incremental cost, (e) regulatory compliance cost, (f) brand/marketing remediation cost, (g) business interruption (if product was top seller) | Finance Controller | Procurement Manager | 4–8 hours |
| 2 | Determine vendor liability — review: (a) vendor contract warranty/indemnity clause, (b) product defect root cause (manufacturing vs. BuildRight handling), (c) vendor insurance coverage, (d) force majeure exclusions; Legal Counsel advises on contractual position | Legal Counsel | Procurement Manager | 2–4 hours |
| 3 | Issue vendor recovery demand — send formal demand letter to vendor: cost breakdown, contractual basis for recovery, supporting documentation, and requested reimbursement timeline (30 days) | Procurement Manager | Legal Counsel | 2 hours |
| 4 | Negotiate settlement — vendor may: (a) accept full reimbursement via credit memo, (b) accept partial (dispute certain cost categories), (c) reject (claim force majeure or BuildRight fault); negotiate to resolution; for disputed claims > PHP 1 million, engage Legal for mediation | Procurement Manager | Finance VP | 4–20 hours (over 2–8 weeks) |
| 5 | Process vendor credit memo — upon agreement, record vendor credit in AP module; offset against future invoices or request direct payment; post recovery to recall cost center | Finance Controller | Finance VP | 2 hours |
| 6 | Insurance recovery coordination — if vendor recovery insufficient, coordinate with Insurance Coordinator for product liability or recall insurance claim (per W864); document unrecovered balance | Finance Controller | Insurance Coordinator | 2 hours |

### System Touchpoints
- **Finance Module** — recall cost center, vendor credit memo, recovery accounting
- **ERP Procurement Module** — vendor contract reference, communication history
- **Document Management** — demand letter, vendor response, settlement agreement
- **Legal Matter Management** — contract review, dispute tracking
- **Insurance Module** — product liability claim initiation (if applicable)

### Pain Points / Risks
- Vendor may be financially unable to reimburse — especially small/provincial vendors
- Contract indemnity clauses may have caps or exclusions that limit recovery
- Force majeure claims (natural disaster affecting vendor manufacturing) are difficult to dispute
- Recovery timeline (30–90 days) impacts cash flow — immediate write-off with later recovery creates accounting complexity
- International vendors may have different legal jurisdictions — enforcement is challenging
- Partial recovery is common — 60–80% recovery rate is typical for legitimate claims

### Staffing Implication
- Procurement Manager: lead negotiator for vendor recovery
- Finance Controller: cost documentation and recovery accounting
- Legal Counsel: contract interpretation and dispute support

### Time Estimate
- Per recovery: 15–35 person-hours over 4–12 weeks
- **Annual estimate: 4 recoveries × 25 hours = 100 person-hours/year**

---

## W878. Product Recall Effectiveness Audit & Close-Out

| Field | Detail |
|---|---|
| **Trigger** | Recall campaign nearing completion (typically 60–90 days after launch); or regulatory-mandated effectiveness check |
| **Frequency** | 3–5 recall close-outs per year |
| **Volume** | Each audit covers 1–50 SKUs across 200 stores + 4 DCs |
| **Owner** | Quality Manager / Compliance Officer |
| **Participants** | LP Director, Store Manager (sample), Finance Controller, Compliance Officer, External Auditor (for major recalls) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Calculate recall effectiveness metrics — compute: (a) % of affected inventory recovered (target: ≥ 80% for Critical recalls), (b) % of identified customers notified, (c) % of notified customers who responded, (d) % of customer remedies completed, (e) store-level compliance audit results | Quality Manager | VP Operations | 4 hours |
| 2 | Conduct store compliance spot-checks — LP Officers visit sample of 20–30 stores to verify: (a) recalled product not on sales floor, (b) POS block still active, (c) quarantine area clear, (d) signage removed (if recall concluded), (e) staff awareness of recall; document any non-compliance | LP Officer | LP Director | 4–8 hours (field visits) |
| 3 | Assess recall effectiveness against targets — compare actual recovery rate to target; for Critical recalls with < 80% recovery: extend recall campaign, increase notification frequency, or escalate to DTI (if mandatory); for non-Critical: document low recovery rationale | Quality Manager | VP Operations | 2 hours |
| 4 | Compile recall close-out report — comprehensive document including: (a) incident summary and root cause, (b) recall scope and timeline, (c) customer notification metrics, (d) inventory recovery and disposition, (e) vendor recovery outcome, (f) regulatory submissions and agency response, (g) total financial impact, (h) lessons learned and preventive actions | Quality Manager | Compliance Officer | 4–8 hours |
| 5 | Submit final report to regulatory agencies — file close-out report with DTI/FDA/DENR as required; obtain regulatory clearance; archive all documentation per retention policy (10 years for recall records) | Compliance Officer | Legal Counsel | 2 hours |
| 6 | Implement preventive actions — update: (a) vendor quality requirements for affected product category, (b) incoming inspection protocols, (c) product safety testing requirements, (d) vendor scorecard criteria; assign action owners and track completion | Quality Manager | Procurement Manager | 4 hours |
| 7 | Lift product hold (if replacement stock available) — once corrective action verified, remove POS block for non-affected batches; release new stock to stores; communicate to customers that safe product is available | Inventory Manager | Quality Manager | 2 hours |

### System Touchpoints
- **BI Dashboard** — recall effectiveness metrics, store compliance tracking
- **ERP LP Module** — store audit results, compliance documentation
- **Inventory Module** — hold removal, new stock release
- **POS System** — sale block removal for non-affected batches
- **Document Management** — close-out report archive, regulatory submission copies
- **Compliance Module** — recall record, preventive action tracking

### Pain Points / Risks
- Effectiveness rate of 80% is aspirational — actual rate may be 50–60% for low-cost items where customers don't bother returning
- Store compliance spot-checks cover only 10–15% of stores — non-compliant stores may be missed
- Regulatory close-out may take 3–6 months — recall file remains open consuming resources
- Preventive actions may require vendor investment (new testing, process changes) — vendor resistance likely
- Lifting product hold prematurely risks selling remaining affected stock — thorough verification essential

### Staffing Implication
- Quality Manager: close-out is 20% of total recall effort
- LP Officers: 4–8 hours for spot-checks per recall
- Compliance Officer: regulatory close-out coordination

### Time Estimate
- Per close-out: 20–30 person-hours over 2–4 weeks
- **Annual estimate: 4 close-outs × 25 hours = 100 person-hours/year**
