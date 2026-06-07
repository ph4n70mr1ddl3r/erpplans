# Loss Prevention & Asset Protection Workflows

> Workflows governing retail shrinkage reduction, theft detection, fraud prevention, investigation management, and asset protection across all 200 BuildRight Depot stores and 4 distribution centers. These workflows address internal theft, external theft (shoplifting and organized retail crime), vendor fraud, administrative errors, and cash handling exceptions to maintain the corporate shrinkage target of < 1.5% of net sales.

Back to [Workflow Index](README.md)

---

## Workflows in This Domain

| Workflow | Name | Criticality |
|---|---|---|
| W837 | Daily Store Exception-Based Reporting & Transaction Monitoring | Tier 1 |
| W838 | CCTV & Surveillance System Daily Operations & Incident Review | Tier 1 |
| W839 | Internal Theft Investigation & Employee Dishonesty Case Management | Tier 2 |
| W840 | Organized Retail Crime Detection, Tracking & Task Force Coordination | Tier 2 |
| W841 | Refund & Return Fraud Detection, Investigation & Prevention | Tier 1 |
| W842 | Cash Handling Exception Monitoring & Sweethearting Detection | Tier 1 |
| W843 | Vendor & Delivery Fraud Detection & Dock Security Audit | Tier 2 |
| W844 | Store Entrance/Exit Audit & Electronic Article Surveillance (EAS) Management | Tier 2 |
| W845 | Shrinkage Analysis, Root Cause Investigation & Reduction Program | Tier 2 |
| W846 | Loss Prevention Training, Awareness & Compliance Program | Tier 3 |

---

## W837. Daily Store Exception-Based Reporting & Transaction Monitoring

| Field | Detail |
|---|---|
| **Trigger** | Automated — POS transaction data feed processed nightly; exception alerts generated when thresholds breached |
| **Frequency** | Daily (every store, every operating day) |
| **Volume** | 200 stores × ~15–25 flagged exceptions per store per day = ~3,000–5,000 exception alerts daily chain-wide |
| **Owner** | Loss Prevention Manager (Regional) |
| **Participants** | Store Manager, LP Analyst, POS System Administrator, Finance Controller |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Automated POS data extraction and exception rule engine execution — flag voids, no-sales, excessive discounts, high-value refunds, post-void patterns, and override frequency by cashier | LP Analyst | LP Manager (Regional) | 30 min (automated + validation) |
| 2 | Review prioritized exception dashboard — sort by severity (critical: repeat offenders, high-value anomalies; medium: single threshold breach; low: borderline) | LP Analyst | LP Manager (Regional) | 45 min |
| 3 | Cross-reference flagged transactions against CCTV timestamp log and cashier shift schedule | LP Analyst | Store Manager | 30 min |
| 4 | Escalate critical exceptions (value > PHP 10,000 or repeat pattern ≥ 3 occurrences) to regional LP Manager with evidence package | LP Analyst | LP Manager (Regional) | 15 min |
| 5 | Document non-critical exceptions in case log with disposition (explained, under review, escalated) | LP Analyst | Store Manager | 20 min |
| 6 | Generate daily LP summary report — total exceptions by category, store ranking, trend vs. prior week | LP Analyst | LP Manager (Regional) | 15 min |
| 7 | Store Manager reviews and acknowledges store-level exception summary; provides context for explained items | Store Manager | LP Manager (Regional) | 20 min |

### System Touchpoints
- **POS System** — transaction log extraction, void/refund/override audit trail
- **ERP LP Module** — exception rule engine, alert generation, case management
- **CCTV/DVR System** — timestamp cross-reference via API integration
- **BI Dashboard** — daily LP scorecard, store ranking, trend analysis
- **HR System** — cashier shift schedule, employee ID correlation

### Pain Points / Risks
- Exception rule thresholds may need frequent tuning to reduce false positives without missing genuine incidents
- Manual CCTV cross-referencing is time-intensive; AI-based video analytics not yet deployed
- Store Manager acknowledgment may be delayed during peak trading days
- Data latency between POS close and exception report availability (target: within 4 hours of store close)

### Staffing Implication
- 1 LP Analyst per 40 stores (5 regional LP Analysts chain-wide) + 1 National LP Analytics Lead
- Each analyst handles ~600–1,000 exceptions daily, requiring strong data analysis skills
- Store Managers allocate 20 min daily to exception acknowledgment

