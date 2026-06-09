# Business Continuity & Disaster Recovery Workflows

> Workflows governing emergency preparedness, disaster response, business continuity activation, IT disaster recovery, and post-disaster restoration across all BuildRight Depot operations. These workflows address the Philippines' high exposure to typhoons (average 20 per year), earthquakes (Pacific Ring of Fire), flooding, volcanic activity, and pandemic risks — ensuring operational resilience for 200 stores, 4 distribution centers, and headquarters in Davao City.

Back to [Workflow Index](README.md)

---

## Workflows in This Domain

| Workflow | Name | Criticality |
|---|---|---|
| W847 | Business Continuity Plan Annual Review & Update | Tier 2 |
| W848 | Typhoon & Natural Disaster Store Emergency Protocol & Response | Tier 1 |
| W849 | IT Disaster Recovery Site Activation & Failover Execution | Tier 1 |
| W850 | Store Emergency Closure & Reopening Procedure | Tier 1 |
| W851 | Critical System Recovery & Service Restoration | Tier 1 |
| W852 | Supply Chain Disruption Business Impact Assessment & Recovery | Tier 2 |
| W853 | Business Continuity Plan Tabletop Exercise & Drill Execution | Tier 3 |
| W854 | Pandemic/Epidemic Business Continuity Activation & Operations | Tier 2 |
| W855 | Communication Tree Activation & Crisis Communication Management | Tier 1 |
| W856 | Post-Incident Review, Lessons Learned & Plan Update | Tier 2 |

---

## W847. Business Continuity Plan Annual Review & Update

| Field | Detail |
|---|---|
| **Trigger** | Scheduled — annual (Q1 each year); or ad-hoc triggered by material organizational change (new store format, DC addition, IT platform migration) |
| **Frequency** | Annual formal review; quarterly interim updates for material changes |
| **Volume** | 1 comprehensive plan revision per year covering all 205 locations + HQ |
| **Owner** | Business Continuity Manager / VP Operations |
| **Participants** | IT Director, Finance VP, HR Director, Supply Chain Director, LP Director, Legal Counsel, Department Heads |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Distribute BCP self-assessment questionnaire to all department heads — assess current recovery capabilities, identify new single points of failure, validate RTO/RPO targets, and confirm contact lists | BC Manager | VP Operations | 1 week (elapsed) |
| 2 | Conduct business impact analysis (BIA) update — reassess critical business processes, maximum tolerable downtime, financial impact per hour of outage, and interdependency map for all 5 legal entities | BC Manager | VP Operations | 2 weeks (elapsed) |
| 3 | Review and update IT disaster recovery plan — verify DR site readiness (Clark DC for Luzon, Cebu DC for Visayas, Davao DC for Mindanao), test data replication integrity, update system inventory and recovery sequences | IT Director | VP Operations | 1 week |
| 4 | Update store emergency response procedures — incorporate lessons from prior year incidents, update emergency contact directories (PNP, BFP, Red Cross, LGU), verify emergency supply stock levels | BC Manager | VP Operations | 1 week |
| 5 | Validate communication tree — update all-staff contact database, test SMS blast system, verify satellite phone inventory for areas with unreliable cellular coverage | HR Director | VP Operations | 3 days |
| 6 | Present updated BCP to Executive Committee for approval — key changes, cost implications, identified gaps, and investment recommendations | BC Manager | CEO | 2 hours |
| 7 | Distribute updated BCP materials — digital copies to all Store Managers, physical emergency binders to all 200 stores and 4 DCs, and updated intranet portal | BC Manager | VP Operations | 1 week |

### System Touchpoints
- **ERP Document Management** — BCP version control, distribution tracking
- **HR System** — employee contact database, communication tree
- **IT DR Platform** — replication status dashboard, DR site health monitoring
- **Communication Platform** — SMS blast system, satellite phone inventory
- **BI Dashboard** — prior year incident summary, recovery time actuals vs. targets

### Pain Points / Risks
- BCP review is often deprioritized during peak business periods (Q4 holiday season)
- Store Manager turnover means emergency binder holders may not be current
- IT DR testing is expensive and requires weekend downtime; may be skipped to avoid sales impact
- Philippine telecom infrastructure is vulnerable during disasters — backup channels essential
- Insurance coverage gaps may emerge between annual reviews as operations expand

### Staffing Implication
- 1 FTE Business Continuity Manager (reports to VP Operations)
- Department Heads: ~20 hours each for annual self-assessment
- IT Team: ~40 hours for DR plan update and testing
- External consultant: engaged every 2 years for independent BCP assessment

