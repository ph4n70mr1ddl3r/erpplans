# Fleet Operations & Driver Management Workflows

> Management of company-owned delivery fleet, driver performance, route optimization, fuel efficiency, fleet accident & incident management, and driver onboarding, training & certification.
>
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W196. Route Planning & Dispatch Optimization](#w196-route-planning-dispatch-optimization)
- [W197. Driver Performance & Safety Management](#w197-driver-performance-safety-management)
- [W198. Fuel Management & Consumption Monitoring](#w198-fuel-management-consumption-monitoring)
- [W199. Fleet Telematics & Real-Time Tracking](#w199-fleet-telematics-real-time-tracking)
- [W431. LGU-Specific "Truck Ban" & Route Governance](#w431-lgu-specific-truck-ban-route-governance)
- [W653. Fleet Accident & Incident Management](#w653-fleet-accident--incident-management)
- [W654. Driver Onboarding, Training & Certification](#w654-driver-onboarding-training--certification)

---

## W196. Route Planning & Dispatch Optimization

| Field | Detail |
|---|---|
| **Trigger** | Released Home Delivery orders (W19) or Store Replenishment orders (W4) |
| **Frequency** | Daily (Morning and Evening waves) |
| **Volume** | ~115 home deliveries/DC/day; ~33 store replenishments/DC/day |
| **Owner** | Logistics Planner |
| **Participants** | Logistics Planner, DC Dispatch, Drivers, 3PL Partners |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Batching**: System aggregates all pending deliveries by zone, weight, and volume (CBM) | System | Logistics Planner | Automated |
| 2 | **Vehicle Allocation**: System recommends vehicle type (10-wheeler vs. 6-wheeler vs. small van) based on load and delivery access restrictions (e.g., "Truck Ban" zones) | System | — | Automated |
| 3 | **Optimization**: Route optimization engine calculates most efficient sequence to minimize kilometers and fuel; accounts for traffic patterns and delivery windows | System | Logistics Planner | 5 min |
| 4 | **Manifest Generation**: Finalize route; system generates Trip Manifest and Load List; assigns to Driver/Vehicle | Logistics Planner | DC Manager | 10 min |
| 5 | **Driver Briefing**: Driver receives digital manifest on mobile app; verifies load; starts trip | Driver | DC Dispatch | 15 min |

### System Touchpoints
- Route Optimization Engine integration (Step 3)
- Driver Mobile App — manifest delivery, POD capture, route navigation
- Vehicle Master (ERP) — vehicle type, capacity, availability

### Pain Points / Risks
- MMDA truck ban hours in Metro Manila restrict delivery windows and force suboptimal route timing
- LTO driver license compliance — expired licenses halt dispatch
- Philippine fuel price volatility (PHP/USD + VAT impact) erodes route cost estimates

### Staffing Implication
Daily across 4 DCs. ~115 home deliveries + ~33 store replenishments per DC per day. 1 Logistics Planner per DC (5 FTE), ~2 hours/day on routing.

### Time Estimate
~30 min/DC/day for batching, optimization, and manifest generation; driver briefing 15 min/trip.

---

## W197. Driver Performance & Safety Management

| Field | Detail |
|---|---|
| **Trigger** | New driver onboarding; or monthly performance review cycle |
| **Frequency** | Continuous monitoring; Monthly review |
| **Volume** | ~250–300 company drivers |
| **Owner** | Fleet Manager |
| **Participants** | Driver, Fleet Manager, Safety Officer, HR |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Licensing & Compliance**: System tracks Driver License expiries and professional certifications (e.g., Hazmat for paint) | System | Fleet Manager | Automated |
| 2 | **Safety Monitoring**: Telematics system logs events: Harsh braking, over-speeding, idling, and unauthorized stops | System | — | Real-time |
| 3 | **Incident Review**: Safety Officer reviews telematics alerts daily; conducts "Coaching Session" for frequent offenders | Safety Officer | — | 20 min |
| 4 | **Performance Scoring**: Monthly "Driver Scorecard" based on: On-time delivery %, fuel efficiency (km/L), and safety incidents | Fleet Manager | — | 30 min |
| 5 | **Rewards/Discipline**: High scorers eligible for "Safety Bonus"; low scorers trigger HR counseling (W72) | Fleet Manager | CHRO | Monthly |

### System Touchpoints
- Telematics / GPS provider API integration (Step 2)
- Driver Mobile App — safety alerts and coaching notifications
- HR Module (W72) — disciplinary and counseling workflows
- Fleet Dashboard — Driver Safety KPIs

### Pain Points / Risks
- LTO driver license compliance tracking — missed expiries create legal exposure
- Lalamove/Transportify competition for driver retention — gig economy poaches experienced drivers
- DOLE fatigue management regulations for drivers — maximum driving hours enforcement

### Staffing Implication
~250-300 company drivers. Monthly scorecard generation ~30 min each = ~125-150 hours/month. 1 Fleet Manager + 1 Safety Officer. Absorbed.

### Time Estimate
~30 min/driver/month for scorecard; daily incident review ~20 min/session; monthly review cycle ~3-4 hours per DC.

---

## W198. Fuel Management & Consumption Monitoring

| Field | Detail |
|---|---|
| **Trigger** | Fueling event; or end of month |
| **Frequency** | Ongoing |
| **Volume** | ~PHP 10M–15M monthly fuel spend |
| **Owner** | Fleet Accountant |
| **Participants** | Driver, Gas Station (Vendor), Fleet Accountant, Finance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Fueling**: Driver uses company Fuel Card; enters odometer reading at pump | Driver | — | 5 min |
| 2 | **Data Integration**: Fuel vendor (Shell/Petron) sends daily electronic file of all transactions | System | Fleet Accountant | Automated |
| 3 | **Reconciliation**: System matches fuel transaction to vehicle and compares odometer jump vs. fuel volume to calculate actual km/L | System | — | Automated |
| 4 | **Exception Alert**: System flags anomalies: (a) Fuel volume > Tank capacity; (b) Low km/L (potential fuel siphoning); (c) Fueling far from assigned route | System | Fleet Accountant | Real-time |
| 5 | **Investigation**: Fleet Manager investigates flagged transactions; if fraud confirmed, trigger W123 (Fraud Protocol) | Fleet Manager | — | 1 hour |
| 6 | **Payment**: Finance processes monthly fuel invoice; system allocates costs to specific vehicles and cost centers | Finance | Controller | Per W7 |

### System Touchpoints
- Fuel Card provider data integration — Shell/Petron daily electronic file (Step 2)
- Fleet Dashboard — fuel KPIs (km/L, cost-per-km, exception count)
- Integration with W123 (Fraud Protocol) for confirmed fuel siphoning cases
- Integration with W7 (AP Payment) for monthly fuel invoice processing

### Pain Points / Risks
- Philippine fuel price volatility (PHP/USD + VAT impact) — budget variances of 5-10% monthly
- Fuel siphoning and card misuse — detection relies on odometer accuracy and driver honesty
- Insurance claims for fleet accidents — fuel-related incidents complicate claim processing

### Staffing Implication
PHP 10-15M monthly fuel spend. Daily reconciliation automated. Monthly investigation ~10-15 flagged transactions × 1 hour each. 1 Fleet Accountant. Absorbed.

### Time Estimate
Daily reconciliation automated; monthly investigation ~10-15 hours; payment processing per W7.

---

## W199. Fleet Telematics & Real-Time Tracking

| Field | Detail |
|---|---|
| **Trigger** | Vehicle starts trip |
| **Frequency** | Real-time |
| **Owner** | DC Dispatch |
| **Participants** | DC Dispatch, Customer Service, Customer |
| **Volume** | Continuous tracking of ~100-150 active delivery vehicles daily |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **GPS Tracking**: System tracks vehicle location, speed, and status (moving/stopped/idle) | System | — | Real-time |
| 2 | **Dynamic ETA**: System recalculates Estimated Time of Arrival (ETA) based on live traffic; updates customer via SMS/App | System | — | Automated |
| 3 | **Geofencing**: System alerts DC Dispatch when vehicle arrives at or leaves a store/customer site; logs "Time on Site" | System | — | Automated |
| 4 | **Dispatch Dashboard**: DC Dispatch monitors all active vehicles on map; identifies delays or breakdowns | DC Dispatch | — | Continuous |
| 5 | **Maintenance Integration**: Odometer data from telematics auto-triggers "Preventive Maintenance" in W188 when thresholds reached | System | — | Automated |

### System Touchpoints
- Telematics / GPS provider API integration (Step 1)
- Customer-facing SMS/App — ETA notifications and delivery tracking
- Fleet Dashboard — live map, vehicle status, delay alerts
- Integration with W188 (Preventive Maintenance) — odometer-triggered work orders
- Integration with W196 (Route Planning) — dynamic rerouting on delays

### Pain Points / Risks
- Telematics GPS accuracy in provincial/remote areas — dead zones delay ETA updates
- MMDA truck ban hours in Metro Manila — real-time rerouting needed when ban starts
- Insurance claims for fleet accidents — telematics data required as evidence
- DOLE fatigue management regulations for drivers — telematics idle/stop data used for compliance

### Staffing Implication
Real-time monitoring. 1 DC Dispatch per shift per DC (~10 FTE across 4 DCs). Continuous monitoring absorbed into dispatch role.

### Time Estimate
Continuous monitoring during active shifts (absorbed into dispatch role); geofence alert handling ~5 min/event.

---

## W431. LGU-Specific "Truck Ban" & Route Governance

| Field | Detail |
|---|---|
| **Trigger** | Daily route planning (W196) for deliveries in Metro Manila or provincial cities with active truck bans |
| **Frequency** | Daily |
| **Volume** | ~150 delivery trips/day (DC to Store and DC to Customer) |
| **Owner** | Logistics Planner |
| **Participants** | DC Dispatch, Driver, Regional Manager, MMDA / LGU Traffic Enforcers |

### Background

Managing large-format deliveries in the Philippines involves navigating a complex web of "Truck Ban" hours. Metro Manila (MMDA) and various provincial LGUs (e.g., Cebu City, Davao City) enforce different ban hours, restricted routes, and "window hours" (e.g., 10 AM to 5 PM). Violating a truck ban results in heavy fines and vehicle impounding, which disrupts the entire supply chain.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Truck Ban Database Maintenance**: Logistics Planner updates the ERP "Truck Ban Master" with current ban hours per city, vehicle type (e.g., 6-wheeler vs. 10-wheeler), and exemption status (e.g., refrigerated or essential goods) | Logistics Planner | — | 1 hour/week |
| 2 | **Route Constraint Input**: Route optimization engine (W196) pulls active ban hours from the Master; system blocks delivery windows that fall within ban periods for specific zones | System | — | Automated |
| 3 | **Dispatch Timing**: DC Dispatch adjusts the "Release Time" for trucks to ensure they reach their destination before the morning ban starts (typically 6:00 AM) or after the afternoon ban ends | DC Dispatch | DC Manager | 10 min/trip |
| 4 | **Exemption Management**: For "Essential Relief" goods (W428), Regional Manager applies for special LGU "Truck Ban Exemptions"; system tags specific vehicles with the exemption permit number | Regional Manager | Logistics Mgr | 1 day |
| 5 | **Real-Time Diversion**: If a truck is delayed (traffic/accident) and risks being caught in the ban, DC Dispatch sends an "Immediate Stop" alert via the Driver App; Driver parks at a pre-designated "Safe Zone" until the ban lifts | DC Dispatch | Driver | 5 min |
| 6 | **Fine & Impound Handling**: In case of apprehension, Driver logs the incident in the Fleet App; Logistics Manager coordinates with the LGU/MMDA for fine payment and vehicle release | Driver / Logistics Mgr | — | 4–8 hours |

### System Touchpoints

- Truck Ban Master: repository of LGU-specific traffic rules and restricted zones (W431.1)
- Route Optimization Engine: integrates time-based road constraints into routing logic (W431.2)
- Integration with W196 (Route Planning), W199 (Telematics), and W428 (Disaster Relief)

### Pain Points / Risks

- **Ad-hoc Ban Changes**: LGUs often change ban hours or restricted routes with little notice (e.g., during "ASEAN Summit" or "Pista"), causing immediate routing failures
- **"Window Hour" Congestion**: The 10 AM to 5 PM window in Metro Manila creates a massive surge in truck traffic, often leading to gridlock that prevents trucks from finishing their deliveries before the 5 PM ban resumes
- **Impounding Delays**: If a truck carrying high-value materials (appliances/electronics) is impounded, the customer delivery is delayed by days, leading to high CSR volume and potential damage to goods

### Staffing Implication

Managed by the Logistics Planner and DC Dispatch as part of daily operations. No incremental headcount.

### Time Estimate

**Total**: Database maintenance — 1 hour/week; Route adjustment — 10 min per affected trip; **Total: ~2 hours/day cumulative effort per DC**

---

## W653. Fleet Accident & Incident Management

| Field | Detail |
|---|---|
| **Trigger** | Vehicle accident, cargo damage incident, or third-party property damage during delivery operations |
| **Frequency** | ~10–15 incidents/month across fleet |
| **Volume** | ~2–4 per week |
| **Owner** | Fleet Safety Officer |
| **Participants** | Driver, Fleet Manager, Insurance Claims Coordinator, LP Analyst, HR Business Partner (if driver injury) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Driver activates incident protocol: stops vehicle, secures scene, checks for injuries, calls emergency services if needed, notifies Fleet Manager via mobile app within 15 minutes | Driver | Fleet Safety Officer | Immediate |
| 2 | Driver collects evidence: photographs of vehicle damage, third-party vehicle/property damage, road conditions, cargo condition; obtains third-party information (name, contact, vehicle details, insurance); identifies witnesses; does NOT admit fault | Driver | Fleet Safety Officer | 30 min |
| 3 | For accidents with injuries or significant property damage: Driver files police report at nearest PNP station; obtains police blotter reference number | Driver | Fleet Safety Officer | 1–2 hours |
| 4 | Fleet Safety Officer receives incident report; classifies severity (Minor: cosmetic damage only, Moderate: functional damage, cargo affected, Major: injury, total loss, third-party claim); activates appropriate response level | Fleet Safety Officer | Fleet Manager | 30 min |
| 5 | Fleet Manager arranges: vehicle recovery/towing if undrivable, cargo salvage/transfer to backup vehicle for delivery completion, driver medical assessment if injured | Fleet Manager | Fleet Safety Officer | 2–4 hours |
| 6 | Insurance Claims Coordinator initiates insurance claim per W610: submits incident report with evidence, obtains repair estimate from accredited shop, tracks claim to settlement | Insurance Claims Coordinator | Fleet Manager | 1–2 weeks |
| 7 | Fleet Safety Officer conducts investigation: reviews telematics data (speed, braking, location), driver history, route conditions; determines root cause (driver error, vehicle failure, third-party fault, road hazard); classifies preventability | Fleet Safety Officer | Fleet Manager | 3 days |
| 8 | For preventable accidents: Fleet Manager applies progressive discipline per driver safety program (W197); assigns remedial training; adjusts driver safety score | Fleet Manager | VP Supply Chain | Per W197 |
| 9 | Monthly: Fleet Safety Officer produces incident analytics: incident rate per 100,000 km, preventability rate, cost per incident, trend by driver/route/vehicle/time; feeds driver performance dashboard (W197) | Fleet Safety Officer | Fleet Manager | 2 hours/month |

### System Touchpoints
- Fleet telematics (W199), incident reporting mobile app, insurance claims module (W610), driver management (W197), repair work order system

### Time Estimate
- Scene management: 1–2 hours; investigation: 3 days; claim resolution: 1–2 weeks

### Pain Points / Risks
- Driver panic or flight from accident scene; third-party fraud (staged accidents); evidence collection quality varies by driver composure; insurance claim processing delays in Philippine insurance market; cargo damage claims with customer impact during peak season

### Staffing Implication
- **Fleet Safety Officer**: ~2 hours/month on incident analytics + ad hoc investigation time (varies by incident frequency). Absorbed within existing safety role.
- **Fleet Manager**: per-incident response time varies; ~2–4 hours per moderate/major incident for recovery coordination. Absorbed within existing role.
- **Insurance Claims Coordinator**: ~1–2 weeks per claim tracking. Absorbed within existing insurance/finance role.

---

## W654. Driver Onboarding, Training & Certification

| Field | Detail |
|---|---|
| **Trigger** | New driver hire; annual recertification requirement; triggered by safety event requiring retraining |
| **Frequency** | ~20–30 new driver hires/year (turnover replacement); all drivers recertified annually |
| **Volume** | ~30–50 drivers (owned fleet); additional 3PL driver coordination |
| **Owner** | Fleet Safety Officer |
| **Participants** | Fleet Manager, HR Business Partner, Training Facilitator, Driver |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | HR Business Partner confirms driver hire per recruitment process (W15); verifies professional driver's license (restriction code 2 or 3 for trucks), valid medical certificate, NBI clearance, and drug test result (per COM-001) | HR Business Partner | Fleet Manager | Per W15 |
| 2 | Fleet Safety Officer conducts 2-day driver onboarding: Day 1 — company orientation, fleet policies, safety culture, incident reporting protocol (W653), drug and alcohol policy, customer service standards; Day 2 — vehicle familiarization, telematics system training (W199), mobile app operation, DC check-in/check-out procedures, fuel card usage (W198) | Fleet Safety Officer | Fleet Manager | 2 days |
| 3 | Fleet Manager assigns experienced driver mentor for 1-week ride-along program: route familiarization, LGU truck ban awareness (W431), DC and store delivery point familiarization, customer interaction coaching, live cargo handling practice | Mentor Driver | Fleet Manager | 1 week |
| 4 | Fleet Safety Officer conducts supervised driving assessment: pre-trip inspection, driving evaluation (city, highway, loading dock maneuvers), post-trip inspection, cargo securing assessment; passes/fails based on scoring rubric (minimum 80%) | Fleet Safety Officer | Fleet Manager | 0.5 day |
| 5 | For passing drivers: Fleet Manager activates driver in dispatch system (W196); assigns initial routes with mentor backup; issues fuel card, mobile device, PPE, and vehicle keys | Fleet Manager | VP Supply Chain | 0.5 day |
| 6 | Annual recertification: Fleet Safety Officer conducts refresher training (safety updates, new regulations, accident review from past year); supervised driving re-assessment; license and medical certificate renewal verification | Fleet Safety Officer | Fleet Manager | 1 day/driver |
| 7 | For post-incident retraining: Fleet Safety Officer conducts targeted remedial training based on incident root cause (W653); specialized modules: defensive driving, hazmat transport, load securing, adverse weather driving; re-assessment before return to active duty | Fleet Safety Officer | Fleet Manager | 1–2 days |

### System Touchpoints
- Fleet management module, driver qualification database, training module (W51), telematics (W199), HR module (employment records)

### Time Estimate
- New hire: 2 days classroom + 1 week ride-along + 0.5 day assessment; annual recert: 1 day; remedial: 1–2 days

### Pain Points / Risks
- Professional driver license fraud in the Philippines; mentor availability during peak season; 1-week ride-along creates temporary capacity reduction; driver training attrition (hires leaving after training investment); limited training infrastructure at DC locations

### Staffing Implication
- **Fleet Safety Officer**: primary trainer for onboarding and recertification; ~2 days per new hire + ~1 day/driver annual recert. With 20–30 new hires/year and 30–50 drivers recertifying, this represents ~70–110 training days/year. Dedicated training role within fleet operations.
- **Mentor Drivers**: 1-week ride-along per new hire; rotates among experienced drivers. Impact on normal delivery capacity during ride-along period.

---

## W799. Vehicle Acquisition, Registration, Insurance & Disposal Lifecycle Management

| Field | Detail |
|---|---|
| **Trigger** | Fleet expansion need (new store openings); vehicle end-of-life (mileage/age threshold); insurance renewal; annual registration |
| **Frequency** | Vehicle acquisition: 5-10 per year; registration: annual per vehicle; insurance: annual renewal; disposal: 3-5 per year |
| **Volume** | ~40 owned vehicles (20% of fleet); mixed fleet of owned and 3PL per model-company profile |
| **Owner** | Fleet Manager |
| **Participants** | VP Supply Chain, Finance, Procurement, Insurance Provider, LTO, External Dealer |

### Background

BuildRight operates approximately 40 owned trucks (20% of total fleet, per model-company profile) for DC-to-store delivery and inter-DC transfers. The remaining 80% of transport is handled by 3PL partners per W242. Each owned vehicle has a lifecycle from acquisition through registration, insurance, maintenance, and eventual disposal. Philippine vehicles require annual registration with the Land Transportation Office (LTO), emission testing per Clean Air Act, and comprehensive insurance including third-party liability. This workflow governs the full vehicle asset lifecycle.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Vehicle Requirement & Acquisition**: When fleet expansion is needed: (a) Fleet Manager assesses vehicle type needed (6-wheeler, 10-wheeler, wing van) based on route characteristics and volume per W196; (b) Procurement issues RFP per W224 to authorized truck dealers (Isuzu, Hino, Mitsubishi Fuso); (c) evaluate bids on: purchase price, fuel efficiency, after-sales support, parts availability in Philippines, resale value; (d) Finance approves CAPEX per W21; (e) register new vehicle in Fleet Master per W401 with all specifications, purchase date, warranty terms | Fleet Manager / Procurement | VP Supply Chain | 4-6 weeks per vehicle |
| 2 | **LTO Registration & Compliance**: All owned vehicles must be registered annually with LTO: (a) emission testing per Clean Air Act (RA 8749) at LTO-accredited testing center; (b) vehicle inspection at LTO; (c) compulsory third-party liability (CTPL) insurance; (d) LTO registration fee payment; (e) registration sticker and plate renewal; (f) system tracks registration expiry dates with 60-day advance alerts per W506; (g) vehicle cannot be operated with expired registration per Philippine law | Fleet Admin | Fleet Manager | 1-2 days per vehicle |
| 3 | **Insurance Management**: Annual fleet insurance renewal: (a) Fleet Manager reviews current coverage: comprehensive, third-party liability, cargo insurance, acts of God (typhoon, flood); (b) obtain competitive quotes from insurance providers; (c) negotiate fleet discount based on claim history per W610; (d) ensure coverage meets BuildRight cargo liability requirements; (e) register insurance policy in system per W59 with expiry alerts; (f) add new vehicles to policy; remove disposed vehicles | Fleet Manager | VP Supply Chain / Finance | 1-2 weeks annual renewal |
| 4 | **Preventive Maintenance Scheduling**: Fleet Manager schedules PM per W188 based on: (a) manufacturer-recommended intervals (mileage or time-based); (b) telematics data per W199 (actual odometer vs. PM threshold); (c) seasonal requirements (pre-typhoon inspection, post-typhoon undercarriage check); (d) safety-critical items: brakes, tires, steering, lights inspected every 10,000 km; (e) system auto-generates PM work orders when mileage threshold approaches; (f) vehicle grounded if PM overdue by >10% | Fleet Manager / Mechanic | VP Supply Chain | Per W188 schedule |
| 5 | **Vehicle Disposal**: When vehicle reaches end-of-life (typically 8-10 years or 500,000 km): (a) Fleet Manager recommends disposal based on: maintenance cost trend, reliability history, resale value projection, safety risk; (b) Finance approves disposal per W39 fixed asset disposal; (c) remove vehicle registration from LTO; (d) cancel insurance coverage; (e) sell via competitive bid to used truck dealers; (f) or trade-in with dealer for new vehicle acquisition per Step 1; (g) remove from Fleet Master per W401; (h) book gain/loss on disposal per W39 | Fleet Manager / Finance | VP Supply Chain | 2-4 weeks per vehicle |

### System Touchpoints

- Fleet Master per W401 with vehicle specifications, lifecycle dates, and cost history
- LTO registration tracking with expiry alerts per W506
- Insurance policy management per W59 with renewal alerts
- Preventive maintenance scheduling per W188 with telematics integration per W199
- Fixed Asset module per W39 for depreciation, CAPEX, and disposal accounting
- Procurement integration per W224 for vehicle acquisition bidding
- Fuel management integration per W198 for total cost of ownership tracking
- Telematics integration per W199 for odometer-based PM triggers

### Pain Points / Risks

- **LTO registration backlogs**: Philippine LTO offices often have processing backlogs; vehicles with pending registration cannot legally operate, disrupting delivery schedules
- **Emission testing failures**: older vehicles may fail emission testing, requiring engine overhaul before registration can proceed; unplanned cost and downtime
- **Insurance premium increases after claims**: fleet accident rate per W653 directly impacts insurance premiums; high claim frequency can increase premiums by 20-40%
- **Vehicle resale value depreciation**: Philippine truck resale values drop significantly after 8 years; early disposal (at 6-7 years) maximizes resale value but increases annual CAPEX
- **Parts availability for older vehicles**: manufacturers may discontinue parts for older models; maintenance costs and downtime increase as vehicles age past parts support
- **Driver abuse and vehicle damage**: driver behavior directly impacts vehicle lifespan; telematics per W199 and driver scorecard per W197 are critical for vehicle longevity

### Staffing Implication

- **Fleet Manager**: ~8-12 hours/month on vehicle lifecycle management; absorbed by existing role
- **Fleet Admin**: ~4-6 hours/month on registration and insurance paperwork; absorbed by existing admin role
- **No incremental headcount**.

### Time Estimate

- Vehicle acquisition: 4-6 weeks per vehicle
- Annual registration: 1-2 days per vehicle × 40 vehicles = 40-80 days/year
- Insurance renewal: 1-2 weeks/year (all vehicles)
- PM scheduling: per W188 (ongoing)
- Vehicle disposal: 2-4 weeks per vehicle