### Time Estimate
- Automated processing: 30 min
- Analyst review and disposition: ~2 hours per analyst per day
- Store Manager acknowledgment: 20 min per store per day
- **Total daily effort: ~13 analyst-hours + 200 × 20 min Store Manager time (67 hours) = 80 person-hours chain-wide**

---

## W838. CCTV & Surveillance System Daily Operations & Incident Review

| Field | Detail |
|---|---|
| **Trigger** | Scheduled — daily operations review; ad-hoc triggered by exception report (W837) or incident report |
| **Frequency** | Daily (continuous monitoring during store hours; incident review within 24 hours) |
| **Volume** | 200 stores × average 2–3 incident reviews per day = ~400–600 reviews; 24/7 continuous monitoring at 4 DCs |
| **Owner** | LP Officer (Store-Level) / Security Operations Center (SOC) Lead |
| **Participants** | LP Analyst, Store Manager, IT Security, External Security Agency (contracted) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Verify all store CCTV cameras online and recording — automated health check at store open; flag any offline cameras to IT Security for immediate remediation | IT Security | SOC Lead | 20 min |
| 2 | Monitor real-time camera feeds at SOC for 4 DCs and 10 highest-shrinkage stores (rotating selection monthly) | SOC Operator | SOC Lead | Continuous (shift-based) |
| 3 | Review flagged incidents from exception report (W837) — retrieve footage for timestamp window, document observation, tag for investigation if warranted | LP Analyst | LP Manager (Regional) | 60 min |
| 4 | Conduct spot-check surveillance review — random selection of 5 stores per day for cashier area, entrance/exit, and high-value merchandise zones | LP Analyst | LP Manager (Regional) | 45 min |
| 5 | Archive incident footage per retention policy — 30 days routine, 1 year for active investigation, 7 years for prosecuted cases (aligned with BIR/legal requirements) | LP Analyst | SOC Lead | 15 min |
| 6 | Generate daily CCTV operational status report — camera uptime %, incident captures, response time to offline alerts | SOC Operator | SOC Lead | 15 min |

### System Touchpoints
- **CCTV/DVR/NVR System** — camera health monitoring, footage retrieval, archival
- **ERP LP Module** — incident tagging, case linking, evidence management
- **IT Operations Monitoring** — camera uptime alerts, storage capacity tracking
- **Access Control System** — integration with entrance/exit camera feeds
- **AI Video Analytics Platform** (future) — automated behavior detection, person tracking

### Pain Points / Risks
- Camera uptime target is 98%; actual may be lower in provincial stores with poor connectivity
- Storage capacity for 30-day retention across 200 stores requires ~500 TB
- SOC staffing for 24/7 monitoring is expensive; currently only 4 DCs and 10 stores covered
- Privacy concerns under RA 10173 (Data Privacy Act) — CCTV signage and notice requirements

### Staffing Implication
- SOC: 3 operators × 3 shifts = 9 operators + 1 SOC Lead (national)
- LP Analysts include CCTV review in daily exception workflow (W837)
- IT Security: 1 FTE dedicated to CCTV infrastructure maintenance

### Time Estimate
- Daily health check: 20 min automated
- Incident review: 60 min per analyst per day
- Spot checks: 45 min per analyst per day
- Archival and reporting: 30 min per analyst per day
- **Total daily effort: ~6 analyst-hours + 9 SOC operator shifts**

---

## W839. Internal Theft Investigation & Employee Dishonesty Case Management

