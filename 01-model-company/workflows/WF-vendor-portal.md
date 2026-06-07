# Vendor Portal & Supplier Collaboration Workflows

> Workflows governing the supplier-facing digital portal platform that enables vendor self-service, collaboration, and transaction automation between BuildRight Depot and its ~800–1,000 active vendors. These workflows cover portal user management, PO acknowledgment, invoice submission, document exchange, dispute resolution, performance transparency, and RFQ/bid management — supporting the integration architecture's bidirectional supplier portal connecting vendors to the ERP system.

Back to [Workflow Index](README.md)

---

## Workflows in This Domain

| Workflow | Name | Criticality |
|---|---|---|
| W865 | Vendor Portal User Onboarding, Access Provisioning & Training | Tier 2 |
| W866 | Vendor Self-Service Purchase Order Acknowledgment & Confirmation | Tier 1 |
| W867 | Vendor Self-Service Invoice Submission & Payment Status Inquiry | Tier 1 |
| W868 | Vendor Catalog & Product Information Self-Service Management | Tier 2 |
| W869 | Vendor Dispute Resolution & Issue Ticketing | Tier 2 |
| W870 | Vendor Compliance Document Upload & Expiration Tracking | Tier 2 |
| W871 | Supplier Scorecard Portal Publication & Performance Transparency | Tier 2 |
| W872 | Vendor RFQ & Bid Submission Portal Management | Tier 2 |

---

## W865. Vendor Portal User Onboarding, Access Provisioning & Training

| Field | Detail |
|---|---|
| **Trigger** | New vendor approved (per procurement vendor onboarding workflow), or existing vendor requests portal access for additional users |
| **Frequency** | Estimated 30–50 new vendor onboardings per year; 100–200 additional user requests per year |
| **Volume** | ~800 active vendors × 2–3 users each = ~1,600–2,400 vendor portal users at steady state |
| **Owner** | Procurement Specialist / IT Portal Administrator |
| **Participants** | Vendor Contact, Procurement Manager, IT Portal Administrator, Vendor Account Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Receive vendor portal access request — triggered by vendor approval workflow or vendor-initiated request via email; verify vendor is active and approved in ERP vendor master | Procurement Specialist | Procurement Manager | 15 min |
| 2 | Create vendor portal account — provision user account with role-based access: (a) Order Management (view POs, confirm shipments), (b) Invoice Management (submit invoices, view payment status), (c) Catalog Management (update product info), (d) Full Access (all features + RFQ participation); assign to correct vendor entity | IT Portal Administrator | Procurement Manager | 15 min |
| 3 | Send portal credentials and welcome kit — email vendor contact with login credentials, portal URL, user guide (PDF), video tutorial link, and IT support contact; credentials expire in 7 days if not activated | IT Portal Administrator | Procurement Specialist | 10 min |
| 4 | Conduct vendor portal training (for strategic vendors, top 100 by spend) — 30-minute web-based training covering PO acknowledgment, invoice submission, document upload, and dispute ticketing; record attendance | Procurement Specialist | Procurement Manager | 30 min per session |
| 5 | Verify first login and confirm functionality — monitor vendor activation within 7 days; follow up with non-activated vendors; confirm first PO acknowledgment or invoice submission as validation | IT Portal Administrator | Procurement Specialist | 15 min |
| 6 | Quarterly portal user review — deactivate accounts for inactive vendors (> 90 days no login), remove access for terminated vendor contacts, and update role assignments | IT Portal Administrator | Procurement Manager | 2 hours quarterly |

### System Touchpoints
- **Vendor Portal Platform** — user provisioning, role management, activity logging
- **ERP Procurement Module** — vendor master verification, PO/invoice data exchange
- **Email System** — credential delivery, welcome kit distribution
- **LMS** — video tutorial hosting, training attendance tracking
- **IT Identity Management** — account lifecycle, deactivation rules

### Pain Points / Risks
- Vendor IT literacy varies — some provincial vendors may struggle with portal adoption
- Credentials may be shared among vendor staff — security risk; enforce per-user accounts
- Portal downtime during business hours disrupts vendor operations — 99.5% uptime SLA required
- Multi-entity vendor companies may need separate accounts per BuildRight entity (Holdings, Depot, Logistics)
- Vendor resistance to portal adoption — some prefer email/phone communication; mandate portal use for PO acknowledgment and invoicing

