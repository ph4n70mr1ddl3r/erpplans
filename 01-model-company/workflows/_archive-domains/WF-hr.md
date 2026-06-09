# HR & Payroll Workflows

> Payroll, recruitment, shift scheduling, onboarding/offboarding, training, performance, expenses, employee loans, PPE & uniform, succession & internal mobility, management trainee program, statutory benefits & claims administration, employee cross-entity & cross-location transfer processing, store-level health & safety committee operations, store-level employee daily attendance verification & exception processing, employee exit interview & attrition analysis, store-level employee engagement survey & action planning, employee recognition & rewards program management, off-cycle & ad-hoc payment processing, HMO & private benefits administration, final pay computation & separation settlement, 13th month pay reconciliation & compliance, strategic workforce planning, HR service desk operations, and employee data privacy compliance operations.
>
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W10. Payroll Processing](#w10-payroll-processing)
- [W15. Recruitment & Employee Onboarding](#w15-recruitment-employee-onboarding)
- [W34. Store Shift Scheduling](#w34-store-shift-scheduling)
- [W43. Employee Separation & Offboarding](#w43-employee-separation-offboarding)
- [W51. Employee Training & Skills Development](#w51-employee-training-skills-development)
- [W72. Employee Performance Management](#w72-employee-performance-management)
- [W74. Employee Expense Reimbursement](#w74-employee-expense-reimbursement)
- [W76. Employee Loans & Advances](#w76-employee-loans-advances)
- [W172. Employee PPE & Uniform Lifecycle](#w172-employee-ppe-uniform-lifecycle)
- [W178. Employee Succession & Internal Mobility](#w178-employee-succession-internal-mobility)
- [W179. Management Trainee (Cadetship) Program](#w179-management-trainee-cadetship-program)
- [W251. Philippine Statutory Benefits & Claims Administration (SSS, PhilHealth, Pag-IBIG)](#w251-philippine-statutory-benefits-claims-administration-sss-philhealth-pag-ibig)
- [W269. Vendor Promodizer & Third-Party Staff Management](#w269-vendor-promodizer-third-party-staff-management)
- [W280. Court-Ordered Wage Garnishment & Third-Party Deductions](#w280-court-ordered-wage-garnishment-third-party-deductions)
- [W429. Vendor-Funded Promodizer Incentive Management](#w429-vendor-funded-promodizer-incentive-management)
- [W449. Promodizer Labor Compliance & DOLE 174 Governance](#w449-promodizer-labor-compliance--dole-174-governance)
- [W511. Employee Cross-Entity & Cross-Location Transfer Processing](#w511-employee-cross-entity--cross-location-transfer-processing)
- [W512. Store-Level Health & Safety Committee Operations](#w512-store-level-health--safety-committee-operations)
- [W555. Seasonal & Temporary Staffing Process](#w555-seasonal--temporary-staffing-process)
- [W561. Employee Attendance Exception Management](#w561-employee-attendance-exception-management)
- [W567. Employee Cross-Training & Skill Matrix Management](#w567-employee-cross-training--skill-matrix-management)
- [W594. Store-Level Employee Daily Attendance Verification & Exception Processing](#w594-store-level-employee-daily-attendance-verification--exception-processing)
- [W628. Employee Exit Interview & Attrition Analysis](#w628-employee-exit-interview--attrition-analysis)
- [W629. Store-Level Employee Engagement Survey & Action Planning](#w629-store-level-employee-engagement-survey--action-planning)
- [W630. Employee Recognition & Rewards Program Management](#w630-employee-recognition--rewards-program-management)
- [W641. Off-Cycle & Ad-Hoc Payment Processing](#w641-off-cycle--ad-hoc-payment-processing)
- [W642. HMO & Private Benefits Administration](#w642-hmo--private-benefits-administration)
- [W643. Final Pay Computation & Separation Settlement](#w643-final-pay-computation--separation-settlement)
- [W644. 13th Month Pay Reconciliation & Compliance](#w644-13th-month-pay-reconciliation--compliance)
- [W645. Strategic Workforce Planning](#w645-strategic-workforce-planning)
- [W646. HR Service Desk Operations](#w646-hr-service-desk-operations)
- [W647. Employee Data Privacy Compliance Operations](#w647-employee-data-privacy-compliance-operations)
- [W715. Employee Referral Program Management & Reward Processing](#w715-employee-referral-program-management--reward-processing)
- [W716. Internal Communication & Company-Wide Announcement Management](#w716-internal-communication--company-wide-announcement-management)
- [W717. Workplace Violence Prevention & Response Protocol](#w717-workplace-violence-prevention--response-protocol)
- [W718. Employee Relocation & Housing Assistance Management](#w718-employee-relocation--housing-assistance-management)
- [W719. Diversity, Equity & Inclusion (DEI) Program Management](#w719-diversity-equity--inclusion-dei-program-management)

---

## W10. Payroll Processing

| Field | Detail |
|---|---|
| **Trigger** | Semi-monthly payroll calendar (14th and 28th/30th) |
| **Frequency** | 10 payroll runs/month (5 entities × 2) |
| **Volume** | ~6,715 employees total |
| **Owner** | Payroll Manager |
| **Participants** | Payroll Officer, HR Assistant, Department Heads (OT/leave approval), Finance (bank file) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Payroll Officer pulls time & attendance data from biometric/RFID system | Payroll Officer | Payroll Manager | 30 min/run |
| 2 | HR Assistant verifies approved leaves, overtime, and schedule adjustments are posted | HR Assistant | Payroll Manager | 2 hours/run |
| 3 | Payroll Officer validates: basic salary + OT + night differential + holiday pay + allowances | Payroll Officer | Payroll Manager | 1 hour/run |
| 4 | System calculates deductions: SSS, PhilHealth, Pag-IBIG, withholding tax (TRAIN law), loans, advances | System | — | Automated |
| 5 | Payroll Officer reviews computed payroll for anomalies (negative net pay, unusually high OT) | Payroll Officer | Payroll Manager | 1 hour/run |
| 6 | Payroll Manager reviews and approves payroll register | Payroll Manager | CHRO | 30 min/run |
| 7 | System generates bank file for payroll crediting (BDO, BPI, etc.) | System | — | Automated |
| 8 | Finance/Treasury reviews bank file; transmits to bank | Treasury Analyst | CFO | 30 min/run |
| 9 | System posts payroll journal entries to GL (salary expense, payable, deductions) | System | — | Automated |
| 10 | Payslips generated; distributed via email or employee self-service portal | System | — | Automated |
| 11 | Monthly: generate SSS PRN, PhilHealth contribution, Pag-IBIG contribution files for remittance | Payroll Officer | Payroll Manager | 1 hour/month |
| 11a | Payroll Officer reconciles statutory contribution schedule (per-employee breakdown) to generated remittance file and bank payment confirmation; investigates and resolves discrepancies before remittance deadline; system flags employees with missing or incomplete statutory data | Payroll Officer | Payroll Manager | 30 min/month |
| 11b | Contractual / fixed-term workers: system tracks contract start/end dates and auto-alerts HR Assistant 30 days before expiry; payroll computes pro-rated 13th month pay and statutory benefits per contract duration; end-of-contract settlement computed similar to final pay (W10 step 12) but with different legal basis; if employee converts to regular status, HR Assistant updates employee type in system and payroll adjusts benefit computation accordingly | HR Assistant / Payroll Officer | Payroll Manager | 15 min/employee |
| 12 | Final pay computation (upon employee separation): system calculates pro-rated 13th month pay, converted unused leave credits, less outstanding loans/advances and clearance deductions | Payroll Officer | Payroll Manager | 30 min/employee |
| 13 | System posts final pay as separate payroll run or adjustment; generates final payslip | System | — | Automated |

**Total payroll processing time**: ~6 hours per run per entity. With 5 entities, can be parallelized across 2–3 payroll officers.

### System Touchpoints
- Time & attendance import from biometric system (W10.1)
- Leave and overtime approval workflow (W10.2)
- Philippine payroll computation engine (TRAIN law, SSS, PhilHealth, Pag-IBIG tables) (W10.3–4)
- Payroll anomaly detection (W10.5)
- Bank file generation in Philippine bank formats (W10.7)
- GL posting from payroll (W10.9)
- Payslip distribution (W10.10)
- Statutory contribution file generation with PRN (W10.11)
- Statutory remittance reconciliation: per-employee contribution schedule vs. remittance file vs. bank confirmation; discrepancy flagging (W10.11a)
- Contractual/fixed-term worker management: contract date tracking, pro-rated benefit computation, end-of-contract settlement, regularization conversion (W10.11b)
- Agency / manpower contractor worker management: for seasonal and peak-period staffing (Christmas season, bi-monthly sale events, new store openings), BuildRight engages licensed manpower agencies per DOLE Department Order No. 174 (Labor-Only Contracting rules); agency workers are NOT employees of BuildRight entities — they appear in the agency's payroll, not in BuildRight's W10 payroll run; system tracks agency worker headcount separately from regular headcount for workforce planning; Store Manager submits agency staffing request to HR with headcount, duration, and skill requirements; HR coordinates with approved agency partners; agency invoices are processed as non-PO service invoices per W7C with DOLE-compliant documentation (agency service agreement, worker deployment list, attendance records); agency workers are issued temporary POS and access badges with limited system permissions and defined expiry dates; system distinguishes agency hours from regular employee hours for labor cost reporting (agency cost is a contract service expense, not payroll); typical agency worker deployment: 2–5 per store during November–December peak, and 10–15 per new store opening (W16) for the first 2 weeks of operations
- Agency worker access provisioning: Store Manager submits agency worker access request to IT via W48 helpdesk ticket, specifying worker name, agency, assignment duration, and required access level; IT creates temporary system account with predefined "Agency Worker" permission template (POS transaction processing only — no voids, no price overrides, no manager functions, no reports); access badge created with defined expiry date matching deployment end date; system auto-revokes access on expiry date; at end of deployment, Store Manager verifies badge return and IT confirms system deactivation; if deployment extended, Store Manager submits extension request before expiry; system logs all agency worker access with agency name, worker name, store, start/end dates, and permission level; monthly: IT generates agency worker access report showing active, expired, and unreturned badges; unreturned badges flagged for Store Manager follow-up (W10, cross-reference W71 access badge management)

### Statutory Compliance Calendar

The following table shows all recurring statutory remittance deadlines per entity. System generates alerts 5 business days before each deadline.

| Statutory Obligation | Frequency | Deadline | Remittance Method | Responsible | Cross-Reference |
|---|---|---|---|---|---|
| SSS employee + employer contributions | Monthly | Last day of following month (or 10th of second month per SSS schedule) | PRN via SSS online portal or bank | Payroll Officer | W10.11 |
| PhilHealth contributions | Monthly | Every 10th of the following month | Electronic remittance via PhilHealth portal | Payroll Officer | W10.11 |
| Pag-IBIG contributions | Monthly | Every 10th of the following month | Online remittance via Pag-IBIG portal | Payroll Officer | W10.11 |
| BIR Withholding Tax on Compensation (1601-C) | Monthly | 10th of following month | eFPS / eBIRForms | Tax Accountant | W9A.16 |
| BIR Expanded Withholding Tax (1601-E) | Monthly | 10th of following month | eFPS / eBIRForms | Tax Accountant | W9A.16a |
| BIR VAT Return (2550M) | Monthly | 20th or 25th of following month (per BIR filing threshold) | eFPS / eBIRForms | Tax Accountant | W9A.16 |
| BIR Quarterly VAT / Income Tax (2550Q / 1702Q) | Quarterly | 25th of month following quarter end | eFPS / eBIRForms | Tax Accountant | W9A.16 |
| Local Business Tax per LGU | Per LGU calendar (annual or quarterly) | Per LGU deadline | Per LGU (online, OTC, or LGU office) | Tax Accountant | W9A.16c |
| 13th Month Pay distribution | Annual | On or before December 24 | Via payroll run | Payroll Officer | W10, W9B.18 |
| BIR Annual Income Tax Return (1702RT) | Annual | April 15 (or as extended) | eFPS / eBIRForms | Tax Accountant | W9B.21 |

> **Note**: Deadlines are based on current BIR and statutory agency guidelines; Payroll Manager reviews for regulatory changes quarterly. The 5-entity structure means each obligation is filed per-entity TIN; Payroll Officer and Tax Accountant process 5 submissions per deadline.

### Pain Points / Risks
- **Statutory deduction errors**: SSS, PhilHealth, and Pag-IBIG contribution tables change periodically; failure to update payroll tables results in under- or over-deduction per employee, requiring manual retroactive adjustments and potential penalties from government agencies
- **Bank file generation failures**: Incorrect bank file formats (BDO, BPI, etc.) or transmission errors can delay salary crediting for thousands of employees, triggering immediate employee complaints and trust erosion
- **Multi-entity reconciliation complexity**: Running 10 payroll cycles/month across 5 legal entities with different TIN registrations creates significant reconciliation overhead; intercompany employee transfers (W43.15) add further complexity to entity-specific payroll totals
- **Negative net pay risk**: When loan deductions, salary advances, and statutory contributions coincide, an employee's net pay may fall below minimum wage; the system must dynamically cap deductions, but manual overrides can bypass this safeguard
- **Payroll anomaly detection gaps**: With ~6,715 employees, manual review of the payroll register for anomalies (unusually high OT, negative net pay, incorrect deductions) is time-consuming and error-prone; undetected errors cascade into incorrect payslips and bank transfers

### Staffing Implication
- **2–3 Payroll Officers**: 5 entities × 2 runs = 10 runs/month. Each run takes ~6 hours. Total ~60 hours/month of payroll processing. 2 officers can handle this with time for reconciliation and inquiries.
- **1 Payroll Manager**: Approval, oversight, statutory compliance.
- **1–2 HR Assistants**: Leave and OT verification (data entry-heavy during payroll week).
- Fits within the ~16-person HR team.

### Time Estimate
**Per payroll run**: ~6 hours per entity (data validation + computation + review + bank file generation). With 5 entities and bi-monthly runs, total monthly payroll processing time is ~60 hours (5 entities × 2 runs × 6 hours). Quarter-end and year-end runs (13th month, bonus periods) add ~50% additional time per run. Year-end W9B tax reconciliation (W9B) requires an additional 2–3 days of concentrated effort by the Payroll team.

---

## W15. Recruitment & Employee Onboarding

| Field | Detail |
|---|---|
| **Trigger** | Vacancy created (resignation, new position, new store opening) |
| **Frequency** | ~100–130 hires/month (1,200–1,600/year including turnover + growth) |
| **Volume** | Peaks during new store openings (30 hires per new store) |
| **Owner** | HR Recruitment Officer |
| **Participants** | Recruitment Officer, HR Assistant, Hiring Manager, HR Head |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Hiring Manager submits staffing request with role, department, justification | Hiring Manager | Dept. Head | 15 min |
| 2 | HR Recruitment Officer posts job on job boards, social media, walk-in postings | Recruitment Officer | HR Head | 30 min/role |
| 3 | Screen applications; shortlist candidates | Recruitment Officer | HR Head | 2–4 hours/role |
| 3a | **Applicant tracking detail**: system tracks all applicants through a structured pipeline — Applied → Phone Screen → Interview (1st) → Interview (2nd) → Offer → Hired / Rejected; each pipeline stage records date, recruiter notes, interviewer feedback (rating 1–5), and outcome; system auto-sends rejection email to unsuccessful candidates at each stage with configurable template; for high-volume store roles (Sales Associates, Cashiers, Stock Associates), Recruitment Officer may use a walk-in hiring event model with batch applicant entry and bulk status updates; system generates recruitment analytics: time-to-fill by role, sourcing channel effectiveness (job boards, walk-in, referral, social media), offer acceptance rate, interviewer assessment scores; applicant data retained for 1 year per RA 10173 (with candidate consent) for potential future openings | Recruitment Officer | HR Head | Ongoing |
| 4 | Conduct interviews (1st: HR; 2nd: Hiring Manager) | Recruitment Officer + Hiring Manager | Dept. Head | 1 hour/candidate |
| 5 | Select candidate; extend offer | Recruitment Officer | HR Head | 30 min |
| 6 | New hire completes pre-employment requirements (SSS, PhilHealth, Pag-IBIG, TIN, medical, NBI clearance) | New Hire | Recruitment Officer | — |
| 7 | HR Assistant creates employee record in system (personal info, position, salary, entity, tax status); employee type classified as regular, probationary, fixed-term, or project-based with contract start/end dates for non-regular employees | HR Assistant | HR Head | 30 min |
| 8 | System generates employee ID; enrolls in payroll with correct statutory deductions | System | — | Automated |
| 9 | Assign biometric/RFID credentials for time & attendance | HR Assistant | — | 10 min |
| 10 | Onboarding: safety orientation, company policies, POS/system training | Dept. Supervisor + HR | Hiring Manager | 2–3 days |
| 11 | First payroll: system computes pro-rated salary for partial month | System | — | Automated |

### Pain Points / Risks
- **High-volume hiring strain**: 100–130 hires/month with peaks of 30 per new store opening (W16) stretches the 2-person recruitment team; sourcing quality candidates for store-level roles (Cashiers, Sales Associates, Stock Associates) in provincial locations is particularly difficult
- **Pre-employment document delays**: SSS, PhilHealth, Pag-IBIG, TIN, NBI clearance, and medical results can take 1–3 weeks for candidates to complete, delaying onboarding and leaving positions unfilled; some new hires start without complete documentation, creating payroll compliance gaps
- **Onboarding quality inconsistency**: 2–3 day onboarding across 200 stores varies significantly in quality depending on Department Supervisor commitment; new hires in remote stores may receive inadequate safety and system training
- **Applicant data retention risk**: RA 10173 requires candidate consent for 1-year data retention; manual tracking of consent across thousands of applications creates compliance exposure if retention/deletion is not systematically enforced

---

### System Touchpoints
- Staffing request workflow with role, department, and justification capture (W15.1)
- Job posting management: multi-channel publishing to job boards, social media, and walk-in posting boards (W15.2)
- Applicant Tracking System (ATS): structured pipeline tracking (Applied → Phone Screen → Interview → Offer → Hired/Rejected) with stage-level date, recruiter notes, interviewer ratings (1–5), and outcome; auto-rejection emails; batch applicant entry for walk-in hiring events; recruitment analytics (time-to-fill, sourcing channel effectiveness, offer acceptance rate) (W15.3a)
- Employee record creation with full statutory data (SSS, PhilHealth, Pag-IBIG, TIN, tax status) and employee type classification (regular, probationary, fixed-term, project-based) (W15.7)
- Automated payroll enrollment with correct statutory deduction setup (W15.8)
- Biometric/RFID credential assignment integrated with time & attendance system (W15.9)
- Onboarding program tracking with completion milestones (W15.10)
- Pro-rated salary computation for partial-month first payroll (W15.11)
- Integration with W10 (payroll — employee master and first pay), W34 (scheduling — new employee shift assignment), W43 (separation — reverse process), W51 (training — onboarding training), W172 (PPE/uniform issuance)

### Time Estimate
- Staffing request: 15 min
- Job posting: 30 min/role
- Screening and shortlisting: 2–4 hours/role
- Interviews (HR + Hiring Manager): 1 hour/candidate
- Offer extension: 30 min/candidate
- Employee record creation: 30 min/new hire
- Biometric enrollment: 10 min/new hire
- Onboarding program: 2–3 days/new hire
- **Total end-to-end per hire**: ~4–6 hours of HR time + 2–3 days onboarding

### Staffing Implication
- **1–2 Recruitment Officers**: 100–130 hires/month. Each hire takes ~4–6 hours of HR time (screening + interview + paperwork). With 2 recruiters: ~60 hires each/month × 5 hours = 300 hours ÷ 160 working hours/month = ~2 recruiters at near-full capacity. 2 is appropriate.
- **2 HR Assistants**: Employee record creation, credentials, onboarding logistics. 130 hires × 1 hour admin each = 130 hours/month. 2 assistants can handle alongside other HR admin.

## W34. Store Shift Scheduling

| Field | Detail |
|---|---|
| **Trigger** | Weekly schedule creation cycle |
| **Frequency** | Weekly per store; published 1 week in advance |
| **Volume** | 30 staff × 200 stores = 6,000 weekly shift assignments; 2–3 shifts per day (opening: 7 AM–2 PM, mid: 10 AM–6 PM, closing: 2 PM–10 PM) |
| **Owner** | Store Manager |
| **Participants** | Store Manager, Assistant Store Manager, Department Supervisors, HR Assistant |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System generates draft schedule based on: (a) store operating hours, (b) staffing model per shift (min cashiers, floor associates, receiving), (c) historical sales volume by day and hour, (d) approved leave requests, (e) labor budget (max hours per employee per week) | System | — | Automated |
| 2 | Store Manager reviews draft schedule; adjusts for: expected delivery days (DSD receiving), upcoming promotions, special events, employee skill mix per shift | Store Manager | Store Ops Director | 1 hour/week |
| 3 | Department Supervisors review shift assignments for their departments; flag conflicts or coverage gaps | Dept. Supervisor | Store Manager | 30 min/week |
| 4 | Store Manager finalizes and publishes schedule in system; employees receive notification (mobile app, SMS, or bulletin board) | Store Manager | — | 15 min |
| 5 | Employee views schedule; submits swap requests to Store Manager if needed | Employee | — | Self-service |
| 6 | Store Manager approves or denies shift swap requests; updates schedule | Store Manager | — | 15 min/week |
| 7 | During the week: if unplanned absence (sick leave, emergency): Store Manager activates contingency (call in off-duty employee, redistribute floor staff, cover cashier shift personally) | Store Manager | — | Ad hoc |
| 8 | System tracks actual hours worked (biometric/RFID clock-in/out) vs. scheduled hours; flags overtime and undertime | System | — | Automated |
| 9 | Weekly: Store Manager reviews schedule adherence report; adjusts next week's plan based on actuals | Store Manager | Regional Manager | 15 min/week |
| 10 | Monthly: Regional Manager reviews overtime hours per store vs. labor budget; flags stores consistently exceeding targets | Regional Manager | Store Ops Director | 2 hours/month (across 50 stores) |

### System Touchpoints
- Automated schedule generation based on rules engine (W34.1)
- Leave request integration (W34.1d)
- Shift swap request and approval workflow (W34.5–6)
- Schedule publishing with employee notification (W34.4)
- Time & attendance integration: actual vs. scheduled hours comparison (W34.8)
- Overtime alerting (W34.8)
- Attendance exception handling: system detects clock-in/out anomalies — (a) **missed punch**: employee forgot to clock in or out; system generates missed punch alert; employee submits missed punch request via self-service portal (W51) within 24 hours with estimated in/out time; Department Supervisor approves or adjusts; system retroactively calculates hours; (b) **biometric reader failure**: if biometric device malfunctions, Store Manager records attendance manually in system with reason code; IT Helpdesk (W48) notified as P2 incident for device repair; manual records reconciled upon device restoration; (c) **late arrival / early departure**: system flags employees clocking in > 15 minutes after shift start or clocking out > 15 minutes before shift end; Store Manager reviews daily exception list; habitual lateness (> 3 occurrences/month) triggers HR counseling; (d) **unmatched punch**: employee clocks in at one terminal and out at another, or forgets to clock out and clocks in next day; system generates unmatched punch alert; employee submits correction via self-service; supervisor approves; system resolves unmatched pair; all attendance exceptions logged per employee with timestamp, type, resolution, and approver; monthly: HR Assistant generates attendance exception summary per store for Regional Manager review (W34)
- Schedule adherence and labor budget reporting (W34.9–10)
- Integration with payroll (W10) for hour calculation

### Time Estimate
- Draft schedule generation: Automated
- Store Manager review and adjustment: 1 hour/week
- Supervisor review: 30 min/week
- Finalization and publishing: 15 min/week
- Ongoing swap/unplanned absence handling: ~30 min/week
- **Total per store per week**: ~2–2.5 hours

### Pain Points / Risks
- **Unplanned absences**: Sick calls and no-shows disrupt carefully planned schedules; Store Managers spend significant ad-hoc time finding coverage, especially during peak seasons
- **Labor budget overruns**: Stores in high-traffic locations consistently exceed allotted overtime hours, requiring Regional Manager intervention and labor cost reforecasting
- **Shift swap abuse**: Informal shift swapping without system approval creates audit gaps in time & attendance and can lead to under-staffed shifts
- **Skill-mix gaps**: Automated scheduling may fill headcount but fail to ensure required skill coverage (e.g., enough trained cashiers during peak hours, forklift-certified staff during receiving)

### Staffing Implication
- **Store Manager**: ~2 hours/week on scheduling. Absorbed into existing duties.
- **Department Supervisors**: ~30 min/week reviewing their section schedules. Absorbed.
- **Regional Managers**: ~2 hours/month reviewing overtime reports across their 50 stores. Absorbed.
- No incremental headcount. The system's automated draft generation significantly reduces manual scheduling effort.

---

## W43. Employee Separation & Offboarding

| Field | Detail |
|---|---|
| **Trigger** | Employee submits resignation, or management initiates termination, or employee retires |
| **Frequency** | ~100–130 separations/month (1,200–1,600/year at 15–20% annual turnover) |
| **Volume** | Peaks in January (post-13th month pay resignations) and during store opening months (transfer to new store vs. separation) |
| **Owner** | HR Assistant |
| **Participants** | HR Assistant, HR Head, Department Head, Payroll Officer, IT, Employee |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Employee submits resignation letter (or management issues termination notice) | Employee / Dept. Head | Dept. Head | — |
| 2 | HR Assistant creates separation record in system: resignation date, last working day (30-day notice per Labor Code or garden leave), separation type (resignation, termination, retirement, end of contract) | HR Assistant | HR Head | 10 min |
| 3 | Department Head conducts exit interview; documents feedback (work conditions, compensation, management, reason for leaving) | Dept. Head | HR Head | 30 min |
| 4 | HR Assistant initiates clearance process: system generates clearance form routed to all relevant departments | System | HR Assistant | Automated |
| 5 | **IT clearance**: IT confirms return of laptop/tablet/phone (if issued); deactivates system accounts (ERP, POS, email, VPN); revokes access badges | IT Team | CIO | 15 min/employee |
| 6 | **Department clearance**: Dept. Head confirms return of company property (uniforms, tools, keys); approves final leave usage | Dept. Head | Dept. Head | 10 min/employee |
| 7 | **Finance clearance**: AP Clerk confirms no outstanding cash advances or loans; AR confirms no corporate account exposure | AP / AR Clerk | AP/AR Supervisor | 10 min/employee |
| 8 | **Store Operations clearance** (if store employee): Store Manager confirms no pending inventory accountability issues, cash drawer reconciled | Store Manager | Store Ops Director | 10 min/employee |
| 9 | HR Assistant collects all signed clearances; marks clearance as complete in system | HR Assistant | HR Head | 10 min/employee |
| 10 | Payroll Officer computes final pay per W10 step 12: pro-rated salary for final pay period, pro-rated 13th month pay (1/12 of annual basic salary × months worked ÷ 12), converted unused leave credits (VL to cash per company policy), less outstanding loans/advances and clearance deductions; final pay computation varies by separation type — resignation: pro-rated salary + 13th month + VL conversion; termination for cause: pro-rated salary + 13th month (VL conversion per company discretion); retirement: pro-rated salary + 13th month + VL conversion + retirement pay per Labor Code or company plan (whichever is higher); end of contract: pro-rated salary + 13th month + VL conversion + separation pay if applicable per DOLE; system auto-calculates final pay based on separation type classification from W43.2 with Payroll Officer review and validation | Payroll Officer | Payroll Manager | Per W10 |
| 11 | System generates final pay as separate payroll run or adjustment; final payslip issued (W10 step 13) | System | — | Automated |
| 12 | System updates employee status to "Separated"; deactivates payroll processing; retains record for regulatory retention (7 years) | System | — | Automated |
| 13 | System generates COE (Certificate of Employment) on request: dates of employment, position, compensation range (optional) | System / HR Assistant | HR Head | 5 min/request |
| 14 | HR Head includes separation data in monthly turnover report: rate by department, store, and separation type; exit interview themes | HR Head | CHRO | 1 hour/month |
| 15 | Cross-entity employee transfer (between legal entities, e.g., Depot Inc. → Logistics Inc.): HR Assistant initiates transfer with effective date, destination entity, and new position; system processes as simultaneous separation from source entity and onboarding in destination entity with continuity of service — accumulated leave credits, 13th month pay pro-ration, and seniority carry forward; system deactivates employee in source entity payroll, creates employee record in destination entity with transferred balances, reassigns SSS/PhilHealth/Pag-IBIG to new entity's remittance, and switches BIR withholding tax to new entity's TIN registration; final pay computed at source entity (pro-rated) and first pay at destination entity for the same period; no break in employment continuity | HR Assistant / Payroll Officer | HR Head | 30 min/transfer |

**Total cycle time**: 30 days (notice period) + 5 business days after last day for final pay release

### System Touchpoints
- Separation record creation with type classification (W43.2)
- Automated clearance form generation and routing (W43.4)
- Clearance status tracking per department (W43.5–9)
- System account deactivation trigger (W43.5)
- Final pay computation by separation type: system auto-calculates final pay based on separation type (resignation, termination, retirement, end of contract) including pro-rated salary, pro-rated 13th month pay per BIR rules (1/12 of basic salary × months worked), unused VL monetization, applicable separation/retirement pay per Labor Code, less outstanding loans and deductions; final tax withholding per BIR rules (different treatment for retirement pay vs. resignation); final statutory contribution period computed per SSS/PhilHealth/Pag-IBIG rules; Payroll Officer reviews system calculation before processing (W43.10)
- Employee status lifecycle: Active → On Notice → Separated (W43.12)
- Certificate of Employment generation (W43.13)
- Cross-entity employee transfer: simultaneous separation and onboarding across legal entities with continuity of service; automatic payroll entity switch with transferred leave balances, 13th month pro-ration, and statutory reassignment; SSS/PhilHealth/Pag-IBIG reassigned to new entity; BIR withholding tax switched to new entity's TIN; GL postings to both entity payrolls for the transfer period (W43.15)
- Turnover analytics (W43.14)
- Integration with W10 (payroll) and W15 (onboarding — reverse process)

### Time Estimate
- Separation record creation: 10 min/employee
- Exit interview: 30 min/employee
- Clearance collection (all departments): ~45 min/employee over 1–2 weeks
- Final pay computation: 30 min/employee
- **Total per separation**: ~2 hours of HR/Payroll time spread across 30-day notice period
- **Cycle time**: 30 days (notice period) + 5 business days for final pay release

### Pain Points / Risks
- **Clearance bottlenecks**: IT deactivation or store inventory reconciliation delays can block final pay release beyond the 5-day target, creating employee grievances and potential DOLE complaints
- **Post-13th month spike**: January resignation surge (after 13th month pay) strains HR capacity and creates simultaneous vacancy backfills across 200 stores
- **Final pay disputes**: Employees frequently contest loan deductions or leave conversion amounts; Payroll Officer must reconcile manually when system-calculated final pay is challenged
- **Cross-entity transfer complexity**: Transfers between BuildRight's 5 legal entities require simultaneous separation and re-onboarding; errors in leave balance carry-forward or statutory reassignment cause payroll discrepancies

### Staffing Implication
- **HR Assistants (2)**: 100–130 separations/month × ~45 min admin each (clearance coordination + documentation) = ~90 hours/month. With 2 assistants that's ~45 hours each. Manageable alongside other HR admin duties.
- **IT**: 100–130 deactivations/month × 15 min each = ~30 hours/month. Absorbed by IT helpdesk.
- **Department Heads / Store Managers**: ~20 min per separating employee for clearance. With ~100/month spread across 200 stores, most managers handle < 1 separation/month. Negligible impact.

---

## W51. Employee Training & Skills Development

| Field | Detail |
|---|---|
| **Trigger** | New hire onboarding (W15), new system rollout, compliance requirement, periodic schedule, performance review finding |
| **Frequency** | Continuous; formal training sessions monthly per store; compliance training quarterly |
| **Volume** | ~6,715 employees; ~1,200–1,600 new hires/year requiring onboarding training; all employees require periodic refresher |
| **Owner** | HR — Training Officer |
| **Participants** | Training Officer, Department Supervisors, Store Managers, Category Managers (product knowledge), IT (system training), external trainers |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Training Officer maintains annual training calendar: (a) new hire onboarding (W15 step 10 — continuous), (b) quarterly compliance refreshers (safety, BIR procedures, data privacy), (c) semi-annual product knowledge updates (aligned with W1 assortment review and W32 seasonal planning), (d) annual system refresher (POS, ERP updates), (e) leadership development for supervisors and managers | Training Officer | HR Head | 4 hours/quarter (planning) |
| 2 | Training Officer develops or sources training materials per category: (a) creates in-house materials for company-specific processes (POS operations, returns handling, safety procedures, customer service standards), (b) sources external content for compliance topics (fire safety, first aid, hazmat handling for paint/chemicals), (c) coordinates with Category Managers for product knowledge content (new product features, seasonal items) | Training Officer | HR Head | Ongoing |
| 3 | Training delivery methods by audience: (a) **Store staff (6,000)**: monthly 30-minute department huddles led by Department Supervisors using provided materials; quarterly 2-hour group sessions at store level; (b) **DC staff (600)**: quarterly safety and equipment training at DC; (c) **HQ staff (~300)**: quarterly system and process training at HQ; (d) **New hires**: W15 onboarding program (2–3 days); (e) **Managers and supervisors**: semi-annual leadership and management skills workshops | Training Officer / Dept. Supervisors / External Trainers | HR Head | Per schedule |
| 4 | System tracks training completion per employee: attendance recording, quiz/assessment scores (where applicable), certification status and expiry dates | System / HR Assistant | Training Officer | Automated + 15 min/session |
| 5 | Training Officer generates compliance dashboard: completion rates by training type, overdue trainings by location, certification expiries (e.g., forklift license, fire safety) | Training Officer | HR Head | 1 hour/month |
| 6 | Department Supervisors and Store Managers identify training needs from performance observations (W34 schedule adherence, W37 exception patterns, W41 complaint root causes) and submit training requests to Training Officer | Dept. Supervisor / Store Manager | HR Head | As needed |
| 7 | Annual: HR Head reviews training program effectiveness: training hours per employee, correlation between training completion and key metrics (POS accuracy, shrinkage rate, customer satisfaction), budget utilization | HR Head | CHRO | 4 hours/year |

### Training Categories

| Category | Frequency | Audience | Delivery Method | Assessment |
|---|---|---|---|---|
| **New hire onboarding** | Per W15 | New employees | In-person at store/DC + e-learning modules | POS competency test, safety quiz |
| **POS operations** | Annual refresher; ad-hoc for system updates | Cashiers, CSRs | Hands-on at POS terminal | Speed and accuracy test |
| **Product knowledge** | Quarterly (aligned with W1 assortment review) | Sales Associates, Dept. Supervisors | Department huddle with Category Manager materials | Informal — supervisor observation |
| **Safety & compliance** | Quarterly | All employees | E-learning (LMS) + annual practical drill | Mandatory quiz (pass/fail) |
| **Hazmat handling** | Annual (for paint/chemical departments) | Paint dept. staff, receiving clerks | In-person with certified trainer | Written test + practical demo |
| **Loss prevention awareness** | Semi-annual | All store staff | E-learning + LP officer presentation (W37) | Awareness quiz |
| **Leadership development** | Semi-annual | Store Managers, Dept. Supervisors, Asst. Managers | Workshop (2 days) | 360 feedback |
| **IT system updates** | Per system change (W48 change management) | Affected users | E-learning + release notes | N/A |

### System Touchpoints
- Training calendar management with automated scheduling (W51.1)
- Training material repository (document storage per category) (W51.2)
- Training attendance tracking with digital sign-in or manager confirmation (W51.4)
- Assessment and certification tracking with expiry alerts (W51.4–5)
- Compliance dashboard: completion rates, overdue trainings, certification status by location and employee (W51.5)
- Learning Management System (LMS) integration for e-learning modules and assessments (W51.3)
- Integration with W15 (onboarding), W34 (shift scheduling — training time scheduled), W37 (LP awareness), W43 (separation — training history retained), W48 (system change training)
- Employee self-service portal: system provides a web-based or mobile-accessible self-service portal for employees with the following capabilities: (a) **payslip viewing**: employees view and download current and historical payslips (secure, accessible only by the employee); (b) **leave management**: employees submit leave requests (VL, SL, maternity, paternity, etc.) with automatic routing to Department Supervisor / Store Manager for approval; view leave balance and approval status; (c) **personal information update**: employees update contact information (address, phone, emergency contact), bank account details for payroll crediting, and dependent information; changes require HR Assistant verification before updating the payroll master; (d) **tax document access**: employees view and download BIR Form 2316 (Certificate of Compensation Payment/Tax Withheld) annually; (e) **benefits inquiry**: view SSS, PhilHealth, Pag-IBIG contribution history and loan balances (linked to agency portals or displayed from payroll data); (f) **training enrollment**: browse and enroll in available training sessions from the W51 training calendar; view training history and certification status; (g) **announcement board**: HR and management post company announcements, policy updates, and employee engagement content; portal access is role-based (employees see their own data only; managers see additional team-level information such as team leave calendar); mobile-responsive design for access from smartphones; requirement priority: Should Have (not all features needed at go-live — payslips and leave management are highest priority)

### Time Estimate
- Training calendar planning: 4 hours/quarter
- Training material development: Ongoing (~8–12 hours/month)
- Monthly department huddle delivery: 30 min/store/month (by Dept. Supervisors)
- Quarterly group session: 2 hours/store/quarter
- New hire onboarding: 2–3 days/employee
- Compliance dashboard review: 1 hour/month
- Annual program review: 4 hours/year

### Pain Points / Risks
- **Scale of delivery across 200 stores**: Coordinating consistent training quality across 200+ locations with only 1 Training Officer relies heavily on Department Supervisors who may deprioritize training during busy periods
- **Compliance tracking gaps**: With 6,715 employees, tracking certification expiry (forklift, hazmat, fire safety) is error-prone; lapsed certifications create legal liability and safety risks
- **New hire training compression**: During peak hiring (new store openings at 30 hires each), the 2–3 day onboarding may be rushed, leading to higher early-stage errors in POS operations and safety awareness
- **Training effectiveness measurement**: Difficulty correlating training completion to operational KPIs (POS accuracy, shrinkage, CSAT); without clear ROI data, training budget is vulnerable during cost-cutting

### Staffing Implication
- **1 Training Officer** (within HR team): manages training calendar, develops materials, coordinates external trainers, and monitors compliance. With 6,715 employees across 200+ locations, this is a full-time role.
- **Department Supervisors (per store)**: deliver monthly department huddles (30 min/month) — absorbed into existing duties.
- **HR Assistants (2)**: support attendance recording and logistics — absorbed into existing duties.
- **External trainers**: engaged for specialized topics (fire safety, hazmat, first aid, forklift certification, leadership) on a per-event basis.

---

## W72. Employee Performance Management

| Field | Detail |
|---|---|
| **Trigger** | Annual performance review cycle; or periodic performance improvement need |
| **Frequency** | Annual formal review; quarterly check-in; ongoing performance coaching |
| **Volume** | ~6,715 employees; all employees reviewed annually |
| **Owner** | Department Head (for direct reports); Store Manager (for store staff) |
| **Participants** | Store Manager, Department Supervisors, Department Heads, HR Head, employees |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Annual goal-setting** (January): Department Heads and Store Managers set performance goals for each direct report aligned with department/store KPIs — (a) quantitative goals (sales targets, accuracy rates, shrinkage targets for Dept. Supervisors; transaction speed, cash variance for Cashiers; receiving accuracy for Receiving Clerks; cycle count accuracy for Stock Associates), (b) qualitative goals (customer service standards, teamwork, adherence to company policies), (c) development goals (training completion per W51, skill acquisition, cross-training); goals entered in system with measurable targets and timeline | Dept. Head / Store Manager | VP / Store Ops Director | 30 min/employee |
| 2 | **Quarterly check-in**: Store Manager or Department Supervisor conducts 15-minute check-in with each direct report — review progress against goals, identify obstacles, adjust goals if business conditions changed; system sends quarterly reminder to managers; check-in notes documented in system | Store Manager / Dept. Supervisor | Dept. Head | 15 min/employee/quarter |
| 3 | **Mid-year calibration** (June): Store Ops Director conducts calibration session with Regional Managers to ensure consistent performance standards across stores; HR Head provides aggregate performance data by department and region; significant rating adjustments documented | Store Ops Director / HR Head | COO | 4 hours/year |
| 4 | **Annual performance review** (December): manager completes formal assessment per employee — (a) rates performance against each goal (Exceeds Expectations, Meets Expectations, Needs Improvement, Does Not Meet Expectations), (b) documents key achievements and areas for development, (c) proposes overall rating, (d) submits to next-level manager for review and approval | Store Manager / Dept. Supervisor | Dept. Head / Store Ops Director | 45 min/employee |
| 5 | **Employee acknowledgment**: employee reviews assessment in system; provides written comments (optional); signs acknowledgment (digital signature); if employee disagrees, may submit written rebuttal retained in system alongside the assessment | Employee | — | 15 min |
| 6 | **Rating confirmation and compensation action**: Dept. Head or Store Ops Director confirms final rating; HR Head approves ratings distribution (ensures no grade inflation); ratings linked to: (a) merit increase (if budgeted — typically 3–5% for Meets Expectations, 5–8% for Exceeds), (b) 13th month pay is statutory and not performance-linked, (c) promotional readiness identification, (d) performance improvement plan trigger for Needs Improvement/Does Not Meet | HR Head / CFO | CEO | 1 week/year |
| 7 | **Performance Improvement Plan (PIP)**: for employees rated Needs Improvement or Does Not Meet — (a) manager creates PIP in system with specific improvement targets, timeline (typically 30–60 days), and support resources (training per W51, closer supervision, mentoring), (b) employee acknowledges PIP, (c) manager conducts weekly check-ins during PIP period, (d) at PIP conclusion: manager assesses outcome — improved (close PIP, continue standard monitoring), insufficient improvement (extend PIP 30 days or initiate separation per W43 with HR Head approval), (e) system tracks PIP status and outcomes for HR reporting | Store Manager / Dept. Head | HR Head | 2 hours/PIP |
| 8 | **Promotion and transfer identification**: during annual review cycle, managers identify employees meeting promotion criteria — (a) consistent Exceeds Expectations ratings for 2+ years, (b) demonstrated readiness for next-level responsibilities, (c) completed required training per W51; promotion recommendations submitted to HR Head for review and inclusion in annual headcount plan; inter-store or inter-entity transfers processed per W43.15 (cross-entity transfer) or simplified location transfer within same entity | Store Manager / Dept. Head | HR Head | Part of annual review |
| 9 | **Analytics**: HR Head generates annual performance dashboard — rating distribution by department, store, region, and entity; year-over-year rating trend; correlation between training completion (W51) and performance ratings; PIP completion rate and outcomes; promotion rate; turnover rate by performance tier | HR Head | CHRO | 4 hours/year |

### System Touchpoints
- Performance goal entry with measurable targets and timeline (W72.1)
- Quarterly check-in reminder and documentation (W72.2)
- Annual assessment form with goal-by-goal rating, comments, and digital signature (W72.4–5)
- Rating workflow: manager proposes → next-level manager reviews → HR Head approves distribution (W72.6)
- PIP creation with improvement targets, timeline, weekly check-in logging, and outcome tracking (W72.7)
- Promotion/transfer identification linked to performance history (W72.8)
- Performance analytics dashboard: rating distribution, trends, training correlation, PIP outcomes (W72.9)
- Integration with W10 (merit increase in payroll), W15 (onboarding — initial goal-setting during first 90 days), W43 (PIP failure may lead to separation), W51 (training completion feeds into performance assessment), W67 (store performance KPIs inform goal-setting for store staff)

### Time Estimate
- Annual goal-setting: 30 min/employee (January)
- Quarterly check-in: 15 min/employee/quarter
- Annual formal review: 45 min/employee (December)
- Mid-year calibration: 4 hours/year (Store Ops Director + Regional Managers)
- PIP management: 2 hours/PIP
- Annual analytics and reporting: 4 hours/year (HR Head)
- **Total distributed effort**: ~6,000 hours/year across ~230 managers for ~6,715 employees

### Pain Points / Risks
- **Manager inconsistency**: With 200+ stores and ~230 managers conducting reviews, rating calibration is difficult; some stores may inflate ratings while others are strict, creating perceived unfairness and retention risk
- **Quarterly check-in non-compliance**: Managers under operational pressure (especially during sale events) often skip quarterly check-ins, undermining the continuous feedback model and making the annual review a surprise to employees
- **PIP documentation risk**: Poorly documented PIPs create legal exposure if a separated employee files an illegal dismissal case with DOLE/NLRC; system must enforce mandatory documentation at each PIP milestone
- **Merit budget constraints**: Limited merit increase budgets (3–5%) may not meaningfully differentiate high performers from average, reducing the incentive value of the performance cycle

### Staffing Implication
- **No incremental headcount.** Performance reviews are distributed across ~230 managers (Store Managers, Dept. Supervisors, Dept. Heads). Annual cycle adds ~45 min/employee/year for ~6,715 employees = ~6,000 hours total effort, distributed across the management team.
- **HR Head**: adds ~8 hours/year for calibration and rating distribution approval. Absorbed.

---

## W74. Employee Expense Reimbursement

| Field | Detail |
|---|---|
| **Trigger** | Employee incurs business expense not covered by petty cash (W25), purchase order (W2), or corporate card |
| **Frequency** | ~300–500 expense claims/month across all locations; peaks at month-end and during travel periods |
| **Volume** | Average claim value PHP 1,000–5,000; primarily travel, meals, training materials, field supplies, client entertainment |
| **Owner** | Employee (claimant); Department Head (approval) |
| **Participants** | Employee, Department Head / Store Manager, AP Clerk, Finance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Employee submits expense claim in system (self-service portal or mobile app): expense date, category (travel, meals, supplies, training, entertainment, other), amount, business purpose, cost center, and receipt attachment (photo or PDF) | Employee | — | 10 min/claim |
| 2 | System validates claim: (a) receipt amount matches claimed amount, (b) expense date within allowable claim window (typically 30 days from expense date), (c) expense category is valid for employee's role, (d) total monthly claims for employee do not exceed department expense budget allocation | System | — | Automated |
| 3 | System routes claim for approval per tier: (a) ≤ PHP 5,000: immediate supervisor, (b) PHP 5,001–20,000: Department Head / Store Manager, (c) > PHP 20,000: VP / C-Suite; entertainment expenses always require Department Head approval regardless of amount | System | — | Automated routing |
| 4 | Approver reviews claim: validates business purpose, checks receipt authenticity, confirms expense is within policy (meal per diem limits, travel class restrictions, entertainment pre-approval); approves, returns for correction, or rejects with reason | Approver | Finance Manager | 5 min/claim |
| 5 | Approved claim routed to AP Clerk for processing; AP Clerk validates GL coding and cost center; posts expense to GL (Dr. Department Expense / Cr. Employee Payable) | AP Clerk | AP Supervisor | 5 min/claim |
| 6 | Reimbursement: system includes approved expense reimbursement in the next semi-monthly payroll run (W10) as a separate line item on the payslip — not taxed as compensation if supported by receipts per BIR rules; alternatively, for large reimbursements (> PHP 20,000), AP Clerk processes via separate bank transfer per W7 payment run | Payroll Officer / AP Clerk | AP Supervisor | Per W10 / W7 |
| 7 | Monthly: AP Supervisor generates expense report by department, category, and employee; Finance Manager reviews for policy compliance and unusual patterns; includes in department budget variance report per W26 | AP Supervisor | Finance Manager | 1 hour/month |

### Expense Policy Parameters (Configurable in System)

| Category | Limit | Notes |
|---|---|---|
| **Meal per diem** | PHP 500/day (local); PHP 1,000/day (provincial travel) | Receipt required for amounts exceeding per diem; per diem is non-taxable per BIR rules with supporting travel order |
| **Travel — airfare** | Economy class for domestic; requires pre-approved travel order | Receipt required; booked through admin or approved booking platform |
| **Travel — lodging** | PHP 2,000/night maximum (provincial); requires hotel receipt | Exceptions require VP approval |
| **Transportation** | Taxi, grab, or shuttle receipts | Fuel claims only for authorized vehicle users per W52 |
| **Client entertainment** | PHP 3,000/event maximum; requires pre-approval from Dept. Head | Must specify client name, attendees, and business purpose |
| **Training materials** | Per approved training plan per W51 | Requires training enrollment confirmation |
| **Claim window** | 30 days from expense date | Claims > 30 days require Finance Manager approval |
| **Monthly claim limit** | PHP 20,000 per employee (standard) | Exceptions require VP approval |

### System Touchpoints
- Employee expense claim form in self-service portal (W74.1) with receipt photo upload, category selection, and business justification (W51 employee self-service portal)
- Automated validation rules: receipt matching, claim window enforcement, monthly limit check (W74.2)
- Tiered approval workflow with routing by amount and category (W74.3–4)
- GL posting with cost center allocation (W74.5)
- Payroll integration: approved reimbursements included in semi-monthly payroll as non-taxable line items (per BIR rules — reimbursement of substantiated business expenses is not compensation); alternatively processed via AP payment run for large amounts (W74.6)
- Expense policy parameter configuration by category with limits and approval rules (W74 policy table)
- Monthly expense reporting by department, category, and employee with budget variance integration (W74.7)
- Integration with W7 (AP processing), W10 (payroll — reimbursement payment), W25 (petty cash — boundary: petty cash is for small operational expenses at location; employee expense claims are for individual employee-incurred business expenses), W26 (budget — expense tracking against department budgets), W51 (self-service portal)

### Time Estimate
- Employee claim submission: 10 min/claim
- System validation: Automated
- Approver review: 5 min/claim
- AP Clerk processing and GL posting: 5 min/claim
- Monthly reporting: 1 hour/month
- **Total**: ~25–42 hours/month for AP team across 300–500 claims

### Pain Points / Risks
- **Receipt fraud and photocopy reuse**: Manual receipt verification is time-consuming and error-prone; employees may submit altered or duplicated receipts, especially for cash-based transactions common in the Philippines
- **30-day claim window violations**: Store-based employees frequently miss the claim window due to operational workload; late claims require Finance Manager exception approval, creating bottlenecks and employee frustration
- **Manager rubber-stamping**: Department Heads and Store Managers processing 2–5 claims/month may approve without thorough review, allowing policy violations (excess per diem, unauthorized entertainment) to pass through
- **Payroll vs. AP processing confusion**: Dual reimbursement channels (small amounts via payroll per W10, large amounts via AP per W7) create tracking complexity and occasional double-payments if not carefully reconciled

### Staffing Implication
- **AP Clerk**: ~300–500 claims/month × 5 min each = ~25–42 hours/month. Absorbed within existing AP team (~8–10 clerks); ~3–5 hours/clerk/month.
- **Department Heads / Store Managers**: ~5 min per claim × average 2–5 claims/approver/month = ~10–25 min/month. Absorbed.
- No incremental headcount.

---

## W76. Employee Loans & Advances

| Field | Detail |
|---|---|
| **Trigger** | Employee requests salary advance, calamity loan, or company-internal loan |
| **Frequency** | ~100–200 loan/advance requests/month chain-wide; spikes after typhoons (W49) and during enrollment season (May–August) |
| **Volume** | Salary advances: PHP 5,000–20,000; Calamity loans: PHP 10,000–50,000; Company loans: PHP 10,000–100,000 |
| **Owner** | HR Assistant (intake); Payroll Officer (processing) |
| **Participants** | Employee, Department Head / Store Manager, HR Assistant, Payroll Officer, Finance Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Employee submits loan/advance request in self-service portal (W51) or paper form to HR Assistant: type (salary advance, calamity loan, company loan), amount, reason, proposed repayment period | Employee | — | 10 min |
| 2 | HR Assistant verifies eligibility: (a) salary advance — employee must be regular status, employed ≥ 6 months, no outstanding salary advance; limit = 1× basic monthly salary; (b) calamity loan — triggered by declared natural disaster (W49) affecting employee's residence; limit = 2× basic monthly salary; requires disaster declaration or barangay certification; (c) company loan — employee must be regular status, employed ≥ 1 year, no outstanding loan delinquency; limit = 3× basic monthly salary; requires documented purpose (medical, education, housing repair) | HR Assistant | HR Head | 15 min/request |
| 3 | Approval per tier: (a) salary advance ≤ PHP 20,000: Store Manager / Dept. Head; (b) calamity loan ≤ PHP 50,000: HR Head + Finance Manager; (c) company loan ≤ PHP 100,000: HR Head + CFO; (d) > PHP 100,000: CEO | Approver | Approver | 10 min/request |
| 4 | Payroll Officer creates loan record in system: principal amount, disbursement date, repayment schedule (typically 3–6 monthly installments for salary advance; 6–12 months for calamity/company loan), interest rate (salary advance: 0% per company policy; calamity loan: 0% per DOLE guidance; company loan: 6% per annum or BIR-prescribed minimum per arm's-length rules if officer/owner), monthly deduction amount | Payroll Officer | Payroll Manager | 10 min/loan |
| 5 | System disburses loan: salary advance included in next semi-monthly payroll run as a separate non-taxable line item (Dr. Employee Loans Receivable / Cr. Cash); calamity and company loans processed via separate bank transfer (Dr. Employee Loans Receivable / Cr. Cash) within 3 business days of approval | System / Treasury Analyst | Payroll Manager | Automated + 15 min |
| 6 | System automatically deducts monthly loan repayment from employee's payroll per schedule (Dr. Cash / Cr. Employee Loans Receivable); deduction appears as separate line on payslip; if employee's net pay would fall below minimum wage after deduction, system reduces deduction amount and extends repayment period | System | — | Automated |
| 7 | Monthly: Payroll Officer generates loan portfolio report — total outstanding loans by type, aging (current vs. overdue), delinquency rate, new disbursements, collections; Finance Manager reviews for provisioning adequacy | Payroll Officer | Finance Manager | 1 hour/month |
| 8 | **Employee separation with outstanding loan**: at separation (W43), Payroll Officer settles outstanding loan balance from final pay (W10 step 12) — system deducts remaining principal and accrued interest from final pay before other deductions; if final pay insufficient to cover full loan balance, employee signs promissory note for remaining balance and Payroll Officer tracks post-employment collection; write-off per Controller approval if uncollectible | Payroll Officer / Controller | Finance Manager | Per W43 |

### System Touchpoints
- Loan/advance request form in self-service portal with eligibility validation (employment status, tenure, outstanding loans) (W76.1–2)
- Loan record creation with amortization schedule and automatic payroll deduction (W76.4, W76.6)
- Loan disbursement via payroll or bank transfer with GL posting (W76.5)
- Loan portfolio reporting: outstanding, aging, delinquency, disbursements, collections (W76.7)
- Final pay settlement of outstanding loans at separation (W76.8)
- Minimum wage protection: system ensures net pay does not fall below minimum wage after loan deduction (W76.6)
- Integration with W10 (payroll deduction), W43 (separation — final pay settlement), W49 (calamity loan trigger), W51 (self-service portal)

### Time Estimate
- Employee request submission: 10 min
- HR eligibility verification: 15 min/request
- Approval routing: 10 min/request
- Loan record creation and disbursement: 10 min/loan + 15 min manual processing
- Monthly portfolio reporting: 1 hour/month
- **Total**: ~40–70 hours/month for HR Assistant + Payroll Officer across 100–200 requests

### Pain Points / Risks
- **Post-typhoon volume surge**: Calamity loan requests spike dramatically after typhoons (W49), potentially overwhelming HR capacity when staff themselves may be affected by the same disaster
- **Minimum wage floor constraint**: System must dynamically reduce loan deductions when net pay would fall below minimum wage, extending repayment periods and increasing delinquency risk
- **Separation-time recovery shortfall**: Final pay often insufficient to cover outstanding loan balances for separated employees; post-employment collection is difficult and write-off rates are high
- **Policy inconsistency risk**: Multiple loan types (salary advance, calamity, company) with different eligibility rules and approval tiers create confusion; HR Assistants may misclassify loans, leading to incorrect interest rates or approval authority bypass

### Staffing Implication
- **HR Assistant**: ~100–200 requests/month × 15 min = ~25–50 hours/month. Absorbed within existing 2 HR Assistants.
- **Payroll Officer**: loan creation + portfolio reporting adds ~15 hours/month. Absorbed within existing payroll team.
- **No incremental headcount.**

---

## W172. Employee PPE & Uniform Lifecycle

| Field | Detail |
|---|---|
| **Trigger** | New hire onboarding; or periodic replacement schedule; or damage/loss report |
| **Frequency** | Annual mass distribution; semi-annual replenishment; ad-hoc for new hires |
| **Volume** | ~6,715 employees; ~20,700 sets of uniforms (3 per employee) + safety gear |
| **Owner** | HR Operations Manager |
| **Participants** | HR Assistant, Store/DC Manager, Procurement, Vendor, Employee |

### Background

With over 6,715 employees in retail and distribution, maintaining a consistent professional image and ensuring safety compliance (PPE) is a significant logistical task. BuildRight provides uniforms and mandatory safety gear (safety shoes, helmets, vests) to all store and DC personnel.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Sizing & Allocation**: During onboarding (W15), HR Assistant captures employee sizes (shirt, pants, shoes); system assigns standard entitlement (e.g., 3 shirts, 2 pants, 1 pair of safety shoes, 1 helmet) | HR Assistant | HR Ops Manager | 10 min |
| 2 | **Issuance**: HR Assistant issues gear from store/DC stock; employee signs "Property Acknowledgment" in the system/portal; system links items to employee ID for accountability | HR Assistant | Store/DC Mgr | 15 min |
| 3 | **Inventory Tracking**: System tracks PPE/Uniform stock as "Internal Use Inventory"; replenishment triggered via W4 when stock falls below reorder point | HR Assistant | Procurement | Automated |
| 4 | **Replacement**: (a) **Periodic**: Every 12 months, employees are eligible for a new set; (b) **Damage**: If gear is damaged in the line of duty, employee returns old item for a free replacement; (c) **Loss**: If lost, employee pays a replacement fee via payroll deduction (W10) | HR Assistant | Store/DC Mgr | 10 min |
| 5 | **Return at Separation**: Upon separation (W43), employee must return all non-consumable gear (helmets, vests, badges); HR Assistant verifies return before final clearance approval | HR Assistant | Dept Head | 15 min |
| 6 | **Audit**: Quarterly: HR Ops Manager audits PPE compliance on the floor (ensuring correct shoes/helmets worn); feeds into W72 Performance Review | HR Ops Mgr | Store/DC Mgr | 2 hours/site |

### System Touchpoints
- Employee entitlement module (linking roles to specific PPE requirements)
- Property acknowledgment log with digital signature
- Payroll deduction integration for lost items (W10)
- Internal-use inventory replenishment (W4)
- PPE compliance flag in Performance Management (W72)

### Time Estimate
- Sizing and allocation (new hire): 10 min/employee
- Issuance and acknowledgment: 15 min/employee
- Replacement processing: 10 min/request
- Separation return verification: 15 min/employee
- Quarterly compliance audit: 2 hours/site
- **Annual mass distribution**: ~1 week of coordinated effort per site

### Pain Points / Risks
- **Sizing errors and exchanges**: Incorrectly sized uniforms (especially safety shoes) generate costly exchanges and delays; store-level sizing is approximate and return rates to vendor can be high
- **Stock availability at 200 locations**: Maintaining adequate PPE/uniform stock across 200 stores and 4 DCs is a distribution challenge; new hires may wait weeks for proper-sized gear, creating safety compliance gaps
- **Lost gear recovery at separation**: Employees frequently fail to return non-consumable items (helmets, vests, badges) at separation; payroll deduction for replacement is often insufficient and erodes employee goodwill during offboarding
- **Vendor lead time for custom-branded items**: Uniforms with BuildRight branding require 4–6 week lead times from vendor; poor demand forecasting during new store openings (W16) can leave new hires without proper attire

### Staffing Implication
- **HR Ops Manager**: quarterly compliance audits at 204 sites (200 stores + 4 DCs) × 2 hours/site = ~410 hours/year; with ~8 audits/quarter across the team, this is absorbed within the HR Ops Manager role supplemented by HR Assistants.
- **HR Assistants (2)**: sizing/issuance for ~1,200–1,600 new hires/year × 25 min each = ~500–660 hours/year (~40–55 hours/month); replacement processing adds ~20–30 hours/month. Absorbed within existing 2 HR Assistants.
- **Store/DC Managers**: 15 min per issuance event and 15 min per separation return. With ~130 separations/month spread across 200+ locations, most managers handle < 1 event/month. Absorbed.
- **No incremental headcount.**

---

## W178. Employee Succession & Internal Mobility

| Field | Detail |
|---|---|
| **Trigger** | Retirement of key leader; store expansion; or high-potential (HiPo) identification |
| **Frequency** | Annual HiPo review and succession mapping; ongoing internal postings per vacancy |
| **Volume** | ~200 Store Manager and ~30 HQ Director/Manager roles requiring succession plans; ~30–50 internal promotions/transfers per year |
| **Owner** | CHRO |
| **Participants** | CEO, Department Heads, HR Manager, High-Potential Employees |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **HiPo Identification**: Annual review of performance (W72) and potential; tag employees for "Internal Mobility" in ERP | HR Manager | CHRO | 2 weeks |
| 2 | **Succession Mapping**: Identify "Ready Now" and "Ready in 1–2 Years" successors for all Store Manager and HQ Director roles | Department Head | CEO | 1 week |
| 3 | **Individual Development Plan (IDP)**: Successors assigned to specific training (W51) and cross-functional rotations | HR Manager | — | 1 year |
| 4 | **Internal Posting**: Vacancies posted internally for 5 days before external search; system alerts eligible internal candidates | System | HR Manager | Automated |
| 5 | **Transfer/Promotion**: Selected candidate's contract and payroll (W10) updated; system auto-triggers offboarding from old role and onboarding to new | System / HR | — | 30 min |

### System Touchpoints
- Talent pool tagging in HRIS
- Career path visualization and tracking
- Automatic internal job alerts based on profile

### Time Estimate
- HiPo identification and tagging: 2 weeks/year (HR Manager, Department Heads)
- Succession mapping: 1 week/year (Department Heads + CEO)
- Individual Development Plan creation: Ongoing over 1 year
- Internal vacancy posting: Automated
- Transfer/Promotion processing: 30 min/employee
- **Total annual effort**: ~3 weeks concentrated effort from senior leadership plus ongoing IDP management

### Pain Points / Risks
- **Thin leadership bench**: With 200 stores requiring 200 Store Managers, identifying and developing enough "Ready Now" successors for rapid expansion (10–15 new stores/year) is a persistent challenge; many successors are "Ready in 1–2 Years" which creates a pipeline gap
- **Succession plan secrecy vs. transparency**: Employees tagged as HiPo may expect accelerated promotion; if organizational growth slows, frustrated HiPo employees may leave for competitors, creating a talent drain
- **Internal posting bypass risk**: Hiring managers may pre-select external candidates before the 5-day internal posting window closes, undermining employee trust in the internal mobility program and triggering grievances
- **Cross-entity transfer complexity**: Moving employees between BuildRight's 5 legal entities requires full separation and re-onboarding (W43.15); the administrative burden discourages cross-entity mobility and keeps talent siloed within entities

### Staffing Implication
- **CHRO + HR Manager**: ~3 weeks/year of concentrated effort for HiPo identification, succession mapping, and IDP oversight. Absorbed within existing senior HR roles.
- **Department Heads + CEO**: ~1 week/year for succession mapping reviews. Absorbed as part of strategic planning duties.
- **HR Assistants**: ~30 min per transfer/promotion processing × 30–50 per year = ~15–25 hours/year. Negligible.
- **No incremental headcount.**

---

## W179. Management Trainee (Cadetship) Program

| Field | Detail |
|---|---|
| **Trigger** | Annual corporate strategy (10–15 new stores/year growth) |
| **Frequency** | Annual intake (Cohort-based) |
| **Volume** | ~30–50 trainees per year |
| **Owner** | CHRO |
| **Participants** | Store Managers (Mentors), Trainees, Learning & Development Team |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Recruitment**: Campus hiring and assessment centers targeting fresh graduates | HR Manager | — | 2 months |
| 2 | **Orientation**: 1-week corporate orientation at HQ | L&D Team | CHRO | 1 week |
| 3 | **Rotational Training**: 6-month rotation through all store departments (Receiving, Sales, Cashier, Operations) | Trainee | Store Manager | 6 months |
| 4 | **Project Assignment**: Trainees assigned a "Process Improvement" project in a specific store | Trainee | Dept Head | 2 months |
| 5 | **Graduation & Deployment**: Successful trainees deployed as "Assistant Store Managers" or "Department Supervisors" in new stores | CHRO | CEO | — |

### System Touchpoints
- Training progress tracking (W51)
- Rotation schedule management (W34)
- Trainee-to-Mentor mapping and feedback loop

### Time Estimate
- Campus recruitment and assessment centers: 2 months/year
- Corporate orientation at HQ: 1 week
- Rotational training: 6 months per cohort
- Project assignment: 2 months per cohort
- Graduation and deployment: 1–2 weeks
- **Total cycle time**: ~9–10 months from recruitment to deployment as Assistant Store Manager / Department Supervisor

### Pain Points / Risks
- **Trainee attrition during rotation**: 6-month rotation across store departments is demanding; trainees may resign for competing offers, especially from BPO sector offering higher starting pay, wasting the company's recruitment and training investment
- **Mentor availability and quality**: Store Managers serving as mentors are already managing full store operations; mentoring quality varies significantly, and some trainees receive inadequate guidance during rotations
- **Deployment bottleneck**: If new store openings are delayed, graduates of the cadetship program compete for limited Assistant Store Manager slots, creating retention risk among highly trained candidates who expected immediate promotion
- **Assessment center cost and scalability**: Running assessment centers for 30–50 candidates annually requires external facilitator fees and venue costs (~PHP 500K–1M/year); scaling the program beyond 50 trainees would require significant additional investment

### Staffing Implication
- **CHRO**: oversees program design and graduation/deployment decisions (~1 week/year for recruitment and deployment phases). Absorbed.
- **L&D Team**: 1-week corporate orientation + ongoing rotation supervision + project assignment oversight = ~20–30 hours/month during active cohort periods. Requires 1 dedicated L&D Coordinator (can be the Training Officer or a dedicated program coordinator within the HR team).
- **Store Managers (mentors)**: 200 Store Managers serve as rotation mentors; ~2–4 hours/week per active trainee assignment. With 30–50 trainees rotating across stores, most mentors handle 1 trainee at a time. Absorbed but adds supervisory load during rotation periods.
- **Assessment center external cost**: ~PHP 500K–1M/year for external facilitators and venue. Budgeted within HR/L&D operating budget.
- **No incremental headcount** — L&D Coordinator role can be absorbed within existing Training Officer role or HR team.

---

## W251. Philippine Statutory Benefits & Claims Administration (SSS, PhilHealth, Pag-IBIG)

| Field | Detail |
|---|---|
| **Trigger** | Employee sickness event, maternity event, or application for SSS/Pag-IBIG statutory loan |
| **Frequency** | Continuous; daily processing of claims and semi-monthly reconciliation |
| **Volume** | 6,715 employee base; average ~120–180 sickness claims/month, ~40–60 maternity leaves/month, and ~250–350 loan applications/month |
| **Owner** | HR Benefits Specialist |
| **Participants** | Employee, HR Benefits Specialist, Payroll Specialist, Finance (Treasury) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Claim Submission**: Employee uploads medical certificate, SSS Maternity Notification, or loan request documents to the HRIS/ERP system via Employee Self-Service (ESS) portal (W251.1) | Employee | — | 15 min |
| 2 | **Eligibility Verification**: HR Benefits Specialist reviews the uploaded documents; system auto-checks employee contribution history against SSS/PhilHealth criteria to verify eligibility (W251.2) | HR Benefits | CHRO | 30 min |
| 3 | **Agency Portal Certification**: HR Benefits Specialist logs into the government agency's online portal (SSS Sickness/Maternity portal, Pag-IBIG Virtual Employer portal) to certify the employee's leave or confirm the employer endorsement for a salary/calamity loan (W251.3) | HR Benefits | — | 20 min |
| 4 | **Benefit Advance Computation**: For SSS Sickness/Maternity, under Philippine law, the employer must advance the SSS benefit. System automatically computes the daily SSS benefit rate based on the employee's average daily salary credit and schedules the advance payment (W251.4) | System | Payroll Mgr | Automated |
| 5 | **Payroll Disbursal**: Payroll Specialist reviews the computed statutory advance and approves it for inclusion in the next semi-monthly payroll run (W10) (W251.5) | Payroll Spec | Payroll Mgr | 10 min |
| 6 | **Reimbursement Claim Submission**: After the employee returns or the leave completes, HR Benefits Specialist submits a digitized SSS Reimbursement Claim via the online portal to recover the advanced amount from the government (W251.6) | HR Benefits | — | 15 min |
| 7 | **Reconciliation & Settlement**: SSS releases the reimbursement via direct deposit to the company's bank account. Finance reconciles the incoming bank settlement against the SSS Receivable ledger to close the transaction loop (W251.7) | Treasury / Accountant | Controller | 30 min |
| 8 | **Loan Deduction Scheduling**: For SSS/Pag-IBIG loans, once approved, the system imports the monthly electronic billing files from SSS/Pag-IBIG, matches loan accounts with active employee profiles, and schedules the statutory semi-monthly deductions in the payroll system, ensuring compliance with minimum wage take-home pay rules (W251.8) | System | Payroll Mgr | Automated |

### System Touchpoints
- Employee Self-Service (ESS) portal for digital document upload and notification tracking
- HRIS Integration with Payroll (W10) for automated advanced benefit calculation and statutory loan deductions
- General Ledger integration: SSS Receivable reconciliation and bank settlement auto-matching (W89)
- Government billing file import interface (semi-monthly SSS and Pag-IBIG billing formats)

### Time Estimate
- Claim submission (employee): 15 min/claim
- Eligibility verification: 30 min/claim
- Agency portal certification: 20 min/claim
- Benefit advance computation: Automated
- Payroll disbursal review: 10 min/claim
- Reimbursement claim submission: 15 min/claim
- Reconciliation and settlement: 30 min/claim
- **Total HR Benefits effort**: ~120–180 sickness claims + 40–60 maternity claims + 250–350 loan applications per month = ~60–80 hours/month

### Pain Points / Risks
- **SSS reimbursement delays**: Government reimbursement processing times are unpredictable (30–90 days), creating cash flow pressure as the company must advance employee benefits before recovering from SSS; the SSS Receivable ledger can grow significantly
- **Government portal downtime**: SSS and Pag-IBIG online portals experience frequent outages and slow performance, especially during deadline periods; HR Benefits Specialists lose productive time and miss filing windows
- **Contribution history discrepancies**: Mismatches between company records and government agency records (due to data entry errors, late posting by agencies, or employee transfer between employers) require manual reconciliation for each affected employee
- **Regulatory change frequency**: SSS contribution table changes, PhilHealth premium rate adjustments, and Pag-IBIG fund rule changes require timely system updates; failure to update payroll tables results in under/over-deduction and potential penalties

### Staffing Implication
- **HR Benefits Specialist (1–2)**: ~60–80 hours/month handling 400–590 claims and loan applications. With 2 specialists, ~30–40 hours each/month. This is a full-time role; recommend 2 dedicated Benefits Specialists within the HR team.
- **Payroll Specialist**: ~10 min per disbursal review × ~400–590 claims/month = ~65–100 hours/month. Shared with existing payroll team (W10).
- **Treasury / Accountant**: ~30 min per reconciliation × ~120–180 sickness claims + 40–60 maternity claims = ~80–120 hours/month. Shared with Finance team.
- **Fits within the ~16-person HR team** with 2 dedicated Benefits Specialists.


---

## W269. Vendor Promodizer & Third-Party Staff Management

| Field | Detail |
|---|---|
| **Trigger** | Vendor assigns a promodizer to a specific store location. |
| **Frequency** | Daily / As needed |
| **Volume** | 2-10 promodizers per store |
| **Owner** | Store Manager |
| **Participants** | Promodizer, Vendor Account Manager, Store Admin |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Vendor submits promodizer credentials and schedule to HR. | Store Manager | HR Admin | 15 min |
| 2 | Store Admin creates a non-employee profile in the system. | Security Guard | Store Manager | 10 min |
| 3 | System provisions limited POS access (for sales attribution) and biometric attendance profile. | Vendor Account Mgr | Store Manager | 15 min |
| 4 | Promodizer logs time in/out; data is shared with vendor for their payroll. | Store Manager | HR Admin | 5 min/day |
| 5 | Store Manager reviews promodizer sales performance and revokes access upon offboarding. | HR Admin | HR Director | 20 min |

### System Touchpoints
- HR (Non-Employee Master)
- Time & Attendance
- POS (Sales Attribution)
- Security (Access Control)

### Time Estimate
- Vendor credential submission and HR review: 15 min/promodizer
- Non-employee profile creation: 10 min/promodizer
- POS access and biometric provisioning: 15 min/promodizer
- Daily time logging and vendor data sharing: 5 min/day per promodizer
- Sales performance review and access revocation: 20 min/offboarding
- **Total per onboarding cycle**: ~60 min; **Total per offboarding**: ~20 min

### Pain Points / Risks
- **Unauthorized access risk**: Promodizers with limited POS access may attempt to process voids, price overrides, or manager-level functions if role-based access control is not strictly enforced; insufficient access revocation at offboarding leaves dormant accounts vulnerable to misuse
- **Missing sales attribution for commissions**: If POS transactions are not properly tagged to promodizer IDs, vendor commissions cannot be accurately calculated, leading to billing disputes and potential over/under-payment to vendor partners
- **Unaccounted headcount during emergencies**: Promodizers are not BuildRight employees and may not appear in emergency headcount systems; during fire drills, typhoons (W49), or security incidents (W37), unregistered promodizers create safety and accountability gaps
- **Vendor data sharing compliance**: Sharing attendance and sales data with third-party vendors must comply with RA 10173 data privacy requirements; failure to include data-sharing provisions in vendor agreements creates regulatory exposure

### Staffing Implication
- **Store Manager**: ~15 min per promodizer onboarding + 20 min per offboarding. With 2–10 promodizers per store, this averages ~30–90 min/store/month. Absorbed into existing duties.
- **HR Admin**: ~15 min per credential review. With 200 stores × average 5 promodizers, centralized HR handles ~1,000 profiles. ~25 hours/month total. Absorbed within HR team.
- **No incremental headcount.**


---

## W280. Court-Ordered Wage Garnishment & Third-Party Deductions

| Field | Detail |
|---|---|
| **Trigger** | HR receives a legal order or authorized request to deduct funds directly from an employee's net pay (e.g., child support, cooperative loan, union dues). |
| **Frequency** | Bi-weekly payroll cycle |
| **Volume** | 50-100 employees affected |
| **Owner** | Payroll Manager |
| **Participants** | HR Admin, Legal, Employee, Third-Party Payee |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Legal/HR receives and verifies the garnishment order or loan agreement. | Payroll Admin | Payroll Manager | 15 min |
| 2 | Payroll Admin configures a recurring deduction wage type in the employee's compensation profile. | Legal Counsel | HR Director | 20 min |
| 3 | System logic applies prioritization rules (e.g., statutory taxes first, court orders second, voluntary loans third) to ensure net pay does not fall below legal minimums. | Payroll Manager | CFO | Automated |
| 4 | Payroll runs; funds are deducted and booked to a specific AP liability account. | Payroll Admin | Payroll Manager | 10 min |
| 5 | Finance remits the consolidated deducted funds to the court, union, or cooperative. | HR Admin | HR Director | 15 min |

### System Touchpoints
- HR Payroll Engine (Deduction Rules)
- General Ledger
- Accounts Payable

### Time Estimate
- Garnishment order receipt and verification: 15 min/order
- Deduction wage type configuration: 20 min/order
- Payroll deduction processing: Automated per run
- Post-run verification and AP booking: 10 min/employee
- Remittance to court/union/cooperative: 15 min/batch
- **Total per new garnishment setup**: ~60 min; **Ongoing per payroll run**: ~10 min verification per affected employee

### Pain Points / Risks
- **Legal liability for non-compliance**: Failure to implement a court-ordered garnishment on time exposes BuildRight to contempt of court charges, fines, and potential liability for the full garnishment amount; manual tracking of court deadlines is error-prone across 50–100 affected employees
- **Complex deduction prioritization logic**: When an employee has multiple simultaneous deductions (statutory taxes, SSS/PhilHealth/Pag-IBIG loans, court garnishment, company loans), the system must apply strict prioritization rules while ensuring net pay does not fall below minimum wage; incorrect prioritization creates legal and employee relations issues
- **Garnishment order changes and terminations**: Court orders may be modified (increased, decreased, or terminated) with varying effective dates; failure to update deduction configurations promptly results in over- or under-deduction requiring manual correction and potential restitution
- **Employee privacy and morale**: Garnishment orders are sensitive legal matters; Payroll Officers with access to garnishment data must maintain strict confidentiality; employees facing wage garnishment may experience financial stress affecting performance and retention

### Staffing Implication
- **Payroll Admin**: ~15 min per garnishment setup × 50–100 affected employees = ~12–25 hours/month for initial setups and modifications. Absorbed within existing payroll team.
- **Legal Counsel**: ~20 min per order verification. With 5–10 new orders/month, ~2–3 hours/month. Absorbed within Legal team.
- **HR Admin**: ~15 min per remittance batch, typically 2–4 batches per payroll run = ~2–4 hours/month. Absorbed within HR team.
- **No incremental headcount.**

---

## W429. Vendor-Funded Promodizer Incentive Management

| Field | Detail |
|---|---|
| **Trigger** | Vendor launches a sales incentive program (SPIFF) for their promodizers |
| **Frequency** | Monthly or per promotional event |
| **Volume** | ~500–1,000 active promodizers across 200 stores |
| **Owner** | HR Operations Manager |
| **Participants** | Store Manager, Category Manager, Vendor Account Manager, Payroll Officer |

### Background

Promodizers (vendor-provided staff) are often given cash incentives by their parent vendors based on sales performance of specific SKUs within BuildRight stores. To prevent "side-payments" that could bypass company transparency and integrity policies, BuildRight requires all vendor-funded incentives to be declared, validated against POS data, and ideally processed via BuildRight's administrative system (recharged to the vendor) or strictly monitored. This workflow ensures that promodizer incentives do not create conflicts of interest or "dark" labor costs.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Incentive Declaration**: Vendor Account Manager submits the "Promodizer Incentive Program" mechanics (SKUs, target levels, payout rates) to the Category Manager for approval | Vendor Account Mgr | Category Mgr | 30 min |
| 2 | **System Configuration**: HR Assistant tags the approved promodizers and the covered SKUs in the "Incentive Tracking Module" (linked to W269 sales attribution) | HR Assistant | HR Ops Manager | 20 min |
| 3 | **Monthly Sales Validation**: System generates a "Promodizer Sales Achievement Report" showing actual POS sales for the target SKUs attributed to each promodizer ID (W269.3) | System | — | Automated |
| 4 | **Incentive Computation**: HR Assistant computes the incentive payout per promodizer based on the validated POS data; Vendor verifies the total | HR Assistant | Vendor Account Mgr | 1 hour |
| 5 | **Vendor Billing**: Finance generates a "Service Invoice" to the Vendor for the total incentive amount + an administrative fee (e.g., 5%) for processing | AR Clerk | Finance Mgr | 20 min |
| 6 | **Payout Execution**: Upon receipt of vendor payment, BuildRight dispatches the incentive to promodizers (either via a separate payroll run or via the Vendor's agency) | Payroll Officer | HR Ops Manager | 30 min |
| 7 | **Audit & Integrity Check**: Compliance Manager reviews a sample of payouts to ensure no unauthorized "direct-to-promodizer" cash payments were made by vendors in violation of the "No-Gift Policy" (W426) | Compliance Manager | CHRO | 2 hours/month |

### System Touchpoints

- Incentive Tracking Module: links promodizer IDs (W269) to specific SKUs and payout logic (W429.2)
- Promodizer Sales Achievement Report: real-time POS attribution report (W429.3)
- Integration with W269 (Promodizer Management), W426 (Gift Policy), and W7C (Non-PO Invoicing)

### Pain Points / Risks

- **Side-Payments**: Vendors paying promodizers cash "under the table" to prioritize their brands over more profitable house brands; undermines BuildRight's merchandising strategy
- **Sales Misattribution**: If a cashier fails to scan the promodizer's ID at POS (W269), the incentive is not credited, leading to promodizer frustration and data inaccuracy
- **Billing Delays**: Vendors may delay payment of the "Incentive Invoice," leaving BuildRight in a difficult position regarding the disbursement to the promodizers

### Staffing Implication

Effort is primarily administrative (Category Manager approval and HR Assistant validation). Total: ~10–15 hours/month across the HR team.

### Time Estimate
**Total**: Declaration — 30 min; Validation & Billing — 2 hours/month; Audit — 2 hours/month; **Total cycle: ~5 hours per month per major vendor program**

---

## W449. Promodizer Labor Compliance & DOLE 174 Governance

| Field | Detail |
|---|---|
| **Trigger** | Quarterly HR Compliance Audit cycle |
| **Frequency** | Quarterly |
| **Volume** | ~500–1,000 active promodizers across 200 stores |
| **Owner** | HR Compliance Manager |
| **Participants** | Store Manager, HR Assistant, Legal, Vendor Account Manager |

### Background

Under Philippine **DOLE Department Order 174**, "Labor-Only Contracting" is prohibited. Promodizers (third-party staff) must not be treated as regular employees and must not perform "core" functions or be under the direct supervision of BuildRight managers for their daily work methods.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Desk Audit**: Review current promodizer list (W269) and vendor service agreements for compliant DOLE-174 clauses | HR Compliance Mgr | CHRO | 1 day |
| 2 | **On-site Observation**: Randomly visit stores to observe promodizer activities; ensure they are not performing cashiering, inventory receiving, or store cleaning | HR Compliance Mgr | Store Manager | 4 hours/site |
| 3 | **Interview**: Conduct brief interviews with promodizers to confirm they receive instructions from their agency, not BuildRight | HR Compliance Mgr | — | 15 min/person |
| 4 | **Documentation Review**: Verify that vendors submit monthly proof of SSS/PhilHealth/Pag-IBIG remittances for their deployed staff | HR Assistant | HR Compliance Mgr | 1 hour/vendor |
| 5 | **Gap Analysis**: Document any "co-employment" risks (e.g., BuildRight managers issuing disciplinary memos to promodizers) | HR Compliance Mgr | Legal | 2 hours |
| 6 | **Remediation**: Issue "Corrective Action Request" to Store Managers or Vendors found in violation of DOLE-174 guidelines | HR Compliance Mgr | CHRO | 1 hour |

### System Touchpoints
- Vendor Master: storage of Service Agreements and DOLE-174 registration certificates
- HRIS: non-employee profile tagging (W269)
- Compliance Dashboard: tracking audit findings and remediation status

### Pain Points / Risks
- **Creeping Control**: Store Managers often treat long-term promodizers as "their own" staff, giving them direct orders and including them in store huddles
- **Regularization Risk**: Misclassification can lead to mandatory regularization of thousands of workers, impacting financial sustainability
- **Vendor Non-compliance**: Small vendors may fail to pay statutory benefits, creating secondary liability for BuildRight

### Time Estimate
- Quarterly audit: ~1–2 weeks total effort for HR Compliance Manager across sample sites
- Ongoing vendor documentation review: 4 hours/month

---

## W493. Labor Union & Collective Bargaining Management

| Field | Detail |
|---|---|
| **Trigger** | Union certification petition filed with DOLE; collective bargaining agreement (CBA) expiration (60-day freedom period); labor dispute or strike notice |
| **Frequency** | Event-driven (certification, CBA negotiation, disputes); CBA renewal every 3–5 years per affected unit |
| **Volume** | 0–2 active CBA negotiations/year; ongoing union relationship management |
| **Owner** | CHRO |
| **Participants** | CEO, CFO, COO, VP Legal, HR Labor Relations Manager, External Labor Counsel, Union Representatives, NCMB, DOLE |

### Background

With 6,715 employees across 200 stores, 4 DCs, and HQ, BuildRight is exposed to labor union organizing activity. Under the Philippine Labor Code, employees have the right to self-organization and collective bargaining (Article 244). Labor unions in Philippine retail typically organize by establishment or by category of employees (e.g., rank-and-file store employees, warehouse workers). If certified as the exclusive bargaining representative by DOLE through a certification election, BuildRight must bargain in good faith with the union for a Collective Bargaining Agreement (CBA). CBA negotiations cover wages, benefits, working conditions, grievance procedures, and no-strike/no-lockout provisions. This workflow covers the full lifecycle: prevention/preparation, certification response, CBA negotiation, CBA administration, and dispute resolution. None of the existing HR workflows (W10–W79) address labor union management.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Union Prevention & Employee Engagement**: Proactive measures to maintain direct employee relationships: (a) CHRO ensures competitive compensation and benefits benchmarking against retail industry peers; (b) regular town halls and employee feedback mechanisms (W79 — grievance channel); (c) transparent communication on company performance and policies; (d) Store Manager training on positive labor relations (no anti-union threats or intimidation per Article 248 — unfair labor practice); (e) monitor employee sentiment indicators (turnover rates, grievance volume, exit interview themes per W43) | CHRO / HR Labor Relations Manager | CEO | Ongoing |
| 2 | **Union Organizing Activity Detection & Response**: If union organizing activity is detected: (a) HR Labor Relations Manager monitors for signs: employee meetings, distribution of union materials, inquiries about labor rights, DOLE certification petition filing; (b) brief CEO, CFO, COO, and VP Legal on situation; (c) engage external labor counsel for legal guidance; (d) ensure management actions comply with Labor Code Article 248 (prohibited acts: dismissal, discrimination, interference, coercion); (e) prepare management's position for potential certification election; (f) conduct supervisory training on lawful and unlawful conduct during organizing campaigns | HR Labor Relations Manager | CHRO | Event-driven |
| 3 | **Certification Election Response**: If a union petitions DOLE for certification election: (a) VP Legal reviews petition for procedural compliance; (b) prepare list of employees in the proposed bargaining unit (ensure correct scope — e.g., rank-and-file only, excluding supervisors/managers); (c) attend DOLE-mediated pre-election conference; (d) management may participate in the election process as observer (but cannot campaign against the union); (e) if union wins certification: acknowledge result and prepare for CBA negotiation; (f) if union loses: document outcome and continue employee engagement | VP Legal / HR Labor Relations Manager | CEO | 30–60 days |
| 4 | **CBA Negotiation**: If union is certified as bargaining representative: (a) CHRO assembles management's CBA negotiation panel: CHRO, VP Legal, Finance representative, Store Ops representative, External Labor Counsel; (b) prepare management's CBA proposals: economic provisions (wage increases, benefits, 13th month enhancements, rice/medical allowances), non-economic provisions (grievance procedure, no-strike clause, union security clause, management prerogatives); (c) conduct collective bargaining sessions with union panel (typically 10–30 sessions over 3–6 months); (d) if deadlock on economic provisions: file notice of strike with NCMB (or union files); (e) attend NCMB conciliation-mediation conferences; (f) if agreement reached: draft CBA and submit to affected employees for ratification; (g) if no agreement after conciliation: union may vote to strike; management may declare lockout (last resort) | CHRO / VP Legal | CEO | 3–12 months |
| 5 | **CBA Registration & Implementation**: Upon CBA ratification: (a) register CBA with DOLE Regional Office (mandatory within 30 days of ratification per Article 231); (b) distribute CBA copies to all affected employees; (c) update HR policies and payroll (W10) to reflect CBA provisions (new wage rates, new benefits, new leave types, new grievance procedures); (d) train Store Managers and supervisors on CBA provisions and their obligations; (e) update employee handbook and SOPs (W186) to align with CBA | HR Labor Relations Manager | CHRO | 30 days |
| 6 | **CBA Administration**: During CBA term (typically 3–5 years): (a) HR Labor Relations Manager manages ongoing CBA compliance: ensure all economic provisions are implemented (wage increases, benefits, allowances); (b) attend regular labor-management meetings (typically quarterly) with union representatives to discuss issues, resolve grievances at the first step, and build cooperative relationship; (c) track CBA provision deadlines (wage increase effective dates, benefit implementation dates); (d) ensure management prerogative clauses are exercised within CBA boundaries; (e) prepare for CBA renewal negotiation (60-day freedom period before expiry) | HR Labor Relations Manager | CHRO | Ongoing |
| 7 | **Grievance Handling Under CBA**: For employee grievances filed through the CBA grievance machinery: (a) Step 1: Employee and Union Steward present grievance to immediate supervisor (Store Manager); (b) Step 2: If unresolved, escalate to HR Labor Relations Manager; (c) Step 3: If unresolved, escalate to CHRO and Union President; (d) Step 4: If unresolved, submit to voluntary arbitration (per CBA provision); maintain documentation at each step; ensure timelines per CBA grievance procedure are met; coordinate with W79 (employee grievance & whistleblower) for non-union-related grievances | HR Labor Relations Manager | CHRO | Per grievance |
| 8 | **Strike/Lockout Contingency**: If a notice of strike is filed: (a) CHRO activates strike contingency plan: (b) assess which stores/DCs are affected (union may not represent all locations); (c) prepare temporary staffing plan (skeletal workforce from non-union stores, agency workers — but cannot hire permanent replacement workers during strike); (d) ensure store physical security (W71) for picket line management; (e) coordinate with LGU and PNP for peace and order during picket (W209, W471); (f) VP Legal assesses legality of strike (procedural requirements: strike vote, notice to DOLE, cooling-off period); (g) continue NCMB conciliation to seek resolution; (h) if strike occurs: maintain minimum operations (management employees can perform bargaining unit work under Philippine law); (i) document all events for potential unfair labor practice filings | CHRO / VP Legal | CEO | Event-driven |

### System Touchpoints
- HRIS: employee records by bargaining unit, union membership status, CBA provision tracking
- Payroll Module (W10): CBA wage increase implementation, benefit administration
- Compliance Dashboard: CBA compliance tracking, grievance status monitoring
- Document Management (W255): CBA registration, grievance records, negotiation minutes
- Integration with W10 (payroll), W15 (onboarding — union orientation), W43 (separation — CBA-related termination provisions), W72 (performance — CBA disciplinary procedures), W79 (grievance — non-union channel), W186 (SOP governance — CBA policy alignment)

### Pain Points / Risks
- **Multi-location fragmentation**: A union may organize only certain stores or regions, creating a patchwork of unionized and non-unionized locations with different wage scales, benefits, and working conditions — administratively complex and creating employee resentment across locations
- **CBA cost impact**: Union-negotiated wage increases and benefits above market rates can significantly impact BuildRight's labor cost structure (currently ~10–12% of revenue); for a chain operating on 12–14% EBITDA margins, a 2–3% increase in labor costs is material
- **Management prerogative erosion**: CBAs typically constrain management's ability to unilaterally change work rules, schedules (W34), job assignments, and disciplinary procedures; this can reduce operational flexibility in a dynamic retail environment
- **Strike risk during peak season**: A strike during the Christmas peak (November–December, which can represent 15–20% of annual revenue) would be devastating; CBA negotiations must be timed to avoid peak season disruption
- **Political and community pressure**: In the Philippines, labor disputes attract political attention (barangay officials, city councilors, DOLE intervention); community pressure (W209) can force management into unfavorable settlements

### Time Estimate
- Union prevention and employee engagement: ~10–15 hours/month (absorbed into existing CHRO/HR duties)
- Certification election response: ~40–80 hours over 30–60 days
- CBA negotiation: ~200–400 hours over 3–12 months (management panel)
- CBA administration: ~8–12 hours/month
- Grievance handling: ~4–8 hours/grievance
- **Total during active CBA negotiation year**: ~400–600 hours for CHRO and management panel

### Staffing Implication
- **CHRO**: Leads labor relations strategy and CBA negotiation. ~200–400 hours during CBA negotiation year; ~50–80 hours/year during CBA administration.
- **HR Labor Relations Manager**: Dedicated labor relations function. If not existing, may need to be created or assigned from existing HR team. ~100–200 hours/year during CBA administration; ~300–500 hours during CBA negotiation.
- **VP Legal**: Legal guidance and compliance. ~50–100 hours during CBA negotiation.
- **External Labor Counsel**: Retained for CBA negotiation and dispute resolution. Budgeted separately (~PHP 500K–2M during CBA negotiation year).
- **Potential new role**: HR Labor Relations Manager may need to be a dedicated position if BuildRight faces multiple union certifications across locations.

---

## W494. Employee Wellness & Mental Health Program Management

| Field | Detail |
|---|---|
| **Trigger** | Annual program planning cycle; DOLE/DOH wellness program mandates; post-incident support (W140 OHS, W484 pandemic); employee assistance request |
| **Frequency** | Annual (program planning); quarterly (program activities); event-driven (crisis support) |
| **Volume** | 6,715 employees across all locations |
| **Owner** | CHRO |
| **Participants** | HR Training & Development, HR Compliance Manager, External EAP Provider, Store Managers, Safety Officer |

### Background

DOLE Department Order 198-18 (Implementing Rules of the Occupational Safety and Health Standards) and increasing Philippine corporate governance expectations require employers to provide programs supporting employee well-being beyond physical safety (covered by W140, W141, W187). BuildRight's workforce faces unique wellness challenges: (a) physical demands of store and warehouse work (lifting heavy building materials, standing for long shifts); (b) psychological stress from customer-facing roles (dealing with difficult customers, sales targets, robbery/trauma incidents — W471); (c) tropical heat exposure during yard and outdoor operations (W438, W470); (d) shift work disruption (W34 — 2–3 shifts, including night differential per W10); (e) separation from family for employees transferred to provincial stores; (f) financial stress among entry-level retail workers. This workflow establishes the wellness program framework. W51 covers training and skills development but not wellness. W140 covers OHS incident response but not proactive wellness.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Annual Wellness Program Planning**: CHRO designs the annual Employee Wellness Program: (a) conduct employee wellness needs assessment (anonymous survey, health risk assessment, utilization data from existing benefits); (b) define program pillars: physical health, mental health, financial wellness, social/community; (c) set annual program budget and activity calendar; (d) select and contract External Employee Assistance Program (EAP) provider for counseling services; (e) obtain CEO and CFO budget approval; (f) communicate program launch to all employees | CHRO | CEO | 1 week/annual |
| 2 | **Employee Assistance Program (EAP) Operations**: External EAP provider delivers confidential counseling services: (a) 24/7 hotline for mental health crises, personal problems, financial stress, relationship issues, substance abuse; (b) up to 6 free counseling sessions per employee per year (face-to-face, phone, or video); (c) critical incident stress debriefing after traumatic events (robbery, accident, workplace violence — W140, W471); (d) quarterly utilization report to CHRO (anonymized — no individual employee data shared); (e) EAP provider maintains separate confidential records per Data Privacy Act (RA 10173) | External EAP Provider | CHRO | Ongoing |
| 3 | **Physical Health Programs**: HR Training & Development implements physical health initiatives: (a) annual health screening for all employees (basic blood panel, blood pressure, BMI) — coordinate with DOLE-required annual medical examination per W140; (b) ergonomic assessment for cashiers (W34 — prolonged standing), DC workers (W3 — heavy lifting), and office workers; (c) stretch break protocols for store and DC workers (5-minute stretch breaks per shift); (d) flu vaccination drive during rainy season (subsidized or free for employees); (e) hydration and heat stress awareness during dry season (especially for yard workers — W438, W470) | HR Training & Development | CHRO | Per activity calendar |
| 4 | **Mental Health Awareness & Anti-Stigma**: HR Compliance Manager implements mental health awareness initiatives: (a) mental health literacy workshops (quarterly — online or in-person per region); (b) mental health first aid training for Store Managers and supervisors (recognize signs of mental health issues, provide initial support, refer to EAP); (c) anti-stigma communication campaigns (posters, intranet articles, Slack/Teams channels); (d) compliance with Philippine Mental Health Act (RA 11036) — employer obligations for mental health in the workplace | HR Compliance Manager | CHRO | Per activity calendar |
| 5 | **Financial Wellness Program**: HR implements financial wellness initiatives: (a) financial literacy seminars (budgeting, saving, debt management — especially relevant for entry-level retail workers earning near minimum wage); (b) coordinate with SSS, PhilHealth, Pag-IBIG for employee education on statutory benefits (W251); (c) employee loan management (W76 — ensure employees are not over-indebted); (d) coordinate with accredited banks for employee banking products (salary loans at preferential rates); (e) pre-retirement financial planning for employees nearing retirement age (W175) | HR / Finance | CHRO | Per activity calendar |
| 6 | **Crisis Support Activation**: Event-driven wellness support for employees affected by: (a) workplace incident (W140 — OHS incident → immediate EAP critical incident stress debriefing); (b) robbery or violence (W471 — security incident → trauma counseling); (c) pandemic (W484 → heightened anxiety support); (d) natural disaster (W49 → employee displacement, property loss → financial assistance coordination); (e) employee death (bereavement support for team, funeral assistance for family per W10 benefits); (f) Store Manager or HR triggers EAP referral for individual employees showing signs of distress | HR Labor Relations / EAP Provider | CHRO | Event-driven |
| 7 | **Program Effectiveness Measurement**: CHRO reviews program effectiveness annually: (a) EAP utilization rate (target: >5% of employees utilizing counseling services per year); (b) employee wellness survey scores (annual); (c) absenteeism rate trend (correlated with wellness program activities); (d) turnover rate trend (especially voluntary turnover — W43); (e) ROI analysis: program cost vs. reduced absenteeism, reduced turnover, reduced workers' compensation claims; (f) report to CEO and Board (W124) as part of HR metrics | CHRO | CEO | 1 week/annual |

### System Touchpoints
- HRIS: employee wellness program enrollment, health screening tracking, wellness activity attendance
- EAP Provider Portal: confidential case management (separate from BuildRight systems per RA 10173)
- Compliance Dashboard: wellness program activity tracking, utilization metrics
- Integration with W10 (payroll — wellness benefit deductions/contributions), W15 (onboarding — wellness program orientation), W43 (separation — exit wellness referral), W51 (training — wellness workshops), W140 (OHS — physical health coordination), W471 (security incidents — trauma support), W251 (statutory benefits — health education)

### Pain Points / Risks
- **Stigma in Philippine workplace culture**: Mental health remains heavily stigmatized in Philippine culture; employees may be reluctant to utilize EAP counseling services for fear of being perceived as "weak" or having their employment affected — even with confidentiality assurances
- **EAP utilization typically low**: Philippine corporate EAP utilization rates are typically 2–5% (vs. 5–10% in Western markets); low utilization makes it difficult to justify the program cost and demonstrate ROI
- **Geographic coverage**: Providing equitable wellness services to 6,715 employees across 200 stores in provincial and island locations is logistically challenging; health screening and face-to-face counseling require physical presence
- **Supervisor mental health literacy**: Store Managers are not trained counselors and may not recognize mental health issues (depression, anxiety, burnout) in their staff; misinterpreting mental health symptoms as "laziness" or "attitude problems" can worsen the situation and create liability
- **Cost justification**: Wellness programs are difficult to cost-justify in a company with 12–14% EBITDA margins; the CFO may resist program expansion without clear ROI evidence, especially for mental health services with indirect and delayed benefits

### Time Estimate
- Annual program planning: 1 week
- EAP coordination: ~2–4 hours/month
- Physical health programs: ~1 day per initiative
- Mental health awareness: ~2 days per quarter for training delivery
- Financial wellness: ~1 day per quarter
- Annual effectiveness review: 1 week
- **Total annual**: ~150–200 hours for HR team

### Staffing Implication
- **CHRO**: ~30–40 hours/year for wellness program strategy and oversight. Absorbed.
- **HR Training & Development**: ~80–120 hours/year for program delivery. Absorbed within existing W51 training duties.
- **External EAP Provider**: Outsourced. Budgeted as employee benefit cost (~PHP 300–500/employee/year × 6,715 = ~PHP 2.0–3.4M/year).
- **No incremental headcount** — wellness program management is absorbed into existing HR roles.

---

## W511. Employee Cross-Entity & Cross-Location Transfer Processing

| Field | Detail |
|---|---|
| **Trigger** | Employee transfer request (initiated by employee, manager, or HR); or organizational restructuring requires relocation |
| **Frequency** | ~20–30 transfers/month across 5 entities and 200+ locations |
| **Volume** | ~25 average/month; ~300/year |
| **Owner** | HR Manager |
| **Participants** | Employee, Current Manager, Receiving Manager, HR Manager, Payroll Manager, IT Support |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Transfer request initiated: employee submits transfer request via HR system, OR manager initiates transfer for organizational needs; specifies: current entity/location/position, target entity/location/position, requested effective date, transfer reason | Employee / Manager | HR Manager | 10 min |
| 2 | HR Manager classifies transfer type: (a) same-entity, different location (store-to-store); (b) same-entity, location-to-HQ or HQ-to-location; (c) cross-entity (e.g., Depot → Logistics); (d) cross-entity AND cross-location | HR Manager | HR Manager | 5 min |
| 3 | System performs eligibility checks: (a) probation period complete (minimum 6 months); (b) no pending disciplinary actions; (c) no outstanding employee loans exceeding PHP 20K threshold; (d) performance rating meets minimum (satisfactory or above); (e) target position vacancy confirmed | System | — | Automated |
| 4 | For cross-entity transfers: HR Manager initiates position and salary review — target entity may have different salary structure, benefits package, or payroll schedule; FP&A validates budget impact | HR Manager / FP&A | CFO (if salary change) | 30 min |
| 5 | Current Manager confirms handover plan: knowledge transfer timeline, pending work completion, project handover list; system sets 30-day transition period | Current Manager | HR Manager | 30 min |
| 6 | Receiving Manager confirms acceptance and prepares onboarding at new location/entity: workstation, system access requirements, training needs | Receiving Manager | HR Manager | 15 min |
| 7 | HR Manager approves transfer; system generates transfer order with effective date, old and new position details, salary changes (if any), entity change (if cross-entity) | HR Manager | HR Director (for cross-entity) | 10 min |
| 8 | Payroll Manager processes payroll entity change: (a) final payroll at old entity with pro-rated earnings and deductions; (b) mid-period proration if transfer effective date is not payroll period start; (c) benefits portability check: SSS, PhilHealth, Pag-IBIG remain continuous (same employee, different employer entity — update employer contribution allocation) | Payroll Manager | HR Manager | 20 min |
| 9 | IT Support updates access provisioning: (a) deactivate entity-specific roles at old entity; (b) provision entity-specific roles at new entity; (c) update location-based access (store system, reporting); (d) update email group memberships | IT Support | HR Manager | 15 min |
| 10 | System updates employee master: entity, location, position, department, cost center, reporting line, salary (if changed), payroll entity; full audit trail preserved | System | — | Automated |
| 11 | Post-transfer: HR Coordinator confirms 30-day check-in with employee and receiving manager; documents any adjustment issues | HR Coordinator | HR Manager | 15 min |

### System Touchpoints
- Transfer request workflow with type classification (HR-018)
- Automated eligibility validation against HR rules (HR-018)
- Position and salary review integration for cross-entity transfers (HR-018)
- Payroll entity change with mid-period proration (W10, HR-018)
- Benefits portability verification for SSS/PhilHealth/Pag-IBIG continuity (W251)
- IT access provisioning update (W152, HR-018)
- Employee master update with full audit trail (W292, MDM-011)
- Location master update for location-based changes (W254)
- Cost center transfer for budget tracking (W26, FIN-012)

### Time Estimate
~2–3 hours per transfer (request + eligibility + approval + payroll change + IT update). At ~25/month = ~50–75 staff-hours/month. Absorbed by HR Manager, Payroll Manager, and IT Support within existing FTE.

### Pain Points / Risks
- Cross-entity salary structure mismatch — employee may expect equivalent or higher salary; mitigated by upfront position review and transparency
- Benefits portability gap — some entity-specific benefits may not transfer; mitigated by benefits comparison during transfer review
- Knowledge loss at originating location during 30-day transition — mitigated by structured handover plan with documentation requirement

### Staffing Implication
- Absorbed within existing HR Manager, Payroll Manager, and IT Support FTEs.
- ~25 transfers/month adds ~50–75 staff-hours to monthly HR workload.

---

## W512. Store-Level Health & Safety Committee Operations

| Field | Detail |
|---|---|
| **Trigger** | Monthly safety committee meeting schedule; ad hoc safety concern requiring committee action |
| **Frequency** | Monthly committee meetings per qualified establishment (200 stores, 4 DCs, HQ); ~205 committees meeting monthly |
| **Volume** | ~205 meetings/month = ~2,460 meetings/year |
| **Owner** | Safety Officer (per establishment) |
| **Participants** | Safety Committee Members (management representative, worker representatives, safety officer, first aiders, maintenance representative) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Safety Officer prepares monthly committee meeting agenda: (a) review of previous meeting action items; (b) incident/accident review for the month (W140); (c) safety inspection findings (W141); (d) upcoming safety training schedule (W51); (e) new safety concerns from workers; (f) regulatory compliance updates | Safety Officer | Store Manager | 30 min |
| 2 | Safety committee meeting conducted (minimum quorum: management representative + worker representative + safety officer); minutes recorded in system with attendance log | Safety Officer | Store Manager | 60 min |
| 3 | Committee reviews all safety incidents for the month: incident type, severity, root cause, corrective action status, lessons learned; identifies trends and patterns | Committee | Safety Officer | 20 min |
| 4 | Committee reviews safety inspection findings (W141): open items from previous inspections, new findings, corrective action completion rate; assigns corrective actions with deadlines and responsible persons | Committee | Safety Officer | 15 min |
| 5 | Committee discusses new safety concerns raised by workers or management; classifies concern severity; assigns investigation or immediate action | Committee | Safety Officer | 10 min |
| 6 | Safety Officer documents meeting minutes in system: attendance, discussions, decisions, action items (description, responsible person, deadline); system auto-assigns action items to responsible persons with deadline tracking | Safety Officer | Store Manager | 20 min |
| 7 | System tracks action item completion: sends reminders at 7 days before deadline; escalates overdue items to Store Manager and Regional Safety Coordinator | System | — | Automated |
| 8 | Quarterly: Regional Safety Coordinator reviews safety committee effectiveness across region: meeting attendance rate, action item completion rate, incident reduction rate; identifies underperforming locations | Regional Safety Coordinator | VP Operations | 4 hours/quarter |
| 9 | Annually: Safety Officer conducts committee composition review per DOLE DO 198 requirements: confirms required members present (employer representative, workers' representative, safety officer, first aider, maintenance representative); updates committee roster as needed | Safety Officer | HR Manager | 2 hours/year |

### System Touchpoints
- Monthly meeting scheduling with attendance tracking (HR-019)
- Meeting minutes template with structured agenda sections (HR-019)
- Action item assignment with deadline tracking and escalation (HR-019)
- Incident review integration (W140) for monthly incident discussion (HR-019)
- Safety inspection findings integration (W141) for corrective action tracking (HR-019)
- Committee composition management per DOLE DO 198 requirements (HR-019)
- Regional effectiveness dashboard with attendance, action completion, and incident metrics (HR-019)
- Integration with DOLE annual OHS reporting (W436)

### Time Estimate
Meeting preparation: ~30 min. Meeting: ~60 min. Minutes and action items: ~20 min. Total: ~110 min/month per establishment. At 205 establishments = ~376 staff-hours/month across the company. Each store's committee members absorb this within monthly duties.

### Pain Points / Risks
- Committee meetings skipped or conducted superficially — mitigated by system attendance tracking and Regional Safety Coordinator quarterly review
- Action items not completed by deadline — mitigated by automated reminders and Store Manager escalation
- Worker representative not genuinely representing worker concerns — mitigated by DOLE-mandated composition requirements and anonymous concern submission option

### Staffing Implication
- Safety committee members serve as additional duty; no incremental headcount.
- Regional Safety Coordinator (within HQ Safety team) absorbs quarterly effectiveness reviews.
- Each establishment's safety committee consumes ~2 hours/month of member time.

---

## W555. Seasonal & Temporary Staffing Process

| Field | Detail |
|---|---|
| **Trigger** | Seasonal peak forecast (Christmas October–January, summer March–May, back-to-school May–June); new store opening schedule; or special event staffing need |
| **Frequency** | 2–3 major seasonal peaks per year plus ad hoc store openings (~10–15 new stores/year) |
| **Volume** | ~500–800 seasonal hires per Christmas peak across 200 stores; ~50–80 per new store opening |
| **Owner** | HR Business Partner / Store Manager (store-level coordination) |
| **Participants** | HR Business Partner (R), Recruitment Specialist (R), Store Manager (A/C), HR Director (A for policy), Payroll Specialist (I), Training Coordinator (C) |

### Background

W15 covers permanent recruitment and onboarding with full background checks, benefits enrollment, and long-term development planning. W269 covers vendor promodizer management. W511 covers cross-entity transfers. W179 covers management trainee programs. However, no workflow covers seasonal and temporary staffing — the abbreviated recruitment, onboarding, and offboarding process for workers hired for defined periods (typically 3–5 months for Christmas, 2 months for summer). Philippine labor law (DOLE Department Order 174) distinguishes between probationary employment (max 6 months), project employment (fixed-term), and seasonal employment (recurring seasonal work). Each classification has different compliance requirements. For a 200-store retailer with PHP 62.3B revenue, seasonal staffing represents ~8–12% of total headcount during peak periods and is critical for maintaining service levels.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Store Manager submits seasonal staffing request to HR: headcount by role (sales associate, cashier, stockroom), start and end dates, justification (seasonal peak, new store opening, special event), budget impact estimate | Store Manager | HR Business Partner | 30 min/request |
| 2 | HR Business Partner validates request against seasonal demand forecast (W31) and historical staffing data (previous year's seasonal headcount, sales-per-employee ratios, customer traffic patterns); confirms or adjusts headcount | HR Business Partner | HR Director | 1–2 hours |
| 3 | HR classifies employment type per DOLE 174: (a) seasonal employment — recurring seasonal work (Christmas, summer) with expected recall next season; (b) project employment — fixed-term for specific project (new store opening); (c) probationary employment — if there is intent for permanent employment after probationary period; classification determines statutory benefits, termination rules, and documentation requirements | HR Business Partner | HR Director | 15 min/request |
| 4 | Abbreviated recruitment: HR posts job listing (store-level bulletin, local barangay, social media, job boards); conducts 1-round interview (vs. 3 rounds for permanent per W15) focused on availability, physical capability, basic customer service aptitude; performs reference check (1 reference vs. 3 for permanent); recruitment cycle target: 5–7 days (vs. 21 days for permanent) | Recruitment Specialist | HR Business Partner | 5–7 days elapsed |
| 5 | Pre-employment requirements: SSS/PhilHealth/Pag-IBIG registration for new workers or re-activation for returning seasonal workers (system checks employee master for previous employment record); medical clearance (basic physical for manual roles); NBI clearance (or barangay clearance as alternative in provincial areas where NBI processing exceeds 5 days) | Recruitment Specialist | HR Business Partner | 1–2 days |
| 6 | Abbreviated onboarding (1 day vs. 3 days for permanent): (a) store tour and department layout; (b) safety briefing — emergency exits, fire extinguisher locations, first aid kit, hazard reporting per W512; (c) POS basics — log-in, item lookup, tender types, void transaction per W1; (d) department-specific product knowledge — top 50 SKUs, basic customer scenarios; (e) HR policies — attendance rules, dress code, code of conduct, anti-sexual harassment policy | Training Coordinator / Store Manager | HR Business Partner | 1 day (8 hours) |
| 7 | Payroll setup with correct employment classification: seasonal employment status in HR master, statutory deduction enrollment (SSS, PhilHealth, Pag-IBIG, withholding tax per TRAIN law), pro-rated 13th month pay accrual activated; Payroll Specialist confirms setup per W10 requirements | Payroll Specialist | HR Business Partner | 15 min/employee |
| 8 | Shift assignment per W34 scheduling with seasonal shift patterns: Store Manager assigns seasonal workers to high-traffic shifts (weekends, payday weekends, holiday rush); biometric enrollment (HR-005) for time & attendance; system ensures seasonal workers are scheduled within legal working hour limits (8 hours/day, 40 hours/week per Labor Code) | Store Manager | HR Business Partner | 30 min/employee |
| 9 | Mid-season performance check (at ~60% of seasonal employment period): Store Manager conducts brief performance review — customer service quality, attendance record, POS accuracy, teamwork; for underperformers: additional coaching or early termination per DOLE 174 just cause provisions; for top performers: flag for potential permanent employment conversion or returning worker priority | Store Manager | HR Business Partner | 15 min/employee |
| 10 | Pre-end-of-season offboarding plan (2 weeks before seasonal end date): HR Business Partner prepares offboarding checklist — last payroll computation including pro-rated 13th month pay (1/12 × monthly basic salary × months worked), certificate of employment issuance, return of uniforms/PPE per W172, SSS/PhilHealth/Pag-IBIG final reporting | HR Business Partner | HR Director | 30 min/batch |
| 11 | End-of-season offboarding execution (abbreviated W43 — no garden leave, no knowledge transfer, no exit interview required for seasonal workers): final clearance sign-off by Store Manager (uniform returned, no pending cash accountability); final payslip generated; certificate of employment issued; system updates employment status to "separated — end of seasonal engagement" | HR Business Partner / Store Manager | HR Director | 0.5 day |
| 12 | Returning seasonal worker database update: system flags separated seasonal workers as eligible for re-hire next season; stores performance rating and re-hire eligibility (eligible / not eligible / eligible with conditions); next season recruitment priority: returning eligible workers contacted first (re-activation of SSS/PhilHealth/Pag-IBIG only, no repeat NBI clearance if within 12 months) | HR Business Partner | HR Director | 15 min/employee |

### System Touchpoints

- Seasonal staffing request workflow with employment type classification (HR-020)
- Abbreviated recruitment process linked to W15 base process (HR-009)
- Multi-entity payroll seasonal setup (HR-001, W10)
- Time & attendance biometric enrollment for seasonal workers (HR-005)
- Shift scheduling with seasonal shift patterns (W34)
- PPE & uniform lifecycle for seasonal issuance and return (W172)
- Abbreviated separation/offboarding linked to W43 base process (HR-020, W43)
- Returning seasonal worker database with re-hire eligibility tracking (HR-020)

### Time Estimate

Abbreviated recruitment cycle: 5–7 days elapsed (vs. 21 days for permanent). Onboarding: 1 day (8 hours). Offboarding: 0.5 day. Seasonal HR admin: ~20 hours per Store Manager per season. At ~500–800 seasonal hires per Christmas peak: ~1,000–1,600 person-hours for recruitment + onboarding across all stores.

### Pain Points / Risks

- Returning seasonal workers may have inactive SSS/PhilHealth/Pag-IBIG requiring re-enrollment — delays payroll setup; mitigated by pre-season batch re-activation
- DOLE audit risk if seasonal workers exceed 5-month threshold — must be reclassified as regular employees with full benefits; mitigated by system-enforced end date tracking with 30-day advance warning
- Competition for seasonal workers with other retailers during Christmas (SM, Robinsons, Puregold) — wage rate pressure and candidate scarcity; mitigated by early recruitment (August–September for Christmas) and returning worker priority
- Abbreviated training may result in lower service quality — customer satisfaction may dip during peak season; mitigated by assigning seasonal workers to lower-complexity roles and experienced associates as buddies
- NBI clearance delays in provincial areas (some provinces have 7–10 day processing) — mitigated by accepting barangay clearance as interim document while NBI processing completes

### Staffing Implication

- Covered by existing HR Business Partners and Recruitment Specialists; no incremental headcount needed.
- ~20 hours per Store Manager per season for seasonal HR coordination; absorbed within existing duties.
- Training Coordinator workload increases by ~1 day per seasonal hire batch; absorbed within existing capacity.

---

## W561. Employee Attendance Exception Management

| Field | Detail |
|---|---|
| **Trigger** | Biometric/attendance system generates exception (late arrival, unauthorized absence, undertime, biometric failure, missing punch, overtime without approval) |
| **Frequency** | ~800–1,200 exceptions per day across 200 stores + 4 DCs + HQ (6,715 employees, ~12–18% exception rate) |
| **Volume** | Higher on Mondays (+25%), after holidays (+40%), during rainy season/typhoons (+30%, Metro Manila and low-lying areas), during MRT/LRT service disruptions |
| **Owner** | HR Supervisor / Store Manager (store-level) |
| **Participants** | Employee (R for self-service), Department Supervisor (R for approval), HR Supervisor (A), Payroll Specialist (I), Store Manager (A for store-level) |

### Background

W10 covers payroll processing which consumes attendance data. W34 covers shift scheduling which defines expected hours. HR-005 covers time and attendance system integration. However, no workflow covers the daily management of attendance exceptions — the process of reviewing, classifying, approving/denying, and resolving the ~1,000 daily discrepancies between scheduled and actual attendance. For a 200-store chain with biometric attendance systems, exceptions are inevitable: biometric readers fail in high-humidity conditions (Philippine tropical climate), employees forget to punch in/out, shift swaps are not reflected in the system, and force majeure events (typhoons, floods, transportation strikes) create mass exceptions. Without a structured exception management process, payroll accuracy degrades and DOLE compliance risk increases.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System generates daily exception report from biometric/attendance system, categorized by type: (a) late arrival (punch-in after shift start + grace period); (b) unauthorized absence (no punch for full shift, no pre-filed leave); (c) undertime (punch-out before shift end); (d) missing punch (only in-punch or out-punch recorded); (e) biometric failure (system unable to read fingerprint/face); (f) unauthorized overtime (punch-out after shift end without pre-approved OT) | System | — | Automated (daily batch at 06:00) |
| 2 | HR Supervisor reviews exception dashboard prioritized by severity: unauthorized absence (critical) > missing punch (high) > late arrival (medium) > undertime (low); dashboard shows exception count by store, department, and category with trend comparison to previous period | HR Supervisor | Store Manager | 30–45 min/day |
| 3 | For biometric failures: HR Supervisor verifies employee identity against employee photo in HR master, creates manual punch entry with reason code "biometric failure," obtains Department Supervisor confirmation that employee was present; submits IT ticket per W48 for biometric reader repair/maintenance; recurring biometric failures (>3/month for same employee) trigger re-enrollment with alternate biometric (e.g., switch from fingerprint to face recognition) | HR Supervisor | Store Manager | 5 min/exception |
| 4 | For late arrivals: Department Supervisor confirms whether late arrival was communicated in advance (SMS, call, team messaging app); system auto-calculates deduction per company policy — grace period: 15 minutes (no deduction); 16–60 minutes late: 1-hour deduction; >60 minutes late: half-day deduction; if late was due to verified force majeure (MRT breakdown, flooding), HR Supervisor applies excused tardiness with no deduction | Department Supervisor / HR Supervisor | Store Manager | 3 min/exception |
| 5 | For absences: system checks if leave was pre-filed per HR-007 leave management; if leave filed and approved → no exception (system auto-clears); if leave not filed → classify as absent without pay; if absence due to force majeure (typhoon signal, declared calamity) → classify per company policy as excused with pay (up to 5 days/year) or special emergency leave per DOLE advisory | HR Supervisor | Store Manager | 5 min/exception |
| 6 | For undertime: verify if early departure was authorized by Department Supervisor (system checks for approved early departure request); if authorized → no deduction, update timesheet; if unauthorized → system deducts proportional hours from daily pay; pattern detection: employee with >3 unauthorized undertime incidents in 30 days flagged for Store Manager counseling | HR Supervisor | Store Manager | 3 min/exception |
| 7 | For missing punches: employee submits self-service correction request via HR portal or mobile app with reason (forgot to punch, system down, was at other location for task); Department Supervisor approves or denies within 2 business days; if approved → system creates corrected punch entry with audit trail; if denied → exception remains and standard deduction applies | Employee / Department Supervisor | HR Supervisor | 2 min/exception (system); 5 min if manual |
| 8 | For unauthorized overtime: system verifies against pre-approved overtime per W34 shift schedule; if OT was pre-approved → clear exception, system calculates OT pay (125% regular, 130% rest day, per Labor Code); if unapproved → flag for Store Manager review — Store Manager decides whether to approve retroactively (with justification) or deny (OT hours not compensated); pattern detection: employee with repeated unapproved OT flagged for counseling | HR Supervisor / Store Manager | Store Manager | 5 min/exception |
| 9 | Mass exception handling (typhoon, transportation strike, widespread flooding): HR Director issues blanket excused attendance directive per DOLE advisory — specifies affected areas, dates, and pay treatment (excused with pay, offset against leave credits, or no-pay); system applies mass exception clearance for all affected employees in specified locations; no individual review required for covered exceptions | HR Director | HR Director | 1–2 hours/event |
| 10 | Approved exceptions update payroll input file for W10: system generates corrected attendance file with all resolved exceptions reflected; unresolved exceptions (pending supervisor approval) carry forward to next payroll cutoff with default deduction applied; exceptions resolved after payroll run trigger retroactive adjustment in next payroll period | System | — | Automated (daily sync) |
| 11 | Weekly exception trend analysis: HR Supervisor generates exception trend report by store, department, and category; identifies: stores with exception rates >20% (above company average), repeat offenders (>5 exceptions/month), exception categories trending upward; report shared with Store Manager and HR Business Partner for corrective action | HR Supervisor | HR Business Partner | 1 hour/week |
| 12 | Monthly attendance compliance report: aggregated exception data feeds into W72 (employee performance — attendance scorecard component) and W67 (store performance — labor compliance metric); stores with exception rates >20% for 2 consecutive months flagged for HR Business Partner intervention; annual attendance compliance data supports DOLE labor standards audit documentation | HR Supervisor | HR Director | 2 hours/month |

### System Touchpoints

- Attendance exception management module with categorization and severity prioritization (HR-021)
- Biometric/attendance system integration for exception detection (HR-005)
- Self-service punch correction workflow with supervisor approval (HR-021)
- Overtime calculation with pre-approval verification (HR-010)
- Holiday pay exception handling (HR-011)
- Leave management integration for absence verification (HR-007)
- Payroll processing corrected data feed (W10)
- Shift scheduling as schedule source (W34)
- IT helpdesk integration for biometric repair tickets (W48)
- Employee performance attendance scorecard feed (W72)
- Store performance labor compliance metric feed (W67)

### Time Estimate

~2–3 minutes per exception; ~1,000 exceptions/day × 2.5 min = ~42 person-hours daily across all HR Supervisors. Weekly trend analysis: ~1 hour. Monthly compliance report: ~2 hours. Total: ~230 person-hours/month across the company. Absorbed by HR Supervisors at stores and HQ HR team.

### Pain Points / Risks

- Biometric readers in outdoor lumber yards and garden centers fail frequently due to rain and humidity — generates excessive false exceptions; mitigated by IT preventive maintenance schedule per W48 and alternative punch methods (RFID badge backup)
- Mass exceptions during typhoons overwhelm manual processing — 200 stores × ~30 employees = 6,000 exceptions in a single day; mitigated by automated mass exception clearance (step 9)
- Self-service correction adoption is low among store associates (estimated <30% adoption) — most corrections still require HR Supervisor manual entry; mitigated by mobile app simplification and associate training
- Late punch "buddy punching" (one employee punching in for another) requires LP investigation per W37 — biometric system reduces but does not eliminate this risk; mitigated by random CCTV audit of biometric stations by LP team

### Staffing Implication

- Covered by existing HR Supervisors at stores and HR team; no incremental headcount needed.
- ~42 person-hours/day distributed across ~200 store HR Supervisors = ~12 min/day per HR Supervisor; absorbed within existing duties.
- Weekly and monthly analysis absorbed by HR Business Partners.

---

## W567. Employee Cross-Training & Skill Matrix Management

| Field | Detail |
|---|---|
| **Trigger** | New department assignment; quarterly skill assessment cycle; new product category launch; staffing gap requiring cross-trained coverage |
| **Frequency** | Quarterly skill assessments for all 6,715 employees; continuous cross-training assignments (~1,500–2,000 per quarter) |
| **Volume** | Higher during new store openings (cross-training for new departments) and seasonal peaks |
| **Owner** | Training Manager / Store Manager (store-level execution) |
| **Participants** | Training Manager (A), Department Supervisor (R for training execution), Employee (R), Store Manager (A for assignment), HR Business Partner (I) |

### Background

W51 covers employee training and skills development including training needs analysis, program delivery, and effectiveness evaluation. W72 covers employee performance management including goal setting and competency assessment. However, no workflow covers multi-department cross-training and skill matrix management — the systematic process of training store associates across multiple departments so they can provide coverage during absences, peak periods, and staffing gaps. For a hardware retailer with 8 distinct departments (lumber, plumbing, electrical, tiles, paint, tools, hardware, garden) and 35,000 SKUs, deep product knowledge in each department takes months to develop. Cross-training ensures that when the plumbing expert calls in sick, another associate can assist customers with basic plumbing questions. This is especially critical for a 200-store chain with ~29 employees per store — limited staffing means cross-functional flexibility is essential.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Training Manager establishes skill matrix template per department: (a) product knowledge levels — beginner (top 20 SKUs, basic features), intermediate (top 50 SKUs, customer scenarios, compatibility), advanced (full catalog, technical specifications, project consultation); (b) POS operations — basic (scan, tender, void) and advanced (special orders, returns, layaway); (c) safety procedures — department-specific hazards and PPE requirements; (d) specialized services — paint mixing, lumber cutting, pipe threading, tile cutting, electrical testing; template configured in ERP skill matrix module | Training Manager | VP Operations | 2–3 days (initial setup); 1 day/quarter review |
| 2 | Initial skill assessment: Department Supervisor evaluates each associate against the skill matrix for their assigned department using structured assessment form — product knowledge quiz (top 20 SKUs by sales value), POS proficiency test, safety procedure walkthrough; results recorded in ERP with assessor ID and date; self-assessment component (employee rates own confidence per skill area) included for gap comparison | Department Supervisor | Training Manager | 30 min/employee |
| 3 | Gap analysis: system identifies departments where cross-coverage is weakest — minimum coverage threshold: 2 associates per department with intermediate-level product knowledge; system generates cross-coverage heatmap per store showing departments below threshold in red, at threshold in amber, above in green; identifies individual employees whose skill gaps limit their cross-department utility | System | — | Automated |
| 4 | Cross-training plan creation: Training Manager generates quarterly training calendar with rotation assignments based on gap analysis — priority: (a) departments below minimum coverage threshold; (b) employees with narrow skill sets (competent in only 1 department); (c) new product category launches requiring new skills; each cross-training assignment targets 1 new department per associate per quarter | Training Manager | Store Manager | 4–6 hours/quarter |
| 5 | Cross-training execution: assigned associate shadows experienced associate in target department for 2–4 hour sessions (minimum 3 sessions per department); session 1: department orientation — layout, top 20 SKUs, customer personas, common questions; session 2: hands-on — assist customers under supervision, practice POS transactions for department-specific items; session 3: assessment preparation — review product guide, practice customer scenarios, safety procedures | Employee / Department Supervisor | Store Manager | 2–4 hours/session × 3 sessions = 6–12 hours/department |
| 6 | Practical assessment: target department Department Supervisor tests cross-trainee on: (a) top 20 SKUs — identify product, explain key features, suggest alternatives; (b) 3 basic customer scenarios — assist customer with product selection, handle return/exchange, process special order; (c) safety procedures — department-specific hazards, PPE requirements, emergency procedures; pass threshold: 70% correct; if failed, 1 additional shadow session + re-assessment within 2 weeks | Department Supervisor | Training Manager | 30–45 min/employee |
| 7 | Skill matrix update in ERP: system records certification date, skill level (beginner/intermediate/advanced) per department per employee, assessor ID, assessment score; cross-coverage heatmap auto-refreshes; store-level skill matrix dashboard updated for Store Manager visibility | System | — | Automated |
| 8 | Store Manager reviews cross-coverage heatmap — identifies departments still below minimum coverage threshold; escalates persistent gaps (>2 consecutive quarters below threshold) to Training Manager for targeted intervention; approves or modifies shift assignments to leverage cross-trained associates | Store Manager | Training Manager | 1 hour/month |
| 9 | Scheduling integration: W34 shift scheduling prioritizes cross-trained associates for coverage during absences — when associate calls in sick, system suggests cross-trained replacement from another department; during peak periods (weekends, payday, seasonal rush), Store Manager assigns cross-trained associates to high-traffic departments; scheduling system flags departments at risk of no cross-coverage in upcoming schedule | Store Manager / System | Training Manager | Absorbed in W34 scheduling |
| 10 | Recognition and development: top cross-trained associates (certified in 3+ departments at intermediate level) identified for: (a) recognition per W72 performance management — cross-training achievement as performance differentiator; (b) potential promotion to Department Supervisor or Senior Sales Associate; (c) management trainee program candidate identification per W179; (d) higher-priority consideration for preferred shift assignments | Training Manager / HR Business Partner | VP Operations | Absorbed in W72 cycle |
| 11 | Quarterly re-assessment: system tracks certification age — certifications older than 6 months without practice (no shifts worked in certified department) flagged for re-assessment; skill decay mitigation: associates assigned to work at least 1 shift per quarter in each cross-trained department to maintain certification; expired certifications downgraded to beginner level pending re-assessment | System / Department Supervisor | Training Manager | 15 min/employee (re-assessment) |
| 12 | Annual skill matrix review: Training Manager aggregates cross-training data for annual talent review — feeds into W178 (succession planning — cross-trained associates as internal mobility candidates) and W179 (management trainee — high-performing cross-trained associates identified as program candidates); annual report to VP Operations: cross-coverage by store, certification rates, training hours invested, turnover impact analysis | Training Manager | VP Operations | 1 week/year |

### System Touchpoints

- Cross-training and skill matrix module with department-specific skill templates (HR-022)
- Training governance policy framework integration (GOV-016)
- Training delivery execution linked to W51 (W51)
- Employee performance management feed for cross-training achievement (W72)
- Shift scheduling integration for cross-trained associate deployment (W34)
- Succession planning pipeline feed (W178)
- Management trainee candidate identification feed (W179)

### Time Estimate

3–4 hours per cross-training session per associate (shadow sessions + assessment); ~1,750 cross-training sessions/quarter × 3.5 hours = ~6,125 person-hours/quarter. Quarterly plan creation: ~4–6 hours. Monthly heatmap review: ~1 hour/store. Annual review: ~1 week. Distributed across Training Manager, Department Supervisors, and associates.

### Pain Points / Risks

- Product knowledge depth varies dramatically across departments — electrical requires technical knowledge (wiring, load calculations), paint requires color mixing expertise, lumber requires grading knowledge; cross-training to intermediate level is realistic but advanced level is impractical for most departments; mitigated by focusing cross-training on beginner-to-intermediate levels
- Cross-training time reduces selling-floor coverage — when associates are shadowing in another department, their home department may be understaffed; mitigated by scheduling cross-training during lower-traffic periods (weekday mornings)
- Skill decay is rapid without regular practice — associates certified in a department but never assigned shifts there will lose proficiency within 3–6 months; mitigated by quarterly minimum-shift requirement and re-assessment protocol
- Associates may resist cross-department assignments — preference for familiar department and discomfort with new product categories; mitigated by linking cross-training to career progression and recognition
- Measuring cross-training ROI is difficult — the benefit is primarily risk mitigation (coverage during absences) rather than direct revenue; mitigated by tracking metrics: cross-coverage percentage, customer service continuity during absences, and internal promotion rate

### Staffing Implication

- Covered by existing Training Manager and Department Supervisors; no incremental headcount needed.
- ~6,125 person-hours/quarter for cross-training execution is absorbed by associates during scheduled training time and Department Supervisors during assessment.
- Training Manager quarterly planning (~4–6 hours) and annual review (~1 week) absorbed within existing capacity.

---

## W594. Store-Level Employee Daily Attendance Verification & Exception Processing

| Field | Detail |
|---|---|
| **Trigger** | Daily attendance data pull from biometric/RFID system (automated at 06:00); schedule-vs-actual comparison triggers exception flags |
| **Frequency** | Daily at all 200 stores; exceptions processed throughout the day |
| **Volume** | ~5,800 store-level employees across 200 stores (avg 29 per store); ~700–1,100 daily attendance exceptions (~12–18% exception rate); exception types: no-show (~15%), tardiness (~40%), unauthorized overtime (~10%), missing punch (~25%), undertime (~10%) |
| **Owner** | Department Supervisor / Store Manager (store-level); HR Supervisor (oversight) |
| **Participants** | Department Supervisor (R/A), Store Manager (A for escalation), HR Supervisor (R for payroll feed), Employee (R for self-service correction), HR Business Partner (I for trend analysis) |

### Background

W34 covers shift scheduling which defines expected employee hours. W10 covers payroll processing which consumes attendance data. W561 covers the broader attendance exception management process across all locations (stores, DCs, HQ). HR-005 covers time and attendance system integration. HR-010 covers overtime policy. HR-021 covers attendance exception categories. However, W561 operates at the enterprise level with HR Supervisor ownership; no workflow addresses the store-level daily operational routine — the morning attendance verification, real-time exception handling, and immediate management response that Store Managers and Department Supervisors must perform every day before store opening.

For a 200-store chain with ~5,800 store-level employees, the daily attendance check is operationally critical: a no-show cashier means a closed register during peak morning hours; a missing department supervisor means no shelf walk (W573) or replenishment supervision (W554); an unauthorized overtime situation creates Labor Code compliance risk. Store Managers need real-time visibility into who is present, who is absent, and what coverage gaps exist — not a next-day HR report.

This workflow complements W561 by defining the store-level daily operational cadence. W561 handles the system-level exception management, payroll feed, and HR analytics; W594 handles the immediate store-level response: manager notification, coverage decisions, absence documentation, and same-day resolution.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Overnight attendance data pull**: system pulls biometric/RFID punch data from all 200 stores via automated batch at 06:00; data includes: employee ID, store code, punch-in time, punch-out time (if applicable), biometric device ID; system cross-references punch data against published shift schedule per W34 for each store | System | — | Automated (06:00 batch, ~15 min) |
| 2 | **Schedule-vs-actual comparison**: system generates store-level attendance comparison report — for each scheduled employee: (a) matched: punched in within grace period of shift start; (b) late: punched in after grace period (15 min per company policy) but within 60 minutes; (c) no-show: no punch recorded by 60 minutes after shift start; (d) missing punch: punch-in recorded but no punch-out (or vice versa) from previous day; (e) early arrival: punched in >30 min before shift start (potential unauthorized OT risk); report distributed to Store Manager and Department Supervisors via mobile app notification by 06:30 | System | — | Automated |
| 3 | **No-show identification and manager notification**: for each no-show, system sends immediate mobile notification to: (a) the no-show employee's Department Supervisor (primary), (b) Store Manager (informational); notification includes: employee name, department, shift start time, elapsed time since shift start, employee contact number; Department Supervisor attempts to contact employee by phone within 15 minutes of notification — (a) if employee answers and provides valid reason (illness, family emergency, transportation issue): Supervisor logs reason code in system, proceeds to coverage decision (step 5); (b) if employee unreachable after 2 attempts within 30 minutes: classify as unexcused absence, proceed to step 4 | Department Supervisor | Store Manager | 15 min per no-show |
| 4 | **Absence documentation**: for confirmed absences — (a) excused absence (employee contacted, valid reason): system logs absence reason, checks leave balance per HR-007, applies against leave credits if applicable (sick leave, emergency leave, VL); if leave credits exhausted: absence without pay; (b) unexcused absence (employee unreachable or no valid reason): system logs unexcused absence without pay, flags for Store Manager counseling; (c) system auto-generates absence notification to employee's registered email/SMS with absence status and pay impact; (d) pattern detection trigger: system flags employee with 3+ unexcused absences in rolling 30-day period for HR Business Partner review | Department Supervisor / System | Store Manager | 5 min per absence |
| 5 | **Tardiness logging**: for late arrivals — (a) system auto-calculates tardiness duration: punch-in time minus shift start minus grace period; (b) tardiness categories: 1–15 min (late but within tolerance, logged but no deduction), 16–60 min (late, 1-hour pay deduction), >60 min (very late, half-day deduction); (c) Department Supervisor confirms tardiness classification; (d) if employee provides verified force majeure reason (MRT/LRT breakdown, flooding, PAGASA-declared weather advisory): Supervisor applies excused tardiness with no deduction per company policy; (e) pattern detection: employee with 5+ tardiness incidents in rolling 30-day period flagged for Store Manager counseling and HR Business Partner notification | Department Supervisor | Store Manager | 3 min per tardy employee |
| 6 | **Overtime pre-approval verification**: system identifies employees who punched out after shift end — (a) cross-reference against pre-approved overtime requests per W34/HR-010; (b) if OT was pre-approved: system clears flag, calculates OT hours and OT pay rate (125% regular day, 130% rest day per Labor Code Article 87); (c) if OT was not pre-approved: flag for Store Manager review — Store Manager decides within 2 business days: (i) approve retroactively with documented justification (e.g., customer rush, unexpected delivery, emergency restocking), or (ii) deny (OT hours not compensated); (d) pattern detection: employee with 3+ unapproved OT incidents in 30 days flagged for Store Manager counseling — may indicate poor shift scheduling or workload imbalance | Department Supervisor / Store Manager | Store Manager | 3 min per unapproved OT |
| 7 | **Coverage decision for no-shows and absences**: for each confirmed absence that leaves a department understaffed (below minimum coverage threshold per W34), Store Manager executes coverage plan — (a) check cross-trained associates per W567 skill matrix for inter-department coverage; (b) check off-duty associates available for call-in (maintain call-in availability list per store); (c) if coverage gap persists: redistribute floor staff from lower-traffic departments; (d) if critical gap (e.g., no cashier available): Department Supervisor covers register or Store Manager opens "Manager Register" with override credentials; (e) document coverage decision in system for payroll (overtime if applicable) and W34 schedule adjustment | Store Manager | — | 10–15 min per coverage gap |
| 8 | **Exception resolution for missing punches**: for employees with missing punch records from previous day — (a) system generates self-service correction notification to employee via mobile app; (b) employee submits correction request with reason (forgot to punch, biometric failure, was at other location for task); (c) Department Supervisor approves or denies within 2 business days; (d) if approved: system creates corrected punch entry with audit trail; (e) if employee does not submit correction within 3 business days: Supervisor creates manual entry based on documented observation (subject to HR audit) | Employee / Department Supervisor | HR Supervisor | 2 min per correction (system) |
| 9 | **Payroll feed**: resolved and unresolved exceptions feed into W10 payroll processing — (a) approved exceptions update the daily attendance file with corrected punch data, absence codes, tardiness deductions, and OT hours; (b) unresolved exceptions (pending supervisor approval) carry forward to next payroll cutoff with default deduction applied; (c) exceptions resolved after payroll run trigger retroactive adjustment in next payroll period; (d) daily sync between attendance system and payroll module at 22:00; (e) HR Supervisor receives daily exception resolution summary: total exceptions, resolved count, unresolved count, resolution rate by store | System / HR Supervisor | HR Supervisor | Automated (daily sync) |
| 10 | **Daily store-level attendance summary**: by 08:00 each day, Store Manager reviews attendance summary for their store — (a) present count vs. scheduled count by department; (b) open exceptions requiring resolution; (c) coverage status: departments at/above/below minimum staffing; (d) week-to-date attendance trend; Store Manager signs off on daily summary via mobile app; unresolved items carry forward to next day with escalation priority | Store Manager | — | 10–15 min/day |
| 11 | **Weekly store-level exception trend review**: HR Supervisor generates weekly exception trend report per store — (a) exception rate by store (target: <15%); (b) exception category breakdown (no-show, tardiness, OT, missing punch); (c) stores with exception rates >20% for 2 consecutive weeks flagged for HR Business Partner intervention; (d) Store Manager receives weekly exception summary with comparison to regional and company averages; (e) data feeds into W72 (employee performance — attendance component) and W67 (store performance — labor compliance metric) | HR Supervisor | HR Business Partner | 1 hour/week |
| 12 | **Monthly attendance compliance report for DOLE readiness**: HR Supervisor compiles monthly attendance compliance documentation per store — (a) attendance rate (days present / days scheduled); (b) overtime compliance (all OT hours with documented pre-approval or retroactive approval); (c) rest day compliance (mandatory 24-hour rest day per week per Labor Code); (d) holiday pay compliance (correct calculation per Labor Code rules — 200% for unworked regular holiday, 300% for worked regular holiday, etc.); (e) stored per store as DOLE inspection-ready documentation per Labor Code Article 108 and DOLE Department Order No. 174 | HR Supervisor | HR Director | 2–3 hours/month |

**Total time per store per day**: ~30–45 min (Department Supervisor: ~15–20 min; Store Manager: ~15–25 min)

### System Touchpoints (W594 — Store-Level Attendance Verification)

- Biometric/RFID attendance system integration for daily punch data pull (HR-005)
- Shift scheduling module for schedule-vs-actual comparison (W34, HR-004)
- Mobile app notification system for real-time no-show and exception alerts (HR-021)
- Self-service punch correction workflow with supervisor approval (HR-021)
- Leave management integration for absence verification and leave credit deduction (HR-007)
- Overtime pre-approval verification and calculation engine (HR-010)
- Holiday pay calculation engine per Philippine Labor Code (HR-011)
- Cross-training skill matrix for coverage decision support (W567)
- Payroll processing data feed (W10)
- Employee performance attendance scorecard feed (W72)
- Store performance labor compliance metric feed (W67)
- IT helpdesk integration for biometric device issues (W48)

### Pain Points / Risks

- **Biometric reader failures in tropical conditions**: outdoor lumber yards, garden centers, and loading dock areas experience high failure rates due to humidity, rain, and dust; estimated 3–5% of punches fail biometric read, generating false exceptions; mitigated by RFID badge backup, scheduled biometric maintenance per W48, and manual Supervisor override for confirmed device failures
- **Mass exceptions during typhoon season**: Philippine typhoon season (June–November) generates mass attendance exceptions — PAGASA Signal No. 1–5 declarations affect different regions differently; 200 stores across Luzon, Visayas, and Mindanao experience disruptions at different times; mitigated by W561 step 9 mass exception handling (HR Director blanket excused attendance directive) and store-level force majeure tardiness exemption (step 5d)
- **Morning exception resolution conflicts with store opening**: the attendance verification process (steps 2–7) occurs during the critical 06:30–08:00 pre-opening window when Department Supervisors are also responsible for cash drawer preparation, shelf walk (W573), and opening procedures; competing priorities can delay exception handling; mitigated by automated notification (step 3) and streamlined mobile app workflow
- **Buddy punching and attendance fraud**: biometric systems reduce but do not eliminate buddy punching (one employee punching in for another); CCTV monitoring at biometric stations and LP spot-checks (W37/562) provide additional deterrence; RFID badges without biometric verification are higher risk
- **Self-service punch correction adoption is low**: estimated <30% of store associates use the mobile app for self-service corrections; most corrections still require Supervisor manual entry, adding to Supervisor workload; mitigated by mobile app simplification, associate training, and 3-business-day auto-escalation if correction not submitted

### Staffing Implication

- **Covered by existing Department Supervisors and Store Managers** at each of 200 stores; no incremental headcount needed.
- Per-store daily effort: ~30–45 min total across Department Supervisors and Store Manager; absorbed within pre-opening and daily management routines.
- **HR Supervisor oversight**: ~1 hour/week for trend analysis + ~2–3 hours/month for DOLE compliance report; absorbed by HR Supervisors distributed across regions.
- **HR Business Partner**: intervention for high-exception stores (~10–20 stores/quarter); absorbed within existing HRBP cadence.
- **Total chain-wide daily effort**: 200 stores × ~40 min = ~133 person-hours/day across Department Supervisors and Store Managers; this is an existing operational activity being formalized, not incremental workload.

---

## W628. Employee Exit Interview & Attrition Analysis

| Field | Detail |
|---|---|
| **Trigger** | Employee submits resignation; employee terminated; employee retirement |
| **Frequency** | Per separation event; ~600-800 separations/year |
| **Volume** | ~50-70 separations/month across all locations |
| **Owner** | HR Business Partner |
| **Participants** | HR Business Partner, departing employee, Department Supervisor/Store Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Departing employee notification received (per W43 offboarding); HR Coordinator schedules exit interview within employee's notice period (30 days for regular employees per Labor Code) | HR Coordinator | HR Business Partner | 5 min |
| 2 | HR Business Partner sends confidential exit interview questionnaire to departing employee via online survey link: covers (a) primary reason for leaving (compensation, career growth, management, work environment, relocation, personal, retirement), (b) satisfaction with role and team, (c) relationship with supervisor, (d) perception of company culture, (e) suggestions for improvement, (f) whether they would recommend BuildRight as employer | HR Business Partner | — | 5 min |
| 3 | Exit interview conducted (in-person for HQ/DC employees, video call for store employees, phone for remote locations): HR Business Partner explores survey responses, probes for additional context, and captures qualitative insights; assures confidentiality of responses | HR Business Partner | — | 30 min |
| 4 | HR Business Partner records structured exit interview data in HR analytics module: reason category, sub-reasons, verbatim quotes (anonymized), rehire eligibility assessment, and department/location metadata | HR Business Partner | — | 15 min |
| 5 | For high-performer departures or unexpected resignations: HR Business Partner conducts stay-interview-style debrief with Department Supervisor/Store Manager to understand team dynamics and identify retention risks for remaining team members | HR Business Partner | — | 30 min |
| 6 | Monthly: HR Business Partner generates attrition analytics dashboard — (a) attrition rate by location/store, department, tenure band, and employment type, (b) top reasons for leaving, (c) average tenure at departure, (d) new hire 90-day attrition rate, (e) regretted vs. non-regretted attrition, (f) attrition cost estimate (recruitment + training + productivity loss) | HR Business Partner | CHRO | 4 hours |
| 7 | Quarterly: HR Business Partner presents attrition trend analysis to CHRO and Department Heads — identifies departments/stores with above-average attrition, root cause themes, and recommended retention interventions; links to employee engagement survey results (per W629) | HR Business Partner | CHRO | 2 hours |
| 8 | Annually: CHRO incorporates attrition analysis into strategic workforce plan; sets annual retention targets; allocates retention budget (compensation adjustments, benefits enhancements, career development programs per W51) | CHRO | CEO | 4 hours |

### System Touchpoints
- ERP HR module: separation processing (per W43), exit interview data capture, attrition analytics
- ERP BI module: attrition dashboard, trend analysis, cost modeling
- Online survey platform: exit interview questionnaire delivery and response collection
- Employee master (W292): tenure data, performance ratings, rehire eligibility flag

### Pain Points / Risks
- **Low exit interview participation**: departing employees may decline to participate or provide superficial answers; mitigated by scheduling interview early in notice period, offering anonymous written option, and framing as feedback opportunity
- **Honesty bias**: employees may not share true reasons for leaving (especially if related to management) to avoid burning bridges; mitigated by confidentiality assurance, anonymized reporting, and third-party survey option
- **Data without action**: attrition data collected but not acted upon erodes management credibility; mitigated by quarterly action-oriented review and tracking of retention interventions implemented
- **Store-level access**: store employees may be harder to reach for exit interviews due to shift schedules and remote locations; mitigated by offering phone/video interviews and flexible scheduling

### Staffing Implication
- **HR Business Partner**: ~30 min per exit interview + ~4 hours/month analytics + ~2 hours/quarter presentation = ~12 hours/month. Absorbed within existing role.
- **HR Coordinator**: ~5 min scheduling per separation. Absorbed within existing role.

---

## W629. Store-Level Employee Engagement Survey & Action Planning

| Field | Detail |
|---|---|
| **Trigger** | Semi-annual survey calendar; annual comprehensive survey |
| **Frequency** | Semi-annual pulse surveys; annual comprehensive engagement survey |
| **Volume** | ~6,715 employees across 200 stores, 4 DCs, HQ |
| **Owner** | HR Business Partner |
| **Participants** | HR Business Partner, CHRO, Store/DC Managers, Department Heads, all employees |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | HR Business Partner configures engagement survey in survey platform: selects question set (comprehensive: 40-50 questions across 10 dimensions; pulse: 10-15 questions on focus areas), configures demographics (location, department, tenure, role level — no individually identifying data to protect anonymity), sets survey period (2 weeks), and sends launch communication | HR Business Partner | CHRO | 4 hours |
| 2 | Survey communication cascade: CHRO sends company-wide email announcing survey purpose and confidentiality; Store/DC Managers announce in team huddles; system sends personalized survey link to each employee via email and SMS; reminder sent at Day 7 for non-respondents | CHRO / Store Managers | — | 30 min |
| 3 | Employees complete survey on mobile device, POS terminal (during non-selling time), shared store tablet, or personal phone; estimated completion time: 10-15 minutes (comprehensive), 5 minutes (pulse); survey platform ensures anonymity (no IP tracking, no timestamps linked to individuals) | Employee | — | 10-15 min |
| 4 | HR Business Partner monitors response rate daily; targets ≥ 80% response rate; sends targeted reminders to locations/departments below 60% at Day 5 and Day 10; extends survey period by 3 days if overall response rate < 70% at Day 12 | HR Business Partner | — | 15 min/day |
| 5 | Survey platform auto-generates results: (a) overall engagement score (0-100), (b) dimension scores (leadership, communication, career development, compensation, work environment, teamwork, recognition, well-being, safety, company pride), (c) scores by demographic segment, (d) open-ended response themes (NLP-based sentiment analysis), (e) comparison to prior period and external benchmarks | System | — | Automated |
| 6 | HR Business Partner prepares engagement results presentation: company-wide results, location-level breakdown (store/DC/HQ), dimension analysis, strongest and weakest areas, verbatim theme summary, and action planning framework | HR Business Partner | CHRO | 8 hours |
| 7 | CHRO presents company-wide results to C-suite and Department Heads; each Department Head receives their department-specific results with action planning template; Store Managers receive store-specific results via Regional Manager | CHRO | CEO | 2 hours |
| 8 | Action planning: each Store Manager and Department Head identifies top 3 engagement actions for their area (using action planning template); actions must be specific, measurable, and achievable within 6 months; system tracks action plan submission and completion | Store/DC Managers / Dept. Heads | HR Business Partner | 2 hours |
| 9 | Monthly: HR Business Partner tracks action plan execution; facilitates peer learning among Store Managers on effective engagement practices; updates engagement dashboard with action completion rates | HR Business Partner | — | 4 hours |
| 10 | Semi-annual: pulse survey measures progress on focus areas from previous comprehensive survey; results compared to baseline to validate improvement | HR Business Partner | CHRO | Per Steps 1-8 |

### System Touchpoints
- Online survey platform: survey configuration, distribution, collection, analytics
- ERP HR module: employee demographics, organizational hierarchy, response rate tracking
- ERP BI module: engagement dashboard, trend analysis, benchmarking
- Mobile app: survey access, action plan tracking, manager reminders

### Pain Points / Risks
- **Survey fatigue**: employees tired of surveys without seeing results may not participate; mitigated by visible action on prior survey results, clear communication of changes made, and limiting survey frequency
- **Anonymity concerns**: employees may fear responses can be traced back to them, especially in small departments; mitigated by third-party survey administration, suppression of results for groups < 5 respondents, and transparent anonymity methodology
- **Low store response rates**: store employees during shifts may not have time for survey; mitigated by dedicated survey time during shift, tablet access in break room, and response rate targets tied to Store Manager accountability
- **Action plan execution gap**: managers may create action plans but not execute them; mitigated by monthly tracking, peer accountability, and engagement score improvement as factor in Store Manager performance evaluation

### Staffing Implication
- **HR Business Partner**: ~4 hours setup + ~2 min/day × 14 days monitoring + ~8 hours analysis + ~4 hours/month action tracking = ~20 hours per survey cycle. Absorbed within existing role with project allocation.
- **CHRO**: ~2 hours per survey cycle for executive presentation. Absorbed within existing role.
- **Store/DC Managers**: ~2 hours per survey cycle for action planning. Absorbed within existing role.

---

## W630. Employee Recognition & Rewards Program Management

| Field | Detail |
|---|---|
| **Trigger** | Employee achievement; monthly/quarterly/annual recognition cycle; peer nomination |
| **Frequency** | Continuous peer recognition; monthly spot awards; quarterly excellence awards; annual milestone recognition |
| **Volume** | ~600-800 peer recognitions/month; ~50-100 spot awards/month; ~20-30 quarterly awards; ~150-200 annual service milestones |
| **Owner** | HR Coordinator |
| **Participants** | HR Coordinator, Store/DC Managers, Department Heads, CHRO, all employees |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Peer recognition (continuous)**: any employee sends peer recognition via mobile app — selects colleague, selects recognition type (Great Service, Team Player, Innovation, Safety Champion, Living Our Values), writes brief message (max 200 characters); recipient and their supervisor receive notification; system tallies peer recognitions per employee per month | Employee | — | 2 min |
| 2 | **Spot awards (monthly)**: Store Manager and Department Supervisors can award spot bonuses (PHP 500-2,000) for exceptional performance: (a) exceeding sales target by > 20%, (b) preventing safety incident, (c) outstanding customer service (validated by customer feedback per W608), (d) cost-saving suggestion implemented; Store Manager approves and submits to HR Coordinator for payroll processing | Store Manager / Dept. Supervisor | HR Coordinator | 5 min/award |
| 3 | **Quarterly excellence awards**: Department Heads nominate employees for quarterly awards in 5 categories: Sales Excellence, Customer Champion, Innovation, Safety Leader, and Team Player of the Quarter; nominations include achievement description and supporting metrics | Dept. Head / Store Manager | HR Coordinator | 15 min/nomination |
| 4 | HR Coordinator compiles nominations; CHRO and selection committee review; select winners per category (1 per region for store-level, 1 per HQ department); winners receive certificate, monetary award (PHP 5,000-10,000), and recognition on company intranet | HR Coordinator | CHRO | 4 hours/quarter |
| 5 | **Annual service milestones**: system auto-identifies employees reaching service milestones (5, 10, 15, 20, 25 years); generates milestone list 60 days before anniversary; HR Coordinator coordinates recognition: (a) 5 years: certificate + PHP 5,000 gift, (b) 10 years: plaque + PHP 10,000 gift + extra VL day, (c) 15+ years: personalized award + PHP 15,000+ gift + extra VL day + CEO handshake event | System / HR Coordinator | CHRO | 2 hours/month |
| 6 | **Employee of the Year (annual)**: Regional Managers nominate 1 store employee per region; HQ Department Heads nominate 1 per department; finalists presented to CHRO and CEO; winner receives PHP 50,000, trophy, feature in company newsletter, and development opportunity (conference attendance or special project assignment) | Regional Manager / Dept. Head | CEO | 4 hours/year |
| 7 | Monthly: HR Coordinator generates recognition program analytics — peer recognition volume by department/location, spot award distribution, budget utilization, and program participation rate; identifies locations with low recognition activity for Store Manager coaching | HR Coordinator | HR Business Partner | 2 hours |
| 8 | Quarterly: HR Business Partner correlates recognition data with engagement scores (per W629) and attrition rates (per W628); validates recognition program impact on retention and engagement; recommends program adjustments to CHRO | HR Business Partner | CHRO | 4 hours |

### System Touchpoints
- ERP HR module: recognition and rewards tracking, service milestone calculation
- ERP Payroll module: spot award and bonus payment processing
- Mobile app: peer recognition submission, award notifications, milestone alerts
- Company intranet: winner announcements, recognition wall, leaderboard
- BI dashboard: recognition analytics, program participation, budget tracking

### Pain Points / Risks
- **Recognition inequity**: some Store Managers may be more generous with spot awards than others, creating perceived unfairness across 200 stores; mitigated by spot award budget allocation per store (PHP 10,000/month) and system-tracked distribution analytics
- **Peer recognition trivialization**: employees may exchange peer recognitions without genuine merit; mitigated by supervisor co-sign requirement for recognitions > 5 per month per employee and quality spot-check by HR
- **Budget overruns**: spot awards and quarterly awards may exceed allocated budget; mitigated by monthly budget tracking and approval workflow for awards exceeding threshold
- **Remote worker exclusion**: DC and provincial store employees may feel excluded from HQ-centric awards; mitigated by regional representation in quarterly and annual awards

### Staffing Implication
- **HR Coordinator**: ~2 hours/month on program administration + ~4 hours/quarter on awards processing = ~4 hours/month. Absorbed within existing role.
- **CHRO**: ~2 hours/quarter on award selection + ~4 hours/year on annual awards = ~3 hours/quarter. Absorbed within existing role.
- **Store/DC Managers**: ~5 min/spot award × ~5 awards/month = ~25 min/month. Absorbed within existing role.

---

## W641. Off-Cycle & Ad-Hoc Payment Processing
- **Trigger**: Off-cycle payment request (DOLE order for back-pay, NLRC decision, retroactive wage adjustment, corrected payslip, emergency salary release, final pay outside regular payroll run)
- **Frequency**: ~50–80 off-cycle payments/month
- **Volume**: ~15–20 per entity per month
- **Owner**: Payroll Manager
- **Participants**: HR Business Partner (requester), Finance Manager (approver), Payroll Specialist (processor), Employee (payee)
- **Steps**:
  1. HR Business Partner or Department Head submits off-cycle payment request via self-service portal with: employee ID, payment type (back-pay, wage adjustment, corrected payslip, emergency release, court-ordered), amount or basis of computation, supporting documentation (DOLE order, NLRC decision, management memo), and urgency classification (standard 3-day, urgent next-business-day) (R: HR Business Partner, A: Payroll Manager, Duration: 15 min/request)
  2. Payroll Manager validates request: confirms employee status (active, on-leave, separated), verifies supporting documentation completeness, confirms correct payment type classification (R: Payroll Manager, A: Finance Manager, Duration: 30 min/request)
  3. For amounts > PHP 50,000 or retroactive periods > 6 months: route to Finance Manager for approval before processing (R: Finance Manager, A: CFO, Duration: 1 day)
  4. Payroll Specialist processes off-cycle payment: computes gross amount, applies statutory deductions (SSS, PhilHealth, Pag-IBIG, BIR withholding tax) per TRAIN law tables, nets to take-home pay (R: Payroll Specialist, A: Payroll Manager, Duration: 30 min/payment)
  5. System validates minimum wage protection (net pay cannot fall below applicable regional minimum wage for the period); flags if violation detected (R: System, A: Payroll Manager, Duration: Automated)
  6. Payroll Specialist generates bank file for off-cycle crediting or manual check preparation; routes for bank file approval (R: Payroll Specialist, A: Payroll Manager, Duration: 15 min/batch)
  7. System auto-adjusts next regular payroll run to reflect off-cycle payment: updated YTD totals, adjusted tax withholding for remaining periods, corrected statutory deduction brackets (R: System, A: Payroll Specialist, Duration: Automated)
  8. Payroll Specialist generates corrected payslip (if applicable) or supplementary payslip with detailed computation; distributes to employee (R: Payroll Specialist, A: Payroll Manager, Duration: 10 min)
- **System Touchpoints**: Payroll module (off-cycle batch processing), tax engine (TRAIN law tables), statutory deduction calculator, bank file generator, employee self-service portal (payslip distribution)
- **Time Estimate**: Standard: 2–3 days from request to payment; Urgent: next business day
- **Pain Points / Risks**: Minimum wage protection violations when large deductions offset regular pay; complex tax computation for retroactive adjustments spanning multiple tax brackets; YTD accumulation errors if off-cycle payments not properly integrated into regular payroll; DOLE compliance timeline for back-pay orders (typically 5 working days from decision)

---

## W642. HMO & Private Benefits Administration
- **Trigger**: New hire enrollment (W15); annual renewal; qualifying life event (marriage, birth, dependent change); employee separation (W43)
- **Frequency**: ~100–130 enrollment/changes/month (new hires + events); annual renewal for 6,715 employees
- **Volume**: ~6,715 covered employees + ~2,000 dependents across 5 entities
- **Owner**: HR Benefits Specialist
- **Participants**: HR Business Partner, Employee, HMO Provider Representative, Finance Analyst
- **Steps**:
  1. For new hire enrollment: HR Benefits Specialist enrolls employee in HMO plan within 5 business days of onboarding (W15); selects plan tier based on job level (executive, managerial, staff); collects dependent information and supporting documents (marriage certificate, birth certificates) (R: HR Benefits Specialist, A: HR Manager, Duration: 20 min/employee)
  2. For qualifying life events: Employee submits life event notification within 30 days of event with supporting documentation; HR Benefits Specialist updates enrollment; HMO provider adds/removes dependents (R: HR Benefits Specialist, A: HR Manager, Duration: 15 min/change)
  3. Monthly: HR Benefits Specialist reconciles HMO enrollment roster against employee master (W292) to identify coverage gaps (un-enrolled new hires, terminated employees still covered) (R: HR Benefits Specialist, A: HR Manager, Duration: 4 hours/month)
  4. Monthly: Finance Analyst verifies HMO premium invoice against enrollment roster and contracted rates; approves for payment (R: Finance Analyst, A: Finance Manager, Duration: 2 hours/month)
  5. Quarterly: HR Benefits Specialist compiles HMO utilization report from provider (consultations, hospitalizations, max benefit limit utilization, top conditions); identifies trends and recommendations for plan design changes (R: HR Benefits Specialist, A: HR Manager, Duration: 1 day/quarter)
  6. Annual renewal: HR Manager negotiates premium rates and plan design with HMO provider based on utilization data and market benchmarking; obtains competitive quotes from 2 alternative providers; presents recommendation to CHRO (R: HR Manager, A: CHRO, Duration: 2 weeks)
  7. For separation (W43): HR Benefits Specialist processes HMO coverage termination effective last day of employment; provides conversion option information to separating employee (individual continuation per HMO policy) (R: HR Benefits Specialist, A: HR Manager, Duration: 10 min)
- **System Touchpoints**: HR module (benefits enrollment), employee self-service portal (dependent management, utilization inquiry), HMO provider integration (enrollment feed, utilization data), AP module (premium payment)
- **Time Estimate**: Enrollment: 20 min/employee; monthly reconciliation: 4 hours; annual renewal: 2 weeks
- **Pain Points / Risks**: Enrollment data sync lag between HR system and HMO provider creates coverage gaps; dependent documentation fraud (fake birth certificates); rising HMO premiums in Philippine market (10–15% annual increase); max benefit limit exhaustion for high-cost hospitalizations; employee dissatisfaction with provider network limitations in provincial areas

---

## W643. Final Pay Computation & Separation Settlement
- **Trigger**: Employee separation (resignation, termination, retirement, end of contract) per W43
- **Frequency**: ~100–130 separations/month (~15–20% annual turnover rate)
- **Volume**: ~5–7 per business day across all entities
- **Owner**: Payroll Specialist
- **Participants**: HR Business Partner, Department Head (clearance sign-off), Finance Analyst, Employee
- **Steps**:
  1. HR Business Partner initiates final pay computation trigger in system on separation effective date (or upon receipt of resignation letter for proactive processing); classifies separation type (resignation, termination for just cause, authorized cause separation, retirement, end of contract) (R: HR Business Partner, A: HR Manager, Duration: 10 min)
  2. System auto-computes final pay components: (a) proportionate basic salary through last day, (b) proportionate 13th month pay per PD 851 (1/12 × monthly basic × months worked), (c) cash conversion of unused Service Incentive Leave (minimum 5 days per Labor Code; company policy may grant more), (d) proportionate Sil (if company grants beyond 5 days statutory minimum), (e) overtime/holiday/night differential unpaid in last period, (f) separation pay if applicable (authorized causes per Art. 298–299: redundancy = ½ month per year, retrenchment = 1 month per year, etc.), (g) retirement pay per RA 7641 if qualified (½ month per year of service) (R: System, A: Payroll Specialist, Duration: Automated computation)
  3. Payroll Specialist reviews system computation; validates each component against employee's records: attendance, leave balance, salary history, outstanding loans (W76), prior 13th month payments (R: Payroll Specialist, A: Payroll Manager, Duration: 30 min)
  4. Payroll Specialist computes statutory deductions: (a) withholding tax on final pay per BIR rules (different treatment for resignation vs. retirement vs. termination — retirement pay and separation pay below PHP 90,000 threshold are tax-exempt per TRAIN law Section 32(B)(6)(b)), (b) final SSS, PhilHealth, Pag-IBIG contributions for last period, (c) outstanding employee loan deductions, (d) salary advance or cash advance offsets, (e) company property non-return deductions (if authorized per policy) (R: Payroll Specialist, A: Payroll Manager, Duration: 20 min)
  5. Payroll Manager approves final pay computation; validates net pay is non-negative (minimum wage protection does not apply to final pay but net should not be zero unless deductions exceed pay) (R: Payroll Manager, A: HR Manager, Duration: 10 min)
  6. Finance Analyst processes payment: generates bank transfer file for direct deposit; for employees without bank accounts, prepares manual check (R: Finance Analyst, A: Finance Manager, Duration: 15 min)
  7. HR Business Partner coordinates clearance process: ensures all department clearances completed (IT equipment return per W152, company property return, PPE return per W172, confidential document return) before payment release (R: HR Business Partner, A: HR Manager, Duration: 1–5 days clearance)
  8. Payment released within DOLE Advisory 06-2020 timeline: 30 days from separation date for resignation; immediately for termination/retirement; or per specific DOLE/Labor Arbiter order (R: Payroll Specialist, A: Payroll Manager, Duration: Per timeline)
  9. Employee receives final pay with itemized computation document; HR Business Partner obtains signed acknowledgment (R: HR Business Partner, A: HR Manager, Duration: 15 min)
- **System Touchpoints**: Payroll module (final pay computation), tax engine (separation pay tax rules), loan management (W76 outstanding balance), leave management (unused leave balance), employee master (salary history, employment dates)
- **Time Estimate**: 1–2 hours computation + 1–5 days clearance + payment processing
- **Pain Points / Risks**: 30-day DOLE timeline pressure when clearance delays occur; complex tax computation for different separation types; separation pay computation errors for authorized causes (different formulas per cause); NLRC disputes when employee contests final pay; outstanding loan offsets that reduce net pay significantly

---

## W644. 13th Month Pay Reconciliation & Compliance
- **Trigger**: Monthly accrual cycle; December payment preparation
- **Frequency**: Monthly accrual booking; November review and reconciliation; December payment
- **Volume**: 6,715 employees across 5 entities
- **Owner**: Payroll Specialist
- **Participants**: Payroll Manager, Finance Analyst, HR Business Partner
- **Steps**:
  1. Monthly: System auto-accrues 13th month pay per employee based on basic salary earned during the month (1/12 of total basic salary earned from January 1); excludes allowances, overtime pay, night differential, and non-taxable benefits per PD 851 and DOLE guidelines (R: System, A: Payroll Specialist, Duration: Automated)
  2. Monthly: Payroll Specialist reviews accrual computation: validates base salary definition (basic salary only — excludes COLA, hazard pay, overtime, commissions unless mandated by CBA per W493); flags employees with mid-year salary changes for correct pro-ration (R: Payroll Specialist, A: Payroll Manager, Duration: 2 hours/month)
  3. Monthly: Finance Analyst posts accrual journal entry (DR 13th Month Pay Expense / CR 13th Month Pay Accrued Liability) per entity; verifies total accrual against payroll register (R: Finance Analyst, A: Finance Manager, Duration: 1 hour/month)
  4. November: Payroll Specialist performs comprehensive reconciliation: total accrued 13th month per employee vs. YTD basic salary ÷ 12; identifies discrepancies from mid-year salary changes, leaves without pay, absences, and split-entity employment (R: Payroll Specialist, A: Payroll Manager, Duration: 1 day)
  5. November: Payroll Specialist adjusts accruals for: (a) separating employees who already received proportionate 13th month in final pay (W643), (b) employees who received employer's elected half payment in May (if BuildRight practices May + December split), (c) employees with salary adjustments requiring retroactive accrual correction (R: Payroll Specialist, A: Payroll Manager, Duration: 0.5 day)
  6. November: Payroll Specialist computes tax impact: 13th month pay is tax-exempt up to PHP 90,000 threshold per TRAIN law Section 32(B)(6)(e); excess amount subject to graduated withholding tax; generates report of employees exceeding threshold for Finance Manager review (R: Payroll Specialist, A: Finance Manager, Duration: 0.5 day)
  7. December 1–15: Payroll Manager prepares 13th month payment batch: confirms final amounts per employee, validates bank account details, generates bank file, routes for approval (R: Payroll Manager, A: Finance Manager, Duration: 1 day)
  8. December 15–24: Finance Analyst executes payment via bank transfer; ensures all 6,715 employees receive payment by December 24 deadline per PD 851 (R: Finance Analyst, A: Finance Manager, Duration: 1 day)
  9. December 31: System reverses remaining accrual balance to actual payment; Finance Analyst reconciles GL accrual account to zero (R: Finance Analyst, A: Finance Manager, Duration: 0.5 day)
- **System Touchpoints**: Payroll module (13th month accrual and payment), GL (accrual journal entries), tax engine (PHP 90,000 threshold monitoring), employee master (salary history, employment dates)
- **Time Estimate**: Monthly: 3 hours; November reconciliation: 2 days; December payment: 2 days
- **Pain Points / Risks**: Confusion between basic salary and total compensation in 13th month base calculation; multi-entity employees requiring consolidated 13th month tracking; December 24 payment deadline falls during holiday bank processing delays; tax exemption threshold requires careful monitoring to avoid under/over-withholding; DOLE penalties for late 13th month payment

---

## W645. Strategic Workforce Planning
- **Trigger**: Annual planning cycle aligned with budget (W26); triggered by new store opening plan (10–15/year) or significant business change
- **Frequency**: Annual comprehensive plan; quarterly progress review; monthly headcount tracking
- **Volume**: 6,715 current headcount; ~10–15 new stores/year requiring ~290–435 net new hires; ~1,200–1,600 turnover replacements/year
- **Owner**: HR Manager (Workforce Planning)
- **Participants**: CHRO, VP Store Operations, VP Supply Chain, FP&A Manager, Regional Managers
- **Steps**:
  1. FP&A Manager provides business growth plan: new store openings by quarter, revenue targets by region, capex plan for new locations, and projected channel mix shifts (R: FP&A Manager, A: CFO, Duration: 1 day)
  2. VP Store Operations provides new store staffing requirements: 29 positions per new store (per company profile); ramp curve (Month 1: 80% staffing, Month 3: 100%); geographic distribution of new stores (R: VP Store Operations, A: COO, Duration: 1 day)
  3. VP Supply Chain provides DC and logistics headcount requirements: new DC activation plans, DC expansion staffing, fleet expansion requirements (R: VP Supply Chain, A: COO, Duration: 0.5 day)
  4. HR Manager analyzes current workforce supply: headcount by entity, location, department, job family, and employment type; identifies retirement eligibility within 12 months; analyzes turnover trends by location and department (W628 data); assesses internal pipeline from succession plans (W178) and cadetship (W179) (R: HR Manager, A: CHRO, Duration: 2 days)
  5. HR Manager performs gap analysis: demand (steps 1–3) minus supply (step 4) = hiring gap by role, location, and quarter; identifies critical roles with longest time-to-fill; quantifies headcount shortfall by entity (R: HR Manager, A: CHRO, Duration: 1 day)
  6. HR Manager develops hiring plan: recruitment volume by role and quarter; identifies sourcing channels (campus, referral, agency, direct); estimates recruitment budget (job board fees, agency fees, relocation costs, training costs per W51); proposes seasonal staffing plan (W555) (R: HR Manager, A: CHRO, Duration: 2 days)
  7. CHRO presents workforce plan and budget to CEO and CFO for approval; integrates with annual operating budget (W26) and capex plan (W21) (R: CHRO, A: CEO, Duration: 0.5 day)
  8. Monthly: HR Manager tracks actual hiring vs. plan; flags gaps to CHRO with corrective action recommendations (accelerate recruitment, redeploy from other locations, adjust new store timeline) (R: HR Manager, A: CHRO, Duration: 0.5 day/month)
- **System Touchpoints**: HR module (headcount and workforce analytics), FP&A planning module, budget module (W26), recruitment module (W15), succession planning (W178)
- **Time Estimate**: Annual plan: 5–7 days; monthly tracking: 0.5 day
- **Pain Points / Risks**: New store opening timeline changes invalidate hiring plan; Philippine labor market competition for store managers and skilled workers; geographic hiring challenges in provincial areas; high turnover undermining planned headcount stability; disconnect between finance headcount budget and HR recruitment capacity

---

## W646. HR Service Desk Operations
- **Trigger**: Employee inquiry or request received via any channel (walk-in, phone, email, chat, self-service ticket)
- **Frequency**: ~400–600 inquiries/week across all entities (~20,000–30,000/year)
- **Volume**: ~80–120 per day
- **Owner**: HR Service Desk Lead
- **Participants**: HR Assistant (Tier 1), HR Business Partner (Tier 2), HR Manager (Tier 3), Employee (inquirer)
- **Steps**:
  1. HR Assistant receives and logs inquiry in HR ticketing system; classifies by category (policy question, benefit inquiry, payroll concern, leave issue, document request, complaint, other) and entity; assigns priority (standard: 3-day SLA, urgent: 1-day SLA, emergency: 4-hour SLA) (R: HR Assistant, A: HR Service Desk Lead, Duration: 5 min/ticket)
  2. HR Assistant resolves Tier 1 inquiries from knowledge base: standard policy questions, FAQ responses, document request fulfillment (COE per W43, employment verification, payslip reprint), leave balance inquiry, benefit coverage inquiry (R: HR Assistant, A: HR Service Desk Lead, Duration: 10–20 min/ticket)
  3. For Tier 1 resolution: HR Assistant closes ticket with resolution notes and sends satisfaction survey to employee (R: HR Assistant, A: HR Service Desk Lead, Duration: 5 min)
  4. For Tier 2 escalation (complex benefit claims, payroll discrepancies, policy interpretation, leave disputes): HR Business Partner investigates and resolves within category SLA (R: HR Business Partner, A: HR Manager, Duration: 1–3 days)
  5. For Tier 3 escalation (complaints, disciplinary matters, union grievances, legal inquiries): HR Manager handles per relevant policy; coordinates with Legal (W125) or Compliance (W79) as needed (R: HR Manager, A: CHRO, Duration: 3–10 days)
  6. Weekly: HR Service Desk Lead reviews ticket analytics: volume by category and entity, SLA compliance rate, average resolution time, escalation rate, employee satisfaction score, knowledge base gaps (R: HR Service Desk Lead, A: HR Manager, Duration: 2 hours/week)
  7. Monthly: HR Service Desk Lead updates knowledge base with new FAQs, policy changes, and resolution patterns; identifies training needs for Tier 1 staff (R: HR Service Desk Lead, A: HR Manager, Duration: 4 hours/month)
- **System Touchpoints**: HR ticketing system, knowledge base portal, employee self-service module, payroll inquiry module, benefits administration module
- **Time Estimate**: Ongoing daily operations; ~2 FTE HR Assistants for Tier 1
- **Pain Points / Risks**: Volume spikes during payroll dates (15th/30th) and benefit enrollment periods; inconsistent knowledge base leading to incorrect answers; walk-in inquiries at 200 stores without local HR staff; phone inquiry hold times during peak periods; sensitive inquiry handling (complaints, payroll errors) requiring privacy beyond open ticketing system

---

## W647. Employee Data Privacy Compliance Operations
- **Trigger**: Ongoing operational compliance with RA 10173 (Data Privacy Act); triggered by data subject request, privacy impact assessment requirement, or regulatory deadline
- **Frequency**: Continuous compliance operations; quarterly compliance review; annual privacy program assessment
- **Volume**: ~6,715 active employee records + ~100,000 former applicant records + ~20,000 former employee records under retention
- **Owner**: Data Protection Officer (DPO)
- **Participants**: HR Manager, IT Security Lead, Legal Counsel, NPC (regulator)
- **Steps**:
  1. Quarterly: DPO conducts privacy compliance review of HR systems: verifies consent records are current for all active employees (per RA 10173 requirements for processing employee data), reviews data retention compliance (expired records destroyed per retention schedule), and assesses access controls on HR data (R: DPO, A: CHRO, Duration: 2 days/quarter)
  2. For data subject access requests (DSAR): Employee or former employee requests access to their personal data; DPO verifies identity, retrieves all records held across HR, payroll, benefits, and medical systems; provides response within 30 days per RA 10173; no fee for first request per year (R: DPO, A: Legal Counsel, Duration: 3–5 days/request)
  3. For data rectification requests: Employee requests correction of inaccurate personal data; DPO coordinates with HR to verify and update across all systems (employee master W292, payroll, benefits, SSS/PhilHealth/Pag-IBIG if affected) (R: DPO, A: HR Manager, Duration: 5 days/request)
  4. For new HR system or process: DPO conducts Data Privacy Impact Assessment (DPIA per W389 adapted for HR context); identifies privacy risks, recommends mitigations, and provides clearance for implementation (R: DPO, A: CHRO, Duration: 3–5 days/assessment)
  5. For HR data breach (e.g., unauthorized access to employee records, lost employee files): DPO activates breach response protocol — containment within 24 hours, assessment within 48 hours, NPC notification within 72 hours if breach is notifiable, affected employee notification within 5 days, remediation plan within 30 days (R: DPO, A: CHRO, Duration: Per breach severity)
  6. Annual: DPO conducts comprehensive privacy program assessment; reviews consent validity, data processing lawfulness, third-party data sharing compliance (HMO providers, benefits providers, payroll bank), and retention schedule enforcement; submits annual compliance report to CHRO and NPC (R: DPO, A: CHRO, Duration: 5 days)
  7. Annual: DPO ensures NPC registration renewal (per W434) covers all HR data processing systems and activities (R: DPO, A: CHRO, Duration: 1 day)
- **System Touchpoints**: HR module (employee data), payroll system, benefits administration, DPO compliance tool, NPC registration portal, data subject request portal
- **Time Estimate**: Quarterly review: 2 days; DSAR: 3–5 days each; annual assessment: 5 days
- **Pain Points / Risks**: Employee data spread across multiple systems (HR, payroll, benefits, recruitment) complicating DSAR fulfillment; third-party data sharing with HMO and benefits providers requires Data Processing Agreements; NPC enforcement increasing in Philippines; high-volume applicant data (100,000+ records) with complex retention rules; balancing data privacy with legitimate business need for employee monitoring

---

## W682. Employee Career Development & Internal Job Posting Operations

| Field | Detail |
|---|---|
| **Trigger** | Monthly internal job posting cycle; employee career development plan review |
| **Frequency** | Monthly job posting; quarterly career development review; annual talent review |
| **Volume** | ~50-80 internal job postings/year; ~1,200-1,600 external hires/year (internal fill target: 30%) |
| **Owner** | HR Business Partner |
| **Participants** | Hiring Manager, HR Coordinator, Department Head, Employee |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Hiring Manager submits job requisition for open position; HR Coordinator checks if position is eligible for internal posting first per company policy (all non-entry-level positions posted internally for 5 business days before external sourcing) | Hiring Manager | HR Coordinator | 30 min |
| 2 | HR Coordinator posts position on internal job board (ERP self-service portal): job description, required qualifications, location, department, salary range indication, and application deadline | HR Coordinator | — | 30 min |
| 3 | Employee submits internal application with current resume, manager endorsement (or confidential application for sensitive situations), and statement of interest | Employee | — | 1 hour |
| 4 | HR Business Partner screens internal applications: verifies minimum qualifications met, confirms employee is off probation (≥ 6 months in current role), checks performance rating (≥ satisfactory), validates no active disciplinary actions per W603 | HR Business Partner | — | 1-2 hours |
| 5 | HR Business Partner coordinates interview with Hiring Manager; for cross-entity transfers, ensures payroll entity change feasibility per HR-018 | HR Business Partner | Hiring Manager | 1 hour |
| 6 | Hiring Manager interviews internal candidates alongside external candidates (if external sourcing initiated after internal posting period); gives preference to equally qualified internal candidates per policy | Hiring Manager | — | 1-2 hours per candidate |
| 7 | If internal candidate selected: HR Business Partner processes transfer per W511 (cross-entity) or department change; current manager receives 30-day transition period notification; effective date coordinated between departments | HR Business Partner | Department Head | 2 hours |
| 8 | If internal candidate not selected: HR Business Partner provides constructive feedback to employee; suggests development areas per W683 competency assessment; updates career development plan | HR Business Partner | — | 30 min |
| 9 | Quarterly: HR Business Partner reviews career development plans for high-potential employees per W178 succession plan; identifies readiness for promotion; coordinates stretch assignments and cross-training per W567 | HR Business Partner | Department Head | 1 day |
| 10 | Annual: HR Manager conducts talent review with Department Heads: succession pipeline strength, internal promotion rate, internal mobility heat map, and career development program effectiveness metrics | HR Manager | Department Heads | 3 days |

### System Touchpoints
- Internal job board
- Employee self-service portal
- Applicant tracking module
- Employee master (W292)
- Performance module (W72)
- Succession planning module (W178)

### Time Estimate
- Per posting: 3-5 hours
- Quarterly review: 1 day
- Annual talent review: 3 days

### Pain Points / Risks
- Current manager resistance to releasing good employees
- Employee reluctance to apply for fear of current manager reaction
- Salary equity issues when internal transfers result in different pay for same role
- Provincial store employees having fewer internal opportunities than HQ

### Staffing Implication
- HR Business Partner: ~5 hours/week on internal mobility
- Absorbed within existing role

---

## W683. Employee Competency Assessment & Certification Management

| Field | Detail |
|---|---|
| **Trigger** | Annual competency assessment cycle; role-change events; regulatory certification requirements |
| **Frequency** | Annual formal assessment; semi-annual recertification for safety-critical roles; ad-hoc for role changes |
| **Volume** | 6,715 employees across 5 entities; ~200 unique competency profiles across roles |
| **Owner** | HR Training Manager |
| **Participants** | Department Supervisor/Manager, HR Business Partner, Employee, External Certification Body |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | HR Training Manager maintains competency framework per role: store associate (product knowledge per department, POS operations, customer service, safety), store supervisor (leadership, inventory management, merchandising, scheduling), DC staff (forklift, RF scanning, safety, hazmat), corporate staff (role-specific technical competencies) | HR Training Manager | — | Ongoing |
| 2 | Annual: system generates competency assessment schedules for all employees based on role and last assessment date; Department Supervisor receives assessment forms per direct report | HR Training Manager | Department Supervisor | 1 hour setup |
| 3 | Employee completes self-assessment against competency profile: rates each competency 1-5 (1=Awareness, 2=Basic, 3=Intermediate, 4=Advanced, 5=Expert) with supporting evidence | Employee | — | 1 hour |
| 4 | Department Supervisor conducts assessment: reviews self-assessment, validates through observation and practical demonstration for technical skills, interviews employee on behavioral competencies, assigns final rating | Department Supervisor | — | 1-2 hours |
| 5 | System auto-generates competency gap analysis: identifies competencies below role minimum level (target level by competency); produces individual development plan (IDP) template with recommended training interventions per W51 | System (automated) | HR Training Manager | Automated |
| 6 | For safety-critical roles requiring regulatory certification (forklift operator, electrical worker, hazmat handler per W655): HR Training Manager tracks certification expiry dates; schedules recertification before expiry; system restricts work assignments for expired certifications | HR Training Manager | — | 2 hours/month ongoing |
| 7 | For trade-specific certifications (PCAB for construction project sales per W162, PRC license for engineers per W600): HR Business Partner verifies active license status; tracks continuing professional development (CPD) units | HR Business Partner | — | 2 hours/month ongoing |
| 8 | Quarterly: HR Training Manager produces competency dashboard for HR Manager: assessment completion rate, average competency scores by role/location, gap distribution, certification compliance rate (target ≥ 95% per W655) | HR Training Manager | HR Manager | 1 day |
| 9 | Annual: HR Manager reviews competency framework effectiveness with Department Heads; updates competency profiles based on evolving role requirements (e.g., digital skills, new product categories); calibrates assessment standards across 200 stores and 4 DCs | HR Manager | Department Heads | 3 days |

### System Touchpoints
- Competency management module
- Learning management system
- Certification tracking
- Employee master (W292)
- Safety certification module (W655)

### Time Estimate
- Per employee assessment: 1-2 hours
- Annual cycle management: 20 days across all entities
- Quarterly reporting: 1 day

### Pain Points / Risks
- Assessment subjectivity across 200 stores (different supervisors applying different standards)
- Competency framework becoming outdated as roles evolve
- Certification tracking complexity with multiple regulatory bodies
- Employee resistance to competency gap identification

### Staffing Implication
- HR Training Manager: ~5 days/quarter on assessment cycle management
- Department Supervisors: ~2 hours/employee/year
- Absorbed within existing roles

---

## W715. Employee Referral Program Management & Reward Processing

| Field | Detail |
|---|---|
| **Trigger** | Employee submits a referral for an open position; or referred candidate is hired |
| **Frequency** | Ongoing (~100-150 referrals/month across 6,715 employees) |
| **Volume** | ~1,200-1,600 annual hires, target 20-25% from referrals (~240-400 referral hires/year) |
| **Owner** | HR Manager |
| **Participants** | Referring Employee, Hiring Manager, HR Recruiter, Payroll Accountant |

### Background

Employee referrals are the highest-quality and lowest-cost source of hires in retail. With ~1,200-1,600 annual hires and 15-20% turnover, BuildRight Depot's 6,715 employees represent a powerful recruitment network. Referred candidates have higher retention rates, faster time-to-productivity, and lower recruitment cost per hire. This workflow manages the referral lifecycle from submission to reward payout, complementing W15 (recruitment & onboarding).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Referral submission**: referring employee submits candidate via HR self-service portal or mobile app: (a) selects open position from active job postings; (b) enters candidate name, contact info, and relationship; (c) optional: uploads candidate resume; (d) system creates referral record linked to referring employee and open position; (e) system sends confirmation email to referring employee with referral tracking number | Referring Employee | — | 10 min |
| 2 | **Referral validation**: HR Recruiter validates referral within 2 business days: (a) check if candidate already exists in applicant database (from previous applications or other referrals); (b) verify referring employee is eligible (active employee, not on disciplinary action, not the hiring manager for the position); (c) verify candidate meets minimum qualifications for the position; (d) if invalid: notify referring employee with reason; (e) if valid: proceed to candidate outreach | HR Recruiter | HR Manager | 15-30 min per referral |
| 3 | **Candidate processing**: referred candidate enters standard recruitment pipeline per W15: (a) HR Recruiter contacts candidate within 3 business days (priority over non-referral applicants); (b) interview scheduling and assessment per W15 steps; (c) hiring manager receives notification that candidate is a referral with referring employee name; (d) system tracks referral status: Submitted → Validated → Interviewing → Offer → Hired / Not Hired | HR Recruiter / Hiring Manager | — | Per W15 |
| 4 | **Referral reward eligibility determination**: upon candidate hire: (a) system verifies referral-to-hire criteria: (i) candidate completed probationary period (6 months for store-level, 3 months for HQ); (ii) referring employee still actively employed at time of reward; (iii) candidate was not already in the active applicant pool (referred before any other application); (b) reward tier: Store-level position = PHP 5,000; HQ/supervisory position = PHP 10,000; Management/technical position = PHP 15,000-25,000; (c) system generates reward eligibility notification to HR Manager | System / HR Recruiter | HR Manager | Automated + 15 min verification |
| 5 | **Reward processing**: upon eligibility confirmation: (a) HR Manager approves referral reward; (b) Payroll Accountant processes reward through next available payroll run per W10: (i) reward added as non-taxable benefit (BIR-exempt under de minimis if within threshold) or taxable supplement per current tax ruling; (ii) reward split: 50% at hire confirmation, 50% after candidate completes probationary period; (c) system sends notification to referring employee: "Your referral [Name] has been hired! PHP [X] reward will be included in your [Date] payroll."; (d) referral reward tracked in employee's referral history for program reporting | Payroll Accountant / HR Manager | HR Manager | 15-20 min per reward |
| 6 | **Quarterly program analytics**: HR Manager generates quarterly referral program report: (a) total referrals submitted, validated, hired; (b) conversion rate: referral-to-hire vs. general applicant-to-hire; (c) time-to-fill comparison: referral positions vs. standard recruitment; (d) retention rate: referral hires vs. non-referral hires at 6-month and 12-month mark; (e) referral reward cost vs. agency/recruitment platform cost per hire; (f) department-level referral participation rate; (g) top referrers recognition; (h) recommendations for program improvement (reward amounts, eligible positions, promotion) | HR Manager | CHRO | 2-3 hours/quarter |

### System Touchpoints

- HR self-service portal with referral submission module
- Applicant tracking system linked to recruitment pipeline per W15
- Employee master data per W292 for eligibility verification
- Payroll module per W10 for reward processing
- Referral analytics dashboard for quarterly reporting
- Job posting board integration for open position selection

### Pain Points / Risks

- **Referral quality decline**: as referral volume increases, quality may decrease if employees refer unqualified candidates to earn rewards; mitigated by validation step and reward split tied to probation completion
- **Hiring manager bias**: hiring managers may feel pressure to favor referred candidates to maintain relationships with colleagues, potentially overlooking better-qualified external candidates; mitigated by standard assessment process per W15
- **Referral reward taxation complexity**: BIR treatment of referral rewards varies based on amount and frequency; amounts exceeding de minimis thresholds are taxable compensation requiring proper withholding per HR-003
- **Program fatigue**: initial enthusiasm may wane after employees exhaust their networks; program needs ongoing promotion, success story sharing, and periodic reward tier adjustments
- **Exclusion of new employees**: employees on probationary status may feel excluded from the program if eligibility is restricted to regular employees only

### Staffing Implication

HR Recruiter: ~5-8 hours/month on referral validation and candidate processing (absorbed within existing recruitment duties). Payroll Accountant: ~2-3 hours/month on reward processing. HR Manager: ~2-3 hours/quarter on analytics. No incremental headcount.

### Time Estimate

**Per referral**: ~30-45 min total HR time (10 min submission + 15-30 min validation + processing through W15). **Reward processing**: 15-20 min per hire. **Quarterly analytics**: 2-3 hours.

---

## W716. Internal Communication & Company-Wide Announcement Management

| Field | Detail |
|---|---|
| **Trigger** | Need to communicate company-wide or targeted information to employees; regulatory update affecting operations; policy change; crisis communication; executive announcement |
| **Frequency** | Daily (mixed channels); major announcements ~2-4/month |
| **Volume** | ~10-15 internal communications/week across 6,715 employees in 205+ locations |
| **Owner** | Internal Communications Manager |
| **Participants** | Department Head (content owner), CHRO, CEO/Executive Office, IT (distribution), Store Manager (cascading) |

### Background

BuildRight Depot's 6,715 employees across 200 stores, 4 DCs, and HQ need timely, accurate information to perform their roles effectively. With a geographically dispersed workforce spanning the Philippine archipelago, internal communication is both more critical and more challenging than in a single-location company. This workflow manages the lifecycle of internal communications from creation through distribution, acknowledgment tracking, and effectiveness measurement. It complements W571 (store-level daily communication) which handles routine daily memos, by addressing strategic, enterprise-wide communications.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Communication request**: department head or executive initiates communication request: (a) identifies topic: policy change, regulatory update, company announcement, crisis communication, event notification, HR update; (b) determines urgency: urgent (within 2 hours), standard (within 24 hours), scheduled (planned date); (c) identifies target audience: all employees, store-level only, management only, specific departments, specific regions; (d) submits content draft to Internal Communications Manager | Department Head / Executive | — | 30-60 min |
| 2 | **Content development**: Internal Communications Manager develops communication: (a) reviews content for accuracy, completeness, and clarity; (b) translates to Filipino for store-level audiences where appropriate (bilingual format); (c) formats for channel: email for detailed content, SMS/mobile push for urgent/short, digital signage per W504 for in-store, intranet post for reference, town hall briefing script for W231; (d) determines need for acknowledgment tracking (compliance-sensitive communications require signed acknowledgment); (e) develops FAQ or talking points for manager cascading if needed | Internal Comms Manager | CHRO | 1-3 hours |
| 3 | **Review and approval**: (a) content owner reviews for accuracy; (b) CHRO reviews for sensitivity and employee relations impact; (c) for policy changes: Legal Counsel review per W230; (d) for crisis communications: CEO approval per W134; (e) approved content queued for distribution | Content Owner / CHRO / Legal | CEO (for crisis) | 30-60 min |
| 4 | **Distribution**: system distributes communication through appropriate channels: (a) email to targeted employee groups via employee master distribution lists; (b) mobile push notification via employee app for urgent items; (c) digital signage update per W504 for in-store visual communications; (d) intranet posting for permanent reference; (e) SMS for store-level employees without email/app access (field and warehouse staff); (f) manager cascade pack: talking points and FAQ for Store Managers and Department Supervisors to discuss in daily huddles | System / IT | Internal Comms Manager | 15-30 min |
| 5 | **Acknowledgment tracking**: for compliance-sensitive communications (policy changes, safety updates, regulatory requirements): (a) system generates acknowledgment request to each targeted employee; (b) employee acknowledges via mobile app, self-service portal, or physical sign-off form (for non-digital employees); (c) system tracks acknowledgment rate by location, department, and role; (d) Store Manager follows up on unacknowledged communications within 48 hours; (e) escalation to Regional Manager if store acknowledgment rate <90% within 72 hours | System / Store Manager | Regional Manager | Automated + 30 min/day follow-up |
| 6 | **Effectiveness measurement**: monthly, Internal Communications Manager reviews: (a) communication volume and channel utilization; (b) average read/open rate by channel (email, app, intranet); (c) acknowledgment completion rate for tracked communications (target: 95% within 72 hours); (d) employee feedback on communication quality (quarterly pulse survey); (e) recommendations for channel optimization and content improvement | Internal Comms Manager | CHRO | 2-3 hours/month |

### System Touchpoints

- Employee communication platform with multi-channel distribution
- Employee master data per W292 for audience targeting and distribution lists
- Mobile employee app with push notification capability
- Digital signage content management system per W504
- Intranet/knowledge base for permanent reference
- Acknowledgment tracking system with compliance reporting
- Analytics dashboard for read rates, open rates, and acknowledgment tracking

### Pain Points / Risks

- **Communication overload**: with ~10-15 communications/week, employees may experience message fatigue, causing important communications to be missed or ignored; mitigated by strict prioritization and channel selection
- **Non-digital employee reach**: ~5,800 store-level and DC employees may have limited email/app access during working hours; reliance on manager cascading and physical sign-off creates gaps
- **Bilingual communication quality**: translating policy and regulatory content from English to Filipino risks nuance loss; important compliance communications must maintain legal accuracy in both languages
- **Cascading inconsistency**: Store Managers may interpret and communicate messages differently across 200 stores, leading to inconsistent understanding; mitigated by standardized talking points and FAQ
- **Acknowledgment without comprehension**: employees may acknowledge receiving communications without actually reading or understanding them, creating a false sense of compliance; mitigated by periodic comprehension spot-checks

### Staffing Implication

Internal Communications Manager: ~15-20 hours/week on content development, distribution, and tracking. Absorbed within existing Marketing team (shared resource with W143 PR & corporate communications) or a dedicated role if volume justifies. IT support: ~2-3 hours/week on distribution system management. No incremental headcount.

### Time Estimate

**Per standard communication**: 2-4 hours (30-60 min content request + 1-3 hours development + 30-60 min approval + 15-30 min distribution). **Urgent communications**: 1-2 hours from request to distribution. **Monthly effectiveness review**: 2-3 hours.

---

## W717. Workplace Violence Prevention & Response Protocol

| Field | Detail |
|---|---|
| **Trigger** | Threatening behavior by customer, employee, or third party; actual violent incident; report of domestic violence affecting workplace; robbery or armed threat |
| **Frequency** | Ad-hoc (rare but critical) |
| **Volume** | ~10-20 serious incidents/year across 200 stores; ~50-100 lower-level altercations/year |
| **Owner** | VP HR / Security Manager |
| **Participants** | Store Manager, Security Guard, Safety Officer, HR Manager, VP Legal, Police/Barangay |

### Background

Retail employees face elevated workplace violence risks: customer altercations, robbery, domestic violence spillover, and employee-on-employee conflicts. For BuildRight Depot with 200 stores across the Philippine archipelago, where some stores operate in high-crime urban areas and others in remote provincial locations, a structured violence prevention and response protocol is essential for employee safety, legal compliance under DOLE, and business continuity. This workflow complements W330 (emergency response), W471 (security incident reporting), and W140 (OHS incident management).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Prevention — Risk Assessment**: quarterly, Security Manager and HR conduct violence risk assessment per store: (a) review store crime statistics from local PNP and Barangay; (b) assess store physical security: CCTV coverage per W207, guard presence, lighting, parking lot visibility; (c) review prior incidents at store level; (d) identify high-risk periods: payday weekends per W578, late-night closing, isolated locations; (e) classify stores: Standard Risk, Elevated Risk, High Risk; (f) implement proportional prevention measures | Security Manager | VP HR | 2-3 days/quarter |
| 2 | **Prevention — Training**: annual workplace violence prevention training for all employees: (a) Module 1 — De-escalation Techniques (2 hours): verbal de-escalation, maintaining safe distance, recognizing escalation signs, when to disengage; (b) Module 2 — Robbery Response Protocol (1 hour): comply with demands, do not resist, observe and remember details, trigger silent alarm only when safe; (c) Module 3 — Active Threat Response (1 hour): Run-Hide-Fight protocol, evacuation routes per W695, assembly points, communication protocol; (d) training delivered by Security Manager with PNP-accredited trainer; (e) completion tracked in employee training record per W51 | Security Manager / HR Manager | VP HR | 4 hours/employee; ~27,000 training hours/year absorbed over annual cycle |
| 3 | **Immediate response — Active incident**: upon violent incident or threat: (a) Store Manager or senior staff on duty activates response protocol: (i) if active threat to life: trigger silent alarm to security provider and PNP; initiate evacuation per W695; (ii) if verbal altercation: intervene with de-escalation techniques; call security guard if escalation continues; (iii) if robbery in progress: comply, do not resist, observe details; (b) prioritize employee and customer safety over property; (c) if injuries: activate first aid response per W501; call emergency services (911 or local number); (d) secure scene after threat is resolved; preserve evidence for police | Store Manager / Security Guard | VP HR | Immediate |
| 4 | **Incident documentation**: within 2 hours of incident resolution: (a) Store Manager completes Workplace Violence Incident Report: (i) date, time, location; (ii) type of incident (customer altercation, robbery, employee conflict, domestic violence, threat); (iii) individuals involved; (iv) description of events; (v) injuries sustained; (vi) property damage; (vii) witnesses; (viii) police report number (if applicable); (ix) CCTV footage reference per W207; (b) report submitted to HR Manager and Security Manager via system | Store Manager | VP HR | 30-60 min |
| 5 | **Employee support**: within 24 hours: (a) HR Manager contacts affected employees: (i) offer immediate emotional support and counseling referral (Employee Assistance Program per W494 wellness program); (ii) provide information on workers' compensation claim process if injured; (iii) discuss work schedule accommodation (temporary reassignment, paid leave); (iv) ensure no retaliation or victim-blaming; (b) for witnesses: offer counseling referral; (c) for store-wide trauma: engage professional crisis counselor for group debriefing within 48 hours | HR Manager | VP HR | 2-4 hours per incident |
| 6 | **Investigation and resolution**: within 7 business days: (a) HR Manager and Security Manager conduct joint investigation: (i) interview involved parties and witnesses; (ii) review CCTV footage per W207; (iii) review prior incidents involving same individuals; (b) determine root cause and contributing factors; (c) implement corrective actions: (i) employee disciplinary action per W603 if employee-initiated violence; (ii) customer ban from store if customer-initiated; (iii) security upgrades if facility contributed; (iv) policy or training updates if systemic gap identified; (d) investigation report documented and filed | HR Manager / Security Manager | VP HR | 4-8 hours per incident |
| 7 | **Regulatory reporting**: if incident results in serious injury or fatality: (a) report to DOLE regional office within 24 hours per Labor Code; (b) report to Barangay and PNP as required; (c) for robbery: cooperate with police investigation; provide CCTV footage and witness statements; (d) for employee injury: file SSS sickness benefit claim per W251 | HR Manager / VP Legal | VP HR | 2-4 hours |
| 8 | **Post-incident review**: monthly, Security Manager reviews all workplace violence incidents: (a) trend analysis by location, time, type, and severity; (b) identify repeat-incident locations or patterns; (c) assess effectiveness of prevention measures; (d) update risk assessment per step 1; (e) report to VP HR and VP Store Operations with recommendations | Security Manager | VP HR | 2-3 hours/month |

### System Touchpoints

- Incident reporting module integrated with W140 (OHS incident management)
- CCTV system per W207 for evidence retrieval
- Employee training record per W51 for violence prevention training tracking
- Employee Assistance Program integration per W494
- SSS claim processing per W251 for injury-related claims
- Store risk assessment database with quarterly update tracking
- Police and Barangay reporting templates

### Pain Points / Risks

- **Underreporting of lower-level incidents**: employees often do not report verbal threats, customer intimidation, or minor altercations, creating blind spots in the risk assessment; mitigated by anonymous reporting option and manager training to recognize and document lower-level incidents
- **Security guard limitations**: contracted security guards may lack de-escalation training and may respond with excessive force, escalating rather than resolving incidents; requires security provider contract provisions for trained guards
- **Provincial store vulnerability**: remote stores with delayed police response times (30+ minutes) face greater risk during robbery or violent incidents; mitigated by enhanced physical security measures (barrier glass, panic rooms, GPS-enabled panic buttons)
- **Domestic violence spillover**: employees experiencing domestic violence may face threats or attacks at the workplace; DOLE requires employers to provide reasonable accommodation and support
- **PTSD and long-term effects**: employees who experience violence may develop anxiety, reduced job performance, or leave the company; counseling support and return-to-work programs are essential

### Staffing Implication

Security Manager: ~4-6 hours/week on prevention activities (risk assessment, training coordination, incident review). HR Manager: ~2-3 hours per incident for documentation, support, and investigation. Store Managers: absorbed within existing duties for prevention and response. No incremental headcount; counseling services contracted as needed.

### Time Estimate

**Prevention**: 4 hours/employee/year training + 2-3 days/quarter risk assessment. **Per incident**: 4-8 hours investigation + 2-4 hours employee support + 2-4 hours regulatory reporting (if applicable). **Monthly review**: 2-3 hours.

---

## W718. Employee Relocation & Housing Assistance Management

| Field | Detail |
|---|---|
| **Trigger** | Employee approved for cross-entity or cross-location transfer per W511 to a location requiring relocation; or new store opening per W702 requiring staff transfer; or management reassignment |
| **Frequency** | ~30-50 relocations/year (driven by new store openings, management rotations, and cross-entity transfers) |
| **Volume** | Average relocation cost: PHP 50,000-150,000 per employee depending on distance and family size |
| **Owner** | HR Manager |
| **Participants** | Transferring Employee, HR Manager, Finance (payroll), Receiving Store Manager, Corporate Housing Coordinator |

### Background

BuildRight Depot operates across the Philippine archipelago with 200 stores and 4 DCs spanning Mindanao, Visayas, and Luzon. Cross-location transfers per W511 — especially for management rotations, new store opening staffing per W702, and specialized role deployments — sometimes require employees to relocate to a different city or island. The Philippine geographic context (island-to-island moves involving ferries or flights, cost-of-living differences between Metro Manila and provincial areas, and family disruption) makes relocation support essential for transfer acceptance and employee retention. This workflow complements W511 (cross-entity/cross-location transfer) by addressing the logistical and financial aspects of relocation.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Relocation need identification**: when transfer is approved per W511: (a) HR Manager assesses relocation requirement: does the employee need to move residence to perform the new role?; (b) classify relocation: (i) Local transfer (within same city/municipality): no relocation support needed; (ii) Regional transfer (within same island, different city): moderate support; (iii) Inter-island transfer (Mindanao to Visayas, Visayas to Luzon, etc.): full relocation package; (iv) Metro Manila to provincial or vice versa: full relocation with cost-of-living adjustment consideration | HR Manager | CHRO | 30 min |
| 2 | **Relocation package determination**: HR Manager determines applicable package based on employee level and transfer type: (a) Management/Senior Staff: (i) temporary housing allowance (PHP 15,000-25,000/month for up to 3 months); (ii) house-hunting trip (1 trip, 3 days, transportation + accommodation); (iii) household goods shipping (up to 2 container loads); (iv) transportation for family (economy airfare + ferry for inter-island); (v) relocation assistance payment (PHP 30,000-50,000 one-time); (vi) school transfer assistance for dependents (PHP 10,000); (b) Store-level/Staff: (i) temporary housing in company billeting per W441 (up to 30 days); (ii) transportation (ferry/bus for inter-island); (iii) relocation assistance payment (PHP 10,000-20,000); (iv) optional: corporate housing per W441 if available at receiving location | HR Manager | CHRO | 30-60 min |
| 3 | **Approval and budget allocation**: (a) HR Manager prepares relocation cost estimate; (b) Finance Manager approves budget allocation from the transferring entity's HR budget; (c) for management-level relocations > PHP 100,000: CHRO approval required; (d) budget recorded in system linked to employee transfer record per W511 | HR Manager / Finance Manager | CHRO | 15-30 min |
| 4 | **Logistics coordination**: HR Manager coordinates relocation logistics: (a) book transportation (flights, ferries, ground transport); (b) arrange temporary housing at receiving location: company billeting per W441 or short-term rental; (c) engage moving company for household goods shipment; (d) coordinate with receiving Store Manager for welcome and settling-in support; (e) provide employee with relocation guide: local area information, schools, hospitals, markets, places of worship, transportation routes | HR Manager | — | 2-4 hours per relocation |
| 5 | **Employee relocation execution**: employee relocates: (a) system updates employee location master per W254; (b) payroll entity change processed per W511 with mid-period proration if applicable; (c) IT access updated for new location per W152; (d) employee checks into temporary housing; (e) Store Manager at receiving location provides orientation: store tour, introductions, community information | HR Manager / Store Manager | HR Manager | 1-2 days |
| 6 | **Permanent housing settlement**: within the temporary housing period (30-90 days): (a) employee finds permanent housing with HR assistance; (b) HR provides: list of nearby residential options, average rental rates, lease contract review per W117 if BuildRight is the lessor; (c) employee signs lease; (d) temporary housing support ends; (e) household goods delivered to permanent address | Employee / HR Manager | — | Varies (typically 30-60 days) |
| 7 | **Relocation expense settlement**: within 30 days of relocation completion: (a) employee submits relocation expense report with receipts: transportation, moving costs, temporary housing, house-hunting trip; (b) HR Manager reviews for policy compliance; (c) Finance processes reimbursement through payroll per W74 or separate bank transfer; (d) relocation assistance payment released as agreed (full upon relocation or split 50/50 upon relocation + 6-month retention); (e) system records total relocation cost for transfer analytics | Employee / HR Manager / Finance | HR Manager | 30-60 min per settlement |
| 8 | **Retention and satisfaction follow-up**: at 30, 90, and 180 days post-relocation: (a) HR Manager contacts employee for satisfaction check: housing, community integration, role satisfaction, family adjustment; (b) if employee is struggling: offer additional support (extended housing subsidy, community connection, family support); (c) track relocation success rate: % of relocated employees still with BuildRight at 12 months; (d) feed insights into relocation policy and package optimization | HR Manager | CHRO | 30 min per check-in |

### System Touchpoints

- Employee transfer record per W511
- Location master data per W254
- Corporate housing/billeting management per W441
- Payroll module per W10 for relocation payments and entity change
- Expense management module per W74 for relocation reimbursement
- IT provisioning per W152 for access updates
- Lease management per W117 for housing references
- Budget tracking for relocation cost allocation

### Pain Points / Risks

- **Transfer refusal due to relocation burden**: employees (especially those with families and school-age children) frequently decline transfers that require relocation, limiting BuildRight's ability to deploy talent where needed; mitigated by generous relocation packages and family support
- **Cost-of-living adjustment disputes**: employees transferred from provincial locations to Metro Manila face significantly higher living costs (rent, food, transportation) without commensurate salary adjustment; addressing this requires policy clarity on geographic pay differentials
- **Temporary housing shortage**: company billeting per W441 has limited capacity, especially during new store opening surges per W702 when multiple employees may need temporary housing simultaneously
- **Household goods damage or loss**: moving company liability for damaged or lost items is typically limited; employees may bear unreimbursed losses, creating dissatisfaction at the start of their new assignment
- **Spouse/partner employment disruption**: relocation often disrupts the employee's spouse's employment, creating household income loss and family pressure that contributes to early attrition

### Staffing Implication

HR Manager: ~4-6 hours per relocation for coordination and documentation. At ~30-50 relocations/year, this represents ~120-300 hours/year (~0.1-0.15 FTE). Absorbed within existing HR team. Corporate Housing Coordinator (shared with W441): ~1-2 hours per relocation for billeting arrangement.

### Time Estimate

**Per relocation**: ~8-12 hours HR time over 30-90 days (30 min assessment + 30-60 min package + 15-30 min approval + 2-4 hours logistics + 30-60 min settlement + 90 min follow-up). Employee's personal relocation time varies.

---

## W719. Diversity, Equity & Inclusion (DEI) Program Management

| Field | Detail |
|---|---|
| **Trigger** | Annual DEI program calendar; quarterly DEI metrics review; or specific DEI incident/complaint |
| **Frequency** | Ongoing program with quarterly review cycles |
| **Volume** | 6,715 employees across 5 entities, 200 stores, 4 DCs |
| **Owner** | HR Manager |
| **Participants** | CHRO, Department Heads, DEI Committee, Legal Counsel, External DEI Consultant |

### Background

As a large Philippine employer with 6,715 employees across the archipelago, BuildRight Depot has a responsibility to ensure equitable treatment regardless of gender, age, disability status, indigenous group membership, religion, or sexual orientation. Philippine law (Labor Code, Magna Carta for Women RA 9710, Solo Parents Welfare Act RA 11861, PWD benefits RA 10754, Anti-Age Discrimination in Employment Act RA 10911) mandates specific protections. This workflow manages BuildRight's DEI program including policy enforcement, metrics tracking, training, and compliance with Philippine labor and anti-discrimination laws. It complements existing HR workflows by providing a structured DEI governance framework.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Annual DEI assessment**: Q1 each year, HR Manager conducts DEI assessment: (a) workforce composition analysis: gender distribution by level and department; age distribution; PWD employment rate (DOLE requires companies with 100+ employees to reserve 1% of positions for PWDs); solo parent representation; indigenous group representation; (b) pay equity analysis: compensation comparison by gender within same role/grade; identify unexplained pay gaps; (c) promotion and hiring analysis: diversity in promotions, lateral moves, and new hires; (d) employee engagement analysis: break down W629 engagement scores by demographic group; (e) complaint and grievance analysis: DEI-related complaints from W79 by type and resolution; (f) compare against Philippine labor law requirements and industry benchmarks | HR Manager | CHRO | 2-3 days |
| 2 | **DEI program planning**: based on assessment, HR Manager develops annual DEI action plan: (a) set measurable DEI targets: PWD hiring target (1% minimum per RA 10524), gender balance in management, pay equity gap reduction; (b) identify initiatives: unconscious bias training, PWD workplace accommodation, flexible work arrangements, anti-harassment campaign, cultural sensitivity training; (c) allocate budget for DEI initiatives; (d) assign accountability to department heads for their area targets; (e) present plan to CHRO and CEO for approval | HR Manager | CHRO | 1-2 days |
| 3 | **Policy review and enforcement**: semi-annually: (a) review HR policies for DEI compliance: hiring (W15), promotion (W72), compensation (W10), benefits, disciplinary process (W603); (b) verify compliance with Philippine anti-discrimination laws: RA 10911 (age), RA 9710 (gender), RA 7277 (PWD), RA 8371 (indigenous peoples), RA 10364 (anti-trafficking); (c) update anti-harassment and anti-discrimination policies; (d) ensure grievance process per W79 is accessible and retaliation-free; (e) Legal Counsel review of policy changes per W230 | HR Manager / Legal Counsel | CHRO | 1-2 days |
| 4 | **DEI training delivery**: quarterly, deliver targeted DEI training: (a) all employees: annual anti-sexual harassment refresher (2 hours, mandatory per RA 7877); anti-discrimination awareness (1 hour); PWD sensitivity and accommodation awareness (1 hour); (b) managers and supervisors: unconscious bias training (4 hours); inclusive hiring practices (2 hours); reasonable accommodation for PWD employees (2 hours); (c) HR team: DEI incident investigation protocol (4 hours); pay equity analysis methodology (2 hours); (d) training tracked in employee records per W51 | HR Manager / External DEI Trainer | CHRO | ~8 hours/year per employee for mandatory modules |
| 5 | **PWD workplace accommodation**: when a PWD employee is hired or an existing employee acquires a disability: (a) HR Manager conducts accommodation needs assessment with employee; (b) implement reasonable accommodation per RA 7277: (i) physical accessibility: ramps, modified workstations, accessible restrooms (already covered in W497 PWD accessibility compliance); (ii) assistive technology: screen readers, magnification software, modified keyboards; (iii) schedule accommodation: flexible hours, reduced hours with proportional pay if elected; (iv) job modification: adjust non-essential job functions; (c) track accommodation costs for tax incentive claims (RA 7277 provides tax deductions for accommodation costs); (d) review accommodation effectiveness quarterly with employee | HR Manager / IT | CHRO | Varies per accommodation |
| 6 | **Quarterly DEI metrics review**: HR Manager presents DEI dashboard to CHRO: (a) workforce composition metrics vs. targets; (b) pay equity gap trend; (c) PWD employment rate and accommodation status; (d) DEI training completion rate; (e) DEI-related complaint count and resolution time; (f) hiring and promotion diversity metrics; (g) initiatives completed vs. planned; (h) recommendations for course correction | HR Manager | CHRO | 2-3 hours/quarter |
| 7 | **Annual DEI report**: at year-end, HR Manager prepares annual DEI report: (a) comprehensive workforce composition analysis; (b) year-over-year progress on all DEI metrics; (c) regulatory compliance status: PWD 1% requirement met, anti-harassment training completion rate, equal pay certification; (d) DEI program spend vs. budget; (e) employee feedback and sentiment from W629 engagement survey; (f) action plan for next year; (g) report submitted to CHRO, CEO, and included in ESG reporting per W694 | HR Manager | CHRO | 1-2 days |

### System Touchpoints

- HR analytics module for workforce composition analysis
- Compensation data per W10 for pay equity analysis
- Recruitment data per W15 for hiring diversity tracking
- Employee engagement survey per W629 for DEI sentiment analysis
- Grievance system per W79 for DEI complaint tracking
- Training management per W51 for DEI training completion tracking
- ESG reporting per W694 for annual DEI disclosure
- Payroll module per W10 for accommodation cost tracking and tax incentive documentation

### Pain Points / Risks

- **PWD hiring target achievement**: finding qualified PWD candidates for retail roles (especially physically demanding store positions like stocking and receiving) is challenging; mitigated by partnering with DSWD and PWD organizations, and identifying roles suitable for accommodation (customer service, cashier, administrative)
- **Pay equity analysis complexity**: comparing compensation across 6,715 employees in 5 entities with varying regional wage orders and role-specific allowances requires careful normalization to avoid misleading conclusions
- **Training fatigue**: DEI training competes with operational training (POS, safety, product knowledge) for employee time; store-level employees may view DEI training as lower priority than job skills
- **Cultural sensitivity in Philippine context**: DEI conversations around gender identity and sexual orientation may encounter cultural and religious resistance; program must balance inclusivity with respect for diverse belief systems
- **Measurement challenges**: some DEI metrics (inclusion sentiment, microaggression frequency) are inherently subjective and difficult to quantify objectively

### Staffing Implication

HR Manager: ~10-15 hours/month on DEI program management (assessment, training coordination, metrics review, accommodation management). External DEI Consultant: ~10-15 days/year for training delivery and program evaluation. No incremental internal headcount.

### Time Estimate

**Annual assessment**: 2-3 days. **Program planning**: 1-2 days. **Policy review**: 1-2 days (semi-annual). **Training delivery**: ~8 hours/employee/year (mandatory modules). **Quarterly review**: 2-3 hours. **Annual report**: 1-2 days. **Accommodation management**: varies.

---

## W753. Store-Level Employee Meal Break & Rest Period Scheduling & DOLE Compliance

| Field | Detail |
|---|---|
| **Trigger** | Shift start (W34); mid-shift meal break window |
| **Frequency** | Daily per employee; ~29 employees per store × 2 shifts |
| **Volume** | 200 stores × ~29 employees/day × 1 meal break + 2 rest breaks = ~17,400 break events/day chain-wide |
| **Owner** | Store Manager / Department Supervisor |
| **Participants** | Floor Associates, Department Supervisor, Store Manager, HR (compliance) |

### Background
Philippine Labor Code (Articles 83–85) mandates: (1) 60-minute meal break for employees working 8+ hours, (2) paid rest periods of not less than 5 minutes for every 4 hours of continuous work. DOLE inspections (W505) frequently cite meal break violations. This workflow ensures compliant break scheduling across 200 stores while maintaining customer service coverage.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Break schedule generation — System auto-generates break schedule based on shift roster (W34): staggers breaks to maintain minimum staffing per department; ensures no more than 30% of department staff on break simultaneously | System | — | Automated |
| 2 | Pre-shift break schedule communication — During morning huddle (W739), Store Manager confirms break schedule; Department Supervisors receive their zone's break schedule on handheld device | Store Manager | Store Manager | 2 min |
| 3 | Meal break execution — Employee clocks out for 60-minute meal break at scheduled time; system monitors break start time; employee must clock back in within 65 minutes (5-minute grace period) | Employee | Department Supervisor | 60 min |
| 4 | Rest break execution — Two paid 5-minute rest breaks per 8-hour shift; employee takes break at designated time; no clock-out required (paid break); Department Supervisor tracks completion | Employee | Department Supervisor | 5 min each |
| 5 | Break coverage verification — Department Supervisor confirms replacement coverage before releasing employee for break; if coverage unavailable, reschedules break within compliance window | Department Supervisor | Department Supervisor | 2 min |
| 6 | Compliance monitoring — System flags: (a) missed meal break (no clock-out within 5 hours of shift start), (b) shortened meal break (< 45 minutes), (c) late meal break (> 6 hours after shift start), (d) missed rest break | System | — | Automated |
| 7 | Non-compliance escalation — System sends compliance alert to Store Manager for any flagged violations; Store Manager investigates and documents corrective action; repeat violations escalated to HR | Store Manager | HR | 10 min |
| 8 | Monthly compliance report — System generates monthly break compliance report per store: compliance rate, violation count by type, repeat offenders; HR reviews for DOLE inspection preparation (W505) | System / HR | HR | Automated + 30 min review |

### System Touchpoints
- W34 shift scheduling integration — break schedule auto-generation from shift roster
- Time & attendance system — meal break clock-out/clock-in tracking
- Compliance monitoring dashboard — real-time break status per employee per store
- DOLE inspection readiness report (W505) — break compliance documentation
- W10 payroll integration — break violation deductions (if applicable) and overtime triggers
- W561 attendance exception management — break violation as exception type
- W739 daily huddle — break schedule communication channel

### Pain Points / Risks
- Peak hour coverage — during payday weekends and Ber months, maintaining break compliance while serving high customer volume is extremely difficult
- Cashier break challenge — with only 3 POS terminals per store, cashier breaks directly impact checkout capacity (W526 queue management)
- "Working through breaks" culture — employees may skip breaks to complete tasks or earn more; this creates DOLE liability for the company even if voluntary
- Seasonal worker compliance — temporary workers (W555) unfamiliar with break schedules; abbreviated onboarding may not adequately cover break rights
- DOLE inspection exposure — break violations are among the top 3 DOLE findings in retail inspections; each violation carries penalties

### Time Estimate
Break schedule generation: automated. Daily compliance monitoring: automated. Weekly exception review: 15 min per store. Monthly report review: 30 min per store. Total monthly per store: ~2 hours.

### Staffing Implication
No incremental headcount. Break scheduling managed by Department Supervisors within existing duties. Compliance monitoring automated. 200 stores × ~2 hours/month compliance management = ~400 hours/month absorbed by Store Managers and HR.

---

## W754. Store-Level New Hire First-30-Day Performance Check-In & Early Intervention

| Field | Detail |
|---|---|
| **Trigger** | New hire completes 7, 15, and 30 days of employment |
| **Frequency** | 3 check-ins per new hire within first 30 days |
| **Volume** | ~200 new hires chain-wide at any given time (based on annual turnover ~40% × 6,715 employees / 12 months) |
| **Owner** | Department Supervisor |
| **Participants** | New Hire, Department Supervisor, Store Manager, HR (W15 onboarding) |

### Background
Retail industry turnover is highest in the first 90 days. BuildRight Depot's structured onboarding (W15) and buddy system (W609) provide initial support, but without formal performance check-ins during the critical first 30 days, early performance issues go undetected until they become termination cases. This workflow creates structured touchpoints that identify at-risk employees early, provide targeted support, and improve first-year retention.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Day-7 check-in — Department Supervisor conducts 15-minute structured check-in: (a) comfort with POS systems, (b) product knowledge assessment for assigned department, (c) integration with team, (d) any concerns or questions; Supervisor rates confidence level (1–5) | Department Supervisor | Store Manager | 15 min |
| 2 | Day-7 intervention trigger — If confidence rating ≤ 2 in any area: Supervisor creates targeted support plan: additional shadow shifts with buddy (W609), focused product training (W51), or schedule adjustment | Department Supervisor | Store Manager | 15 min |
| 3 | Day-15 check-in — Department Supervisor conducts 20-minute check-in: (a) sales performance vs. peer benchmark, (b) customer interaction quality, (c) attendance and punctuality record (W561), (d) progress on Day-7 support plan (if any); rates overall progress (On Track / Needs Support / At Risk) | Department Supervisor | Store Manager | 20 min |
| 4 | Day-15 intervention — If "At Risk": Store Manager conducts 1-on-1 with new hire; develops Performance Improvement Plan (PIP) with specific, measurable goals for next 15 days; HR notified | Store Manager | HR | 30 min |
| 5 | Day-30 check-in — Store Manager conducts 30-minute comprehensive review: (a) performance metrics vs. department standards, (b) cross-training progress (W567), (c) cultural fit and teamwork, (d) career interests; rates: Proceed to Regular / Extend Probation / Separate | Store Manager | Store Manager | 30 min |
| 6 | Probation completion recommendation — Store Manager records recommendation in system with supporting evidence; HR reviews for DOLE compliance (probationary employment rules per Labor Code) | Store Manager | HR | 15 min |
| 7 | Data analytics — System aggregates first-30-day outcomes: pass rate by department, by store, by hiring source, by training approach; HR uses data to optimize W15 onboarding and W34 scheduling practices | System / HR | HR | Automated + 1 hour/month |
| 8 | Exit interview trigger — If separation during first 30 days: mandatory early-exit interview (distinct from W628) focused on onboarding experience; data feeds W15 onboarding improvement | HR | Store Manager | 30 min |

### System Touchpoints
- New hire tracking module with Day-7/15/30 check-in calendar
- Structured check-in forms with rating scales and comment fields
- W609 buddy system integration — buddy feedback on new hire progress
- W15 onboarding module — check-in data feeds onboarding effectiveness
- W567 cross-training integration — skill assessment tracking
- W522 cashier performance audit — performance data source for cashier new hires
- W34 scheduling — probationary status flag for schedule considerations
- HR analytics dashboard — first-30-day outcomes and trends

### Pain Points / Risks
- Supervisor time investment — each new hire requires ~65 minutes of structured check-ins within first 30 days, adding to supervisor workload during high-turnover periods
- Subjective ratings — without calibrated rating criteria, supervisors may rate all new hires "On Track" to avoid difficult conversations, undermining early intervention purpose
- Legal risk — documented "At Risk" ratings during probation create paper trail that must be handled carefully per DOLE probationary employment rules; poor documentation can undermine lawful termination
- Check-in compliance — busy supervisors may skip or delay check-ins, especially during peak seasons; system enforcement (mandatory check-in before timesheet approval) may be needed

### Time Estimate
Day-7 check-in: 15 min. Day-15 check-in: 20 min. Day-30 check-in: 30 min. Total per new hire: ~65 minutes of supervisor time + 15 minutes Store Manager + 15 minutes HR review = ~95 minutes total.

### Staffing Implication
No incremental headcount. Check-ins absorbed by Department Supervisors and Store Managers. ~200 active new hires at any time × 65 min = ~217 supervisor-hours ongoing. HR analytics: 1 hour/month.

---

## W755. Store-Level Employee Internal Theft Prevention Awareness & Compliance Daily Operations

| Field | Detail |
|---|---|
| **Trigger** | Daily LP operations; monthly awareness topic rotation; new hire onboarding |
| **Frequency** | Daily awareness operations; monthly topic focus |
| **Volume** | 200 stores × daily awareness touchpoints |
| **Owner** | Store Manager (Operations); LP Analyst (Oversight) |
| **Participants** | Store Manager, Floor Associates, LP Team, HR |

### Background
Internal theft (employee theft) accounts for a significant portion of retail shrinkage — industry benchmarks suggest 30–40% of total shrinkage. While W710 addresses LP analytics and W562 covers LP daily routines, this workflow specifically addresses the daily operational prevention and awareness activities that create a culture of honesty and deter internal theft across 200 stores.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Daily awareness touchpoint — During morning huddle (W739), Store Manager includes one internal theft prevention tip or reminder: reporting procedures, policy highlights, consequence reminders, or recent case studies (anonymized) | Store Manager | — | 1 min |
| 2 | Cash handling compliance verification — Daily: Department Supervisor verifies cash handling procedures are followed: (a) only one cashier per drawer (W517), (b) no unauthorized voids (W529), (c) personal purchases processed through separate transaction (W205), (d) no personal bags at register | Department Supervisor | Store Manager | 10 min |
| 3 | Stockroom access monitoring — Daily: Stockroom access log reviewed for unusual patterns: (a) access outside scheduled shift, (b) extended dwell time, (c) access by non-authorized personnel | LP Analyst | Store Manager | 10 min |
| 4 | Employee purchase verification — System flags employee purchases (W205) for monthly review: (a) purchases exceeding monthly limit, (b) purchases of items outside normal pattern, (c) purchases during shift with unusual timing | System / LP Analyst | — | Automated + 15 min/week |
| 5 | Monthly awareness campaign — LP team designs monthly awareness topic: poster for break room, email to all store associates, quiz for completion; topics rotate through: refund fraud, sweethearting, coupon abuse, merchandise concealment, time theft | LP Team | HR | 4 hours/month design + 5 min/associate for quiz |
| 6 | Anonymous reporting promotion — Monthly: Store Manager reminds associates of anonymous reporting channel (W79 grievance/whistleblower); ensures reporting posters are visible in break room | Store Manager | — | 2 min |
| 7 | Monthly compliance scorecard — LP generates monthly internal controls compliance scorecard per store: cash handling compliance rate, stockroom access anomalies, employee purchase flags, awareness quiz completion rate | System / LP Analyst | — | Automated |
| 8 | Quarterly LP meeting — Quarterly: LP Manager presents internal theft trends, case studies, and prevention strategy updates to Store Managers at regional meeting | LP Manager | VP Store Ops | 2 hours/quarter |

### System Touchpoints
- W205 employee purchase program — transaction monitoring and flagging
- W517 cashier shift handover — single-drawer compliance tracking
- W529 void & refund authorization — unauthorized void detection
- W742 access card management — stockroom access log analysis
- W79 grievance/whistleblower — anonymous reporting channel
- W710 LP analytics — internal theft pattern detection
- W562 LP daily routine — daily LP activity integration
- Awareness training module (LMS) — monthly quiz delivery and completion tracking

### Pain Points / Risks
- "Trust" culture resistance — employees may perceive prevention activities as lack of trust, affecting morale; communication must emphasize protection of honest employees
- Sweethearting detection difficulty — cashiers giving unauthorized discounts to friends/family is hard to detect without transaction analytics (W710)
- Time theft — buddy punching (clocking in for absent coworker) requires biometric controls (W561 attendance management)
- Seasonal worker vulnerability — temporary workers (W555) with less organizational commitment are statistically more likely to commit internal theft
- Whistleblower fear — despite anonymous channels, employees may fear retaliation; robust non-retaliation policy enforcement is essential

### Time Estimate
Daily: awareness touchpoint 1 min + cash handling verification 10 min + stockroom review 10 min = 21 min/day. Monthly: awareness campaign 5 min/associate × 29 = ~2.5 hours + LP design 4 hours. Quarterly: LP meeting 2 hours. Total monthly per store: ~15 hours.

### Staffing Implication
No incremental headcount. Prevention activities absorbed by Store Manager, Department Supervisors, and LP team. LP team: 1 LP analyst per region (~10–12 LP analysts chain-wide) designs monthly campaigns and reviews compliance scorecards.

---

## W777. Employee Leave Balance Management & Annual Leave Carry-Forward Processing

| Field | Detail |
|---|---|
| **Trigger** | Semi-monthly payroll cycle; annual leave year-end processing |
| **Frequency** | Continuous (leave requests daily); monthly balance reconciliation; annual carry-forward (December) |
| **Volume** | 6,715 employees × ~4-6 leave requests/year = ~27,000-40,000 leave transactions/year |
| **Owner** | HR Business Partner |
| **Participants** | Employee, Direct Supervisor, HR Business Partner, Payroll Accountant |

### Background
Philippine labor law mandates specific leave entitlements: Service Incentive Leave (SIL) of 5 days per year after 12 months of service per Article 95 of the Labor Code, plus company-provided Vacation Leave (VL) and Sick Leave (SL) above statutory minimums. BuildRight Depot provides 15 VL days and 15 SL days per year (in addition to special holidays and maternity/paternity leave per HR-007). Managing leave balances, approvals, accruals, and year-end carry-forward for 6,715 employees across 5 entities requires systematic workflow management to ensure DOLE compliance, payroll accuracy, and employee satisfaction.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Leave request submission**: Employee submits leave request via self-service portal (HR-008) or mobile app: (a) leave type (VL, SL, SIL, maternity, paternity, solo parent, bereavement, others per HR-007), (b) start and end dates, (c) reason (confidential for SL), (d) contact during leave | Employee | — | 5 min |
| 2 | **Balance and eligibility check**: System validates: (a) leave type eligibility (SL requires medical certificate for > 2 days per policy), (b) available balance, (c) probation period completed (VL not available during 6-month probation), (d) no conflicting approved leave for same dates, (e) department coverage verification (minimum staffing met per W34 scheduling) | System | — | Instant |
| 3 | **Supervisor approval workflow**: Direct Supervisor receives notification: (a) reviews request against department schedule per W34, (b) approves, modifies dates, or denies with reason, (c) for SL > 3 days: requires supporting medical documentation upload, (d) system enforces approval SLA: 24 hours for standard, 4 hours for same-day emergency SL | Supervisor | — | 5 min |
| 4 | **Payroll integration**: Approved leave feeds to payroll per W10: (a) paid leave (VL, SL within balance): regular daily rate, (b) unpaid leave (beyond balance or LWOP): daily rate deduction per HR-010, (c) half-day SL: proportional deduction, (d) leave premium for regular holidays during VL period per HR-011 | System | Payroll Accountant | Automated |
| 5 | **Monthly leave balance reconciliation**: HR Business Partner reviews: (a) leave accrual accuracy (1.25 days/month VL, 1.25 days/month SL), (b) negative leave balance flags (employee used more than accrued — requires recovery plan), (c) leave abuse patterns (> 15 SL days/year, frequent Monday/Friday SL), (d) department leave utilization rates (target: 70-80% VL utilization for work-life balance) | HR BP | HR Manager | 2 hours/month |
| 6 | **Annual carry-forward processing (December)**: System performs year-end leave processing: (a) VL carry-forward: maximum 10 days (company policy — excess forfeited per policy communicated at hire), (b) SL carry-forward: up to 15 days (accumulates as emergency buffer), (c) SIL: statutory 5 days non-cumulative (use or convert to cash per DOLE rules), (d) generate employee leave balance statement for next year, (e) conversion of unused VL to cash for resigning/retiring employees per W643 final pay | System | HR Manager | Automated + 4 hours review |
| 7 | **Annual leave encashment**: For employees who qualify per policy: (a) excess VL beyond 10-day carry-forward converted to cash at daily rate, (b) SIL unused days converted to cash per Article 95 Labor Code, (c) encashment processed through December payroll per W10, (d) BIR withholding tax applied per TRAIN law graduated table | Payroll Accountant | HR Manager | 2 hours/year |

### System Touchpoints

- HR leave management module — request, approval, balance tracking, and accrual engine
- W10 payroll processing — leave deduction and premium calculation
- W34 shift scheduling — leave impact on department staffing
- HR-007 leave management — leave type configuration and policy rules
- HR-008 employee self-service — leave request and balance inquiry portal
- HR-010 overtime calculation — leave interaction with overtime eligibility
- HR-011 holiday pay — holiday pay during leave periods
- W643 final pay computation — unused leave encashment at separation
- W561 attendance exception management — leave integration with attendance tracking

### Pain Points / Risks

- Leave abuse — patterns of Monday/Friday SL, frequent short absences, or exceeding entitlements; monitoring via monthly reconciliation and supervisor awareness training
- Negative leave balances — employees who use more leave than accrued create recovery complexity; policy must address deductions from final pay per W643
- Carry-forward fairness — employees who cannot take leave due to workload feel penalized by forfeiture; managers must ensure equitable leave opportunities
- Multi-entity complexity — leave policies may differ across 5 entities (e.g., Holdings vs. Depot Inc.); system must enforce entity-specific rules
- Peak period coverage — multiple employees requesting same dates (especially holiday periods, payday weekends per W578); scheduling conflict resolution requires manager judgment

### Time Estimate

Daily: leave request processing is largely automated. Monthly reconciliation: 2 hours. Annual carry-forward: 4 hours review + 2 hours encashment = 6 hours. Per-entity: multiply by 5 for annual processing.

### Staffing Implication

Absorbed within existing HR Business Partner and Payroll Accountant roles. Monthly: ~2 hours. Annual: ~6 hours concentrated in December. No incremental headcount.

---

## W778. Employee Benefits Annual Open Enrollment & Plan Selection Management

| Field | Detail |
|---|---|
| **Trigger** | Annual benefits enrollment period (typically November for January 1 effective date) |
| **Frequency** | Annual open enrollment; ad-hoc for qualifying life events |
| **Volume** | 6,715 employees × annual enrollment + ~200 qualifying life event changes/year |
| **Owner** | HR Benefits Administrator |
| **Participants** | HR Benefits Admin, Employee, HMO Provider, Payroll Accountant, HR Manager |

### Background
BuildRight Depot offers employee benefits beyond statutory requirements including HMO coverage per HR-032, life insurance, and optional supplementary benefits. Annual open enrollment allows employees to review, change, or add dependents to their coverage. While W642 covers ongoing HMO administration, this workflow manages the concentrated annual enrollment period — the logistics of communicating options, collecting elections, validating dependent documentation, and transmitting enrollment data to benefit providers.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Pre-enrollment preparation (T-4 weeks)**: HR Benefits Admin: (a) reviews current plan utilization and cost data per HR-032, (b) evaluates provider options and premium rates for next year, (c) negotiates renewal rates with HMO providers, (d) prepares enrollment communication package: benefit summary, premium comparison, plan changes, and FAQ | HR Benefits Admin | HR Manager | 2-3 days |
| 2 | **Enrollment communication launch (T-3 weeks)**: Distribute enrollment materials: (a) company-wide email per W716 internal communications, (b) digital signage per W504 in stores and DCs, (c) self-service portal enrollment guide, (d) FAQ document and hotline number, (e) mandatory enrollment deadline (2-week window) | HR Benefits Admin | — | 4 hours |
| 3 | **Employee enrollment election**: Employee reviews and submits elections via self-service portal: (a) plan tier selection (Employee Only, Employee + Spouse, Employee + Family), (b) add/remove dependents with supporting documents (marriage certificate, birth certificates), (c) voluntary supplementary coverage opt-in/opt-out, (d) beneficiary designation for life insurance | Employee | — | 15-30 min |
| 4 | **Dependent documentation verification**: HR Benefits Admin verifies: (a) marriage certificate for spouse enrollment, (b) birth certificates for dependent children, (c) maximum dependents per plan tier, (d) age eligibility (children up to 21 years, or 25 if full-time student per HMO terms), (e) requests additional documentation if incomplete | HR Benefits Admin | — | 10 min/employee with dependents |
| 5 | **Payroll deduction configuration**: For each election: system configures semi-monthly payroll deduction: (a) employee share of HMO premium by tier, (b) voluntary coverage premium, (c) pre-tax vs. post-tax treatment per BIR rules, (d) effective date: January 1 (or first payroll of new year) | System | Payroll Accountant | Automated |
| 6 | **Provider enrollment transmission**: HR Benefits Admin transmits enrollment data to providers: (a) HMO provider enrollment file (new enrollees, plan changes, terminations), (b) life insurance enrollment file, (c) supplementary benefit providers, (d) reconcile transmission acknowledgment with system records | HR Benefits Admin | — | 4 hours |
| 7 | **Qualifying life event processing (ad-hoc)**: Throughout the year, process mid-year changes triggered by: (a) marriage, (b) birth/adoption, (c) divorce/legal separation, (d) spouse job loss, (e) dependent aging out; employee has 30 days from event to request change; same verification and transmission process | HR Benefits Admin | — | 20 min/event |
| 8 | **Post-enrollment audit**: After enrollment close: (a) verify all active employees made an election or defaulted to prior year coverage, (b) reconcile total enrollment vs. employee master per W292, (c) reconcile total premiums vs. payroll deductions, (d) report enrollment analytics (tier distribution, dependent count, cost per employee) | HR Benefits Admin | HR Manager | 4 hours |

### System Touchpoints

- HR benefits module — enrollment election, dependent management, and plan configuration
- W642 HMO & private benefits administration — ongoing HMO operations
- W10 payroll processing — premium deduction configuration
- HR-008 employee self-service — enrollment portal
- W716 internal communications — enrollment campaign distribution
- W504 digital signage — in-store enrollment communication
- W292 employee master data — employee and dependent data verification
- W43 employee separation — benefit termination at separation

### Pain Points / Risks

- Enrollment deadline non-compliance — employees who miss enrollment window are locked into prior year coverage (or no coverage for new hires); exceptions require HR Manager approval
- Dependent documentation fraud — falsified documents for non-eligible dependents increase claims cost; verification essential
- Premium cost escalation — annual HMO premium increases (typically 10-20% in Philippines) may force plan design changes that reduce coverage or increase employee contributions; sensitive employee relations issue
- Data transmission errors — incorrect enrollment data sent to providers causes claim denials for employees; reconciliation critical
- Multi-provider coordination — different enrollment formats and deadlines for HMO, life insurance, and supplementary providers create administrative complexity

### Time Estimate

Annual enrollment period: Preparation (2-3 days) + communication (4 hours) + enrollment processing (~40 hours for 6,715 employees) + verification (~20 hours) + transmission (4 hours) + audit (4 hours) = ~80-90 hours concentrated in 4-6 weeks. Ad-hoc qualifying events: ~20 min each × 200/year = ~67 hours distributed throughout year.

### Staffing Implication

Absorbed within existing HR Benefits Admin role. Enrollment period requires full-time dedication for 2-3 weeks. No incremental headcount.

---

## W779. Store-Level Employee Injury Incident Reporting & Workers' Compensation Claim Processing

| Field | Detail |
|---|---|
| **Trigger** | Employee work-related injury or illness |
| **Frequency** | Ad-hoc; ~5-10 workplace injuries per month chain-wide |
| **Volume** | ~60-120 reported workplace injuries/year across 200 stores, 4 DCs, and HQ |
| **Owner** | Store Manager |
| **Participants** | Store Manager, Injured Employee, HR Business Partner, Safety Officer, SSS/EC Claims, DOLE |

### Background
BuildRight Depot's operations involve physical risks: heavy lifting (cement bags, lumber), forklift operations in DCs, ladder use for high shelving, and equipment operation (cutting, mixing). When employees are injured on the job, DOLE requires incident reporting, and the employee is entitled to SSS Employees' Compensation (EC) benefits per PD 626. While W140 covers OHS incident management broadly and W501 covers first aid response, this workflow specifically addresses the employee injury administrative process — from incident documentation through workers' compensation claim filing, modified duty management, and return-to-work processing.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Immediate incident response**: (a) first aid administered per W501, (b) if serious: emergency medical transport coordinated, (c) scene secured per W140, (d) Store Manager notified immediately | First Aider / Supervisor | Store Manager | 10-30 min |
| 2 | **Incident documentation (within 4 hours)**: Store Manager completes incident report: (a) date, time, location of incident, (b) employee details and department, (c) description of what happened, (d) witnesses and statements, (e) injury description and body part affected, (f) immediate cause and contributing factors, (g) photos of scene and equipment involved, (h) first aid or medical treatment provided | Store Manager | Safety Officer | 30-60 min |
| 3 | **Medical treatment and documentation**: Employee seeks medical attention: (a) if minor: company-designated clinic or HMO provider per W642, (b) if serious: nearest hospital emergency room, (c) all medical certificates, treatment records, and receipts collected for SSS EC claim, (d) Store Manager ensures "off-duty" status recorded in time & attendance per W561 | Employee / Store Manager | HR BP | 2-4 hours |
| 4 | **DOLE incident reporting**: For serious incidents (fatality, serious injury requiring > 7 days absence, or mass casualty): (a) HR BP submits DOLE report within 24 hours per DOLE Department Order 198, (b) report includes incident details, causes, and corrective actions taken, (c) DOLE may conduct investigation — coordinate per W505 labor inspection protocol | HR BP | HR Manager | 2-4 hours |
| 5 | **SSS EC claim filing (within 30 days)**: HR BP files SSS Employees' Compensation claim: (a) SSS EC claim form (B-300), (b) employer's incident report, (c) medical certificate from attending physician, (d) proof of SSS contributions, (e) salary payment records for disability benefit computation; SSS processes: (i) temporary total disability (TTD) — daily allowance, (ii) permanent partial/total disability — lump sum or pension, (iii) medical reimbursement | HR BP | — | 4-6 hours/claim |
| 6 | **Modified duty management**: For employees cleared for light duty: (a) Safety Officer and HR BP review medical restrictions, (b) assign modified duties within restrictions (e.g., cash desk duty for employee with lifting restriction), (c) coordinate with W34 scheduling, (d) monitor recovery progress with medical clearance updates | HR BP | Store Manager | 1-2 hours/week during recovery |
| 7 | **Return-to-work processing**: When employee receives full medical clearance: (a) HR BP processes return-to-work documentation, (b) fitness-for-work certification filed, (c) employee reinstated to full duties, (d) any workplace accommodation made permanent if needed per W497 accessibility standards, (e) incident closed in OHS system | HR BP | Store Manager | 1 hour |
| 8 | **Incident investigation and corrective action**: Safety Officer investigates root cause: (a) 5-Why analysis, (b) equipment inspection per W579, (c) procedure review, (d) corrective action implementation (e.g., additional training per W655, equipment replacement, PPE upgrade per W172), (e) corrective action tracked to completion per W140 | Safety Officer | HR Manager | 4-8 hours |
| 9 | **Monthly injury analytics**: HR Manager reports: (a) injury frequency rate (target: < 2.0 per 200,000 hours worked), (b) lost-time injury rate, (c) injury type and cause distribution, (d) average days lost per injury, (e) claim settlement rate and amount, (f) corrective action completion rate | HR Manager | COO | 2 hours/month |

### System Touchpoints

- OHS incident management module — incident reporting and tracking per W140
- W501 first aid & medical emergency — immediate response integration
- W140 OHS incident management — incident investigation and corrective action
- W655 safety training & certification — training remediation trigger
- W579 daily equipment safety check — equipment-related incident investigation
- W172 PPE & uniform lifecycle — PPE adequacy review
- W561 attendance exception management — injury-related absence tracking
- W34 shift scheduling — modified duty assignment
- W10 payroll processing — salary continuation during recovery
- W251 statutory benefits — SSS EC claim tracking
- W642 HMO administration — medical treatment coordination
- W505 DOLE labor inspection — regulatory reporting integration

### Pain Points / Risks

- Underreporting — employees may not report minor injuries due to fear of disciplinary action or perceived weakness; safety culture training per W720 daily briefing is preventive
- SSS EC claim delays — Philippine SSS processing times for EC claims can be 3-6 months; employees may face financial hardship during recovery
- Modified duty availability — not all store roles can accommodate light duty restrictions; HR BP must work creatively with Store Manager on task reassignment
- DOLE investigation — serious incidents trigger DOLE investigation with potential fines and mandatory corrective actions; thorough documentation is legal defense
- Litigation risk — employees may file labor complaints per W79 grievance if they feel injury was caused by employer negligence (e.g., lack of PPE, faulty equipment); W655 certification tracking mitigates

### Time Estimate

Per incident: Immediate response (10-30 min) + documentation (30-60 min) + medical (2-4 hours) + DOLE reporting if serious (2-4 hours) + SSS EC filing (4-6 hours) + investigation (4-8 hours) = 12-24 hours total spread over weeks. Monthly analytics: 2 hours.

### Staffing Implication

Absorbed within existing Store Manager and HR BP roles. Per incident: ~12-24 hours of combined management time. Safety Officer: 4-8 hours per investigation. No incremental headcount.

---

## W780. Store-Level Employee Uniform & PPE Periodic Issuance & Replacement Processing

| Field | Detail |
|---|---|
| **Trigger** | Scheduled periodic issuance (quarterly for uniforms, as-needed for PPE); new hire onboarding per W15; worn-out replacement request |
| **Frequency** | Quarterly scheduled issuance; daily ad-hoc replacement |
| **Volume** | 200 stores × 29 employees × 4 uniform sets/year = ~23,200 uniform sets/year; ~5-10 PPE replacement requests per store per month |
| **Owner** | Store Manager |
| **Participants** | Store Manager, Department Supervisor, Employee, Procurement (W172) |

### Background
BuildRight Depot provides branded uniforms (polo shirts, slacks/jeans, safety shoes) and Personal Protective Equipment (hard hats, safety goggles, gloves, masks, back support belts) per DOLE requirements and corporate safety policy per W172. While W172 covers PPE and uniform lifecycle at the governance level, this workflow manages the store-level operational process — the periodic issuance of uniform sets, replacement of worn-out items, and ensuring all employees have appropriate PPE for their assigned tasks. With 5,800 store-level employees across 200 stores, uniform and PPE management is a daily operational concern.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **New hire uniform & PPE issuance**: At onboarding per W15: (a) Store Manager issues 2 sets of uniform (polo shirt + company ID), (b) assigns safety shoes (steel-toe for receiving/yard staff, non-slip for cashiers), (c) issues role-specific PPE per W655 certification matrix: hard hat (yard/receiving), safety goggles (cutting/chemical areas), gloves (receiving/lumber), high-visibility vest (yard), (d) employee signs receipt in uniform/PPE register | Store Manager | — | 15 min/new hire |
| 2 | **Quarterly uniform issuance**: Every quarter: (a) system generates uniform replacement schedule based on issuance date, (b) Store Manager distributes 2 new uniform sets per employee, (c) old uniforms collected for disposal or donation per W502 waste management, (d) employee signs receipt | Store Manager | — | 5 min/employee × 29 = ~2.5 hours/quarter |
| 3 | **PPE condition assessment**: Department Supervisors continuously monitor PPE condition during daily operations: (a) gloves — wear/tear check (replace when holes or loss of grip), (b) safety goggles — scratch/crack check, (c) hard hats — impact/crack check (replace after any significant impact), (d) safety shoes — sole integrity and steel toe exposure, (e) back support belts — elasticity loss | Dept Supervisor | Store Manager | 5 min/employee/week |
| 4 | **PPE replacement request**: Employee or Supervisor requests PPE replacement: (a) submit request via mobile app or to Store Manager, (b) include reason (worn out, damaged, lost — lost items may require incident report per W779), (c) Store Manager approves standard replacements; Department Supervisor approves within quota | Employee / Supervisor | Store Manager | 5 min |
| 5 | **PPE inventory management**: Store Manager maintains PPE inventory: (a) stock levels by type and size, (b) reorder point triggers per W312 replenishment parameters, (c) emergency PPE availability (at minimum 5 sets of each type per store), (d) quarterly PPE inventory count and replenishment order | Store Manager | — | 30 min/week |
| 6 | **Employee separation collection**: At separation per W43: (a) collect all company-issued uniforms, (b) collect all PPE items, (c) verify against original issuance receipt, (d) missing items may be deducted from final pay per W643 within DOLE limits, (e) collected items assessed for reuse or disposal per W502 | Store Manager | — | 10 min/separation |
| 7 | **Monthly PPE compliance report**: Store Manager reports: (a) PPE issuance compliance rate per role (target: 100%), (b) PPE replacement frequency by type (excessive replacement may indicate misuse or quality issue), (c) PPE inventory levels, (d) uniform compliance spot-check results (target: 100% in proper uniform during business hours) | Store Manager | — | 15 min/month |

### System Touchpoints

- Uniform/PPE issuance module — tracking, scheduling, and receipt management
- W172 PPE & uniform lifecycle — governance and policy management
- W655 safety training & certification — role-based PPE requirement matrix
- W15 recruitment & onboarding — new hire uniform/PPE issuance trigger
- W43 employee separation — collection and reconciliation at separation
- W643 final pay computation — missing item deduction calculation
- W502 non-hazardous waste management — uniform/PPE disposal
- W312 replenishment parameters — PPE inventory reorder points
- W779 employee injury incident — PPE-related injury investigation

### Pain Points / Risks

- Uniform compliance — employees not wearing proper uniform during business hours impacts brand image; Department Supervisor spot-checks essential
- PPE non-compliance — employees skipping PPE for convenience (e.g., not wearing gloves during receiving) creates safety risk and DOLE violation; zero-tolerance enforcement per W720 daily safety briefing
- PPE quality — cheap PPE fails faster, requiring more frequent replacement and higher total cost; procurement per W172 must balance cost and durability
- Sizing issues — incorrect PPE sizing (too large gloves, tight shoes) reduces protection effectiveness; exchange process must be responsive
- Theft and loss — company-issued items may be taken home or lost; replacement policy must distinguish between normal wear and negligence

### Time Estimate

New hire: 15 min. Quarterly issuance: ~2.5 hours per store. PPE condition monitoring: integrated into daily operations. Inventory management: 30 min/week. Total per store: ~5-6 hours/quarter concentrated + 30 min/week ongoing.

### Staffing Implication

Absorbed within existing Store Manager and Department Supervisor duties. Quarterly concentrated effort: ~2.5 hours. Weekly ongoing: ~30 min. No incremental headcount.

---

## W815. Employee Business Travel Request, Approval & Expense Management

| Field | Detail |
|---|---|
| **Trigger** | Employee needs to travel for business purposes (store visits, vendor meetings, DC audits, training, conferences) |
| **Frequency** | Daily; ~50-80 travel requests per month chain-wide |
| **Volume** | ~50-80 trips/month: HQ-to-store visits (40%), DC audits/visits (20%), vendor/supplier meetings (15%), training/conferences (15%), cross-site project work (10%) |
| **Owner** | HR Administrator |
| **Participants** | Employee, Department Supervisor/Manager, HR Administrator, Finance Analyst, Travel Coordinator |

### Background

With 200 stores across Luzon, Visayas, and Mindanao, plus 4 DCs and HQ in Davao City, business travel is routine for BuildRight Depot. Store Operations regional managers travel weekly to visit stores in their clusters; merchandising buyers travel to Manila, Cebu, and international destinations for vendor meetings; IT staff travel to stores for system deployments and POS upgrades; internal audit staff travel for store-level compliance audits. W74 covers expense reimbursement but only after expenses are incurred — it does not address the pre-travel approval, booking coordination, travel policy compliance, or per diem management aspects. This workflow covers the full travel lifecycle from request to settlement. Philippine business travel involves inter-island flights via Philippine Airlines, Cebu Pacific, and AirAsia, hotel bookings in major cities (Manila, Cebu, Davao, Iloilo, Cagayan de Oro), and ground transportation including Grab, rental vehicles, and company service vehicles. The travel policy must comply with BIR deductible expense requirements — official receipts (ORs) from BIR-registered establishments are mandatory for expense claims, and a Travel Order document is required for tax-deductible business travel per BIR regulations. With approximately 600-960 business trips per year across the organization, structured travel management delivers significant cost savings through corporate airline rates, hotel chain agreements, and policy compliance enforcement.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Employee submits travel request via HR self-service portal**: Employee completes travel request form including: (a) destination (store number, DC, vendor location, conference venue), (b) purpose (store visit, vendor meeting, DC audit, training, conference, project work), (c) travel dates and preferred times, (d) estimated total cost broken down by transport, accommodation, meals, and other, (e) requested transport mode (economy air, premium economy, ferry/bus for inter-island, company vehicle, Grab/rental), (f) preferred hotel or accommodation type, (g) justification linking travel to business objective or project per W128 | Employee | — | 15 min |
| 2 | **System performs automated travel policy check**: ERP validates request against travel policy matrix: (a) budget tier by employee level (rank-and-file: PHP 3,000/day max including accommodation; supervisors: PHP 5,000/day; managers: PHP 7,000/day; VP and above: PHP 12,000/day), (b) transport class eligibility (economy for all domestic unless >4 hour flight for managers+), (c) required approval level based on estimated cost (< PHP 20K: Department Manager; PHP 20K-50K: Department Manager + HR Admin; > PHP 50K: VP approval required), (d) duplicate trip detection (flag if same destination within 2 weeks), (e) blackout date check (typhoon season travel advisories, company holiday periods) | System | HR Administrator | Automated (instant) |
| 3 | **Department Manager reviews and approves/rejects**: Manager receives notification in workflow inbox: (a) reviews business justification, (b) confirms travel necessity and timing, (c) verifies budget availability in department cost center, (d) approves, rejects (with reason), or returns for modification; if estimated cost exceeds PHP 50K, system routes to VP for secondary approval after Manager approval | Dept Manager | VP (if > PHP 50K) | 4-8 hours (SLA) |
| 4 | **Travel Coordinator or employee books flights and hotel**: Upon approval: (a) Travel Coordinator books flights using corporate accounts with PAL, Cebu Pacific, AirAsia (negotiated corporate rates: 10-20% discount), (b) books hotel from approved hotel list (BIR-registered establishments with corporate rates: Astoria, Dusit, Seda, Park Inn by Radisson, Go Hotels), (c) arranges ground transportation if needed (Grab for Business account, rental car, or company vehicle request), (d) system generates Travel Order document with approved itinerary, budget, and authorization — required by BIR for tax-deductible expense substantiation | Travel Coordinator / Employee | HR Administrator | 30 min |
| 5 | **System creates travel advance if requested**: For trips exceeding PHP 10K estimated cost: (a) system calculates per diem advance (PHP 1,500/day domestic standard for meals and incidentals + accommodation budget based on approved hotel rate), (b) generates travel advance voucher per W25 petty cash or W556 AP payment run, (c) advance disbursed to employee payroll account or e-wallet per W261, (d) employee acknowledges advance receipt in self-service portal | Finance Analyst | HR Administrator | 15 min |
| 6 | **Employee travels and submits expenses**: During and after travel: (a) employee collects all BIR official receipts (ORs) for transport, accommodation, meals, and incidental expenses, (b) within 5 business days of return, submits expense report via HR self-service: itemized expenses with photo uploads of receipts, (c) receipts must include TIN, BIR registration number, and registered business name — non-compliant receipts flagged, (d) employee declares any unused advance amount for refund | Employee | — | 20 min |
| 7 | **System matches expenses to approved travel request**: Automated reconciliation: (a) matches each expense line to approved budget category, (b) flags policy exceptions: expenses exceeding daily rate, non-approved expense categories, missing receipts, non-BIR registered establishment receipts, (c) calculates variance: actual vs. approved budget, (d) routes exceptions to HR Administrator for manual review and approval or denial | System | HR Administrator | 5 min (automated) |
| 8 | **Finance processes per diem settlement**: Settlement calculation: (a) actual expenses vs. advance amount, (b) if actual < advance: employee refunds excess via payroll deduction per W10 or direct refund, (c) if actual > advance: reimbursement of shortfall processed per W74 expense reimbursement, (d) all expenses must have valid BIR ORs — unsupported amounts treated as taxable benefit, (e) Finance Analyst approves settlement, posts to GL cost center | Finance Analyst | Payroll Manager | 15 min |
| 9 | **Monthly travel analytics**: HR Administrator generates consolidated travel report: (a) total travel spend by department and cost center, (b) spend by travel purpose (store visits, vendor meetings, DC audits, training, projects), (c) spend by destination region (Luzon, Visayas, Mindanao, international), (d) policy compliance rate (target: 95%+ compliant trips), (e) average cost per trip by category, (f) advance outstanding aging report (target: 100% settled within 30 days of trip), (g) share with Finance Manager for budget variance analysis per W35 | HR Administrator | Finance Manager | 2 hours/month |
| 10 | **Quarterly travel policy review and vendor negotiation**: HR Administrator and Finance Manager: (a) review travel spend trends and policy effectiveness, (b) negotiate corporate rates with airlines (PAL, Cebu Pacific, AirAsia) based on volume commitments, (c) negotiate hotel chain agreements (national chains with presence in BuildRight store locations), (d) review and update per diem rates based on actual accommodation and meal costs, (e) benchmark travel policy against Philippine retail industry standards, (f) update approved hotel and transport provider lists | HR Administrator | Finance Manager | 2 hours/quarter |

### System Touchpoints

- W74 expense reimbursement — post-travel expense settlement and shortfall reimbursement
- W25 petty cash — travel advance disbursement for smaller amounts
- W556 AP payment run — travel advance disbursement for larger amounts
- W10 payroll processing — per diem processing and advance refund via payroll deduction
- W128 enterprise project management — project-related travel budget tracking and approval
- W121 operational audit — audit travel scheduling and expense justification
- W152 IT provisioning — remote access and mobile connectivity during travel
- W35 management reporting — travel expense analytics and budget variance reporting

### Pain Points / Risks

- Unapproved travel claims — employees booking travel before receiving approval, creating pressure for retroactive authorization; system should block expense reimbursement for unapproved trips
- Receipt collection challenges — lost receipts, receipts from non-BIR registered establishments (common in provincial areas and smaller cities), faded thermal receipts; digital receipt photo capture at point-of-sale mitigates
- Per diem abuse — employees claiming full per diem while staying with family/friends or in company-provided accommodation; system should cross-check accommodation bookings against per diem claims
- Last-minute booking premiums — urgent travel requests result in higher airfare and hotel rates, often 30-50% above advance booking rates; 7-day advance booking policy with escalation path
- Typhoon and weather disruptions — Philippine typhoon season (June-November) frequently causes flight cancellations and rebooking costs; travel insurance and flexible rebooking policies essential
- Travel advance outstanding tracking — employees failing to settle advances within policy timeframe; aging report and automatic payroll deduction after 30-day deadline per W10
- Cross-entity travel cost allocation — employees from one entity traveling for another entity's business require intercompany cost allocation per W752

### Time Estimate

Per trip: request submission (15 min) + approval processing (automated routing, 4 hours to 1 day SLA) + booking (30 min) + expense submission (20 min) + settlement processing (15 min) = ~1-2 hours total employee time across the travel lifecycle. Monthly travel analytics: 2 hours. Travel Coordinator daily operations: ~4 hours/day or ~20 hours/week. Quarterly policy review: 2 hours.

### Staffing Implication

1 Travel Coordinator (can be shared with HR Administrator role; primarily handles booking coordination, vendor management, and advance tracking); partially absorbed by existing HR Service Desk per W646 for routine request intake and receipt processing. Estimated incremental load: 20 hours/week for Travel Coordinator function. No additional headcount required if redistributed from existing HR Admin capacity.

---

## W816. Multi-Entity Payroll Consolidation & Cross-Entity Reconciliation

| Field | Detail |
|---|---|
| **Trigger** | Semi-monthly payroll run completion across all 5 entities per W10 |
| **Frequency** | Semi-monthly; 2 consolidation runs per month |
| **Volume** | 5 entities × 2 runs = 10 payroll runs per consolidation cycle |
| **Owner** | Payroll Manager |
| **Participants** | Payroll Manager, HR BP, Finance Manager, Tax Accountant |

### Background

BuildRight Depot Corp operates through 5 legal entities — BuildRight Holdings Corp (parent), BuildRight Depot Inc (retail operations), BuildRight Logistics Inc (supply chain and DC operations), BuildRight Digital Commerce Inc (e-commerce and digital platforms), and BuildRight Property Management Inc (real estate and facilities) — each with separate employer registrations and independent payroll runs per W10. While W10 handles individual entity payroll processing including timekeeping integration, statutory deductions, and bank file generation, there is no existing workflow for reconciling and consolidating payroll data across all entities. Cross-entity payroll complexities include: employees with dual entity assignments (e.g., shared services staff in IT, Finance, and HR whose costs are allocated to operating entities), intercompany labor cost allocations requiring transfer pricing compliance per W235, consolidated statutory reporting requirements (SSS, PhilHealth, and Pag-IBIG filings can be per employer entity but must reconcile to consolidated totals), and consolidated payroll expense reporting for management reporting per W35. With 6,715 employees across 5 entities and a combined monthly payroll of approximately PHP 280-350 million, precise cross-entity reconciliation is essential for accurate financial reporting, statutory compliance, and intercompany balance settlement. The Philippine regulatory environment adds complexity — each entity has separate BIR registration (with different RDO codes), separate SSS/PhilHealth/Pag-IBIG employer numbers, and separate bank accounts for payroll disbursement.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Confirm all entity payroll runs completed**: Payroll Manager verifies: (a) all 5 entity payroll runs completed successfully per W10, (b) payroll registers approved and locked by each entity's authorized signatory, (c) all payroll entries posted to respective entity general ledgers, (d) no pending payroll corrections or void transactions, (e) bank disbursement files generated and transmitted per entity; any entity with incomplete payroll blocks consolidation start | Payroll Manager | — | 30 min |
| 2 | **System generates cross-entity payroll reconciliation report**: Automated report includes: (a) total gross payroll by entity with breakdown (basic salary, overtime, allowances, bonuses, commissions), (b) total deductions by entity (SSS ER/EE, PhilHealth ER/EE, Pag-IBIG ER/EE, BIR withholding tax, loans, other deductions), (c) net payroll by entity, (d) intercompany labor allocations summary — shared services costs allocated to operating entities per W752, (e) cross-entity employee list — employees paid by one entity but with costs allocated to another entity (e.g., IT staff employed by Holdings but serving Depot), (f) statutory contribution totals by entity vs. consolidated total, (g) intercompany payroll receivable/payable balances | System | Payroll Manager | Automated (15 min generation) |
| 3 | **Review intercompany labor allocations**: Payroll Manager and Finance Manager validate: (a) HQ shared services allocation (IT, Finance, HR, Legal) — costs distributed to Depot (60%), Logistics (20%), Digital Commerce (15%), Property Management (5%) per W752 allocation keys, (b) allocation methodology matches approved transfer pricing policy per W235 — arm's length basis using headcount + revenue weighting, (c) verify no shared services employee is duplicated (paid by Holdings AND allocated to operating entity — should be paid once and allocated), (d) check for new employees not yet included in allocation methodology, (e) validate allocation journal entries posted correctly to each entity GL | Payroll Manager | Finance Manager | 1-2 hours |
| 4 | **Reconcile statutory contributions across entities**: Tax Accountant performs: (a) SSS — verify each entity's SSS ER and EE contributions reconcile to consolidated total; check against SSS online portal per entity, (b) PhilHealth — verify each entity's PhilHealth contributions (2026 rate: 5% of monthly basic salary, split 2.5% ER / 2.5% EE) reconcile to consolidated; verify against PhilHealth employer portal, (c) Pag-IBIG — verify each entity's Pag-IBIG contributions (PHP 100 EE + PHP 100 ER for employees earning >PHP 1,500/month) reconcile to consolidated, (d) BIR withholding tax — verify each entity's expanded withholding tax on compensation reconciles to consolidated; cross-check against BIR eFPS filing per entity per W90 | Tax Accountant | Payroll Manager | 1-2 hours |
| 5 | **Identify and resolve discrepancies**: Common discrepancy types: (a) cross-entity employee paid by wrong entity — employee transferred mid-period per W511 but payroll not updated in time, resulting in dual payment or missed payment; requires reversal and rebooking, (b) allocation calculation errors — rounding differences, headcount changes not reflected in allocation keys, or manual override errors; requires correction to W752 allocation parameters, (c) statutory calculation differences — SSS/PhilHealth/Pag-IBIG contribution caps applied differently across entities due to configuration variance; requires system correction, (d) intercompany balance mismatches — shared services allocation posted in one entity but not the receiving entity; requires journal entry correction per W638 | Payroll Manager | Finance Manager | 1-2 hours |
| 6 | **Post consolidation adjustments**: For each identified discrepancy: (a) prepare journal entries per W638 journal entry review workflow, (b) intercompany corrections require dual-entry (debit in receiving entity, credit in sending entity), (c) adjustments must maintain balanced intercompany positions per W235, (d) post adjustments with full documentation supporting the correction, (e) re-run reconciliation report to verify zero remaining discrepancies or document accepted variances below materiality threshold (PHP 5,000 per entity pair) | Payroll Manager | Finance Manager | 30-60 min |
| 7 | **Generate consolidated payroll expense report**: Payroll Manager produces consolidated report for management reporting per W35: (a) consolidated payroll expense by natural account (basic salary, overtime, allowances, statutory ER contributions, HMO, other benefits), (b) payroll expense by entity, (c) payroll expense by department/function, (d) intercompany allocation summary, (e) month-over-month and year-over-year comparison, (f) headcount reconciliation by entity (opening + hires - separations = closing per W645), (g) payroll-to-revenue ratio (target: <12% for retail operations) | Payroll Manager | Finance Manager | 1 hour |
| 8 | **Monthly payroll tax reconciliation**: Tax Accountant reconciles: (a) BIR withholding tax on compensation per entity vs. consolidated per W590, (b) verify withholding tax deposits made per entity per W90 deadlines (10th and 25th of following month), (c) reconcile taxable compensation per entity with BIR Alphalist of Employees (due January 31 following year), (d) verify SSS/PhilHealth/Pag-IBIG remittance per entity matches payroll register per W251, (e) flag any entity with late remittance for immediate action to avoid penalties and surcharges | Tax Accountant | Payroll Manager | 1 hour |
| 9 | **Quarterly methodology review with Finance Manager**: Validate: (a) cross-entity allocation methodology still appropriate — headcount and revenue weighting ratios, (b) transfer pricing documentation per W235 compliant with BIR requirements, (c) any new shared services functions requiring allocation methodology update, (d) benchmark allocation methodology against industry practices, (e) review intercompany payroll balance aging — ensure all intercompany balances settled within quarter, (f) update allocation parameters in system if methodology changes approved | Payroll Manager | Finance Manager | 2 hours/quarter |

### System Touchpoints

- W10 payroll processing — entity-level payroll run completion triggers consolidation
- W752 IC management fee allocation — shared services labor cost allocation methodology and posting
- W235 transfer pricing — intercompany pricing compliance for labor allocations
- W638 journal entry review — consolidation adjustment posting and approval
- W35 management reporting — consolidated payroll expense reporting
- W590 tax provision — consolidated tax reconciliation
- W251 statutory benefits — SSS, PhilHealth, Pag-IBIG reconciliation by entity
- W90 tax filing — BIR withholding tax filing per entity
- W261 e-wallet settlement — payroll disbursement reconciliation
- W444 13th month reconciliation — 13th month pay also requires cross-entity reconciliation

### Pain Points / Risks

- Cross-entity employee tracking errors — employees who transfer between entities mid-payroll period per W511 may be paid by the wrong entity or duplicated; real-time entity assignment synchronization between HR module and payroll is critical
- Allocation methodology disputes — entity controllers may challenge shared services allocation ratios, arguing their entity is over-allocated; clear transfer pricing documentation per W235 and quarterly review mitigates
- Mid-period employee transfers — employee transferring from Depot to Digital Commerce on the 10th creates split payroll: 10 days Depot, remaining days Digital Commerce; manual intervention often required
- Statutory contribution filing deadlines — each entity has separate filing deadlines and employer numbers; missing any entity's deadline results in penalties and surcharges; centralized tracking dashboard essential
- Consolidated reporting lag — waiting for all 5 entity payrolls to complete before consolidation can begin; if one entity has issues, entire consolidation is delayed; SLA enforcement per entity per W10 critical
- Intercompany balance settlement — intercompany payroll receivables/payables must be settled regularly; unresolved balances accumulate and complicate entity-level financial statements per W235
- BIR audit risk — BIR may examine consolidated employer-employee relationships during tax assessments; clear entity separation documentation and transfer pricing support essential

### Time Estimate

Per consolidation cycle (semi-monthly): Step 1 confirmation (30 min) + Step 2 report generation (automated, 15 min) + Step 3 allocation review (1-2 hours) + Step 4 statutory reconciliation (1-2 hours) + Step 5 discrepancy resolution (1-2 hours) + Step 6 adjustments (30-60 min) + Step 7 consolidated reporting (1 hour) + Step 8 tax reconciliation (1 hour) = 5-7 hours semi-monthly. Quarterly methodology review: 2 hours. Annual total: ~140-180 hours.

### Staffing Implication

Absorbed by Payroll Manager and existing Finance team. Estimated Payroll Manager time: 10-14 hours/month (5-7 hours × 2 cycles). Tax Accountant: 4 hours/month. Finance Manager: 4 hours/month for review and quarterly methodology sessions. No incremental headcount — this is a governance and reconciliation function within existing roles.

---

## W817. Employee Sabbatical, Study Leave & Secondment Management

| Field | Detail |
|---|---|
| **Trigger** | Employee requests extended leave for education, professional development, or cross-functional assignment |
| **Frequency** | Monthly; ~5-10 requests per month |
| **Volume** | ~5-10 active sabbaticals/study leaves/secondments at any time; ~60-120 per year |
| **Owner** | HR Business Partner |
| **Participants** | Employee, Department Manager, HR BP, Training Manager, Finance Analyst, Receiving Department Manager (for secondment) |

### Background

BuildRight Depot's aggressive growth strategy — expanding from 200 to 250+ stores within 3 years — requires a deeply developed talent pipeline beyond what traditional training programs per W51 can deliver. This workflow manages three distinct extended development programs: (a) Study Leave for advanced degrees and professional certifications — employees pursuing MBA degrees (commonly at Ateneo de Davao, University of the Philippines, or De La Salle), engineering certifications (Licensed Civil Engineer, Certified Supply Chain Professional), or specialized retail management programs; typically 3-12 months with partial to full pay depending on whether company-sponsored or self-initiated, per Philippine Labor Code provisions and company policy; (b) Sabbatical for burnout prevention and professional renewal — available to employees with 5+ years of continuous service, typically 1-6 months at 50% base pay continuation, supporting mental health and retention objectives per W645 workforce planning; (c) Secondment / Cross-Functional Assignment — 3-12 months in a different department, entity, or location to develop cross-functional skills and organizational depth, directly supporting W567 cross-training at a deeper level and W178 succession planning. With 6,715 employees, even a modest 1-2% participation rate means 67-134 employees annually in these programs. BIR implications include continued tax withholding during study leave (taxable compensation even if reduced), entity change processing for cross-entity secondments per W511, and benefits continuation accounting across entities. DOLE compliance requires proper documentation of leave nature, expected duration, and return-to-work commitment.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Employee submits request via HR self-service**: Employee completes extended leave/assignment request form: (a) type: sabbatical, study leave, or secondment, (b) proposed duration and dates (minimum 3 months, maximum 12 months with extension possible), (c) purpose and objectives: for study leave — degree/program details and institution; for sabbatical — personal development plan; for secondment — target department, role, and learning objectives, (d) for secondment: proposed receiving department and location (may be different entity per W511), (e) impact statement: how current responsibilities will be covered, (f) expected return date and post-program commitment (company policy: minimum 1 year return service agreement for company-sponsored study leave) | Employee | — | 30 min |
| 2 | **HR BP reviews eligibility**: Automated and manual eligibility check: (a) minimum tenure — 5 years continuous service for sabbatical, 2 years for study leave, 1 year for secondment, (b) performance rating — must be "Meets Expectations" or above in most recent performance review per W72; "Needs Improvement" or below disqualifies, (c) no pending disciplinary actions or PIP (Performance Improvement Plan) per W603 disciplinary process, (d) department coverage feasibility — HR BP reviews W34 shift scheduling to confirm department can sustain operations without the employee, (e) program-specific checks: study leave — verify institution accreditation (CHED-recognized for Philippine institutions); secondment — verify receiving department has capacity and meaningful assignment; sabbatical — verify no previous sabbatical within last 3 years | HR BP | — | 30 min |
| 3 | **Department Manager approves with coverage plan**: Manager must submit coverage plan: (a) backfill from cross-trained employee pool per W567 — identify specific employee(s) who can absorb responsibilities, (b) temporary hire per W555 seasonal staffing if role is customer-facing and cannot be absorbed by existing team (e.g., Store Cashier, Sales Floor staff), (c) workload redistribution plan — which tasks are redistributed to which team members, (d) performance impact assessment — HR BP and Manager jointly assess risk to department KPIs during employee absence, (e) for secondment: both sending and receiving Department Managers must approve | Dept Manager | HR BP | 1-2 hours |
| 4 | **Compensation and benefits determination**: HR BP and Finance Analyst determine: (a) sabbatical — 50% base pay continuation, no overtime/allowance/commission, benefits (HMO per W642, SSS/PhilHealth/Pag-IBIG contributions) continue at full rate with employer portion unchanged, (b) study leave — full pay if company-sponsored program (BuildRight has partnerships with local universities for Retail Management and Supply Chain Management programs); partial pay (60%) if self-initiated degree; no pay if employee requests pure academic leave beyond company sponsorship, (c) secondment — full pay from receiving entity if cross-entity per W511 transfer rules; same-entity secondment retains original cost center allocation; any location differential (e.g., from Davao HQ to Manila store) adjusted per company policy, (d) 13th month pay eligibility — maintained for sabbatical and secondment at reduced rate proportional to pay; maintained at full for company-sponsored study leave per W444 | HR BP | Finance Analyst | 1 hour |
| 5 | **Execute cross-entity transfer for secondment (if applicable)**: For cross-entity secondments: (a) process temporary transfer per W511 between entities (e.g., Depot to Logistics), (b) establish temporary reporting line — functional reporting to receiving manager, administrative reporting to original entity HR, (c) set secondment objectives collaboratively with both sending and receiving managers: specific skills to develop, projects to complete, measurable outcomes, (d) document secondment agreement signed by both managers, employee, and HR BP, including return-to-original-role commitment date | HR BP | Receiving Dept Manager | 1 hour |
| 6 | **System updates and provisioning**: HR Administrator processes: (a) employee status change in HR module (sabbatical/study leave/secondment status with expected return date), (b) cost center allocation update — for secondments: move cost center to receiving department/entity; for sabbatical/study leave: allocate to department overhead or separate development cost center, (c) benefits continuation — ensure HMO per W642 remains active, SSS/PhilHealth/Pag-IBIG contributions continue (employer portion unchanged, employee portion deducted from reduced pay), (d) IT access provisioning per W152 — for secondment: grant receiving department system access while retaining original access; for sabbatical/study leave: may restrict operational system access based on security policy, (e) update W645 workforce planning module — reflect employee in development program status | HR Administrator | IT (W152) | 30 min |
| 7 | **Ongoing program monitoring**: During the program: (a) HR BP conducts monthly check-in with employee via phone, video call, or in-person (for study leave: academic progress; for sabbatical: well-being and professional development activities; for secondment: integration and skill development), (b) secondment receiving manager provides quarterly feedback to sending manager and HR BP on employee performance and development, (c) system tracks program milestones and return date countdown, (d) early termination handling: if employee requests to return early or program is terminated — HR BP coordinates immediate return processing, (e) extension requests: employee may request extension up to 3 months with re-approval from both managers | HR BP | — | 30 min/month × program duration |
| 8 | **Return to work processing**: At program completion: (a) HR BP schedules re-onboarding meeting 1 week before return — review changes in department during absence, updated processes, new team members, (b) Department Manager assigns updated responsibilities — may include new projects or expanded role reflecting skills gained, (c) employee presents learnings and achievements to team — knowledge transfer session (mandatory for study leave and secondment, optional for sabbatical), (d) system restores original employee status, cost center, and reporting line, (e) for secondment: reverse cross-entity transfer per W511, transfer knowledge to receiving department colleagues, (f) IT access per W152 restored or adjusted based on updated role, (g) update W645 workforce planning with skills inventory additions | HR BP | Dept Manager | 1 hour |
| 9 | **Post-program evaluation and impact assessment**: Within 30 days of return: (a) skills gained assessment — HR BP and Training Manager document new competencies per W682 career development, (b) ROI evaluation — Finance Analyst compares program cost (pay continuation + replacement costs + admin overhead) against tangible benefits (skills applied to projects, process improvements, promotions), (c) career path impact — update employee's career development plan per W682 with new skills and potential career trajectory changes, (d) feed into W645 workforce planning — aggregate data on program effectiveness, retention rates of program participants vs. non-participants, succession pipeline depth improvement, (e) annual program report: participation rates, cost, ROI, retention impact, diversity metrics — presented to CHRO and executive committee | HR BP | Training Manager | 1 hour |

### System Touchpoints

- W72 performance management — eligibility based on performance rating
- W34 shift scheduling — department coverage feasibility assessment
- W511 cross-entity transfer — secondment entity change processing
- W567 cross-training — backfill from cross-trained employee pool
- W645 workforce planning — program participation tracking and talent pipeline impact
- W178 succession & internal mobility — secondment as development pathway for succession candidates
- W642 HMO administration — benefits continuation during program
- W152 IT provisioning — access changes during and after program
- W555 seasonal staffing — temporary hire for coverage during extended absence
- W682 career development — post-program skills assessment and career path update
- W10 payroll processing — pay continuation and statutory contribution processing
- W15 onboarding — re-onboarding process upon return from extended program
- W444 13th month reconciliation — pro-rated 13th month pay during reduced-pay periods

### Pain Points / Risks

- Department coverage gaps — extended absence of experienced employees, especially in small store teams (29 employees per store), can strain operations; Store Manager must redistribute workload to remaining staff, potentially impacting customer service levels per W30 customer feedback
- Reintegration challenges — employees returning after 6-12 months may find their team has changed, processes have been updated, and their role has evolved; structured re-onboarding per W15 is essential but often neglected
- Compensation disputes — employees on reduced pay (sabbatical at 50%, study leave at 60%) may feel financially strained, especially in Philippine context where extended family financial obligations are common; clear pre-program counseling on financial impact is necessary
- Skills atrophy during sabbatical — employees on sabbatical not engaged in professional development may lose technical currency; minimum professional development activity requirement (e.g., 1 course, 2 books, 1 conference attendance) should be enforced
- Secondment host department reluctance — receiving department may resist returning high-performing seconded employee to original department; clear secondment agreement with fixed return date and no-poach clause mitigates
- Selection bias in program access — perception that development programs favor certain groups (HQ vs. store, certain departments, or certain demographics); transparent eligibility criteria, application process, and selection committee with diverse representation per W641 DEI training is essential
- Return service agreement enforcement — company-sponsored study leave requires 1-year return service; if employee resigns immediately after, company must recover costs; legal enforceability under Philippine labor law varies; pro-rated clawback clause recommended
- Impact measurement difficulty — ROI of development programs is inherently difficult to quantify; without structured tracking, programs may be perceived as "perks" rather than strategic investments; post-program evaluation framework in Step 9 addresses this

### Time Estimate

Per program: eligibility review (30 min) + approval coordination with coverage plan (1-2 hours) + compensation setup (1 hour) + system provisioning (30 min) + monthly check-ins (30 min × number of months) + return processing (1 hour) + post-program evaluation (1 hour) = ~6-10 hours per program depending on duration. Monthly portfolio review (all active programs): 2 hours. Annual program effectiveness report: 4 hours.

### Staffing Implication

Absorbed by HR BP team within existing headcount. Estimated HR BP time: 10-15 hours/month (assuming 5-10 active programs with monthly check-ins). Finance Analyst: 2-3 hours/month for compensation setup and ROI evaluation. Training Manager: 2-3 hours/month for skills assessment coordination. No incremental headcount required; program volume (5-10 active at any time) is manageable within existing HR BP portfolio of 25-30 employees per BP.