### Time Estimate
- BC Manager: ~160 hours over 6 weeks (annual)
- Department Heads: ~20 hours each × 15 departments = 300 hours
- IT Team: ~40 hours for DR review
- **Total annual effort: ~500 person-hours**

---

## W848. Typhoon & Natural Disaster Store Emergency Protocol & Response

| Field | Detail |
|---|---|
| **Trigger** | PAGASA typhoon warning Signal No. 2 or above in store's area; earthquake intensity ≥ V (PHIVOLCS scale); or LGU mandatory evacuation order |
| **Frequency** | Estimated 5–8 activations per year across the chain (Philippines averages 20 typhoons/year; not all affect BuildRight locations) |
| **Volume** | Each activation may affect 20–80 stores depending on typhoon path; DC activations average 2–3 per year |
| **Owner** | VP Operations / Regional Operations Director |
| **Participants** | Store Manager, DC Manager, LP Officer, IT Security, HR Director, BC Manager, External Emergency Services |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Activate disaster monitoring — BC Manager tracks PAGASA bulletins every 3 hours; classify stores by risk zone (direct path, peripheral, minimal); pre-position emergency response resources | BC Manager | VP Operations | Continuous (from Signal No. 1) |
| 2 | Issue pre-emptive store advisory (at Signal No. 1) — Store Managers activate preparedness checklist: secure outdoor merchandise (lumber, garden center), sandbag entrances in flood-prone locations, verify generator fuel and emergency supplies | Store Manager | Regional Ops Director | 4 hours |
| 3 | Execute controlled store closure (at Signal No. 2) — complete all customer transactions, secure cash in safe, power down non-essential equipment, deploy window protection, activate security alarm, send staff home with safety advisory | Store Manager | VP Operations | 2 hours |
| 4 | DC emergency protocol — secure all inventory above flood level, activate backup power, secure dock doors, protect hazardous materials, maintain skeleton crew if safe to do so | DC Manager | Supply Chain Director | 4 hours |
| 5 | HQ crisis team activation — establish situation room, activate communication tree (W855), coordinate with all affected stores/DCs, liaise with LGU emergency management | VP Operations | CEO | Continuous |
| 6 | Post-disaster rapid damage assessment (within 24 hours of all-clear) — Store Manager or designated key holder conducts site visit, photographs damage, assesses structural integrity, inventory loss, and equipment condition | Store Manager / LP Officer | VP Operations | 2–4 hours per store |
| 7 | Submit damage report and insurance claim trigger — compile damage assessment, inventory loss estimate, and business interruption impact; notify Insurance Coordinator to initiate claim (per W876) | BC Manager | Finance VP | 4 hours |
| 8 | Execute store reopening (see W850) — prioritize based on structural safety, inventory availability, staff safety, and community need (BuildRight often serves as recovery supply hub) | VP Operations | CEO | 1–3 days per store |

### System Touchpoints
- **PAGASA Integration** — automated weather alert ingestion and store risk mapping
- **ERP Communication Module** — mass notification, store status tracking, two-way check-in
- **LP/Security System** — alarm monitoring during closure, remote CCTV access
- **Insurance Module** — claim initiation, damage documentation, loss estimation
- **HR System** — employee safety check-in, staff location tracking
- **Finance Module** — business interruption loss calculation, emergency expense tracking

### Pain Points / Risks
- PAGASA forecasts can change rapidly; premature closure loses sales, delayed closure endangers staff
- Staff may be unable to report for post-disaster assessment due to personal property damage or flooding
- Looters target closed retail stores during disasters — security patrols may be needed
- Structural damage assessment requires licensed engineer; availability is limited after major disasters
- Communication infrastructure (cell towers) may be down — satellite phone backup is essential but expensive
- Supply chain for recovery materials (lumber, roofing, hardware) spikes immediately after disaster — pricing and allocation challenges

### Staffing Implication
- BC Manager: full-time during activation (may last 3–7 days)
- VP Operations: 50% of time during activation
- Store Managers: full-time during closure and reopening
- External: structural engineer on retainer for post-disaster assessment

### Time Estimate
- Per activation: ~40–60 person-hours per affected store over 3–7 days
- **Annual estimate: 6 activations × 50 stores avg × 50 hours = 15,000 person-hours/year**

---

## W849. IT Disaster Recovery Site Activation & Failover Execution