### Staffing Implication
- IT Portal Administrator: 0.5 FTE for vendor user management
- Procurement Specialist: training and follow-up (2 hours/week during ramp-up)
- Helpdesk: vendor portal support queue (estimated 10 tickets/day)

### Time Estimate
- Per vendor onboarding: 45 min
- Per additional user: 20 min
- **Annual estimate: 40 onboarding × 45 min + 150 user additions × 20 min + quarterly reviews = 110 person-hours/year**

---

## W866. Vendor Self-Service Purchase Order Acknowledgment & Confirmation

| Field | Detail |
|---|---|
| **Trigger** | New PO issued by BuildRight procurement; PO status changed to "Sent to Vendor" in ERP |
| **Frequency** | ~2,000–3,000 POs per month across ~800 active vendors |
| **Volume** | Each PO contains 5–50 line items; vendor acknowledgment expected within 24–48 hours |
| **Owner** | Procurement Specialist / Vendor Account Manager |
| **Participants** | Vendor Contact, Procurement Specialist, Warehouse Receiving Team |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | PO issued and pushed to vendor portal — ERP automatically sends PO to vendor portal with email notification; PO includes item, quantity, delivery date, ship-to location, and special instructions | ERP System (automated) | Procurement Manager | 5 min (automated) |
| 2 | Vendor reviews PO in portal — vendor sees PO details, delivery requirements, and pricing; can acknowledge all lines, propose changes (quantity, date), or reject with reason | Vendor Contact | Vendor Account Manager | 15–30 min per PO |
| 3 | Vendor submits acknowledgment — options: (a) Full Accept — confirm all lines as ordered, (b) Partial Accept — confirm available lines, propose alternatives for rest, (c) Reject — decline PO with reason (discontinued, pricing dispute, capacity); system updates PO status in real-time | Vendor Contact | Vendor Account Manager | 5 min |
| 4 | Procurement reviews vendor response — for Full Accept: auto-confirm in ERP; for Partial Accept: Procurement Specialist reviews proposals, accepts/modifies/rejects; for Reject: determine alternative vendor or escalate | Procurement Specialist | Procurement Manager | 10–30 min per PO |
| 5 | Send ASN reminder — if PO confirmed and delivery date is within 3 days, automated reminder to submit ASN (Advanced Shipping Notice) via portal; ASN required before DC receiving | ERP System (automated) | Procurement Specialist | 5 min (automated) |
| 6 | Escalate unacknowledged POs — POs not acknowledged within 48 hours trigger automated escalation: email to vendor, notification to Procurement Specialist, and follow-up call for critical orders | Procurement Specialist | Procurement Manager | 15 min per escalation |

### System Touchpoints
- **Vendor Portal Platform** — PO display, acknowledgment workflow, proposal submission
- **ERP Procurement Module** — PO generation, status updates, confirmation recording
- **WMS** — ASN receipt, delivery scheduling
- **Email Notification System** — PO issuance alert, acknowledgment confirmation, escalation notices
- **BI Dashboard** — PO acknowledgment rate, average response time, vendor ranking

### Pain Points / Risks
- Vendor acknowledgment rate target: 90% within 48 hours; actual may be 60–70% during ramp-up
- Partial accept proposals create rework for Procurement — line-by-line negotiation
- Vendor may accept PO but deliver wrong quantities — acknowledgment ≠ delivery guarantee
- System-generated POs (auto-replenishment) may not be reviewed by vendor — phantom acknowledgment
- Cultural preference for verbal PO confirmation over portal — requires policy enforcement

### Staffing Implication
- Procurement Specialists: PO acknowledgment monitoring is part of daily workflow (~1 hour/day)
- Vendor Account Managers: follow-up on unacknowledged POs (~30 min/day)

### Time Estimate
- Automated processing: minimal human effort
- Manual intervention: ~15% of POs require Procurement review = ~400 POs/month × 20 min = 133 hours/month
- **Annual estimate: ~1,600 person-hours/year for manual intervention**

---

## W867. Vendor Self-Service Invoice Submission & Payment Status Inquiry

