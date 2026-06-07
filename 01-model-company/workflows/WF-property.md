# Real Estate & Lease Management Workflows

> Site selection, lease administration, rent processing, and property tax management.
>
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W116. Site Selection & Feasibility Analysis](#w116-site-selection-feasibility-analysis)
- [W117. Lease Administration & Renewal](#w117-lease-administration-renewal)
- [W118. Rent & CAM Payment Processing](#w118-rent-cam-payment-processing)
- [W119. Real Property Tax (Amillaramento) Management](#w119-real-property-tax-amillaramento-management)
- [W275. IFRS 16 / PFRS 16 Lease Accounting & Modifications](#w275-ifrs-16-pfrs-16-lease-accounting-modifications)
- [W430. LGU Business Permit & "Amillaramento" (RPT) On-Site Inspection](#w430-lgu-business-permit--amillaramento-rpt-on-site-inspection)
- [W807. Store Closure, Lease Termination & Asset Recovery Management](#w807-store-closure-lease-termination--asset-recovery-management)

---

## W116. Site Selection & Feasibility Analysis

| Field | Detail |
|---|---|
| **Trigger** | Strategic growth plan (10–15 new stores/year target) |
| **Frequency** | Ongoing; ~15–20 sites evaluated monthly |
| **Volume** | ~10–15 approved sites/year |
| **Owner** | VP for Property Management |
| **Participants** | Property Acquisition Manager, Finance (ROI analysis), CEO/Board (approval) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Identify potential site (greenfield or existing building) based on catchment analysis | Property Manager | VP Property | 1–2 weeks |
| 2 | Conduct site survey: size (8k–15k sqm), zoning, access, utilities, competitors | Property Manager | VP Property | 3–5 days |
| 3 | Financial Feasibility: Calculate projected store sales (W13) vs. build/lease cost | Finance Analyst | CFO | 2–3 days |
| 4 | Draft Letter of Intent (LOI) and initial lease terms | Property Manager | VP Property | 2 days |
| 5 | Present Site Selection Memo to Board/CEO for approval | VP Property | CEO | 1 hour |
| 6 | Execute Lease Agreement (W117) | Legal / VP Property | VP Property | 1–2 weeks |

### System Touchpoints
- Lease master data: initial site parameters, LOI tracking
- Document management for site surveys, feasibility studies, and board memos
- Financial planning module for ROI / NPV modeling

### Pain Points / Risks
- Philippine real estate market volatility (land values in Metro Manila vs. provinces)
- LGU zoning and land-use conversion delays

### Staffing Implication
15–20 evaluations/month, 10–15 approvals/year. ~2 weeks per evaluation. 1 Property Acquisition Manager + VP Property oversight. Absorbed.

### Time Estimate
~2 weeks per site evaluation from identification to Board approval.

---

## W117. Lease Administration & Renewal

| Field | Detail |
|---|---|
| **Trigger** | Signed lease or upcoming expiry (12–18 months prior) |
| **Frequency** | Managed per contract; ~200+ active leases |
| **Volume** | ~20–30 renewals/year |
| **Owner** | Lease Administrator |
| **Participants** | VP Property, Legal, Finance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Input new lease into ERP: terms, escalations (e.g., 5% every 2 years), grace periods | Lease Admin | VP Property | 2 hours |
| 2 | System flags upcoming expiry (T-minus 18 months) | System | — | Automated |
| 3 | Evaluate store performance and strategic value of location | Store Ops / Finance | COO | 1 week |
| 4 | Negotiate renewal terms with lessor | VP Property | VP Property | 2–4 weeks |
| 5 | Legal review of renewal addendum | Legal Counsel | VP Legal | 3–5 days |
| 6 | Update ERP with new lease end date and revised escalation schedule | Lease Admin | VP Property | 1 hour |

### System Touchpoints
- Lease master data: terms, escalations, renewals, security deposits
- Automated expiry alerts (18-month notification)
- Document management for scanned lease agreements and addenda
- Integration with AP for recurring rent payments (W118)

### Pain Points / Risks
- Lease escalation clause interpretation (percentage vs. fixed)
- CAM charge disputes with lessors
- BIR documentary stamp tax on lease agreements

### Staffing Implication
200+ active leases, 20–30 renewals/year. 1 Lease Administrator full-time.

### Time Estimate
~2 hours per new lease setup; 2–4 weeks per renewal cycle.

---

## W118. Rent & CAM Payment Processing

| Field | Detail |
|---|---|
| **Trigger** | Monthly billing or lease schedule |
| **Frequency** | Monthly |
| **Volume** | ~250 payments/month (Stores, DCs, Offices, Parking) |
| **Owner** | AP Specialist (Lease) |
| **Participants** | Lease Administrator, Finance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System generates payment schedule for base rent per lease master | System | — | Automated |
| 2 | Receive lessor invoice for Common Area Maintenance (CAM) and utility recharges | Lease Admin | — | Monthly |
| 3 | Validate CAM charges against lease caps/clauses | Lease Admin | VP Property | 30 min/inv |
| 4 | Create AP voucher in ERP (2-way match: Invoice to Lease Master) | AP Specialist | AP Supervisor | 15 min/inv |
| 5 | Route for approval per tiered matrix | AP Supervisor | Finance Manager | 10 min/inv |
| 6 | Release payment (Check or Bank Transfer) | Treasury | CFO | 1 day |

### System Touchpoints
- AP module: recurring payment schedules, 2-way match (Invoice to Lease Master)
- Lease master data for rent amounts and CAM caps
- Treasury module for payment release (check or bank transfer)
- Integration with GL for rent expense and CAM allocation

### Pain Points / Risks
- CAM charge disputes with lessors
- Lease escalation clause interpretation (percentage vs. fixed)

### Staffing Implication
~250 payments/month. ~5 min per payment after initial setup. 1 AP Specialist (Lease) full-time.

### Time Estimate
~5 min per recurring payment after initial setup; ~30 min per CAM invoice validation.

---

## W119. Real Property Tax (Amillaramento) Management

| Field | Detail |
|---|---|
| **Trigger** | Annual/Quarterly tax assessment from LGU |
| **Frequency** | Annual (with quarterly installment options) |
| **Volume** | ~50 owned sites (Land/Building) |
| **Owner** | Tax Manager |
| **Participants** | Lease Admin (for records), Finance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Consolidate list of owned properties and current tax declarations | Lease Admin | VP Property | 2 days |
| 2 | Receive Tax Bill from LGU (Provincial/City Treasurer) | Tax Manager | — | Annual |
| 3 | Validate assessment against previous year and improvements made | Tax Manager | CFO | 1 hour/site |
| 4 | Calculate prompt-payment discounts (if applicable) | Tax Manager | Tax Manager | 15 min/site |
| 5 | Process payment via manager's check or bank transfer to LGU | Treasury | CFO | 1–2 days |
| 6 | File receipt and update property records in ERP (Fixed Asset module) | Lease Admin | — | 30 min |

### System Touchpoints
- Fixed Asset module for owned property tax tracking
- AP module for LGU tax payments
- Document management for tax declarations and receipts

### Pain Points / Risks
- Real property tax assessment disputes with LGU assessors
- LGU zoning and land-use conversion delays affecting assessments

### Staffing Implication
50 owned sites, annual cycle. ~1 hour per site = ~50 hours/year. Absorbed by Tax Manager.

### Time Estimate
~1 hour per site validation; ~50 hours/year total. Concentrated in Q1 (annual assessment cycle).

---

## W275. IFRS 16 / PFRS 16 Lease Accounting & Modifications

| Field | Detail |
|---|---|
| **Trigger** | Execution of a new long-term store lease, or modification (renewal, rent escalation, space reduction) of an existing lease. |
| **Frequency** | Monthly |
| **Volume** | 5-10 modifications or new setups per month |
| **Owner** | Finance (Lease Accounting Controller) |
| **Participants** | Real Estate Team, Finance, Legal |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Real Estate finalizes the lease terms (W117) and routes executed contract to Finance | VP Property / Lease Admin | Finance (Lease Accounting Controller) | 1 day |
| 2 | Lease Accounting Controller inputs the lease parameters (term, incremental borrowing rate, fixed/variable payments, payment schedule) into the ERP Lease Accounting module | Lease Accounting Controller | Controller | 30 min |
| 3 | System calculates the initial Right-of-Use (ROU) Asset and Lease Liability using present-value method; Controller reviews the calculation for accuracy | System | Controller | 15 min |
| 4 | System posts the initial journal entry (Dr. ROU Asset / Cr. Lease Liability); monthly auto-posts depreciation on ROU asset and interest expense on liability | System | Lease Accounting Controller | Automated |
| 5 | Upon a modification (e.g., rent escalation, space reduction, lease extension), Lease Admin notifies Finance; Controller triggers a reassessment in the ERP which recalculates the present value and adjusts the liability and ROU asset balances dynamically | Lease Accounting Controller | Controller | 30 min |
| 6 | External auditor reviews a sample of lease accounting entries during annual audit (W95); Finance provides supporting documentation (lease contracts, discount rate methodology, modification history) | Lease Accounting Controller | External Auditor | Per W95 |

### System Touchpoints
- Lease Administration Module
- General Ledger
- Fixed Assets

### Pain Points / Risks
- Audit failures due to incorrect discount rates, manual spreadsheet errors resulting in restated financial statements.
- PFRS 16 / IFRS 16 discount rate determination challenges

### Staffing Implication
5–10 setups/modifications/month x 2 hours each = ~10–20 hours/month. 1 Lease Accounting Controller. Absorbed by existing Finance team.

### Time Estimate
2 hours per lease setup/modification

---

## W430. LGU Business Permit & "Amillaramento" (RPT) On-Site Inspection

| Field | Detail |
|---|---|
| **Trigger** | Scheduled or surprise inspection by LGU (Bureau of Fire Protection, Sanitary, Building Official) |
| **Frequency** | Annual (for renewal) or ad-hoc |
| **Volume** | 200 stores × ~3–4 inspection types/year = ~600–800 inspections |
| **Owner** | Store Manager |
| **Participants** | Store Admin, Facilities Coordinator, LGU Inspector, Regional Manager |

### Background

In the Philippines, operating a big-box retail store requires multiple local government permits (Mayor's Permit, Fire Safety Inspection Certificate, Sanitary Permit, etc.). LGU inspectors from the Bureau of Fire Protection (BFP) and the City/Municipal Engineering Office conduct on-site inspections to verify compliance with safety, health, and building standards. This workflow manages the interaction with inspectors and the resolution of "Notice of Violations."

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Inspector Arrival**: LGU inspector arrives at the store; Store Manager verifies inspector credentials (Mission Order) and registers them in the Compliance Log | Store Manager | — | 15 min |
| 2 | **On-Site Walkthrough**: Store Manager and Store Admin accompany the inspector through the premises: (a) fire exits, (b) extinguisher pressure/maintenance, (c) sanitary conditions in restrooms/canteen, (d) structural safety of lumber yard racks | Store Manager | Regional Mgr | 1–2 hours |
| 3 | **Inspection Report**: Inspector issues an "After Mission Report" or "Notice of Inspection"; Store Manager scans and uploads the document to the Compliance Portal | Store Manager | — | 15 min |
| 4 | **Notice of Violation (NOV) Intake**: If violations are found (e.g., blocked fire exit, expired extinguisher), the inspector issues an NOV with a 5-to-15 day correction period | Store Manager | Regional Mgr | 30 min |
| 5 | **Correction Action**: Store Manager triggers an "Emergency Work Order" (W47) to fix the violation; Facilities Coordinator manages the contractor/maintenance team | Store Manager / Facilities | Store Ops Director | 1–3 days |
| 6 | **Re-Inspection & Clearing**: Store Manager notifies LGU of correction; inspector returns for re-inspection; Store Manager receives the "Cleared" status and pays any required fines | Store Manager | Finance Mgr | 2 hours |
| 7 | **Permit Renewal Linkage**: Cleared inspection reports are attached to the "LGU Permit Renewal" workflow (W54) to ensure the Mayor's Permit can be renewed the following year | Store Admin | — | 15 min |

### System Touchpoints

- Compliance Portal: tracks inspection history, pending NOVs, and correction deadlines for 200 sites (W430.3)
- Integration with W47 (Store Maintenance — for fixing violations) and W54 (Permit Renewal)
- LGU Violation Log: dashboard for Regional Managers to track systemic issues (e.g., recurring fire safety violations)

### Pain Points / Risks

- **Discretionary Enforcement**: Different LGUs may interpret fire or sanitary codes inconsistently, leading to unexpected NOVs for previously compliant stores
- **Closure Risk**: Severe fire safety violations (e.g., non-functional sprinkler system) can lead to immediate "Cease and Desist" or store closure orders by the BFP
- **Record Inaccessibility**: If the store cannot produce the previous year's permit or inspection receipt during a surprise visit, it faces immediate fines

### Staffing Implication

Managed by the Store Manager as part of store administration duties. Effort is ~4–6 hours per year per store.

### Time Estimate

**Total**: Arrival & Walkthrough — 2 hours; NOV Resolution — 1–3 days elapsed; Re-inspection — 2 hours; **Total cycle: ~1 week for NOV resolution**


---

## W441. Corporate Staff Housing & Billeting Management

| Field | Detail |
|---|---|
| **Trigger** | Assignment/relocation of management staff to a provincial store; or assignment of specialist audit/project teams |
| **Frequency** | Monthly (occupancy changes); Weekly (utility payments) |
| **Volume** | ~100–150 active staff houses/leases chain-wide |
| **Owner** | Property Manager |
| **Participants** | HR, Store Manager, Finance, Property Admin |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Request for Housing**: HR triggers request based on approved relocation or project deployment | HR | — | 10 min |
| 2 | **Lease Identification**: Property Admin sources local apartment/house; verifies safety/proximity to store | Property Admin | Property Mgr | 2–3 days |
| 3 | **Contracting**: System generates Lease Agreement; Finance processes security deposit and advance rent | Property Admin | Property Mgr | 1 day |
| 4 | **Inventory/Turnover**: Admin performs move-in inspection; documents condition and provided furniture/appliances | Property Admin | — | 1 hour |
| 5 | **Utility Management**: Admin sets up accounts (Water, Electricity, Internet); sets up recurring payment in ERP | Property Admin | Finance | 2 hours |
| 6 | **Occupancy Tracking**: HR updates "Billeting Log" with staff names and expected duration | HR | — | 5 min |
| 7 | **Maintenance**: Occupant submits maintenance request (W47); Admin coordinates with landlord/contractor | Occupant / Admin | — | Varies |
| 8 | **Closure/Move-out**: Admin performs move-out inspection; calculates utility prorations; Finance processes deposit recovery | Property Admin | Property Mgr | 2 hours |

### System Touchpoints
- Property Management module for tracking staff house leases and inventory
- AP integration for recurring rent and utility payments (W7)
- Billeting Log / Occupancy dashboard linked to Employee Master (W292)

### Pain Points / Risks
- High utility costs due to unmonitored consumption by billeted staff.
- Landlord disputes over security deposit recovery upon lease termination.
- Security risks if staff houses are in high-crime areas or lack basic safety features.

### Staffing Implication
Property Admin at HQ spends ~10–15 hours/week managing the billeting portfolio. Store Managers assist with local inspections.

---

## W807. Store Closure, Lease Termination & Asset Recovery Management

| Field | Detail |
|---|---|
| **Trigger** | Store performance review per W67 identifies chronically underperforming location; lease expiry without renewal decision; strategic market exit; force majeure (typhoon damage, LGU closure order) |
| **Frequency** | Ad-hoc; estimated 2-5 store closures/year as BuildRight optimizes its 200-store network |
| **Volume** | Each closure involves inventory valued at PHP 15-30M, fixed assets of PHP 5-10M, and 25-35 employees |
| **Owner** | VP for Store Operations |
| **Participants** | Store Manager, Finance, HR, Legal, Real Estate, Merchandising, IT, Loss Prevention, VP Supply Chain |

### Background

BuildRight operates 200 stores and regularly evaluates store performance per W67. Underperforming locations — those with negative EBITDA for 2+ consecutive quarters, or where lease renewal terms are economically unfavorable — are candidates for closure. Store closure is the reverse of W16 new store opening: it involves inventory liquidation, employee transfer or separation, lease termination, asset recovery, regulatory de-registration, and community relations. This workflow ensures store closures are executed in compliance with Philippine labor law (DOLE due process for separations), lease agreements (proper notice per contract terms), and regulatory requirements (BIR, LGU, BFP de-registration).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Closure Decision & Approval**: VP Store Operations presents closure recommendation to CEO and Board: (a) store P&L analysis per W67 showing sustained underperformance; (b) lease terms review per W117: remaining lease term, early termination penalty, renewal option; (c) market analysis: is underperformance location-specific or market-wide; (d) employee impact: number of employees, transfer opportunities at nearby stores, separation cost estimate per W43; (e) inventory and asset recovery estimate; (f) total closure cost vs. continued operation loss projection; (g) CEO approves closure; Board approves if closure cost exceeds DOA threshold | VP Store Ops | CEO / Board | 2-4 weeks |
| 2 | **Lease Termination**: Legal handles lease termination per W117: (a) review lease agreement for termination notice requirements (typically 60-90 days); (b) if early termination: negotiate termination fee with landlord per lease terms; (c) if lease expiry: serve non-renewal notice per contractual deadline; (d) negotiate security deposit return; (e) document condition of premises (photos, video) to protect against damage claims; (f) coordinate with VP Legal on any lease disputes | VP Legal / Real Estate | VP Store Ops | 2-3 months |
| 3 | **Employee Communication & Transition**: HR manages employee impact per DOLE requirements: (a) 30-day advance notice to affected employees per DOLE guidelines; (b) individual meetings with each employee: present options (transfer to nearby store, voluntary separation with enhanced package, or retrenchment with statutory separation pay per W43); (c) for transfers: coordinate with receiving Store Manager per W511 cross-location transfer; (d) for separations: compute final pay per W643 including separation pay (1/2 month per year of service for retrenchment under LC Art. 298); (e) assist with DOLE reporting if retrenchment exceeds threshold; (f) employee communication timeline must not precede public announcement to prevent premature store disruption | HR Manager / VP HR | VP Store Ops | 30-60 days |
| 4 | **Inventory Liquidation**: Merchandising and Supply Chain execute inventory removal: (a) W93 markdown execution for slow-moving items: progressive discounts (25%, 50%, 75%) over 4-6 weeks before closure; (b) transferable inventory: ship to nearby stores or DC per W22 at cost; (c) consignment inventory: return to vendor per W23; (d) unsold remaining inventory: bulk liquidation to discount retailers or jobbers; (e) inventory write-off for unsalvageable items per W587; (f) target: recover 70-85% of inventory value | Merchandising / Supply Chain | VP Store Ops | 4-8 weeks |
| 5 | **Asset Recovery**: Facilities and IT execute asset removal: (a) IT equipment (POS terminals per W265, servers, networking) decommissioned and shipped to IT warehouse for redeployment per W131; (b) store fixtures and furniture: assess reuse potential; ship reusable items to warehouse for new store deployment; (c) shelving and racking: sell to used fixture dealers or scrap per W443; (d) signage and branding: removed per lease requirements; (e) fixed assets: update register per W39 with disposal accounting | IT / Facilities / Finance | VP Store Ops | 1-2 weeks |
| 6 | **Regulatory De-Registration**: Legal and Finance handle regulatory closure per W437: (a) BIR: notify RDO of branch closure, cancel CAS registration per W54A, file final tax return; (b) LGU: surrender Business Permit, cancel LBT registration per W802; (c) BFP: FSIC cancellation per W476; (d) DENR: cancel Permit to Operate if applicable per W477; (e) SSS/PhilHealth/Pag-IBIG: update employer location records; (f) update Location Master per W254 to "Closed" status | Legal / Finance | VP Legal | 1-2 months |
| 7 | **Community & Customer Communication**: VP Communications manages stakeholder communication: (a) customer notification: post signage in-store 30 days before closure, redirect to nearest BuildRight store; (b) loyalty members per W17: notify of nearest alternative location, maintain points balance; (c) community: coordinate with Barangay per W209 for respectful departure; (d) media: prepare press statement if closure attracts media attention; (e) update store locator on website and app per W615 | VP Communications / VP Store Ops | CEO | 30 days before closure |
| 8 | **Premises Handover & Close-Out**: Final handover to landlord: (a) remove all BuildRight fixtures, signage, and materials per lease "make-good" requirements; (b) restore premises to contractually agreed condition; (c) final walkthrough with landlord representative; (d) document condition with photos; (e) settle any outstanding rent, CAM charges, or utility bills per W118; (f) receive security deposit return; (g) close all utility accounts (electricity, water, telecom); (h) Finance closes store cost center in GL per W9 | Facilities / Finance / Legal | VP Store Ops | 1-2 weeks |

### System Touchpoints

- Store performance analytics per W67 for closure decision support
- Lease management module per W117 for termination terms
- HR separation processing per W43, W643 for employee transition
- Inventory management per W93, W22, W23, W587 for liquidation
- IT asset management per W131, W265 for equipment recovery
- Fixed asset disposal per W39
- Location Master per W254 for deactivation
- Compliance calendar per W506 for regulatory de-registration deadlines
- Customer notification module per W615 for digital channel updates
- Finance GL per W9 for cost center closure

### Pain Points / Risks

- **Lease termination penalty**: early lease termination penalties can reach 6-12 months of rent; for a PHP 500K/month lease, this is PHP 3M-6M in sunk cost; negotiating favorable exit terms is critical
- **DOLE retrenchment compliance**: if 10+ employees are retrenched at a single location, DOLE requires 30-day advance notice to both employees and DOLE Regional Office; non-compliance risks illegal dismissal case
- **Landlord "make-good" disputes**: landlords may claim the premises require restoration beyond what BuildRight considers fair wear-and-tear; disputes can delay security deposit return by months
- **Inventory liquidation value erosion**: markdown prices attract opportunistic buyers but erode margin; transferring inventory to nearby stores is better for value recovery but requires logistics coordination
- **Customer migration leakage**: not all customers from a closed store will migrate to the nearest alternative BuildRight; some will defect to competitors, permanently reducing market share
- **Employee morale impact**: store closures at one location create anxiety at nearby stores; clear communication about closure criteria and employee transfer opportunities is essential

### Staffing Implication

- **VP Store Operations**: 20-30 hours per closure on coordination and decision-making; absorbed by existing role
- **HR Manager**: 20-40 hours per closure on employee transition; absorbed by existing role with peak support from HR team
- **Legal**: 10-20 hours per closure on lease termination; absorbed by existing role
- **Finance**: 10-15 hours per closure on financial close-out; absorbed by existing role
- **No incremental headcount**; closure team assembled from existing functional roles per closure project

### Time Estimate

- Closure decision: 2-4 weeks
- Lease termination: 2-3 months
- Employee transition: 30-60 days
- Inventory liquidation: 4-8 weeks
- Asset recovery: 1-2 weeks
- Regulatory de-registration: 1-2 months
- Premises handover: 1-2 weeks
- **Total closure timeline**: 3-6 months from decision to final handover
