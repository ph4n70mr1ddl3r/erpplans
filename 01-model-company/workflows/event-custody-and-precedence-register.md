# Event Custody & Precedence Register

> Single-answer routing for cross-cutting business events that touch more than one value
> stream: which value stream **decides**, which **execute**, and who holds **incident command**.
> Born from the 2026-09-03 overlap review (three value streams independently governed
> typhoon response with conflicting triggers, owners, and frequency canons; POS returns were
> owned by a value stream the POS catalog never referenced). The declared overlap pairs in
> §4 are enforced bidirectionally by validator
> [Check 64](../../07-methodology/validate-repo.sh) — every pair must cross-reference in
> **both** directions.
>
> Back to [Workflow Index](README.md)

---

## 1. Event Custody Table

For each cross-cutting event: **Accountable** names the single throat-to-choke that decides;
**Canon** names the workflow that governs; **Supporting** workflows execute under it.

| # | Event | Accountable (decides) | Canon workflow | Supporting workflows | Boundary note |
|---|---|---|---|---|---|
| E-01 | Typhoon / natural-disaster preparedness (Signal 1–2) | Store Manager (site execution); Regional Manager (regional supervision) | VS-69 W2503 (store readiness checklist); VS-26 W848 (BCP protocol activation & monitoring, Signal 2+) | VS-26 W1221 (merchandise protection & regional BCP reporting layer); VS-24 W1386 (HSE preparedness activation at Signal 3, or Signal 2 with forecast intensification); VS-69 W2502/W2504 (pre-positioning; DC protocol) | W1221's protective actions execute through the W2503 checklist; W1221 retains the regional supervision and BCP reporting layer only |
| E-02 | Store emergency closure decision & execution | Regional Manager (VP Store Operations approves multi-store events; COO issues chain-wide directives) | VS-69 W2510 (closure decision matrix & execution) | VS-26 W850 (closure/reopening procedure mechanics, cash securing, reporting); W848 Step 3 (executes the controlled closure under W2510's authority) | The decision always follows W2510; W850 governs *how* a closure is executed and reopened, never *whether* |
| E-03 | In-store customer safety during sudden weather deterioration | Store Manager | VS-69 W2517 | VS-26 W848/W850 (defer in-store authority); VS-24 W695 (evacuation protocol upkeep & drills) | Site-level incident command is the Store Manager's at all times (see §3) |
| E-04 | Power outage / generator & power contingency | Store Manager (store); DC Operations Manager (DC) | VS-24 W1223 (store-level, any cause) | VS-69 W2514 (DC-level power contingency & typhoon-specific fuel logistics; defers store-level operations to W1223) | One generator canon per site type: stores → W1223; DCs → W2514 |
| E-05 | Flood response | Store Manager | VS-24 W1387 (response, inventory elevation, water-damage mitigation) | VS-26 W1213 (retains BCP/insurance linkage — damage documentation feeding W876 — and defers operational response to W1387) | W1387 owns the water; W1213 owns the claim trail |
| E-06 | Post-disaster damage assessment & reopening | Regional Manager | VS-69 W2518 (rapid damage triage & reopening, typhoon events) | VS-26 W1552 (phased reopening governance for multi-store/major events; W848 Step 8 chains here); W850 (reopening procedure mechanics); W1386's post-disaster assessment component defers to W2518 | Single typhoon-store triage = W2518; multi-store phasing program = W1552 |
| E-07 | Disaster insurance claim | CFO (via Insurance Coordinator) | VS-26 PA-26.3 W876 (claim processing & settlement) | VS-69 W2519 (loss quantification & claim initiation — feeds W876); W848 Step 7 (claim trigger) | Claim initiation may originate in VS-69; claim processing always lands in VS-26 |
| E-08 | Crisis communications & crisis management team | COO (chairs CMT situation room per W848 Step 5) | VS-26 W855 (communication tree) + W848 Step 5 (CMT activation) | VS-159 GSOC (maintains corporate incident command for security-class incidents until handoff; hands BCP-class command to the CMT) | Communications during any declared disaster always ride W855, regardless of which value stream is operationally leading |
| E-09 | In-store customer return | Customer Service Manager (per W1622 tiers) | VS-32 W1622–W1630 (eligibility, approval tiers, credit issuance, disposition) | VS-07 W12A/W12B/W12C (the store-execution variants: same-store counter flow, online-initiated drop-off ≈ 3,300–4,200/mo, cross-store with SM approval above PHP 5,000); VS-10 W1273 (the in-store drop-off experience & grading for ecommerce purchases — the same population as W12B); VS-08 W1538 (multi-tender refund mechanics); VS-08 W605 (fraud screening) | The POS value stream executes tender mechanics only; return *decisions* never originate in VS-08; W1623 owns ALL ecommerce return requests (≈ 4,000–5,000/mo, ~10–12% of ~42,900 orders) of which W12B's store drop-offs are the ≈ 8–10% subset |
| E-10 | Cash-on-delivery cash custody chain | Finance (COD program owner per VS-142) | VS-142 (end-to-end COD program: driver/3PL remittance, reconciliation, settlement) | VS-56 (3PL partner onboarding & settlement interfaces only) | VS-142 owns the cash trail end-to-end; VS-56 never touches COD cash reconciliation |
| E-11 | Personal-data breach response | Data Protection Officer (DPO) | VS-91 (NPC 72-hour notification canon) | VS-27 (cyber incident containment feeds the breach assessment) | Technical containment may run in VS-27; the notification clock, assessment, and NPC filing always run in VS-91 |
| E-12 | Store emergency / urgent purchase | Store Manager (walk-in cash emergencies ≤ PHP 5,000/purchase, ≤ PHP 20,000/month; Regional Manager phone approval above) | VS-34 W1674 (enterprise emergency/urgent purchase program: urgency classes, quote bypass < PHP 50K, monthly Finance pattern review) | VS-07 W1272 (store walk-in fast path within SM authority); VS-02 W921 (HQ supply-planning emergency sourcing for merchandise) | Store-level cash fast path = W1272; anything above store authority, DC/HQ events, and system-routed urgent POs = W1674; merchandise replenishment emergencies prefer W4/W921 |
| E-13 | Non-merchandise (indirect) procurement | Procurement (engine owner) | VS-03 W136 (the requisition → approval → PO → 3-way-match engine for all non-merch spend) | VS-34 W1668–W1672 (category programs: store supplies, IT, uniforms/PPE, marketing print, facility maintenance), VS-34.2 service-provider management, VS-34.3 spend monitoring | VS-34 owns category *policy and programs*; every requisition executes through the W136 engine — there is exactly one indirect-spend engine |
| E-14 | Freight & carrier management | VP Supply Chain (transportation spend) | VS-110 (carrier contracting, rate management, routing guides, freight audit — every leg) | VS-56 (last-mile courier partner layer: onboarding, SLA, settlement); VS-06 (own fleet operations) | Last-mile couriers = VS-56's partner layer; own-fleet ops = VS-06; carrier contracts, rates, and freight-audit always ride VS-110 |
| E-15 | Digital promotions & coupons | Category Manager (promo owner per W13) | VS-01 W13 (promo & pricing *execution* canon: setup, price file, activation) | VS-58 (coupon/voucher campaign issuance, redemption-fraud programs); VS-08 W539 (POS coupon redemption mechanics) | Campaign issuance = VS-58; redemption mechanics = VS-08 W539; price-file execution always chains W13 |
| E-16 | Third-party onboarding & risk gating | Risk owner per VS-161 tier model | VS-161 TPRM (risk tiering, due-diligence depth, continuous monitoring — the gate) | VS-03 W36 (merchandise-vendor onboarding, gated by VS-161 before activation); VS-172 (installer/contractor network onboarding, risk DD per VS-161) | The VS-161 gate applies to both onboarding paths; merchandise vendors via VS-03, installers via VS-172 — neither activates a high-risk tier without VS-161 sign-off |
| E-17 | Bulky-item delivery & installation | VS-143 program owner (bulky last-mile discipline) | VS-143 (bulky/white-goods delivery, installation, haul-away & recycling — crew scheduling, POD, reconciliation) | VS-12 W138 (installation service sales & scheduling — books the job, hands dispatch to VS-143); VS-10 PA-10.2 (parcel home delivery — never carries bulky items) | Bulky items never ride the parcel path; W138 sells and schedules, VS-143 executes the physical leg |
| E-18 | Store lifecycle (open / remodel / close) | Real Estate & Store Development per phase | VS-37 (new-store commissioning) · VS-109 (remodel/refurbishment) · VS-59 (closure/decommissioning) | VS-20 (site selection & construction feed VS-37); W850/W2510 (emergency closure is E-02, not lifecycle) | A closure-then-reopen remodel chains VS-59 → VS-109 → VS-37's reopening leg; emergency closures never route through VS-59 |
| E-19 | Structure fire (store or DC) | Store Manager (store); DC Operations Manager (DC); Regional Manager / VP Supply Chain own multi-site reopen gates | VS-24 W5537 (fire event response, suppression & post-fire BFP clearance — the event canon) | W330 (generic in-store protocol defers fire-specific execution); W695 (evacuation mechanics); W806 (suppression recertification at the reopen gate); W1296 (equipment inspection & impairment tracking); VS-26 W876 (claim trail); W140/W436 (injury chain); VS-147.3 (customer-injury claims) | Prevention & testing stay with W806/W1296 and the VS-04 DC PM checks; the fire *event* is always W5537; the claim always lands in VS-26 |
| E-20 | Earthquake | Store Manager (site command); Regional Manager (multi-store assessment phasing) | VS-26 W1450 (earthquake response, structural assessment & reopening safety verification — the quake canon) | W330 (in-store immediate response defers for the post-quake structural phase); W1223 (power contingency any cause); W848 (BCP monitoring/activation if multi-site); VS-69 W2518/W1552 analog does NOT apply — the PAGASA ladder governs typhoons only | The PAGASA signal ladder is typhoon-only; quake response follows W1450's own trigger ladder — never W2510's closure matrix |
| E-21 | In-progress armed violence / robbery / active threat | Store Manager (during-event site command) | VS-19.1 W717 (workplace violence prevention & response protocol — the program & response canon) | W330 (evacuation/medical mechanics); W501 (first aid); W471 (post-event Category-A police/Barangay reporting & evidence); VS-23 (LP investigation support); W1325 (death-in-service benefits); W855 (crisis comms if escalated) | During-event command is always the Store Manager; W717's CHRO ownership governs prevention training, threat assessment and post-event response — never overrides site command |
| E-22 | Mass mispricing / price-file integrity event | Revenue Assurance Lead / Merchandising-Pricing (decides); VP Legal owns the regulatory posture | VS-118.2 W5543 (price-file integrity event response & mass-mispricing rollback — the event canon) | W3697 (detection feeds the trigger); W13 (rollback executes through the price-file canon — never around it); W63 (store re-label task campaign); W1622/W1538 (customer refund mechanics); W427/W658 (DTI response pattern); VS-57 (stale-price steady state) | Detection stays W3697; rollback execution always rides W13; POS refund mechanics never decide the event — W5543 owns scope, posture and quantification |
| E-23 | Stored-value & loyalty platform outage | Category Manager (Gift Cards) with CRM-Loyalty Manager (acceptance-exposure decisions); CFO (liability) | VS-54.2 W5548 (downtime-acceptance & manual-redemption canon) | VS-27/IT incident canon (technical restoration); VS-08 (POS manual-mode flags & mechanics); VS-13 (customer remediation desk); W3699 (integrity monitoring feeds the fraud watch) | Technical restoration runs IT incident management; the acceptance matrix, manual-redemption exposure and the liability ledger always live in VS-54 — never at store discretion |
| E-24 | Card-network / acquirer outage | Head of Customer Service (chain-wide tender protocol) | VS-08.1 W5547 (payment-network & acquirer outage response canon) | W535 (store-side offline POS is a different failure layer — connectivity, not network); W537/W3701 (settlement reconciliation & chargeback disputes always land here); VS-27 incident canon (if a cyber cause is suspected); LP (outage-window fraud watch) | Outage response & tender policy = W5547; settlement discrepancies land in W537/W3701 reconciliation, never in the outage protocol itself |
| E-25 | Regulator-ordered suspension / closure of a site (BIR Oplan Kandado class) | CFO via Tax Manager (comply/protest/settle decision) | VS-79.3 W5545 (tax-enforcement suspension & closure-order response canon) | W850 (closure & reopening mechanics — the how, never the whether); W658/W2773 (inspection-response & controversy governance); VS-22 (regulatory desk); W5019 (disclosure if material) | The order dictates closure; W850 executes mechanics only; reopening requires the written BIR lifting order — never W850's trading judgment alone |
| E-26 | Key-executive incapacitation, death or sudden departure | Board Chair (CEO events); CEO (other C-level) | VS-36.1 W5544 (emergency executive succession & decision-rights continuity canon) | W1717/W1718 (resolution & SEC records); W317 (bank mandates); Tax (BIR/eFPS signatory continuity per W5546); W1408 (SoD re-check on reassignment); W5017/W5019 (disclosure for a listed company); W1325 (death-in-service benefits); W855/W134 (comms rings) | The emergency bridge (interim appointment, delegations, signatory continuity) is always W5544; the permanent succession rides W178; disclosure timing is decided by IR per W5017, never by comms improvisation |

## 2. PAGASA Signal Ladder (Single Canon)

One trigger ladder for all typhoon-family workflows. No workflow may activate a closure
outside this ladder.

| Condition | State | Governing workflows |
|---|---|---|
| PAGASA Signal No. 1 raised, or typhoon within 48-h projected path | Readiness: execute store checklist; seasonal pre-positioning | W2503 (checklist), W2502 (pre-positioning), W1221 (merchandise protection via W2503), W848 Steps 1–2 (monitoring & advisory) |
| PAGASA Signal No. 2 | Heightened preparation — **no closure** absent an LGU order or facility safety failure | W848 (full protocol activation), W1223 (generator fueling & test), W1386 (only if forecast intensification), W2504 (DC protocol) |
| PAGASA Signal No. 3+, LGU evacuation order, or facility safety failure | Closure decision & execution | W2510 (decision — Regional Manager; VP Store Operations for multi-store), W848 Step 3 / W850 (execution mechanics), W2517 (in-store customer safety), W2511 (DC shutdown) |
| Signal lifted / flood receded / all-clear | Assessment & phased reopening | W2518 (rapid triage), W1552 (phased reopening governance), W850 (reopening procedure), W2519 → W876 (loss quantification → claim) |

> **Frequency-canon reconciliation.** The three closure/response frequencies describe
> different populations and all stand: **W850** — 5–10 emergency closures per store per year
> (all causes, incl. power outages and civil disturbance); **W2510** — 2–5 typhoon-signal
> closures per store per year (the Signal 3+/LGU-order subset); **W848** — 5–8 protocol
> activations per year chain-wide (Signal 2+ events, most of which never reach closure).

## 3. Incident Command Ladder (Single Canon)

Command escalates up exactly one ladder, regardless of which value stream's workflows are
executing:

1. **Site Incident Commander — Store Manager** (per VS-07 PA-07.2 staffing canon). Commands
   all in-store response (W2517, W1387, W1223) from first signal through reopening.
2. **Closure Authority — Regional Manager** (per W2510). Approves/decides closure; VP Store
   Operations approves multi-store events; COO issues chain-wide directives.
3. **Corporate Crisis Command — Crisis Management Team** (activated per W848 Step 5; COO
   chairs the situation room; BC Manager runs monitoring; communications ride W855). The
   GSOC (VS-159) maintains corporate incident command for **security-class** incidents and
   hands BCP-class command to the CMT at activation.

## 4. Declared Overlap Pairs

Each declared pair must cross-reference in **both directions** (any file of VS-A citing VS-B
and vice versa); enforced by validator Check 64. Adding a pair here without shipping the
bidirectional links fails validation.

| Pair ID | Value-stream pair | Shared event domain |
|---|---|---|
| OP1 | VS-24 ↔ VS-26 | Disaster response & business continuity (E-01, E-04, E-05, E-06, E-08) |
| OP2 | VS-24 ↔ VS-69 | Typhoon preparedness & response (E-01, E-04, E-05, E-06) |
| OP3 | VS-26 ↔ VS-69 | Typhoon BCP vs operational response (E-01, E-02, E-06, E-07, E-08) |
| OP4 | VS-08 ↔ VS-32 | POS return execution vs return decisioning (E-09) |
| OP5 | VS-07 ↔ VS-32 | Cross-store return variant & thresholds (E-09) |
| OP6 | VS-03 ↔ VS-34 | Indirect-spend engine vs category programs (E-13) |
| OP7 | VS-07 ↔ VS-34 | Emergency-purchase authority ladder (E-12) |
| OP8 | VS-110 ↔ VS-56 | Freight/carrier vs last-mile courier layer (E-14) |
| OP9 | VS-110 ↔ VS-06 | Freight carrier procurement vs own-fleet ops (E-14) |
| OP10 | VS-58 ↔ VS-01 | Coupon campaign issuance vs promo execution canon (E-15) |
| OP11 | VS-58 ↔ VS-08 | Coupon campaigns vs POS redemption mechanics (E-15) |
| OP12 | VS-03 ↔ VS-161 | Vendor onboarding vs TPRM risk gate (E-16) |
| OP13 | VS-03 ↔ VS-172 | Merchandise-vendor vs installer-class onboarding (E-16) |
| OP14 | VS-12 ↔ VS-143 | Installation service sales vs bulky delivery canon (E-17) |
| OP15 | VS-10 ↔ VS-143 | Parcel home delivery vs bulky routing (E-17) |
| OP16 | VS-37 ↔ VS-59 | Opening vs closure lifecycle (E-18) |
| OP17 | VS-37 ↔ VS-109 | Opening vs remodel lifecycle (E-18) |

---

*Back to [Workflow Index](README.md) | See also [Dependency Map](workflow-dependency-map.md) · [Criticality Classification](workflow-criticality-classification.md)*

*Date: 2026-09-05 (v1.4) — fourth custody wave (batch 17): events E-23–E-26 added with the batch-17 workflow gap fill: E-23 stored-value & loyalty platform outage (canon W5548, PA-54.2 — the acceptance-exposure decision and liability ledger live in VS-54, never at store discretion), E-24 card-network/acquirer outage (canon W5547, PA-08.1 — distinct from W535's store-connectivity offline layer; settlement discrepancies always land W537/W3701), E-25 regulator-ordered suspension/closure — the BIR Oplan Kandado class (canon W5545, PA-79.3 — the order dictates closure, W850 executes mechanics, reopening requires the written lifting order), and E-26 key-executive incapacitation/death/sudden departure (canon W5544, PA-36.1 — the emergency bridge to interim stability; permanent succession rides W178; disclosure timing owned by IR per W5017). No new OP pairs declared — each new event routes through a single-VS canon with named supporting workflows, matching the E-04/E-10/E-11/E-19–E-22 precedent. Prior v1.3 (2026-09-05) — third custody wave (batch 16): events E-19–E-22 added, closing the register's own blind spot — the register was born from the typhoon triple-collision, but fire, earthquake, armed violence and mass mispricing had the same multi-VS collision pattern with no custody ruling (fire touched VS-24 W330/W806/W1296 vs VS-07 vs VS-26 W876 vs VS-04 DC checks; quake had a canon in W1450 that the ladder never named; in-progress robbery was commanded by W330's Store Manager while W717's accountable owner is CHRO; pricing fragments lived in W13/W3697/W1622 with no event owner). The wave shipped with the batch-16 workflow gap fill: W5537 (fire event canon, PA-24.2), W5538 (bomb threat, PA-24.2), W5536 (missing-child / Code Adam, PA-07.2), W5539 (elevator/escalator entrapment, PA-07.2), W5540 (payroll run failure, PA-19.2), W5541 (bank-failure / frozen-deposit contingency, PA-18.3), W5542 (liquidity stress & payment-prioritization escalation, PA-105.3), W5543 (price-file integrity event, PA-118.2). No new OP pairs declared — E-19/E-20 route through the existing OP1–OP3 disaster pairs and single-VS canons, matching the E-04/E-10/E-11 precedent. Prior v1.2 (2026-09-03) — residual sweep after the second custody wave: the ecommerce-returns canon (W1623 ≈ 4,000–5,000 total requests ≈ 10–12% of ~42,900 orders; W12B store drop-offs ≈ 3,300–4,200 ≈ 8–10%; courier-pickup remainder ≈ 800–1,700 ≈ 3–7% of home-delivery orders) propagated to the five surfaces the wave missed — W1273 (VS-10 PA-10.2, whose 20–25%/8,500–14,300 variant contradicted the canon; Frequency/Volume/Background/Time Estimate/Staffing re-derived and a custody bullet added), W509 (7–9% → 10–12% with the 8,000–15,000 item band), W707 (8–10%/110–140-day → 10–12%/130–170-day), W215 (1–2%/200–400 → 3–7%/800–1,700 with the staffing cascade re-derived), W2308 (5–8% → 10–12%), plus the two stale ~2,250/month stragglers the wave's own CHANGELOG claimed retired (W12's staffing bullet and W101's refund TE line); E-09's supporting list now names VS-10 W1273 explicitly. Two broken relative links to this register repaired (VS-08/VS-32 READMEs missing the `../` prefix) and validator Check 66 added (file-level relative-link resolution outside PA files).* Prior v1.1 (same day) — second custody wave: events E-12–E-18 added (emergency-purchase ladder W1272/W1674, indirect-procurement engine W136 vs VS-34 category programs, freight/carrier VS-110 vs VS-56/VS-06, promotions W13/VS-58/W539, third-party onboarding risk gate VS-161 over VS-03/VS-172, bulky delivery VS-143 over W138/PA-10.2, store lifecycle VS-37/59/109); E-09 extended (W12A/W12B named store-execution variants; online-returns canon trued — W1623 ≈ 4,000–5,000 total requests ≈ 10–12% of ~42,900 ecommerce orders, W12B ≈ 3,300–4,200 store drop-offs ≈ 8–10%; the stale ~2,250 figure retired from W12B's Time Estimate and VS-15.2's refund volume); pairs OP6–OP17 declared (all bidirectionally linked at issue; Check 64 enforces). Validator Check 65 added the same pass (cross-VS duplicate-event guard: byte-identical event Triggers and distinctive Frequency canons, with the 33 adjudicated legitimate shared-cadence/canon clusters allowlisted).* Prior v1.0 (same day) — initial issue: typhoon triple-collision, POS-returns routing, COD/breach custody confirmations, PAGASA signal ladder, incident-command ladder, Check 64.