| Field | Detail |
|---|---|
| **Trigger** | Primary data center outage (Davao HQ); or pre-emptive failover before major disaster (Signal No. 3+ in Davao) |
| **Frequency** | Target: never (preventive); actual: estimated 0–2 real activations per year |
| **Volume** | 1 failover event affects entire chain (all 200 stores, 4 DCs, ecommerce, all systems) |
| **Owner** | IT Director |
| **Participants** | IT Infrastructure Team, Database Administrator, Network Engineer, Application Support, BC Manager, VP Operations |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Declare disaster — IT Director confirms primary site failure or pre-emptive trigger; obtain CEO/VP Operations authorization for DR activation | IT Director | CEO | 15 min |
| 2 | Activate DR communication — notify all IT staff, Store Managers (via backup communication channel), and BC Manager; switch to satellite/backup network if primary network is affected | IT Director | VP Operations | 30 min |
| 3 | Execute failover sequence (automated runbook) — (a) DNS switchover to DR site (Clark or Cebu), (b) promote DR database replicas to primary, (c) activate application servers at DR site, (d) redirect POS terminal connections, (e) re-establish ecommerce endpoint | IT Infrastructure Team | IT Director | 30–60 min (target RTO: 1 hour) |
| 4 | Validate system health — run automated smoke tests for all critical systems (POS, WMS, ecommerce, finance, HR); verify data integrity against last replication checkpoint (target RPO: 15 minutes) | Database Administrator | IT Director | 30 min |
| 5 | Notify business users — all-clear communication to Store Managers that systems are available; provide reconnection instructions for POS terminals | IT Director | VP Operations | 15 min |
| 6 | Monitor DR site performance — continuous monitoring for 72 hours; watch for capacity constraints, latency issues, and data consistency anomalies | IT Infrastructure Team | IT Director | Continuous (72 hours) |
| 7 | Plan and execute failback — once primary site is restored, schedule planned failback during low-traffic window; replicate DR data back to primary; validate and switch | IT Infrastructure Team | IT Director | 4–8 hours (planned weekend) |

### System Touchpoints
- **DR Site Infrastructure** — standby servers, replicated storage, network failover equipment
- **DNS/CDN** — traffic redirection, geographic failover rules
- **Database Replication** — synchronous (critical) and asynchronous (non-critical) replication
- **POS System** — automatic reconnection to DR endpoint
- **Ecommerce Platform** — CDN-based failover, session persistence
- **Monitoring Platform** — system health dashboard, automated alerting

### Pain Points / Risks
- RPO of 15 minutes means up to 15 minutes of transaction data may be lost; manual reconciliation required for affected transactions
- POS terminal reconnection may require manual intervention at older stores with legacy network equipment
- DR site capacity may not handle full peak load — priority tier system needed (POS > ecommerce > WMS > analytics)
- Failback is riskier than failover — must be carefully planned and tested
- Annual DR testing cost: ~PHP 2–3 million (weekend testing window, external consultant, staff overtime)

### Staffing Implication
- IT Infrastructure Team: 5 FTE during activation (24-hour rotation)
- Database Administrator: 2 FTE during activation
- 1 DR Site Manager (Cebu or Clark)
- External DR consultant: annual testing engagement

### Time Estimate
- Failover execution: 1–2 hours
- Validation: 30 min
- Monitoring: 72 hours (continuous, 5-person rotation)
- Failback: 4–8 hours (planned)
- **Per activation: ~200 person-hours over 72 hours**

---

## W850. Store Emergency Closure & Reopening Procedure

| Field | Detail |
|---|---|
| **Trigger** | Natural disaster (W848), civil disturbance, power outage > 4 hours, structural concern, or government-mandated closure |
| **Frequency** | Estimated 5–10 closures per store per year (most are weather-related half-day closures) |
| **Volume** | ~1,000–2,000 closure events per year chain-wide |
| **Owner** | Store Manager |
| **Participants** | Regional Operations Director, LP Officer, IT Helpdesk, HR, BC Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Receive and validate closure authorization — VP Operations or Regional Director issues closure directive; Store Manager confirms with regional office; log closure reason and expected duration | Store Manager | Regional Ops Director | 15 min |
| 2 | Execute in-store closure procedure — (a) announce last call to customers, (b) complete all pending POS transactions, (c) reconcile cash drawers and secure in safe, (d) power down non-essential systems per shutdown checklist, (e) secure all entrances, (f) activate security alarm, (g) verify all staff have safe transport home | Store Manager | Regional Ops Director | 1–2 hours |
| 3 | Submit closure report to regional office — store ID, closure time, reason, estimated reopening, staff headcount confirmed safe, cash secure status, and any known damage | Store Manager | Regional Ops Director | 15 min |
| 4 | During closure: maintain remote monitoring — CCTV remote access, alarm system monitoring, LP coordination with security agency for physical patrol if warranted | LP Officer | LP Manager (Regional) | Continuous |
| 5 | Reopening assessment — Store Manager or designated key holder conducts pre-reopening inspection: structural safety, electrical safety, water damage, inventory condition, POS/system functionality, staff availability | Store Manager | Regional Ops Director | 2–4 hours |
| 6 | Execute reopening — (a) restore systems (POS startup, network verification), (b) cash drawer opening and float distribution, (c) brief staff on any modified procedures, (d) restock damaged/displaced merchandise, (e) reopen to customers | Store Manager | Regional Ops Director | 2–3 hours |
| 7 | Submit reopening report — time opened, damage summary (if any), sales impact estimate, and any follow-up actions required | Store Manager | Regional Ops Director | 15 min |