| Field | Detail |
|---|---|
| **Trigger** | Exception report pattern (W837), CCTV observation (W838), anonymous tip, or inventory variance threshold breach |
| **Frequency** | As-needed; estimated 5–10 active investigations ongoing at any time chain-wide |
| **Volume** | ~50–80 completed investigations per year; average case duration 2–6 weeks |
| **Owner** | LP Manager (Regional) |
| **Participants** | LP Investigator, HR Manager, Legal Counsel, Store Manager, Finance Controller, Union Representative (if applicable) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Receive and document allegation — source (exception report, tip, CCTV), subject employee(s), initial evidence summary, and estimated loss value | LP Investigator | LP Manager (Regional) | 1 hour |
| 2 | Conduct preliminary assessment — verify exception patterns, review transaction history (30-day lookback), cross-reference with inventory variance data | LP Investigator | LP Manager (Regional) | 4 hours |
| 3 | Determine investigation classification — minor (< PHP 50,000): store-level resolution; major (> PHP 50,000 or management-level subject): regional/national investigation | LP Manager (Regional) | National LP Director | 1 hour |
| 4 | Build evidence package — compile transaction logs, CCTV footage, inventory discrepancy reports, witness statements, and pattern analysis | LP Investigator | LP Manager (Regional) | 8–16 hours (over multiple days) |
| 5 | Conduct integrity interview (with HR witness present) — present evidence, obtain written statement, document admission or denial | LP Investigator | LP Manager (Regional) | 1–3 hours |
| 6 | Determine disciplinary action in consultation with HR and Legal — options range from written warning to termination, criminal complaint, or civil recovery | LP Manager (Regional) | National LP Director | 2 hours |
| 7 | Process recovery — deduct from final pay (within DOLE limits), file insurance claim if applicable, issue demand letter for civil recovery | LP Investigator | Finance Controller | 4 hours |
| 8 | Close case — update case management system, archive evidence per retention policy, generate lessons-learned summary, update exception rules if new pattern identified | LP Investigator | LP Manager (Regional) | 2 hours |

### System Touchpoints
- **ERP LP Module** — case management, evidence linking, workflow tracking
- **POS System** — transaction history extraction for subject employee
- **HR System** — employee record, disciplinary action logging, final pay processing
- **Finance Module** — recovery accounting, civil recovery tracking
- **CCTV System** — evidence extraction, time-locked footage archive
- **Inventory Module** — variance analysis for subject department/category

### Pain Points / Risks
- Integrity interview requires HR witness; scheduling delays can compromise investigation
- DOLE regulations limit salary deduction for recovery (max 1 week per month under Art. 113 LC)
- Criminal complaint process in Philippine courts is slow (6–18 months to resolution)
- Risk of wrongful termination claim if evidence is insufficient — requires Legal sign-off
- Unionized stores may have CBA provisions requiring union representative presence

### Staffing Implication
- 1 LP Investigator per region (5 investigators national) + 1 National LP Director
- Legal Counsel: 0.5 FTE allocated to LP cases
- HR Manager involvement: ~4 hours per case

### Time Estimate
- Average case: 20–35 person-hours over 2–6 weeks
- **Annual estimate: 50–80 cases × 25 hours average = 1,250–2,000 person-hours/year**

---

## W840. Organized Retail Crime Detection, Tracking & Task Force Coordination

| Field | Detail |
|---|---|
| **Trigger** | Pattern recognition — multiple stores hit by similar MO within rolling 30-day window; or external intelligence from law enforcement or industry LP association |
| **Frequency** | As-needed; estimated 3–5 active ORC cases at any time |
| **Volume** | ~10–15 ORC rings identified per year; average loss per ring PHP 500,000–5,000,000 |
| **Owner** | National LP Director |
| **Participants** | LP Manager (Regional), LP Investigator, Legal Counsel, External Law Enforcement (PNP), Store Managers (affected stores), Industry LP Association (ORCA) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Identify ORC pattern — aggregate theft incidents across stores by method-of-operation (MO), merchandise category, vehicle description, or suspect description; threshold: ≥ 3 stores with similar MO in 30 days | LP Analyst | National LP Director | 4 hours |
| 2 | Activate ORC case file — create dedicated case, assign lead investigator, establish secure evidence repository restricted from store-level access | LP Investigator | National LP Director | 2 hours |
| 3 | Coordinate with affected Store Managers — provide awareness briefing (without compromising investigation), deploy targeted surveillance, assign plain-clothes LP during peak risk windows | LP Manager (Regional) | National LP Director | 4 hours |
| 4 | Liaise with external partners — share anonymized intelligence with industry LP association (ORCA), coordinate with PNP if criminal activity threshold met | National LP Director | VP Operations | 2 hours |
| 5 | Execute coordinated surveillance operation — deploy LP resources across multiple stores simultaneously based on predicted target pattern | LP Investigator | National LP Director | 8–40 hours (operation duration) |
| 6 | Apprehension and turnover — coordinate with PNP for in-store apprehension, evidence documentation, blotter filing, and prosecution support | LP Investigator | National LP Director | 4–8 hours |
| 7 | Post-case review — update ORC intelligence database, brief all Store Managers on new MO, enhance preventive controls, close case file | National LP Director | VP Operations | 4 hours |

