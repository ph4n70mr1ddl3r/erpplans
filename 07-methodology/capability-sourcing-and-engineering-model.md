# BuildRight Depot Corp. — Capability Sourcing & Engineering Model

> Companion to [`it-product-operating-model.md`](it-product-operating-model.md) (v2.9): how
> each business capability is **sourced** — configured in the unified ERP core, bought
> best-of-breed, or built in-house — plus the decision gate, the Capability Sourcing
> Register, the build-squad engineering standard, and the Software Engineering Platform (SEP)
> team definition.

---

## 1. Purpose & Scope

The IT product operating model v1.x assumed a **single-vendor unified cloud ERP**: the vendor
delivered all code and BuildRight's IT configured it. On 2026-09-03 the company adopted a
**hybrid capability-sourcing strategy**: the ERP remains the unified core, selected edge
capabilities move to **best-of-breed (BoB) products** from specialist vendors, and genuinely
differentiating capabilities are **built in-house** by dedicated software squads.

This document defines:

1. The **landscape principle** — what stays core, what is bought, what is built (§2).
2. The **sourcing decision gate** (Configure / Buy / Build) and its governance (§3).
3. The **Capability Sourcing Register** — the single record of every sourcing decision (§4).
4. The **team archetypes and build-squad shape** the strategy requires (§5).
5. The **Software Engineering Platform (SEP)** team and the paved road (§6).
6. The **engineering standard** build squads must meet (SDLC, security, delivery) (§7).
7. The **best-of-breed lifecycle** — vendor management, release intake, exit reserves (§8).
8. **Funding, TCO and capitalization** rules per archetype (§9).
9. KPIs and **risks** (§10–§11).

Scope is the same steady state as the operating model: post-go-live operations of the 188
value streams. Team membership, RACI, sizing and governance bodies live in the operating
model; this document governs the sourcing decisions that determine team shape.

---

## 2. Landscape Principle — Unified Core, Bought Edges, Built Differentiators

The strategy does **not** abandon the unified ERP. It partitions the landscape into three
tiers, each with a default sourcing posture:

| Tier | What it contains | Default posture | Why |
|---|---|---|---|
| **Core** | Financials & consolidation, procure-to-pay, the inventory ledger, HR & payroll (PH statutory), POS (offline-capable estate), approvals workflow | **Configure** in the unified cloud ERP | Protects the 5-working-day close (FIN KPI), BIR/SSS/PhilHealth/Pag-IBIG statutory compliance, the 808-control register's single control surface, and the ≥ 8h offline POS + event-replay architecture (`technical-guidelines.md` §1) — too costly and risky to de-unify |
| **Edges** | Capabilities where specialist vendors outperform the ERP suite: warehouse execution (WMS), transport management (TMS), store workforce management (WFM), field service management (FSM) | **Buy** best-of-breed, integrate via IAP | ERP fit-to-standard gap is high **and** a mature specialist market exists; commodity capability is not a moat |
| **Differentiators** | Capabilities where BuildRight's operating model is genuinely unlike generic retail: omnichannel order orchestration; trade & project services coordination | **Build** in-house squads | High gap, no vendor solves it well, deep data/control needs — the capability *is* competitive advantage |

**Guardrail:** nothing may be removed from the Core tier without a CEO-noted waiver of the
unified-core principle — the same protection the single-vendor principle had in operating
model v1.x, now scoped to the core rather than the whole landscape.

---

## 3. The Sourcing Decision Gate

Every capability decision routes through one gate with three exits. The default order is
**configure → buy → build**: build is chosen only when both alternatives are demonstrably
inadequate. Demand reaches the gate through the capability demand-intake & backlog-triage
front door (**W5535**, PA-113.2): stakeholders raise needs with their paired IT PO/PM; the
PO logs the item and EA triages it against the 188-VS catalog — enhancements stay in team
backlogs, missing workflow-level owners enter the gap-analysis admission path, and only
genuine new-capability candidates arrive here as sourcing proposals with their triage pack.

### 3.1 Decision criteria (scored, not vibes)