| Field | Detail |
|---|---|
| **Trigger** | Vendor submits invoice through portal after goods delivered; or vendor inquires on payment status |
| **Frequency** | ~3,000–4,000 vendor invoices per month |
| **Volume** | Average 4–5 invoices per vendor per month; payment terms: 30–60 days |
| **Owner** | AP Accountant / Procurement Specialist |
| **Participants** | Vendor Contact, AP Accountant, Procurement Specialist, Finance Controller |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Vendor uploads invoice via portal — vendor fills invoice form with: invoice number, invoice date, PO reference, line items (matching PO quantities and prices), and attaches scanned invoice PDF; system validates PO reference and performs 3-way match (PO vs. GRN vs. invoice) | Vendor Contact | AP Accountant | 10 min per invoice |
| 2 | Automated validation — portal checks: (a) PO exists and is confirmed, (b) quantities within PO tolerance (+/- 5%), (c) prices match PO, (d) vendor is active, (e) no duplicate invoice number; auto-route to AP for matching invoices; flag exceptions for manual review | Portal System (automated) | AP Accountant | 5 min (automated) |
| 3 | AP reviews and processes matched invoices — for clean 3-way match: auto-approve for payment per payment terms; for discrepancies: route to Procurement for resolution (quantity, price, or receiving variance) | AP Accountant | Finance Controller | 5 min per clean invoice; 30 min per exception |
| 4 | Vendor payment status inquiry — vendor logs into portal to view invoice status: (a) Submitted, (b) In Review, (c) Approved for Payment, (d) Paid (with payment date and reference); reduces AP phone/email inquiries | Vendor Contact (self-service) | AP Accountant | 0 min (self-service) |
| 5 | Payment confirmation push — upon payment run execution, portal automatically updates invoice status to "Paid" with payment date, check/bank reference; vendor receives email notification | ERP Finance Module (automated) | Finance Controller | 5 min (automated) |
| 6 | Dispute invoice processing — vendor can flag invoice as disputed with reason (partial payment, pricing disagreement, damaged goods); routes to Procurement and AP for joint resolution (see W869) | Vendor Contact | Procurement Specialist | 5 min |

### System Touchpoints
- **Vendor Portal Platform** — invoice submission form, validation engine, status display
- **ERP AP Module** — 3-way match, payment processing, invoice status update
- **ERP Procurement Module** — PO reference, receiving confirmation
- **WMS** — goods receipt note (GRN) for 3-way match
- **Bank Integration** — payment confirmation, bank reference capture
- **BI Dashboard** — invoice processing time, exception rate, payment on-time %, vendor satisfaction

### Pain Points / Risks
- Invoice format inconsistency — vendors may not follow portal format, requiring manual entry
- 3-way match exception rate may be 15–20% initially — high manual review workload for AP
- Vendor payment term negotiation via portal is not supported — requires offline discussion
- Philippine banking system payment confirmation may take 1–2 days — vendor sees "Paid" before funds arrive
- Portal does not support credit memo offsetting against invoices — manual AP adjustment required
- Tax compliance: portal invoice must meet BIR e-invoicing requirements once mandated

### Staffing Implication
- AP Accountants: invoice processing is core function; portal reduces manual entry by ~40%
- Procurement Specialists: exception resolution (~20% of invoices)
- IT Portal Administrator: portal invoice module maintenance

### Time Estimate
- Per invoice (automated): 5 min AP review
- Per invoice (exception): 30 min AP + Procurement
- **Annual estimate: ~3,000 invoices/month × 80% automated × 5 min + 20% exception × 30 min = 420 hours/month = 5,040 person-hours/year** (reduced from ~8,400 without portal)

---

## W868. Vendor Catalog & Product Information Self-Service Management