### System Touchpoints
- **ERP LP Module** — ORC case management, cross-store incident aggregation, MO pattern matching
- **CCTV System** — multi-store footage retrieval and comparison
- **BI Analytics** — geographic heat map of incidents, temporal pattern analysis
- **External Intelligence Platform** — industry LP association data sharing (ORCA Philippines)
- **PNP Coordination System** — blotter, case referral, evidence chain-of-custody

### Pain Points / Risks
- ORC rings often target multiple retailers simultaneously; intelligence sharing with competitors is culturally sensitive
- PNP response time may be slow for non-violent retail theft; private security apprehension has legal limitations
- High-value power tools and construction materials are primary ORC targets — estimated 30% of total shrinkage
- Provincial stores have less LP coverage and are more vulnerable to ORC
- Risk of physical confrontation during apprehension — requires trained security personnel

### Staffing Implication
- National LP Director: 30% of time allocated to ORC
- LP Investigators: 1 dedicated to ORC at national level
- Regional LP Managers: ad-hoc coordination role during active cases

### Time Estimate
- Per case: 50–80 person-hours over 4–12 weeks
- **Annual estimate: 12 cases × 65 hours average = 780 person-hours/year**

---

## W841. Refund & Return Fraud Detection, Investigation & Prevention

| Field | Detail |
|---|---|
| **Trigger** | Exception report flags refund anomalies (W837), or cashier reports suspicious return behavior |
| **Frequency** | Daily monitoring; investigation initiated as needed |
| **Volume** | ~200–300 flagged return anomalies per week chain-wide; ~15–25 confirmed fraud cases per month |
| **Owner** | LP Analyst / LP Manager (Regional) |
| **Participants** | Store Manager, Cashier, Customer Service Supervisor, Finance Controller |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Automated return anomaly detection — flag: returns without receipt exceeding PHP 5,000, same customer returning ≥ 3 times in 7 days, returns of commonly stolen items (power tools, copper wire, adhesives), refunds to different payment method than original purchase | LP Analyst | LP Manager (Regional) | 30 min (automated) |
| 2 | Review flagged returns — verify against original transaction (if receipted), check CCTV for return counter activity, cross-reference customer loyalty ID or government ID captured at return | LP Analyst | Store Manager | 30 min per case |
| 3 | Classify fraud type — receipt fraud (forged/altered receipt), wardrobing (used item return), employee collusion, return-of-stolen-merchandise, or organized return fraud ring | LP Analyst | LP Manager (Regional) | 15 min per case |
| 4 | For confirmed fraud: block customer from future no-receipt returns, recover funds if possible, escalate to investigation if value > PHP 20,000 or ring pattern detected | LP Manager (Regional) | National LP Director | 1 hour |
| 5 | Update return policy rules engine — tighten return window or require manager approval for flagged categories/individuals | LP Analyst | LP Manager (Regional) | 30 min |
| 6 | Generate weekly return fraud summary — trend analysis, top stores, top categories, estimated loss, policy recommendation | LP Analyst | LP Manager (Regional) | 1 hour |

### System Touchpoints
- **POS System** — return transaction log, receipt lookup, customer ID capture
- **ERP LP Module** — fraud detection rules engine, case management, customer flag database
- **CCTV System** — return counter footage, customer identification
- **CRM/Loyalty System** — customer return history, loyalty ID lookup
- **BI Dashboard** — return analytics, fraud trend reporting

### Pain Points / Risks
- Philippine Consumer Act (RA 7394) protects legitimate return rights — policy must not violate consumer protections
- No-receipt returns are a necessary customer service concession but account for ~60% of return fraud
- Forged receipts are increasingly sophisticated — requires POS receipt verification barcode
- Customer confrontation during fraud denial can escalate to social media complaints or DTI filing

### Staffing Implication
- LP Analysts: return fraud review is part of daily exception workflow (~1 hour/day)
- Customer Service Supervisors: trained on fraud indicators and escalation procedure
- 1 FTE dedicated to return fraud analytics at national level

### Time Estimate
- Daily monitoring: 1 hour per analyst
- Weekly summary: 1 hour per analyst
- Investigation: 2–4 hours per confirmed case
- **Annual estimate: ~800 person-hours for detection + ~600 hours for investigation = 1,400 hours/year**

