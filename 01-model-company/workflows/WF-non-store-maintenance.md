# Facility & Asset Maintenance (HQ & DC) Workflows

> Maintenance of non-store facilities: Distribution Centers (DCs), Head Office (HQ), and specialized DC equipment.
>
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W240. DC Facility & Warehouse Equipment Maintenance](#w240-dc-facility-warehouse-equipment-maintenance)
- [W241. HQ Office Facility & Executive Asset Maintenance](#w241-hq-office-facility-executive-asset-maintenance)
- [W242. 3PL & Logistics Partner Performance Review](#w242-3pl-logistics-partner-performance-review)
- [W243. Power of Attorney (POA) & Board Resolution Lifecycle](#w243-power-of-attorney-poa-board-resolution-lifecycle)
- [W700. Facility Condition Assessment & Capital Planning Support](#w700-facility-condition-assessment-capital-planning-support)
- [W701. Utility Infrastructure Management & Metering Operations](#w701-utility-infrastructure-management-metering-operations)
- [W808. Generator Preventive Maintenance, Fuel Management & Load Testing](#w808-generator-preventive-maintenance-fuel-management--load-testing)

---

## W240. DC Facility & Warehouse Equipment Maintenance

| Field | Detail |
|---|---|
| **Trigger** | Odometer/Hour-meter reading (Forklifts); or scheduled facility audit |
| **Frequency** | Weekly/Monthly/Quarterly |
| **Volume** | ~4 DCs, ~20 PM events/month |
| **Owner** | DC Maintenance Supervisor |
| **Participants** | DC Staff, External Technicians |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Inspection**: Weekly walk-through of DC (Racking, Lighting, Flooring, Fire Sprinklers) | Maint Supervisor | — | 2 hours |
| 2 | **Equipment PM**: Preventive Maintenance (PM) for Forklifts, Conveyors, and Dock Levelers | Technician | Maint Supervisor | 4 hours |
| 3 | **Racking Audit**: Annual structural audit of pallet racking (Philippine Seismic Code compliance) | Ext Auditor | DC Manager | 2 days |
| 4 | **Work Order**: Create repairs in W47 system for any failures | Maint Supervisor | — | 10 min |

### System Touchpoints
- WMS maintenance module (work order creation, PM scheduling)
- Digital Asset Register for DC equipment (forklifts, conveyors, dock levelers)
- Incident management module (W140) for safety-related failures
- Integration with W47 (Work Order system) for repair tracking

### Pain Points / Risks
- Philippine Seismic Code compliance for pallet racking — requires licensed structural engineer sign-off; non-compliance risks DOLE shutdown
- LGU building permit requirements for DC modifications — varying municipal ordinances cause delays
- Fire safety inspection certificate (FSIC) renewal from BFP — missed renewal halts warehouse operations

### Staffing Implication
Weekly walk-throughs at 4 DCs = ~260/year x 2 hours = ~520 hours/year. PM events monthly per DC = ~60/year x 4 hours = ~240 hours. 1 DC Maintenance Supervisor per DC (5 FTE).

### Time Estimate
Walk-through: 2 hours/DC/week; PM event: 4 hours/DC/month; Annual racking audit: 2 days/DC.

---

## W241. HQ Office Facility & Executive Asset Maintenance

| Field | Detail |
|---|---|
| **Trigger** | Employee request; or scheduled lease/utility review |
| **Frequency** | Ongoing |
| **Volume** | ~200 requests/month |
| **Owner** | HQ Facilities Manager |
| **Participants** | Office Admin, IT, Vendors |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Request Intake**: Employee submits HQ facility request (AC cooling, lighting, furniture) via service portal | Employee | — | 5 min |
| 2 | **Priority Triage**: Categorize request by urgency — Critical (safety/HVAC failure), High (executive boardroom), Normal (routine), Low (aesthetic) | Office Admin | Facilities Mgr | 10 min |
| 3 | **Vendor Dispatch**: For complex repairs (elevator, centralized AC, electrical), dispatch contracted vendor with SLA commitment | Facilities Mgr | — | 30 min |
| 4 | **Execution & Verification**: Vendor or in-house team completes repair; requestor confirms resolution | Vendor / Office Admin | Facilities Mgr | 1-4 hours |
| 5 | **SLA Tracking & Escalation**: Monitor resolution against SLA targets; escalate overdue items to COO if Critical/High exceeds 24 hours | Facilities Mgr | COO | 15 min |
| 6 | **Budget Coding**: Assign completed work order cost to requesting department's cost center; reconcile against facilities budget | Office Admin | Finance | 10 min |
| 7 | **Asset Tracking & Quarterly Deep-Clean**: Maintain register of HQ-specific assets (Boardroom AV, Gym equipment, Executive vehicles); schedule quarterly deep-clean/sanitization of pantry, restrooms, and boardrooms | Office Admin | Facilities Mgr | Ongoing |

### System Touchpoints
- Facilities service portal (ticket intake, SLA monitoring, escalation)
- Digital Asset Register for HQ assets (Boardroom AV, gym equipment, executive vehicles)
- Budget / Cost Center module for department charge-backs
- Contract Management (W62) for cleaning, security, and canteen vendor SLAs

### Pain Points / Risks
- LGU building permit requirements for HQ office renovations — municipal engineering office lead times can exceed 30 days
- Data privacy for contractor badges and visitor logs (RA 10173 — Philippine Data Privacy Act) — CCTV footage and contractor PII must be handled per NPC guidelines
- Vendor performance SLAs — cleaning and security vendors frequently miss response-time commitments

### Staffing Implication
~200 requests/month, mostly low-complexity. 1 HQ Facilities Manager + 1 Office Admin. Absorbed by existing roles.

### Time Estimate
~5-10 min per request for triage and dispatch; complex repairs 1-4 hours; quarterly deep-clean 1 day/event.

---

## W242. 3PL & Logistics Partner Performance Review

| Field | Detail |
|---|---|
| **Trigger** | Quarterly review calendar |
| **Frequency** | Quarterly |
| **Volume** | ~5–10 key logistics partners |
| **Owner** | Fleet Manager |
| **Participants** | DC Dispatch, Customer Experience, Finance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **KPI Aggregation**: Compile On-Time Delivery (OTD), Damage Rate, and Billing Accuracy for the 3PL | System | Fleet Manager | 2 hours |
| 2 | **CX Feedback**: Review customer complaints/satisfaction related to 3PL deliveries (W41) | CX Manager | — | 1 hour |
| 3 | **Review Meeting**: Present findings to 3PL executives; identify improvement areas | Fleet Manager | Supply Chain Mgr | 2 hours |
| 4 | **Rate Review**: Compare 3PL performance vs. contract rates; initiate re-negotiation if needed | Fleet Manager | — | 1 day |

### System Touchpoints
- Contract Management (W62) for 3PL rate tables and SLA terms
- Fleet Dashboard — On-Time Delivery, Damage Rate, Billing Accuracy KPIs
- Customer Experience module (W41) for delivery complaint correlation
- Integration with W52 (Fleet) for hybrid fleet vs. 3PL cost comparison

### Pain Points / Risks
- Vendor performance SLAs for 3PL partners — penalty clauses often unenforced due to lack of real-time KPI visibility
- Philippine fuel price volatility (PHP/USD + VAT) makes fixed-rate 3PL contracts risky for both parties
- Seasonal surge capacity — 3PL partners may lack trucks during Q4 (Ber months) peak

### Staffing Implication
Quarterly review of 5-10 partners. ~8 hours per review cycle. Absorbed by existing Fleet Manager.

### Time Estimate
~8 hours per quarterly review cycle (KPI aggregation + CX review + meeting + rate review).

---

## W243. Power of Attorney (POA) & Board Resolution Lifecycle

| Field | Detail |
|---|---|
| **Trigger** | Need for specific authorization (Bank, Government, Contracts) |
| **Frequency** | Ad-hoc; ~10–20 per month |
| **Volume** | ~10–20 POAs and Board Resolutions per month |
| **Owner** | Corporate Secretary |
| **Participants** | Board of Directors, Legal, Authorized Signatories |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Request**: Dept Head requests specific authority (e.g., to sign LTO documents or open bank account) | Dept Head | Legal Counsel | 15 min |
| 2 | **Drafting**: Corp Sec drafts Board Resolution or Secretary's Certificate | Corp Sec | — | 1 hour |
| 3 | **Approval**: Circulate to Board for signature (Digital or Physical) | Corp Sec | Chairman | 2 days |
| 4 | **Notarization**: Obtain notarization (Mandatory for PH legal documents) | Legal Assistant | — | 4 hours |
| 5 | **Register**: Upload scanned copy to "Authority Matrix" / POA Register; issue to requestor | Legal Assistant | — | 10 min |
| 6 | **Expiry Tracking**: Monitor expiry of specific POAs; trigger renewal 30 days before | Legal Assistant | — | Monthly |

### System Touchpoints
- Legal Document Management System (DMS) for POA/Resolution storage and versioning
- Authority Matrix module — tracks signatory scope, validity, and expiry dates
- Integration with W124 (Corp Sec) for board meeting and resolution workflows
- Integration with W52 (Fleet) for LTO-related POAs

### Pain Points / Risks
- Notarization requirements for POAs (PH-specific) — notary public availability and document re-submission cycles cause delays
- Board signature collection — directors may be overseas or unavailable; digital signature acceptance varies by bank/government agency
- POA expiry risk — missed renewals can halt time-sensitive transactions (banking, customs, LTO registrations)

### Staffing Implication
10-20 POAs/month x ~4 hours each = ~40-80 hours/month. 1 Corporate Secretary + 1 Legal Assistant. Absorbed by existing roles.

### Time Estimate
~4 hours per POA/Resolution (drafting 1 hr + board circulation 2 days + notarization 4 hrs + filing 10 min); expiry tracking ~1 hour/month.

---

## W700. Facility Condition Assessment & Capital Planning Support

| Field | Detail |
|---|---|
| **Trigger** | Annual facility assessment cycle; post-disaster damage assessment; lease renewal decision; major equipment replacement consideration |
| **Frequency** | Annual comprehensive assessment; quarterly targeted inspections; ad-hoc post-disaster |
| **Volume** | 4 DCs + HQ + 200 store leases requiring annual condition assessment |
| **Owner** | Facilities Manager |
| **Participants** | DC Maintenance Supervisors, Store Managers (lease condition reporting), External Engineering Consultant, Finance (capital planning), Real Estate Manager (lease decisions) |

### Background

BuildRight operates 4 large distribution centers (130,000 sqm total) and a headquarters office that are company-owned or long-leased, plus 200 store locations under various lease terms. The condition of these facilities directly impacts operational efficiency, safety compliance, and capital expenditure planning. This workflow provides systematic assessment of facility condition to support capital planning per W184, lease renewal decisions per W635, and safety compliance per W141.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Annual DC condition assessment**: External Engineering Consultant conducts comprehensive assessment of each DC: (a) structural condition (racking integrity, floor condition, roof/ceiling, seismic compliance per Philippine Structural Code); (b) mechanical systems (HVAC, fire suppression, plumbing, electrical); (c) building envelope (walls, doors, loading docks, dock levelers); (d) site conditions (parking, drainage, fencing, security systems); (e) rate each element on 1-5 scale (1=Critical/Replace, 2=Poor/Repair within 1 year, 3=Fair/Monitor, 4=Good, 5=Excellent); (f) estimate remaining useful life and replacement cost for each element | External Engineering Consultant | Facilities Manager | 2-3 days per DC |
| 2 | **HQ office condition assessment**: Facilities Manager conducts annual assessment of HQ: (a) building systems (elevator, centralized AC, electrical, plumbing, fire suppression); (b) office infrastructure (carpeting, ceiling, lighting, partition walls); (c) specialized areas (server room, boardroom AV, cafeteria equipment); (d) rate each element and estimate replacement cost | Facilities Manager | VP Operations | 1 day |
| 3 | **Store lease condition reporting**: Store Managers complete annual lease condition report: (a) general condition of leased premises (flooring, walls, ceiling, lighting, signage); (b) landlord-provided systems condition (HVAC, plumbing, electrical per lease terms); (c) BuildRight-installed fixtures condition (racking, display units, POS counter, paint mixing station); (d) identify items requiring landlord repair vs. BuildRight maintenance per lease terms; (e) rate overall facility condition 1-5; (f) attach photos of significant issues | Store Manager | Facilities Manager | 2-3 hours per store |
| 4 | **Capital planning input**: Facilities Manager consolidates all assessment data into capital planning input for Finance: (a) items rated 1 (Critical): immediate capex request per W184 — structural repairs, safety-critical system replacements; (b) items rated 2 (Poor): include in next year's capex budget with estimated cost and timeline; (c) items rated 3 (Fair): include in 2-3 year capital forecast; (d) items rated 4-5: routine maintenance per W240/W241; (e) total estimated capital requirement by year for 3-year rolling forecast | Facilities Manager | CFO | 1 week |
| 5 | **Lease renewal decision support**: for stores approaching lease expiry: (a) Facilities Manager provides facility condition assessment to Real Estate Manager; (b) if condition is poor and landlord unwilling to invest: factor into lease renewal negotiation or relocation decision; (c) if condition is good: support lease renewal with planned maintenance schedule; (d) estimate BuildRight's leasehold improvement investment at current location vs. cost of new location buildout per W223 | Facilities Manager | Real Estate Manager | Per lease renewal cycle |
| 6 | **Post-disaster damage assessment**: after significant natural disaster (typhoon, earthquake, flood): (a) Facilities Manager dispatches assessment team to affected locations within 24-48 hours; (b) rapid damage assessment: structural safety (can building be occupied?), equipment damage (what needs replacement?), inventory damage per W91; (c) insurance claim documentation per W184; (d) temporary operational plan per W576 typhoon protocol and W685 BC plan | Facilities Manager / External Engineer | VP Operations | 1-3 days per affected location |

### System Touchpoints

- Facility condition assessment database with rating history
- Capex planning integration per W184
- Lease management integration per W635
- Maintenance management per W240/W241
- Photo documentation per W255
- Insurance claim integration
- BC plan integration per W685

### Pain Points / Risks

- **Assessment coverage vs. cost**: comprehensive engineering assessment of 4 DCs and HQ is expensive (PHP 2-5M annually for external consultants); store-level assessments rely on Store Manager self-reporting which may lack technical accuracy
- **Hidden deterioration**: some building systems (embedded plumbing, electrical wiring behind walls, roof membrane under membrane) cannot be visually assessed and may fail without warning
- **Philippine seismic compliance**: DCs in Mindanao (Davao) are in active seismic zones; structural compliance assessment requires licensed structural engineer — limited availability in provincial areas
- **Lease incentive misalignment**: landlords have limited incentive to invest in improvements for leased properties, leading to gradual deterioration; BuildRight must negotiate maintenance clauses effectively

### Staffing Implication

- **Facilities Manager**: ~2-3 weeks/year on assessment coordination and capital planning input. Absorbed within existing role.
- **External Engineering Consultant**: ~8-12 days/year for DC assessments.
- **Store Managers**: ~2-3 hours/year per store on lease condition reporting = ~400-600 hours total.
- **No incremental headcount**.

### Time Estimate

- DC assessment: 2-3 days per DC (4 DCs = 8-12 days)
- HQ assessment: 1 day
- Store lease reports: 2-3 hours per store (200 stores)
- Capital planning consolidation: 1 week
- Post-disaster assessment: 1-3 days per affected location

---

## W701. Utility Infrastructure Management & Metering Operations

| Field | Detail |
|---|---|
| **Trigger** | Monthly utility billing; meter reading cycle; utility rate change notification; infrastructure upgrade project |
| **Frequency** | Monthly billing review; quarterly rate analysis; annual infrastructure review |
| **Volume** | ~205 utility accounts (electricity, water, internet/telecom) across 200 stores, 4 DCs, and HQ |
| **Owner** | Facilities Manager (DCs/HQ); Finance (utility payments) |
| **Participants** | Store Managers (meter readings), AP Clerks (utility payments per W7), Sustainability Lead (energy monitoring per W692), IT (telecom/internet), Utility Providers |

### Background

BuildRight manages ~205 utility connections across its locations: electricity (primary cost driver — MERALCO, Davao Light, VECO, CEBECO, and other regional electric cooperatives), water (local water districts), and internet/telecom (PLDT, Globe, and regional providers). This workflow manages the operational aspects of utility infrastructure: meter reading, billing verification, rate analysis, connection management for new/closed locations, and infrastructure upgrade coordination.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Monthly meter reading & billing verification**: (a) for locations with smart meters (DCs, HQ): system captures automated readings; (b) for locations with manual meters: Store Manager submits monthly meter reading via mobile app by billing cycle cutoff; (c) AP Clerk receives utility bill per W7 and cross-references: meter reading vs. billed consumption, rate per kWh vs. contracted rate, demand charges vs. transformer capacity, any penalties (late payment, power factor penalties); (d) flag bills with >20% variance from prior month for investigation | AP Clerk / Store Manager | Finance Manager | 15-30 min per location/month |
| 2 | **Rate analysis & optimization**: quarterly, Finance reviews utility rates across all locations: (a) compare electricity rates across electric cooperatives (significant variation: MERALCO PHP 11-12/kWh vs. provincial co-ops PHP 8-10/kWh); (b) evaluate time-of-use (TOU) rate opportunities for DCs (shift energy-intensive operations to off-peak); (c) verify demand charge optimization: ensure contracted transformer capacity matches actual peak demand (over-contracted = wasted cost, under-contracted = penalties); (d) evaluate competitive retail electricity supply options per Electric Power Industry Reform Act (EPIRA) where available | Finance Analyst | CFO | 1 day/quarter |
| 3 | **New location utility connection**: for new store openings per W702: (a) Facilities Manager initiates utility connection applications 3-6 months before opening: electricity (load calculation, transformer sizing, application to local electric cooperative), water (application to local water district), internet/telecom (application to PLDT/Globe); (b) track application status; (c) coordinate electrical inspection and meter installation; (d) for DCs: coordinate high-voltage connection with NGCP or distribution utility | Facilities Manager | VP Operations | 3-6 months lead time per new location |
| 4 | **Location closure utility disconnection**: for store closures per W703: (a) Facilities Manager initiates utility disconnection and final billing; (b) ensure final meter reading is captured; (c) settle outstanding utility balances before lease handover; (d) recover utility deposits from providers; (e) ensure no ongoing utility charges after location vacated | Facilities Manager | Finance Manager | 1-2 months per closure |
| 5 | **Infrastructure upgrade coordination**: when utility infrastructure requires upgrade: (a) transformer upgrade (load increase due to additional equipment — paint mixing station, expanded refrigeration); (b) electrical panel and wiring upgrade (for safety per BFP requirements); (c) backup generator installation (for business continuity per W685); (d) solar panel installation per W173; (e) Facilities Manager coordinates with utility provider and licensed electrical engineer; submits capex request per W184 | Facilities Manager | VP Operations | Varies by project |
| 6 | **Annual utility contract review**: Finance reviews all utility contracts: (a) electricity supply agreements (review terms, compare market rates, negotiate renewal); (b) internet/telecom contracts (review bandwidth adequacy vs. POS and ecommerce transaction growth per data-volumes-and-integrations.md); (c) water supply agreements; (d) aggregate utility spend analysis: total spend by utility type, spend per location, year-over-year comparison | Finance Analyst | CFO | 2-3 days/year |

### System Touchpoints

- Smart meter data integration (DCs and HQ)
- Mobile app for manual meter reading submission
- AP utility invoice matching per W7
- Utility rate benchmarking dashboard
- New location project tracking per W702
- Closure process tracking per W703
- Capex request integration per W184
- Energy monitoring integration per W692
- ESG reporting integration per W192/W692

### Pain Points / Risks

- **Electric cooperative reliability**: provincial locations served by electric cooperatives experience more frequent and longer outages than MERALCO-served Metro Manila locations; backup generator per W470 essential
- **New connection lead times**: utility connection applications for new store locations (especially in provincial areas) can take 3-6 months; delays impact store opening schedule per W702
- **Rate volatility**: Philippine electricity rates fluctuate monthly (generation charge, transmission charge, system loss charge components); budget forecasting requires buffer for rate increases
- **Deposit recovery**: utility providers require deposits (often 2-3 months estimated billing); recovering deposits upon location closure can take 6-12 months

### Staffing Implication

- **Facilities Manager**: ~6-8 hours/month on utility management. Absorbed within existing role.
- **AP Clerks**: ~15-30 min per location per month on billing verification = ~50-100 hours/month for all 205 locations. Absorbed within existing AP team.
- **Finance Analyst**: ~1 day/quarter on rate analysis + 2-3 days/year on contract review. Absorbed within existing role.
- **No incremental headcount**.

### Time Estimate

- Monthly billing verification: 15-30 min per location
- Quarterly rate analysis: 1 day
- New connection: 3-6 months lead time
- Closure disconnection: 1-2 months
- Annual contract review: 2-3 days

---

## W808. Generator Preventive Maintenance, Fuel Management & Load Testing

| Field | Detail |
|---|---|
| **Trigger** | Preventive maintenance schedule (monthly, quarterly, annual); rotational brownout requiring generator activation; post-typhoon inspection; fuel level monitoring |
| **Frequency** | Monthly visual inspection; quarterly load testing; annual full service; fuel top-up per consumption |
| **Volume** | 200 stores + 4 DCs + HQ = ~205 generator sets; estimated 50-200 running hours/year per generator depending on location brownout frequency |
| **Owner** | Facilities Manager |
| **Participants** | Generator Service Technician, DC/Store Manager, Fuel Supplier, Finance, Safety Officer |

### Background

Philippine electrical grid reliability varies significantly by region. Rotational brownouts (scheduled power outages) are common in Visayas and Mindanao, and unscheduled outages occur nationwide during typhoon season. BuildRight's 200 stores and 4 DCs require backup power for: POS operations (minimum 2 hours to complete transactions), refrigerated/temperature-sensitive goods per W492 at DCs, security systems per W797, and emergency lighting per W806. Generator sets (typically 50-100 kVA for stores, 500-1000 kVA for DCs) are critical infrastructure. This workflow governs generator preventive maintenance, fuel management, and load testing to ensure reliable backup power.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Monthly Visual Inspection**: Facilities Manager or designated store/DC staff conducts monthly inspection: (a) check engine oil level and condition; (b) check coolant level; (c) check battery voltage and terminal connections; (d) check fuel level in day tank; (e) inspect for leaks (oil, coolant, fuel); (f) check belt condition and tension; (g) verify control panel shows "Ready" status with no fault indicators; (h) run generator for 15-30 minutes under no-load to verify startup; (i) log inspection results and runtime hours in maintenance system per W400 | Store/DC Staff | Facilities Manager | 30-45 min/month per generator |
| 2 | **Fuel Management**: Facilities Manager monitors fuel levels and quality: (a) maintain minimum fuel level for 8-hour continuous operation (per POS offline requirement per W535); (b) fuel top-up schedule: monthly for high-brownout locations (Visayas, Mindanao), quarterly for reliable-grid locations (Metro Manila); (c) diesel fuel has 6-12 month shelf life: implement fuel polishing (filtration) program for generators with low usage to prevent microbial growth and degradation; (d) fuel consumption tracked per generator per W198 for cost allocation; (e) emergency fuel delivery agreement with local supplier for extended outages (typhoon) | Facilities Manager / Fuel Supplier | VP Operations | 1-2 hours/month fuel logistics |
| 3 | **Quarterly Load Bank Testing**: Generator service technician conducts quarterly load bank test: (a) connect external load bank to generator; (b) run generator at 25%, 50%, 75%, and 100% rated load for minimum 30 minutes each step; (c) record voltage, frequency, amperage, and exhaust temperature at each load level; (d) verify automatic transfer switch (ATS) operation: simulate power failure, verify generator starts within 10 seconds and ATS transfers load; (e) verify transfer back to utility power when restored; (f) compare performance to manufacturer specifications; (g) log results in maintenance system | Generator Service Technician | Facilities Manager | 2-4 hours per generator |
| 4 | **Annual Full Service**: Generator service technician conducts annual major service: (a) change engine oil and oil filter; (b) replace fuel filter(s); (c) replace air filter(s); (d) inspect and adjust valve clearance; (e) inspect and clean fuel injectors; (f) test battery under load and replace if below 80% capacity; (g) inspect alternator and connections; (h) inspect and clean ATS contacts; (i) update service log in asset maintenance record per W400; (j) estimate remaining useful life based on total runtime hours and condition | Generator Service Technician | Facilities Manager | 4-8 hours per generator |
| 5 | **Post-Event Inspection**: After extended generator run (brownout >4 hours, typhoon outage): (a) inspect engine for abnormal wear (oil consumption, coolant loss); (b) check exhaust system for damage or leaks; (c) refuel to minimum level per Step 2; (d) log runtime hours and any anomalies; (e) if generator ran >24 hours continuously: schedule abbreviated service (oil check, coolant check, belt inspection) before returning to normal standby | Store/DC Staff / Technician | Facilities Manager | 1-2 hours per event |
| 6 | **Generator Replacement Planning**: Facilities Manager tracks generator lifecycle: (a) typical generator lifespan: 15,000-20,000 runtime hours or 15-20 years; (b) track runtime hours per W400 EAM master; (c) generators approaching end-of-life: include in annual CAPEX budget per W21 for replacement; (d) consider upgrade: larger capacity for expanding stores, quieter models for residential-adjacent stores, emission-compliant models per Clean Air Act per W799 | Facilities Manager | VP Operations | Part of annual CAPEX planning |

### System Touchpoints

- Asset maintenance record per W400 with generator specifications and runtime tracking
- PM scheduling module with monthly/quarterly/annual task generation
- Fuel management tracking per W198 for consumption and cost monitoring
- Compliance calendar per W506 for testing schedule tracking
- Service log with technician certification verification per W655
- CAPEX budget integration per W21 for replacement planning
- Utility monitoring per W701 for brownout correlation

### Pain Points / Risks

- **Generator failure during extended outage**: if generator fails during a typhoon-induced multi-day power outage, the store cannot operate POS (after 8-hour offline battery depletes per W535), temperature-sensitive inventory at DC may spoil per W492, and security systems go offline per W797
- **Diesel fuel degradation in low-usage generators**: stores in reliable-grid locations (Metro Manila) may rarely use generators, causing diesel to degrade; fuel polishing adds PHP 5,000-10,000 per event
- **Generator noise complaints**: generators running during brownouts in residential-adjacent stores may generate community complaints per W209; LGU may impose noise restrictions limiting operating hours
- **ATS failure**: automatic transfer switch is the most common failure point; if ATS fails to detect power loss and start generator, backup power is unavailable despite generator being functional
- **Service technician availability during typhoon**: after major typhoons, all generator service technicians are fully booked; BuildRight must have framework agreements with multiple service providers
- **Fuel supply disruption during typhoon**: diesel supply may be disrupted after major typhoons when roads are blocked and fuel stations are without power; pre-typhoon fuel top-up is critical

### Staffing Implication

- **Facilities Manager**: ~4-6 hours/month on generator fleet management across all locations; absorbed by existing role
- **Store/DC Staff**: ~30-45 min/month per location on visual inspection; absorbed by existing maintenance routine
- **Generator Service Technician**: outsourced service; ~PHP 5,000-15,000 per quarterly load test per generator × 205 generators = significant annual cost; framework agreement with national service provider
- **No incremental BuildRight headcount**.

### Time Estimate

- Monthly inspection: 30-45 min per generator
- Fuel management: 1-2 hours/month
- Quarterly load test: 2-4 hours per generator
- Annual full service: 4-8 hours per generator
- Post-event inspection: 1-2 hours per event
- Generator replacement planning: part of annual CAPEX cycle
