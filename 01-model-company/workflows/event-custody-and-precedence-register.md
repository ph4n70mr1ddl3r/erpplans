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
| E-09 | In-store customer return | Customer Service Manager (per W1622 tiers) | VS-32 W1622–W1630 (eligibility, approval tiers, credit issuance, disposition) | VS-08 W1538 (multi-tender refund mechanics at POS); VS-07 W12 (cross-store variant — Store Manager approval above PHP 5,000); VS-08 W605 (fraud screening) | The POS value stream executes tender mechanics only; return *decisions* never originate in VS-08 |
| E-10 | Cash-on-delivery cash custody chain | Finance (COD program owner per VS-142) | VS-142 (end-to-end COD program: driver/3PL remittance, reconciliation, settlement) | VS-56 (3PL partner onboarding & settlement interfaces only) | VS-142 owns the cash trail end-to-end; VS-56 never touches COD cash reconciliation |
| E-11 | Personal-data breach response | Data Protection Officer (DPO) | VS-91 (NPC 72-hour notification canon) | VS-27 (cyber incident containment feeds the breach assessment) | Technical containment may run in VS-27; the notification clock, assessment, and NPC filing always run in VS-91 |

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

---

*Back to [Workflow Index](README.md) | See also [Dependency Map](workflow-dependency-map.md) · [Criticality Classification](workflow-criticality-classification.md)*

*Date: 2026-09-03 | Event Custody & Precedence Register v1.0 — issued by the event-custody
overlap pass: the typhoon triple-collision (VS-24/VS-26/VS-69), the POS-returns routing gap
(VS-08↔VS-32, VS-07↔VS-32), the COD-cash and data-breach custody confirmations (VS-142,
VS-91), the unified PAGASA signal ladder and incident-command ladder, and the Check 64
bidirectional-link guard. Dependency-map self-loop edges (W54→W54, W288→W288) repaired in
the same pass (map v4.17).*