### System Touchpoints
- **ERP Store Operations Module** — closure/reopening status tracking, notification workflow
- **POS System** — shutdown/restart procedure, transaction finalization
- **Security/Alarm System** — remote monitoring, alarm activation/deactivation
- **CCTV System** — remote access for closure monitoring
- **Communication Platform** — staff notification, regional reporting
- **HR System** — staff safety check-in, absence logging

### Pain Points / Risks
- Closure decision timing is critical — too early loses sales, too late endangers staff
- Staff may be personally affected by same disaster; availability for reopening is unpredictable
- Power restoration timeline from utility company is uncertain — generator fuel must be conserved
- Inventory spoilage (garden center plants, mixed paint) increases with closure duration
- Customer dissatisfaction from unexpected closure; proactive communication is essential but difficult when telecom is affected
- Insurance claim documentation must begin during closure — competing priorities for Store Manager

### Staffing Implication
- Store Manager: full-time during closure and reopening
- Regional Operations Director: oversees 30–40 store closures during regional events
- LP Officer: remote monitoring during closure

### Time Estimate
- Planned closure: 1–2 hours + reopening: 2–3 hours = ~4–5 hours per event
- **Annual estimate: 1,500 events × 5 hours = 7,500 person-hours/year**

---

## W851. Critical System Recovery & Service Restoration

| Field | Detail |
|---|---|
| **Trigger** | System outage affecting critical business process — POS system down > 15 min, WMS unavailable > 30 min, ecommerce platform down > 30 min, or ERP core unavailable > 1 hour |
| **Frequency** | Estimated 2–4 critical outages per month across the chain |
| **Volume** | ~25–50 critical system recovery events per year; most resolved within SLA |
| **Owner** | IT Director / IT Operations Manager |
| **Participants** | IT Infrastructure Team, Application Support, Database Administrator, Store Manager (if POS-related), Business Process Owner |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Incident detection and classification — automated monitoring alert or user report; classify severity: P1 (chain-wide outage), P2 (regional/multi-store), P3 (single store/system); notify appropriate response team | IT Operations | IT Director | 5 min |
| 2 | Activate incident response team — for P1: full infrastructure team + IT Director; for P2: on-call engineer + application support; for P3: helpdesk + store IT contact | IT Operations | IT Director | 10 min |
| 3 | Execute recovery procedure from runbook — follow documented recovery steps for affected system (server restart, failover to standby, database recovery, network rerouting); document actions taken in incident log | IT Infrastructure Team | IT Director | 15–60 min (target by severity) |
| 4 | Validate recovery — confirm system functionality via automated smoke test and user acceptance; verify data integrity (no transaction loss); check dependent systems for cascading impact | Application Support | IT Director | 15–30 min |
| 5 | Communicate status updates — provide regular updates to affected business users (every 15 min for P1, every 30 min for P2, hourly for P3); issue all-clear when resolved | IT Operations | IT Director | 5 min per update |
| 6 | Post-incident analysis — for P1 and P2: conduct root cause analysis within 48 hours; document findings, corrective actions, and preventive measures; update runbook if needed | IT Infrastructure Team | IT Director | 2–4 hours |
| 7 | Track SLA compliance — log incident start time, resolution time, and SLA target; report to IT Director monthly; escalate recurring issues for infrastructure investment | IT Operations | IT Director | 30 min per incident |

### System Touchpoints
- **IT Monitoring Platform** — automated alerting, system health dashboard, SLA tracking
- **ITSM (IT Service Management)** — incident logging, runbook access, escalation workflow
- **ERP System** — recovery target, data integrity validation
- **POS System** — offline mode fallback, transaction queue, resynchronization
- **Communication Platform** — status update distribution, stakeholder notification