---

## W842. Cash Handling Exception Monitoring & Sweethearting Detection

| Field | Detail |
|---|---|
| **Trigger** | Automated — POS cash variance threshold breach, or sweethearting pattern detected by analytics |
| **Frequency** | Daily monitoring; investigation as needed |
| **Volume** | ~100–150 cash variance alerts per day chain-wide; ~5–10 sweethearting investigations per month |
| **Owner** | LP Analyst / Finance Controller |
| **Participants** | Store Manager, Cashier, HR Manager, LP Investigator |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Automated cash variance monitoring — flag: drawer shortage > PHP 500, drawer overage > PHP 200, repeated small shortages by same cashier (≥ 3 in 5 days), no-sale drawer opens > 5 per shift | LP Analyst | Finance Controller | 30 min (automated) |
| 2 | Sweethearting pattern detection — flag: cashier passes items without scanning, manual price entry below SRP, unauthorized discount application, cancellation of items after customer leaves with merchandise, scanning personal loyalty card for customer purchases | LP Analyst | LP Manager (Regional) | 45 min daily review |
| 3 | Cross-reference cash exceptions with CCTV at POS terminal — verify legitimate explanations (system error, customer dispute, training issue) vs. deliberate manipulation | LP Analyst | Store Manager | 30 min per escalated case |
| 4 | For confirmed sweethearting: compile evidence package, escalate to LP Investigator for integrity interview (per W839 process) | LP Investigator | LP Manager (Regional) | 4–8 hours per case |
| 5 | Cash handling coaching — for non-fraud variances, Store Manager conducts corrective coaching with cashier; document in HR file | Store Manager | LP Manager (Regional) | 30 min per session |
| 6 | Monthly cash variance trend report — store ranking, cashier ranking, trend vs. prior month, root cause analysis for top 10 variance stores | LP Analyst | Finance Controller | 2 hours |

### System Touchpoints
- **POS System** — cash drawer audit trail, transaction detail, void/no-sale logging
- **ERP LP Module** — cash variance tracking, sweethearting analytics, cashier scoring
- **CCTV System** — POS terminal camera feeds with transaction overlay
- **HR System** — disciplinary action tracking, coaching documentation
- **Finance Module** — daily cash reconciliation, variance accounting

### Pain Points / Risks
- Sweethearting is difficult to detect without POS-CCTV transaction overlay technology
- Cashier turnover is high (~30–40% annually in Philippine retail); training investment is lost
- Small cash variances may be dismissed as immaterial but can aggregate to significant losses
- Cultural reluctance to accuse employees of dishonesty without overwhelming evidence
- Cash handling policies must comply with DOLE regulations on salary deductions for shortages

### Staffing Implication
- LP Analysts: cash monitoring is part of daily exception workflow
- Store Managers: cash coaching requires 30 min per session (estimated 10 sessions/month per store)
- Finance Controller: monthly review of chain-wide cash variance

### Time Estimate
- Daily monitoring: 45 min per analyst
- Monthly report: 2 hours per analyst
- Investigation: 4–8 hours per case (60–96 hours/year for 12 cases)
- **Annual estimate: ~1,200 person-hours for monitoring + ~800 hours for coaching and investigation**

---

## W843. Vendor & Delivery Fraud Detection & Dock Security Audit

| Field | Detail |
|---|---|
| **Trigger** | Scheduled dock audits (weekly per store); or triggered by receiving variance exception from WMS |
| **Frequency** | Weekly dock audits per store; continuous monitoring via receiving variance data |
| **Volume** | 200 stores × 1 dock audit/week = ~800 audits/month; ~5–10 vendor fraud cases per year |
| **Owner** | LP Manager (Regional) |
| **Participants** | Store Receiving Clerk, Store Manager, Procurement Specialist, LP Investigator, Vendor Account Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Conduct unannounced dock audit — verify incoming shipment against PO and ASN: unit count, SKU accuracy, weight verification, condition assessment; compare vendor delivery vehicle manifest against system PO | LP Analyst / Store Receiving Clerk | LP Manager (Regional) | 60 min per audit |
| 2 | Review receiving variance data — flag vendors with > 2% quantity variance rate or > PHP 5,000 cumulative variance in rolling 30-day period | LP Analyst | Procurement Manager | 30 min weekly |
| 3 | Identify fraud indicators — short shipment, phantom items (invoiced but not delivered), substitution (lower-grade product), duplicate delivery, or collusion with receiving clerk | LP Investigator | LP Manager (Regional) | 2–4 hours per case |
| 4 | Conduct vendor fraud investigation — compile receiving records, interview receiving clerk, review CCTV of dock area, contact vendor for explanation | LP Investigator | LP Manager (Regional) | 8–16 hours per case |
| 5 | Vendor resolution — issue debit memo for shortage, require vendor corrective action plan, escalate to Procurement for vendor review/suspension if pattern confirmed | Procurement Specialist | Procurement Manager | 4 hours per case |
| 6 | Quarterly dock security assessment — evaluate physical security (locking gates, CCTV coverage, scales calibration), receiving clerk procedures compliance, and vendor credential verification | LP Manager (Regional) | National LP Director | 4 hours per region (quarterly) |