| Field | Detail |
|---|---|
| **Trigger** | Vendor needs to update product information (new items, discontinued items, specification changes, images); or BuildRight MDM team requests vendor catalog refresh |
| **Frequency** | ~200–300 catalog update requests per month across all vendors |
| **Volume** | ~55,000 total SKU master; ~5,000–10,000 catalog updates per year |
| **Owner** | MDM Specialist / Procurement Specialist |
| **Participants** | Vendor Contact, MDM Specialist, Merchandising Manager, Ecommerce Content Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Vendor submits catalog update request via portal — options: (a) New Item Submission (with specs, images, pricing, compliance docs), (b) Item Discontinuation Notice, (c) Specification Update (dimensions, weight, materials, packaging), (d) Image/Media Update | Vendor Contact | MDM Specialist | 15 min per item |
| 2 | Automated data quality check — portal validates: (a) mandatory fields completed, (b) image resolution meets minimum (500×500px), (c) weight/dimension within category norms, (d) barcode/UPC format valid; flag failures for vendor correction | Portal System (automated) | MDM Specialist | 5 min (automated) |
| 3 | MDM review and enrichment — MDM Specialist reviews submission: (a) verify against existing catalog for duplicates, (b) map to BuildRight category taxonomy, (c) assign internal SKU if new item, (d) validate compliance documentation (PS marking, FCC, DENR) | MDM Specialist | Merchandising Manager | 20 min per item |
| 4 | Merchandising approval (for new items) — new item submissions routed to Merchandising for assortment decision: accept into active assortment, add as special-order-only, or reject with reason | Merchandising Manager | Procurement Manager | 10 min per item |
| 5 | Update ERP master data — approved changes propagated to Item Master, ecommerce catalog, POS product database, and WMS slotting; vendor receives notification of update completion | MDM Specialist | MDM Manager | 10 min per item |
| 6 | Monthly catalog health report — portal generates vendor catalog completeness score (% of items with complete specs, images, compliance docs); share with vendors to drive improvement | MDM Specialist | Procurement Manager | 2 hours monthly |

### System Touchpoints
- **Vendor Portal Platform** — catalog submission form, image upload, validation engine
- **ERP MDM Module** — Item Master update, taxonomy mapping, SKU assignment
- **Ecommerce Platform** — product catalog sync, image/media management
- **POS System** — product database update
- **WMS** — slotting and dimension update
- **BI Dashboard** — catalog completeness score, update turnaround time

### Pain Points / Risks
- Vendor product data quality is inconsistent — missing dimensions, low-resolution images, inaccurate specs
- Category taxonomy mapping requires BuildRight-specific knowledge — vendor cannot self-classify accurately
- New item approval pipeline can take 2–4 weeks — vendors frustrated by slow time-to-shelf
- Image copyright and licensing must be verified — vendor-provided images may have usage restrictions
- Compliance documentation (PS marking for electrical, DENR for chemicals) must be attached but vendors often omit

### Staffing Implication
- MDM Specialist: catalog review is 30% of role (~60 hours/month)
- Merchandising Manager: new item approval (~10 hours/month)
- Ecommerce Content Manager: image quality review (~8 hours/month)

### Time Estimate
- Per item submission: 45 min total across all roles
- **Annual estimate: ~8,000 updates × 45 min = 6,000 person-hours/year**

---

## W869. Vendor Dispute Resolution & Issue Ticketing

| Field | Detail |
|---|---|
| **Trigger** | Vendor submits dispute ticket via portal, or BuildRight initiates dispute (receiving variance, quality issue, delivery failure) |
| **Frequency** | ~150–250 vendor disputes per month across all vendors |
| **Volume** | Average resolution time: 5–10 business days; ~15% escalate to Procurement Manager |
| **Owner** | Procurement Specialist / AP Accountant |
| **Participants** | Vendor Contact, Procurement Specialist, AP Accountant, Warehouse Receiving Lead, Quality Inspector |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Vendor or BuildRight creates dispute ticket — categorize as: (a) Payment Dispute (short payment, late payment, unauthorized deduction), (b) PO Dispute (cancellation, specification change, quantity change), (c) Delivery Dispute (late delivery, wrong item, damaged goods), (d) Quality Dispute (product defect, non-conformance), (e) Pricing Dispute (contract price vs. invoiced price) | Vendor Contact / Procurement Specialist | Procurement Manager | 10 min |
| 2 | Auto-route ticket to appropriate resolver — (a) Payment → AP, (b) PO → Procurement, (c) Delivery → Warehouse + Procurement, (d) Quality → Quality Inspector + Procurement, (e) Pricing → Procurement + Merchandising; SLA: first response within 4 hours | Portal System (automated) | Procurement Manager | 5 min (automated) |
| 3 | Investigate dispute — resolver reviews supporting documents in portal (PO, GRN, invoice, photos, quality report); contacts vendor if clarification needed; documents findings | Resolver (role varies) | Procurement Manager | 30–120 min |
| 4 | Propose resolution — options: (a) Vendor credit note / BuildRight debit memo, (b) Replacement shipment, (c) Price adjustment, (d) Claim denied with evidence; submit proposal via portal | Resolver | Procurement Manager | 15 min |
| 5 | Vendor accepts or counters — vendor reviews proposal, accepts (ticket resolved), counters with alternative, or escalates to Procurement Manager; SLA: vendor response within 48 hours | Vendor Contact | Procurement Manager | 10 min |
| 6 | Escalation to Procurement Manager — unresolved disputes escalated after 5 business days or vendor counters; Procurement Manager reviews, mediates, and makes final determination | Procurement Manager | VP Operations | 30 min |
| 7 | Execute resolution and close ticket — apply agreed adjustment in ERP (credit note, debit memo, price update), close ticket with resolution summary, and update vendor scorecard | AP Accountant / Procurement Specialist | Procurement Manager | 15 min |