### Pain Points / Risks
- POS offline mode can store transactions locally for up to 4 hours but requires resync — risk of data loss if power failure corrupts local storage
- WMS downtime at DCs halts all outbound shipments — cascading delay to store replenishment
- Ecommerce downtime directly impacts revenue and customer satisfaction; social media amplifies outage complaints
- Root cause analysis for intermittent issues is time-consuming and may not yield definitive findings
- Aging infrastructure at older stores increases failure rate — modernization budget constraints

### Staffing Implication
- IT Operations: 24/7 on-call rotation (3 shifts × 2 engineers = 6 FTE)
- Application Support: 2 FTE during business hours, 1 on-call after hours
- IT Director: escalation point for P1/P2 incidents

### Time Estimate
- P1 incident: 8–16 person-hours over 2–4 hours
- P2 incident: 4–8 person-hours over 1–2 hours
- P3 incident: 2–4 person-hours over 30–60 min
- **Annual estimate: 5 P1 × 12 hours + 15 P2 × 6 hours + 30 P3 × 3 hours = 270 person-hours/year**

---

## W852. Supply Chain Disruption Business Impact Assessment & Recovery

| Field | Detail |
|---|---|
| **Trigger** | Major supply chain disruption — port closure (Manila South Harbor, Cebu, Davao), vendor manufacturing halt, container shipping disruption, or national transportation strike |
| **Frequency** | Estimated 2–4 significant disruptions per year |
| **Volume** | Each disruption may affect 10–50% of inbound supply depending on scope |
| **Owner** | Supply Chain Director |
| **Participants** | Procurement Manager, Warehouse Manager, Merchandising Manager, Finance VP, BC Manager, Store Operations Director |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Assess disruption scope — identify affected POs (in-transit, pending shipment, at port), affected vendors, affected categories, estimated duration of disruption, and inventory coverage in days-of-supply | Supply Chain Planner | Supply Chain Director | 4 hours |
| 2 | Quantify business impact — estimate lost sales by category, store impact (which locations most affected), customer satisfaction impact, and financial exposure | Supply Chain Analyst | Finance VP | 4 hours |
| 3 | Activate alternative sourcing — identify backup vendors, authorized substitute SKUs, alternative ports of entry, and expedited air freight options for critical items | Procurement Manager | Supply Chain Director | 8–16 hours (over 2–3 days) |
| 4 | Implement allocation strategy — if supply is constrained, allocate available inventory to stores based on sales velocity, strategic importance, and customer impact | Supply Chain Planner | Merchandising VP | 4 hours |
| 5 | Communicate to Store Managers — provide impacted category list, expected recovery timeline, substitute SKU guidance, and customer messaging for out-of-stock items | Supply Chain Director | VP Operations | 2 hours |
| 6 | Monitor recovery — track alternative vendor performance, port reopening status, container movement, and inventory replenishment rate against normal levels | Supply Chain Planner | Supply Chain Director | Daily until resolved (1–4 weeks) |
| 7 | Post-disruption review — document root cause, response effectiveness, inventory impact, financial cost, and recommendations for supply chain resilience improvement | Supply Chain Director | VP Operations | 4 hours |

### System Touchpoints
- **Supply Chain Planning Module** — disruption scenario modeling, inventory coverage analysis
- **Procurement Module** — alternative vendor identification, expedited PO creation
- **WMS** — inventory allocation, substitute SKU mapping
- **BI Dashboard** — supply chain disruption dashboard, financial impact tracker
- **Communication Platform** — store notification, vendor communication

### Pain Points / Risks
- Alternative vendors may not meet quality or price standards — margin impact
- Air freight for bulky construction materials is prohibitively expensive; may not be viable
- Port closures in Manila affect 60% of import volume — limited alternative routing
- Customer switching to competitors during stock-out — brand loyalty risk
- Vendor force majeure claims may eliminate contractual remedies

### Staffing Implication
- Supply Chain Director: full-time during disruption
- Procurement Team: all hands on deck for alternative sourcing
- Supply Chain Planners: daily monitoring during recovery

### Time Estimate
- Per disruption: 40–80 person-hours over 1–4 weeks
- **Annual estimate: 3 disruptions × 60 hours = 180 person-hours/year**

---

## W853. Business Continuity Plan Tabletop Exercise & Drill Execution