### System Touchpoints
- **WMS/Receiving Module** — PO vs. received quantity variance tracking
- **ERP LP Module** — dock audit checklist, vendor fraud case management
- **Procurement Module** — vendor performance scoring, debit memo processing
- **CCTV System** — dock area camera coverage, receiving activity footage
- **Weighbridge/Scale System** — weight verification for bulk materials

### Pain Points / Risks
- DSD (Direct Store Delivery) vendors have direct dock access — highest fraud risk
- Receiving clerks in provincial stores may have personal relationships with delivery drivers
- Weight verification is impractical for small-item shipments; only viable for bulk materials (cement, steel, lumber)
- Scale calibration drift can cause false positives; quarterly calibration required
- Short-staffed stores may skip receiving verification during peak hours

### Staffing Implication
- LP Analysts: dock audits as part of weekly field visit schedule
- Receiving Clerks: trained on fraud indicators (refresher every 6 months)
- LP Investigator: 1 case at a time; ~5–10 cases/year

### Time Estimate
- Per dock audit: 60 min
- Per investigation: 15–25 hours
- **Annual estimate: ~800 dock audit hours + ~150 investigation hours = 950 person-hours/year**

---

## W844. Store Entrance/Exit Audit & Electronic Article Surveillance (EAS) Management

| Field | Detail |
|---|---|
| **Trigger** | Scheduled — monthly per store; or triggered by EAS alarm frequency spike or shrinkage result |
| **Frequency** | Monthly per store (200 stores = ~200 audits/month); daily EAS alarm response |
| **Volume** | ~200 entrance/exit audits/month; ~500–800 EAS alarm responses per day chain-wide |
| **Owner** | LP Officer (Store-Level) / Security Guard (contracted) |
| **Participants** | Store Manager, LP Analyst, Security Guard Agency Supervisor, IT Security |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | EAS alarm response — security guard approaches customer, requests to verify purchase, checks receipt against bag contents, tags/detags merchandise, logs alarm in incident register | Security Guard | Store Manager | 5 min per alarm |
| 2 | Daily EAS alarm log review — Store Manager reviews incident register; flag repeat alarm locations (may indicate tag deactivation failure), repeat individuals, or alarm-to-apprehension ratio | Store Manager | LP Manager (Regional) | 15 min daily |
| 3 | Monthly entrance/exit audit — verify EAS gate functionality, tag application compliance at checkout, source-tagging compliance for high-risk SKUs, security guard presence and procedure adherence | LP Analyst | LP Manager (Regional) | 60 min per store |
| 4 | EAS tag inventory management — reconcile EAS tag stock (hard tags, soft labels), order replenishment, ensure tag availability at all POS terminals and receiving dock | Store Manager | LP Manager (Regional) | 30 min monthly |
| 5 | Source-tagging compliance verification — confirm vendor-applied EAS labels on high-risk categories (power tools, electrical, plumbing fittings, adhesives) per vendor agreement | LP Analyst | Procurement Manager | 2 hours monthly |
| 6 | Generate monthly EAS effectiveness report — alarm rate, apprehension rate, tag application compliance %, shrinkage correlation by store | LP Analyst | LP Manager (Regional) | 2 hours |

### System Touchpoints
- **EAS System** — gate alarm logging, tag/deactivation counter, system health monitoring
- **POS System** — tag deactivation confirmation at checkout
- **ERP LP Module** — alarm incident register, audit checklist, tag inventory tracking
- **Procurement Module** — source-tagging vendor compliance tracking
- **BI Dashboard** — EAS effectiveness analytics, store comparison

