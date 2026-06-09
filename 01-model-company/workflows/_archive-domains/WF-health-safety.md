# Health, Safety & Environment (HSE) Workflows

> Management of occupational health and safety (OHS), incident reporting, safety compliance, annual statutory reporting, and safety training & certification tracking.
>
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W140. Occupational Health & Safety (OHS) Incident Management](#w140-occupational-health-safety-ohs-incident-management)
- [W141. Workplace Safety Inspection & Audit](#w141-workplace-safety-inspection-audit)
- [W187. Contractor & Third-Party On-site Safety Orientation](#w187-contractor-third-party-on-site-safety-orientation)
- [W436. Annual OHS Statutory Reporting (WAIR/AMR)](#w436-annual-ohs-statutory-reporting-wairamr)
- [W655. Safety Training & Certification Tracking](#w655-safety-training--certification-tracking)
- [W695. Emergency Response & Evacuation Protocol Management](#w695-emergency-response-evacuation-protocol-management)
- [W696. Contractor & Visitor Safety Induction & Access Control](#w696-contractor-visitor-safety-induction-access-control)
- [W697. Workplace Ergonomics Assessment & Musculoskeletal Injury Prevention](#w697-workplace-ergonomics-assessment-musculoskeletal-injury-prevention)
- [W804. Occupational Health Surveillance, Employee Medical Monitoring & Record Management](#w804-occupational-health-surveillance-employee-medical-monitoring--record-management)
- [W805. Workers' Compensation, SSS/ECC Claims & Return-to-Work Processing](#w805-workers-compensation-sssecc-claims--return-to-work-processing)
- [W806. Annual Fire Safety System Testing, Certification & BFP Compliance](#w806-annual-fire-safety-system-testing-certification--bfp-compliance)

---

## W140. Occupational Health & Safety (OHS) Incident Management

| Field | Detail |
|---|---|
| **Trigger** | Workplace accident, "near miss," or safety hazard reported (involving employee, customer, or contractor) |
| **Frequency** | Ad-hoc; ~50–100 reportable incidents/year chain-wide |
| **Volume** | Covers all 200 stores, 4 DCs, and HQ |
| **Owner** | Safety Officer (HQ/DC); Store Manager (Store) |
| **Participants** | Affected Individual, First Aider, Store/DC Manager, HR, Legal, Insurance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Emergency Response**: Immediate first aid or medical evacuation; secure the scene to prevent further injury | First Aider / Manager | Store Manager | Immediate |
| 2 | **Incident Reporting**: Manager creates Incident Report in system within 2 hours: date/time, location, individuals involved, description of event, and immediate actions taken | Store/DC Manager | Safety Officer | 20 min |
| 3 | **Evidence Capture**: Upload photos of the scene, witness statements, and CCTV footage to the incident record | Store/DC Manager | — | 30 min |
| 4 | **Investigation**: Safety Officer conducts root cause analysis (e.g., "5 Whys"); classifies incident (Minor, Medical Treatment, Lost Time Injury, Fatality) | Safety Officer | VP HR | 1–3 days |
| 5 | **Corrective Action (CAPA)**: System generates CAPA tasks (e.g., repair floor, replace PPE, retraining); tracks completion | Safety Officer | Dept Head | Varies |
| 6 | **Regulatory Notification**: If required (e.g., serious injury), DPO/Safety Officer notifies DOLE (Department of Labor and Employment) within prescribed timelines | Safety Officer | Legal Head | 4 hours |
| 7 | **Insurance/Claims**: If involving customer injury or significant property damage, initiate insurance claim per W3.6a | Store Manager / Finance | CFO | Per W3.6a |
| 8 | **Closure**: Review all actions completed; Safety Officer closes the case; system archives for 10 years | Safety Officer | VP HR | 15 min |
| 9 | **Monthly Review**: Monthly Safety Committee meeting reviews incident trends, "near miss" patterns, and CAPA completion rates | Safety Committee | CEO | 2 hours/month |

### System Touchpoints
- Incident Reporting Module with photo/evidence upload and witness statement capture (Step 2–3)
- CAPA Task Tracking System with automated reminders and escalation for overdue corrective actions (Step 5)
- DOLE Notification Workflow Integration — auto-generates DOLE-compliant report forms within prescribed timelines (Step 6)
- Insurance Claims Integration linked to W59/W185 for customer injury and property damage claims (Step 7)
- Safety Compliance Dashboard showing incident trends, near-miss patterns, and CAPA completion rates by location/region (Step 9)
- CCTV Footage Retrieval System — time-stamped clip extraction linked to incident record (Step 3)
- 10-year digital archiving with legal-hold capability for regulatory audit (Step 8)

### Pain Points / Risks
- **DOLE Department Order 198-18** — full compliance with the OSH Standards requires documented risk assessments, safety committees, and qualified safety officers per establishment
- **DOLE reporting timelines** — 24 hours for fatalities, 48 hours for serious injuries; late filing triggers penalties and potential work stoppage orders
- **PhilHealth ECC claims** — work-related injuries require Employees' Compensation Commission processing; incomplete incident documentation delays claims
- **RA 11058 (OSH Standards compliance)** — mandates employer-provided PPE, safety training, and worker participation; non-compliance carries fines per violation
- **Contractor non-compliance risk** — unaccredited or uninsured workers on-site expose the company to joint liability (see W187)
- **Permit-to-Work enforcement** — hot work, confined space, and height work permits must be issued per task; lapses create regulatory and safety exposure
- **Fire Safety Inspection Certificate (FSIC)** — required from Bureau of Fire Protection (BFP) per location; expired FSIC blocks business permit renewal

### Staffing Implication
- ~50–100 reportable incidents/year chain-wide across 200 stores, 4 DCs, and HQ
- Each incident: ~20 min for initial reporting (Step 2) + 1–3 days investigation (Step 4) + varies for CAPA completion (Step 5)
- 1 Safety Officer per region (~10–12 Safety Officers total); investigation time absorbed into existing responsibilities
- No incremental headcount required; workload peaks are managed through regional rotation and HQ Safety Committee support

### Time Estimate
| Phase | Duration |
|---|---|
| Emergency Response & Reporting | 2–3 hours (includes 2-hour reporting SLA) |
| Evidence Capture & CCTV Retrieval | 30 min – 1 hour |
| Investigation & Root Cause Analysis | 1–3 business days |
| CAPA Implementation | Varies (hours to weeks depending on severity) |
| Regulatory Notification (if applicable) | 4 hours |
| Case Closure & Archiving | 15 min |
| **Total (typical non-fatal incident)** | **3–5 business days** |

---

## W141. Workplace Safety Inspection & Audit

| Field | Detail |
|---|---|
| **Trigger** | Scheduled monthly inspection; or pre-opening checklist for new store |
| **Frequency** | Monthly per location |
| **Volume** | ~204 inspections/month |
| **Owner** | Safety Officer |
| **Participants** | Store/DC Manager, Maintenance, external fire/safety inspectors |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Inspection Prep**: System generates monthly inspection checklist for the location (tailored for Store vs. DC) | System | Safety Officer | Automated |
| 2 | **Walkthrough**: Manager/Safety Officer conducts physical inspection: fire exits clear, fire extinguishers charged, racking integrity (DC), spill kits stocked, PPE usage, electrical safety | Store/DC Manager | Safety Officer | 1–2 hours |
| 3 | **Findings Logging**: Record "Pass/Fail" for each item; capture photos of any non-compliance | Store/DC Manager | — | 30 min |
| 4 | **Immediate Fixes**: Resolve low-risk items immediately (e.g., move a box blocking an exit); log as "Corrected on Site" | Store/DC Manager | — | Ongoing |
| 5 | **Maintenance Request**: For structural/equipment issues, auto-generate Work Order in Facilities Mgmt system (W47) | System | Maintenance | Automated |
| 6 | **Certification Tracking**: System tracks expiry of mandatory certifications: Fire Safety Inspection Certificate (FSIC), Elevator/Escalator permits, Forklift operator licenses | Safety Officer | Regulatory Officer | 15 min/month |
| 7 | **Dashboard**: Safety Officer reviews "Safety Compliance Score" per region/location; flags high-risk locations for unannounced audit | Safety Officer | VP Store Ops | 1 hour/month |

### System Touchpoints
- Mobile-friendly Safety Inspection App with photo/GPS capture
- Automated integration with Facilities Maintenance (W47) for repairs
- Compliance calendar with automated alerts for permit/license expiries
- Incident analytics dashboard for trend reporting

### Pain Points / Risks
- **DOLE Department Order 198-18** — monthly inspections must satisfy OSH Standards documentation requirements
- **FSIC from BFP** — expired Fire Safety Inspection Certificate blocks business permit renewal; tracking across 204 locations is error-prone without automated alerts
- **Permit/license expiry management** — forklift operator licenses, elevator/escalator permits, and fire extinguisher certifications can lapse without system-driven reminders
- **Inspector consistency** — subjective pass/fail criteria across 200+ locations may produce inconsistent findings; requires standardized checklists
- **RA 11058 compliance** — safety officers must be DOLE-accredited; stores lacking accredited officers cannot legally certify inspections

### Staffing Implication
- Monthly per location × ~204 locations (200 stores, 4 DCs) = ~204 inspections/month
- 1–2 hours per inspection (walkthrough + findings logging); completed by Store/DC Managers as part of regular operational duties
- Safety Officers review dashboards and flag high-risk locations (~1 hour/month regional review)
- No incremental headcount required; absorbed into existing Store Manager and Safety Officer responsibilities

### Time Estimate
| Phase | Duration |
|---|---|
| Checklist Generation (System) | Automated |
| Physical Walkthrough | 1–2 hours |
| Findings Logging & Photo Capture | 30 min |
| Immediate Fixes | Ongoing during walkthrough |
| Dashboard Review (Regional) | 1 hour/month |
| **Total per Location per Month** | **~2–3 hours** |

---

## W187. Contractor & Third-Party On-site Safety Orientation

| Field | Detail |
|---|---|
| **Trigger** | Contractor or 3rd party arriving to perform work (maintenance, construction, cleaning) |
| **Frequency** | As occurred |
| **Volume** | ~500–1,000 orientations/month chain-wide |
| **Owner** | Store Manager / DC Manager |
| **Participants** | Contractor Supervisor, Safety Officer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Contractor signs in at Security/Receiving; presents work order and valid ID | Security | — | 10 min |
| 2 | Manager/Safety Officer verifies Contractor Insurance & Accreditation (W62) | Manager | — | 5 min |
| 3 | Contractor undergoes "Safety Briefing": fire exits, PPE requirements, hazardous areas, emergency contacts | Manager | Safety Officer | 20 min |
| 4 | Contractor signs digital "Safety Acknowledgement" and "Permit to Work" (for hot work, height work, or confined space) | Contractor | Manager | 10 min |
| 5 | Security issues "Contractor Badge"; logs entry time in ERP | Security | — | 5 min |
| 6 | Periodic monitoring: Safety Officer checks contractor compliance during the shift | Safety Officer | — | Ongoing |
| 7 | Completion: Contractor signs out; Security logs exit time; Badge returned | Security | — | 5 min |

### System Touchpoints
- Contractor Management Module with Accreditation status (W187.2)
- Digital Safety Induction & Permit-to-Work Portal (W187.4)
- Visitor/Contractor Log integrated with ERP Access Control (W187.5)

### Pain Points / Risks
- **Contractor non-compliance risk** — unaccredited or uninsured workers on-site expose BuildRight Depot to joint liability under DOLE regulations
- **Permit-to-Work enforcement** — hot work, confined space, and height work permits must be issued per task per contractor; manual processes increase skip-rate
- **RA 11058 (OSH Standards compliance)** — third-party workers must receive safety orientation; failure to document exposes the company to fines
- **DOLE Department Order 198-18** — contractor safety briefing records must be retained and producible upon inspection
- **Insurance gaps** — contractor insurance verification (Step 2) must catch expired or insufficient coverage before work commences; lapses create liability exposure
- **BFP Fire Safety compliance** — contractors performing hot work must have additional fire safety clearance tied to FSIC requirements

### Staffing Implication
- ~500–1,000 orientations/month chain-wide (varies by season and project volume)
- ~45 min per orientation (sign-in + verification + briefing + Permit-to-Work + badge issuance)
- Absorbed by Store Managers and Safety Officers as part of receiving and site-management duties
- No incremental headcount required; peak periods (store renovations, seasonal buildouts) managed through scheduling coordination

### Time Estimate
| Phase | Duration |
|---|---|
| Sign-In & ID Verification | 10 min |
| Insurance & Accreditation Check | 5 min |
| Safety Briefing | 20 min |
| Safety Acknowledgement & Permit-to-Work | 10 min |
| Badge Issuance & ERP Log | 5 min |
| Sign-Out & Badge Return | 5 min |
| **Total per Contractor** | **~45–55 min** |


---

## W436. Annual OHS Statutory Reporting (WAIR/AMR)

| Field | Detail |
|---|---|
| **Trigger** | Annual statutory deadline (typically January/February) |
| **Frequency** | Annual |
| **Volume** | 200 Stores + 4 DCs + 1 HQ |
| **Owner** | Safety Officer |
| **Participants** | HR Manager, Company Physician/Nurse, Store Managers, DOLE |

### Background

The **Department of Labor and Employment (DOLE)** mandates the submission of annual safety reports under the **Occupational Health and Safety (OHS) Standards**. Key reports include the **Work Accident/Illness Report (WAIR)**, the **Annual Medical Report (AMR)**, and the **Report on Safety Organization (RSO)**.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Data Consolidation**: Aggregates all workplace incident records (W140) and safety inspection findings (W141) for the calendar year | Safety Officer | — | 3 days |
| 2 | **Medical Data**: Company Nurse consolidates employee health records, clinic consultations, and annual physical exam (APE) results for the AMR | Company Nurse | HR Manager | 2 days |
| 3 | **Report Drafting**: Safety Officer prepares the WAIR and RSO; Physician prepares the AMR | Safety Officer / Physician | VP HR | 1 day |
| 4 | **Review & Signing**: Store Managers sign the branch-specific reports; Safety Officer and Physician sign the technical sections | Safety Officer / Physician | Store Manager | 1 hour/loc |
| 5 | **Online/Manual Submission**: Submit the consolidated reports to the DOLE Regional Office or via the DOLE Establishment Report System (ERS) | Safety Officer | — | 4 hours |
| 6 | **Acknowledgement**: System archives the "Received" copy of the reports for future DOLE inspections | System | Safety Officer | 15 min |

### System Touchpoints
- Incident Management Module (W140)
- Employee Health Record (HRIS integration)
- DOLE Online Reporting Portal (External)
- Document Management System (W255)

### Pain Points / Risks
- **Non-Compliance Fines**: Failure to submit annual OHS reports leads to fines and increased likelihood of a comprehensive DOLE labor inspection.
- **Data Integrity**: Inconsistencies between the monthly incident logs and the annual summary reports.

---

## W655. Safety Training & Certification Tracking

| Field | Detail |
|---|---|
| **Trigger** | New hire onboarding (W15); annual recertification cycle; triggered by regulatory change or incident |
| **Frequency** | Continuous enrollment; monthly tracking; annual compliance audit |
| **Volume** | 6,715 employees requiring various safety certifications across 200 stores, 4 DCs, and HQ |
| **Owner** | Safety Training Coordinator |
| **Participants** | Department Supervisors, DC Safety Officer, External Training Provider, DOLE-Accredited Safety Practitioner |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Safety Training Coordinator maintains certification requirement matrix by role and location: forklift operators (DC — initial + 3-year renewal), first aiders (all locations — 2-year renewal per Red Cross), fire extinguisher operation (all employees — annual), electrical safety (maintenance staff — annual), working at heights (maintenance/yard — annual), hazmat handling (paint/chemical areas — annual per W237), ladder safety (store associates — annual), manual handling (all store and DC — annual), defensive driving (drivers — annual per W654) | Safety Training Coordinator | Safety Officer | Ongoing maintenance |
| 2 | Monthly: System auto-generates certification status dashboard: certified, expiring within 30 days, expired, untrained — by role, location, and certification type | System | Safety Training Coordinator | Automated |
| 3 | Safety Training Coordinator schedules training sessions for expiring certifications: in-house sessions for common certifications (fire extinguisher, manual handling, ladder safety); external provider sessions for specialized certifications (first aid/CPR, forklift, working at heights); coordinates with Department Supervisors for employee availability | Safety Training Coordinator | Safety Officer | 4 hours/month scheduling |
| 4 | Training facilitator conducts training session; documents attendance with sign-in sheet; administers written and/or practical assessment; records pass/fail in system | Training Facilitator | Safety Training Coordinator | Varies by course |
| 5 | For failed assessments: Safety Training Coordinator schedules remedial training within 14 days; employee restricted from associated task until recertified (e.g., forklift operator restricted from forklift operation) | Safety Training Coordinator | Department Supervisor | 14 days |
| 6 | Quarterly: Safety Training Coordinator produces compliance report: certification compliance rate by location (target: ≥ 95%), training hours per employee, gap analysis by location, cost per certification; reports to Safety Officer and CHRO | Safety Training Coordinator | Safety Officer | 1 day/quarter |
| 7 | Annual: DOLE-accredited Safety Practitioner audits certification compliance across all locations during workplace safety inspection (W141); findings feed into OHS statutory report (W436) | Safety Practitioner | Safety Officer | During W141 |

### System Touchpoints
- Training management module, employee master (W292), certification database, scheduling module, compliance reporting

### Time Estimate
- Monthly scheduling: 4 hours; quarterly reporting: 1 day; annual audit: during W141

### Pain Points / Risks
- High employee turnover (15–20%) continuously creating untrained new hires; training scheduling conflicts with operational needs (store coverage, DC throughput); geographic dispersal across Philippine archipelago making in-person training expensive; inconsistent external training provider quality; DOLE inspection finding expired certifications resulting in penalties

### Staffing Implication
- **Safety Training Coordinator** (1 FTE at HQ): ~4 hours/month on scheduling + 1 day/quarter on reporting + ongoing maintenance of certification matrix. Dedicated training coordination role within HSE department.
- **External Training Providers**: contracted for specialized certifications (first aid, forklift, working at heights). Variable cost based on number of trainees per session.

---

## W695. Emergency Response & Evacuation Protocol Management

| Field | Detail |
|---|---|
| **Trigger** | Annual drill schedule; post-incident protocol update; new store opening; regulatory requirement (BFP fire safety inspection) |
| **Frequency** | Semi-annual evacuation drills; quarterly protocol review; continuous protocol maintenance |
| **Volume** | 200 stores, 4 DCs, HQ — each requiring location-specific emergency response plans; ~205 emergency response protocols maintained |
| **Owner** | Safety Officer |
| **Participants** | Store Managers, DC Managers, HR, VP Operations, Local Emergency Services (BFP, barangay), External Safety Consultant |

### Background

BuildRight operates 200 stores and 4 DCs across the Philippine archipelago, exposed to multiple emergency scenarios: earthquakes (Philippine fault zone, Mindanao earthquakes), typhoons (average 20 typhoons/year per PAGASA), fires (BFP-reported commercial fire incidents), flooding (especially during monsoon season), and workplace violence/robbery incidents. DOLE requires documented emergency response plans for all workplaces with >10 employees, and BFP requires semi-annual fire drills as a condition of Fire Safety Inspection Certificate (FSIC) renewal. This workflow manages the lifecycle of emergency response protocols across all locations.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Location-specific emergency plan development**: Safety Officer develops emergency response plan template covering: (a) fire evacuation routes and assembly points; (b) earthquake duck-cover-hold procedure and post-earthquake building assessment; (c) typhoon/flood response (sandbagging, stock elevation, early closure decision per W576); (d) hazmat spill containment per W238; (e) active threat/robbery response protocol; (f) medical emergency response (first aid, AED use, ambulance coordination); (g) bomb threat procedure; (h) power failure response per W470; each plan customized to location layout, staffing, and local emergency service contacts (nearest fire station, hospital, police station, barangay disaster coordinator) | Safety Officer | VP Operations | 1-2 days per new location |
| 2 | **Emergency team appointment**: for each location, Store/DC Manager appoints emergency response team: (a) Floor Wardens (per department/zone — guide evacuation); (b) Assembly Point Coordinator (headcount at assembly area); (c) First Aid Responders (trained per W655 first aid certification); (d) Fire Marshal (fire extinguisher and suppression system operation); (e) Communication Officer (contacts emergency services and HQ); post appointments in system with contact details; update when personnel change | Store/DC Manager | Safety Officer | 2 hours per location; updated as needed |
| 3 | **Semi-annual evacuation drill**: per BFP requirement: (a) Safety Officer schedules drill calendar (avoid peak business hours; alternate between announced and unannounced); (b) conduct drill: activate alarm, execute evacuation, assembly point headcount, all-clear and re-entry; (c) drill evaluation: evacuation time (target <5 minutes for full store evacuation), headcount accuracy (target 100%), identified bottlenecks (blocked exits, malfunctioning alarms); (d) document drill in system with photos, evaluation scores, and corrective actions | Safety Officer / Store Manager | VP Operations | 2-3 hours per drill per location |
| 4 | **Post-drill corrective action**: for any deficiencies identified during drill: (a) blocked or obstructed emergency exits → clear immediately, install monitoring signage; (b) malfunctioning fire alarms or emergency lighting → maintenance request per W188 with emergency priority; (c) emergency team members absent or untrained → schedule makeup training per W655; (d) evacuation time exceeds target → investigate bottleneck and modify floor plan or routing | Store Manager | Safety Officer | 1-5 days per corrective action |
| 5 | **Protocol update trigger**: update emergency response plans when: (a) post-incident review identifies protocol gaps (after any actual emergency event); (b) store layout changes (renovation, new department, fixture rearrangement); (c) new regulatory requirements (BFP, DOLE circulars); (d) new store opening per W702; (e) semi-annual drill identifies needed changes; (f) annual plan review | Safety Officer | VP Operations | 2-4 hours per update |
| 6 | **Emergency communication system testing**: quarterly, IT tests emergency communication cascade: (a) mass notification to all 200 stores via SMS, email, and mobile app; (b) verify message delivery rate (target >95% within 5 minutes); (c) test two-way communication (store confirms receipt and reports status); (d) integrate with W685 BC plan communication protocols | IT Operations | Safety Officer | 2 hours/quarter |
| 7 | **Annual emergency preparedness audit**: Safety Officer conducts annual audit per W141 framework: (a) verify all locations have current emergency response plans on file; (b) verify drill completion (2 drills/year per BFP requirement); (c) verify emergency equipment inspection (fire extinguishers monthly per BFP, AED battery check, first aid kit replenishment); (d) verify emergency team appointments are current; (e) compile audit report for VP Operations and CHRO | Safety Officer | VP Operations | 1-2 weeks |

### System Touchpoints

- Emergency response plan document management per W255
- Drill scheduling and documentation module
- Emergency communication system (mass notification, two-way status reporting)
- Maintenance request integration per W188
- Training management integration per W655
- BC plan integration per W685
- BFP compliance calendar per W506
- Location master data (floor plans, exits, assembly points)

### Pain Points / Risks

- **Drill fatigue and complacency**: 200 stores conducting semi-annual drills creates logistical burden; store staff may treat drills as routine without genuine engagement
- **Multi-floor and multi-exit complexity**: larger BuildRight stores may have complex layouts with multiple exits, loading docks, and mezzanine levels requiring detailed evacuation planning
- **Barangay coordination**: emergency response in the Philippines relies heavily on barangay (local village) disaster risk reduction councils; BuildRight stores must coordinate with local barangay officials who have varying levels of disaster preparedness
- **Night shift coverage**: DCs operating night shifts have reduced staffing and may lack trained emergency team members during low-attendance periods
- **Post-disaster protocol execution**: after a major typhoon or earthquake, standard evacuation protocols may be insufficient (building structural damage, flooded roads, overwhelmed local emergency services)

### Staffing Implication

- **Safety Officer**: ~4-6 hours/month on drill coordination and protocol maintenance. Absorbed within existing role.
- **Store/DC Managers**: ~2-3 hours/drill (2 drills/year) + 2 hours/year on protocol review. Absorbed within existing role.
- **IT Operations**: ~2 hours/quarter on communication system testing. Absorbed within existing role.
- **No incremental headcount**.

### Time Estimate

- Plan development (new location): 1-2 days
- Semi-annual drill: 2-3 hours per location per drill
- Post-drill corrective action: 1-5 days
- Annual audit: 1-2 weeks
- Communication system test: 2 hours/quarter

---

## W696. Contractor & Visitor Safety Induction & Access Control

| Field | Detail |
|---|---|
| **Trigger** | Contractor arrives at BuildRight location for work; vendor representative visits for meeting; government inspector arrives for inspection per W658; delivery driver not on approved list; job applicant or visitor enters operational area |
| **Frequency** | Continuous (~100-200 contractor/visitor entries/day across all locations) |
| **Volume** | ~25,000-50,000 contractor/visitor entries/year; major contractors: construction/renovation crews, IT installers, maintenance technicians, cleaning services, vendor merchandisers |
| **Owner** | Store/DC Manager (location-level); Facilities Manager (HQ) |
| **Participants** | Security Guard, Contractor/Vendor, Safety Officer, Department Supervisor |

### Background

BuildRight's 200 stores, 4 DCs, and HQ receive continuous visits from contractors, vendors, government inspectors, and other third parties. W187 covers general contractor safety orientation, but this workflow addresses the day-to-day operational process of inducting and controlling access for all non-employee visitors to BuildRight locations — including verifying safety qualifications, issuing access credentials, monitoring activities, and ensuring proper checkout. DOLE requires that employers ensure workplace safety for all persons on premises, including contractors and visitors.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Pre-arrival registration**: for planned contractor/vendor visits: (a) host department registers visitor/contractor in system: name, company, purpose, expected duration, areas to access, host employee; (b) for contractors performing physical work: system verifies contractor has valid safety orientation record per W187 and required certifications per W655 (e.g., working at heights, electrical safety); (c) system generates visitor/contractor pass with access level: General (office/retail areas only), Operational (warehouse/DC floor with escort), Restricted (requires Safety Officer escort + specific permit) | Department Supervisor | Store/DC Manager | 10-15 min |
| 2 | **Arrival check-in**: Security Guard verifies: (a) visitor/contractor identity (government ID); (b) matches pre-registration or registers walk-in visitor; (c) issues color-coded visitor badge with photo, access level, and expiry time; (d) for contractors: verify PPE compliance (hard hat, safety shoes, high-visibility vest per W187 requirements); (e) for government inspectors: follow W658 inspection response protocol; (f) captures entry timestamp in visitor log | Security Guard | Store/DC Manager | 5-10 min |
| 3 | **Safety briefing**: for visitors entering operational areas (DC floor, construction zones, maintenance areas): (a) Security Guard or designated staff provides 5-minute safety briefing: emergency exits, assembly point, restricted areas, PPE requirements, prohibited activities (photography without authorization per data privacy); (b) for contractors performing work: review specific hazards in work area (e.g., forklift traffic in DC, electrical hazards, overhead work); (c) visitor/contractor signs safety acknowledgment | Security Guard / Safety Officer | Store/DC Manager | 5-10 min |
| 4 | **Activity monitoring**: during visit/contractor work: (a) host employee or designated escort monitors visitor/contractor compliance with safety rules; (b) for extended contractor work (>1 day): daily check-in with contractor supervisor to confirm safety compliance; (c) Security Guard conducts periodic checks on contractors in restricted areas; (d) any safety violation: Security Guard or Safety Officer issues verbal warning, then written warning, then removal from premises for repeated violations | Host Employee / Security Guard | Store/DC Manager | Ongoing during visit |
| 5 | **Incident handling**: if visitor/contractor is involved in any safety incident: (a) respond per W140 incident management protocol; (b) provide first aid if needed; (c) document incident in visitor/contractor incident log; (d) notify contractor's employer per contractual obligation; (e) for serious incidents: DOLE reporting per W436 may apply | Safety Officer | Store/DC Manager | Per W140 |
| 6 | **Checkout & badge return**: upon departure: (a) visitor/contractor returns badge to Security Guard; (b) Security Guard records exit timestamp; (c) host confirms work completion (for contractors); (d) for contractors: system records work completion for contractor performance tracking; (e) visitor log entry closed | Security Guard | Store/DC Manager | 5 min |
| 7 | **Monthly access compliance reporting**: Security Guard team lead compiles monthly report: total entries by category (contractor, vendor, visitor, inspector), safety briefing completion rate, PPE compliance rate, incident count, average visit duration; report shared with Safety Officer and Store/DC Manager | Security Team Lead | Safety Officer | 2 hours/month |

### System Touchpoints

- Visitor/contractor management module (registration, badge printing, log)
- Contractor safety orientation record per W187
- Certification verification per W655
- Security guard post management system
- Incident management integration per W140
- W658 government inspection response integration
- Data privacy compliance for visitor PII per RA 10173

### Pain Points / Risks

- **Walk-in contractor management**: emergency repairs (plumbing leak, electrical fault) require immediate contractor access without pre-registration; expedited safety briefing and PPE verification needed
- **Badge sharing and tailgating**: contractors or visitors sharing badges or following authorized personnel through access points without check-in
- **Visitor PII data privacy**: visitor logs containing names, ID numbers, and photos are subject to RA 10173; must be stored securely and retained only as long as legally required per W256
- **Language barriers**: foreign contractor specialists (e.g., equipment vendors from Japan, Germany) may not understand safety briefings in English or Filipino; translated materials or interpreters needed
- **Government inspector access**: cannot deny entry to authorized government inspectors; must balance safety compliance with cooperative regulatory relationship per W658

### Staffing Implication

- **Security Guards**: ~10-15 min per visitor/contractor for check-in/out. Absorbed within existing security staffing (~2-4 guards per location).
- **Store/DC Manager**: ~15-30 min/day on contractor coordination. Absorbed within existing role.
- **Safety Officer**: ~4-6 hours/month on monthly reporting and incident follow-up. Absorbed within existing role.
- **No incremental headcount**.

### Time Estimate

- Pre-registration: 10-15 min per planned visit
- Check-in: 5-10 min per visitor/contractor
- Safety briefing: 5-10 min per visitor to operational areas
- Activity monitoring: ongoing during work
- Checkout: 5 min per visitor/contractor
- Monthly reporting: 2 hours

---

## W697. Workplace Ergonomics Assessment & Musculoskeletal Injury Prevention

| Field | Detail |
|---|---|
| **Trigger** | Employee reports musculoskeletal discomfort; quarterly assessment cycle; new workstation or work process introduction; post-injury return-to-work |
| **Frequency** | Quarterly workstation assessments; continuous for reported discomfort; annual program review |
| **Volume** | ~6,715 employees across 200 stores, 4 DCs, and HQ; high-risk roles: cashiers (prolonged standing, repetitive scanning), DC pickers (lifting, bending), lumber yard staff (heavy lifting), paint mixing staff (repetitive arm motion) |
| **Owner** | Safety Officer |
| **Participants** | HR (employee health records), Department Supervisors, External Ergonomics Consultant, Occupational Health Provider, Store/DC Managers |

### Background

Retail hardware operations involve physically demanding tasks: lifting heavy building materials (cement bags 40kg, lumber, steel bars), repetitive scanning at POS terminals, prolonged standing for cashiers and sales associates, and repetitive motion for paint mixing and lumber cutting operations. The Philippine DOLE Department Order No. 197-18 requires employers to implement occupational safety and health programs including ergonomics. Musculoskeletal disorders (MSDs) are among the most common workplace injuries in retail, leading to lost workdays, workers' compensation claims, and reduced productivity.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Risk identification by role**: Safety Officer classifies all roles by ergonomic risk level: (a) **High risk**: DC pickers/packers (lifting >20kg repeatedly, bending, twisting), lumber yard staff (lifting long/heavy materials), paint mixing operators (repetitive arm motion, chemical exposure); (b) **Medium risk**: cashiers (prolonged standing, repetitive scanning, awkward postures for bagging heavy items), receiving clerks (unloading delivery trucks); (c) **Low risk**: office staff (prolonged sitting, computer use), sales associates (standing, walking); (d) document risk assessment per role with specific hazard identification | Safety Officer | VP HR | 1-2 days initial; updated annually |
| 2 | **Quarterly workstation assessment**: for high and medium risk roles: (a) Department Supervisor conducts quarterly self-assessment using ergonomic checklist: workstation height, reach distances, lifting requirements, posture, break frequency; (b) for cashiers: verify anti-fatigue mat condition, scanner height, bagging area layout; (c) for DC pickers: verify lifting aid availability (hand trucks, lift tables), shelving height optimization (heavy items at waist level); (d) for lumber yard: verify lifting team protocols, mechanical aid availability; (e) submit assessments to Safety Officer for review | Department Supervisor | Safety Officer | 30 min per workstation/quarter |
| 3 | **Employee discomfort reporting**: employees can report musculoskeletal discomfort via HR self-service portal: (a) anonymous option available to encourage reporting without fear of judgment; (b) system prompts for: affected body part (back, shoulder, wrist, knee, etc.), severity (1-5), specific task triggering discomfort, duration of symptoms; (c) reports routed to Safety Officer for assessment and response within 48 hours | Employee | Safety Officer | 5 min per report |
| 4 | **Ergonomic assessment by consultant**: for reported discomfort cases or high-risk areas: (a) External Ergonomics Consultant conducts on-site assessment: observe work tasks, measure workstation dimensions, assess posture and movement patterns, review injury history; (b) consultant provides written recommendations: workstation modification, equipment changes (anti-fatigue mats, adjustable-height platforms, lifting aids), task rotation schedules, stretching exercise programs; (c) recommendations shared with Department Supervisor for implementation | External Ergonomics Consultant | Safety Officer | 2-4 hours per location |
| 5 | **Intervention implementation**: Department Supervisor implements ergonomic improvements: (a) immediate low-cost fixes: adjust shelf heights, reposition equipment, provide anti-fatigue mats, implement task rotation schedule; (b) medium-cost fixes: purchase lifting aids (hand trucks, lift tables), ergonomic floor mats, adjustable cashier platforms; submit request per W188 maintenance workflow; (c) high-cost fixes: shelving system redesign, automated material handling equipment — submit capex request per W184; (d) all fixes documented in system with before/after photos and expected impact | Department Supervisor | Store/DC Manager | Varies by intervention |
| 6 | **Stretching & exercise program**: Safety Officer implements stretching break program for high-risk roles: (a) 5-minute group stretching sessions at start of shift and mid-shift for DC and lumber yard staff; (b) posted stretching exercise guides at cash registers and DC workstations; (c) incorporate ergonomic awareness into W655 safety training curriculum | Safety Officer / Department Supervisor | VP HR | Ongoing (~10 min/day per team |
| 7 | **Return-to-work ergonomic accommodation**: for employees returning from musculoskeletal injury: (a) Safety Officer coordinates with Occupational Health Provider on work restrictions (weight limits, restricted movements, maximum standing time); (b) Department Supervisor implements temporary modified duty: reduced lifting, alternate task assignment, additional breaks; (c) gradual return-to-full-duty schedule over 2-4 weeks; (d) system tracks modified duty assignments and clearance dates | Safety Officer / Department Supervisor | VP HR | 2-4 weeks per case |
| 8 | **Annual MSD trend analysis**: Safety Officer compiles annual MSD trend report: (a) MSD incident rate by location and role type; (b) common injury types (back strain, shoulder strain, wrist CTS, knee strain); (c) lost workdays due to MSDs; (d) workers' compensation claims related to MSDs; (e) intervention effectiveness: pre/post-intervention MSD rates at assessed locations; (f) feed findings into annual OHS report per W436 and BC plan per W685 | Safety Officer | VP HR | 1 day/year |

### System Touchpoints

- Ergonomic risk assessment module by role type
- Quarterly workstation self-assessment checklist tool
- Employee discomfort reporting portal (HR self-service)
- Ergonomic assessment tracking and recommendation implementation
- Maintenance request integration per W188
- Capex request integration per W184
- Training management integration per W655
- Incident management integration per W140
- Workers' compensation claims tracking
- Annual OHS reporting integration per W436

### Pain Points / Risks

- **Underreporting of discomfort**: employees may not report early symptoms for fear of being seen as weak or complaining, leading to progression from discomfort to injury
- **Lifting culture in hardware retail**: macho workplace culture in hardware stores may discourage use of mechanical aids or requesting help with heavy loads; Safety Officer must reinforce that using aids is standard practice, not a sign of weakness
- **Cost of ergonomic interventions**: comprehensive ergonomic retrofit (anti-fatigue mats, lifting aids, shelving redesign) across 200 stores and 4 DCs represents significant investment; must be prioritized by injury rate and risk level
- **Seasonal workload variation**: during peak seasons (Christmas, back-to-school), increased customer traffic and stocking volumes increase physical demands; stretching programs and task rotation may be skipped under pressure
- **Contractor and agency worker inclusion**: temporary and agency workers may not receive the same ergonomic training and assessment as regular employees, creating risk gaps

### Staffing Implication

- **Safety Officer**: ~8-12 hours/quarter on ergonomic assessments and program management. Absorbed within existing role.
- **External Ergonomics Consultant**: ~5-10 days/year for high-risk location assessments.
- **Department Supervisors**: ~30 min/quarter per workstation for self-assessments. Absorbed within existing role.
- **No incremental headcount**.

### Time Estimate

- Risk identification: 1-2 days (initial), updated annually
- Quarterly self-assessment: 30 min per workstation
- Consultant assessment: 2-4 hours per location
- Intervention implementation: varies
- Annual trend analysis: 1 day
- Stretching program: ~10 min/day per team

---

## W758. Store-Level Fire Safety Equipment Daily Inspection & Compliance

| Field | Detail |
|---|---|
| **Trigger** | Daily store opening (W5A); scheduled daily inspection |
| **Frequency** | Daily per store |
| **Volume** | 200 stores × daily inspection |
| **Owner** | Maintenance Associate |
| **Participants** | Maintenance Associate, Store Manager, BFP (annual inspection W476) |

### Background
Beyond the annual Fire Safety Inspection Certificate (FSIC) from the Bureau of Fire Protection (W476) and periodic fire drills (W582), daily fire safety equipment inspections ensure that fire extinguishers, fire alarm systems, emergency lighting, sprinkler systems, and fire exits are functional at all times. A single non-functional fire extinguisher during an actual fire event can result in catastrophic liability and loss of life.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Inspection checklist generation — System generates daily fire safety checklist per store location based on installed equipment: fire extinguishers (type, location, pressure gauge), fire alarm panels, emergency exit lights, sprinkler pressure gauges, fire exit paths, fire door closers | System | — | Automated |
| 2 | Equipment walk-through — Maintenance Associate walks store following system-guided inspection route; at each equipment point: (a) verify equipment present, (b) check visual indicators (pressure gauge in green zone, no visible damage), (c) confirm exit path clear, (d) scan equipment barcode/QR for digital logging | Maintenance Associate | Store Manager | 20 min |
| 3 | Failed item documentation — If any equipment fails visual check: Maintenance Associate photographs deficiency, records description, and marks item as "Failed" in system; system auto-generates maintenance work order (W47) | Maintenance Associate | Store Manager | 5 min |
| 4 | Fire extinguisher pressure verification — Monthly: Maintenance Associate weighs each fire extinguisher (weight indicates charge level); records weight in system; if weight below minimum threshold, system triggers replacement request | Maintenance Associate | — | 1 hour/month |
| 5 | Emergency exit light test — Monthly: Maintenance Associate simulates power failure to verify emergency exit lights activate; records pass/fail per unit | Maintenance Associate | — | 30 min/month |
| 6 | Compliance documentation — System compiles daily inspection records into monthly compliance report; archives for 5 years per BFP requirements; accessible for W476 FSIC inspection and W141 safety audit | System | — | Automated |
| 7 | Equipment expiry tracking — System tracks fire extinguisher expiry dates, sprinkler system inspection dates, and fire alarm system certification dates; auto-generates replacement/inspection requests 30 days before expiry | System | — | Automated |
| 8 | Escalation for critical failures — If critical fire safety equipment fails (no fire extinguisher coverage for a zone, fire alarm system down, blocked fire exit): immediate escalation to Store Manager; Store Manager contacts fire safety vendor for same-day emergency repair | Store Manager | Store Manager | Immediate |

### System Touchpoints
- Fire safety equipment registry with per-item barcode/QR, installation date, expiry date, and inspection schedule
- Mobile inspection app with barcode scanning and photo capture
- W47 facility maintenance integration — auto-generated work orders for failed equipment
- W476 FSIC compliance documentation — inspection archives
- W141 safety inspection integration — fire safety as monthly inspection component
- Equipment expiry tracking with automated replacement scheduling
- Emergency vendor notification system for critical failures

### Pain Points / Risks
- Inspection fatigue — daily checks of the same equipment lead to "rubber-stamping" without genuine visual inspection; rotate inspection routes and conduct spot-checks
- Fire extinguisher vandalism — in high-traffic stores, extinguishers may be tampered with or discharged by customers; daily visual check catches this
- Exit blockage recurrence — merchandise, display units, and stock boxes are frequently placed in front of fire exits during restocking (W554); compliance requires constant vigilance
- Vendor response time — fire safety equipment vendors may not offer same-day emergency repair in provincial locations; stores in remote areas need backup equipment

### Time Estimate
Daily inspection: 20 min. Monthly extinguisher weighing: 1 hour. Monthly exit light test: 30 min. Total monthly per store: ~12 hours.

### Staffing Implication
No incremental headcount. Maintenance Associate absorbs fire safety inspection within existing duties. 200 stores × 12 hours/month = ~2,400 staff-hours/month across chain.

---

## W759. Store-Level Hazardous Material Customer Advisory & Safe Handling Guidance

| Field | Detail |
|---|---|
| **Trigger** | Customer purchases or inquires about hazardous products (chemicals, pesticides, solvents, adhesives, paint, sealants, asbestos-containing materials) |
| **Frequency** | Daily; ~20–30 hazmat customer interactions per store per day |
| **Volume** | 200 stores × ~25 hazmat interactions/day = ~5,000 interactions/day chain-wide |
| **Owner** | Department Supervisor (Chemicals/Building Materials) |
| **Participants** | Floor Associate, Department Supervisor, Customer |

### Background
As a hardware and home improvement retailer, BuildRight Depot sells products regulated by the Fertilizer and Pesticide Authority (FPA), DENR, and FDA (W479). Customers purchasing pesticides, industrial solvents, strong adhesives, and other hazardous materials need proper handling, storage, and disposal guidance. Providing this guidance is both a legal obligation and a customer safety imperative that reduces product liability (W185).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Hazmat product identification — When customer inquires about or scans a hazardous product, system identifies hazard classification based on item master GHS (Globally Harmonized System) attributes (W252): flammable, corrosive, toxic, oxidizer, irritant, environmental hazard | System | — | Instant |
| 2 | Customer advisory prompt — Floor associate receives system prompt with key safety information: (a) primary hazards, (b) required PPE, (c) safe handling procedures, (d) first aid measures, (e) proper disposal guidance | System / Floor Associate | — | 1 min |
| 3 | Verbal safety briefing — Floor associate provides verbal safety briefing to customer covering: (a) what the product is designed for, (b) what NOT to do with it, (c) required ventilation and PPE, (d) storage away from children and pets, (e) proper disposal per LGU regulations | Floor Associate | — | 3 min |
| 4 | SDS offer — Floor associate offers customer a printed Safety Data Sheet (SDS) per W698 SDS lifecycle management; for regular trade customers, associate confirms they have current SDS on file | Floor Associate | — | 1 min |
| 5 | Alternative suggestion — For high-hazard products where a safer alternative exists (e.g., water-based vs. solvent-based paint), floor associate suggests the safer alternative | Floor Associate | — | 2 min |
| 6 | Purchase quantity flag — System flags unusually large quantity purchases of regulated products (e.g., > 5L of industrial solvent, > 2kg of pesticide); prompts cashier to verify intended use during checkout (W5B) | System / Cashier | — | 1 min |
| 7 | Customer acknowledgment — For high-hazard purchases, customer signs digital acknowledgment of receiving safety guidance; archived per W256 retention policy for W185 product liability defense | Customer | Floor Associate | 1 min |
| 8 | Incident link — If customer later reports adverse reaction or injury from product, advisory acknowledgment and SDS provided are retrieved from archives for W185 product liability and W140 OHS incident processing | System | — | Automated |

### System Touchpoints
- W252 item master — GHS hazard classification attributes per SKU
- W698 SDS lifecycle management — current SDS availability and distribution
- W185 product liability — advisory documentation for liability defense
- W479 FDA LTO compliance — HHS product registration tracking
- W467 specialized hardware permits — FPA-regulated product tracking
- W236/W237 hazmat storage and handling — store-side hazmat compliance
- Digital acknowledgment capture with 7-year archival per W256

### Pain Points / Risks
- Customer resistance to "lectures" — some customers perceive safety guidance as condescending, especially professional contractors who use the products daily
- Floor associate knowledge gap — associates may not be familiar with all hazardous products in their department; system prompts compensate but cannot replace product knowledge
- SDS availability — maintaining current SDS for thousands of chemical SKUs requires vendor cooperation and systematic refresh; outdated SDS create liability
- Over-flagging — if every cleaning product triggers an advisory, associates and customers will experience alert fatigue; classification thresholds must be calibrated

### Time Estimate
Per interaction: 5–8 minutes total (1 min identification + 3 min briefing + 1 min SDS offer + 1 min acknowledgment + 2 min optional alternative suggestion).

### Staffing Implication
No incremental headcount. Hazardous material advisory is absorbed within existing floor associate duties. Additional training: 4 hours per associate on GHS hazard classification and safety communication, refreshed annually per W655 safety training. 200 stores × 5,000 interactions/day × 6 min = ~500 staff-hours/day, distributed across existing floor staff.

---

## W804. Occupational Health Surveillance, Employee Medical Monitoring & Record Management

| Field | Detail |
|---|---|
| **Trigger** | New employee hire (pre-employment medical); annual medical examination cycle; incident-specific medical evaluation per W140; DOLE periodic health assessment requirements |
| **Frequency** | Pre-employment: per hire (~1,200-1,600/year); Annual: per employee at DC and high-exposure roles; Incident: per W140 |
| **Volume** | ~6,715 employees; ~1,500-2,000 annual medical examinations for DC staff, drivers, paint/chemical handlers, and noise-exposed roles |
| **Owner** | HR Manager (Health & Benefits) |
| **Participants** | Employee, Occupational Health Physician, HR, Department Heads, HMO Provider, DOLE |

### Background

Philippine DOLE Department Order No. 198-18 (DO 198-18) requires employers to provide occupational health services proportionate to workplace risk. BuildRight's operations include specific health hazards: DC workers exposed to noise (material handling equipment, compressors), paint department staff exposed to volatile organic compounds (VOCs), lumber yard staff exposed to dust, and drivers exposed to prolonged sitting and traffic stress. This workflow ensures employee health monitoring is conducted per DOLE requirements, health records are maintained per RA 10173 data privacy, and occupational health findings drive workplace improvements.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Pre-Employment Medical Examination**: As part of W15 onboarding: (a) new hire completes pre-employment medical at BuildRight-designated clinic: physical examination, chest X-ray, drug test per W483, vision test, hearing test (audiometry for DC and yard roles), blood chemistry; (b) Occupational Health Physician reviews results and issues fitness-for-work certificate; (c) if medical condition is identified: assess reasonable accommodation per Magna Carta for Disabled Persons; (d) medical records stored confidentially per RA 10173; (e) HR receives fitness certificate only (not medical details) per data privacy | HR / Occupational Health Physician | HR Manager | 1-2 days per hire |
| 2 | **Annual Medical Examination (DC & High-Risk Roles)**: Annual schedule for employees in designated high-risk roles: (a) DC warehouse staff: audiometry (noise exposure), pulmonary function test (dust exposure), musculoskeletal assessment (manual handling); (b) Paint department staff: blood chemistry (lead, solvent exposure monitoring), pulmonary function test; (c) Drivers: vision test, blood pressure check, sleep apnea screening, driving fitness assessment per LTFRB requirements; (d) Yard staff: audiometry, pulmonary function test; (e) results compared to baseline (pre-employment) to detect occupational health trends | Occupational Health Physician / HR | HR Manager | 1 day per employee |
| 3 | **Incident-Specific Medical Evaluation**: After workplace incident per W140: (a) if employee exposed to chemical substance: refer to poison control or hospital within 24 hours; specific antidote or treatment per SDS per W698; (b) if employee exposed to noise trauma (explosion, impact): immediate audiometry within 48 hours; (c) if employee reports ergonomic pain or repetitive strain: refer to occupational health physician for assessment; (d) all incident-related medical evaluations documented in employee health file and incident file per W140 | Safety Officer / HR | HR Manager | Per W140 timeline |
| 4 | **Health Trend Analysis**: Quarterly, HR Manager and Occupational Health Physician review aggregate health data (no individual identification per data privacy): (a) audiometry trends: any DC zones showing hearing threshold shifts indicating excessive noise exposure; (b) pulmonary function trends: any departments showing respiratory function decline; (c) musculoskeletal injury patterns: repetitive strain by job function; (d) drug test results per W483; (e) findings reported to VP HR with recommendations for workplace improvements (engineering controls, PPE upgrades, job rotation) | HR Manager / Occupational Health Physician | VP HR | 2-4 hours/quarter |
| 5 | **Medical Record Management**: HR maintains confidential employee health records: (a) stored in secure HR system with restricted access per RA 10173; (b) retention: employment duration + 5 years post-separation per DOLE requirements; (c) only HR Manager and Occupational Health Physician have access to individual health records; (d) Department Heads receive fitness-for-work status only; (e) employee may request copy of own health records per W271 data subject access; (f) annual audit of health record access logs per W647 data privacy compliance | HR Manager | VP HR | Continuous |

### System Touchpoints

- HR module with confidential medical record subsystem per RA 10173
- Occupational health examination scheduling integrated with W34 shift scheduling
- HMO integration per W642 for medical service provision
- Incident reporting module per W140 for incident-specific medical referral
- SDS access per W698 for chemical exposure treatment protocols
- Drug testing management per W483
- Data privacy compliance module per W647 for record access control
- W271 data subject access request processing

### Pain Points / Risks

- **Occupational disease latency**: hearing loss and respiratory conditions develop over years; without annual monitoring, BuildRight may not detect occupational disease until significant and irreversible damage has occurred
- **DOLE compliance for medical clinics**: DO 198-18 requires employers with 50+ employees to maintain or have access to occupational health clinic; BuildRight's 200 stores with 25-35 staff each fall below threshold individually, but DCs with 150-250 workers require on-site or nearby occupational health services
- **Data privacy breach of medical records**: unauthorized disclosure of employee health information violates RA 10173 with penalties up to PHP 5M; medical records must be strictly segregated from general HR records
- **Occupational disease liability**: if employee develops occupational disease (e.g., hearing loss, respiratory condition) and BuildRight cannot demonstrate adequate health monitoring, the company faces SSS ECC claims and potential DOLE investigation
- **Annual medical examination cost**: 1,500-2,000 examinations/year at PHP 3,000-5,000 per exam = PHP 4.5M-10M annual occupational health cost

### Staffing Implication

- **HR Manager (Health & Benefits)**: ~6-8 hours/month on occupational health coordination; absorbed by existing role
- **Occupational Health Physician (contracted)**: per-clinic engagement for DC locations; 1-2 days/quarter per DC for annual examination cycles; not BuildRight FTE
- **No incremental BuildRight headcount**.

### Time Estimate

- Pre-employment medical: 1-2 days per hire
- Annual medical examination: 1 day per employee × 1,500-2,000 employees = staggered over 12 months
- Quarterly trend analysis: 2-4 hours
- Record management: continuous

---

## W805. Workers' Compensation, SSS/ECC Claims & Return-to-Work Processing

| Field | Detail |
|---|---|
| **Trigger** | Workplace injury or illness reported per W140; or occupational disease detected per W804 |
| **Frequency** | Ad-hoc; estimated 50-100 workplace injuries/year across 200 stores and 4 DCs (mostly minor) |
| **Volume** | ~5-10 SSS sickness benefit claims/month; ~2-5 ECC (Employees' Compensation Commission) claims/year for work-related injury/illness |
| **Owner** | HR Benefits Officer |
| **Participants** | Injured Employee, Store/DC Manager, Safety Officer, Occupational Health Physician, SSS, ECC, HR Manager, Department Head |

### Background

Philippine law requires employers to provide workers' compensation for work-related injuries and illnesses through the Social Security System (SSS) sickness benefit and the Employees' Compensation Commission (ECC) under PD 626. BuildRight's 6,715 employees across 200 stores and 4 DCs face workplace hazards: material handling injuries at DCs, slip-and-fall incidents at stores, chemical exposure in paint departments, and vehicle accidents for delivery drivers. This workflow manages the full workers' compensation lifecycle from injury reporting through SSS/ECC claim filing, medical treatment, and return-to-work processing.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Immediate Injury Response**: When workplace injury occurs: (a) first aid administered per W501; (b) if emergency: transport to nearest hospital; (c) incident reported per W140 within 24 hours; (d) Safety Officer conducts initial investigation; (e) Store/DC Manager notifies HR Benefits Officer within 24 hours; (f) HR confirms if injury is work-related based on incident report and circumstances | Safety Officer / Store Manager | HR Benefits Officer | Within 24 hours |
| 2 | **Medical Treatment & Documentation**: (a) employee receives medical treatment at company-designated clinic or nearest hospital; (b) attending physician completes Medical Certificate with: diagnosis, treatment plan, estimated recovery period, work restrictions; (c) for injuries requiring >3 days absence: physician issues SSS sickness notification; (d) HR Benefits Officer collects all medical documentation; (e) for serious injuries: Occupational Health Physician coordinates ongoing medical management | Employee / Occupational Health Physician | HR Benefits Officer | 1-7 days |
| 3 | **SSS Sickness Benefit Filing**: For work-related absence >3 days: (a) HR Benefits Officer files SSS Sickness Benefit claim: SSS sickness notification form, medical certificate, employer certification of salary deduction; (b) SSS processes claim and pays daily sickness allowance (90% of average daily salary credit) directly to employee; (c) BuildRight advances sickness allowance to employee within salary period and recovers from SSS; (d) claim processing time: 30-60 days | HR Benefits Officer | HR Manager | 3-5 days filing + 30-60 days SSS processing |
| 4 | **ECC Claim Filing (Serious Injury/Illness)**: For serious work-related injury or occupational disease: (a) HR Benefits Officer files ECC claim under PD 626: ECC claim form, incident report per W140, medical certificates, SSS sickness benefit documentation; (b) ECC provides additional benefits: income benefit, medical reimbursement, rehabilitation services, carer's allowance; (c) ECC claim processing: 60-90 days; (d) if claim denied: VP Legal assists with appeal to ECC | HR Benefits Officer / VP Legal | HR Manager | 5-10 days filing + 60-90 days ECC processing |
| 5 | **Return-to-Work Processing**: When employee is medically cleared: (a) Occupational Health Physician issues Return-to-Work Certificate with any restrictions (light duty, restricted lifting, modified hours); (b) HR coordinates with Department Head for work accommodation; (c) if restrictions apply: modified duty assignment for recovery period (typically 1-4 weeks); (d) if permanent partial disability: assess reasonable accommodation per Magna Carta; (e) if unable to return to any role: coordinate with SSS for disability benefit and process separation per W43 | Occupational Health Physician / HR / Department Head | HR Manager | 1-5 days |
| 6 | **Incident Trend Analysis**: Monthly, HR Benefits Officer and Safety Officer review workers' compensation data: (a) injury frequency rate by location, department, and cause; (b) lost workdays by injury type; (c) SSS/ECC claim costs; (d) repeat injury locations or roles; (e) findings feed into W512 store-level safety committee and W141 safety inspection programs; (f) quarterly report to VP HR and VP Operations | HR Benefits Officer / Safety Officer | VP HR | 2-3 hours/month |

### System Touchpoints

- Incident reporting module per W140 with injury classification
- SSS integration for sickness benefit filing and tracking
- ECC claim management module with document checklist
- Medical record management per W804 with return-to-work tracking
- HR module for work restriction and accommodation management
- W34 shift scheduling for modified duty assignment
- W43 separation processing for permanent disability cases
- Analytics dashboard for injury trend analysis

### Pain Points / Risks

- **SSS processing delays**: SSS sickness benefit claims take 30-60 days to process; BuildRight must advance the benefit to employees and recover from SSS, creating cash flow management overhead
- **ECC claim documentation burden**: ECC claims require extensive documentation including employer incident reports, medical certificates, and witness statements; incomplete documentation results in denial
- **Fraudulent injury claims**: some employees may claim non-work injuries as work-related to access SSS benefits; Safety Officer investigation per W140 and Occupational Health Physician assessment mitigate
- **Return-to-work non-compliance**: employees may not follow work restrictions upon return, risking re-injury; Department Head must enforce restrictions
- **Occupational disease causation disputes**: SSS/ECC may dispute that a disease (e.g., hearing loss, respiratory condition) is work-related, denying the claim; BuildRight's W804 health surveillance data provides critical evidence

### Staffing Implication

- **HR Benefits Officer**: ~6-10 hours/month on workers' compensation claims management; absorbed by existing role
- **Occupational Health Physician**: per-incident involvement; 2-4 hours per serious injury; absorbed by contracted physician services
- **No incremental headcount**.

### Time Estimate

- Immediate response: within 24 hours
- Medical treatment documentation: 1-7 days
- SSS claim filing: 3-5 days
- ECC claim filing: 5-10 days
- Return-to-work processing: 1-5 days
- Monthly trend analysis: 2-3 hours

---

## W806. Annual Fire Safety System Testing, Certification & BFP Compliance

| Field | Detail |
|---|---|
| **Trigger** | Annual fire safety system testing schedule; BFP inspection notice per W476; fire safety certificate renewal; post-incident testing after fire event |
| **Frequency** | Annual per location; ad-hoc after fire incidents or BFP orders |
| **Volume** | 200 stores + 4 DCs + HQ = 205 locations; each requires annual fire safety system certification |
| **Owner** | Facilities Manager (per location) |
| **Participants** | BFP-Licensed Fire Safety Inspector, DC/Store Manager, Fire Safety Officer, BFP Regional Office, Insurance Provider |

### Background

The Philippine Fire Code (RA 9514) requires all buildings to maintain functional fire safety systems and obtain annual Fire Safety Inspection Certificate (FSIC) from the Bureau of Fire Protection (BFP). BuildRight's 200 stores and 4 DCs have fire alarm systems, sprinkler systems (for larger stores), fire extinguishers, emergency lighting, fire exit signage, and smoke detectors. Annual testing and certification by BFP-licensed fire safety inspectors is mandatory for FSIC renewal per W476. Failure to maintain current FSIC risks BFP closure order, LGU Business Permit non-renewal per W54, and insurance claim denial per W610 in the event of fire.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Annual Testing Schedule**: Facilities Manager develops annual testing schedule: (a) schedule BFP-licensed fire safety inspector for each location 60 days before FSIC expiry; (b) group proximate stores on same inspector visit for efficiency; (c) ensure all 205 locations tested within 12-month rolling window; (d) schedule tracked in compliance calendar per W506 | Facilities Manager | VP Operations | 1-2 days/year planning |
| 2 | **Pre-Inspection Readiness**: Before inspector visit, Facilities Manager verifies: (a) all fire extinguishers are serviced and within expiry date (monthly inspection per W758 confirms daily visual check); (b) fire alarm panels show no active faults or trouble conditions; (c) sprinkler system pressure gauges within normal range (for equipped locations); (d) emergency lighting functional (tested per W758 monthly); (e) fire exits unobstructed and properly signed; (f) fire exit doors functional and not locked; (g) fire safety signage current and visible | Facilities Manager / Store Safety Officer | Store Manager | 2-4 hours per location |
| 3 | **Fire Safety System Testing**: BFP-licensed inspector conducts annual testing: (a) fire alarm system: test all smoke detectors, heat detectors, manual pull stations, horn/strobe notification devices; verify panel programming and zone mapping; (b) sprinkler system: visual inspection of all heads, flow test, alarm valve test, fire pump test (for equipped locations); (c) fire extinguishers: verify type, placement, pressure gauge, seal integrity, service date tag; (d) emergency lighting: simulate power failure, verify illumination duration (minimum 90 minutes per Fire Code); (e) fire exit routes: walk all exit paths, verify signage, clearance, door hardware functionality; (f) fire suppression kitchen hood system (for stores with food service areas) | BFP-Licensed Inspector | Facilities Manager | 4-8 hours per location |
| 4 | **Deficiency Remediation**: If inspector identifies deficiencies: (a) classify by severity: critical (system non-functional — must fix before FSIC can be issued), major (partial functionality — fix within 30 days), minor (cosmetic/administrative — fix within 90 days); (b) Facilities Manager dispatches maintenance technician or fire safety contractor for repair; (c) critical deficiencies: fire watch protocol activated until repair completed; (d) re-inspection by BFP-licensed inspector after remediation; (e) all costs tracked per location maintenance budget per W47 | Facilities Manager | Store Manager | 1-30 days depending on severity |
| 5 | **FSIC Application**: After successful testing: (a) Facilities Manager submits FSIC application to BFP Regional Office: fire safety inspection report, building occupancy permit, floor plan showing fire exits, fire safety system certificates; (b) BFP issues FSIC valid for 1 year; (c) FSIC displayed prominently in store per BFP requirement; (d) FSIC copy filed in Document Management System per W255; (e) FSIC copy provided to LGU for Business Permit renewal per W54; (f) FSIC copy provided to insurance provider per W610 | Facilities Manager / Fire Safety Officer | VP Operations | 1-2 weeks |
| 6 | **Annual Compliance Report**: VP Operations reviews annual fire safety compliance: (a) % locations with current FSIC (target: 100%); (b) deficiency rate by type and severity; (c) remediation timeliness; (d) locations with recurring deficiencies; (e) fire safety maintenance cost trend; (f) report to CEO and Board per W124 corporate governance | VP Operations | CEO | 1 day/year |

### System Touchpoints

- Compliance calendar per W506 with FSIC expiry tracking per location
- Fire safety inspection checklist mobile app
- Work order system for deficiency remediation per W47
- Document Management System per W255 for FSIC and inspection report filing
- BFP FSIC application tracking
- Insurance policy integration per W610 for certification evidence
- LGU Business Permit integration per W54 for FSIC submission
- Analytics dashboard for annual compliance reporting

### Pain Points / Risks

- **BFP-licensed inspector shortage**: limited pool of BFP-licensed fire safety inspectors, especially in provincial areas; scheduling may require 4-8 week advance booking
- **BFP FSIC processing delays**: BFP regional offices may take 2-4 weeks to issue FSIC after successful inspection; stores cannot operate with expired FSIC in strict LGU jurisdictions
- **Sprinkler system testing disruption**: flow testing sprinkler systems requires temporary system shutdown, which means the building has reduced fire protection during testing; must schedule during lowest-risk hours
- **Fire extinguisher servicing logistics**: 200 stores × 10-15 extinguishers per store = 2,000-3,000 extinguishers requiring annual servicing; logistics of collection, servicing, and return is significant
- **Budget pressure on fire safety maintenance**: fire safety maintenance is a non-revenue cost that store managers may deprioritize; centralized scheduling and budget allocation mitigates

### Staffing Implication

- **Facilities Manager**: ~4-6 hours/month on fire safety testing coordination; absorbed by existing role (shared across W47, W700, W701)
- **Store Safety Officers**: ~2-4 hours per annual inspection per location; absorbed by existing role
- **BFP-Licensed Fire Safety Inspector**: outsourced service; ~PHP 5,000-10,000 per location per inspection = ~PHP 1M-2M/year total
- **Fire Safety Contractor**: on-call for deficiency remediation; framework agreement for emergency response
- **No incremental BuildRight headcount**.

### Time Estimate

- Annual schedule planning: 1-2 days
- Pre-inspection readiness: 2-4 hours per location
- Annual testing: 4-8 hours per location
- Deficiency remediation: 1-30 days per deficiency
- FSIC application: 1-2 weeks
- Annual compliance report: 1 day