| Field | Detail |
|---|---|
| **Trigger** | Scheduled — annual full exercise; semi-annual tabletop; quarterly IT DR test |
| **Frequency** | 1 full exercise/year, 2 tabletops/year, 4 IT DR tests/year |
| **Volume** | 1 full exercise involving 10–20 key personnel; 2 tabletops involving 8–12 participants each; 4 IT DR tests involving IT team |
| **Owner** | BC Manager |
| **Participants** | Executive Committee, IT Director, VP Operations, HR Director, Finance VP, Supply Chain Director, LP Director, Store Manager representatives |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Design exercise scenario — based on realistic threat (typhoon Signal No. 4 hitting Visayas, 7.2 magnitude earthquake in Mindanao, ransomware attack on ERP, or pandemic resurgence); define inject points and expected responses | BC Manager | VP Operations | 8 hours |
| 2 | Prepare exercise materials — scenario briefing document, inject cards (escalating events), evaluation rubric, participant roles, and communication simulation plan | BC Manager | VP Operations | 4 hours |
| 3 | Conduct tabletop exercise — walk through scenario with Executive Committee and department heads; discuss decision points, communication protocols, resource allocation, and escalation procedures | BC Manager | CEO | 3–4 hours |
| 4 | For full exercise: simulate operational response — activate communication tree (simulated), conduct mock store closure/reopening at 2 volunteer stores, test IT DR failover, and simulate supply chain rerouting | BC Manager | VP Operations | 1 full day |
| 5 | Evaluate exercise performance — assess decision speed, communication effectiveness, plan adequacy, resource availability, and interdepartmental coordination | BC Manager | VP Operations | 2 hours |
| 6 | Document findings and recommendations — identify plan gaps, training needs, resource shortfalls, and system improvements; assign corrective action owners and deadlines | BC Manager | VP Operations | 4 hours |
| 7 | Track corrective action completion — follow up on all identified improvements; verify implementation before next exercise cycle | BC Manager | VP Operations | Ongoing (quarterly review) |

### System Touchpoints
- **ERP Document Management** — exercise materials, findings documentation
- **IT DR Platform** — test failover execution and validation
- **Communication Platform** — simulated notification testing
- **HR System** — staff availability simulation
- **BI Dashboard** — exercise performance metrics

### Pain Points / Risks
- Executive time is scarce — tabletop scheduling requires 3–4 weeks advance notice
- Full exercises are expensive (PHP 1–2 million for operational disruption, IT testing, external evaluators)
- Exercise findings may not be acted on if not tied to accountability and budget
- IT DR testing during business hours risks impacting operations; weekend testing requires overtime budget
- Scenarios may be too theoretical — participants may not take them seriously

### Staffing Implication
- BC Manager: 80 hours per year for exercise design, execution, and follow-up
- Executive Committee: 4 hours per tabletop, 8 hours per full exercise
- IT Team: 16 hours per DR test × 4 tests = 64 hours
- External evaluator: engaged for full exercise (1 day)

### Time Estimate
- Per tabletop: ~40 person-hours total
- Per full exercise: ~200 person-hours total
- Per IT DR test: ~30 person-hours
- **Annual estimate: 2 × 40 + 200 + 4 × 30 = 400 person-hours/year**

---

## W854. Pandemic/Epidemic Business Continuity Activation & Operations

| Field | Detail |
|---|---|
| **Trigger** | WHO declares pandemic with Philippine impact; DOH declares epidemic alert; or company medical advisor recommends activation |
| **Frequency** | Rare (COVID-19-level events: estimated 1–2 per decade); preparedness maintained continuously |
| **Volume** | 1 activation affects all 200 stores, 4 DCs, and HQ; duration may be 3–18 months |
| **Owner** | CEO / VP Operations |
| **Participants** | Executive Committee, HR Director, BC Manager, IT Director, Supply Chain Director, Legal Counsel, External Medical Advisor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Activate pandemic response plan — CEO convenes crisis management team; declare pandemic operating mode; establish daily situation briefings and weekly strategy reviews | CEO | Board of Directors | 4 hours |
| 2 | Implement workplace safety protocols — mandatory masking, social distancing (store capacity limits), temperature screening, sanitation stations, contact tracing, and isolation rooms at each location | HR Director | VP Operations | 1 week deployment |
| 3 | Activate remote work for HQ/support functions — deploy VPN and collaboration tools for all non-store employees; maintain skeleton crew at HQ for essential on-site functions | IT Director | VP Operations | 1 week |
| 4 | Adjust store operations — reduced operating hours, BOPIS/curbside pickup emphasis, contactless payment promotion, queue management, and vulnerable population shopping hours | VP Operations | CEO | Immediate |
| 5 | Manage workforce availability — track employee health status (anonymized), activate cross-training for critical roles, hire temporary staff for increased sanitation, and manage leave policies (quarantine, isolation, caregiving) | HR Director | VP Operations | Continuous |
| 6 | Activate supply chain pandemic protocols — prioritize essential categories (sanitizers, PPE, building materials for home improvement), implement purchase limits for high-demand items, coordinate with vendors for supply continuity | Supply Chain Director | CEO | 1 week |
| 7 | Financial impact management — daily cash flow monitoring, expense reduction activation, government subsidy application (DOLE, SSS), rent renegotiation with landlords, and investor communication | Finance VP | CEO | Continuous |
| 8 | Deactivation and recovery — transition to post-pandemic operations as DOH guidance permits; phased return to normal operations; employee wellness support program; capture lessons learned | VP Operations | CEO | 1–3 months |