### Pain Points / Risks
- EAS false alarm rate can be high (> 30%) due to tag deactivation failures, causing customer frustration
- Security guard agencies have high turnover (~50% annually); continuous training required
- Source-tagging vendor compliance is inconsistent; some vendors resist cost of tag application
- EAS system maintenance (gate calibration, deactivator pad replacement) requires specialized vendor support
- Cultural sensitivity: customers may feel accused when EAS alarm triggers; staff must handle with courtesy

### Staffing Implication
- Security guards: 2 per store × 200 stores = 400 guards (contracted through agency)
- LP Analysts: monthly audit rotation (each analyst covers ~40 stores)
- 1 FTE EAS System Administrator (national, under IT Operations)

### Time Estimate
- Daily EAS response: 5 min × ~3 alarms/store = 15 min/store/day
- Monthly audit: 60 min per store
- **Annual estimate: ~18,000 alarm response hours + ~400 audit hours + ~200 admin hours = 18,600 person-hours/year**

---

## W845. Shrinkage Analysis, Root Cause Investigation & Reduction Program

| Field | Detail |
|---|---|
| **Trigger** | Monthly inventory count results, quarterly physical inventory, or mid-year shrinkage result exceeding 1.5% target |
| **Frequency** | Monthly analysis; quarterly deep-dive; mid-year and year-end comprehensive review |
| **Volume** | 200 stores × 12 monthly counts = 2,400 count events; 4 DCs × 4 quarterly counts = 16 DC counts |
| **Owner** | National LP Director |
| **Participants** | LP Manager (Regional), LP Analyst, Store Manager, Inventory Manager, Finance Controller, Merchandising Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Compile shrinkage results — aggregate monthly count variance by store, department, category; calculate shrinkage % against net sales; compare to 1.5% target and prior period | LP Analyst | National LP Director | 4 hours |
| 2 | Classify shrinkage by type — known vs. unknown; for known: administrative error, vendor fraud, damage, employee theft, shoplifting; allocate unknown proportionally based on investigation findings | LP Analyst | National LP Director | 2 hours |
| 3 | Root cause analysis for top 20 shrinkage stores — detailed review of LP incidents, cash variances, receiving variances, damage rates, and employee turnover; identify contributing factors | LP Manager (Regional) | National LP Director | 8 hours per store (quarterly) |
| 4 | Identify category-level hot spots — SKU-level analysis for categories exceeding 2% shrinkage (power tools, electrical fittings, adhesives, copper products are typical); trigger targeted LP intervention | LP Analyst | Merchandising Manager | 4 hours |
| 5 | Develop and deploy shrinkage reduction action plans for bottom-quartile stores — LP interventions, staffing adjustments, physical security enhancements, EAS coverage expansion | LP Manager (Regional) | National LP Director | 4 hours per store |
| 6 | Quarterly shrinkage review meeting — present chain-wide results to VP Operations, Merchandising VP, Finance VP; secure budget for reduction initiatives | National LP Director | VP Operations | 2 hours |
| 7 | Track reduction program effectiveness — measure shrinkage delta for stores with active interventions; adjust strategies based on results | LP Analyst | National LP Director | 2 hours monthly |

### System Touchpoints
- **Inventory Module** — cycle count results, variance analysis, shrinkage calculation
- **ERP LP Module** — shrinkage analytics, root cause classification, action plan tracking
- **BI Dashboard** — shrinkage heat map, trend analysis, store/category ranking
- **Finance Module** — shrinkage P&L impact, reserve adjustment
- **Merchandising Module** — category shrinkage analysis, high-risk SKU identification

### Pain Points / Risks
- Monthly cycle count accuracy depends on count discipline — rushed counts produce unreliable data
- Unknown shrinkage category (no identified cause) typically represents 40–60% of total — limits targeted intervention
- Shrinkage reduction programs require capital investment (EAS expansion, CCTV upgrades) with 12–24 month payback
- Provincial stores may under-report shrinkage due to local management pressure on KPIs
- Seasonal patterns (construction season, holiday) distort monthly trends — need year-over-year comparison

### Staffing Implication
- National LP Director: 30% of time on shrinkage analysis and program management
- LP Analysts: 1 FTE dedicated to shrinkage analytics
- Store Managers: accountable for store shrinkage result (KPI component)