### System Touchpoints
- **Vendor Portal Platform** — ticketing system, communication thread, document attachment
- **ERP AP Module** — credit/debit memo processing, payment adjustment
- **ERP Procurement Module** — PO amendment, price update
- **WMS** — receiving variance data, quality inspection report
- **BI Dashboard** — dispute volume, resolution time, vendor ranking, dispute category breakdown

### Pain Points / Risks
- Dispute resolution SLA compliance may be low — resolver workload varies; backlog common during peak seasons
- Vendor frustration with denied claims can damage relationship — clear evidence documentation is essential
- Multi-line PO disputes are complex — individual line resolution tracking needed
- Dispute data is valuable for vendor performance scoring but underutilized if not systematically captured
- Language barrier with some international vendors — disputes in English may not be clearly understood

### Staffing Implication
- Procurement Specialists: dispute resolution is 20% of daily workload
- AP Accountants: payment disputes are 15% of daily workload
- Procurement Manager: escalation reviews (2 hours/week)

### Time Estimate
- Per dispute: 60–120 min total effort
- **Annual estimate: ~2,400 disputes × 90 min = 3,600 person-hours/year**

---

## W870. Vendor Compliance Document Upload & Expiration Tracking

| Field | Detail |
|---|---|
| **Trigger** | Vendor onboarding (initial document submission), document approaching expiration (60-day alert), or regulatory change requiring new documentation |
| **Frequency** | ~50–80 document uploads per month; ~30–40 expiration alerts per month |
| **Volume** | ~800 vendors × 5–10 compliance documents each = ~4,000–8,000 tracked documents |
| **Owner** | Procurement Specialist / Compliance Officer |
| **Participants** | Vendor Contact, Procurement Specialist, Compliance Officer, Legal Counsel |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Vendor uploads compliance documents via portal — required documents vary by vendor type: (a) BIR Certificate of Registration, (b) SEC/DTI Registration, (c) Mayor's Permit, (d) PhilHealth/ECC Certificate, (e) DENR Environmental Compliance (for chemical vendors), (f) FDA License (for regulated products), (g) Insurance Certificate, (h) PS/ICC Marking Certificate (for regulated products), (i) ISO Certifications (if applicable) | Vendor Contact | Procurement Specialist | 10 min per document |
| 2 | Automated expiration tracking — portal extracts expiration dates from uploaded documents; set 60-day advance alert to vendor and Procurement Specialist; auto-flag expired documents | Portal System (automated) | Procurement Specialist | 5 min (automated) |
| 3 | Procurement reviews and validates documents — verify document authenticity (cross-reference with government databases where possible), confirm document matches vendor legal entity name, and check for required endorsements or amendments | Procurement Specialist | Compliance Officer | 10 min per document |
| 4 | Issue compliance gap notice — for expired or missing documents: automated email to vendor with 15-day remediation deadline; if not resolved, escalate to Procurement Manager for vendor suspension consideration | Portal System (automated) | Procurement Manager | 5 min (automated) |
| 5 | Update vendor compliance status — approved documents update vendor compliance score; non-compliant vendors flagged in PO creation workflow (warning or block depending on severity) | Procurement Specialist | Procurement Manager | 5 min |
| 6 | Quarterly compliance report — generate vendor compliance health report: overall compliance rate, top non-compliant vendors, expiring documents in next quarter, and regulatory changes requiring new documentation | Compliance Officer | Procurement Manager | 4 hours quarterly |