### System Touchpoints
- **HR System** — employee health tracking, contact tracing, leave management, remote work tracking
- **Communication Platform** — daily briefings, employee notifications, customer messaging
- **IT Infrastructure** — VPN capacity scaling, collaboration tools (Zoom, Teams), remote desktop
- **POS System** — contactless payment promotion, purchase limit enforcement, capacity counter
- **Supply Chain Module** — essential category prioritization, purchase limit rules
- **Finance Module** — daily cash flow dashboard, expense tracking, subsidy application tracking

### Pain Points / Risks
- Store employees cannot work remotely — frontline exposure risk is unavoidable
- Pandemic duration is unpredictable — business model sustainability beyond 6 months of reduced operations is uncertain
- Government regulations (IATF resolutions) change frequently — compliance requires rapid policy updates
- Supply chain for pandemic-essential items (masks, sanitizers) may face government price controls and allocation mandates
- Employee mental health and morale deterioration during prolonged crisis
- Customer behavior shift to ecommerce may be permanent — requires accelerated digital investment

### Staffing Implication
- Crisis Management Team: full-time during initial activation, then weekly cadence
- HR Director: 50% of time on pandemic workforce management
- IT Director: 30% of time on remote work infrastructure
- External medical advisor: retained for pandemic duration

### Time Estimate
- Initial activation: 200 person-hours over first 2 weeks
- Ongoing management: 40 person-hours/week for crisis team
- **Per pandemic year: ~2,200 person-hours above normal operations**

---

## W855. Communication Tree Activation & Crisis Communication Management

| Field | Detail |
|---|---|
| **Trigger** | Any event requiring coordinated communication to multiple stakeholder groups simultaneously — natural disaster, system outage, product recall, workplace safety incident, or PR crisis |
| **Frequency** | 3–5 activations per year (major); 10–15 minor activations |
| **Volume** | Each major activation reaches 6,715 employees, 200 Store Managers, 4 DC Managers, and potentially 600,000 loyalty customers |
| **Owner** | VP Operations / Corporate Communications Manager |
| **Participants** | CEO, HR Director, IT Director, Legal Counsel, BC Manager, Store Managers, External PR Agency (for public-facing crises) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Assess communication scope — determine stakeholder groups affected (employees, customers, vendors, media, regulators), message urgency (immediate/same day/next day), and communication channel (SMS blast, email, intranet, social media, press release) | Corporate Communications | VP Operations | 30 min |
| 2 | Draft and approve message — prepare factual, non-speculative message appropriate for each audience; Legal Counsel reviews for liability; CEO approves external communications | Corporate Communications | CEO | 30–60 min |
| 3 | Activate internal communication tree — (a) SMS blast to all Store Managers (target: within 15 min), (b) email to all employees, (c) intranet posting, (d) department head cascade (phone tree for P1 events), (e) employee hotline activation | Corporate Communications | VP Operations | 15–30 min |
| 4 | Activate external communication — (a) customer notification (SMS/email for affected loyalty members), (b) social media post (advisory or statement), (c) vendor notification for supply chain events, (d) press statement for media events, (e) regulatory notification (BIR, DOLE, LGU) as required | Corporate Communications | CEO | 30–60 min |
| 5 | Establish ongoing communication cadence — regular status updates at defined intervals (hourly for P1, every 4 hours for P2, daily for P3) until event resolved | Corporate Communications | VP Operations | Continuous |
| 6 | Monitor social media and feedback — track customer/employee reactions on social media, respond to inquiries, correct misinformation, and escalate negative sentiment trends | Corporate Communications | VP Operations | Continuous during event |
| 7 | Issue closure communication — all-clear notification, summary of event and resolution, thank stakeholders for patience, and provide next steps or resources | Corporate Communications | CEO | 30 min |