### Time Estimate
- Monthly analysis: 8 hours per analyst
- Quarterly deep-dive: 160 hours (8 hours × 20 stores)
- Annual comprehensive review: 40 hours
- **Annual estimate: ~96 hours analysis + ~640 hours deep-dive + ~100 hours program management = 836 person-hours/year**

---

## W846. Loss Prevention Training, Awareness & Compliance Program

| Field | Detail |
|---|---|
| **Trigger** | Scheduled — onboarding (new hire), annual refresher (all store employees), quarterly update (Store Managers and LP-sensitive roles) |
| **Frequency** | Onboarding: per new hire (~200 new hires/month given ~30% annual turnover); Annual refresher: all 4,500+ store employees; Quarterly update: 200 Store Managers + 400 key holders |
| **Volume** | ~2,400 training completions per year (onboarding) + 4,500 annual refresher completions + 800 quarterly update completions |
| **Owner** | LP Training Coordinator / HR Training Manager |
| **Participants** | LP Manager (Regional), Store Manager, New Hire Employee, HR Training Manager, External Training Provider (for specialized topics) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | New hire LP orientation (Day 2 of onboarding) — cover cash handling policy, return/refund procedure, receiving verification, EAS tagging, incident reporting, whistleblower channel, and consequences of theft | Store Manager / HR Training | LP Manager (Regional) | 2 hours per new hire batch |
| 2 | Annual LP refresher training (e-learning + in-store practical) — update on new fraud schemes, policy changes, exception report awareness, and shrinkage results; includes quiz (minimum 80% pass rate) | LP Training Coordinator | National LP Director | 1 hour per employee (e-learning) + 30 min practical |
| 3 | Quarterly LP awareness update for Store Managers — review chain-wide LP metrics, share anonymized case studies, introduce new detection tools or policy changes, set quarterly LP targets | LP Manager (Regional) | National LP Director | 2 hours per session (regional grouping) |
| 4 | Specialized LP training for receiving clerks — vendor fraud indicators, dock security procedures, weight verification, short-shipment detection; certification required before solo receiving shifts | LP Training Coordinator | LP Manager (Regional) | 4 hours per clerk (initial) + 2 hours annual refresh |
| 5 | LP awareness campaign execution — monthly LP tip of the month (digital poster + store huddle talking point), quarterly LP awareness week (in-store displays, reward for LP tips), annual LP excellence awards | LP Training Coordinator | National LP Director | 4 hours monthly |
| 6 | Training effectiveness measurement — track shrinkage correlation with training completion rates, quiz scores, and time-to-incident for new hires; adjust curriculum based on findings | LP Analyst | National LP Director | 4 hours quarterly |

### System Touchpoints
- **LMS (Learning Management System)** — e-learning delivery, quiz administration, completion tracking
- **HR System** — training record, certification status, onboarding checklist
- **ERP LP Module** — shrinkage data for training effectiveness correlation
- **Communication Platform** — digital poster distribution, awareness campaign delivery
- **BI Dashboard** — training completion rates by store, quiz pass rates, correlation analytics

### Pain Points / Risks
- High employee turnover (30–40%) means ~30–40% of trained staff leave within 12 months — continuous retraining required
- E-learning completion rates in provincial stores may be low due to limited computer access
- Training is perceived as non-revenue-generating and may be deprioritized during peak seasons
- Filipino cultural norm of "pakikisama" (getting along) can discourage reporting of colleague theft
- Whistleblower channel awareness is critical but utilization is typically low without trust-building

### Staffing Implication
- 1 FTE LP Training Coordinator (national)
- HR Training Manager: 20% of time allocated to LP training
- Store Managers: 2 hours per new hire batch for LP orientation
- External provider: for annual specialized training (investigation techniques, interview skills)

### Time Estimate
- New hire orientation: 2 hours × 200 batches/year = 400 hours
- Annual refresher: 1.5 hours × 4,500 employees = 6,750 hours (mostly self-service e-learning)
- Quarterly updates: 2 hours × 5 sessions × 4 quarters = 40 hours
- Specialized training: 4 hours × ~100 clerks/year = 400 hours
- **Annual estimate: ~1,000 live instruction hours + 6,750 e-learning hours = 7,750 total hours/year**