### System Touchpoints
- **Vendor Portal Platform** — document upload, expiration tracking, compliance status display
- **ERP Procurement Module** — vendor compliance flag, PO blocking rules
- **Document Management** — compliance document storage, version control
- **Government Database Integration** — BIR TIN validation, SEC registration verification (where available)
- **BI Dashboard** — compliance rate by vendor, document type, expiration timeline

### Pain Points / Risks
- Government database integrations in Philippines are unreliable — manual verification often required
- Vendor legal entity names may not match exactly across documents — name matching rules needed
- Regulatory requirements change (BIR, DENR, FDA) — compliance document list must be updated annually
- Small/provincial vendors may lack required registrations — policy exception process needed
- Document quality (blurry scans, incomplete pages) requires re-submission cycles

### Staffing Implication
- Procurement Specialist: document review is 10% of workload
- Compliance Officer: quarterly report + regulatory change monitoring (8 hours/quarter)

### Time Estimate
- Per document review: 10 min
- **Annual estimate: ~1,000 document reviews × 10 min + quarterly reporting = 230 person-hours/year**

---

## W871. Supplier Scorecard Portal Publication & Performance Transparency

| Field | Detail |
|---|---|
| **Trigger** | Monthly scorecard calculation cycle (automated from ERP data); or quarterly business review (QBR) preparation |
| **Frequency** | Monthly scorecard publication; quarterly QBR meeting |
| **Volume** | ~800 vendor scorecards generated monthly; top 100 vendors reviewed in quarterly QBR |
| **Owner** | Procurement Manager |
| **Participants** | Vendor Contact, Procurement Manager, Category Manager, Supply Chain Planner |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Calculate monthly vendor scorecard — ERP automatically computes: (a) On-Time Delivery % (target: ≥ 95%), (b) In-Full Delivery % (target: ≥ 98%), (c) Quality Rejection Rate (target: < 1%), (d) Invoice Accuracy % (target: ≥ 98%), (e) Price Competitiveness (vs. market index), (f) Responsiveness (PO acknowledgment within 48h), (g) Compliance Status (documents current) | ERP System (automated) | Procurement Manager | 30 min (automated) |
| 2 | Publish scorecard to vendor portal — vendor sees own scorecard with trend vs. prior months, category ranking (anonymized peer comparison), and improvement areas; flag vendors below threshold for action plan | Procurement Specialist | Procurement Manager | 1 hour |
| 3 | Vendor reviews and acknowledges scorecard — vendor logs in, reviews scores, and can submit improvement plan for underperforming areas; acknowledgment required within 5 business days | Vendor Contact | Procurement Manager | 15 min |
| 4 | Procurement reviews vendor improvement plans — for vendors scoring below 70% composite: review submitted improvement plan, accept or request revision, set 90-day review milestone | Procurement Manager | VP Operations | 30 min per underperformer |
| 5 | Quarterly business review (top 100 vendors) — present detailed scorecard, discuss performance trends, review upcoming demand forecast, address issues, and align on improvement targets | Procurement Manager | Category Manager | 1 hour per vendor (quarterly) |
| 6 | Annual vendor classification — based on 12-month scorecard performance: Strategic Partner (top 10%), Preferred Vendor (11–40%), Approved Vendor (41–80%), Probationary (bottom 20%); adjust PO allocation and payment terms accordingly | Procurement Manager | VP Operations | 8 hours (annual) |

### System Touchpoints
- **Vendor Portal Platform** — scorecard display, trend charts, peer comparison, improvement plan submission
- **ERP Procurement Module** — scorecard calculation engine, vendor classification
- **BI Dashboard** — vendor performance analytics, category spend analysis
- **WMS** — delivery performance data (OTIF)
- **Finance Module** — invoice accuracy data, payment term management

### Pain Points / Risks
- Scorecard methodology must be transparent and accepted by vendors — disputes on measurement criteria
- Anonymized peer comparison may be identifiable in categories with few vendors
- Underperforming vendors may dispute scores rather than improve — requires clear evidence
- QBR time commitment is significant for top 100 vendors — 100 hours per quarter
- Scorecard does not capture soft factors (relationship quality, flexibility, innovation contribution)