### System Touchpoints
- **SMS Blast Platform** — mass notification to employees and customers
- **ERP Communication Module** — internal messaging, Store Manager broadcast
- **HR System** — employee contact database, emergency contact information
- **CRM/Loyalty System** — customer notification, segment-specific messaging
- **Social Media Management Platform** — scheduled posts, sentiment monitoring, response management
- **Press/Media Contact Database** — media distribution list management

### Pain Points / Risks
- SMS blast system reliability during disasters — telecom congestion may delay delivery
- Premature or inaccurate communication can create liability (Legal review is essential but adds delay)
- Social media amplifies negative incidents — response time window is < 1 hour for viral content
- Employee personal social media posts about company incidents can complicate official messaging
- Regulatory notification requirements (BIR, DOLE, DENR) have specific timeframes and formats — non-compliance risk
- Language considerations — communications may need to be in English, Filipino, and regional languages (Bisaya for Mindanao)

### Staffing Implication
- Corporate Communications Manager: 1 FTE (lead for all crisis communications)
- External PR Agency: retainer for public-facing crisis support
- Legal Counsel: available within 30 min for communication review
- Department heads: phone tree participants for P1 events

### Time Estimate
- Per major activation: 20–40 person-hours over 24–72 hours
- Per minor activation: 5–10 person-hours over 4–8 hours
- **Annual estimate: 4 major × 30 hours + 12 minor × 7 hours = 204 person-hours/year**

---

## W856. Post-Incident Review, Lessons Learned & Plan Update

| Field | Detail |
|---|---|
| **Trigger** | After any P1/P2 system incident, natural disaster response completion, major LP case closure, or BCP drill completion |
| **Frequency** | As-needed; estimated 6–10 reviews per year |
| **Volume** | Each review covers one incident or exercise; participants include all involved parties |
| **Owner** | BC Manager / Incident Owner |
| **Participants** | All personnel involved in the incident, department heads, IT Director, LP Director, VP Operations |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Schedule post-incident review — within 5 business days of incident resolution; invite all involved parties; distribute incident timeline and data package to participants 24 hours before meeting | BC Manager | VP Operations | 2 hours (preparation) |
| 2 | Conduct review meeting — walk through incident timeline: (a) what happened (facts), (b) what was supposed to happen (per BCP/runbook), (c) what went well, (d) what didn't go well, (e) what was unexpected | BC Manager | VP Operations | 2–3 hours |
| 3 | Identify root causes — use 5-Why analysis for each failure point; distinguish between systemic issues (process/gap) and execution issues (human error/equipment failure) | BC Manager | VP Operations | 1 hour |
| 4 | Document lessons learned — compile findings, categorize as: (a) plan update needed, (b) training gap, (c) equipment/resource shortfall, (d) communication improvement, (e) vendor/partner issue | BC Manager | VP Operations | 2 hours |
| 5 | Assign corrective actions — each lesson has an owner, deadline, and budget (if needed); track in corrective action register | BC Manager | VP Operations | 1 hour |
| 6 | Update BCP and runbooks — incorporate approved changes into relevant plans, runbooks, training materials, and communication templates; version control all updates | BC Manager | VP Operations | 4–8 hours |
| 7 | Verify corrective action completion — follow up at 30 and 60 days; close out actions only when verified; report completion status to VP Operations | BC Manager | VP Operations | 1 hour/month |

### System Touchpoints
- **ERP Document Management** — review documentation, corrective action tracking
- **ITSM** — incident data extraction, timeline reconstruction
- **BI Dashboard** — incident metrics, resolution time trends, corrective action completion rates
- **Communication Platform** — meeting scheduling, document distribution

### Pain Points / Risks
- Post-incident review may be deprioritized as business returns to normal operations
- Blame culture can inhibit honest discussion of what went wrong — requires facilitation skill
- Corrective actions may not receive budget allocation; tracked but never implemented
- Lessons from provincial stores may not be shared with headquarters team — knowledge gap
- Timeline reconstruction is difficult when multiple systems and people are involved

### Staffing Implication
- BC Manager: 8–12 hours per review
- Participants: 2–3 hours per review
- Corrective action owners: variable (4–20 hours each)

### Time Estimate
- Per review: 20–30 person-hours
- **Annual estimate: 8 reviews × 25 hours = 200 person-hours/year**
