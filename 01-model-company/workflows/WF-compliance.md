# Compliance & Governance Workflows
> Loss prevention, business continuity, LGU permits, BIR audit, government procurement, grievance/whistleblower, hazardous waste disposal, environmental reporting, branch de-registration, DTI price freeze implementation, consumer complaint DTI escalation, DOLE labor inspection response, unified regulatory compliance calendar management, enterprise risk register maintenance & quarterly risk review, product recall effectiveness verification & post-recall review, anti-bribery & anti-corruption (ABAC) compliance program, regulatory change management & impact assessment, general regulatory inspection response protocol, anti-money laundering (AML) compliance program operations, Consumer Act (RA 7394) compliance monitoring & enforcement, and vendor tax compliance monitoring & BIR TIN validation.
>
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W37. Loss Prevention & Exception Reporting](#w37-loss-prevention-exception-reporting)
- [W49. Natural Disaster / Typhoon Business Continuity](#w49-natural-disaster-typhoon-business-continuity)
- [W54. LGU Business Permit Renewal per Location](#w54-lgu-business-permit-renewal-per-location)
- [W77. BIR Tax Audit Response](#w77-bir-tax-audit-response)
- [W78. Government / Institutional Procurement Participation](#w78-government-institutional-procurement-participation)
- [W79. Employee Grievance & Whistleblower Process](#w79-employee-grievance-whistleblower-process)
- [W82. Hazardous Waste Disposal Tracking & DENR Compliance](#w82-hazardous-waste-disposal-tracking-denr-compliance)
- [W95. External Audit Coordination & Support](#w95-external-audit-coordination-support)
- [W114. Sustainability & Environmental Compliance Reporting](#w114-sustainability-environmental-compliance-reporting)
- [W157. E-waste Collection & Circular Economy Operations](#w157-e-waste-collection-circular-economy-operations)
- [W158. Business Continuity Drill & Disaster Recovery Testing](#w158-business-continuity-drill-disaster-recovery-testing)
- [W167. Store & DC Recycling Program (Circular Economy)](#w167-store-dc-recycling-program-circular-economy)
- [W185. Product Liability & Consumer Safety Incident Management](#w185-product-liability-consumer-safety-incident-management)
- [W207. Store-Level Security Camera (CCTV) Audit & LP Integration](#w207-store-level-security-camera-cctv-audit-lp-integration)
- [W209. Barangay & Local Community Relationship Management](#w209-barangay-local-community-relationship-management)
- [W216. BIR CAS (Computerized Accounting System) Compliance Audit](#w216-bir-cas-computerized-accounting-system-compliance-audit)
- [W271. Data Subject Access & Deletion Requests (DPA Compliance)](#w271-data-subject-access-deletion-requests-dpa-compliance)
- [W331. DTI Sales Promotion Permit Application & Compliance](#w331-dti-sales-promotion-permit-application-compliance)
- [W427. DTI Sales Promotion Permit Monitoring & In-Store Compliance](#w427-dti-sales-promotion-permit-monitoring--in-store-compliance)
- [W433. DENR Self-Monitoring (SMR) & Compliance (CMR) Reporting](#w433-denr-self-monitoring-smr-compliance-cmr-reporting)
- [W437. Regulatory Branch De-registration & Permit Cancellation](#w437-regulatory-branch-de-registration-permit-cancellation)
- [W444. Community Solicitation & Donation Processing](#w444-community-solicitation-donation-processing)
- [W446. Temporary LGU Permits for Outdoor Sales & Events](#w446-temporary-lgu-permits-for-outdoor-sales-events)
- [W468. DTI Price Freeze / Emergency Price Control Implementation (RA 7581)](#w468-dti-price-freeze--emergency-price-control-implementation-ra-7581)
- [W469. Customer Complaint DTI Escalation & Consumer Adjudication Management](#w469-customer-complaint-dti-escalation--consumer-adjudication-management)
- [W505. DOLE Labor Inspection Response Protocol](#w505-dole-labor-inspection-response-protocol)
- [W506. Unified Regulatory Compliance Calendar & Dashboard](#w506-unified-regulatory-compliance-calendar--dashboard)
- [W626. Enterprise Risk Register Maintenance & Quarterly Risk Review](#w626-enterprise-risk-register-maintenance--quarterly-risk-review)
- [W627. Product Recall Effectiveness Verification & Post-Recall Review](#w627-product-recall-effectiveness-verification--post-recall-review)
- [W656. Anti-Bribery & Anti-Corruption (ABAC) Compliance Program](#w656-anti-bribery--anti-corruption-abac-compliance-program)
- [W657. Regulatory Change Management & Impact Assessment](#w657-regulatory-change-management--impact-assessment)
- [W658. General Regulatory Inspection Response Protocol](#w658-general-regulatory-inspection-response-protocol)
- [W730. Anti-Money Laundering (AML) Compliance Program Operations](#w730-anti-money-laundering-aml-compliance-program-operations)
- [W731. Consumer Act (RA 7394) Compliance Monitoring & Enforcement](#w731-consumer-act-ra-7394-compliance-monitoring--enforcement)
- [W732. Vendor Tax Compliance Monitoring & BIR TIN Validation](#w732-vendor-tax-compliance-monitoring--bir-tin-validation)

---

## W37. Loss Prevention & Exception Reporting

| Field | Detail |
|---|---|
| **Trigger** | Daily exception report generation; or real-time alert triggered by POS exception |
| **Frequency** | Daily review; real-time alerts for high-severity exceptions |
| **Volume** | ~500–1,000 exception events/day chain-wide across all 200 stores |
| **Owner** | Loss Prevention Officer (LPO) |
| **Participants** | LPO, Store Manager, Regional Manager, Internal Audit, Cashier, Department Supervisor |

### Background

Shrinkage target: < 1.5% of sales (~PHP 75M/month at risk). Exception-based reporting identifies suspicious transaction patterns at POS and receiving dock that may indicate theft, fraud, or process errors.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System automatically monitors POS transactions in real-time and generates exception alerts for: (a) excessive voids/cancels per cashier, (b) high-value refunds without manager override, (c) manual price overrides, (d) sweet-hearting (repeated transactions with loyalty card of same employee or family), (e) excessive no-sale drawer opens, (f) post-void patterns, (g) high ratio of discount transactions | System | — | Real-time |
| 2 | System generates daily exception summary report per store: top exception categories, top cashiers by exception count, transaction drill-down capability | System | — | Automated (daily) |
| 3 | LPO reviews daily exception report; prioritizes investigation of high-risk patterns (e.g., one cashier with 5× average void rate) | LPO | Internal Audit | 1–2 hours/day |
| 4 | For flagged exceptions: LPO pulls transaction details, CCTV timestamps (cross-reference with security footage), and employee history | LPO | Internal Audit | 30 min/case |
| 5 | If investigation confirms irregularity: LPO documents findings; escalates to Regional Manager and Internal Audit for disciplinary action | LPO | Internal Audit | 1 hour/case |
| 6 | For receiving dock exceptions: system monitors GR short shipments, frequent damage claims from same vendor, and receiving patterns outside scheduled appointments | System | DC Manager | Automated |
| 7 | Monthly: LPO generates shrinkage report per store (inventory adjustment value ÷ sales); flags stores exceeding 1.5% threshold | LPO | Internal Audit | 2 hours/month |
| 8 | Monthly: LPO and Regional Manager review top shrinkage stores; develop action plans (additional training, CCTV repositioning, staffing adjustments) | LPO + Regional Manager | Internal Audit | 1 hour/month per high-shrinkage store |
| 9 | Quarterly: Internal Audit includes POS exception trends in audit findings; recommends system configuration changes (e.g., tighten void approval rules) | Internal Audit | CFO | Quarterly report |
| 10 | System tracks all investigation cases: status (open/investigating/closed), resolution, recovery amount, disciplinary action taken | System | — | Automated |

### System Touchpoints
- Real-time POS exception monitoring with configurable thresholds per exception type (W37.1)
- Daily exception summary report with drill-down to transaction level (W37.2)
- Transaction detail with CCTV timestamp cross-reference capability (W37.4)
- Receiving dock exception monitoring (W37.6)
- Shrinkage report per store with threshold alerting (W37.7)
- Investigation case management with status tracking (W37.10)
- Confirmed theft / inventory write-off process: documentation with supporting evidence, police report filing for theft, tiered approval per loss value, GL write-off posting, insurance claim integration, quarterly shrinkage reporting integration (W37.11–16)
- Exception threshold configuration and tuning (W37.9)
- CCTV integration specification: (a) system captures POS transaction timestamp and terminal ID; (b) POS integration layer sends transaction event to CCTV system via API or middleware; (c) CCTV system bookmarks associated video clip (configurable: ± 2 minutes around transaction event); (d) LPO retrieves correlated video from LP investigation dashboard by clicking transaction exception — system deep-links to CCTV playback at the transaction timestamp; (e) CCTV recording retention: minimum 30 days online storage, 90 days archived; (f) CCTV access restricted to LPO, Store Manager, Regional Manager, and Internal Audit via role-based access control; (g) for new store openings (W16), IT configures POS-to-CCTV integration as part of go-live readiness checklist (W16.9a); (h) system does not store video — only stores timestamp reference and CCTV clip ID for retrieval from the CCTV system's own storage
- Loyalty program fraud detection: system monitors for loyalty abuse patterns in addition to POS transaction exceptions; detection rules include: (a) cashier scanning the same loyalty card across > 20% of their transactions (self-scanning or family/friend farming), (b) loyalty points earned on subsequently voided transactions (points earned but not reversed), (c) unusually high points earning on single transaction (points-to-revenue ratio exceeding 3× normal), (d) multiple loyalty accounts with > 85% match on name, phone, or address (farming multiple accounts), (e) redemption velocity spike on dormant accounts; flagged patterns appear on LPO daily exception dashboard alongside POS exceptions; LPO investigates and escalates to Loyalty Manager for account action (W17 manual points adjustment); confirmed fraud cases result in account suspension per W17 manual adjustment approval tiers
- Gift card / store credit fraud detection: system monitors gift card and store credit transactions for fraud patterns: (a) multiple gift card balance inquiries from same terminal within short time window (potential brute-force balance checking), (b) gift card redemption at a different store within 24 hours of activation (potential barcode photocopying or stolen card), (c) return-to-store-credit followed by immediate cash-out attempt (return fraud), (d) employee-associated gift card transactions (employee purchasing or reloading their own gift card with subsequent return manipulation), (e) high-value gift card purchases paid in cash (potential money laundering); flagged patterns appear on LPO daily exception dashboard; LPO investigates and escalates to Store Manager for card suspension and customer verification; confirmed fraud results in gift card deactivation and loss reporting; monthly: LPO includes gift card fraud metrics in shrinkage report (W37.7); any manual gift card balance adjustment requires dual approval (Store Manager + AP Supervisor) with full audit trail

### Time Estimate
- Daily exception report review: 1–2 hours/day for LPO
- Per-case investigation (flagged exceptions): 30 min–1 hour/case
- Monthly shrinkage report: 2 hours/month
- Monthly top-shrinkage store review: 1 hour/store for high-shrinkage locations
- Quarterly audit integration: report preparation absorbed into Internal Audit cycle
- Confirmed theft/write-off case: 1–1.5 hours/case (W37.11–16)
- Overall: LPOs spend ~3–4 hours/day on LP activities + monthly/quarterly reporting cycles

### Pain Points / Risks
- **CCTV-POS correlation gaps**: If CCTV system timestamps drift out of sync with POS transaction timestamps, video evidence becomes unreliable for prosecution; requires quarterly time-synchronization audits across 200 stores
- **Sweethearting detection limits**: Collusion between cashiers and customers (scanning employee/family loyalty cards, deliberate under-ringing) is difficult to detect algorithmically; relies on pattern thresholds that may produce excessive false positives or miss sophisticated schemes
- **Shrinkage attribution accuracy**: At PHP 75M/month at risk, even a 0.1% error in shrinkage attribution (internal theft vs. shoplifting vs. vendor fraud vs. process error) represents PHP 75K/month in misdirected loss prevention investment
- **LPO coverage across 200 stores**: 2 LPOs covering ~100 stores each means physical store visits are infrequent (each store visited ~2–4 times/year); most LP activity is remote dashboard review, limiting deterrent effect and investigative depth

### Staffing Implication
- **2–3 Loss Prevention Officers** (reporting to Internal Audit or a dedicated LP function): Daily review (1–2 hours) + case investigation (5–10 active cases at any time) + monthly shrinkage reporting + quarterly reviews. This is a specialized role that may not exist in the current org chart. Recommend adding 2 LPOs to cover 200 stores (each covering ~70 stores, rotating through physical store visits).
- **Store Managers**: Review their store's exception report daily (~15 min). Absorbed into opening routine.
- **Internal Audit**: Incorporates LP findings into quarterly audit cycle. No incremental headcount.

### Confirmed Theft / Inventory Write-Off Process

When an LPO investigation confirms theft or irrecoverable loss:

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| W37.11 | LPO documents confirmed loss: investigation findings, supporting evidence (CCTV footage, transaction records, witness statements); for theft, files police report with local PNP station | LPO | Internal Audit | 1 hour/case |
| W37.12 | LPO submits inventory write-off request: SKU, quantity, value at WAC, root cause classification (internal theft, external shoplifting, vendor fraud, unexplained loss) | LPO | Internal Audit | 15 min/case |
| W37.13 | Approval per tier: (a) total loss ≤ PHP 10,000: Store Manager, (b) PHP 10,001–50,000: Regional Manager + Internal Audit, (c) PHP 50,001–500,000: Controller + Internal Audit, (d) > PHP 500,000: CFO + CEO | Approver | Approver | 15 min/case |
| W37.14 | System posts write-off: Dr. Inventory Loss / Cr. Inventory; removes items from inventory register; records loss in shrinkage tracking for store KPI | System | — | Automated |
| W37.15 | If loss is insured (e.g., large robbery, transit theft): LPO files insurance claim per W3.6a insurance claim process; Finance posts recovery upon settlement | LPO / Finance | Controller | Per W3.6a |
| W37.16 | Quarterly: LPO includes confirmed theft and write-off totals in shrinkage report (W37.7); feeds into store KPI scoring and loss prevention action plans | LPO | Internal Audit | Part of existing reporting |

---

## W49. Natural Disaster / Typhoon Business Continuity

| Field | Detail |
|---|---|
| **Trigger** | PAGASA raises tropical cyclone warning signal over a store/DC location; or earthquake, flooding, or volcanic activity alert |
| **Frequency** | ~10–20 typhoon-related events/year requiring action across Philippine store network; 2–4 significant events/year with store closures |
| **Volume** | Variable — from 1–2 stores affected (localized flooding) to 50+ stores (major typhoon crossing multiple regions) |
| **Owner** | COO (overall response); Store Manager (store-level execution) |
| **Participants** | COO, Store Ops Director, Regional Managers, Store Managers, DC Managers, IT, HR, Finance, Supply Chain, Marketing, Logistics |

### Background

The Philippines experiences an average of 20 tropical cyclones per year, of which 5–7 make landfall as typhoons (Signal 3 or higher). BuildRight's 200 stores span Luzon, Visayas, and Mindanao, meaning multiple regions can be affected simultaneously or sequentially. The primary risks are: (a) staff safety, (b) inventory damage (especially outdoor lumber yards and building materials), (c) facility structural damage, (d) supply chain disruption, and (e) revenue loss from store closures.

### Phase 1: Pre-Disaster Preparation (48–72 hours before projected landfall)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | COO monitors PAGASA bulletins and NDRRMC advisories; activates disaster monitoring protocol when Signal 1 is raised over any operating region | COO | CEO | Ongoing during typhoon season |
| 2 | Regional Managers notify Store Managers in affected regions to begin preparations; Store Managers brief all staff | Regional Manager | Store Ops Director | 1 hour |
| 3 | **Store preparations**: Store Manager directs staff to: (a) secure outdoor yard inventory — move lumber, cement, and building materials under cover or to higher ground; (b) protect floor-level merchandise from potential flooding (move to higher shelves or backroom); (c) secure display fixtures, signage, and loose items; (d) verify backup power (generator fuel level, battery backup for POS); (e) verify emergency supplies (flashlights, first aid kits, drinking water) | Store Manager | Regional Manager | 4–8 hours |
| 4 | **DC preparations**: DC Manager directs staff to: (a) prioritize outbound shipments to stores in safe zones before transport disruption; (b) secure outdoor inventory and yard areas; (c) verify backup power systems; (d) coordinate with carriers to suspend inbound shipments to affected areas | DC Manager | Supply Chain Manager | 4–8 hours |
| 5 | IT sends system advisory to all locations: reminder of offline POS procedures (W5G), system backup schedule accelerated | IT Team | CIO | 30 min |
| 6 | HR verifies emergency contact information for all employees in affected regions; prepares welfare check plan | HR Head | CHRO | 1 hour |
| 7 | Supply Planner reviews inventory levels at stores and DCs in projected path; identifies potential stockout risks for essential items (tarps, waterproofing, cement, plywood, flashlights, batteries, generators) | Supply Planner | Supply Chain Manager | 1 hour |

### Phase 2: Closure Decision & Execution (24–0 hours before projected landfall)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 8 | COO makes store closure decision based on: PAGASA signal level (Signal 2+ triggers automatic closure), LGU advisory, road conditions, staff safety assessment; decisions made by region, not chain-wide | COO | CEO | 30 min |
| 9 | Marketing communicates closure to customers: update website, social media, Google Business listings; send SMS/email to loyalty members in affected areas | Marketing | CMO | 1 hour |
| 10 | Ecommerce platform: Digital Commerce Inc. suspends BOPIS and delivery orders for closed stores/DCs; displays closure notice | Ecom Team | CMO | 30 min |
| 11 | Store Manager executes early closing procedure (abbreviated W5F): expedited Z-report, cash secured in safe (do NOT send with armored car during typhoon — hold in safe), POS shut down, building secured | Store Manager | Regional Manager | 30 min |
| 12 | Store Manager sends staff home with safety instructions; confirms all staff have departed safely | Store Manager | Regional Manager | 15 min |

### Phase 3: Post-Disaster Assessment & Recovery (0–72 hours after event)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 13 | Store Manager or designated contact conducts visual assessment of store exterior (drive-by or walk-by) as soon as safely possible after event passes; reports to Regional Manager: structural damage, flooding, power status, yard inventory status | Store Manager | Regional Manager | 30 min |
| 14 | Regional Manager compiles damage assessment across affected stores; reports to COO and Store Ops Director | Regional Manager | COO | 2 hours |
| 15 | COO makes reopening decision per store: (a) open immediately if no damage and power/connectivity restored, (b) delayed opening for minor cleanup and repair, (c) remain closed for significant damage requiring repair or insurance assessment | COO | CEO | 1 hour |
| 16 | **If inventory damaged**: Store Manager conducts damage inventory with photos; system creates damage report; disposition per W6.8a (scrap, markdown, RTV, insurance claim) | Store Manager / Maintenance | Regional Manager | 2–4 hours |
| 17 | **If facility damaged**: Facilities Coordinator engages contractors for emergency repair; Store Manager initiates insurance claim per W3.6a process (photos, documentation, claim filing) | Facilities Coordinator / Store Manager | Store Ops Director | Varies |
| 18 | Supply Planner triggers emergency replenishment for disaster-response items (tarps, plywood, cement, paint, waterproofing, tools, generators) to reopened stores; coordinates with DC for expedited shipment | Supply Planner | Supply Chain Manager | 2–4 hours |
| 19 | HR conducts welfare check on all employees in affected regions within 24 hours; provides assistance (advance salary, emergency loan, temporary shelter) per company policy | HR Head | CHRO | 4–8 hours |
| 20 | Marketing communicates reopening to customers; update website and social media; potential "rebuilding supplies" promotion to serve community needs | Marketing | CMO | 1 hour |
| 21 | System reconciles: process any offline POS transactions from pre-closure; reverse pending ecommerce orders for closed stores; update inventory for damaged/scrapped items | IT / Finance | Controller | 2–4 hours |

### Phase 4: Post-Event Review (1–2 weeks after)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 22 | COO conducts after-action review: preparation adequacy, response time, damage extent, recovery speed, staff safety outcomes | COO | CEO | 2 hours |
| 23 | Finance quantifies total loss: inventory damage, facility repair costs, revenue loss from closure days, insurance recovery | Controller | CFO | 1 day |
| 24 | Insurance claims finalized for major events; Finance tracks claim status and settlement | Treasury Analyst | CFO | Varies |
| 25 | Store Ops Director updates disaster response procedures based on lessons learned | Store Ops Director | COO | 2 hours |

### System Touchpoints
- Emergency communication channel integration (SMS blast to store managers, regional managers, employees) (W49.2, 6, 9)
- Store closure/reopening status tracking per location with real-time dashboard (W49.8, 15)
- Ecommerce platform store availability toggle for BOPIS/delivery (W49.10)
- Damage inventory recording with photo attachment and disposition workflow (W49.16)
- Emergency replenishment order generation with priority flag (W49.18)
- Insurance claim tracking per W3.6a process (W49.17, 24)
- Post-disaster inventory and financial reconciliation (W49.21, 23)
- Employee welfare check tracking with HR case management (W49.19)
- Integration with W5G (offline POS recovery), W3.6a (insurance claims), W22 (emergency transfers), W25 (emergency petty cash for cleanup supplies), W47 (facility emergency repair)

### Pain Points / Risks
- **Multi-region simultaneous events**: A major typhoon crossing Luzon to Visayas can affect 50+ stores simultaneously; COO and Store Ops Director cannot personally manage all locations; Regional Manager capacity becomes the bottleneck for damage assessment and reopening decisions
- **Outdoor lumber yard vulnerability**: BuildRight's outdoor yard inventory (lumber, cement, building materials) is the highest-value exposure during typhoons; even with 48-hour preparation, moving thousands of board feet of lumber under cover in a single day may not be physically possible
- **Insurance claim processing delays**: Major typhoons generate thousands of insurance claims across Philippine businesses; insurers are backlogged for months, delaying recovery funds and slowing store repair timelines
- **Staff welfare check coverage**: HR must verify safety of ~6,715 employees across affected regions within 24 hours; if cellular networks are down (common after typhoons), welfare checks default to physical visits that may take days to complete

---

### Time Estimate
- Pre-disaster preparation (Phase 1): 4–8 hours per affected store for physical preparations; 1 hour for IT advisory; 1 hour for HR welfare plan
- Closure decision and execution (Phase 2): 1–2 hours total (COO decision + communications + store closing procedures)
- Post-disaster assessment (Phase 3): 30 min–4 hours per store depending on damage; 2–4 hours for emergency replenishment; 4–8 hours for HR welfare checks
- Post-event review (Phase 4): 2 hours for after-action review; 1 day for Finance loss quantification; 2 hours for procedure updates
- Total per significant typhoon event: 40–80 hours across all participants over 2–3 weeks

### Staffing Implication
- No dedicated disaster response team. Response is a cross-functional effort managed by existing roles (COO leads, Regional Managers execute, Store Managers act).
- **Facilities Coordinator** (recommended in W47) becomes critical during post-disaster recovery for coordinating emergency repairs across multiple affected stores.
- **IT Field Support** (recommended in W48) may need to deploy to affected stores for POS/network restoration.
- Post-disaster emergency replenishment adds temporary surge to Supply Planner and DC workload — absorbed with overtime during recovery period.

## W54. LGU Business Permit Renewal per Location

| Field | Detail |
|---|---|
| **Trigger** | LGU business permit renewal calendar (typically annual, per LGU) |
| **Frequency** | Annual per location; 200 stores + 4 DCs + HQ = ~205 renewals/year, staggered across LGU calendars |
| **Volume** | ~205 locations across ~150 different LGUs (some LGUs have multiple stores); most LGUs require renewal in January–March |
| **Owner** | Legal & Compliance — Regulatory Officer |
| **Participants** | Regulatory Officer, Store Manager, DC Manager, Finance, Facilities Coordinator |

### Background

Each BuildRight Depot store and DC operates within a specific Local Government Unit (LGU — city or municipality). Each LGU requires an annual business permit (Mayor's Permit) to operate, with requirements, fees, and renewal calendars varying by LGU. Failure to maintain current permits risks closure orders, fines, and reputational damage. BuildRight's 200 stores span ~150 distinct LGUs across Luzon, Visayas, and Mindanao.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System maintains LGU permit calendar per location: renewal deadline, LGU name, LGU-specific requirements, required documents, fee schedule (based on LGU rate × estimated gross receipts), prior year permit reference | Regulatory Officer | Legal Head | 4 hours/year (setup) |
| 2 | System alerts Regulatory Officer 60 days before each location's permit renewal deadline | System | — | Automated |
| 3 | Regulatory Officer prepares renewal package per LGU requirements: (a) current year business permit, (b) SEC/DTI registration, (c) BIR registration, (d) lease contract or proof of occupancy, (e) barangay clearance, (f) fire safety inspection certificate (BFP), (g) sanitary/health permit (if applicable), (h) local business tax payment receipt, (i) authorized representative letter if not store manager filing | Regulatory Officer | Legal Head | 1–2 hours/location |
| 4 | Regulatory Officer coordinates with Store Manager: Store Manager obtains barangay clearance (requires physical visit to barangay hall), confirms fire safety inspection is current (W47 preventive maintenance — BFP annual inspection), and verifies physical signage matches registered business name | Store Manager | Regulatory Officer | 1–2 hours/location |
| 5 | Finance processes local business tax payment per LGU schedule (separate from W9A.16c LBT payment — the permit renewal requires payment first or concurrently) | Treasury Analyst | Controller | 30 min/location |
| 6 | Regulatory Officer (or designated Store Manager) submits renewal application to LGU Business Permit and Licensing Office (BPLO); many LGUs now accept online renewal via Business One-Stop Shop (BOSS) portals | Regulatory Officer / Store Manager | Legal Head | 1–4 hours/location |
| 7 | LGU processes renewal; may require inspection or hearing; issues new business permit | LGU | — | External (1–30 days) |
| 8 | Store Manager receives new permit; displays original in store (BIR and LGU requirement); sends copy to Regulatory Officer for system upload | Store Manager | Regulatory Officer | 15 min |
| 9 | Regulatory Officer uploads permit copy to system; updates location master with new permit number, issue date, and expiry date | Regulatory Officer | Legal Head | 5 min/location |
| 10 | System alerts Regulatory Officer if permit not received within 30 days of renewal deadline; escalates to Legal Head | System | — | Automated |
| 11 | Monthly: Regulatory Officer generates permit status dashboard: active, pending renewal, expired, at-risk locations; Legal Head reviews expired permits as priority escalation | Regulatory Officer | Legal Head | 1 hour/month |

### System Touchpoints
- LGU permit calendar per location with renewal deadlines, LGU-specific requirements, and document checklists (W54.1)
- Automated renewal alerts at 60, 30, and 7 days before expiry (W54.2)
- Location master integration: permit number, issue date, expiry date stored per location; active permit required for location to remain in "Operating" status (W54.9)
- Document storage: permit copies attached to location record per DOC-001 (W54.8–9)
- Permit status dashboard with expiry alerting and escalation (W54.11)
- Integration with W9A.16c (LBT payment), W47 (fire safety inspection scheduling), W16 (new store — initial permit acquisition)

### Pain Points / Risks
- **150+ distinct LGUs with varying requirements**: Each LGU has unique renewal requirements, fee schedules, and processing timelines; maintaining accurate LGU-specific requirement matrices for 150+ LGUs is an administrative burden that grows with each new store opening
- **Q1 permit renewal crunch**: Most LGUs require renewal in January–March; with 205 locations, the Regulatory Officer must process ~15–20 renewals/week during Q1, creating a severe peak workload that may lead to missed deadlines if any LGU delays or requires additional documentation
- **LGU bureaucratic delays**: Some LGUs have slow processing (2–4 weeks for simple renewals) and may require physical inspections or hearings; a delayed permit technically places the store in non-compliance, risking closure orders or fines
- **Fire safety inspection dependency**: LGU renewal requires a current BFP fire safety inspection certificate (step 3f); if BFP inspection is delayed or the store has a finding requiring remediation, the entire permit renewal chain is blocked

### Time Estimate
- Permit calendar setup: 4 hours/year (one-time, maintained ongoing)
- Per-location renewal preparation: 1–2 hours (document gathering, coordination with Store Manager)
- LGU submission: 1–4 hours/location (physical visit or BOSS portal)
- LGU processing: external, 1–30 days
- Permit upload and system update: 5 min/location
- Monthly status dashboard: 1 hour/month
- Q1 peak: Regulatory Officer spends ~20–25 hours/week on permit renewals during January–March; ~5–8 hours/week rest of year

### Staffing Implication
- **1 Regulatory Officer** (within Legal & Compliance): ~205 renewals/year × ~3 hours each = ~620 hours/year = ~4 days/month. Concentrated in Q1 when most LGUs require renewal. This role also manages BIR CAS registration (W54A) and regulatory inspection handling. Absorbed within Legal & Compliance team (recommend expanding from ~5 to ~6 with the DPO role in W53).
- **Store Managers**: ~2 hours/year for their location's permit renewal coordination. Absorbed.

### W54A. BIR Computerized Accounting System (CAS) Registration

| Field | Detail |
|---|---|
| **Trigger** | New entity incorporation, new ERP system deployment, major system upgrade requiring re-registration, or annual permit renewal |
| **Frequency** | Initial registration per entity (5 entities); annual renewal per BIR requirements; re-registration if system undergoes major changes |
| **Volume** | 5 entity registrations initially; 5 annual renewals thereafter |
| **Owner** | Regulatory Officer |
| **Participants** | Regulatory Officer, CIO, Controller, CFO, external ERP vendor, BIR Regional Office |

### Background

Under BIR Revenue Regulations No. 11-2018 and Revenue Memorandum Order (RMO) No. 29-2002, any business using a computerized accounting system (including ERP systems) must register the system with the BIR and obtain a CAS Permit before the system can legally generate BIR-registered receipts, invoices, and accounting records. Each of BuildRight's 5 legal entities must obtain its own CAS permit. The system must be able to produce books of accounts (general journal, general ledger, cash receipts journal, cash disbursements journal, sales journal, purchases journal) in the format prescribed by BIR.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Regulatory Officer obtains BIR CAS registration forms: BIR Form 1907 (Application for Registration of Books of Accounts), together with system documentation package | Regulatory Officer | Legal Head | 4 hours/entity |
| 2 | IT and ERP vendor prepare system documentation package per BIR requirements: (a) system overview and architecture diagram, (b) data flow diagram showing transaction processing from source to GL, (c) security and access control documentation, (d) sample outputs: BIR-registered receipt format, sales invoice, purchase invoice, journal voucher, official receipt, books of accounts (general journal, general ledger, cash receipts/disbursements journals, sales/purchases journals), (e) data retention and backup procedures, (f) audit trail documentation, (g) BIR permit application letter signed by entity's authorized representative | IT Team / ERP Vendor | CIO | 2–3 weeks/entity |
| 3 | Controller reviews and validates sample outputs for accounting accuracy: GL account mapping, journal entry formatting, books of accounts layout compliance with BIR-prescribed format | Controller | CFO | 4 hours/entity |
| 4 | Regulatory Officer submits CAS registration application to BIR Regional Office (or Revenue District Office) where the entity is registered; pays registration fee per BIR schedule | Regulatory Officer | Legal Head | 1 day/entity |
| 5 | BIR evaluates application; may conduct system demonstration or on-site inspection at BuildRight office; IT and Finance present system capabilities to BIR evaluators | BIR / IT / Finance | CFO | 1–2 days/entity (if inspection required) |
| 6 | BIR issues CAS Permit (Authority to Use Computerized Accounting System) per entity; permit includes registered system name, entity TIN, permit number, and conditions of use | BIR | — | External (2–6 months from submission) |
| 7 | Regulatory Officer records CAS permit in system: permit number, issue date, expiry date (if applicable — some permits are perpetual unless system changes), entity TIN, authorized system name; uploads permit document to entity master | Regulatory Officer | Legal Head | 15 min/entity |
| 8 | IT configures ERP to print BIR-registered receipt/invoice numbers per CAS permit: system generates sequential, non-skippable invoice/receipt numbers per BIR requirements; TIN, registered business name, and CAS permit number printed on all receipts per BIR format | IT Team | CIO | 2–3 days/entity |
| 9 | **Annual renewal** (if required per BIR ruling): Regulatory Officer submits renewal documentation before expiry; confirms no material system changes since last registration | Regulatory Officer | Legal Head | 2 hours/entity/year |
| 10 | **Re-registration triggers**: if ERP system undergoes major version upgrade, change of ERP platform, or change of entity legal name, Regulatory Officer files amended CAS registration with updated system documentation | Regulatory Officer / IT | CFO | Per initial process |

### System Touchpoints (BIR CAS)
- CAS permit tracking in entity master: permit number, issue date, expiry date, authorized system name (W54A.7)
- BIR-compliant sequential invoice/receipt numbering: system enforces non-skippable, sequential numbering per CAS permit per entity; voided transactions retain number with void indicator per BIR requirements; system prints or records a BIR-compliant void receipt referencing the original transaction number, void reason code, and authorizing manager ID per CAS permit conditions (W54A.8)
- BIR books of accounts generation: system produces general journal, general ledger, cash receipts journal, cash disbursements journal, sales journal, and purchases journal in BIR-prescribed format (per CAS registration commitment) (W54A.2)
- Entity-level CAS permit number printed on all receipts, invoices, and official receipts alongside entity TIN (W54A.8)
- Integration with W5B (BIR-registered receipt printing), W9A (books of accounts generation for close), W16 (new entity setup — CAS registration required before entity can transact), W54 (LGU permits — Regulatory Officer manages both)

### Pain Points / Risks
- **2–6 month BIR processing delay**: BIR CAS permit processing is notoriously slow in the Philippines; the entity cannot legally generate BIR-registered receipts until the permit is issued, creating a go-live risk for new entities or ERP implementations
- **BIR inspection unpredictability**: BIR may or may not conduct an on-site inspection; if requested, IT and Finance must present the system with limited notice, requiring continuous audit readiness during the registration period
- **Sequential invoice numbering strictness**: BIR requires non-skippable sequential numbering; any system bug that skips a number (e.g., due to POS offline mode or failed transaction) creates a compliance gap that must be explained and documented
- **System change re-registration trigger**: Any major ERP upgrade or change of platform requires re-registration with the same 2–6 month BIR timeline; this effectively locks BuildRight into its current ERP platform or creates extended compliance risk during migrations

---

### Time Estimate
- Initial registration per entity: 2–3 weeks for documentation + 1 day for submission + 2–6 months BIR processing + 2–3 days for ERP configuration = ~3–7 months end-to-end per entity
- System documentation package preparation: 2–3 weeks/entity (IT and ERP vendor)
- BIR inspection (if required): 1–2 days/entity
- ERP receipt/invoice configuration: 2–3 days/entity
- Annual renewal: 2 hours/entity/year
- Re-registration (major system change): same as initial registration timeline

### Staffing Implication
- **Regulatory Officer**: initial registration adds ~40–60 hours across 5 entities (concentrated during ERP implementation Phase 2); annual renewals add ~10 hours/year. Absorbed within existing role.
- **IT**: system documentation preparation adds ~2–3 weeks/entity during implementation; absorbed within implementation project.
- **Controller**: sample output validation adds ~4 hours/entity during implementation; absorbed.

## W77. BIR Tax Audit Response

| Field | Detail |
|---|---|
| **Trigger** | BIR issues Letter of Authority (LOA) or audit notification to any BuildRight entity |
| **Frequency** | Occasional; estimated 1–2 BIR audits/year across 5 entities; higher probability for entities with large revenue or import activity |
| **Volume** | Audit scope varies — from specific tax type (VAT only) to comprehensive (income tax, VAT, withholding tax) for 1–3 taxable years |
| **Owner** | Tax Accountant (operational); Controller (oversight); CFO (escalation) |
| **Participants** | Tax Accountant, Controller, CFO, Chief Accountant, AP Clerk, AR Clerk, IT, Legal, external tax advisor, BIR Revenue Officers |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | BIR Revenue Officer presents Letter of Authority (LOA) at entity's registered office or BIR Regional Office; Tax Accountant receives and logs LOA in system: LOA number, audit period, tax types under audit, assigned Revenue Officers, deadline for submission | Tax Accountant | Controller | 30 min |
| 2 | Controller and CFO assess audit scope and risk; engage external tax advisor (CPA firm) for audit representation if assessment is complex or potential exposure is material (> PHP 1M) | Controller / CFO | CEO | 1 hour |
| 3 | Tax Accountant gathers documents per BIR requirements — system generates: (a) books of accounts (general journal, general ledger, cash receipts/disbursements journals, sales/purchases journals) per BIR format and CAS permit (W54A), (b) VAT returns and supporting schedules for audit period, (c) withholding tax returns (1601-E, 1601-C) and alphalist of payees, (d) income tax returns and supporting financial statements, (e) summary of credit/debit notes, (f) list of related-party transactions and IC pricing documentation per W14, (g) fixed asset register and depreciation schedules, (h) inventory records and physical count reports (W42) | Tax Accountant / Chief Accountant | Controller | 2–5 days |
| 4 | Tax Accountant prepares working papers reconciling tax returns to books of accounts; identifies and documents any discrepancies or areas of exposure before submission to BIR | Tax Accountant | Controller | 3–5 days |
| 5 | Tax Accountant or external tax advisor submits documents to BIR Revenue Officers per LOA deadline; logs submission date and receipt confirmation in system | Tax Accountant | Controller | 1 day |
| 6 | BIR conducts examination: Revenue Officers may request additional documents, clarifications, or schedule meetings/walkthroughs; Tax Accountant coordinates responses within 5 business days per BIR practice | Tax Accountant / Controller | CFO | Varies (weeks to months) |
| 7 | BIR issues Preliminary Assessment Notice (PAN) if deficiencies found; Tax Accountant and external tax advisor review PAN; prepare protest or rebuttal within 15 days of receipt if assessment is disputed | Tax Accountant / External Advisor | CFO | 3–5 days |
| 8 | If protest accepted by BIR: case closed; Tax Accountant documents final resolution. If BIR issues Final Assessment Notice (FAN): Tax Accountant evaluates options — (a) accept assessment and pay deficiency tax + surcharge + interest; (b) escalate to Court of Tax Appeals or file motion for reconsideration within 30 days | Tax Accountant / CFO / Legal | CEO | 3–10 days |
| 9 | If payment required: Treasury processes payment per W30; system posts payment (Dr. Tax Payable / Dr. Tax Penalty Expense / Cr. Cash); Tax Accountant files amended returns if applicable | Treasury Analyst / Tax Accountant | CFO | Per W30 |
| 10 | Post-audit: Controller and Tax Accountant conduct lessons-learned review; document findings and corrective actions to prevent recurrence; update internal tax compliance procedures (W9A) if needed; include audit outcomes in next quarterly management committee meeting (W35.14) | Controller / Tax Accountant | CFO | 2 hours/audit |
| 11 | Quarterly: Tax Accountant maintains BIR audit readiness checklist: confirm books of accounts are current and BIR-compliant, withholding tax alphalists reconcile to returns, IC transfer pricing documentation is complete per W14, CAS permit is current per W54A, all tax returns filed on time | Tax Accountant | Controller | 2 hours/quarter |

### System Touchpoints
- BIR audit register: LOA number, audit period, tax types, Revenue Officers, submission deadlines, assessment amounts, protest status, resolution date (W77.1)
- Books of accounts generation in BIR-prescribed format per CAS permit (W77.3, cross-reference W54A)
- Tax return and supporting schedule retrieval for audit periods (W77.3)
- Document submission tracking with deadline alerting (W77.5)
- Assessment tracking with protest deadline management (W77.7–8)
- Integration with W9A (month-end close — source of audit documents), W14 (IC transfer pricing documentation), W30 (payment of deficiencies), W35 (management reporting), W54A (CAS permit compliance)

### Pain Points / Risks
- **Document preparation burden**: Gathering 2–3 years of books of accounts, VAT returns, withholding alphalists, and supporting schedules for 5 entities is extremely labor-intensive; if internal records have reconciliation gaps, preparation time doubles
- **BIR assessment subjectivity**: BIR Revenue Officers have significant discretion in interpreting tax regulations; assessments may include aggressive positions (e.g., disallowing legitimate deductions) that require formal protest within 15 days, creating legal and financial exposure
- **Intercompany transfer pricing scrutiny**: With 5 entities and complex IC transactions (W14), BIR may challenge transfer pricing; if IC documentation is incomplete or pricing is not at arm's length, potential deficiency assessments can be material (PHP millions)
- **Ongoing audit readiness cost**: The quarterly audit readiness checklist (step 11) adds persistent overhead; failure to maintain continuous readiness means the next BIR audit will require emergency document preparation, increasing the risk of errors and unfavorable assessments

---

### Time Estimate
- LOA receipt and logging: 30 min (step 1)
- Scope assessment and advisor engagement: 1 hour (step 2)
- Document gathering and preparation: 2–5 days (step 3)
- Working papers preparation: 3–5 days (step 4)
- Document submission: 1 day (step 5)
- BIR examination period: weeks to months (step 6)
- PAN/FAN response: 3–10 days (steps 7–8)
- Post-audit lessons learned: 2 hours (step 10)
- Quarterly audit readiness: 2 hours/quarter (step 11)
- Total active audit: ~80–160 hours over 2–6 months per audit

### Staffing Implication
- **Tax Accountant**: audit response adds ~40–80 hours per audit over 2–4 months. Absorbed within existing role with priority reallocation during active audits.
- **External tax advisor**: engaged for complex audits; budgeted within Finance operations.
- **No incremental headcount.**

## W78. Government / Institutional Procurement Participation

| Field | Detail |
|---|---|
| **Trigger** | Government agency, LGU, or state-owned enterprise issues Invitation to Bid or Request for Quotation (RFQ) for construction materials, hardware, or related supplies |
| **Frequency** | ~20–40 government procurement opportunities/year; primarily infrastructure agencies (DPWH), LGUs, DepEd, DOH, and state universities |
| **Volume** | Individual contract values PHP 500K–20M; represents ~5–8% of total revenue |
| **Owner** | Sales Rep (Trade & Corporate) — dedicated government accounts representative |
| **Participants** | Sales Rep, Category Manager, Pricing Analyst, Legal, Finance, Supply Planner |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Sales Rep monitors government procurement opportunities: PHILGEPS (Philippine Government Electronic Procurement System) portal, agency websites, and newspaper postings per RA 9184 (Government Procurement Reform Act); identifies opportunities matching BuildRight's product range | Sales Rep | VP Merchandising | 2 hours/week |
| 2 | Sales Rep evaluates opportunity viability: (a) product match — does BuildRight carry the specified items or equivalents, (b) delivery capability — can BuildRight deliver to the agency's required locations within the specified timeline, (c) pricing competitiveness — can BuildRight meet the Approved Budget for the Contract (ABC), (d) eligibility — does BuildRight meet PHILGEPS registration, BIR tax compliance, and other bidder eligibility requirements | Sales Rep | Category Manager | 1–2 hours/opportunity |
| 3 | Sales Rep prepares bid/quote documents per agency requirements: (a) PHILGEPS registration certificate, (b) BIR tax compliance certificate, (c) business permits per W54, (d) audited financial statements (most recent year from W9B), (e) similar completed projects or supply contracts, (f) product specifications and pricing, (g) delivery schedule and terms, (h) bid security (if required) | Sales Rep / Legal | VP Merchandising | 4–8 hours/bid |
| 4 | Category Manager and Pricing Analyst review proposed pricing: ensure margin is adequate (minimum gross margin target for government contracts, typically 10–15%); verify that pricing does not violate any existing contract pricing or trade agreements | Category Manager / Pricing Analyst | VP Merchandising | 1–2 hours/bid |
| 5 | Sales Rep submits bid/quote per agency deadline (sealed bid, electronic submission, or direct quotation depending on procurement method per RA 9184) | Sales Rep | VP Merchandising | Per deadline |
| 6 | **If awarded**: Sales Rep creates Sales Order in system linked to government Purchase Order; applies government-specific pricing and delivery schedule; system creates delivery plan per W19 or in-store pickup per W11 (BOPIS); revenue recognized at delivery per standard process | Sales Rep | Finance Manager | Per W58 |
| 7 | **Billing**: Sales Rep generates billing documents per government agency requirements — (a) standard sales invoice with BIR-registered format, (b) delivery receipt signed by agency receiving officer, (c) collection receipt per agency's accounting procedures; government accounts typically on Net 30–60 terms; collection requires submission of complete billing documents per agency-specific procedures (some agencies require liquidation documents or progress reports) | Sales Rep / AR Clerk | AR Supervisor | Per W8 |
| 8 | **Collection**: AR Clerk follows up on government receivables per W8 collection tiers; government payments may be delayed due to budget processing — Sales Rep coordinates with agency procurement officer and accounting division; system tracks government receivable aging separately from trade accounts for reporting | AR Clerk / Sales Rep | AR Supervisor | Per W8 |
| 9 | Quarterly: Sales Rep and Category Manager review government account portfolio: win rate, revenue, margin, collection timeliness, and bid pipeline; VP Merchandising reviews as part of corporate account portfolio (W58.10) | Sales Rep / Category Manager | VP Merchandising | 2 hours/quarter |

### System Touchpoints
- PHILGEPS registration tracking in vendor/customer master with renewal alerting (W78.1)
- Government customer account with specialized billing requirements, delivery terms, and collection procedures (W78.6–8)
- Government-specific pricing and margin validation per W40 approval workflow (W78.4)
- Government receivable aging separate from trade accounts for reporting and collection management (W78.8)
- Integration with W8 (AR and collections), W19 (delivery), W24 (credit application — government accounts may use purchase orders instead of credit), W40 (pricing), W54 (LGU permits — build compliance documentation), W58 (corporate account management)

### Pain Points / Risks
- **Government payment delays**: Philippine government agencies are notoriously slow payers (Net 60–120 days in practice vs. Net 30–60 contract terms); delayed collections strain working capital and inflate AR aging, requiring dedicated follow-up
- **Bid preparation resource intensity**: Each bid requires compliance documentation (PHILGEPS, BIR tax compliance, business permits, audited financials); with 20–40 opportunities/year, the administrative burden is significant for a single Sales Rep
- **Low margin pressure**: Government procurement's Approved Budget for the Contract (ABC) often compresses margins to 10–15%; if actual costs (delivery to remote agency sites, compliance overhead) are not precisely estimated, winning bids can become loss-making
- **PHILGEPS registration maintenance**: BuildRight must maintain current PHILGEPS registration, BIR tax compliance certificates, and LGU business permits for all 5 entities to remain eligible; any lapsed registration disqualifies the company from all government procurement

---

### Time Estimate
- PHILGEPS monitoring: 2 hours/week (step 1)
- Opportunity viability assessment: 1–2 hours/opportunity (step 2)
- Bid/quote document preparation: 4–8 hours/bid (step 3)
- Pricing review: 1–2 hours/bid (step 4)
- Bid submission: per deadline (step 5)
- Quarterly portfolio review: 2 hours/quarter (step 9)
- Total per bid: ~8–14 hours from identification to submission; at 20–40 opportunities/year, ~160–560 hours/year for government accounts rep

### Staffing Implication
- **1 Sales Rep (dedicated government accounts)**: within the existing 3–4 Sales Reps (Trade & Corporate) per W58, one rep should specialize in government accounts given the unique procurement regulations and document requirements; PHILGEPS monitoring and bid preparation add ~8–12 hours/week during active bidding periods.
- **No incremental headcount.** Absorbed within existing B2B sales team.

## W79. Employee Grievance & Whistleblower Process

| Field | Detail |
|---|---|
| **Trigger** | Employee files a grievance regarding workplace conditions, policy violations, harassment, discrimination, or unethical conduct; or whistleblower report of fraud, corruption, or legal non-compliance |
| **Frequency** | Estimated 20–50 grievance/whistleblower reports/year across all locations |
| **Volume** | Grievance categories: workplace conflict (30%), policy/procedure concern (25%), compensation/benefits dispute (20%), harassment/discrimination (15%), safety concern (10%) |
| **Owner** | HR Head (grievance); Internal Audit (whistleblower reports involving management) |
| **Participants** | Employee, HR Head, Internal Audit, Legal, Department Head / Store Manager, CHRO |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Employee submits grievance or whistleblower report; or incident reported (theft, misconduct, policy violation) | Employee / Manager | — | 15 min |
| 2 | HR Head (grievance) or Internal Audit (whistleblower) acknowledges receipt within 24 hours; assigns case number; classifies severity (Minor, Serious, Grave, Critical) | HR Head / Internal Audit | CHRO | 15 min/case |
| 3 | **Due Process: Notice to Explain (NTE)**: For disciplinary cases, HR issues NTE to employee; provides 120 hours (5 business days) to submit written response per Philippine Labor Code | HR ER Officer | — | 30 min |
| 4 | Employee submits written explanation; system records date/time received; HR reviews explanation | Employee | — | — |
| 5 | **Administrative Hearing**: For Serious/Grave offenses, HR conducts hearing; documents proceedings in system; respondent allowed counsel or union representative | HR ER Officer | Dept Head | 1–2 hours |
| 6 | **Decision / Notice of Decision (NOD)**: HR and Dept Head determine outcome (Exoneration, Warning, Suspension, or Termination) per company table of offenses | HR Head | Dept Head | 1 hour |
| 7 | System generates NOD; issued to employee; system updates employee record with disciplinary status; if Suspension: System auto-blocks timekeeping for suspension dates | HR ER Officer | — | 15 min |
| 8 | **Whistleblower / High Severity Investigation**: For harassment, fraud, or corruption — HR Head and Legal/Audit jointly investigate; whistleblower identity protected; retaliation protection flagged (W79.7) | HR Head / Legal / Internal Audit | CHRO / CEO | 8–20 hours/case |
| 9 | Monthly: HR Head generates grievance/whistleblower summary; reports to CHRO and CEO | HR Head | CHRO | 2 hours/month |

### System Touchpoints
- Grievance submission form in self-service portal with category, severity, and desired resolution fields (W79.1)
- Anonymous whistleblower channel (email or third-party hotline) integration with case management (W79.1)
- Case management with severity classification, investigation tracking, evidence attachment, and resolution documentation (W79.2–6)
- Retaliation protection: system flags adverse actions against grievance filers within 90-day lookback (W79.7)
- Grievance/whistleblower analytics: volume, category, severity, location, resolution time (W79.8)
- Integration with W10 (payroll — preventive suspension with pay), W43 (separation — pending grievance resolved before clearance), W47 (safety concerns), W51 (self-service portal, training improvements), W72 (corrective action and progressive discipline)
- Whistleblower anonymity technical controls: the anonymous whistleblower channel (dedicated email or third-party hotline) is configured with the following technical safeguards: (a) no IP address logging on the whistleblower submission form; (b) no employee ID or session token capture on anonymous submissions; (c) if third-party hotline is used, the provider contractually commits to not disclosing reporter identity to BuildRight management; (d) system stores whistleblower case records with a pseudonymous case ID — the real identity is accessible only to the DPO and Internal Audit lead (dual-access control); (e) retaliation protection (W79.7) is extended to anonymous reporters where identity is later inferred or disclosed; (f) annual: DPO reviews whistleblower channel anonymity safeguards as part of privacy impact assessment (W53)

### Time Estimate
- Grievance submission and acknowledgment: 15–30 min/case (steps 1–2)
- NTE preparation and issuance: 30 min/case (step 3)
- Administrative hearing: 1–2 hours/case for Serious/Grave offenses (step 5)
- Decision and NOD issuance: 1 hour/case (steps 6–7)
- Whistleblower/high-severity investigation: 8–20 hours/case (step 8)
- Monthly summary reporting: 2 hours/month (step 9)
- Estimated total: ~200–400 hours/year across all grievance/whistleblower cases

### Pain Points / Risks
- **Procedural compliance with Philippine Labor Code**: Strict due process requirements (120-hour NTE response window, right to counsel, written NOD) must be followed exactly; any procedural deviation can render a termination illegal, exposing BuildRight to illegal dismissal claims and back-pay liability
- **Whistleblower anonymity breach risk**: If the system's anonymity safeguards (no IP logging, pseudonymous case IDs) are accidentally bypassed — e.g., through system logs, email metadata, or verbal slip by investigators — the whistleblower's identity is exposed, undermining trust in the program and creating legal liability under RA 10173
- **Retaliation detection difficulty**: The 90-day lookback for adverse actions against grievance filers is conceptually sound but difficult to enforce in practice; managers may disguise retaliation as performance-based actions, requiring Internal Audit to make subjective judgments
- **High-severity investigation resource drain**: Cases involving harassment, fraud, or corruption (step 8) require 8–20 hours each from HR Head, Legal, and Internal Audit; with ~5–10 such cases/year, this diverts senior leadership from strategic priorities during multi-week investigations

### Staffing Implication
- **HR Head**: grievance investigation adds ~20–40 hours/year. Absorbed within existing role.
- **Internal Audit**: whistleblower investigation adds ~10–20 hours/year. Absorbed.
- **No incremental headcount.** Grievance handling is a core HR function distributed across existing management.

---

### HQ Departments

| Department | Roles | Count | Key Workflows | Validation |
|---|---|---|---|---|
| **Merchandising & Buying** | VP, Category Managers, Buyers, Pricing Analysts, Merch Planners | ~40 | W1, W2, W13, W20, W23, W27, W29, W32, W36, W40, W44, W68 | ✅ Adequate for daily PO review + quarterly assortment cycles + VMI/consignment oversight + rebate management + seasonal planning + vendor onboarding + price maintenance + product discontinuation lifecycle; includes 1–2 dedicated Buyers for trade/special orders (W38) within the ~40 team |
| **Finance & Accounting** | Controller, Chief Accountant, AP/AR Clerks, Treasury, Tax | ~35 | W7, W7D, W8, W9, W14, W21, W24, W25, W26, W27, W28, W30, W39, W42, W54A (CAS permit validation), W59, W60, W70, W74 | ✅ Stretched during close week; capex/credit/petty cash absorbed; treasury daily cycle manageable with 2–3 analysts; asset disposal and annual physical inventory absorbed; insurance lifecycle and emergency procurement review absorbed; credit/debit note reconciliation absorbed into month-end close and weekly AP/AR review; AP staffing recalculated on business-day basis: ~305–370 invoices/business-day (6,715 merchandise + 2,000–3,000 non-PO per month ÷ 22 business days) requiring 10 clerks at ~5–6 hrs each/day; month-end peak (+50%) requires overtime or Finance staff redeployment; vendor statement reconciliation (W7D) absorbed into monthly AP cycle; employee expense reimbursement (W74) adds ~25–42 hours/month absorbed across AP team |
| **Supply Chain & Logistics** | Supply Planners, Demand Planners, Import Coordinator, Fleet Manager, DC Ops managers | ~31 | W3, W3C, W4, W4B, W19, W19B, W22, W22B, W31, W52, W56, W57, W62B, W66 | ✅ 2–3 planners handle replenishment + store-initiated requests + transfers + backorder fulfillment + promo allocation; home delivery and ship-from-store picked by DC/store staff; 1–2 dedicated demand planners handle forecasting; 1 Fleet Manager manages owned vehicles and 3PL relationships; Import Coordinator absorbs inter-island logistics; DC inbound scheduling (W3C) absorbed by DC Receiving Supervisor; 3PL partner onboarding (W62B) absorbed by Fleet Manager; allocation rule governance reviewed quarterly as part of W31.8 parameter cycle |
| **HR & Payroll** | HR Head, Recruitment, Payroll, Training Officer, HR Assistants | ~16 | W10, W15, W51, W72 | ✅ 2–3 payroll officers + 2 recruiters + 1 Training Officer handle the volume; employee performance management absorbed by ~230 managers |
| **Marketing** | Brand, Promo, Loyalty, Ecommerce, Digital, Content, CS Manager | ~24 | W13, W17, W50, W61, W65 | ✅ Loyalty is largely automated; promo work is cyclical; dedicated Content Manager + 2–3 Content Specialists for ecommerce product content; CS Manager owns customer satisfaction measurement; price match review absorbed by Pricing Analysts |
| **Store Operations** | Director, Regional Managers, CS Manager, Ops Standards, Facilities Coordinator | ~23 | W5, W5D (in-store delivery), W5E (opening delay), W16, W29, W5G (offline recovery), W34, W37, W41, W47, W49, W54A, W67, W69, W71 | ✅ 4 Regional Managers × 50 stores each; oversee new openings and monthly store performance reviews; in-store delivery uses existing 3PL carrier infrastructure; opening delay procedure is Store Mgr responsibility; offline recovery is Store Mgr responsibility; shift scheduling and complaint handling absorbed; 2–3 LPOs recommended for loss prevention; 1 Facilities Coordinator manages store maintenance, disaster response, and physical security oversight; weekly price compliance audits absorbed by Dept. Supervisors and Stock Associates |
| **IT** | Infrastructure, Apps, Data, Security, BI Analyst, Helpdesk | ~28–30 | W16 (store setups), W35 (reporting), W48 (helpdesk & IT ops) | ✅ 4–5 helpdesk agents + 3–4 specialists handle ~800–1,200 tickets/month; 2–3 per store setup + BAU support; 1 BI Analyst supports management reporting; note: for physical IT support across the Philippine archipelago (200 stores + 4 DCs across Mindanao, Visayas, Luzon), 1–2 dedicated field staff may not provide adequate same-day response for P1 incidents in remote locations — recommend (a) training designated Store Managers as first-level hardware troubleshooters (certified on basic POS terminal swap, cable reseat, network restart), (b) contracting regional IT service providers in each major region (Davao, Cebu, Manila, Clark) for emergency on-site support, and (c) maintaining a spare POS terminal and network equipment swap stock at each DC for rapid dispatch |
| **Other** | Legal, Internal Audit, DPO, Regulatory Officer, Customer Service (call center), Executive | ~52 | W41 (complaints), W42 (audit observation), W53 (data privacy breach, DSAR lifecycle, data portability/erasure), W54 (LGU permits), W54A (BIR CAS registration), W62 (vendor contracts) | ✅ Support functions; call center handles multi-channel complaint intake; Legal expanded to include DPO (W53 with full DSAR lifecycle) and Regulatory Officer (W54 LGU + W54A BIR CAS); total Legal & Compliance expands from ~5 to ~7 |

### Per-Store Staffing (30 people)

| Role | Count | Key Workflows | Workload Validation |
|---|---|---|---|
| Store Manager | 1 | W5 (open/close), W5D (in-store delivery coordination), W5E (opening delay handling), W6 (approvals), W12 (returns), W16 (opening), W22B (store-to-DC returns), W54 (LGU permit coordination), W67 (monthly performance review), W69 (price audit review) | Manageable; delegates floor ops to supervisors |
| Asst. Store Manager | 1 | W5 (open/close backup), W6, W12 | Shares management load; covers days off |
| Dept. Supervisors | 4 | W5B (floor selling), W6 (cycle count review), W12 (restock), W69 (price compliance audit execution and review) | 4 depts × 1 supervisor; handles floor + counts + weekly price audits |
| Sales Associates | 12 | W5B (selling, paint mixing, lumber cutting), W5D (in-store delivery staging), W11 (BOPIS pick), W56 (backorder intake), W61 (price match verification) | 3/dept × 2 shifts = adequate for floor coverage |
| Cashiers | 5 | W5B (checkout), W17 (loyalty scan), W28 (gift card sell/reload) | 5 terminals; covered in shifts; tight on coverage |
| Receiving Clerks | 2 | W4 (store receiving from DC), W18 (DSD receiving), W22 (transfer receiving), W22B (store-to-DC return staging) | 2–3 DC trucks/week + 2–3 DSD/week + transfers + return staging; 2 clerks in shifts handle it |
| Stock Associates | 3 | W4 (shelf stocking), W4B (store replenishment request), W6 (cycle counting), W11 (BOPIS pick), W18 (DSD shelving), W19B (ship-from-store picking), W22 (transfer pick/receive), W22B (store-to-DC return packing), W34 (shift adherence), W42 (annual count), W57 (promo stock staging), W63 (shelf label application), W69 (price audit scanning) | 700 SKUs/day counting + stocking + DSD + transfers + label updates + weekly price audit; adequate but minimal slack |
| Customer Service Rep | 1 | W11 (BOPIS handoff), W12 (returns), W24 (credit application assistance), W28 (store credit), W29 (recall returns), W33 (warranty claims), W38 (special order intake), W41 (complaints) | ~4 BOPIS + ~2 returns + ~0.5 gift cards + ~2 warranty claims + ~0.5 special orders + ~10 complaints/day = moderate; also handles special orders |
| Maintenance | 1 | W5F (closing checklist), W47 (facility maintenance & work orders), general upkeep | Standard for big-box format; handles ~10–15 maintenance work orders/month including preventive tasks; external contractors engaged for specialized repairs |
| **Total** | **30** | | **Validated — headcount is lean but supportable** |

### Per-DC Staffing (~150 people)

| Function | Count | Key Workflows | Workload Validation |
|---|---|---|---|
| DC Manager + Supervisors | 5 | W3, W4 (oversight) | 1 manager + 4 shift/area supervisors |
| Receiving | 10–13 | W3 (receiving & putaway), W20 (VMI receipt) | ~40 receipts/day × 1.5–3 hrs; 3–4 clerks + 4–6 putaway + 1–2 QC |
| Picking & Packing | 25–30 | W4 (pick/pack/ship), W19 (home delivery pick/pack) | ~33 store orders + ~115 home delivery orders/day; 15–20 pickers + 8–10 packers; 3–4 dedicated to home delivery; peak ecommerce periods may require surge staffing |
| Loading & Dispatch | 6–8 | W4 (loading) | Multi-drop truck loading; 4–6 crew + dispatch |
| Inventory Control | 2–3 | W6 (DC cycle counts) | DC-level accuracy monitoring |
| Admin & Support | 5–8 | Admin, safety, maintenance | Office, security, equipment maintenance |
| Special Handling (lumber, tiles, paint) | 8–10 | W3, W4 (special areas) | Dedicated teams for heavy/hazardous goods |
| **Total** | **~150** | | **Validated** |

---

## W82. Hazardous Waste Disposal Tracking & DENR Compliance

| Field | Detail |
|---|---|
| **Trigger** | Hazardous waste accumulation at location reaches disposal threshold; or quarterly disposal schedule; or DENR reporting deadline |
| **Frequency** | Disposal: quarterly per location (minimum); DENR reporting: quarterly; Permit renewal: annual per location |
| **Volume** | Hazardous waste categories: paint/chemical waste (sludge, expired products, solvent rags), used oils and lubricants (from fleet maintenance W52, forklift maintenance), broken fluorescent lamps and LED tubes (mercury content), used batteries (lead-acid from forklifts, UPS systems), aerosol cans (residual propellant); ~200 stores + 4 DCs each generating small but regulated quantities |
| **Owner** | Regulatory Officer (HQ); Store Manager / DC Manager (location-level execution) |
| **Participants** | Regulatory Officer, Store Manager, DC Manager, Maintenance Staff, accredited transporter, DENR-accredited treatment/disposal facility, Finance (disposal cost), Legal |

### Background

BuildRight Depot operations generate hazardous waste across several categories regulated by the Philippine Department of Environment and Natural Resources (DENR) under Republic Act 6969 (Toxic Substances and Hazardous and Nuclear Wastes Control Act) and its implementing rules (DAO 29, DENR Administrative Order). Each location (store or DC) that generates hazardous waste is classified as a waste generator and must hold a DENR Hazardous Waste Generator Registration (HWGR). Compliance requires: proper storage and labeling, use of DENR-accredited transporters and treaters, manifest tracking, and quarterly disposal reports.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Location registration**: for each new store (W16) or DC, Regulatory Officer applies for DENR Hazardous Waste Generator Registration (HWGR) — submits required documents (business permit, location map, waste management plan, emergency response plan) to DENR-EMB regional office; receives HWGR certificate with generator ID number; system records HWGR number, registration date, and expiry date per location | Regulatory Officer | Legal Head | 2–4 hours/location (initial) |
| 2 | **Annual renewal**: system alerts Regulatory Officer 90 days before HWGR expiry per location; Regulatory Officer submits renewal documents to DENR-EMB; renewed certificate uploaded to location document management (W54-style permit tracking) | Regulatory Officer | Legal Head | 1 hour/location/year |
| 3 | **Ongoing accumulation at location**: Maintenance Staff (or designated Stock Associate at stores) segregates hazardous waste by category in designated, properly labeled storage containers — (a) **paint/chemical waste**: expired paint, adhesives, solvents, contaminated rags — stored in sealed drums in ventilated area away from ignition sources, (b) **used oils**: from forklift maintenance at DCs and vehicle maintenance per W52 — stored in sealed containers in bunded area, (c) **fluorescent lamps**: broken or expired tubes — stored in original packaging or dedicated collection boxes, (d) **used batteries**: lead-acid batteries from forklifts and UPS systems — stored upright on spill containment pallets, (e) **aerosol cans**: residual product cans — stored in vented containers | Maintenance Staff / Stock Associate | Store Manager / DC Manager | Ongoing |
| 4 | **Accumulation monitoring**: system tracks hazardous waste accumulation per location per waste category — Maintenance Staff logs waste additions (category, estimated quantity, date) in system via handheld or terminal; system flags location when accumulated quantity approaches disposal threshold (configurable per category based on DENR storage limits — typically 90 days maximum storage) | Maintenance Staff | Store Manager / DC Manager | 5 min/entry |
| 5 | **Disposal scheduling**: when location reaches disposal threshold or quarterly schedule triggers — Regulatory Officer coordinates disposal with DENR-accredited transporter and DENR-accredited treatment/storage/disposal (TSD) facility; obtains quotations from accredited providers; selects based on: DENR accreditation status, cost, proximity, service reliability | Regulatory Officer | Legal Head | 1–2 hours/disposal event |
| 6 | **Transporter accreditation verification**: before each shipment, Regulatory Officer verifies transporter's DENR accreditation (PCO license, transport permit, vehicle registration with DENR) is current and valid; system maintains accredited transporter registry with accreditation expiry tracking and auto-alerting | Regulatory Officer | Legal Head | 15 min/verification |
| 7 | **Hazardous waste manifest (DENR Form)**: Regulatory Officer prepares DENR-compliant hazardous waste manifest per shipment — (a) generator information (BuildRight location name, address, HWGR number), (b) waste description (category, quantity, physical state, hazard characteristics), (c) transporter information (company name, DENR transport permit number, vehicle plate, driver name), (d) TSD facility information (company name, DENR permit number, facility address), (e) six-copy manifest per DENR format — signed by generator, transporter, and TSD facility | Regulatory Officer | Store Manager / DC Manager | 30 min/manifest |
| 8 | **Physical pickup**: accredited transporter arrives at location; Maintenance Staff and transporter representative jointly verify waste quantity and category against manifest; both sign manifest copies; transporter loads waste | Maintenance Staff / Transporter | Store Manager / DC Manager | 30–60 min/pickup |
| 9 | **Manifest tracking**: system tracks manifest lifecycle — (a) **Generated**: manifest created and signed by generator, (b) **In Transit**: transporter departs with waste, (c) **Received by TSD**: TSD facility signs manifest confirming receipt and treatment/disposal, (d) **Closed**: TSD returns signed manifest copy (generator copy) to Regulatory Officer within 30 days; if manifest not returned within 30 days, system alerts Regulatory Officer for follow-up with transporter and TSD | Regulatory Officer / System | Legal Head | 15 min/manifest tracking |
| 10 | **Disposal cost processing**: Finance processes disposal invoice from transporter/TSD — (a) invoice matched to manifest number and location, (b) cost allocated to location's operating expense (Dr. Waste Disposal Expense / Cr. Cash), (c) system tracks disposal cost per location per quarter for budgeting (W26) | AP Clerk / Finance | Controller | Per W7 |
| 11 | **Quarterly reporting**: Regulatory Officer prepares DENR quarterly disposal report (due within 30 days after end of quarter) — (a) total waste generated by category per location, (b) total waste disposed by category per location with manifest references, (c) transporter and TSD facility details, (d) current on-site waste inventory per location; report submitted to DENR-EMB regional office per location jurisdiction | Regulatory Officer | Legal Head | 4 hours/quarter |
| 12 | **Annual waste management plan update**: Regulatory Officer reviews and updates the waste management plan per location — (a) projected waste generation by category, (b) disposal schedule and budget, (c) transporter and TSD facility list, (d) emergency response procedures for spills or accidents; updated plan submitted to DENR as part of HWGR renewal | Regulatory Officer | Legal Head | 8 hours/year |
| 13 | **Spill / accidental release response**: if hazardous material spills or is accidentally released at a location — (a) Maintenance Staff contains spill using location's spill kit (positioned at paint area, chemical storage, and battery storage areas), (b) reports spill to Store Manager / DC Manager and Regulatory Officer, (c) Regulatory Officer assesses severity — minor spill (contained on-site, cleaned with standard PPE): location staff handles cleanup with proper disposal of contaminated materials per W82; major spill (spreading, off-site risk, or personnel exposure): Regulatory Officer engages DENR-accredited emergency response contractor and notifies DENR-EMB within 24 hours, (d) system logs spill event with date, location, material, quantity, response actions, and disposal of contaminated cleanup materials | Maintenance Staff / Regulatory Officer | Legal Head | Varies |

### System Touchpoints
- Hazardous waste generator registration (HWGR) tracking per location with expiry alerting (W82.1–2)
- Hazardous waste accumulation log per location per category with disposal threshold alerting (W82.3–4)
- DENR hazardous waste manifest lifecycle tracking: Generated → In Transit → Received by TSD → Closed; auto-alert if manifest not returned within 30 days (W82.7–9)
- Accredited transporter registry with DENR accreditation expiry tracking (W82.6)
- Quarterly disposal reporting: waste generation, disposal, and inventory by location and category (W82.11)
- Disposal cost tracking per location per quarter integrated with AP (W82.10)
- Spill / accidental release event logging with response documentation (W82.13)
- Integration with W16 (new store opening — HWGR registration as part of pre-opening permits), W25 (petty cash — small disposal costs may be paid from petty cash), W26 (budget — annual disposal budget per location), W47 (facility maintenance — spill kit maintenance and replenishment), W48 (IT helpdesk — hazardous waste system support), W52 (fleet — used oil and battery disposal), W54 (LGU permits — HWGR tracked alongside LGU business permits in location compliance dashboard), W62 (vendor contracts — transporter and TSD facility contracts), W68 (product discontinuation — hazardous waste disposal for discontinued chemicals/paint)

### Time Estimate
- Initial HWGR registration per location: 2–4 hours; annual renewal: 1 hour/location/year
- Accumulation logging: 5 min/entry (ongoing by Maintenance Staff)
- Disposal event coordination: 1–2 hours/disposal event (scheduling + transporter verification)
- Manifest preparation: 30 min/manifest; manifest tracking: 15 min/manifest
- Physical pickup: 30–60 min/pickup
- Quarterly DENR reporting: 4 hours/quarter
- Annual waste management plan update: 8 hours/year
- Spill response: varies (30 min for minor to days for major)
- Overall for Regulatory Officer: ~4–6 hours/month ongoing + 4 hours/quarter reporting + 8 hours/year planning

### Pain Points / Risks
- **204 locations with separate DENR registrations**: Each of the 200 stores and 4 DCs must maintain its own HWGR, waste accumulation log, and disposal manifest trail; the administrative volume is massive for a single Regulatory Officer, especially during quarterly DENR reporting deadlines
- **Accredited transporter availability**: DENR-accredited hazardous waste transporters are limited in the Philippines, especially for VisMin locations; if the nearest accredited transporter is fully booked or their DENR permit lapses, disposal may be delayed beyond the 90-day storage limit, creating a compliance violation
- **Spill response at remote stores**: A paint or chemical spill at a remote Visayas or Mindanao store may require a DENR-accredited emergency response contractor who is hours or days away; the delay between containment and professional cleanup increases environmental damage and DENR reporting risk
- **Cost unpredictability**: Disposal costs vary by waste category, volume, location, and transporter availability; with 204 locations each generating small quantities, per-location costs are individually small but collectively material (~PHP 5–10M/year across the chain), and budget overruns are common

### Staffing Implication
- **Regulatory Officer** (1 person in Legal & Compliance team): manages HWGR registrations, disposal scheduling, manifest tracking, DENR reporting, and transporter accreditation for 200 stores + 4 DCs. Quarterly reporting adds ~4 hours; annual plan update adds ~8 hours; ongoing coordination adds ~4–6 hours/month. This role is justified by the regulatory compliance requirement and aligns with the Regulatory Officer position mentioned in the model company profile.
- **Maintenance Staff** (1 per store, part of existing headcount): hazardous waste segregation and logging adds ~15 min/week. Absorbed.
- **DC Safety/Environmental Officer** (1 per DC, within existing support staff): hazardous waste management at DCs adds ~2 hours/month. Absorbed.
- No incremental headcount beyond the Regulatory Officer role already planned in the model company profile.

---

## W95. External Audit Coordination & Support

| Field | Detail |
|---|---|
| **Trigger** | Annual external audit engagement per SEC requirement; quarterly review (if required by lenders or board); or special audit (M&A due diligence, regulatory investigation) |
| **Frequency** | Annual statutory audit (Q1 following fiscal year-end); quarterly interim review (if applicable) |
| **Volume** | 1 annual audit covering 5 entities + consolidated; quarterly reviews if required |
| **Owner** | Controller |
| **Participants** | Controller, CFO, Cost Accountant, AP Supervisor, AR Accountant, Treasury Analyst, Tax Accountant, Internal Audit, IT Manager, external auditors (CPA firm) |

### Background

As a Philippine corporation with 5 legal entities requiring consolidated financial statements, BuildRight must undergo an annual external audit by a SEC-accredited CPA firm per the Philippine Securities and Exchange Commission (SEC) requirements and the Philippine Financial Reporting Standards (PFRS). W77 (BIR Tax Audit Response) covers tax-specific audits by the Bureau of Internal Revenue. This workflow covers the broader external financial statement audit, which is a significant annual undertaking involving 5 entities, 200+ locations, and complex intercompany transactions. The external audit validates the financial statements that investors, lenders, regulators, and management rely upon.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Audit planning — engagement letter**: (a) CFO and Controller review and sign annual audit engagement letter from external auditors (typically signed Q4 for the following year's audit); (b) agree on audit scope (5 entities + consolidated), timeline (fieldwork in February, report by March–April), materiality thresholds, and audit fee; (c) Controller coordinates audit planning meeting with external audit partner and manager | CFO / Controller | CEO | 2 hours |
| 2 | **Pre-audit preparation** (January — after W9B year-end close): Controller assigns preparation tasks across Finance team: (a) **AP Supervisor**: finalize AP aging reconciliation, open GRNI analysis, vendor confirmation letters (send to top 50 vendors requesting confirmation of balances); (b) **AR Accountant**: finalize AR aging, send customer confirmation letters (top 50 trade/corporate accounts), prepare bad debt provision analysis (W81); (c) **Treasury Analyst**: complete all bank reconciliations (W89) through December 31, prepare bank confirmation requests (send to all 4 banks for all 25 accounts); (d) **Tax Accountant**: prepare annual tax reconciliation (W90), reconcile tax liability accounts, compile all BIR filings for the year; (e) **Cost Accountant**: prepare inventory valuation report (W9A.6), inventory reserve analysis (obsolescence, NRV), fixed asset register with depreciation schedule (W39); (f) **IT Manager**: prepare IT general controls documentation (access controls, change management, backup procedures per W48/W55) | Controller | CFO | 8 hours |
| 3 | **PBC (Prepared by Client) list fulfillment**: External auditors provide a PBC list of documents and schedules required for the audit; Controller assigns each item with deadline (typically 1–2 weeks before fieldwork start): (a) trial balance per entity, (b) consolidated elimination entries (W14), (c) intercompany reconciliation (W14.4–5), (d) revenue and expense analysis by category, (e) journal entry listing with supporting documentation for all manual JEs > materiality, (f) bank reconciliation reports (W89), (g) inventory count documentation from W42 annual physical inventory, (h) capex additions and disposals (W21, W39), (i) insurance schedule (W59), (j) related party transactions schedule, (k) contingent liabilities (pending litigation, tax assessments from W77), (l) subsequent events review (transactions after year-end through audit report date) | Finance Team | Controller | 20–30 hours total |
| 4 | **External audit fieldwork** (February — typically 2–3 weeks on-site at HQ): (a) **Opening meeting**: Controller, CFO, and external audit team agree on fieldwork schedule, key contact persons per area, and logistics; (b) **Substantive testing**: auditors test revenue (POS transaction sampling — W5B), purchases (PO and invoice sampling — W2/W7), inventory (observe physical count — W42, or rely on count documentation), bank balances (confirmations from W89), fixed assets (physical verification of additions), intercompany (W14 reconciliation), payroll (W10 sampling); (c) **Internal controls testing**: auditors test key controls — PO approval (W2.5–6), 3-way match (W7.2–3), credit approval (W24), physical security (W71), IT access controls (W48); (d) **Entity walkthroughs**: auditors may visit 1–2 stores and 1 DC for physical observation; Controller coordinates visits with Store Managers and DC Supervisors | External Auditors / Controller | CFO | 2–3 weeks |
| 5 | **Audit queries and information requests** (throughout fieldwork): (a) External auditors issue queries and additional information requests as testing proceeds; Controller triages and routes to appropriate Finance team member; (b) target response time: 2 business days for standard queries, 5 business days for complex analysis; (c) weekly status meetings between Controller and audit manager to track open queries and issues | Controller / Finance Team | CFO | Ongoing during fieldwork |
| 6 | **Draft financial statements review**: (a) External auditors present draft audited financial statements (per entity and consolidated) to Controller and CFO; (b) Controller reviews for accuracy vs. internal records, proper PFRS/IFRS presentation, and adequate disclosure; (c) Controller provides comments and corrections within 1 week | Controller / CFO | CEO | 4–6 hours |
| 7 | **Audit adjustments and passed adjustments**: (a) **Proposed audit adjustments**: external auditors propose correcting entries for any misstatements found during testing; Controller reviews and posts agreed adjustments per W9B year-end close; (b) **Passed adjustments (unadjusted differences)**: misstatements below materiality that auditors note but do not require correction; Controller logs passed adjustments in audit summary for future reference and potential cumulative materiality assessment | Controller | CFO | 2–4 hours |
| 8 | **Exit meeting and management letter**: (a) External auditors conduct exit meeting with Controller, CFO, and CEO to present audit findings, significant observations, and recommendations; (b) external auditors issue management letter with internal control recommendations (e.g., segregation of duties improvements, system access issues, process inefficiencies); (c) Controller prepares management response and action plan for each recommendation with deadlines and responsible persons; (d) management response reviewed and approved by CFO | Controller / CFO / CEO | CEO | 2 hours |
| 9 | **Audit report issuance**: External auditors issue audit opinion and audited financial statements; Controller files with SEC per regulatory deadline (typically within 120 days of fiscal year-end for corporations); files with BIR as part of 1702RT annual return (W90) | Controller / External Auditors | CFO | 2 hours |
| 10 | **Management letter follow-up**: Controller tracks implementation of management letter recommendations: (a) assigns each recommendation to responsible person, (b) tracks implementation progress quarterly, (c) reports status to CFO and Audit Committee, (d) unresolved items > 6 months escalated to CEO; external auditors review prior year recommendations in next year's audit | Controller | CFO | Ongoing |

### System Touchpoints
- Audit document management: engagement letter, PBC list, management letter, audit report stored per entity with DOC-001 document management (W95.1, 3, 8–9)
- Financial data extraction for PBC: trial balance, journal entries, aging reports, elimination entries per entity (W95.3)
- Audit trail: all transactions, approvals, and changes accessible for auditor review with full audit trail per NFR-007 (W95.4)
- Fixed asset register with depreciation schedule for auditor verification (W95.3e)
- Inventory valuation and reserve analysis for auditor review (W95.3e)
- Intercompany reconciliation and elimination documentation (W95.3c)
- Bank reconciliation reports and bank confirmation coordination (W95.3c)
- Management letter recommendation tracker with status and deadlines (W95.10)
- Integration with W7 (AP — vendor confirmations, 3-way match testing), W8 (AR — customer confirmations, bad debt analysis), W9 (financial close — audited financial statements source), W10 (payroll — compensation testing), W14 (IC — intercompany reconciliation and elimination testing), W21 (capex — addition verification), W30 (treasury — bank balance confirmation), W39 (fixed assets — physical verification), W42 (physical inventory — count documentation), W48 (IT — IT general controls), W55 (DR — business continuity documentation), W77 (BIR audit — separate from external audit but may share data), W89 (bank reconciliation — primary audit evidence for cash), W90 (tax — tax reconciliation and filing verification), W92 (inventory adjustments — control testing)

### Time Estimate
- Engagement letter and planning: 2 hours (step 1)
- Pre-audit preparation (January): 8 hours for Controller + distributed effort across Finance team (step 2)
- PBC list fulfillment: 20–30 hours total across Finance team (step 3)
- External audit fieldwork (February): 2–3 weeks; Controller and Finance team spend 1–3 hours/day responding to queries (steps 4–5)
- Draft financial statements review: 4–6 hours (step 6)
- Audit adjustments processing: 2–4 hours (step 7)
- Exit meeting and management response: 2 hours (step 8)
- Audit report issuance and filing: 2 hours (step 9)
- Management letter follow-up: ongoing quarterly, ~2 hours/quarter (step 10)
- Total Finance team effort: ~80–120 hours over January–March audit season

### Pain Points / Risks
- **Annual audit season overload**: January–March is simultaneously the year-end close period (W9B), BIR tax filing season, and external audit fieldwork; the Controller and Finance team must manage all three concurrently, creating severe peak workload with high error risk
- **Intercompany complexity across 5 entities**: With 5 legal entities and complex IC transactions (transfer pricing, management fees, inventory transfers), auditors heavily scrutinize intercompany eliminations; any reconciliation discrepancy in W14 delays the consolidated audit
- **PBC deadline pressure**: External auditors' PBC lists have aggressive deadlines (often 1–2 weeks); if the Finance team is still closing the prior year's books (W9B), PBC preparation competes for the same resources, risking late submissions that extend fieldwork
- **Management letter finding recurrence**: If prior year management letter recommendations are not fully implemented, external auditors escalate findings in the current year; unresolved control weaknesses (e.g., segregation of duties gaps in AP) can ultimately lead to a modified audit opinion, damaging credibility with lenders and regulators

### Staffing Implication
- **Controller**: primary audit liaison; adds ~40–60 hours during Jan–March for audit preparation and coordination. This is the Controller's busiest period; other duties deprioritized during fieldwork.
- **Finance Team** (AP Supervisor, AR Accountant, Treasury Analyst, Tax Accountant, Cost Accountant): each adds ~10–20 hours for PBC preparation and query response during fieldwork. Managed through workload planning during Jan–Feb.
- **Internal Audit**: provides coordination support and observes external audit process; adds ~8–10 hours. Absorbed.
- **Store Managers / DC Supervisors**: 1–2 store/DC visits per year for physical observation; minimal time impact. Absorbed.
- **No incremental headcount.** External audit fee budgeted as professional fees in W26 annual budget.

---

## W114. Sustainability & Environmental Compliance Reporting

| Field | Detail |
|---|---|
| **Trigger** | Annual sustainability reporting cycle; quarterly environmental compliance review; DENR reporting deadline; or ad-hoc triggered by environmental incident or regulatory inquiry |
| **Frequency** | Annual sustainability report; quarterly environmental metrics review; monthly waste and emissions tracking |
| **Volume** | 200 stores + 4 DCs + HQ; environmental data collected per location across waste, energy, water, and emissions categories |
| **Owner** | Facilities Manager (data collection); VP Legal & Compliance (regulatory reporting) |
| **Participants** | Facilities Manager, VP Legal & Compliance, Regulatory Officer, Store Managers, DC Managers, Finance Manager, CSR Coordinator |

### Background

BuildRight operates 200 stores and 4 DCs across the Philippine archipelago. Environmental compliance is governed by the Philippine Clean Air Act (RA 8749), Clean Water Act (RA 9275), Ecological Solid Waste Management Act (RA 9003), Toxic Substances and Hazardous and Nuclear Wastes Control Act (RA 6969), and the Philippine Strategy for Sustainable Development. W82 covers hazardous waste disposal tracking and DENR compliance specifically. W111 covers energy and utility consumption management. However, there is no unified workflow for: (a) tracking environmental metrics beyond hazardous waste (solid waste diversion rate, water consumption, carbon emissions), (b) compiling sustainability data into regulatory reports and voluntary disclosures, (c) setting and monitoring environmental reduction targets, and (d) coordinating environmental compliance across 200+ locations. This workflow creates that comprehensive sustainability governance layer.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Monthly environmental data collection**: System aggregates environmental data per location from multiple sources: (a) **Waste**: hazardous waste manifests (W82), general solid waste collection volumes (from waste hauler invoices per W7C), recyclable materials recovered (cardboard bales, plastic, metal — from recycling vendor records); (b) **Energy**: electricity consumption (W111 utility data), diesel consumption (fleet per W52, generators per W47); (c) **Water**: water consumption per location (W111 utility data); (d) **Emissions**: estimated CO₂ from electricity (using DU emission factor) and diesel (using DEF emission factor) — system calculates carbon footprint estimate per location | System / Facilities Manager | VP Legal & Compliance | Automated (aggregation) + 2 hours/month (verification) |
| 2 | **Quarterly environmental metrics review**: Facilities Manager reviews quarterly environmental dashboard: (a) **Solid waste diversion rate**: recycled waste ÷ total waste — target: ≥ 30%, (b) **Energy intensity**: kWh per sqm per month — target: reduce 2% year-over-year, (c) **Water intensity**: cubic meters per sqm per month — target: reduce 2% year-over-year, (d) **Carbon intensity**: tonnes CO₂ per PHP million revenue — target: reduce 3% year-over-year, (e) **Hazardous waste compliance**: 100% of hazardous waste disposed via DENR-accredited transporters with manifest tracking (W82), (f) per-location outliers flagged for investigation and corrective action | Facilities Manager | VP Legal & Compliance | 2 hours/quarter |
| 3 | **Environmental compliance calendar**: Regulatory Officer maintains environmental compliance calendar per location: (a) **DENR hazardous waste generator registration** renewal per location (W82), (b) **DENR quarterly hazardous waste disposal report** per location, (c) **LGU environmental compliance certificate** renewal (for stores with Environmental Compliance Certificate requirement), (d) **Wastewater discharge permit** (for locations with discharge to waterways — paint/chemical areas), (e) **Air emissions permit** (for DCs with backup generators above threshold); system alerts Regulatory Officer 60 days before each deadline; expired permits escalated to VP Legal & Compliance | Regulatory Officer | VP Legal & Compliance | 2 hours/quarter (calendar maintenance) |
| 4 | **Annual environmental reduction targets**: Facilities Manager and VP Legal & Compliance set annual environmental targets aligned with corporate sustainability strategy: (a) carbon emission reduction target (% year-over-year), (b) energy efficiency improvement target (% reduction in kWh/sqm), (c) water consumption reduction target, (d) solid waste diversion rate improvement, (e) hazardous waste volume reduction; targets approved by CEO; integrated into W26 annual budget as operational KPIs | Facilities Manager / VP Legal & Compliance | CEO | Annual (4 hours) |
| 5 | **Annual sustainability report compilation**: CSR Coordinator compiles annual sustainability data for: (a) voluntary sustainability disclosure (if BuildRight pursues GRI or SASB reporting framework), (b) DENR annual environmental performance report (if required), (c) SEC sustainability reporting requirements (SEC Memorandum Circular No. 4, Series of 2019 requires publicly listed companies to submit sustainability reports — BuildRight prepares and submits these reports accordingly), (d) internal stakeholder communication (sustainability section of annual report); Facilities Manager provides environmental metrics; Finance Manager provides utility spend data; VP Legal & Compliance reviews regulatory compliance status | CSR Coordinator / Facilities Manager | VP Legal & Compliance | Annual (20 hours) |
| 6 | **Environmental incident response**: If environmental incident occurs (chemical spill at paint mixing station, hazardous waste container breach, wastewater discharge violation): (a) Store Manager / DC Supervisor initiates immediate containment per W82 emergency procedures; (b) Regulatory Officer notified within 24 hours; (c) Regulatory Officer assesses reporting requirement — incidents exceeding threshold require DENR notification within 24–72 hours per RA 6969; (d) Facilities Manager coordinates remediation; (e) system logs incident with location, date, type, quantity, response actions, and remediation cost; (f) incident included in quarterly metrics review and annual sustainability report | Store Manager / DC Supervisor / Regulatory Officer | VP Legal & Compliance | Per incident |
| 7 | **Vendor environmental compliance**: Buyer evaluates vendor environmental practices for high-risk categories (paint, chemicals, treated lumber, cement): (a) during vendor onboarding (W36), check for environmental compliance certifications (ISO 14001, DENR compliance for Philippine manufacturers); (b) for import vendors: check compliance with applicable environmental standards in country of manufacture; (c) annual review of vendor environmental compliance as part of W44 vendor scorecard; (d) vendors with environmental violations flagged for CAPA per W110 or vendor exit per W44 termination | Buyer / Regulatory Officer | VP Merchandising | Absorbed within W36/W44 |

### System Touchpoints
- Monthly environmental data aggregation from utility bills (W111), waste manifests (W82), fleet records (W52), and generator maintenance records (W47) (W114.1)
- Carbon footprint estimation calculator using DU emission factors for electricity and DEF factors for diesel (W114.1)
- Quarterly environmental dashboard: waste diversion, energy intensity, water intensity, carbon intensity, hazardous waste compliance (W114.2)
- Environmental compliance calendar per location with permit tracking and renewal alerting (W114.3)
- Annual environmental reduction target configuration with year-over-year tracking (W114.4)
- Environmental incident logging with DENR reporting workflow (W114.6)
- Integration with W47 (facility maintenance — generator emissions, HVAC efficiency), W52 (fleet — fuel consumption and emissions), W60 (emergency procurement — environmental incident supplies), W82 (hazardous waste — manifests and DENR compliance), W111 (energy and utility — consumption data), W26 (annual budget — environmental targets as KPIs)

### Time Estimate
- Monthly data aggregation verification: 2 hours/month (step 1)
- Quarterly environmental metrics review: 2 hours/quarter (step 2)
- Environmental compliance calendar maintenance: 2 hours/quarter (step 3)
- Annual target setting: 4 hours/year (step 4)
- Annual sustainability report compilation: 20 hours/year (step 5)
- Environmental incident response: varies per incident (step 6)
- Vendor environmental compliance review: absorbed within W36/W44 (step 7)
- Overall: Facilities Manager ~40 hours/year; Regulatory Officer ~8 hours/year; CSR Coordinator ~20 hours/year

### Pain Points / Risks
- **Data collection consistency across 204 locations**: Environmental data (waste volumes, energy consumption, water usage) is only as reliable as the manual logging at each store; without automated metering and waste weighing, data accuracy varies widely across locations, undermining report credibility
- **Carbon footprint estimation methodology**: Estimated CO₂ using generic emission factors (DU for electricity, DEF for diesel) is an approximation; external auditors or DENR may challenge the methodology, especially if BuildRight claims carbon reduction targets in public sustainability reports
- **DENR reporting deadline cascading**: Multiple DENR reporting obligations (hazardous waste quarterly per W82, environmental compliance certificate renewals, wastewater discharge permits) have staggered deadlines across 204 locations; missing any single deadline can trigger enforcement action for that specific location
- **Voluntary vs. mandatory reporting tension**: SEC sustainability reporting requirements (MC No. 4, 2019) are evolving; if BuildRight prepares voluntary GRI/SASB disclosures, the bar for data completeness and accuracy is higher than DENR's mandatory requirements, requiring additional investment in data collection infrastructure

### Staffing Implication
- **Facilities Manager**: adds ~2 hours/month for data verification + ~2 hours/quarter for metrics review + ~4 hours/year for target setting = ~40 hours/year. Absorbed within existing Facilities Manager role (formalized in W111).
- **Regulatory Officer**: adds ~2 hours/quarter for environmental compliance calendar maintenance. Absorbed within existing Regulatory Officer role (formalized in W54).
- **CSR Coordinator** (within Marketing team): adds ~20 hours/year for annual sustainability report compilation. Absorbed.
- **No incremental headcount.**

---

## W157. E-waste Collection & Circular Economy Operations

| Field | Detail |
|---|---|
| **Trigger** | Customer brings end-of-life products (batteries, old tools, appliances) to store collection points |
| **Frequency** | Ongoing |
| **Volume** | Covers all 200 stores |
| **Owner** | Sustainability Manager |
| **Participants** | Store Staff, Logistics, Accredited Recyclers, DENR |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Collection**: Customer drops off items at designated in-store bins; Store Staff record weight/type in system | Store Staff | Store Manager | Ongoing |
| 2 | **Incentive**: System issues "Green Points" to customer loyalty account (W17) for participating | System | — | Real-time |
| 3 | **Consolidation**: DC delivery trucks backhaul e-waste to the nearest Hub (W4) | Logistics | — | Weekly |
| 4 | **Certified Disposal**: Accredited 3rd-party recycler collects waste from DC; provide Certificate of Treatment | Recycler | Sustainability Mgr | Monthly |
| 5 | **Impact Reporting**: Track total tonnage diverted from landfills for ESG report (W114) | Sustainability Mgr | CMO | Monthly |

### System Touchpoints
- In-store collection bin weight/type logging module integrated with store inventory or sustainability tracking
- Loyalty engine (W17) for automated "Green Points" issuance upon e-waste drop-off
- DC logistics system (W4) for backhaul scheduling and tracking of e-waste from stores to DCs
- Vendor management module (W62) for accredited recycler contract management and Certificate of Treatment tracking
- Sustainability reporting module (W114) for landfill diversion tonnage aggregation and ESG reporting

### Time Estimate
- Per-customer drop-off recording: 2–3 min/event by Store Staff
- DC backhaul coordination: absorbed into existing DC truck routes (W4), no incremental time
- Certified disposal coordination: 1–2 hours/month for Sustainability Manager (recycler scheduling and Certificate of Treatment collection)
- Monthly impact reporting: 1–2 hours/month for Sustainability Manager
- Annual: ~30–40 hours/year total effort for Sustainability Manager

### Pain Points / Risks
- **DENR hazardous waste classification**: E-waste (batteries, electronics) is classified as hazardous waste under RA 6969; collection, transport, and disposal must comply with DENR regulations including use of accredited transporters and TSD facilities per W82, adding regulatory overhead to what appears to be a simple customer-facing program
- **Customer drop-off volume unpredictability**: Without appointment scheduling, e-waste drop-off volumes vary; if a store receives a surge of bulky items (old appliances, large power tools), in-store collection bins may overflow, creating storage and safety issues
- **Green Points fraud risk**: Automated loyalty points issuance for e-waste drop-off could be gamed if Store Staff record fictitious drop-offs to earn points for themselves or accomplices; requires periodic audit of drop-off logs against actual recycler weight receipts
- **Accredited recycler availability**: DENR-accredited e-waste recyclers are limited in the Philippines, particularly for VisMin regions; if the primary recycler's DENR accreditation lapses or capacity is full, collected e-waste may accumulate at DCs without a compliant disposal outlet

---

### Staffing Implication
Store Staff drop-off recording: ~2–3 min/event, absorbed into floor duties. DC backhaul: absorbed into existing truck routes (W4). Sustainability Manager: ~30–40 hours/year for disposal coordination and impact reporting. No incremental headcount.

## W158. Business Continuity Drill & Disaster Recovery Testing

| Field | Detail |
|---|---|
| **Trigger** | Annual BC/DR schedule or major system change |
| **Frequency** | Semi-annual for IT DR; Annual for full BC drill |
| **Volume** | Covers all 5 legal entities and critical sites (HQ, DCs, 200 stores) |
| **Owner** | VP Legal & Compliance |
| **Participants** | IT Infrastructure Team, DC Managers, Store Managers, HR, Finance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Scenario Planning**: Define the drill scenario (e.g., total network outage, major typhoon landfall in Visayas, fire at DC3) | Compliance Officer | VP Legal & Compliance | 4 hours |
| 2 | **IT Disaster Recovery Test**: Execute "failover" to backup data center; verify data integrity and POS transaction synchronization (W55) | IT Manager | CIO | 8-12 hours |
| 3 | **Communication Drill**: Activate emergency notification tree; verify response times from Store Managers and DC Supervisors | HR Manager | CHRO | 2 hours |
| 4 | **Operational Workarounds**: Stores practice manual sales recording (W5G) and manual inventory logging for 4 hours; DCs practice manual load manifest creation | Store Manager / DC Supervisor | COO | 4 hours |
| 5 | **Post-Drill Review**: Document gaps, system performance issues, and communication bottlenecks; update Business Continuity Plan (BCP) | Compliance Officer | VP Legal & Compliance | 1 day |
| 6 | **Board Reporting**: Present DR/BC readiness status and improvement plan to the Board of Directors | VP Legal & Compliance | CEO | Quarterly |

### System Touchpoints
- BC/DR plan document management system with version control and approval workflows
- DR failover execution console (W55) for IT disaster recovery testing
- Emergency notification system (SMS blast, automated call tree) for communication drill activation
- Offline POS procedure documentation (W5G) accessible via store portal
- Post-drill gap analysis and corrective action tracking module
- Board reporting template integrated with W35 management reporting cycle
- Integration with W49 (typhoon response — BC plan activation), W55 (IT DR — failover testing), W5G (offline POS — manual workaround practice), W48 (helpdesk — incident management during drills)

### Time Estimate
- Scenario planning: 4 hours (step 1)
- IT DR test execution: 8–12 hours (step 2), typically conducted over a weekend maintenance window
- Communication drill: 2 hours (step 3)
- Operational workaround practice: 4 hours per participating store/DC (step 4)
- Post-drill review and BCP update: 1 day (step 5)
- Board reporting preparation: 2 hours/quarter (step 6)
- Total per semi-annual drill cycle: ~30–50 hours across IT, HR, Store Ops, and Compliance participants

### Pain Points / Risks
- **Production system risk during DR test**: Even in a controlled test, failing over to the DR environment risks encountering real issues (replication lag, configuration drift) that can extend the test window beyond the planned maintenance period, impacting Monday morning store operations
- **Store Manager drill participation**: With 200 Store Managers asked to practice manual sales recording for 4 hours, drill fatigue and resistance are likely; stores may treat the drill as a paperwork exercise rather than genuine practice, reducing readiness
- **BCP documentation currency**: The BCP must reflect current systems, org chart, and communication channels; if the BCP is not updated after each drill (step 5), it becomes stale and unreliable when an actual disaster strikes
- **Board-level accountability gap**: DR/BC readiness is a board-level governance item, but operational execution depends on IT and Store Ops teams who may deprioritize drills against revenue-generating activities; without executive enforcement, drill quality and frequency tend to erode over time

---

### Staffing Implication
Semi-annual drill cycle requires ~30–50 hours across IT, HR, Store Ops, and Compliance. IT Manager dedicates 8–12 hours per DR test. Compliance Officer spends ~1.5 days per cycle on planning and review. Store Manager participation: 4 hours per drill (manual workaround practice). All absorbed by existing roles. No incremental headcount.

## W167. Store & DC Recycling Program (Circular Economy)

| Field | Detail |
|---|---|
| **Trigger** | Accumulation of secondary packaging (cartons, plastics, broken pallets) |
| **Frequency** | Weekly |
| **Volume** | Covers all 200 stores and 4 DCs; ~5–10 tonnes of recyclable material per store/month |
| **Owner** | DC Supervisor / Store Manager |
| **Participants** | Stock Associates, Logistics Team, DC Supervisor, Recycling Partners, Sustainability Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Store/DC Associates segregate waste: Carton, Stretch Film (Plastic), Wood (Pallets), Scrap Metal | Associates | — | Ongoing |
| 2 | Materials baled (for carton/plastic) or stacked (for pallets) at DC/Store dock | Stock Associate | — | 30 min/day |
| 3 | Logistics collects recyclables from Stores via **Reverse Logistics** trucks returning to DC | Logistics Team | — | Weekly |
| 4 | DC consolidates recyclables; sells to accredited recycling partners | DC Supervisor | Supply Chain Mgr | Monthly |
| 5 | System records "Recycling Revenue" and weight diverted from landfill; feeds into W114 Sustainability Report | DC Supervisor | — | 15 min |

### System Touchpoints
- Waste segregation and baling tracking at store/DC dock level
- Reverse logistics scheduling module integrated with DC truck routing (W4) for backhaul of recyclables
- Recycling partner vendor management (W62) for accredited recycling buyer contracts
- Recycling revenue recording module linked to miscellaneous income GL account
- Weight tracking integration with W114 sustainability reporting for waste diversion rate calculation
- Integration with W4 (DC delivery — reverse logistics truck loading), W62 (vendor contracts — recycling partner agreements), W114 (sustainability — diversion metrics), W82 (hazardous waste — non-hazardous recyclable segregation from hazardous waste streams)

### Time Estimate
- Daily waste segregation and baling: 30 min/day per store/DC (step 2), absorbed into Stock Associate routine
- Weekly reverse logistics pickup: absorbed into existing DC truck routes, no incremental driver time
- Monthly recycling sale coordination: 1–2 hours/month per DC Supervisor
- Revenue and weight recording: 15 min/month per location
- Overall: minimal incremental time; primarily absorbed into existing receiving/dock and sustainability workflows

### Pain Points / Risks
- **Recyclable material contamination**: If non-recyclable waste (food waste, hazardous materials) is mixed with recyclable cardboard/plastic, recycling partners may reject the load or pay lower rates; segregation discipline across 200 stores with varying staff training levels is difficult to maintain
- **Low revenue vs. operational effort**: Recycling revenue from cardboard bales, plastic film, and scrap metal is modest (estimated PHP 5,000–15,000/store/year); the operational effort of segregation, baling, storage, and coordination may exceed the direct financial return, making this a sustainability-driven rather than profit-driven activity
- **Reverse logistics space constraints**: DC delivery trucks must allocate space for recyclable backhaul; if a truck is already at capacity with outbound deliveries, recyclables may accumulate at stores, creating dock clutter and potential fire hazards
- **Recycling partner reliability**: Accredited recycling buyers may have inconsistent pickup schedules or may cease operations; if a partner fails, accumulated recyclables at DCs require alternative disposal, potentially as general waste (undermining diversion rate targets)


---

### Staffing Implication
Daily segregation and baling absorbed into Stock Associate routine (~30 min/day per location). DC Supervisor spends ~1–2 hours/month on recycling sale coordination. Sustainability Manager reviews metrics ~1–2 hours/month. No incremental headcount; sustainability-driven activity absorbed by existing roles.

## W185. Product Liability & Consumer Safety Incident Management

| Field | Detail |
|---|---|
| **Trigger** | Report of property damage, personal injury, or safety hazard related to a sold product |
| **Frequency** | As occurred |
| **Volume** | < 10 incidents/month |
| **Owner** | Legal & Compliance Manager |
| **Participants** | Customer Service Manager, Risk Manager, Store Manager, Vendor (Supplier) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer Service Rep receives report; records incident details, product SKU, batch/lot (if available), and photos in ERP | CS Rep | CS Manager | 30 min |
| 2 | System flags product; if multiple reports occur for same SKU, alerts Merchandising for potential stop-sell | System | Merchandising Mgr | Real-time |
| 3 | Store Manager/Risk Manager conducts physical inspection of incident site or product remains | Risk Manager | Legal Manager | 4 hours |
| 4 | Legal Manager reviews documentation; determines liability and coordinates with insurance (W59) | Legal Manager | CFO | 2 hours |
| 5 | Formal notice sent to Vendor; request for investigation and indemnity | Legal Manager | — | 1 hour |
| 6 | Coordinate with DTI (Dept of Trade and Industry) if mandatory product recall is triggered (W29) | Legal Manager | — | 2 hours |
| 7 | Resolve claim: settlement, replacement, or legal defense | Legal Manager | CFO | Ongoing |
| 8 | Document "Lessons Learned"; feed into Vendor Performance Review (W44) | Risk Manager | — | 1 hour |

### System Touchpoints
- Incident Management Portal with photo/document upload (W185.1)
- Automated alert for "Product Hazard Threshold" (W185.2)
- Integration with SKU Master (Stop-Sell flag) (W185.2)
- Link to Insurance Claims workflow (W59) (W185.4)
- Link to Product Recall (W29) and Vendor Performance (W44) (W185.6, W185.8)

### Time Estimate
- Incident recording and system flag: 30 min (steps 1–2)
- Physical inspection: 4 hours (step 3)
- Legal review and insurance coordination: 2 hours (step 4)
- Vendor notification: 1 hour (step 5)
- DTI coordination (if recall triggered): 2 hours (step 6)
- Claim resolution: ongoing (step 7)
- Lessons learned documentation: 1 hour (step 8)
- Total per incident: ~10–15 hours for minor incidents; major product liability cases can span weeks to months

### Pain Points / Risks
- **Legal liability for defective products**: As the retailer, BuildRight may be held primarily liable under the Consumer Act of the Philippines (RA 7394) even if the defect originated from the vendor/manufacturer; recovering costs from vendors through indemnity claims is a separate, often slower process
- **Product hazard threshold calibration**: The automated alert for multiple reports on the same SKU (step 2) must balance sensitivity (catching real hazards early) vs. specificity (avoiding false alarms that trigger unnecessary stop-sell orders costing revenue); threshold calibration requires ongoing Merchandising and Legal input
- **DTI mandatory recall escalation**: If DTI determines a mandatory recall is warranted, BuildRight must comply across all 200 stores within DTI's specified timeline; coordinating a chain-wide product pull with customer notification is operationally complex and costly
- **Insurance coverage gaps**: Product liability insurance (W59) may have exclusions or deductibles that leave BuildRight under-covered for certain categories (e.g., electrical products, chemicals, power tools); a large claim could exceed policy limits

---

### Staffing Implication
Low volume (< 10 incidents/month). Minor incidents: ~10–15 hours each, absorbed by Legal & Compliance Manager and CS Manager. Major product liability cases: can require significant Legal and executive time over weeks to months. No incremental headcount.

## W207. Store-Level Security Camera (CCTV) Audit & LP Integration

| Field | Detail |
|---|---|
| **Trigger** | Scheduled audit or suspected internal/external theft incident |
| **Frequency** | Weekly audits of high-risk transactions |
| **Volume** | Covers all 200 stores and 4 DCs |
| **Owner** | Loss Prevention (LP) Manager |
| **Participants** | LP Analyst, Store Manager, IT (for system access) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Exception Identification**: System identifies high-risk POS transactions (e.g., voids, high-value returns, employee discounts) via automated exception reports (W37) | System | LP Analyst | Automated |
| 2 | **CCTV Reconciliation**: LP Analyst retrieves CCTV footage synced with POS transaction timestamps; verifies physical action matches system record | LP Analyst | LP Manager | 30 min/event |
| 3 | **Discrepancy Logging**: If "phantom return" or unrecorded sale discovered, log as a "Confirmed Incident" in LP module | LP Analyst | LP Manager | 15 min |
| 4 | **Investigation**: Confront staff or review external footage for identification; coordinate with HR for disciplinary action (W79) | LP Manager | CHRO | 2-4 hours |
| 5 | **System Update**: Write off confirmed theft inventory (W37.6); update shrinkage metrics in P&L (W102) | Finance | LP Manager | 10 min |
| 6 | **Security Hardening**: Adjust camera angles or POS procedures based on audit findings | IT / Store Manager | LP Manager | 1 hour |

### System Touchpoints
- LP exception reporting module (W37) for automated high-risk transaction identification
- CCTV-POS timestamp synchronization and deep-linking system for footage retrieval
- LP case management module for confirmed incident logging, investigation tracking, and resolution
- Inventory write-off module (W37.6) for confirmed theft inventory adjustment
- Shrinkage metrics dashboard (W102/W37.7) for P&L impact tracking
- Integration with W37 (loss prevention — exception reporting and case management), W48 (IT — CCTV system support and camera angle adjustments), W79 (grievance — disciplinary action coordination), W102 (P&L — shrinkage reporting)

### Time Estimate
- Per-event CCTV reconciliation: 30 min/event (step 2)
- Discrepancy logging: 15 min/event (step 3)
- Investigation: 2–4 hours per confirmed incident (step 4)
- System update and write-off: 10 min/confirmed case (step 5)
- Security hardening: 1 hour per audit finding (step 6)
- Weekly audit cycle: LP Analyst reviews ~20–40 flagged transactions/week; total ~10–15 hours/week across all LP staff

### Pain Points / Risks
- **CCTV storage and retrieval limitations**: CCTV footage is typically retained for 30 days online and 90 days archived (per W37 specifications); if an LP Analyst does not review a flagged transaction within the online retention window, retrieval from archive is slower and may require IT intervention, delaying investigation
- **Camera blind spots and coverage gaps**: Older stores or recently remodeled locations may have camera positions that do not cover all POS terminals or receiving dock areas; LP audits may identify theft patterns that cannot be visually confirmed due to coverage gaps
- **Investigation confrontation risk**: When LP Manager confronts staff suspected of theft (step 4), there is a risk of escalation, workplace safety concerns, or legal liability if the investigation is not conducted per Philippine Labor Code due process requirements (cross-reference W79 NTE process)
- **Scale vs. coverage tension**: With 200 stores generating thousands of exception events weekly, LP team can only audit a fraction of flagged transactions; sophisticated theft patterns that stay below exception thresholds may go undetected

---

### Staffing Implication
Weekly audit cycle requires ~10–15 hours/week from LP Analysts (2–3 LPOs recommended per W37). LP Manager adds ~2–4 hours/week for investigation oversight. IT support for camera adjustments is ad-hoc. Absorbed by existing LP and IT roles. No incremental headcount beyond LPO positions already recommended.

## W209. Barangay & Local Community Relationship Management

| Field | Detail |
|---|---|
| **Trigger** | Store opening (W16); annual local permit cycle (W54); or community grievance |
| **Frequency** | Quarterly check-ins; or as needed |
| **Volume** | One relationship per store/DC location (204+ barangays) |
| **Owner** | Store Manager / DC Manager |
| **Participants** | Barangay Captain, LGU Officials, Legal Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Stakeholder Mapping**: Identify key local officials (Barangay Captain, LGU licensing office, local police) | Store Manager | Legal Manager | 2 hours |
| 2 | **Permit Coordination**: Liaise with Barangay for "Barangay Clearance" required for LGU Business Permit renewal (W54) | Store Manager | Regulatory Officer | 4 hours/year |
| 3 | **Local Employment**: Coordinate with Barangay for local hiring requirements/quotas as part of social responsibility and LGU agreements | HR / Store Manager | — | Monthly |
| 4 | **Community Support**: Manage local CSR requests (e.g., school repair donations, neighborhood cleaning) via CSR Program Execution (W135) | Store Manager | CSR Coordinator | 1 hour |
| 5 | **Dispute Resolution**: Address community complaints (e.g., truck noise, parking congestion) via direct dialogue; document resolution in Legal Case Management (W125) | Store Manager | Legal Manager | Varies |
| 6 | **Annual Appreciation**: Conduct "Community Day" or stakeholder briefing on store performance and local impact | Store Manager | — | 4 hours/year |

### System Touchpoints
- Store-level stakeholder/contact database for Barangay officials, LGU licensing office, and local PNP contacts
- LGU permit tracking system (W54) for Barangay Clearance status per location
- HR recruitment module for local hiring coordination with Barangay referrals
- CSR program tracking (W135) for community donation and event management
- Legal case management (W125) for community dispute documentation and resolution tracking
- Integration with W16 (new store opening — initial Barangay relationship building), W54 (LGU permits — Barangay Clearance), W135 (CSR execution — community support activities), W209 (community events calendar)

### Time Estimate
- Initial stakeholder mapping: 2 hours (new store); updated annually in 1 hour
- Barangay clearance coordination: 4 hours/year (absorbed into W54 permit renewal cycle)
- Local hiring coordination: ~1 hour/month (absorbed into HR recruitment)
- Community CSR request management: ~1 hour/week per Store Manager
- Dispute resolution: varies (30 min for minor complaints to days for major disputes)
- Annual Community Day: 4 hours/year planning and execution
- Overall per Store Manager: ~2–4 hours/month on community relations activities

### Pain Points / Risks
- **Political relationship dependency**: Store operations (permit approvals, traffic access, security coordination) depend on maintaining positive relationships with Barangay Captains and LGU officials; political turnover in Philippine Barangay elections (every 3 years) can reset relationships overnight
- **Community complaint escalation**: Persistent complaints (truck noise at 5 AM for DC deliveries, customer parking overflow into residential streets) can escalate to LGU enforcement action or media exposure if not resolved quickly through direct dialogue; Store Managers may lack negotiation training for sensitive community disputes
- **CSR request volume and prioritization**: Schools, barangay halls, and local organizations frequently request donations (building materials, labor, cash); without clear CSR prioritization criteria and budget limits per store, Store Managers face uncomfortable decisions that may offend community stakeholders
- **Consistency across 200 stores**: Without centralized oversight, each Store Manager manages community relationships independently; inconsistent handling of disputes or CSR requests across stores can create reputational risk for the brand

---

### Staffing Implication
~2–4 hours/month per Store Manager on community relations activities, absorbed into existing duties. DC Managers spend ~1–2 hours/month. Legal Manager supports dispute resolution as needed. CSR Coordinator manages Community Day planning (~4 hours/year per store). No incremental headcount.

## W216. BIR CAS (Computerized Accounting System) Compliance Audit

| Field | Detail |
|---|---|
| **Trigger** | Periodic compliance review; or BIR post-evaluation/inspection of the ERP system |
| **Frequency** | Annual internal review; or as scheduled by BIR |
| **Volume** | Covers all 5 legal entities and centralized accounting |
| **Owner** | VP Legal & Compliance / CIO |
| **Participants** | Tax Manager, IT Manager, External Audit, BIR Officers |

### Background

Philippine regulations require companies using a Computerized Accounting System (CAS) to maintain a Permit to Use (PTU) and adhere to strict audit trail, reporting, and e-invoicing standards.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **System Documentation Update**: Maintain up-to-date system architecture, data flow diagrams, and functional descriptions for BIR submission | IT Manager | CIO | 4 hours |
| 2 | **Audit Trail Verification**: Verify that all transactions (GL, AP, AR, Inventory) have immutable audit trails (who, when, what, previous value) | IT Manager | Internal Audit | 2 hours |
| 3 | **Standard Report Generation**: Generate and validate "Books of Accounts" in BIR-required formats (General Journal, Sales Journal, Purchase Journal, etc.) | Tax Manager | Controller | 4 hours |
| 4 | **E-Invoicing Compliance**: Verify that system-generated Invoices and Official Receipts (OR) comply with BIR serial numbering and mandatory field requirements | Tax Manager | VP Compliance | 2 hours |
| 5 | **CAS Permit Review**: Verify that any significant system changes (W132) have been reported to the BIR as "System Enhancements" per regulation | VP Compliance | — | 1 hour |
| 6 | **Mock Inspection**: Conduct mock BIR walk-through: demonstrate system navigation, report generation, and data archival for BIR officers | Tax Manager | CIO | 1 day |
| 7 | **Archival & Retention**: Verify 7-year data retention and accessibility of archived accounting data (W15.3) | IT Manager | — | 1 hour |

### System Touchpoints
- BIR-compliant reporting module (Books of Accounts)
- Immutable audit trail logs
- Sequential and controlled serial numbering for invoices/receipts
- Data retention and archival system (IT infrastructure)

### Time Estimate
- System documentation update: 4 hours (step 1)
- Audit trail verification: 2 hours (step 2)
- Books of Accounts generation and validation: 4 hours (step 3)
- E-Invoicing compliance verification: 2 hours (step 4)
- CAS permit review (system change reporting): 1 hour (step 5)
- Mock inspection preparation and execution: 1 day (step 6)
- Archival and retention verification: 1 hour (step 7)
- Total annual internal review: ~2–3 days across IT, Tax, and Compliance participants

### Pain Points / Risks
- **BIR audit trail immutability requirement**: BIR requires that all accounting system audit trails be immutable (no editing or deletion of transaction records); if any system process allows modification of posted entries (even with approval), the CAS permit is at risk of revocation; IT must ensure database-level controls prevent unauthorized changes
- **Books of Accounts format compliance**: BIR-prescribed formats for the General Journal, Sales Journal, Purchase Journal, and other books of accounts are specific and rigid; if the ERP's report module produces slightly different column layouts or summaries, BIR may issue a finding requiring remediation and potential permit re-evaluation
- **System change notification gap**: Under BIR regulations, any "material" system change must be reported to BIR as a System Enhancement; the definition of "material" is subjective; if IT deploys a change that BIR later determines should have been reported (e.g., a new module, modified invoice layout), BuildRight faces potential CAS permit suspension
- **7-year data accessibility**: BIR can request accounting data from up to 7 years prior; ensuring that archived data from older ERP versions or system migrations remains accessible and in BIR-compliant format is an ongoing infrastructure challenge, especially after major system upgrades


---

### Staffing Implication
Annual review: ~2–3 days across IT Manager (~8 hours), Tax Manager (~6 hours), and VP Compliance (~4 hours). Ad-hoc BIR inspections may require an additional 1–2 days. Absorbed by existing roles. No incremental headcount.

## W271. Data Subject Access & Deletion Requests (DPA Compliance)

| Field | Detail |
|---|---|
| **Trigger** | Customer or employee formally requests access to or deletion of their personal data. |
| **Frequency** | Low (few per month) |
| **Volume** | 1 per request |
| **Owner** | Data Protection Officer (DPO) |
| **Participants** | Customer Service, IT Data Custodians, Legal |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer submits a formal DSR (Data Subject Request) via portal or email. | Customer Service Rep | Data Protection Officer (DPO) | 15 min |
| 2 | DPO verifies the identity of the requester using government-issued ID or verified email/loyalty account. | Data Protection Officer (DPO) | Legal Counsel | 1 day |
| 3 | DPO routes the request to IT for data extraction or anonymization; logs request in DSAR tracker with deadline. | Data Protection Officer (DPO) | IT Admin | 30 min |
| 4 | IT executes the right to be forgotten (anonymizing PII in ERP/CRM while keeping transactional data for BIR compliance). | IT Admin | Data Protection Officer (DPO) | 1–3 days |
| 5 | DPO formally replies to the customer with a certificate of compliance within 30 days per RA 10173. | Data Protection Officer (DPO) | Legal Counsel | 1 day |

### System Touchpoints
- CRM (Ticket Logging) — DSR intake and status tracking
- Master Data (Anonymization utilities) — PII masking and deletion tooling
- Data Lake (Extraction) — data subject record retrieval across systems
- DSAR Tracker — centralized request log with 30-day countdown and escalation alerts
- Audit Trail — immutable log of all data access and erasure actions for NPC compliance

### Pain Points / Risks
- **NPC compliance deadline risk**: Failure to respond to DSRs within the 30-day RA 10173 mandate exposes BuildRight to NPC enforcement action, including fines of PHP 500K–5M per violation and potential criminal liability for the DPO
- **Relational data integrity on erasure**: Anonymizing PII in ERP/CRM while preserving transactional records for BIR's 7-year retention requirement risks breaking foreign key relationships; if the anonymization utility is not carefully designed, cascading data integrity errors can corrupt financial reporting
- **Identity verification challenges**: Verifying the identity of a data subject requesting access or erasure (especially for non-registered customers or former employees) is prone to social engineering; granting access to the wrong person is itself a data privacy breach
- **Bulk request handling**: If BuildRight's data practices receive media scrutiny (e.g., following a breach per W53), a surge in DSRs could overwhelm the DPO's capacity, creating a backlog that pushes response times beyond the 30-day NPC deadline

### Staffing Implication
Low volume (~5–15 DSRs/year). Each DSR requires 2–5 days of elapsed time but only ~4–8 hours of active DPO effort. IT Admin adds ~2–4 hours per erasure request. Absorbed by existing DPO and IT roles. No incremental headcount.

### Time Estimate
- Per DSR: 2–5 days lead time (identity verification: 1 day, IT data extraction or anonymization: 1–3 days, DPO review and response: 1 day)
- DSRs requiring erasure with complex relational data: up to 7–10 days
- Quarterly DSAR metrics reporting: 2 hours/quarter
- Annual: at ~5–15 DSRs/year, total effort is ~20–50 hours/year for DPO

## W331. DTI Sales Promotion Permit Application & Compliance

| Field | Detail |
|---|---|
| **Trigger** | Marketing team finalizes mechanics for a promotional campaign (W83, W13) |
| **Frequency** | ~20–30 times per year |
| **Volume** | Covers all major sales events, raffles, and "Buy 1 Get 1" promos |
| **Owner** | Regulatory Officer |
| **Participants** | Marketing Campaign Manager, DTI Representative, Finance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Promo Review**: Marketing submits promo mechanics to Regulatory Officer 30-45 days before launch | Marketing Manager | CMO | 30 min |
| 2 | **DTI Filing**: Regulatory Officer prepares and files permit application via DTI portal | Regulatory Officer | VP Legal & Compliance | 2 hours |
| 3 | **Payment & Tracking**: Finance pays DTI processing fee; Regulatory Officer tracks permit status | Finance / Regulatory Officer | Controller | 1 day |
| 4 | **Permit Issuance**: DTI approves and issues Permit Number; Regulatory Officer updates promo record | Regulatory Officer | VP Legal & Compliance | 5–15 days lead time |
| 5 | **Marketing Integration**: Marketing includes DTI Permit Number on all advertising materials | Marketing Manager | CMO | Ongoing |

### System Touchpoints
- Campaign Master (W300) — Attach DTI Permit Number to promo rule
- Document Management (W255) — Store approved DTI Permit
- AP/Finance (W7C) — DTI fee payment tracking

### Pain Points / Risks
- **DTI Compliance Fine**: Running a promo without a DTI permit or omitting the permit number from ads risks fines and suspension of future promos per RA 7394.
- **Approval Delay**: DTI approval takes up to 15 days; late filing delays campaign launch (W83).

### Staffing Implication
Managed by the Regulatory Officer (~24 filings/year x 3 hours = 72 hours/year).

### Time Estimate
2–3 hours effort per promo; 15 days elapsed lead time.

---

## W427. DTI Sales Promotion Permit Monitoring & In-Store Compliance

| Field | Detail |
|---|---|
| **Trigger** | Launch of a DTI-permitted sales promotion (per W331) |
| **Frequency** | Weekly during the promo period |
| **Volume** | ~20–30 major promos per year across 200 stores |
| **Owner** | Regulatory Officer |
| **Participants** | Store Manager, Marketing Audit Team, Loss Prevention, Pricing Analyst |

### Background

While `W331` handles the legal application for DTI permits, this workflow ensures operational compliance. The Department of Trade and Industry (DTI) conducts "spot audits" in the Philippines. If a store displays a promo sign after the permit expiry, or if the POS price does not match the DTI-approved discount, the company faces significant fines and "cease and desist" orders for future promotions.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Compliance Checklist**: Regulatory Officer generates a "DTI Compliance Checklist" for each active promo: (a) DTI Permit Number, (b) Approved Mechanics, (c) Start/End Dates, (d) Covered SKUs and Discount Levels | Regulatory Officer | — | 30 min |
| 2 | **Digital Ad Verification**: Marketing Audit Team reviews current social media ads and website banners; verifies DTI Permit Number is visible and mechanics match the approved filing | Marketing Audit | CMO | 1 hour |
| 3 | **POS Price Audit**: Pricing Analyst runs a system query to compare "Live POS Price" vs. "DTI-Approved Promo Price" for a sample of 20 SKUs; flags any discrepancies | Pricing Analyst | — | 30 min |
| 4 | **Store Spot Check**: Store Manager (or LPO during store visit) conducts a physical walk-through: (a) verify DTI Permit Number is displayed on all shelf talkers; (b) verify no "Expired" promo signage remains on the floor; (c) verify "Terms & Conditions" are available at the CS desk | Store Manager / LPO | Regional Mgr | 30 min |
| 5 | **Exception Correction**: Any discrepancy (e.g., missing permit number, wrong price) must be corrected within 2 hours; Store Manager logs the correction in the Compliance Portal | Store Manager | — | 2 hours |
| 6 | **Audit Trail Archive**: All weekly compliance checks and corrections are archived for use during DTI spot audits or annual compliance reviews | Regulatory Officer | — | 15 min |

### System Touchpoints

- Compliance Portal: centralized dashboard for tracking DTI promo status and store-level compliance logs (W427.5)
- POS-to-DTI Price Validation: system utility that compares ERP promo rules against DTI-approved price matrices (W427.3)
- Integration with W331 (DTI Application), W262 (Promotional Setup), and W69 (Price Audit)

### Pain Points / Risks

- **Signage Hangover**: Failing to remove "Buy 1 Get 1" signs on the day after the promo ends is the most common DTI violation; "Spot auditors" often visit on the first day after a major holiday sale
- **Price Sync Lag**: If the POS price update (W262) fails for a subset of stores, customers may be overcharged, leading to valid DTI complaints and fines
- **Incomplete Mechanics**: Omitting the "Per DTI Permit No. XXX" text on a single Facebook post can trigger a DTI investigation into the entire campaign

### Staffing Implication

Weekly monitoring requires ~2 hours/week from the Regulatory Officer and ~30 min/week per Store Manager during active promos. Effort is absorbed into existing compliance and store routines.

### Time Estimate

**Total**: Checklist generation — 30 min; Ad verification — 1 hour; POS audit — 30 min; Store spot check — 30 min; **Total: ~3 hours/week during promo periods**


---

## W433. DENR Self-Monitoring (SMR) & Compliance (CMR) Reporting

| Field | Detail |
|---|---|
| **Trigger** | Quarterly (SMR) or Semi-Annual (CMR) reporting calendar |
| **Frequency** | Quarterly (SMR); Semi-Annual (CMR) |
| **Volume** | 200 Stores + 4 DCs |
| **Owner** | Regulatory Officer |
| **Participants** | Store Managers, DC Managers, Pollution Control Officer (PCO), DENR-EMB |

### Background

Philippine environmental laws require establishments with Environmental Compliance Certificates (ECC) or those generating hazardous waste to submit periodic reports to the **Department of Environment and Natural Resources (DENR) - Environmental Management Bureau (EMB)**. The **Self-Monitoring Report (SMR)** is submitted quarterly, while the **Compliance Monitoring Report (CMR)** is submitted semi-annually.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Data Collection**: Collect quarterly data per location: hazardous waste volume (W82), water consumption, air emissions (if using large generators), and CSR activities | Store/DC Manager | PCO | 1 week |
| 2 | **Report Preparation**: PCO consolidates data into the SMR/CMR templates; verifies against ECC conditions and hazardous waste manifests | Pollution Control Officer | Regulatory Officer | 2 days |
| 3 | **Review & Approval**: Regulatory Officer reviews the consolidated report for accuracy and legal compliance | Regulatory Officer | VP Compliance | 1 day |
| 4 | **Online Filing**: PCO uploads the reports via the DENR-EMB Online Systems (SMR Online / IIS) | Pollution Control Officer | — | 4 hours |
| 5 | **Proof of Submission**: System archives the "Filing Confirmation" and "Reference Number" for audit purposes | System | Regulatory Officer | Automated |

### System Touchpoints
- Environmental Data Warehouse (linkage to Hazmat manifests, Water bills, Fuel logs)
- Compliance Calendar (W114) with automated SMR/CMR triggers
- Document Management System (W255) for archiving stamped reports

### Pain Points / Risks
- **Late Filing**: DENR-EMB imposes significant fines for late submissions; persistent failure to file can lead to ECC suspension and store closure.
- **Data Gaps**: Incomplete hazardous waste manifests or missing utility data from remote stores delaying the consolidated report.

---

## W437. Regulatory Branch De-registration & Permit Cancellation

| Field | Detail |
|---|---|
| **Trigger** | Formal decision to close or relocate a store (W45) |
| **Frequency** | Ad-hoc (Rare) |
| **Volume** | ~1–2 branches per year |
| **Owner** | Regulatory Officer |
| **Participants** | VP Legal, Finance (Tax), BIR, LGU, DTI, SSS, PhilHealth, Pag-IBIG |

### Background

Closing a store in the Philippines is more complex than opening one. Failure to formally "de-register" a branch leads to the accumulation of "open cases" with the BIR and continuing tax/permit liabilities at the LGU level. This process can take 12–24 months to fully complete.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **BIR Notification**: File "Notice of Closure" with the RDO having jurisdiction over the store within 10 days of closure | Tax Manager | VP Legal | 1 day |
| 2 | **LGU Cancellation**: Surrender the Business Permit and Mayor's Permit to the BPLO; settle any outstanding Local Business Tax (LBT) | Regulatory Officer | Store Manager | 1 week |
| 3 | **Inventory Clearance**: For BIR purposes, declare the final inventory disposition (sale, transfer, or write-off) and settle any associated VAT | Finance | Controller | 3 days |
| 4 | **CAS De-registration**: Formally request the BIR to cancel the "Permit to Use" for POS terminals and the Computerized Accounting System (CAS) at that location | IT Manager | CIO | 1 week |
| 5 | **Statutory Updates**: Notify SSS, PhilHealth, and Pag-IBIG of the branch closure to stop billing for that specific employer branch code (if applicable) | HR Manager | — | 1 week |
| 6 | **Document Archival**: Maintain all "Certificate of No Outstanding Liability" and "Closure Certs" for 10 years per BIR rules | System | Regulatory Officer | Continuous |

### System Touchpoints
- Fixed Asset Register (de-linkage of assets from the closed branch)
- BIR CAS Compliance Module (Permit cancellation tracking)
- Legal Matter Tracker (W125) for monitoring the 24-month closure lifecycle

### Pain Points / Risks
- **BIR Open Cases**: If POS permits aren't formally canceled, the system continues to expect monthly reports, leading to automated "Open Case" penalties.
- **LBT Over-assessment**: LGUs often assess a "closure tax" based on the prior year's gross sales; requires negotiation and proof of actual year-to-date revenue.

---

## W444. Community Solicitation & Donation Processing

| Field | Detail |
|---|---|
| **Trigger** | Receipt of a solicitation letter or donation request from a local Barangay, school, or organization |
| **Frequency** | Weekly; ~5–10 requests per store/month |
| **Volume** | High volume of low-value requests (PHP 2,000–20,000) |
| **Owner** | Store Manager |
| **Participants** | Store Manager, Regional Manager, CSR Lead, Marketing (HQ) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Intake**: CSR receives solicitation letter; logs request in the "CSR Portal"; scans the letter and ID of requester | CSR | Store Manager | 10 min |
| 2 | **Validation**: Store Manager verifies the legitimacy of the requesting organization (e.g., Barangay ID, School Principal signature) | Store Manager | — | 1 hour |
| 3 | **Approval (Tiered)**: (a) Store Manager approves if < PHP 5K (Product only); (b) Regional Manager approves if PHP 5K–20K; (c) HQ Marketing approves if > PHP 20K | Approver | — | 1–3 days |
| 4 | **Item Selection**: Store Manager selects "Donation eligible" SKUs (e.g., damaged-box paint, slow-moving items) | Store Manager | — | 15 min |
| 5 | **Issue Voucher**: System generates a "Donation Voucher"; requester signs "Deed of Donation" / Acknowledgment Receipt | CSR | — | 10 min |
| 6 | **Inventory Release**: Stock Associate releases items at the loading dock; system posts inventory adjustment (Reason Code: DONATION) | Stock Associate | Store Manager | 10 min |
| 7 | **Tax Documentation**: Finance extracts monthly donation log for BIR tax-deductible expense filing | Finance (Tax) | — | 1 hour/month |

### System Touchpoints
- CSR Portal for solicitation tracking and document attachment
- Approval Workflow with tiered limits
- Inventory Adjustment module with specific "Donation" reason codes and GL mapping

### Pain Points / Risks
- Loss Prevention: Unauthorized "donations" to personal contacts by store staff.
- Disorganized tracking: Losing solicitation letters or failing to get acknowledgment receipts, leading to BIR audit issues.
- Community friction: Denying requests from powerful local figures.

### Staffing Implication
Absorbed by Store Manager and CSR.

---

## W446. Temporary LGU Permits for Outdoor Sales & Events

| Field | Detail |
|---|---|
| **Trigger** | Plan for an outdoor parking lot sale, "Bagsakan" clearance event, or seasonal tent caravan |
| **Frequency** | Quarterly or as per Marketing Calendar |
| **Volume** | ~2–4 events per store per year |
| **Owner** | Store Manager |
| **Participants** | Regulatory Officer, Marketing, BFP (Fire Dept), LGU |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Event Application**: Store submits "Special Event Permit" request to the LGU Business Permits Office (BPLO) | Regulatory Officer | Store Manager | 2 hours |
| 2 | **Fire Safety Inspection**: Bureau of Fire Protection (BFP) inspects temporary structures (tents, kiosks) and electrical wiring | BFP / Store Mgr | — | 2 hours |
| 3 | **Signage Permit**: Apply for temporary outdoor banner and billboard permits with the City Engineer's Office | Regulatory Officer | — | 1 day |
| 4 | **Fee Payment**: Finance processes payment for temporary permits/inspection fees | Finance | — | 1 hour |
| 5 | **Permit Display**: Approved temporary permits posted prominently at the event site | Store Manager | — | 5 min |
| 6 | **Event Closure**: Dismantle temporary structures; clear site; notify LGU of event completion | Store Manager | — | 1 day |

### System Touchpoints
- Compliance Calendar (W54) to track temporary permit expiry
- AP module for government fee payments (W7)

### Pain Points / Risks
- Bureaucratic delays: Tent sales starting before permits are issued, leading to fines or shutdown.
- Safety: Storms or typhoons damaging temporary structures (requires W49 Business Continuity integration).

### Staffing Implication
Absorbed by Store Manager and Regulatory Officer.

---

## W468. DTI Price Freeze / Emergency Price Control Implementation (RA 7581)

| Field | Detail |
|---|---|
| **Trigger** | LGU or national declaration of a state of calamity; or DTI issuance of a price freeze order on prime commodities under RA 7581 (Price Act) |
| **Frequency** | ~5–10 events/year requiring price freeze implementation across affected regions (Philippines averages ~20 typhoons/year; not all result in calamity declarations) |
| **Volume** | Variable — from 5–10 stores (localized flooding) to 60+ stores (major typhoon affecting an entire region); typically 100–500 SKUs affected per event (prime commodities only) |
| **Owner** | VP Merchandising (pricing execution); Legal & Compliance — Regulatory Officer (compliance monitoring) |
| **Participants** | VP Merchandising, Pricing Analyst, Regulatory Officer, Store Manager, IT, Ecommerce Team, Marketing |

### Background

Under the Philippine Price Act (RA 7581, as amended by RA 10623), the President, upon recommendation of the DTI Secretary, may impose a price ceiling — or prices shall be automatically frozen at prevailing levels — on "prime commodities" in areas declared under a state of calamity. BuildRight Depot sells several items classified as prime commodities under DTI Administrative Orders: **cement, plywood, galvanized iron (GI) sheets, hollow blocks, nails, and corrugated roofing**. Price freeze violations carry penalties of PHP 5,000–2,000,000 per offense and/or imprisonment of 5–15 years, plus revocation of business permit.

With ~20 typhoons/year and 200 stores across multiple regions, price freeze events are a **predictable, recurring compliance obligation** — not a rare emergency. Multiple existing workflows reference the *risk* of DTI complaints (W13 — promo pricing, W69 — price compliance, W75 — layaway forfeiture, W181 — shelf label errors, W262 — promotional setup), but none cover the end-to-end lifecycle of government-mandated price control implementation.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Trigger detection**: Regulatory Officer monitors (a) NDRRMC and LGU calamity declarations, (b) DTI price freeze issuances via DTI website and official gazette, (c) PAGASA severe weather bulletins that may lead to calamity declarations; when a calamity declaration is issued covering any BuildRight location, Regulatory Officer immediately alerts VP Merchandising and Pricing Analyst | Regulatory Officer | Legal Head | 15 min/event |
| 2 | **Affected location identification**: Regulatory Officer cross-references the calamity-declared areas (by city/municipality) against BuildRight's location master (W254); system identifies all stores, DCs, and facilities within declared areas using PSGC code matching per W310; generates affected location list with address and operating status | Regulatory Officer / System | Legal Head | 30 min/event |
| 3 | **Affected SKU identification**: Pricing Analyst identifies all active SKUs classified as prime commodities under DTI regulations: (a) cement and concrete products, (b) plywood and lumber products, (c) GI sheets and corrugated roofing, (d) nails, screws, and hardware fasteners, (e) hollow blocks and masonry, (f) other items per DTI specific issuance (varies per event); system flags these SKUs with "Price Freeze – Affected" status | Pricing Analyst / System | VP Merchandising | 1 hour/event |
| 4 | **Baseline price determination**: For each affected SKU at each affected location, system captures the "prevailing price" — defined by DTI as the average price at which the commodity was sold in the area during the 15-day period immediately preceding the calamity declaration; system calculates prevailing price per SKU per affected store from POS transaction history (W5B); if a location has insufficient transaction history (< 5 transactions in 15 days), uses the SRP from the pricing master (W289) | System | Pricing Analyst | Automated (30 min validation) |
| 5 | **Price freeze activation**: Pricing Analyst executes price freeze in system — (a) system locks affected SKUs at prevailing prices for affected locations; (b) POS price file updated with frozen prices (pushed immediately, not on hourly schedule); (c) ecommerce platform prices updated for affected store catchment areas (BOPIS and delivery); (d) marketplace listings (Lazada/Shopee per W180) updated with frozen prices for affected delivery zones; (e) promotional pricing on affected SKUs at affected locations is **suspended** (promo price may be lower than prevailing price — system applies the lower of frozen price or promo price per customer-friendly rule) | Pricing Analyst | VP Merchandising | 1–2 hours/event |
| 6 | **Store notification**: System sends urgent notification to all affected Store Managers: (a) list of price-frozen SKUs with frozen prices, (b) effective date/time of price freeze, (c) instruction to reprint shelf labels (W181) immediately for all affected SKUs, (d) instruction that manual price overrides (W5B.4a) are **blocked** for frozen SKUs — system enforces at POS level, (e) reminder of penalties for violations | System / VP Merchandising | Store Ops Director | 30 min |
| 7 | **Shelf label reprinting**: Stock Associates at affected stores reprint and replace shelf labels for all price-frozen SKUs; frozen price labels include "DTI PRICE FREEZE" annotation as visual compliance indicator; Department Supervisors verify label accuracy | Stock Associate / Dept. Supervisor | Store Manager | 2–4 hours/store |
| 8 | **Ongoing compliance monitoring**: (a) system blocks any price change requests (W40) for frozen SKUs at affected locations — Pricing Analyst cannot override without Regulatory Officer approval; (b) system blocks promotional pricing (W13) from applying to frozen SKUs if promo price exceeds frozen price; (c) POS enforces frozen price at scan — even if central price file is erroneous, POS local cache reflects frozen price; (d) daily: system generates compliance report — all transactions on frozen SKUs at affected locations reviewed for price accuracy | System / Pricing Analyst | VP Merchandising | Automated + 30 min/day review |
| 9 | **DTI compliance documentation**: Regulatory Officer maintains price freeze compliance file per event: (a) copy of calamity declaration, (b) DTI price freeze order (if separate issuance), (c) prevailing price computation with supporting POS transaction data, (d) proof of shelf label update (compliance photos from Store Manager), (e) daily compliance reports, (f) list of any exceptions or incidents with resolution documentation; file retained for 5 years per BIR retention standards | Regulatory Officer | Legal Head | 1–2 hours/event |
| 10 | **Price freeze lift**: When the calamity declaration is lifted or expires (typically 60 days per RA 7581, unless extended), Regulatory Officer confirms with DTI; Pricing Analyst deactivates price freeze in system — (a) frozen SKUs revert to current pricing master prices (W289); (b) suspended promotions on affected SKUs are re-evaluated — expired promos are not reactivated; active promos resume automatically; (c) Store Managers instructed to reprint shelf labels with current prices; (d) ecommerce and marketplace prices revert to current; (e) system generates final compliance summary report for the event | Regulatory Officer / Pricing Analyst | VP Merchandising | 1–2 hours/event |
| 11 | **Post-event compliance review**: Within 2 weeks of price freeze lift, VP Merchandising and Regulatory Officer review: (a) any price violations during freeze period (from daily compliance reports), (b) margin impact of frozen prices vs. current cost (if WAC increased during freeze, margin was compressed), (c) margin recovery post-freeze, (d) process improvements for next event | VP Merchandising / Regulatory Officer | Legal Head | 1 hour/event |
| 12 | **Annual**: Regulatory Officer includes price freeze compliance history in annual regulatory compliance report (W437); tracks number of events, stores affected, SKUs affected, violations (if any), and DTI interactions | Regulatory Officer | Legal Head | Absorbed into annual reporting |

### System Touchpoints
- Location master (W254) cross-referenced against calamity-declared areas (PSGC code matching per W310) (W468.2)
- POS transaction history used to calculate 15-day prevailing price per SKU per store (W5B data) (W468.4)
- Pricing master (W289) frozen for affected SKU–location combinations with "Price Freeze" override status (W468.5)
- POS price file push accelerated from hourly to immediate for price freeze activation (W468.5b)
- Ecommerce platform price sync (ECOM-002) updated for affected delivery zones (W468.5c)
- Marketplace integration (W180) updated for affected listings (W468.5d)
- Shelf label printing (W181) triggered for affected SKUs (W468.7)
- POS price override block enforced at terminal level for frozen SKUs (W468.8c)
- Daily compliance report generation — all transactions on frozen SKUs reviewed for price accuracy (W468.8d)
- Integration with W40 (regular price changes — blocked for frozen SKUs), W13 (promotions — suspended/modified), W49 (natural disaster BC — price freeze often coincides with disaster response), W428 (community disaster relief — relief allocation pricing separate from freeze)

### Pain Points / Risks
- **Prevailing price computation complexity**: DTI's definition of "prevailing price" as the average price over 15 days preceding the declaration can produce unexpected results if the period includes promotional pricing, clearance events, or quantity break pricing; system must accurately compute the weighted average across all transaction types, and Pricing Analyst must validate the output before activation
- **Multi-LGU simultaneous freezes**: A single typhoon may trigger calamity declarations across 20+ LGUs on different dates; each declaration may cover a different subset of BuildRight stores, and the "prevailing price" computation window differs per declaration date; managing overlapping freeze periods across store clusters requires precise system tracking
- **Ecommerce and marketplace price segregation**: Price freezes apply to physical locations, but ecommerce delivery zones span multiple LGUs; if a customer in a calamity-declared city orders online with delivery from a non-declared DC, the price freeze technically applies based on the customer's delivery address, not the DC location — requiring address-based price determination in the ecommerce platform
- **Margin compression during extended freezes**: If the price freeze extends beyond 30 days (maximum 60 days per RA 7581), and BuildRight's replacement cost increases during that period (e.g., import price increases for cement or GI sheets), BuildRight sells at frozen prices while incurring higher costs; no compensation mechanism exists under Philippine law for this margin loss
- **Shelf label compliance lag**: Even with immediate system activation, physical shelf label replacement at 50+ affected stores takes 2–4 hours; during this window, the shelf label shows one price and the POS charges the frozen price — creating customer confusion and potential DTI complaints

### Staffing Implication
- **Regulatory Officer**: Absorbs trigger monitoring and compliance documentation duties (~2–4 hours/event across 5–10 events/year = ~20–40 hours/year). This is a core function of the Regulatory Officer role.
- **Pricing Analyst**: Absorbs SKU identification, prevailing price computation, and system activation (~3–5 hours/event across 5–10 events/year = ~25–50 hours/year). Within existing capacity.
- **Store Manager / Stock Associates**: Shelf label reprinting is absorbed into existing duties (2–4 hours/store/event). During major events, this may temporarily compete with W49 typhoon preparation activities.

---

## W469. Customer Complaint DTI Escalation & Consumer Adjudication Management

| Field | Detail |
|---|---|
| **Trigger** | DTI notification of consumer complaint filed against BuildRight Depot (formal letter, email, or DTI portal notification) |
| **Frequency** | ~15–25 DTI complaints/year (estimated: ~1–2 per month, primarily from Metro Manila and urban Visayas stores with higher consumer awareness) |
| **Volume** | Typically 1 case at a time; occasionally 2–3 concurrent cases |
| **Owner** | Legal & Compliance — Regulatory Officer |
| **Participants** | Regulatory Officer, Legal Head, Store Manager, Department Supervisor, Cashier, VP Merchandising, Finance, Marketing |

### Background

Under the Consumer Act of the Philippines (RA 7394), consumers who are unable to resolve complaints directly with a business may file a formal complaint with the DTI. DTI mediates consumer complaints through its Regional/Provincial Offices and, if mediation fails, through formal adjudication. Multiple existing workflows identify the *risk* of DTI escalation as a pain point: W13 (promotional pricing errors), W69 (price tag/shelf label mismatches), W75 (layaway forfeiture disputes), W181 (shelf label printing errors), and W262 (promotional setup compliance). However, W41 (Customer Complaint Resolution) covers internal complaint handling only and stops at internal resolution — it does not cover the DTI mediation and adjudication process once a customer escalates externally.

DTI consumer complaints are distinct from other legal matters (W125) in that they follow a specific regulatory process with defined timelines, mandatory mediation, and adjudication procedures governed by DTI Department Administrative Orders.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Notification receipt**: Regulatory Officer receives DTI complaint notification — (a) formal letter from DTI Regional/Provincial Office addressed to BuildRight Depot, Inc.; (b) complaint includes: complainant name, transaction details (store, date, POS transaction number if available), nature of complaint, supporting documents provided by complainant (receipts, photos); (c) DTI sets a response deadline (typically 5–7 working days from receipt) | Regulatory Officer | Legal Head | 30 min/case |
| 2 | **Case logging and triage**: Regulatory Officer logs case in compliance case management system: (a) case number, complainant, store location, complaint category (pricing error, defective product, misleading advertising, refusal of return/refund, warranty non-compliance, layaway forfeiture dispute, other Consumer Act violation), DTI office handling, response deadline; (b) assigns case severity: **High** (systemic pricing error affecting multiple customers, product safety issue, potential media exposure), **Medium** (individual transaction dispute with moderate value), **Low** (minor complaint with easy resolution path) | Regulatory Officer | Legal Head | 15 min/case |
| 3 | **Internal investigation**: Regulatory Officer coordinates with Store Manager and relevant department to gather evidence: (a) POS transaction details from system (transaction number, items, prices, discounts applied, cashier ID, timestamp); (b) CCTV footage from transaction time (via W71 security infrastructure — ±5 minutes around transaction); (c) shelf label / price tag status at time of incident (from price compliance audit log W69, or photo evidence from Store Manager); (d) promotional pricing setup records (W262) if complaint involves promo pricing; (e) employee statements (Cashier, Department Supervisor, Store Manager); (f) system logs showing price file sync status at time of incident; (g) any prior internal complaint record (W41) for same customer or same issue at same store | Regulatory Officer / Store Manager | Legal Head | 2–4 hours/case |
| 4 | **Root cause determination**: Regulatory Officer and relevant department determine root cause: (a) **System error** — price file sync failure, incorrect promo pricing push, barcode mismatch; (b) **Human error** — cashier incorrect override, Stock Associate placed wrong shelf label; (c) **Process failure** — promo setup brief not followed, price change not activated on time; (d) **Policy gap** — return/refund policy too restrictive, layaway terms unclear; (e) **Legitimate dispute** — customer interpretation differs from policy but BuildRight is compliant; categorization drives both the DTI response and the internal corrective action | Regulatory Officer / Dept. Head | Legal Head | 1–2 hours/case |
| 5 | **Response preparation**: Regulatory Officer prepares BuildRight's written response to DTI: (a) summary of internal investigation findings; (b) BuildRight's position statement (admit fault, deny complaint, or partial admission); (c) supporting evidence (transaction records, system logs, photos, policies); (d) proposed resolution if admitting fault (refund, replacement, store credit, additional compensation); (e) Legal Head reviews and approves response before submission; (f) response submitted to DTI within deadline | Regulatory Officer / Legal Head | VP Legal | 2–4 hours/case |
| 6 | **DTI mediation attendance**: DTI schedules a mediation conference between BuildRight and complainant; Regulatory Officer (or Legal Head for High severity cases) attends on behalf of BuildRight: (a) presents BuildRight's position and evidence; (b) DTI mediator facilitates settlement discussion; (c) if settlement reached: agreement documented by DTI, BuildRight complies within agreed timeline (typically refund or replacement within 5–10 working days); (d) if settlement not reached: DTI escalates to formal adjudication | Regulatory Officer / Legal Head | VP Legal | 2–4 hours/mediation session |
| 7 | **Settlement execution**: If settlement reached at mediation: (a) Finance processes refund per W101 (Customer Refund & Credit Processing); (b) if product replacement: Store Manager coordinates with complainant for in-store pickup or delivery; (c) Regulatory Officer confirms settlement completion to DTI in writing; (d) case closed in case management system | Regulatory Officer / Finance / Store Manager | Legal Head | 1–2 hours/case |
| 8 | **Formal adjudication** (if mediation fails): (a) DTI Hearing Officer conducts formal hearing; BuildRight may engage external counsel; (b) both parties present evidence and arguments; (c) DTI issues Decision: dismiss complaint, order refund/replacement, impose administrative fine, or issue Cease and Desist order; (d) if BuildRight disagrees with Decision: may file Motion for Reconsideration within 15 days, or appeal to DTI Secretary within 15 days; (e) final DTI Decision is binding and enforceable | Legal Head / External Counsel | VP Legal | 2–6 months/case |
| 9 | **Corrective action implementation**: Regardless of case outcome, Regulatory Officer initiates corrective action based on root cause (W469.4): (a) **System error** → IT creates incident ticket (W48) for system fix; Pricing Analyst validates price sync across all stores; (b) **Human error** → Store Manager re-trains affected employee; Regional Manager includes in next store visit audit; (c) **Process failure** → VP Merchandising or relevant department head updates SOP per W186 SOP governance; (d) **Policy gap** → Legal Head and relevant VP review and update customer-facing policy; Marketing updates in-store signage; corrective action tracked in case management system with completion deadline | Regulatory Officer / Dept. Head | Legal Head | 1–4 hours/case + implementation time |
| 10 | **Pattern tracking and reporting**: (a) Regulatory Officer maintains DTI complaint register: case number, store, complaint category, root cause, resolution, DTI decision, corrective action, corrective action completion status; (b) quarterly: Regulatory Officer generates DTI complaint trend report — complaints by store, category, root cause; identifies repeat-offender stores or systemic issues; (c) quarterly report distributed to Legal Head, VP Merchandising, Store Ops Director, and Internal Audit (for potential inclusion in W121 operational audit); (d) annual: Regulatory Officer includes DTI complaint summary in annual regulatory compliance report (W437) | Regulatory Officer | Legal Head | 2 hours/quarter |

### System Touchpoints
- Compliance case management system: case logging, evidence attachment, deadline tracking, status management (W469.2)
- POS transaction lookup: pull transaction details by number, date, store, customer (W469.3a)
- CCTV footage retrieval with transaction timestamp cross-reference (W71 integration) (W469.3b)
- Price compliance audit log access (W69) for shelf label verification (W469.3c)
- Promotional setup records (W262) for promo pricing investigation (W469.3d)
- Internal complaint history (W41) for prior complaint lookup (W469.3g)
- Refund processing (W101) for settlement execution (W469.7a)
- SOP governance (W186) for corrective action documentation (W469.9c)
- Integration with W54 (LGU permits — DTI offices map to LGU jurisdictions per W310), W216 (BIR CAS audit — related regulatory exposure), W331 (DTI sales promotion permits — complaints may involve permitted promotions)

### Pain Points / Risks
- **Tight response deadlines**: DTI typically allows only 5–7 working days for initial response; gathering evidence from a provincial store (CCTV extraction, employee statements, system logs) within this window is challenging, especially if the Store Manager is on leave or the incident occurred weeks before the DTI complaint was filed
- **CCTV footage retention limit**: At 30 days online / 90 days archived (per W71), CCTV evidence may be unavailable for incidents that occurred more than 90 days before the DTI complaint; DTI may view the absence of CCTV evidence unfavorably
- **Systemic pricing errors affecting multiple customers**: A single price sync failure (W262) can cause hundreds of customers to be overcharged across multiple stores; while only one customer may file a DTI complaint, DTI may investigate whether the error was systemic and affect all impacted customers — exponentially increasing BuildRight's refund exposure
- **Consumer advocacy media risk**: DTI complaints are public records; media or consumer advocacy groups may obtain complaint details and publicize them, especially for High severity cases involving vulnerable consumers (senior citizens, PWDs) — reputational damage can exceed the direct financial cost of the complaint
- **Inconsistent store-level evidence preservation**: Store Managers may not preserve physical evidence (shelf labels, promotional signage, receipts) after an incident, assuming the internal complaint (W41) is resolved; when the customer later escalates to DTI, the evidence no longer exists

### Staffing Implication
- **Regulatory Officer**: Absorbs DTI complaint case management (~20–40 hours/year across 15–25 cases, including mediation attendance). This is a core function of the Regulatory Officer role. During formal adjudication cases (rare, ~1–2/year), workload spikes to ~10–20 hours/month for the duration of the hearing process (2–6 months).
- **Legal Head**: Reviews and approves all DTI responses; attends mediations for High severity cases. ~10–15 hours/year.
- **Store Manager**: Provides evidence and statements for complaints at their store. ~2–4 hours/complaint. Absorbed into existing duties.
- **External counsel**: Engaged only for formal adjudication cases (~1–2/year). Budgeted separately.

---

## W483. DOLE Drug-Free Workplace Program Compliance

| Field | Detail |
|---|---|
| **Trigger** | Annual drug testing cycle; new hire onboarding (W15); reasonable suspicion event |
| **Frequency** | Annual (scheduled testing); event-driven (reasonable suspicion, post-accident) |
| **Volume** | ~6,715 employees across 5 entities; annual testing targets ~20–30% random sample (~1,300–2,000 tests/year) |
| **Owner** | HR Compliance Manager |
| **Participants** | CHRO, DOLE-accredited drug testing laboratory, Store Managers, DC Managers, Legal, Security |

### Background

Under DOLE Department Order No. 53-03 (Guidelines on Drug-Free Workplace Policies) and Article V of RA 9165 (Comprehensive Dangerous Drugs Act), Philippine companies with 10 or more employees must formulate and implement a drug-free workplace policy. The policy must include: (a) awareness and education programs; (b) drug testing as part of the company's hiring process and random testing of current employees; (c) rehabilitation and referral programs for confirmed drug users; (d) disciplinary procedures for confirmed positive results. For BuildRight with 6,715 employees across 200 stores and 4 DCs, this is a significant compliance obligation requiring coordination with DOLE-accredited laboratories and a structured testing and rehabilitation framework.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Policy Maintenance**: HR Compliance Manager reviews and updates BuildRight's Drug-Free Workplace Policy annually: (a) ensure alignment with latest DOLE and Dangerous Drugs Board (DDB) guidelines; (b) update list of prohibited substances and testing protocols; (c) review disciplinary procedures and rehabilitation provisions; (d) obtain Legal Head sign-off; (e) distribute updated policy to all employees via HRIS portal and store bulletin boards | HR Compliance Mgr | CHRO | 2 days/annual |
| 2 | **Pre-Employment Drug Testing**: As part of recruitment onboarding (W15): (a) HR includes drug testing requirement in job offer conditional upon negative result; (b) candidate reports to DOLE-accredited laboratory within 5 working days; (c) HR receives result directly from laboratory; (d) positive result triggers adverse action per policy (offer rescission) | HR Assistant | HR Compliance Mgr | Per W15 |
| 3 | **Annual Random Testing Plan**: HR Compliance Manager prepares the annual random drug testing plan: (a) target: 20–30% of total workforce (aligned with DOLE guidance for large employers); (b) random selection using HRIS-generated list; (c) schedule testing per region (Mindanao, Visayas, Luzon, Metro Manila); (d) coordinate with DOLE-accredited laboratory for on-site testing teams at stores and DCs; (e) ensure testing is truly random and not discriminatory (no targeting of specific individuals) | HR Compliance Mgr | CHRO | 1 week |
| 4 | **Testing Execution**: DOLE-accredited laboratory conducts testing: (a) laboratory sends testing teams to designated locations (stores, DCs, HQ); (b) employees are notified on the day of testing (no advance notice); (c) specimen collection follows chain-of-custody protocols; (d) Store Managers and DC Managers facilitate employee release for testing without disrupting operations | Laboratory / HR Compliance Mgr | Store / DC Manager | 1–2 days/location |
| 5 | **Result Processing**: Laboratory issues results: (a) negative results — no further action; employee record updated; (b) positive results — laboratory confirms with confirmatory testing (GC/MS); (c) confirmed positive results reported confidentially to HR Compliance Manager only; (d) HR Compliance Manager secures results in restricted-access employee file (separate from regular personnel file per RA 9165 confidentiality provisions) | HR Compliance Mgr | CHRO | 1–2 weeks/batch |
| 6 | **Confirmed Positive Result Handling**: For confirmed positive results: (a) HR Compliance Manager conducts confidential meeting with employee; (b) employee is given opportunity for independent confirmatory testing at a different DOLE-accredited laboratory within 15 days; (c) if second test is positive: employee is referred to DOLE-accredited rehabilitation center (first offense) or subject to disciplinary action per policy (subsequent offenses); (d) if employee refuses rehabilitation or tests positive again: termination for cause under Article 297 of the Labor Code (serious misconduct); (e) Legal reviews all termination cases to ensure due process | HR Compliance Mgr / Legal | CHRO | 2–4 weeks/case |
| 7 | **Rehabilitation & Reintegration**: For first-time confirmed positive employees who opt for rehabilitation: (a) HR coordinates with DOLE-accredited rehabilitation center; (b) employee placed on leave of absence during rehabilitation; (c) upon successful completion and negative re-test: employee is reintegrated into workforce; (d) HR monitors employee for 12-month follow-up period with quarterly random re-testing | HR Compliance Mgr | CHRO | 3–6 months/case |
| 8 | **Awareness & Education**: Annual drug awareness program: (a) HR conducts drug awareness seminars during new hire orientation (W15); (b) annual refresher seminar for all employees (online or in-person per region); (c) materials posted in store and DC break rooms; (d) document attendance for DOLE compliance records | HR Training (W51) | HR Compliance Mgr | Per W51 |
| 9 | **Reasonable Suspicion Testing**: Event-driven testing when a manager observes specific, articulable indicators of drug use: (a) manager documents observations (behavior, appearance, performance changes); (b) manager reports to HR Compliance Manager; (c) HR Compliance Manager evaluates observations against policy criteria; (d) if criteria met: employee is transported to DOLE-accredited laboratory for immediate testing; (e) employee is suspended with pay pending results (to ensure safety) | Store / DC Manager | HR Compliance Mgr | Event-driven |
| 10 | **Annual Compliance Report**: HR Compliance Manager prepares annual drug-free workplace compliance report: (a) total employees tested; (b) number of positive results (anonymized); (c) rehabilitation referrals and outcomes; (d) awareness program attendance; (e) report submitted to CHRO for Board reporting (W124); (f) report available for DOLE inspection upon request | HR Compliance Mgr | CHRO | 1 day/annual |

### System Touchpoints
- HRIS: employee random selection, testing status tracking, result confidentiality, rehabilitation follow-up scheduling
- Employee Master Data (W292): new hire flag for pre-employment testing trigger
- Compliance Dashboard: drug testing status per location, testing completion rate, rehabilitation tracking
- Document Management (W255): secure storage of positive results (restricted access)
- Integration with W15 (onboarding — pre-employment testing), W51 (training — awareness program), W43 (separation — termination for confirmed positive), W140 (OHS — post-accident testing trigger), W10 (payroll — leave of absence during rehabilitation)

### Pain Points / Risks
- **Operational disruption during testing days**: Pulling 20–30% of store staff for testing on a single day can severely impact store operations, especially during peak hours; scheduling must be carefully coordinated with Store Managers to stagger testing across shifts
- **Geographic reach**: Covering 200 stores across the Philippines with DOLE-accredited laboratory teams requires significant logistics coordination and cost; remote stores (e.g., in rural Mindanao or island provinces) may have limited access to accredited laboratories
- **Confidentiality breach risk**: Positive drug test results are highly sensitive; any leak of positive results can expose BuildRight to liability under RA 9165 and the Data Privacy Act (RA 10173); restricted-access records must be carefully managed
- **Due process challenges**: Terminating an employee for drug use requires strict compliance with twin-notice rule and due process under Philippine labor law; procedural errors can lead to illegal dismissal claims at NLRC
- **Union escalation potential**: If labor unions (W493) view random testing as targeting specific employees or departments, it can become a labor relations issue

### Time Estimate
- Annual policy review: 2 days
- Annual testing plan preparation: 1 week
- Testing execution coordination: ~2 hours/location × 200 stores = ~400 hours (spread across HR team and laboratory)
- Result processing: ~1–2 weeks per batch
- Confirmed positive handling: ~2–4 weeks per case (estimated 5–15 cases/year)
- Annual compliance report: 1 day
- **Total annual HR Compliance Manager effort**: ~120–160 hours/year

### Staffing Implication
- **HR Compliance Manager**: Drug-free workplace program adds ~120–160 hours/year. Significant but manageable within existing role with support from HR Assistants.
- **DOLE-accredited laboratory**: External service provider; budgeted as compliance cost (~PHP 500–800/test × ~2,000 tests/year = ~PHP 1.0–1.6M/year).
- **Store/DC Managers**: Facilitate testing logistics. ~2–4 hours/testing event per location. Absorbed into existing duties.

---

## W484. Pandemic/Epidemic Business Response Protocol

| Field | Detail |
|---|---|
| **Trigger** | WHO/CDC/DOH pandemic declaration; DOH Alert Level escalation; significant local outbreak affecting stores or DCs |
| **Frequency** | Event-driven (activation); annual (plan review and tabletop exercise) |
| **Volume** | Typically 0–1 activations per year; may affect all 200 stores, 4 DCs, and HQ simultaneously |
| **Owner** | COO (Pandemic Response Commander) |
| **Participants** | CEO, CFO, COO, CIO, CHRO, CMO, VP Legal, VP Supply Chain, VP Store Ops, Regional Managers, Safety Officer, DPO |

### Background

The COVID-19 pandemic demonstrated that Philippine retailers must maintain operations during health emergencies while protecting employees and customers. Unlike weather-driven business continuity (W49 — typhoon BC), pandemic response involves: (a) prolonged operational disruption (months, not days); (b) government-mandated restrictions on capacity, hours, and product categories; (c) employee health monitoring and quarantine management; (d) supply chain disruption from import restrictions; (e) customer behavior shifts (panic buying, channel migration to ecommerce); (f) regulatory compliance with DOH/DTI/DOLE pandemic-specific orders. This workflow provides the pandemic-specific response framework that complements the general business continuity plan (W158, W465).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Pandemic Monitoring & Early Warning**: Safety Officer and VP Legal continuously monitor: (a) WHO Public Health Emergency of International Concern (PHEIC) declarations; (b) DOH Epidemiological Bulletins and Alert Level system; (c) DTI/DOLE pandemic-specific orders (store capacity limits, essential retailer classification, employee vaccination requirements); (d) LGU-specific executive orders (may impose stricter rules than national); (e) international travel advisories affecting import logistics (W144); escalate to COO when Alert Level reaches threshold defined in Pandemic Response Plan | Safety Officer / VP Legal | COO | Continuous (absorbed) |
| 2 | **Pandemic Response Team Activation**: COO activates the Pandemic Response Team (PRT): (a) convene PRT within 24 hours of trigger; (b) establish daily situation briefings (08:00 daily); (c) activate communication channels (dedicated Slack/Teams channel, emergency email distribution); (d) assign PRT roles: Operations Lead (COO), Finance Lead (CFO), People Lead (CHRO), IT Lead (CIO), Supply Chain Lead (VP Supply Chain), Legal Lead (VP Legal), Communications Lead (CMO) | COO | CEO | 4 hours |
| 3 | **Employee Health & Safety Measures**: CHRO implements workforce protection protocols: (a) activate remote work policy for HQ employees (per IT VPN/zero trust readiness W393); (b) implement daily health screening for store/DC employees (temperature checks, symptom questionnaire); (c) mandate PPE (masks, face shields per DOH/DOLE requirements W172); (d) establish isolation room at each store/DC for symptomatic employees; (e) implement contact tracing protocols (coordinated with barangay health workers per W209); (f) manage quarantine and isolation leave per DOH/DOLE guidelines (separate from standard SL/VL per W10); (g) coordinate vaccination drives with LGU health centers | CHRO | COO | Ongoing during pandemic |
| 4 | **Store Operations Adjustment**: VP Store Ops adjusts store operations per government mandates: (a) implement capacity limits (e.g., 30%, 50%, 75% based on DOH Alert Level); (b) adjust operating hours per LGU curfew orders; (c) implement queue management and social distancing markers; (d) restrict product categories if mandated (e.g., essential goods only during ECQ); (e) increase sanitization frequency (store opening checklist W5A modified); (f) install safety barriers at POS checkout; (g) shift customers to BOPIS (W11) and home delivery (W19) to reduce in-store traffic; (h) deploy mobile POS (W206) for outdoor/parking lot selling where LGU permits | VP Store Ops | COO | 1–3 days/Alert Level change |
| 5 | **Supply Chain Resilience**: VP Supply Chain activates supply chain contingency: (a) assess import supply disruption risk (W144) — container shipping delays, port closures, origin country lockdowns; (b) identify alternative local suppliers for critical categories (building materials, safety equipment); (c) increase safety stock levels for essential items (W312 parameter override); (d) prioritize DC throughput for essential goods; (e) coordinate with 3PL partners (W242) for continued delivery operations; (f) activate ecommerce surge capacity (W19, W11) for increased online demand | VP Supply Chain | COO | Ongoing during pandemic |
| 6 | **Financial & Cash Flow Management**: CFO activates financial contingency: (a) stress-test cash flow forecast (W233) under pandemic revenue scenarios; (b) identify non-essential capex for deferral (W21 budget hold); (c) draw on credit facilities if needed (W319); (d) apply for government relief programs (DOLE CAMP, SSS calamity loan, BIR tax extensions); (e) accelerate AR collection (W108) and negotiate extended AP terms with vendors; (f) monitor store-level P&L impact and adjust store operating budget (W489) | CFO | CEO | Ongoing during pandemic |
| 7 | **Communications Management**: CMO manages internal and external communications: (a) daily employee updates via HRIS portal and SMS blast; (b) customer communications on store hours, safety protocols, and ecommerce options; (c) media and public relations coordination (W143); (d) social media monitoring for misinformation (W142); (e) coordinate with barangay and LGU officials (W209) for community-level information sharing | CMO | CEO | Ongoing during pandemic |
| 8 | **IT Continuity**: CIO ensures IT systems support pandemic operations: (a) scale VPN capacity for remote HQ workers (W393); (b) ensure POS offline capability (W5G) for stores with degraded connectivity; (c) scale ecommerce infrastructure for surge demand; (d) maintain helpdesk (W48) support for remote workers; (e) ensure data privacy compliance (W53) for employee health data collected during screening | CIO | COO | Ongoing during pandemic |
| 9 | **Stand-Down & Recovery**: When DOH declares end of pandemic or Alert Level returns to normal: (a) COO convenes final PRT meeting for lessons learned; (b) gradual restoration of normal operations per phased approach; (c) employee reintegration for those on extended leave; (d) financial impact assessment and reporting; (e) update Pandemic Response Plan with lessons learned; (f) update Business Continuity Plan (W158, W465) with pandemic-specific learnings; (g) post-pandemic employee wellness program activation (W494) | COO | CEO | 2–4 weeks |
| 10 | **Annual Plan Review & Tabletop Exercise**: Annually (regardless of active pandemic): (a) HR Compliance Manager reviews and updates Pandemic Response Plan against latest DOH/DOLE/WHO guidelines; (b) conduct tabletop exercise with PRT members simulating a pandemic scenario; (c) update contact lists, communication templates, and vendor contingency lists; (d) coordinate with BC/DR testing (W158) for pandemic-specific scenarios | HR Compliance Mgr / Safety Officer | COO | 2 days/annual |

### System Touchpoints
- HRIS: employee health screening tracking, quarantine/isolation leave management, vaccination status
- POS: capacity monitoring, modified operating hours enforcement, restricted category controls
- Ecommerce platform: surge capacity scaling, BOPIS promotion
- Supply Chain Planning (W31): safety stock override parameters
- Treasury/Cash Management (W233, W30): cash flow stress testing
- Communication platforms: SMS blast, internal portal, social media
- Compliance Dashboard: pandemic response status per location
- Integration with W49 (typhoon BC), W158 (BC drill), W465 (network DR), W140 (OHS incidents), W172 (PPE), W209 (barangay relations), W5G (offline POS)

### Pain Points / Risks
- **Simultaneous disruption across all locations**: Unlike typhoons which affect specific regions, a pandemic can impact all 200 stores, 4 DCs, and HQ simultaneously — overwhelming the PRT's capacity to manage location-specific responses; this is fundamentally different from W49 (typhoon BC) which is geographically contained
- **Rapidly changing government mandates**: DOH Alert Levels and LGU executive orders can change with 24–48 hours' notice, requiring rapid operational adjustments across 200 stores in different LGU jurisdictions with different rules
- **Employee fear and absenteeism**: Even without government-mandated closures, employees may refuse to report to work due to fear of infection, creating severe staffing shortages at stores and DCs; this is especially acute for customer-facing store employees
- **Health data privacy**: Collecting employee health data (temperature, symptoms, vaccination status) creates significant Data Privacy Act (RA 10173) compliance obligations; misuse or breach of health data can result in NPC penalties and employee litigation
- **Supply chain cascade failure**: Import dependency (~40% of COGS from international vendors) means a pandemic affecting China, Taiwan, or other source countries can disrupt BuildRight's supply chain for months, well before the pandemic reaches the Philippines
- **Ecommerce infrastructure overload**: A sudden shift of customers from in-store to online can overwhelm ecommerce infrastructure that is sized for 3% of revenue, not 15–20% during a pandemic

### Time Estimate
- PRT activation: 4 hours
- Daily situation briefings: 1 hour/day during active pandemic
- Store operations adjustment: 1–3 days per Alert Level change
- Annual plan review and tabletop: 2 days
- Post-pandemic recovery: 2–4 weeks
- **Active pandemic**: PRT members dedicate 30–50% of working time during peak response

### Staffing Implication
- **No incremental headcount** — PRT is composed of existing executives and managers.
- **Operational time commitment during active pandemic**: COO (50%), CHRO (40%), VP Store Ops (40%), VP Supply Chain (30%), CFO (20%), CIO (20%), CMO (20%), VP Legal (10%).
- **Safety Officer**: Absorbs pandemic monitoring and health protocol implementation as additional duties (~10–20 hours/week during active pandemic).

---

## W505. DOLE Labor Inspection Response Protocol

| Field | Detail |
|---|---|
| **Trigger** | DOLE Regional Office serves notice of labor inspection (routine, complaint-driven, special, or follow-up) |
| **Frequency** | Routine: ~2–4 inspections/year across 200+ locations; complaint-driven: ad hoc (~5–10/year); follow-up: as needed |
| **Volume** | ~10–15 total DOLE inspections/year across the company |
| **Owner** | HR Director |
| **Participants** | HR Director, Legal Counsel, Store Manager (if store inspection), DC Manager (if DC inspection), Payroll Manager, Safety Officer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | HR Director receives DOLE inspection notice; classifies inspection type (routine, complaint-driven, special, follow-up); identifies inspection scope (specific location or HQ-wide) | HR Director | HR Director | 15 min |
| 2 | HR Director assembles inspection response team: HR Manager, Payroll Manager, Legal Counsel, Safety Officer (if OHS-related); assigns document preparation responsibilities | HR Director | VP Legal | 30 min |
| 3 | Document preparation per DOLE checklist: (a) Employment contracts and 201 files for all employees at inspection site; (b) Payroll registers (6 months) showing SSS/PhilHealth/Pag-IBIG deductions; (c) 13th month pay computation and proof of payment; (d) Service incentive leave records; (e) Overtime computation and holiday pay records; (f) SSS/PhilHealth/Pag-IBIG remittance receipts (6 months); (g) DOLE-required workplace postings (minimum wage, holiday pay, 13th month); (h) Safety committee minutes and OSHC compliance documents; (i) Working hours and rest period records; (j) Child labor / youth employment verification | Assigned Team | HR Director | 4–8 hours |
| 4 | HR Director or designate accompanies DOLE inspector during facility visit; takes notes of all inspector questions, observations, and requests | HR Director | VP Legal | Full inspection |
| 5 | DOLE inspector conducts document review and employee interviews; HR team provides requested documents and clarifications | DOLE Inspector / HR Team | HR Director | 2–4 hours |
| 6 | DOLE inspector issues inspection findings report (if deficiencies found); HR Director acknowledges receipt and signs finding report with notation "received for comment" | HR Director | VP Legal | 30 min |
| 7 | Legal Counsel reviews findings; HR Director prepares corrective action plan addressing each finding with specific actions, responsible persons, and target dates | Legal Counsel / HR Director | VP Legal | 4–8 hours |
| 8 | HR Director submits corrective action plan to DOLE within prescribed deadline (typically 5–10 working days from receipt of findings) | HR Director | VP Legal | 1 hour |
| 9 | HR team implements corrective actions; system tracks implementation status per finding; escalation if corrective action not completed by target date | HR Team | HR Director | Variable |
| 10 | If re-inspection: HR Director prepares re-inspection package showing all corrective actions completed with supporting evidence | HR Director | VP Legal | 2–4 hours |
| 11 | Annual: HR Director compiles DOLE inspection history; identifies recurring findings across locations; develops systemic preventive measures | HR Director | VP Legal | 4 hours/year |

### System Touchpoints
- DOLE inspection notice logging with inspection type classification (GOV-047)
- Document preparation checklist with per-item status tracking (GOV-047)
- Inspection findings register with severity classification and corrective action plan (GOV-047)
- Corrective action tracking with deadline monitoring and escalation (GOV-047)
- Payroll and statutory records retrieval for DOLE document requests (W10, W251)
- Safety committee minutes and OHS documentation retrieval (W140, W141, W436)
- Annual DOLE inspection history dashboard with recurring findings analysis (GOV-047)

### Time Estimate
Per inspection: ~8–16 staff-hours (preparation + attendance + corrective action). At ~12 inspections/year = ~96–192 staff-hours/year. Absorbed by HR Director, Legal Counsel, and HR Manager within existing FTE.

### Pain Points / Risks
- DOLE finds systemic non-compliance (e.g., incorrect overtime computation across multiple locations) — may result in penalty assessment affecting all locations
- Employee provides contradictory information during DOLE interview — mitigated by ensuring payroll records are accurate and complete before inspection
- Missed corrective action deadline — DOLE may issue compliance order or refer for legal action; mitigated by system deadline tracking and escalation

### Staffing Implication
- Absorbed within existing HR Director, Legal Counsel, and HR Manager FTEs.
- Adds ~10–15 staff-hours per inspection; ~12 inspections/year = ~120–180 staff-hours/year total.

---

## W506. Unified Regulatory Compliance Calendar & Dashboard

| Field | Detail |
|---|---|
| **Trigger** | Annual compliance calendar setup (January); ongoing deadline monitoring and alerting |
| **Frequency** | Continuous monitoring; daily deadline alerts; weekly compliance status review |
| **Volume** | ~500–700 compliance obligations/year across 5 entities × 200+ locations × 7+ regulatory bodies |
| **Owner** | Compliance Officer |
| **Participants** | Tax Accountant (BIR), Legal Counsel (SEC), Safety Officer (DOLE), Environmental Officer (DENR), Facilities Coordinator (LGU), Regulatory Officer (FDA/CAAP) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Compliance Officer initializes annual compliance calendar: loads all known recurring obligations per regulatory body (BIR monthly/quarterly/annual, LGU annual permits, DOLE annual reporting, DENR quarterly, SEC annual filings, FDA renewals, CAAP clearances) | Compliance Officer | VP Legal | 8 hours/year |
| 2 | System maps each obligation to: responsible person, affected entities, affected locations, deadline date, preparation lead time, required documents, reference workflow | System | — | Automated |
| 3 | System generates automated alerts: 30-day advance notice to responsible person; 7-day reminder; 1-day urgent alert; overdue escalation to Compliance Officer and VP Legal | System | — | Automated |
| 4 | Responsible person updates obligation status: Not Started → In Progress → Submitted → Confirmed; attaches proof of submission (eFiling confirmation, receipt, permit copy) | Responsible Person | Compliance Officer | 5 min/obligation |
| 5 | Compliance Officer reviews weekly compliance dashboard: completion rate, upcoming deadlines, overdue items, at-risk obligations | Compliance Officer | VP Legal | 1 hour/week |
| 6 | For multi-location obligations (e.g., LGU business permits for 200 stores): system provides per-location status view with drill-down; Compliance Officer identifies lagging locations and escalates to Regional Manager | Compliance Officer | VP Operations | 30 min/week |
| 7 | Monthly: Compliance Officer generates compliance status report for executive review: completion rate by regulatory body, overdue items with root cause, risk exposure assessment, upcoming critical deadlines | Compliance Officer | CFO / VP Legal | 2 hours/month |
| 8 | Quarterly: Compliance Officer conducts compliance risk review: identifies new regulatory requirements, assesses impact, assigns to responsible teams for implementation | Compliance Officer | VP Legal | 4 hours/quarter |
| 9 | Annually: Compliance Officer compiles annual compliance report: total obligations, completion rate, penalty exposure, audit findings, improvement recommendations | Compliance Officer | CFO / VP Legal | 8 hours/year |

### System Touchpoints
- Unified compliance calendar with multi-body obligation tracking (GOV-048)
- Automated deadline alerting with tiered escalation (30/7/1 day, overdue) (GOV-048)
- Per-entity and per-location compliance status dashboard (GOV-048)
- Document attachment for proof of submission per obligation (GOV-048)
- Integration with BIR filing workflows (W90, W260, W478)
- Integration with LGU permit workflows (W54, W54A, W448, W476, W485)
- Integration with DOLE reporting workflows (W436, W483, W512)
- Integration with DENR workflows (W433, W477)
- Integration with SEC filing workflows (W481, W482)
- Integration with FDA workflow (W479) and CAAP workflow (W480)
- Compliance risk assessment and regulatory change tracking (GOV-048)

### Time Estimate
Annual setup: ~8 hours. Weekly monitoring: ~1 hour. Monthly reporting: ~2 hours. Quarterly review: ~4 hours. Annual report: ~8 hours. Total: ~84 staff-hours/year. Absorbed by Compliance Officer within existing FTE.

### Pain Points / Risks
- New regulatory requirement not captured in calendar — mitigated by quarterly regulatory scan and subscription to BIR/DOLE/DENR/SEC advisory services
- Multi-location obligations (200 stores × LGU permits) create tracking complexity — mitigated by per-location status dashboard and automated escalation
- Compliance responsibility gaps when assigned person is on leave — mitigated by backup assignment in system and 30-day advance alerting

### Staffing Implication
- 1 Compliance Officer within Legal & Compliance team (9 FTE) dedicated to compliance calendar management.
- Regional Managers assist with location-specific compliance follow-ups within existing FTE.

---

## W626. Enterprise Risk Register Maintenance & Quarterly Risk Review

| Field | Detail |
|---|---|
| **Trigger** | New risk identified; quarterly risk review calendar; risk event occurrence |
| **Frequency** | Continuous risk identification; quarterly formal review; annual comprehensive assessment |
| **Volume** | ~80-120 active risks in enterprise risk register |
| **Owner** | Risk & Compliance Officer |
| **Participants** | Risk & Compliance Officer, C-suite executives, Department Heads, Internal Audit Director, External Risk Advisor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Risk & Compliance Officer maintains enterprise risk register in ERP governance module: each risk entry includes risk ID, category (strategic, operational, financial, compliance, reputational, ESG), description, root cause, affected processes, likelihood rating (1-5), impact rating (1-5), inherent risk score (likelihood × impact), existing controls, residual risk score, risk owner, mitigation plan, and target resolution date | Risk & Compliance Officer | — | Ongoing |
| 2 | New risk identification sources: (a) internal audit findings (per W120-W365), (b) incident reports (per W559, W140), (c) regulatory changes (per W506), (d) vendor risk assessments (per W558), (e) management committee observations, (f) external risk intelligence (per W397), (g) ERM annual workshop (per W122) | Multiple | Risk & Compliance Officer | As needed |
| 3 | When new risk identified: Risk & Compliance Officer drafts risk entry with preliminary assessment; assigns to relevant Department Head as risk owner; Department Head validates likelihood and impact ratings and proposes mitigation plan | Risk & Compliance Officer | Department Head | 30 min/risk |
| 4 | System monitors mitigation plan execution: auto-reminds risk owners of approaching deadlines; escalates overdue mitigation actions to Department Head and Risk & Compliance Officer; updates residual risk score when mitigation completed | System | — | Automated |
| 5 | Monthly: Risk & Compliance Officer reviews risk register for new entries, overdue mitigations, and risk score changes; updates risk dashboard for management visibility | Risk & Compliance Officer | — | 4 hours |
| 6 | Quarterly: Risk & Compliance Officer prepares risk review package — risk heat map, top 10 risks by residual score, new risks this quarter, closed risks, mitigation progress, and emerging risk trends | Risk & Compliance Officer | — | 8 hours |
| 7 | Quarterly Risk Review Committee meeting: Risk & Compliance Officer presents to CEO, CFO, COO, and Department Heads; committee validates risk ratings, approves mitigation plans for new risks, and escalates critical risks to Board Risk Committee (if applicable) | Risk & Compliance Officer | CEO | 2 hours |
| 8 | Annual: Risk & Compliance Officer facilitates enterprise-wide risk assessment workshop with all Department Heads; recalibrates risk universe; identifies strategic risks for next fiscal year; produces annual risk assessment report for Board of Directors | Risk & Compliance Officer | CEO | 16 hours |

### System Touchpoints
- ERP Governance module: risk register, heat map generation, mitigation tracking
- ERP Internal Audit module: audit finding integration (per W120-W365)
- ERP Compliance module: regulatory change tracking (per W506)
- BI dashboard: risk heat map, trend analysis, mitigation progress

### Pain Points / Risks
- **Risk register staleness**: without active maintenance, risk register becomes a compliance exercise rather than a management tool; mitigated by quarterly review discipline and integration with actual incident data
- **Subjective risk ratings**: likelihood and impact ratings may vary significantly between assessors; mitigated by rating criteria definitions with concrete examples and calibration sessions during annual workshop
- **Mitigation plan execution**: risk owners may not implement mitigation actions on schedule; mitigated by automated reminders and quarterly committee accountability
- **Emerging risk blind spots**: novel risks (cybersecurity, climate, pandemic) may not be captured by traditional risk categories; mitigated by external risk intelligence integration (per W397) and annual risk universe refresh

### Staffing Implication
- **Risk & Compliance Officer**: ~4 hours/week on register maintenance + ~8 hours/quarter on review preparation + ~16 hours/year on annual workshop = ~12 hours/week. Dedicated role within Legal & Compliance team.
- **Department Heads**: ~2 hours/quarter on risk review meeting + ~1 hour/quarter on mitigation plan updates = ~12 hours/year. Absorbed within existing roles.

---

## W627. Product Recall Effectiveness Verification & Post-Recall Review

| Field | Detail |
|---|---|
| **Trigger** | Recall execution completed (per W29); 30-day post-recall milestone |
| **Frequency** | Per recall event; estimated ~2-4 recalls/year |
| **Volume** | 1 effectiveness check per recall event |
| **Owner** | VP Merchandising |
| **Participants** | VP Merchandising, Supply Chain Director, LP Manager, QA Manager, Category Manager, Store Operations Director, Legal Counsel |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | At T+7 days after recall initiation (per W29): Category Manager verifies POS block compliance — confirms affected SKU is blocked at all 200 POS terminals and cannot be sold; spot-checks 10 random stores via phone or Regional Manager visit | Category Manager | VP Merchandising | 2 hours |
| 2 | At T+14 days: Supply Chain Director verifies physical stock quarantine — confirms all DC stock is quarantined, all in-transit stock is intercepted, and store-level stock is pulled from shelves; collects store-level confirmation reports | Supply Chain Director | — | 4 hours |
| 3 | At T+21 days: Category Manager verifies customer notification reach — system reports: (a) loyalty members who purchased affected product notified (target ≥ 95%), (b) B2B customers notified, (c) ecommerce customers notified, (d) general public notification published; calculates notification effectiveness rate | Category Manager | — | 2 hours |
| 4 | At T+30 days: VP Merchandising conducts effectiveness verification — (a) calculates % of affected stock accounted for (quarantined + returned + documented disposal), (b) calculates % of affected customers notified, (c) confirms zero additional sales of recalled product, (d) confirms DTI/FDA notification acknowledged | VP Merchandising | COO | 4 hours |
| 5 | If effectiveness targets not met (> 95% stock accounted for, > 90% customer notification): VP Merchandising extends recall period with targeted actions for remaining gaps (additional store visits, extended customer outreach, media re-notification) | VP Merchandising | COO | 2 hours |
| 6 | Post-recall review meeting (within 2 weeks of effectiveness verification): all stakeholders review recall execution timeline, bottlenecks encountered, communication effectiveness, and system performance; documents lessons learned | VP Merchandising | COO | 2 hours |
| 7 | QA Manager conducts root cause analysis with vendor — determines recall cause (manufacturing defect, specification change, contamination, labeling error); develops corrective action with vendor per CAPA process (per W110); updates incoming quality inspection protocol (per W625) if needed | QA Manager | Buyer | 4 hours |
| 8 | VP Merchandising updates recall playbook (W29) with lessons learned; updates mock recall exercise scenarios (per W622) to test improved processes; files regulatory close-out documentation with DTI/FDA as required | VP Merchandising | Legal Counsel | 4 hours |

### System Touchpoints
- ERP Inventory module: stock quarantine status, location-level compliance tracking
- ERP POS module: SKU block compliance monitoring
- ERP CRM module: customer notification tracking, reach analytics
- ERP Quality module: root cause analysis, CAPA tracking (per W110)
- ERP Regulatory module: regulatory filing management

### Pain Points / Risks
- **Incomplete stock accounting**: some affected product may have been sold to untraceable cash customers (no loyalty account); mitigated by broad public notification and in-store signage
- **Vendor non-cooperation**: vendor may dispute recall necessity or delay root cause analysis; mitigated by contractual recall cooperation clause and vendor chargeback for recall costs
- **Reputational damage**: even well-executed recalls generate negative publicity; mitigated by transparent communication, swift action, and customer-first messaging
- **Secondary recall**: if root cause not fully addressed, recall may recur for same product; mitigated by rigorous vendor CAPA in Step 7 and enhanced incoming inspection in Step 7

### Staffing Implication
- **VP Merchandising**: ~12 hours per recall event for effectiveness verification and post-recall review. Absorbed within existing role.
- **Category Manager**: ~6 hours per recall event for compliance verification. Absorbed within existing role.
- **Supply Chain Director**: ~4 hours per recall event for stock verification. Absorbed within existing role.
- **QA Manager**: ~4 hours per recall event for root cause analysis. Absorbed within existing role.

---

## W656. Anti-Bribery & Anti-Corruption (ABAC) Compliance Program

| Field | Detail |
|---|---|
| **Trigger** | Annual program cycle; triggered by suspicion of corrupt activity; periodic third-party due diligence |
| **Frequency** | Annual risk assessment and training; continuous monitoring; quarterly gift register review |
| **Volume** | ~6,715 employees (annual training); ~800–1,000 vendors (due diligence); ~200 LGUs (interaction points) |
| **Owner** | Compliance Officer |
| **Participants** | Legal Counsel, Internal Audit (W159), Procurement Manager, HR Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Annual: Compliance Officer conducts ABAC risk assessment: identifies high-risk roles (procurement buyers, store managers interacting with LGU officials, government procurement team, construction project managers), high-risk transactions (government permits per W54, vendor selection per W632, construction contracts per W224), and high-risk geographies (LGUs with known corruption history) | Compliance Officer | VP Legal | 2 weeks |
| 2 | Annual: HR Manager facilitates anti-corruption training for all employees (online module, 1 hour); enhanced in-person training for high-risk roles (3 hours with case studies and Philippine context — Anti-Graft and Corrupt Practices Act RA 3019) | HR Manager | Compliance Officer | 1 month rollout |
| 3 | Continuous: Compliance Officer manages gift and entertainment register — employees declare all gifts/hospitality received from vendors or government officials exceeding PHP 1,000; system auto-routes declarations to Compliance Officer for review and approval/return | Employee | Compliance Officer | 5 min/declaration |
| 4 | Quarterly: Compliance Officer reviews gift register for patterns (excessive gifts from specific vendor, gifts to specific government officials); investigates anomalies | Compliance Officer | VP Legal | 1 day/quarter |
| 5 | For vendor onboarding (W36/W620): Compliance Officer conducts third-party due diligence for high-risk vendors and agents — beneficial ownership verification, PEP (Politically Exposed Person) screening, sanctions list screening, reputation risk assessment | Compliance Officer | Procurement Manager | 1 day/vendor |
| 6 | For suspected corrupt activity: Compliance Officer activates investigation protocol; coordinates with Internal Audit (W159) and Legal Counsel; ensures whistleblower protection per W79; escalates to CEO and Board Audit Committee if confirmed | Compliance Officer | VP Legal | Per investigation |
| 7 | Annual: Compliance Officer produces ABAC program effectiveness report: training completion rate, gift register compliance, due diligence completion, investigation outcomes, recommendations; presents to Board Audit Committee | Compliance Officer | VP Legal | 1 day |

### System Touchpoints
- Compliance management module, gift/entertainment declaration portal, vendor due diligence system, training module (completion tracking), whistleblower system (W79)

### Time Estimate
- Annual assessment: 2 weeks; training rollout: 1 month; quarterly reviews: 1 day each; ongoing monitoring: 2 hours/week

### Pain Points / Risks
- Cultural normalization of gift-giving in Philippine business; facilitation payment expectations at LGU level for permit processing; gift register under-reporting; difficulty distinguishing legitimate business entertainment from bribery; third-party agent corruption beyond BuildRight's direct control

### Staffing Implication
- **Compliance Officer**: ~2 hours/week ongoing monitoring + 2 weeks annual assessment + 1 day/quarter gift register review + 1 day annual report. Dedicated compliance role, possibly shared with other governance functions.
- **HR Manager**: ~1 month annual training rollout coordination. Absorbed within existing HR role.

---

## W657. Regulatory Change Management & Impact Assessment

| Field | Detail |
|---|---|
| **Trigger** | New regulation, regulation amendment, or regulatory issuance from any Philippine government agency (BIR, DTI, DOLE, DENR, SEC, BOC, FDA, LGU) |
| **Frequency** | ~20–30 regulatory changes/year requiring assessment; ~5–10 requiring operational action |
| **Volume** | Continuous monitoring of ~15 regulatory agencies |
| **Owner** | Regulatory Compliance Officer |
| **Participants** | VP Legal, affected department heads (Finance for BIR, HR for DOLE, Merchandising for DTI, Supply Chain for BOC, IT for data privacy), Compliance Officer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Regulatory Compliance Officer identifies new regulation via monitoring sources: BIR Revenue Regulations/Revenue Memoranda, DTI Department Orders/Administrative Orders, DOLE Department Orders/Labor Advisories, DENR Administrative Orders, SEC Memorandum Circulars, BOC Customs Memorandum Orders, FDA advisories, LGU ordinances, and Official Gazette publications | Regulatory Compliance Officer | VP Legal | Ongoing, 1 hour/day monitoring |
| 2 | Regulatory Compliance Officer performs initial impact assessment: which entities are affected, which operations, which systems, which workflows, what is the compliance deadline, what is the penalty for non-compliance, what is the effort to implement | Regulatory Compliance Officer | VP Legal | 1 day/regulation |
| 3 | Regulatory Compliance Officer distributes impact assessment to affected department heads with implementation action request and deadline | Regulatory Compliance Officer | VP Legal | 0.5 day |
| 4 | Affected department head develops implementation plan: system changes (IT), process changes (operations), training needs (HR), document updates (Legal), budget requirements (Finance); assigns responsible person and target completion date | Department Head | VP Legal | 1–5 days depending on complexity |
| 5 | Regulatory Compliance Officer tracks implementation progress against compliance deadline; sends escalation alerts at T-30 days, T-14 days, and T-7 days for incomplete actions | Regulatory Compliance Officer | VP Legal | Ongoing |
| 6 | Upon implementation: Department Head confirms compliance; Regulatory Compliance Officer verifies and updates compliance calendar (W506) and relevant workflow documentation | Department Head | VP Legal | 0.5 day |
| 7 | Quarterly: Regulatory Compliance Officer produces regulatory change digest summarizing all changes implemented, pending actions, and upcoming regulations in pipeline; distributes to executive team | Regulatory Compliance Officer | VP Legal | 1 day/quarter |

### System Touchpoints
- Compliance calendar (W506), regulatory monitoring service, document management (W255), action tracking system

### Time Estimate
- Daily monitoring: 1 hour; per-regulation assessment: 1 day; quarterly digest: 1 day

### Pain Points / Risks
- Frequency and unpredictability of Philippine regulatory changes (especially BIR revenue regulations before tax season); short compliance deadlines (some BIR regulations have 15-day effective periods); vague regulatory language requiring interpretation; inconsistent LGU ordinance application across 200 jurisdictions; implementation cost for system changes triggered by regulation

### Staffing Implication
- **Regulatory Compliance Officer** (1 FTE): ~1 hour/day monitoring + 1 day per regulation assessed (~20–30 days/year) + 1 day/quarter digest. Dedicated regulatory compliance role within Legal/Compliance function.
- **Department Heads**: 1–5 days per affected regulation; varies widely. Absorbed within existing roles.

---

## W658. General Regulatory Inspection Response Protocol

| Field | Detail |
|---|---|
| **Trigger** | Unannounced regulatory inspection at any location (store, DC, HQ) |
| **Frequency** | ~30–50 inspections/year across 200 stores, 4 DCs, and HQ |
| **Volume** | ~3–5 per month |
| **Owner** | Regulatory Compliance Officer |
| **Participants** | Location Manager (Store Manager/DC Manager), VP Legal, affected Department Head, Compliance Officer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Location Manager receives inspector; verifies inspector credentials (government ID, authority letter, specific agency); confirms inspection type and scope; contacts Regulatory Compliance Officer within 15 minutes for guidance | Location Manager | Regulatory Compliance Officer | 15 min |
| 2 | Regulatory Compliance Officer identifies relevant inspection protocol by agency: BIR (tax compliance, CAS per W216), DTI (consumer protection, pricing per W69, product standards), DOLE (labor standards per W505), DENR (environmental per W477), BFP (fire safety per W476), FDA (product safety per W479), LGU (business permit compliance per W54), SEC (corporate governance per W481); provides Location Manager with inspection-specific checklist and guidance | Regulatory Compliance Officer | VP Legal | 15 min |
| 3 | Location Manager accompanies inspector throughout inspection; provides requested documents (permits, licenses, records); does not volunteer information beyond scope; takes notes on all inspector observations and requests | Location Manager | Regulatory Compliance Officer | Duration of inspection |
| 4 | If inspector issues Notice of Violation or findings on-site: Location Manager signs acknowledgment (not admission of liability); obtains copy of all findings; does NOT agree to on-the-spot payment or penalty | Location Manager | VP Legal | During inspection |
| 5 | Location Manager submits inspection report with findings to Regulatory Compliance Officer within 24 hours; includes inspector name, agency, scope, findings, required response deadline, and any documents provided to or obtained from inspector | Location Manager | Regulatory Compliance Officer | 2 hours |
| 6 | Regulatory Compliance Officer coordinates with VP Legal and affected Department Head to prepare response: corrective action plan addressing each finding; legal review of response language; response submitted within agency-prescribed deadline (typically 5–15 business days) | Regulatory Compliance Officer | VP Legal | 2–5 days |
| 7 | Department Head implements corrective actions; Regulatory Compliance Officer tracks completion and documents closure; updates compliance calendar (W506) if finding relates to permit renewal or recurring requirement | Department Head | VP Legal | Per corrective action timeline |
| 8 | Monthly: Regulatory Compliance Officer produces inspection activity report: inspections by agency, location, finding type, corrective action status, repeat findings; identifies systemic issues requiring enterprise-wide action | Regulatory Compliance Officer | VP Legal | 2 hours/month |

### System Touchpoints
- Compliance calendar (W506), document management (W255), inspection log, corrective action tracker

### Time Estimate
- Inspection day: 2–8 hours; response preparation: 2–5 days; corrective action: varies by finding

### Pain Points / Risks
- Inspector demands for on-the-spot payment or "facilitation fees"; untrained store managers inadvertently making commitments during inspection; inspection timing during peak business hours; inconsistent regulatory interpretation between inspectors; LGU inspections varying by municipality with different requirements; repeat findings at same location indicating systemic non-compliance

### Staffing Implication
- **Regulatory Compliance Officer**: ~2 hours/month on inspection reporting + ad hoc response coordination (2–5 days per inspection with findings). Shared with W657 regulatory change management role.
- **Location Managers** (Store Managers/DC Managers): variable time during inspections; absorbed within existing management responsibilities.

---

## W685. Business Continuity Plan Maintenance & Annual BIA Refresh

| Field | Detail |
|---|---|
| **Trigger** | Annual BIA refresh cycle; post-incident plan update; organizational change (new store, new system, new entity) |
| **Frequency** | Annual comprehensive BIA refresh; semi-annual plan testing (W158 drill); quarterly plan review; post-incident plan update |
| **Volume** | 1 enterprise BC plan covering 200 stores, 4 DCs, HQ; ~15-20 individual BC procedure documents (one per critical function) |
| **Owner** | Compliance Manager (BC Program Owner) |
| **Participants** | Department Heads (all), IT Director, VP Store Operations, VP Supply Chain, CFO, External BC Consultant |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Compliance Manager initiates annual BIA (Business Impact Analysis) refresh: distributes BIA questionnaire to all Department Heads covering: critical business processes, maximum tolerable downtime (MTD), recovery time objectives (RTO), recovery point objectives (RPO), key dependencies (systems, suppliers, people, facilities), and financial impact of outage per hour | Compliance Manager | Department Heads | 1 day |
| 2 | Department Heads complete BIA questionnaire with input from direct reports; Compliance Manager consolidates responses | Department Heads | Compliance Manager | 2-3 hours each |
| 3 | Compliance Manager and External BC Consultant analyze BIA results: identify changes from prior year (new stores, new systems like ecommerce platform, new critical dependencies), validate MTD/RTO/RPO targets against current recovery capabilities (W55 IT DR, W580 manual operations), and update critical process prioritization | Compliance Manager | External BC Consultant | 2 days |
| 4 | Compliance Manager updates BC plan documents: contact tree (all Department Heads, Regional Managers, DC Managers — refreshed for organizational changes), critical system recovery sequence (updated for new ERP modules per W616), alternate site operations (updated for new store locations), communication protocols (updated for new communication tools), and vendor emergency contacts | Compliance Manager | — | 2 days |
| 5 | IT Director updates IT disaster recovery plan per W55 based on BIA refresh: confirms RTO/RPO capabilities, tests failover procedures, updates runbooks for new systems | IT Director | Compliance Manager | 2 days |
| 6 | VP Store Operations updates store-level BC procedures: typhoon protocol per W576, manual operations per W580, power failure per W470, and communication chain for 200 stores | VP Store Operations | Compliance Manager | 2 days |
| 7 | Compliance Manager presents updated BIA and BC plan to Executive Committee (CEO, CFO, COO, CIO) for approval; Executive Committee confirms resource allocation for BC program | Compliance Manager | CEO, CFO, COO, CIO | 2 hours |
| 8 | Semi-annual: Compliance Manager coordinates BC drill per W158; drill results feed back into plan improvements | Compliance Manager | VP Store Operations, IT Director | 1 day |
| 9 | Post-incident (any significant disruption): Compliance Manager conducts post-incident review; documents actual vs. planned response performance; updates BC plan with lessons learned | Compliance Manager | — | 2-3 days |
| 10 | Quarterly: Compliance Manager reviews BC plan for accuracy (contact information, system inventory, vendor contacts) and distributes updated plan to all BC role holders | Compliance Manager | — | 1 day |

### System Touchpoints
- BC plan document management system
- BIA tool
- IT DR plan (W55)
- Emergency communication system
- Contact database

### Time Estimate
- Annual BIA refresh: 10 days
- Quarterly review: 1 day
- Post-incident update: 2-3 days

### Pain Points / Risks
- BIA questionnaire fatigue from annual refresh
- Organizational change velocity outpacing BC plan updates
- 200-store communication chain accuracy
- BC plan testing consuming operational time
- Difficulty quantifying MTD for subjective business processes

### Staffing Implication
- Compliance Manager: ~10 days/year on BC program + quarterly reviews
- External BC Consultant: ~5 days/year on BIA analysis
- Department Heads: ~2 hours/year on BIA questionnaire each

---

## W730. Anti-Money Laundering (AML) Compliance Program Operations

| Field | Detail |
|---|---|
| **Trigger** | Monthly AML compliance review cycle; or suspicious transaction flag from POS per W519 or wholesale per W598; or AMLC audit notification |
| **Frequency** | Monthly (program review); real-time (transaction monitoring) |
| **Volume** | ~2-5 suspicious transaction reports (STRs) per month; ~10-15 covered transaction reports (CTRs) per month |
| **Owner** | Compliance Officer |
| **Participants** | Store Manager, Cashier, Wholesale Manager, Finance Manager, Legal Counsel, AMLC |

### Background

Under the Anti-Money Laundering Act (RA 9160 as amended by RA 10121), BuildRight Depot qualifies as a "covered person" due to the volume of cash transactions processed through its 600 POS terminals (~42% cash transactions = ~PHP 2.1B/month in cash). W519 covers POS-level suspicious transaction detection and reporting, and W354 covers AML screening audit. This workflow addresses the enterprise-level AML compliance program operations: ongoing monitoring, staff training, regulatory filing, record retention, and AMLC engagement. The Philippine AML framework requires covered persons to establish internal AML programs, appoint compliance officers, and file reports with the Anti-Money Laundering Council (AMLC).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Monthly transaction monitoring review**: Compliance Officer reviews aggregated transaction data: (a) cash transactions ≥ PHP 500,000 per W519: verify all were properly reported as Covered Transactions (CTRs) to AMLC within 5 working days; (b) structuring detection: identify customers who conducted multiple transactions just below PHP 500,000 threshold within 72 hours across same or different stores; (c) unusual pattern analysis: (i) sudden large cash purchases by new trade accounts; (ii) wholesale cash buyers with no identifiable business purpose; (iii) repetitive purchases of high-value items (appliances, power tools) inconsistent with customer profile; (iv) B2B customers paying large amounts in cash rather than standard payment terms; (d) generate monthly monitoring report with flagged transactions requiring investigation | Compliance Officer | VP Legal | 4-6 hours/month |
| 2 | **Suspicious Transaction Report (STR) filing**: for transactions flagged as suspicious: (a) Compliance Officer investigates: (i) review customer profile in CRM; (ii) check transaction history; (iii) interview Store Manager or Cashier if needed; (b) if suspicion confirmed: prepare STR per AMLC format: (i) subject identification (name, TIN, ID details); (ii) transaction details (date, amount, store, payment method); (iii) basis for suspicion; (iv) supporting documentation; (c) file STR with AMLC via online portal within required timeline; (d) VP Legal reviews all STRs before filing; (e) system logs STR filing with reference number; (f) maintain strict confidentiality: no tipping off the subject per RA 9160 Section 9 | Compliance Officer | VP Legal | 2-4 hours per STR |
| 3 | **AML training program**: Compliance Officer manages AML training: (a) annual mandatory training for all cashiers per W519 (1 hour): cash transaction thresholds, identification requirements, suspicious behavior indicators, reporting procedure; (b) enhanced training for Store Managers and Wholesale Managers (2 hours): STR indicators, structuring detection, customer due diligence for B2B accounts; (c) Compliance Officer training (4 hours): AMLC regulations, STR preparation, investigation techniques, record retention; (d) new employee onboarding module per W15 (30 min AML awareness); (e) training completion tracked in employee records per W51 | Compliance Officer / HR Manager | VP Legal | Ongoing; ~8,000 training hours/year across all employees |
| 4 | **Customer due diligence (CDD) for B2B accounts**: during trade/corporate account onboarding per W460: (a) verify customer identity: (i) SEC/DTI registration documents; (ii) business permits; (iii) authorized representatives with valid government ID; (b) assess customer risk level: (i) standard risk: established businesses with verifiable registration; (ii) elevated risk: cash-intensive businesses, newly registered companies, politically exposed persons (PEPs); (iii) high risk: businesses in high-risk jurisdictions, complex ownership structures; (c) for elevated/high-risk: enhanced due diligence (EDD): source of funds verification, beneficial ownership identification; (d) CDD records maintained per RA 9160 retention requirements (5 years minimum); (e) periodic CDD refresh: annual for standard, semi-annual for elevated, quarterly for high-risk | Compliance Officer / Credit Analyst | VP Legal | 30-60 min per account |
| 5 | **Record retention and audit readiness**: Compliance Officer ensures AML records are audit-ready: (a) CTRs and STRs: maintain for 5 years per RA 9160; (b) customer identification records: 5 years after business relationship ends; (c) transaction records: 5 years from transaction date; (d) training records: maintain evidence of all AML training per step 3; (e) internal policies and procedures: current version plus 5-year history; (f) annual AML program self-assessment: (i) review CTR/STR filing timeliness; (ii) review training completion rate (target: 100% for mandatory, 95% for enhanced); (iii) review CDD completion rate; (iv) identify program gaps and improvement actions | Compliance Officer | VP Legal | 2-3 days/year |
| 6 | **AMLC examination coordination**: if AMLC notifies BuildRight of an examination: (a) Compliance Officer coordinates: (i) compile requested transaction records, CTRs, STRs, and customer files; (ii) prepare AML program documentation: policies, procedures, training records, board-approved compliance officer designation; (iii) arrange on-site examination logistics at HQ and/or designated stores; (b) during examination: Compliance Officer serves as primary point of contact; (c) post-examination: (i) address any findings or deficiencies within AMLC-prescribed timeline; (ii) implement corrective actions; (iii) report findings to Audit Committee | Compliance Officer | VP Legal | 3-5 days per examination |

### System Touchpoints

- POS transaction monitoring per W519 with AML threshold alerting
- CRM/customer master per CRM-001/003 for customer due diligence data
- AMLC online portal for CTR and STR filing
- Transaction analytics engine for structuring detection and pattern analysis
- Employee training management per W51 for AML training tracking
- Document management per W255 for record retention
- W460 corporate/trade account onboarding for CDD integration

### Pain Points / Risks

- **Cash-intensive business nature**: with ~42% of POS transactions in cash (PHP 2.1B/month), BuildRight processes enormous cash volumes that attract AML scrutiny; the sheer volume makes monitoring challenging
- **Retail AML challenges**: unlike banks, retail staff are not trained financial investigators; cashiers may not recognize sophisticated money laundering techniques
- **AMLC examination penalty exposure**: failure to file CTRs or maintain adequate AML programs can result in fines of PHP 100,000-500,000 per violation per RA 9160
- **Tipping-off risk**: store-level employees discussing suspicious transactions with customers or among themselves violates RA 9160 confidentiality requirements
- **Wholesale cash transactions**: B2B wholesale customers paying in cash (rather than standard terms) are a key AML risk vector that requires enhanced monitoring per W598

### Staffing Implication

Compliance Officer: ~15-20 hours/month on AML program management. VP Legal: ~2-3 hours/month on STR review and program oversight. Cashiers: ~1 hour/year AML training. Store Managers: ~2 hours/year. Absorbed within existing Compliance Officer role. No incremental headcount.

### Time Estimate

**Monthly monitoring**: 4-6 hours. **Per STR**: 2-4 hours. **Training program**: 8,000 hours/year across all employees (absorbed in onboarding and annual cycle). **Annual self-assessment**: 2-3 days. **AMLC examination**: 3-5 days (rare).

---

## W731. Consumer Act (RA 7394) Compliance Monitoring & Enforcement

| Field | Detail |
|---|---|
| **Trigger** | Monthly compliance review cycle; or consumer complaint per W41; or DTI inspection notification |
| **Frequency** | Monthly (monitoring); ad-hoc (complaints, inspections) |
| **Volume** | ~50-100 consumer complaints/month; ~5-10 DTI-related escalations/month; 200 stores requiring compliance |
| **Owner** | Compliance Officer |
| **Participants** | Store Manager, Merchandising Manager, Customer Service, Legal Counsel, DTI |

### Background

The Consumer Act of the Philippines (RA 7394) establishes comprehensive consumer protection requirements affecting retail operations: mandatory price tagging, truthful advertising, product safety standards, return and exchange policies, and warranty compliance. With 200 stores, 600 POS terminals, and 2.8M monthly transactions, Consumer Act compliance is a daily operational concern. W468 covers DTI price freeze compliance and W427 covers sales promotion permits. This workflow covers the broader Consumer Act compliance program including price display compliance, product safety monitoring, return policy enforcement, and DTI engagement.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Monthly price display compliance audit**: Compliance Officer conducts monthly audit of price display compliance per RA 7394 Article 81-82: (a) random sample of 10 stores per month (rotating coverage across 200 stores ensures each store audited at least once per 20 months); (b) verify: (i) every item on shelf has a price tag or shelf label per W181; (ii) price tag shows: selling price, unit of measure, and price per unit; (iii) promotional pricing clearly displays original and discounted price; (iv) no "ghost markdowns" — items displayed at promotional price that have reverted to regular price; (v) price accuracy: physical tag matches POS price and ecommerce price per W678; (c) document findings with photographic evidence; (d) issue compliance report to Store Manager and Regional Manager | Compliance Officer | VP Store Ops | 1 day per store audit; ~10 days/month |
| 2 | **Product safety monitoring**: Compliance Officer monitors product safety compliance per RA 7394 Article 22-30: (a) maintain product safety alert registry: (i) items subject to mandatory DTI-BPS certification per W447; (ii) items with active consumer safety complaints per W41; (iii) items recalled per W29; (iv) items with expired shelf life; (b) for flagged items: (i) verify ICC/SOC mark is displayed on product and packaging; (ii) coordinate with Merchandising per W625 for quality testing results; (iii) remove non-compliant items from shelf immediately if safety risk identified; (c) quarterly product safety review with Merchandising and Quality teams | Compliance Officer | VP Merchandising | 4-6 hours/month |
| 3 | **Return and exchange policy compliance**: monitor adherence to BuildRight's return policy (which must comply with RA 7394): (a) verify stores display return policy: (i) posted at customer service counter; (ii) printed on receipts; (iii) available on website; (b) review return transactions per W12 for policy compliance: (i) are stores accepting returns within policy window?; (ii) are stores improperly denying valid returns?; (iii) are stores granting exceptions that violate policy?; (c) investigate DTI consumer complaints related to returns: (i) compile transaction evidence; (ii) propose resolution (refund, exchange, store credit); (iii) Legal Counsel reviews if complaint escalates to DTI adjudication | Compliance Officer / Store Manager | VP Store Ops | 4-6 hours/month |
| 4 | **DTI inspection response**: when DTI conducts store inspection: (a) Store Manager notifies Compliance Officer immediately; (b) Compliance Officer coordinates response: (i) provide requested documents: business permit per W54, price tags, product certifications per W447, sales promotion permits per W427, consumer complaint log; (ii) accompany DTI inspector during store walkthrough; (iii) address any immediate findings (reprice items, remove non-compliant products); (c) post-inspection: (i) document DTI findings; (ii) develop corrective action plan for any violations; (iii) submit corrective action evidence to DTI within prescribed timeline; (iv) implement preventive measures across all stores if finding is systemic | Compliance Officer / Store Manager | VP Legal | 4-8 hours per inspection |
| 5 | **Consumer complaint DTI escalation management**: for consumer complaints escalated to DTI per W469: (a) Legal Counsel reviews complaint with Compliance Officer; (b) prepare BuildRight response: (i) factual chronology of the transaction and complaint handling; (ii) evidence: receipts, CCTV footage per W207, product photos, communication records; (iii) proposed amicable settlement if appropriate; (c) attend DTI mediation/conciliation proceedings; (d) if settlement reached: execute within agreed timeline; (e) if unresolved: prepare for DTI adjudication with Legal Counsel; (f) track all DTI cases and outcomes for trend analysis | Compliance Officer / Legal Counsel | VP Legal | 4-8 hours per case |
| 6 | **Quarterly Consumer Act compliance report**: Compliance Officer prepares quarterly report: (a) price display compliance rate by store and region; (b) product safety incidents and resolutions; (c) return policy compliance metrics; (d) DTI inspection results and corrective actions; (e) consumer complaint volume, resolution rate, and DTI escalation count; (f) training completion: Consumer Act awareness training for store staff (annual 1-hour module); (g) recommendations for compliance improvement | Compliance Officer | VP Legal / VP Store Ops | 4-6 hours/quarter |

### System Touchpoints

- Price management system per W40 for price accuracy verification
- POS system per W5B for transaction and return data
- Product certification tracking per W447 (DTI-BPS ICC/SOC)
- Consumer complaint management per W41 and W469
- W12 returns workflow for return policy compliance monitoring
- W427 DTI sales promotion permit tracking
- W468 DTI price freeze compliance
- W678 multi-channel pricing consistency monitoring
- Store audit management system

### Pain Points / Risks

- **Price tag compliance at scale**: with 35,000 active SKUs across 200 stores (7M shelf positions), maintaining 100% price tag compliance is nearly impossible; DTI inspectors routinely find gaps during random inspections
- **Consumer complaint volume**: with 2.8M monthly transactions, even a 0.01% complaint rate generates ~280 complaints/month; managing DTI escalation for the small fraction that reach DTI is resource-intensive
- **DTI inspector inconsistency**: different DTI regional offices and inspectors may interpret RA 7394 requirements differently, creating compliance uncertainty for a national chain operating across 200 LGU jurisdictions
- **Product certification gaps**: imported items may arrive without Philippine ICC/SOC marks, requiring BuildRight to either obtain certification or remove items from shelves, creating revenue loss and customer disappointment

### Staffing Implication

Compliance Officer: ~10-15 hours/month on Consumer Act compliance. Store Managers: absorbed within existing duties for daily compliance. Legal Counsel: ~4-8 hours per DTI case. No incremental headcount.

### Time Estimate

**Monthly monitoring**: 10-15 days (including store audits). **Per DTI inspection**: 4-8 hours. **Per DTI case**: 4-8 hours over 1-3 months. **Quarterly report**: 4-6 hours.

---

## W732. Vendor Tax Compliance Monitoring & BIR TIN Validation

| Field | Detail |
|---|---|
| **Trigger** | Vendor onboarding per W36; annual vendor tax compliance review; BIR TIN validation batch run |
| **Frequency** | At vendor onboarding; annual review for all active vendors; monthly batch TIN validation |
| **Volume** | ~800-1,000 active vendors; ~50-100 new vendors/year; ~1,000 monthly TIN validations |
| **Owner** | Tax Accountant |
| **Participants** | AP Clerk, Procurement Manager, Vendor, BIR |

### Background

Under Philippine tax law, BuildRight must ensure that all vendors have valid Tax Identification Numbers (TINs) and proper tax registrations before processing payments and applying withholding tax. Paying a vendor without a valid TIN or with incorrect TIN information exposes BuildRight to: (1) disallowance of deductible expenses (increasing corporate income tax); (2) inability to properly withhold and remit EWT; (3) BIR audit findings and penalties. With ~800-1,000 active vendors processing ~9,500 AP invoices/month, vendor tax compliance is a significant operational concern. This workflow complements W36 (vendor onboarding) and W7 (AP processing) by adding the tax compliance layer.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **TIN validation at vendor onboarding**: during vendor onboarding per W36: (a) AP Clerk collects vendor tax documents: (i) BIR TIN (mandatory for all vendors); (ii) BIR Certificate of Registration (COR) — confirms tax type registrations (VAT, Non-VAT, Percentage Tax); (iii) BIR Form 2303 (Certificate of Registration); (iv) for VAT-registered vendors: VAT registration certificate; (b) Tax Accountant validates TIN: (i) format check: XXX-XXX-XXX-000 (must be 12 digits); (ii) BIR eRegistration/TIN Verifier system lookup (if accessible); (iii) cross-reference vendor declared name vs. BIR-registered name; (c) if TIN is invalid or unverifiable: (i) do not proceed with vendor onboarding; (ii) request vendor to provide correct TIN; (iii) if vendor cannot provide valid TIN: decline vendor and document reason | AP Clerk / Tax Accountant | Procurement Manager | 15-30 min per new vendor |
| 2 | **Monthly batch TIN validation**: Tax Accountant runs monthly batch validation: (a) system extracts all active vendor TINs from vendor master per W287; (b) batch validation checks: (i) TIN format compliance (12-digit format); (ii) duplicate TIN detection (two vendors with same TIN may indicate duplicate vendor records or fraud); (iii) TIN vs. vendor name consistency; (iv) VAT registration status match: vendor claiming VAT-registered status has valid VAT TIN; (c) generate exception report: vendors with TIN issues requiring follow-up; (d) target: process all 800-1,000 vendor TINs within 1 business day | Tax Accountant / System | Finance Manager | 2-3 hours/month |
| 3 | **Annual vendor tax compliance review**: Q1 each year, Tax Accountant conducts annual review: (a) request updated tax documents from all active vendors: (i) current BIR Certificate of Registration; (ii) current Mayor's/Business Permit confirming active business registration; (iii) for VAT-registered: current VAT registration certificate; (b) verify vendor tax status changes: (i) vendors who changed from VAT to Non-VAT (affects EWT rate and input VAT claims); (ii) vendors whose business registration has lapsed; (iii) vendors who changed business name or legal structure (affecting TIN); (c) vendors who fail to provide updated documents within 30 days: (i) flag as "Tax Compliance Pending" in vendor master; (ii) AP holds payments until compliance resolved; (iii) Procurement Manager notified for vendor follow-up | Tax Accountant | Finance Manager | 5-8 days/year |
| 4 | **BIR withholding tax compliance verification**: monthly, Tax Accountant verifies vendor WHT compliance: (a) for each vendor payment subject to EWT per W556: (i) verify correct ATC code applied based on vendor's tax registration and nature of payment; (ii) verify EWT rate matches ATC code (1%, 2%, 5%, 10%, etc.); (iii) verify vendor is not on BIR's list of suspended/cancelled TINs; (b) for VAT-registered vendors: verify that purchases are being claimed correctly for input VAT per FIN-006; (c) for Non-VAT vendors: verify that percentage tax or income tax withholding is correctly applied; (d) discrepancies: (i) correct WHT rate in vendor master per W287; (ii) adjust AP processing for affected invoices; (iii) issue corrected Form 2307 per W711 if already filed | Tax Accountant | Finance Manager | 4-6 hours/month |
| 5 | **BIR audit support for vendor tax issues**: during BIR audit per W77: (a) Tax Accountant provides: (i) complete vendor TIN listing with validation results; (ii) Form 2307 issuance log per W711; (iii) EWT remittance reconciliation per W260; (iv) vendor tax document archive; (b) for BIR-disallowed vendor deductions (invalid TIN, unregistered vendor): (i) compute additional tax liability; (ii) recommend settlement or protest strategy with VP Legal; (c) implement corrective measures for identified systemic gaps | Tax Accountant / VP Legal | CFO | 2-3 days per audit |

### System Touchpoints

- Vendor master data per W287 with TIN field validation
- BIR eRegistration/TIN Verifier integration (manual or API)
- AP module per W7 for EWT rate application tied to vendor tax status
- W556 payment run for batch EWT computation verification
- W711 Form 2307 issuance for withholding tax certificate reconciliation
- W260 BIR eFPS filing for EWT remittance cross-reference
- W36 vendor onboarding for initial TIN validation gate
- Document management per W255 for tax document retention (7 years per BIR)

### Pain Points / Risks

- **Vendor TIN inaccuracy**: many small Philippine vendors provide incorrect or incomplete TINs; BIR's TIN verification system is not always accessible or up-to-date, making validation difficult
- **Vendor tax status changes**: vendors may change VAT registration status (register or deregister) without notifying BuildRight, causing incorrect WHT rates until discovered
- **Duplicate vendor records**: multiple vendor master records for the same vendor (with different TIN formats or name variations) cause duplicate TIN detection false positives and complicate reconciliation
- **Informal vendor challenge**: some vendors operate informally without BIR registration; BuildRight cannot legally process payments to unregistered vendors, but Procurement may have already received goods — creating an operational conflict between procurement needs and tax compliance

### Staffing Implication

Tax Accountant: ~15-20 hours/month on vendor tax compliance (2-3 hours batch validation + 4-6 hours WHT verification + ongoing). Annual review: 5-8 days. AP Clerk: absorbed within existing onboarding duties. No incremental headcount.

### Time Estimate

**Per new vendor**: 15-30 min. **Monthly batch**: 2-3 hours. **Monthly WHT verification**: 4-6 hours. **Annual review**: 5-8 days. **BIR audit support**: 2-3 days per audit.

---

## W834. Customer Account Data Deletion & RA 10173 Privacy Compliance Processing

| Field | Detail |
|---|---|
| **Trigger** | Customer submits data deletion request; NPC-ordered data deletion; account deactivation trigger per W560 |
| **Frequency** | Weekly; ~50-100 deletion requests per month |
| **Volume** | ~50-100 requests/month out of ~600,000 loyalty members; increasing trend with privacy awareness |
| **Owner** | Data Protection Officer (DPO) |
| **Participants** | DPO, IT Security Manager, Legal Counsel, CSR, Marketing Manager |

### Background

Philippine Data Privacy Act (RA 10173) and NPC circulars grant data subjects the right to request deletion of personal data. W271 covers data subject access requests but focuses on access and retrieval, not the full deletion lifecycle. Customer data deletion is complex because: (a) transaction data must be retained for 7 years per BIR requirement (NFR-006), (b) loyalty points liability must be settled before deletion per W104, (c) active orders/deliveries must be completed first, (d) data exists across multiple systems (POS, ecommerce, CRM, CDP, marketing, analytics), (e) backups must be addressed, (f) deletion must be documented for NPC audit. This workflow manages the full data deletion lifecycle in compliance with RA 10173 while respecting BIR retention requirements.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Deletion request receipt**: Customer submits deletion request: (a) via customer portal, email to privacy@buildright.com.ph, or in-store at CSR counter per W271; (b) identity verification required (2-factor: loyalty card + registered email OTP, or government ID in-store) | CSR / Customer | DPO | 10-15 min |
| 2 | **Request logging**: DPO receives and logs request in privacy register: (a) request date; (b) customer identity verified; (c) scope of deletion (full account vs. specific data); (d) RA 10173 legal basis assessment | DPO | — | 10-15 min |
| 3 | **Deletion feasibility assessment**: DPO assesses: (a) check active transactions — if pending orders per W11/W19: must complete first; (b) check loyalty points balance — if positive: customer must redeem or forfeit per W570; (c) check outstanding credit balance per W766 — if positive: refund or forfeit per policy; (d) check BIR retention obligations — transaction data (sales, VAT, withholding) must be retained 7 years per NFR-006; (e) check active warranty claims per W821 — must resolve first; (f) check legal holds — if involved in litigation per W125: deletion blocked until resolved | DPO | Legal Counsel | 30 min |
| 4 | **Deletion plan communication**: DPO communicates deletion plan to customer per W708: (a) what will be deleted immediately: personal identifiers, contact details, preferences, marketing profiles, CDP data per W156; (b) what will be retained per legal obligation: anonymized transaction history (BIR 7-year), warranty records during warranty period; (c) customer consent required for partial deletion approach | DPO | — | 15 min |
| 5 | **Data anonymization execution**: if customer accepts plan, DPO authorizes deletion per W152 access lifecycle: (a) anonymize customer record in CRM (replace name/email with "DELETED-[date]-[ticket#]"); (b) remove from marketing databases per W833; (c) remove from CDP per W675; (d) remove from ecommerce account per W659; (e) remove loyalty account per W17 (points forfeited); (f) retain anonymized transaction history per BIR requirement — POS transactions remain for VAT/audit but customer identity stripped | DPO / IT Security Manager | Legal Counsel | 1-2 hours |
| 6 | **Technical deletion execution**: IT Security Manager executes: (a) ERP customer master anonymization; (b) backup rotation — data removed from next backup cycle (note: cannot delete from existing backups immediately; flagged for exclusion on restore); (c) third-party system deletion — notify marketing platforms, CDP vendors, payment gateways per W257 API lifecycle; (d) verify deletion completeness via system query | IT Security Manager | DPO | 1-2 hours |
| 7 | **Deletion confirmation**: DPO confirms deletion completion to customer: (a) deletion certificate issued; (b) confirmation that BIR-mandated anonymized records remain; (c) 30-day window for customer to raise concerns | DPO | — | 15 min |
| 8 | **Monthly privacy compliance report**: (a) deletion requests received vs. completed; (b) average processing time; (c) retention obligation overrides; (d) data breach incidents per W53; (e) NPC registration status per W434 | DPO | VP Legal | 3-4 hours/month |
| 9 | **Annual privacy assessment**: DPO conducts privacy impact assessment per W389 DPIA; submits annual report to NPC per W434 | DPO | VP Legal / CIO | 20-30 hours/year |

### System Touchpoints

- W271 data subject access requests for request intake and identity verification
- W53 data privacy breach for breach incident cross-reference
- W152 IT provisioning for access removal execution
- W17 loyalty operations for loyalty account deletion
- W156 CDP for customer data platform removal
- W675 CDP daily operations for CDP data purge
- W659 ecommerce incidents for ecommerce account deletion
- W104 loyalty financial governance for points liability settlement
- W570 points expiry for loyalty points forfeiture
- W766 credit note aging for outstanding credit resolution
- W821 project warranty for active warranty claim review
- W125 legal cases for legal hold verification
- W255 document storage for deletion certificate archival
- W257 API lifecycle for third-party system deletion coordination
- W389 DPIA for annual privacy impact assessment
- W434 NPC registration for regulatory compliance reporting
- W833 marketing compliance for marketing database removal

### Pain Points / Risks

- **BIR 7-year retention conflict**: customers expect full deletion but BIR requires 7-year retention of transaction data; explaining anonymization vs. deletion to customers is difficult and may generate complaints
- **Data spread across multiple systems**: customer data exists in POS, ecommerce, CRM, CDP, marketing platforms, analytics, backups, and third-party integrations; complete deletion requires coordination across all systems
- **Third-party vendor data deletion**: marketing platforms, CDP vendors, and payment gateways may not comply with deletion requests immediately or at all; BuildRight remains liable under RA 10173
- **Customer dissatisfaction with partial deletion**: customers who expect complete erasure may be unhappy to learn that anonymized transaction records persist for 7 years
- **Deletion verification across all data stores**: confirming that personal data has been removed from every system, including backups and analytics, is technically challenging
- **NPC audit readiness**: deletion processes must be fully documented and auditable for NPC inspection; informal or ad-hoc deletion creates compliance risk

### Staffing Implication

1 DPO (already in headcount per model company profile) + 1 Privacy Analyst; significant time commitment. DPO: ~20-30 hours/month on deletion processing and compliance. Privacy Analyst: ~30-40 hours/month on case management and technical coordination. IT Security Manager: ~5-10 hours/month on technical execution. CSR: absorbed within existing duties for request intake.

### Time Estimate

Per request: assessment (30 min) + customer communication (15 min) + execution coordination (1-2 hours) + verification (15 min) = ~2-3 hours. Monthly: 50-100 requests = 100-300 hours. Annual DPIA: 20-30 hours.