### Staffing Implication
- Procurement Manager: scorecard review and QBR management (20% of time)
- Category Managers: participate in QBRs for their categories
- Procurement Specialist: scorecard publication and follow-up (5 hours/month)

### Time Estimate
- Monthly scorecard cycle: 8 hours
- Quarterly QBRs: 100 hours
- Annual classification: 8 hours
- **Annual estimate: 96 + 400 + 8 = 504 person-hours/year**

---

## W872. Vendor RFQ & Bid Submission Portal Management

| Field | Detail |
|---|---|
| **Trigger** | Procurement initiates RFQ (Request for Quotation) or tender for category sourcing, new vendor evaluation, or competitive bidding |
| **Frequency** | ~20–30 RFQs per month; 2–3 formal tenders per quarter |
| **Volume** | Each RFQ sent to 3–5 vendors; formal tender to 5–10 vendors |
| **Owner** | Procurement Manager / Category Manager |
| **Participants** | Vendor Contact, Procurement Manager, Category Manager, Merchandising Manager, Finance Controller |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Create RFQ in portal — Procurement specifies: (a) item specifications and quantities, (b) required delivery schedule, (c) evaluation criteria (price, quality, delivery, terms), (d) bid submission deadline (typically 7–14 days), (e) terms and conditions; invite selected vendors | Procurement Manager | Category Manager | 1–2 hours |
| 2 | Vendor downloads RFQ documents and prepares bid — vendor reviews specifications, prepares pricing (itemized), confirms availability and delivery schedule, and uploads supporting documents (product specs, samples, references) | Vendor Contact | Vendor Account Manager | 2–8 hours (over RFQ period) |
| 3 | Vendor submits bid via portal — bids are sealed (not visible to Procurement or other vendors) until submission deadline; system confirms receipt and timestamp; late submissions automatically rejected | Vendor Contact | Procurement Manager | 5 min |
| 4 | Bid opening and evaluation — after deadline, Procurement unseals all bids; system presents comparison matrix (price ranking, delivery commitment, terms comparison); evaluation committee scores each bid against criteria | Procurement Manager | Category Manager | 2–4 hours |
| 5 | Clarification and negotiation — shortlisted vendors invited for clarification round (via portal messaging); negotiate final terms (price, MOQ, payment terms, delivery frequency); document all negotiations | Procurement Manager | Finance Controller | 4–8 hours |
| 6 | Award decision and notification — winning vendor receives award notification via portal; unsuccessful vendors receive thank-you notification with general feedback; award posted to PO creation | Procurement Manager | VP Operations | 1 hour |
| 7 | Archive RFQ and bids — all bid documents, evaluation scoring, and negotiation records archived per retention policy (7 years for audit trail); update vendor scorecard with bid responsiveness | Procurement Specialist | Procurement Manager | 1 hour |

### System Touchpoints
- **Vendor Portal Platform** — RFQ creation, bid submission (sealed), evaluation matrix, notification
- **ERP Procurement Module** — RFQ-to-PO conversion, vendor selection recording
- **Document Management** — RFQ document archive, bid document storage
- **BI Dashboard** — bid comparison analytics, savings tracking, vendor participation rate
- **Finance Module** — cost impact analysis, budget comparison

### Pain Points / Risks
- Bid collusion risk — vendors may coordinate pricing; requires sealed-bid process and multiple participants
- Low vendor participation for niche categories — insufficient competitive pressure
- Bid evaluation subjectivity — non-price criteria can be manipulated; requires clear scoring rubric
- International vendors may not use portal — manual bid submission required (exception process)
- RFQ-to-award cycle time of 2–4 weeks may be too slow for urgent sourcing needs

### Staffing Implication
- Procurement Manager: RFQ creation and evaluation (primary responsibility)
- Category Manager: specification development and evaluation committee
- Finance Controller: cost analysis and budget verification

### Time Estimate
- Per RFQ: 15–25 person-hours over 2–4 weeks
- Per formal tender: 40–60 person-hours over 4–8 weeks
- **Annual estimate: 30 RFQs × 20 hours + 10 tenders × 50 hours = 1,100 person-hours/year**