| Criterion | Points toward **Configure** | Points toward **Buy** | Points toward **Build** |
|---|---|---|---|
| Strategic differentiation | Commodity (GL, AP, payroll) | Commodity, ERP-weak | **Differentiating** — customers would notice if a competitor had it |
| ERP fit-to-standard gap | Low | High but market-solved | High **and** unsolved by the market |
| Integration cost of de-unifying | — | IAP estimate must be < value gained | Same |
| Data gravity | Ledger/master data lives here | Own operational data model | Needs deep data control (e.g., order-state machine) |
| Regulatory fit | Deep (BIR, SSS built in) | **Verify PH localization** — a BoB vendor without Philippine statutory readiness is disqualifying | BuildRight owns the compliance burden entirely |
| Total cost of ownership | Config analysts | License + TPRM + integration run cost | Squad cost + permanent tech-debt backlog |
| Talent & key-person risk | Low | Low (vendor's talent) | Permanent hiring/retention obligation |
| Exit strategy | Vendor roadmap risk | Contract/portability clauses, escrow | None — in-house is forever |

### 3.2 Decision rights

| Decision | Body | Notes |
|---|---|---|
| Configure/buy/build routing (any capability) | **Sourcing & Investment Board (SIB)** — chaired by CIO; Head of EA runs the assessment; members: affected IT PO/BPO, FinOps/TBM analyst, CFO delegate, SEC lead (TPRM, VS-161), Head of Engineering (for builds) | Monthly and on demand; every decision recorded in the Register (§4) |
| Sourcing decision with 3-year TCO > PHP 25M | SIB recommends → **Product Council** ratifies | Product Council already holds funding rights above PHP 5M |
| Removal of a capability from the Core tier | SIB recommends → **CEO** (noted waiver) | Rare; same weight as the v1.x single-vendor waiver |
| Architecture opinion on any sourcing proposal | **Architecture Review Board (ARB)** | Integration patterns, data ownership, retirement of capabilities |

### 3.3 Mandatory appendices per decision

No sourcing decision is valid without:

1. **IAP integration estimate** — flows, contracts, latency budget, run cost.
2. **Control-mapping appendix** — which of the 808 controls in
   [`internal-controls-matrix.md`](../01-model-company/internal-controls-matrix.md) touch the
   capability, and where evidence will come from after the change (vendor attestation, API,
   or in-product audit trail).
3. **TCO sheet** — 3-year license + integration + run + (build) squad cost, FinOps-verified.
4. **Exit plan** (buy) or **run-cost & talent plan** (build).
5. **Re-evaluation trigger** — e.g., "revisit if the ERP vendor ships native WMS execution
   at parity", "revisit at 260 stores".

---

## 4. Capability Sourcing Register (initial issue)

The Register is the single source of truth for what is sourced how. Initial decisions adopted
2026-09-03 (amendments only via the SIB):

| Capability | Value streams | Decision | Product / system | Owning team | Re-evaluation trigger |
|---|---|---|---|---|---|
| Financials, P2P, inventory ledger, HR/payroll, POS, approvals | VS-15–VS-19, VS-07/08 and the rest of the core | **Configure** (reaffirmed) | Unified cloud ERP (core) | FIN, PEO, SSP, MSC, CORP as mapped in OM §4 | Annual reaffirmation at QBR |
| Warehouse execution (RF-directed putaway/pick, wave planning, lot/serial capture) | VS-04, VS-05 | **Buy** — best-of-breed WMS | BoB WMS; ERP remains inventory ledger of record | WLI | ERP vendor ships native WMS at parity |
| Transport planning, carrier tendering, freight audit | VS-06, VS-110 | **Buy** — best-of-breed TMS | BoB TMS; ERP keeps freight cost postings | WLI | Freight spend < PHP 1.2B/yr |
| Store labor scheduling & time capture | VS-07 (staffing PAs) | **Buy** — store workforce management | BoB WFM; payroll stays in ERP core (statutory) | SSP | None scheduled |
| Installation & home-service dispatch, technician mobile app | VS-12 | **Buy** — field service management | BoB FSM | CCP | FSM vendor adds trade-project features |
| Omnichannel order routing, split-order & mixed-basket fulfillment | VS-60 | **Build** — Order Orchestration product (OMO) | In-house event-driven order-state engine on IAP contracts | OMO | None — differentiating |
| Trade & project services coordination (job-site delivery, material staging/phased delivery, bulky install/haul-away) | VS-74, VS-77, VS-143 | **Build** — Trade & Project Services platform (TPS) | In-house scheduling/coordination platform | TPS | None — differentiating |
| Agentic automation runtime (agent platform) | VS-30 (PA-30.2 AI/ML & Automation engineering); governed by VS-128 | **Build** — AI & Agent Platform (AAP) on bought foundation-model APIs | In-house agent runtime: tool registry (IAP contracts only), guardrails, evaluation harness, human-in-the-loop gates | AAP | Foundation-model vendor ships a governed agent runtime at parity |
| Foundation-model access (LLM APIs) | Cross-cutting (all agent use cases) | **Buy** — tier-1 TPRM API contracts | Vendor foundation models consumed through IAP-governed API edges | AAP with SEC (TPRM) | Philippine AI-regulation / NPC guidance change |

The two build decisions create the new stream-aligned products **OMO** and **TPS** in the
operating model §3.2/§4 (VS-60 moves from CCP; VS-74/VS-143 from WLI and VS-77 from CCP).
The four buy decisions add **Vendor Product Manager** capacity inside the existing WLI, SSP
and CCP teams. No value stream changes business-process owner. The two agentic rows
(2026-09-03b) create the **AI & Agent Platform (AAP)** platform team (§12; OM v2.1) —
agents themselves are delivered by the domain product teams that own the workflows being
automated, on the AAP paved road.

---

## 5. Team Archetypes & Build Squads

Domain teams come in three shapes (full membership tables in OM §5):

| Archetype | Teams | Shape |
|---|---|---|
| **Configure** | MSC, FIN, PEO, CORP | The OM v1.x six-role core: PO, product/process architect, 2–4 ERP functional analysts, data & reporting analyst, QA & release analyst |
| **Buy-and-integrate** | WLI, SSP, CCP | Configure core **plus** 1–2 Vendor Product Managers (contract, SLA, vendor release intake, TPRM liaison per BoB product) and added functional-analyst depth for the vendor products' configuration surface |
| **Build** (squads) | OMO, TPS | Product Manager, Tech Lead, 3–4 software engineers, QA automation engineer; shared UX/product designer (SEP pool); matrixed IAP engineer and DP data analyst |

### 5.1 Build-squad roles

| Role | Reports to | Responsibilities |
|---|---|---|
| **Product Manager (PM)** | CIO (solid); product-domain exec (dotted) | The build-side equivalent of the IT PO: outcomes, discovery, roadmap, budget; pairs with the BPO like any domain PO; owns product KPIs and DORA-aware delivery trade-offs |
| **Tech Lead** | Head of Engineering (solid); squad PM (dotted) | Technical design authority for the product; chairs squad design reviews; owns the product's architecture record at the ARB; one of the two build-side seats in the architect community |
| **Software Engineers (3–4)** | Tech Lead | Build and run the product: implementation, code review, on-call for P1/P2, telemetry, cost of the services they own (FinOps tags) |
| **QA Automation Engineer** | Squad PM | Test strategy, automated acceptance and contract tests, regression harness, release verification — the build twin of the configure teams' QA & release analyst |
| **UX / Product Designer** (SEP pool, ~0.5 FTE per squad) | Head of Engineering | Flows, screens, and usability for internal and customer-facing surfaces of built products |

Engineers are **hired into the engineering career track** under the Head of Engineering, not
into per-squad silos — the track and the SEP paved road (§6) are what keep two squads from
becoming two incompatible cultures.

---

## 6. Software Engineering Platform (SEP)

A new **platform team** (the sixth) in the operating model's platform layer. SEP treats build
squads — and, increasingly, configure teams' automation needs — as its customers.

| Member | Role |
|---|---|
| **Head of Engineering** | Engineering standards, squad staffing, technical career track, SEP roadmap; ARB member |
| **DevEx engineers (2)** | The **paved road**: golden-path service templates, CI/CD pipelines, feature-flag and telemetry tooling, internal developer platform — the default way to ship, so squads never assemble their own toolchain |
| **AppSec engineer** | SDLC security: SAST/DAST gates, dependency and SBOM policy, secrets management, threat-review facilitation (dotted to SEC lead) |
| **QA automation lead** | Shared test framework, contract-testing harness against IAP contracts, load-test rigs |
| **Product designer** | Shared UX pool for build squads (~0.5 FTE each) |
| **Build SRE** | Ring-deployment infrastructure, production readiness reviews, on-call coaching for squads (pairs with INFRA SRE) |

---

## 7. Engineering Standard (SDLC for built products)

Built products follow one standard, enforced by the paved road rather than by memo:

1. **Golden path.** New services start from SEP templates (repo layout, CI/CD, observability,
   IaC). Deviating requires an ARB-recorded exception.
2. **Trunk-based development, feature flags.** Continuous integration; incomplete work ships
   dark behind flags; no long-lived branches.
3. **Contract-first integration.** Every integration to another product is an IAP-published
   contract (event or API) with automated consumer-driven contract tests; no squad may call
   another product's database directly.
4. **Ring deployment.** Internal ring → canary stores/DCs → fleet, with automated rollback
   gates on SLO burn. Built products deploy independently of the ERP monthly train (OM §8.2).
5. **Security gates.** SAST + dependency scan on every merge; DAST before each release ring
   expansion; SBOM per release; secrets never in code. The AppSec engineer can block a ring
   expansion.
6. **Data contracts.** Every dataset a built product publishes to DP carries a tested schema
   contract; breaking changes go through the DP shared-object change process (OM §6.3).
7. **Production readiness review** (SEP + INFRA) before first fleet ring: on-call runbook,
   SLOs, capacity model, DR posture — typhoon-season resilience is a launch criterion, not a
   follow-up.
8. **DORA targets** (per squad, reported at QBR): deployment frequency ≥ weekly; change lead
   time < 1 week; MTTR < 4 hours; change-failure rate < 15%.

---

## 8. Best-of-Breed Lifecycle Management

Buying does not outsource ownership. Each BoB product has:

- **A named Vendor Product Manager** in the owning domain team — contract and SLA owner,
  vendor roadmap intelligence, release-intake owner, escalation single point of contact.
- **Contract clauses required at signature:** Philippine data-residency/processing terms
  (RA 10173), statutory-readiness warranty where applicable, exit/transition assistance,
  data-export in open formats, and price-escalation caps.
- **Release intake ring:** vendor releases land in a staging ring and pass the domain's
  regression pack (Tier-1 workflows mandatory) before production — the same standard the ERP
  vendor train meets (OM §8.2).
- **Upgrade currency KPI:** at most one major version behind vendor current — a product two
  versions behind is a Tier & Control Board escalation.
- **TPRM tiering (VS-161):** every BoB vendor is risk-tiered by SEC; tier-1 vendors get
  annual reassessment and audit-report review.
- **Exit reserve:** funded at each QBR (a percentage of license cost, held centrally by the
  CIO Office) so a vendor exit is never unfundable.

---

## 9. Funding, TCO & Capitalization

| Rule | Detail |
|---|---|
| **Persistent envelopes survive** | All teams — configure, buy, build — remain persistent-capacity funded (OM §8.4); nothing reverts to project funding |
| **Build envelopes** | Build squads carry their run cost (squad + infrastructure) in the product envelope; **PFRS / IAS 38** capitalization of qualifying development costs is assessed quarterly with FIN (Controller) — FIN owns the accounting policy, the squad owns the evidence trail |
| **TCO-per-product accounting** | FinOps tags 100% of spend to products (already OM policy); BoB products carry license + integration run cost; built products carry squad + cloud cost. Every QBR shows TCO per product |
| **Sourcing reserve** | The CIO Office central bucket (OM §8.4) funds sourcing transitions — evaluations, migrations, exit execution — so no team's steady-state capacity is cannibalized by a sourcing move |
| **Exit reserves** | Per §8 — accrued centrally, disclosed in the QBR FinOps pack |

---

## 10. KPIs by Archetype

Headline KPIs live in OM §8.3 (which adds OMO, TPS and SEP rows). Summary:

- **Configure products:** unchanged OM v1.x KPIs (uptime, close cycle, filing timeliness…).
- **Buy products:** vendor SLA attainment, integration latency vs budget, upgrade currency,
  regression-pack pass rate on vendor releases.
- **Build products:** DORA metrics (§7 rule 8) **plus** product outcome KPIs (e.g., OMO: routing
  decision latency, split-order success rate; TPS: on-time job-site delivery, staging
  schedule adherence) — a squad green on DORA but flat on outcomes is failing.

---

## 11. Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Integration sprawl silently recreating the pre-ERP silo estate | IAP is the only integration path; contract-first rule (§7 rule 3); ARB reviews every new pipeline; SEP/IAP co-own the contract catalog |
| Fragmented statutory compliance (payroll/tax outside the core) | Core-tier guardrail (§2); PH-localization warranty clause (§8); control-mapping appendix per decision (§3.3) |
| Build squads drifting from the paved road into private toolchains | Golden path + exception records; Head of Engineering owns the engineering track; DORA reporting surfaces drift quickly |
| Key-person risk on built products | Bus-factor ≥ 2 per service (squad review rule); SEP owns runbooks; no solo-owned services |
| Vendor lock-in on BoB edges | Exit clauses, data-export rights, funded exit reserves (§8), annual re-evaluation triggers (§4) |
| Sizing creep — engineering hiring outpacing value | SIB gate requires the build case to beat configure **and** buy; QBR structural review can merge/sunset squads like any product (OM §10); IT sizing stays inside the 65–130 hybrid band (OM §9.2) |
| Control-evidence gaps across vendor boundaries | Control-mapping appendix at decision time; Tier & Control Board signs off changes touching Tier-1 workflows on any product (OM §6.3) |

---

## 12. Agentic Automation Program (VS-30 Engineering · VS-128 Governance)

The company maximizes **agentic AI**: AI agents that execute manual tasks end-to-end inside
guardrails. The program rides entirely on structures that already exist — the sourcing gate
(§3), the register (§4), the AAP platform team (OM §5.3), and VS-128's governance discipline
(model registry, risk tiering, kill-switch, AI incident management, ethics review, RA 10173
automated-decision obligations, ISO 42001/NIST-AI-RMF alignment).

### 12.1 The autonomy ladder (agents obey the workflow Tier register)

| Workflow tier | Agent autonomy | Rule |
|---|---|---|
| **Tier 1** (1,390 workflows) | **Human-approval-gated only** | Agent drafts, summarizes, flags, or prepares — a named human decides and signs (approval-matrix evidence retained) |
| **Tier 2** (3,281) | **Bounded autonomy** | Agent acts inside hard guardrails (limits, whitelists, value caps); sampled human audit; auto-escalation on anomaly |
| **Tier 3** (758) | **Autonomous-in-bounds** | Agent completes the task unattended; full audit trail; kill-switch active |

Hard boundaries regardless of tier: no agent owns a statutory filing path (BIR/SSS/PhilHealth/Pag-IBIG — human sign-off terminal); no agent acts on the POS/OT estate; no agent may hold SoD-conflicting duties (e.g., vendor-create + payment-approve); every agent action is audit-trailed as control evidence against the 808-control register.

### 12.2 Agent lifecycle (extends the VS-128 model discipline)

1. **Candidate intake** — the per-workflow Automation Opportunity inventory (5,406 workflows)
   plus VS-133 process mining surface candidates; scored by hours × frequency × error rate ×
   feasibility (derivable from each workflow's Time Estimate / Staffing Implication data).
2. **Proposal** — the **owning product team** (the team whose workflow it is) proposes with its
   BPO; SIB routes the sourcing (ERP-native automation = configure; vendor agent products =
   buy; custom agents on the paved road = build) — the same gate, one more domain.
3. **Registration & review** — agent registered in the VS-128 registry with a risk tier; AI
   ethics review for anything touching customers, employees, money, or personal data
   (RA 10173 DPIA where automated decisions affect data subjects).
4. **Evaluation** — offline evals → **shadow mode** (agent runs beside humans, no actions) →
   **canary** (bounded actions, sampled audit) — graduation gated by AAP's eval engineer and
   the owning team's QA analyst.
5. **Operation** — AAP runtime: tools are IAP contracts only (no direct database access);
   non-human identity with its own ERP roles; kill-switch with rule-based fallback; drift and
   cost telemetry; quarterly re-registration (or retirement).
6. **Sunset** — QBR portfolio review retires underperforming agents like any product.

### 12.3 Rollout posture (crawl → walk → run)

- **Crawl (read-only):** revenue-assurance leak candidates (VS-118), vendor-scorecard drafts
  (VS-67), LP exception triage (VS-23), store-audit prep, contract-clause checks (VS-100).
- **Walk (draft-with-approval):** PO/reorder drafts feeding the VS-02 ROP engine, journal-entry
  drafts for FIN's close pack, freight-audit matching proposals (VS-110).
- **Run (bounded autonomy on T2/T3):** returns triage, document classification (VS-88),
  planogram-compliance checks (VS-55), data-hygiene sweeps.

### 12.4 Workforce and change

Augmentation-first sequencing; VS-134 owns task redesign, reskilling, and adoption metrics;
CBA/labor-relations sensitivity (VS-84) is assessed before any agent that materially changes
a represented role; the Change & Training Lead pool carries rollout for the 6,762-user base.

## 13. Related Documents

| Document | Relationship |
|---|---|
| [`it-product-operating-model.md`](it-product-operating-model.md) | The operating model this sourcing strategy reshapes (v2.9: 17 teams incl. AAP, three archetypes, SEP, SIB, 122 FTE) |
| [`technical-guidelines.md`](technical-guidelines.md) | §1 POS/offline architecture protected by the Core-tier guardrail; §5 multi-vendor integration reference |
| [`../01-model-company/model-company-profile.md`](../01-model-company/model-company-profile.md) | §14.1 hybrid landscape (unified core + BoB edges + in-house products) |
| [`../01-model-company/data-volumes-and-integrations.md`](../01-model-company/data-volumes-and-integrations.md) | The ten external integration clusters and transaction volumes IAP dimensions against |
| [`../01-model-company/internal-controls-matrix.md`](../01-model-company/internal-controls-matrix.md) | The 808-control register every sourcing decision must map to |
| [`../01-model-company/headcount-reality-check.md`](../01-model-company/headcount-reality-check.md) | IT need band (65–80 pre-hybrid; 65–130 hybrid) the 122-FTE sizing lands in |

---

*Document Version: 2.2 | Date: 2026-09-05 | **Batch-18 gap-fill reconciliation:** the four channel-enforcement, employee-legal-status, OSH-enforcement & app-store-removal workflows (W5550 in PA-10.3; W5551 in PA-19.1; W5552 in PA-24.1; W5553 in PA-75.1; workflow-gap-analysis.md batch 18) true the §12.1 ladder's Tier-1 count 1,389 → 1,390 (W5552, the DOLE imminent-danger stop-work order — the OSH statutory-enforcement class) and Tier-2 count 3,278 → 3,281 (W5550/W5551/W5553; register 5,429 rows = 5,406 unique + 23 sub-workflow rows; Tier 3 unchanged at 758) and the §12.2 intake figure reads 5,406 workflows; the companion OM pin moves to v3.2. No program-rule changes — the agentic autonomy ladder obeys the workflow Tier register unchanged. Prior v2.1 (2026-09-05): **Batch-17 gap-fill reconciliation:** the six regulatory-shock, platform-outage & governance-continuity workflows (W5544 in PA-36.1; W5545/W5546 in PA-79.3; W5547 in PA-08.1; W5548 in PA-54.2; W5549 in PA-24.1; workflow-gap-analysis.md batch 17) true the §12.1 ladder's Tier-1 count 1,387 → 1,389 (W5545/W5546, the statutory-deadline-protection class) and Tier-2 count 3,274 → 3,278 (W5544/W5547/W5548/W5549; register 5,425 rows = 5,402 unique + 23 sub-workflow rows; Tier 3 unchanged at 758) and the §12.2 intake figure reads 5,402 workflows; the companion OM pin moves to v3.1. No program-rule changes — the agentic autonomy ladder obeys the workflow Tier register unchanged. Prior v2.0 (2026-09-05): **Emergency & continuity gap-fill reconciliation:** the eight emergency & continuity workflows (W5536/W5539 in PA-07.2; W5537/W5538 in PA-24.2; W5540 in PA-19.2; W5541 in PA-18.3; W5542 in PA-105.3; W5543 in PA-118.2; workflow-gap-analysis.md batch 16 — the same analysis produced the custody register's third wave, events E-19–E-22) true the §12.1 ladder's Tier-1 count 1,384 → 1,387 (W5536/W5537/W5538, the life-safety in-store emergency class) and Tier-2 count 3,269 → 3,274 (W5539–W5543; register 5,419 rows = 5,396 unique + 23 sub-workflow rows; Tier 3 unchanged at 758) and the §12.2 intake figure reads 5,396 workflows; the companion OM pin moves to v3.0. No program-rule changes — the agentic autonomy ladder obeys the workflow Tier register unchanged. Prior v1.9 (2026-09-04): **Demand-intake gap-fill reconciliation:** the §3 gate's upstream front door now has a workflow-level owner — **W5535** (Capability Demand Intake & Backlog Triage; PA-113.2 — raise → log & triage against the 188-VS catalog → route to team backlog / workflow-catalog gap-admission / the W5515 sourcing gate → Product-Council capacity funding, with an accepted/routed/declined-with-reason closed loop via the BPO; workflow-gap-analysis.md batch 15) — admitted directly confirmed Tier 2 — so the §12.1 ladder's Tier-2 count is trued 3,268 → 3,269 (register 5,411 rows = 5,388 unique + 23 sub-workflow rows; Tiers 1/3 unchanged at 1,384/758) and the §12.2 intake figure reads 5,388 workflows; the §3 intro names the front door explicitly; the companion OM pin moves to v2.9. No program-rule changes — the agentic autonomy ladder obeys the workflow Tier register unchanged. Prior v1.8 (2026-09-04): **Operations-workflow gap-fill reconciliation:** the three operations workflows (W5532 in PA-19.3; W5533 in PA-79.2; W5534 in PA-23.2; workflow-gap-analysis-operations.md) true the §12.1 ladder's Tier-1 count 1,383 → 1,384 (W5533, the statutory BIR 2316-furnishing admission) and Tier-2 count 3,266 → 3,268 (W5532/W5534; register 5,410 rows = 5,387 unique + 23 sub-workflow rows; Tier 3 unchanged at 758) and the §12.2 intake figure reads 5,387 workflows; the companion OM pin moves to v2.8. No program-rule changes — the agentic autonomy ladder obeys the workflow Tier register unchanged. Prior v1.7 (2026-09-03): **Finance-workflow gap-fill reconciliation:** the three finance workflows (W5529 in PA-42.3; W5530/W5531 in PA-17.3/PA-17.4; workflow-gap-analysis-finance.md) true the §12.1 ladder's Tier-2 count 3,265 → 3,266 (register 5,407 rows = 5,384 unique + 23 sub-workflow rows; Tier 1 rises 1,381 → 1,383 on the two statutory-execution admissions W5530/W5531, Tier 3 unchanged at 758) and the §12.2 intake figure reads 5,384 workflows; the companion OM pin moves to v2.7. No program-rule changes — the agentic autonomy ladder obeys the workflow Tier register unchanged. Prior v1.6 (2026-09-03): **People-capability & reporting-policy gap-fill reconciliation:** the four people/finance-policy workflows (W5525–W5527 in PA-19.4; W5528 in PA-17.4; workflow-gap-analysis-people.md) true the §12.1 ladder's Tier-2 count 3,261 → 3,265 (register 5,404 rows = 5,381 unique + 23 sub-workflow rows; Tier 3 unchanged at 758) and the §12.2 intake figure reads 5,381 workflows; the companion OM pin moves to v2.6. No program-rule changes — the agentic autonomy ladder obeys the workflow Tier register unchanged. Prior v1.5 (2026-09-03): **IT gap-fill reconciliation:** the seven VS-27 IT-operating-model workflows (W5518–W5524, workflow-gap-analysis-it.md) true the §12.1 ladder's Tier-2 count 3,256 → 3,261 and Tier-3 count 756 → 758 (register 5,400 rows = 5,377 unique + 23 sub-workflow rows) and the §12.2 intake figure reads 5,377 workflows. No program-rule changes — the agentic autonomy ladder obeys the workflow Tier register unchanged. Prior v1.4 (2026-09-03): **Sourcing-model gap-fill reconciliation:** the rest of this model's program machinery now has workflow-level owners — **W5515** (Sourcing Decision Gate Operation & Capability Sourcing Register; PA-113.3 — the §3 gate and §4 Register: scored configure → buy → build assessment, the §3.3 mandatory appendices incl. the 808-control mapping, SIB/Product-Council/CEO decision-rights routing, annual QBR reaffirmation and re-evaluation triggers), **W5516** (Best-of-Breed Product Lifecycle Management, Vendor Release Intake & Exit Reserves; PA-113.2 — the §8 lifecycle: staging-ring release intake with the Tier-1-mandatory regression pack, the defer-one-never-two upgrade-currency KPI, §8 contract-clause verification, tier-1 TPRM reassessment, QBR exit-reserve accrual), and **W5517** (SEP Paved Road & Engineering Standard Governance for Built Products; PA-113.1 — the §6/§7 standard: golden-path starts with ARB-recorded exceptions, trunk-based/feature-flag delivery, contract-first IAP + data contracts, ring deployment with SLO-burn rollback and the AppSec block right, production readiness review, DORA-at-QBR) — admitted directly confirmed Tier 2 — so the §12.1 ladder's Tier-2 count is trued 3,253 → 3,256 (register 5,393 rows = 5,370 unique + 23 sub-workflow rows) and the §12.2 intake figure reads 5,370 workflows. No program-rule changes. Prior v1.3 (2026-09-03): **Agentic gap-fill reconciliation:** the §12.2 agent lifecycle now has workflow-level owners — W5512–W5514 in VS-128.3 (intake/sourcing/registration, shadow & canary evaluation with autonomy-tier ratification, runtime/guardrail/kill-switch telemetry with quarterly re-registration & QBR sunset), admitted directly confirmed Tier 2 — so the §12.1 ladder's Tier-2 count is trued 3,250 → 3,253 (register 5,390 rows = 5,367 unique + 23 sub-workflow rows) and the §12.2 intake figure reads 5,367 workflows. No program-rule changes. Prior v1.2 (2026-09-03): **Consistency repair (§12.1 tier-count true-up):** the
autonomy ladder's tier figures are re-pointed to the criticality register's current Summary counts
(1,381 / 3,250 / 756 register rows; sum 5,387 rows = 5,364 unique workflows + 23 parent/summary
sub-workflow rows) — v1.1 had quoted the pre-confirmation snapshot (1,375 / 3,243 / 754 of the
5,372-row register as it stood before the 2026-09-02 post-catalog confirmation of
W5497–W5510 and the 2026-09-03 W5511 addition). Guarded going forward: validator Check 59
now re-derives this table from the register's Summary on every run. No program-rule changes.
Prior v1.1 (2026-09-03): **Agentic extension (with OM v2.1):** new §12
Agentic Automation Program — autonomy ladder wired to the workflow Tier register, agent
lifecycle (intake → SIB routing → VS-128 registration → shadow/canary evaluation → operation
→ QBR sunset), hard boundaries (statutory filings, POS/OT, SoD), crawl-walk-run posture, and
workforce/change rules (VS-134, VS-84); two register rows added (agentic runtime = build →
AAP; foundation-model access = buy under tier-1 TPRM); related-docs table renumbered to §13.
Prior v1.0 (2026-09-03): initial issue with the hybrid capability-sourcing decision
(unified ERP core + best-of-breed WMS/TMS/WFM/FSM edges + in-house OMO/TPS differentiators);
IT sizing impact in OM §9 (115 FTE at v2.0) and `optimal-table-of-organization.md`
(HQ 504 / total 6,904 at v1.3).*
