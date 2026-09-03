# BuildRight Depot Corp. — Target-State Table of Organization

> The **adopted target-state table of organization (TO)** for BuildRight Depot Corp. — board
> and governance lines, executive structure, department architecture, field organization,
> spans & layers, mandated roles, and steady-state sizing.
>
> **STATUS — ADOPTED AS TARGET STATE 2026-09-02.** The organization recognizes exactly two
> states. The **current baseline** is the minimum-coverage structure in
> [`model-company-profile.md`](model-company-profile.md) §3.3/§11.1 (HQ 362; total 6,762).
> The **target state** is this document: **HQ 511 / total 6,911** at 200 stores (revised
> 2026-09-03 for the hybrid IT capability-sourcing model + agentic-AI extension), reached
> through the three demand-triggered phases in §11. It does **not** rewrite current-state
> canon — every delta is stated explicitly (§5.1, §11), every figure traces to a source
> ([`headcount-reality-check.md`](headcount-reality-check.md) need bands;
> [`it-product-operating-model.md`](../07-methodology/it-product-operating-model.md) §9 —
> IT = 122 FTE; VS-177 field retail operating model), and each phase's promotion is
> CHANGELOG-recorded. The 300-store continuation of the target is defined in §12.

---

## 1. Purpose & Scope

- **Purpose**: define the *optimal* table of organization for this company — not just the
  minimum structure that closes known gaps (which is what the current baseline implements),
  but the steady-state design the company converges on as volumes, ecommerce ramp, and the
  200 → 300 store growth path materialize. Adopted as the company's target state on
  2026-09-02.
- **Scope**: the whole group — Board, Executive Office, the 18 HQ departments, the field
  retail layer (regions → districts → stores), the 4 DCs, and the 5 legal entities.
- **Out of scope**: individual names/grades, compensation bands, implementation Gantt
  (phasing triggers in §11 only), and store staffing redesign (29/store and 150/DC are
  affirmed, not changed — see §13).

### The two declared states

| State | HQ | Total | Status |
|---|---|---|---|
| **Current baseline** | 362 | 6,762 | Minimum-coverage TO implemented 2026-06-20/25 (profile §3.3) — canonical until phase triggers fire |
| **Target (this document)** | **511** | **6,911** | Adopted 2026-09-02 (HQ 469 / 6,869); revised 2026-09-03 for the hybrid IT capability-sourcing model (+35 IT) and agentic-AI extension (+7 IT); optimal steady state at 200 stores; phased per §11; scales per §12 |

**Design stance.** The current baseline (HQ 362) is the *minimum-viable* TO — the floor that
resolves the known gaps. The adopted target lands at **HQ 511** — the upper edge of the
reality-check's comfortable band (~440–515 after the 2026-09-03 hybrid + agentic revisions;
the band was ~440–470 under the unified-ERP model, when IT = 80), pushed to the top by
IT = 122 per the product
operating model) — reached through **three demand-triggered phases** (§11), never big-bang
hiring.

---

## 2. Design Principles

1. **Every value stream has exactly one accountable owner.** The 188 value streams / 569
   process areas map gap-free onto the TO (§4.2). The S&OP/IBP gap (VS-127 previously
   unowned) is the standing lesson: a program without a named home in the TO is a program
   that will fail.
2. **Legal-entity clarity, shared management.** Five SEC-registered entities, **one**
   management team. Each entity has a designated statutory officer (§6), but no duplicate
   functional departments. Intercompany flows (Depot↔Logistics, Depot↔Digital Commerce,
   Depot↔Property) are governed by the Related-Party Transactions Committee at arm's length.
3. **Regulatory-mandated roles are structurally protected** — never "absorbed" as part-time
   duties: DPO (RA 10173), MLRO/Compliance Officer (AMLA), Safety Officers & Company Nurse
   (RA 11058 / DOLE DO 198-18), Corporate Secretary (Revised Corporation Code). Full
   register in §10.
4. **Three-lines-of-defense risk model.** 1st line = operations (stores, DCs, function
   owners); 2nd line = Legal & Compliance + Risk; 3rd line = Internal Audit, functionally
   reporting to the Board Audit Committee — independence preserved by dotted line to the
   Board, administrative line to the CEO, financial-reporting coordination only with the CFO.
5. **Span-of-control discipline.** CEO ≤ 7; executive/department-head spans 5–8; store
   department supervisors 4–8; District Managers 10–15 stores; Regional Managers 2–3 DMs.
   Any span outside band requires CEO-approved exception (§9).
6. **Layer discipline: ≤ 8 layers** from CEO to store associate — the retail top-quartile
   ceiling. No inserting of coordination layers between DM and Store Manager, ever.
7. **Field-first, HQ-lean.** HQ designs and standardizes; the field executes and feeds back.
   The store support center is a service to stores, not an inspection bureaucracy. Target
   HQ-to-field ratio ≈ 8% (511 : 6,400 = 8.0%), inside the 6–10% big-box norm.
8. **Business-partner model over silos.** HRBPs sit in the regions; Finance partners sit
   with Supply Chain (S&OP finance) and Merchandising (OTB/margin); IT Product Owners pair
   with Business Product Owners in every department (per the IT operating model). The TO
   shows solid lines, but work flows through these pairings.
9. **Scale through the field layer, not HQ.** Store growth adds regions, districts, and
   store staff roughly linearly, but HQ grows at ≤ half that rate by design (§12) — the
   unified ERP absorbs transaction volume without proportional headcount.
10. **Minimum viable org at every stage.** Even the optimal TO contains no speculative
    headcount: every box traces to a named workload driver (transaction volume, statutory
    obligation, or value-stream ownership).

---

## 3. The Master Org Chart

```
                         BOARD OF DIRECTORS — BuildRight Holdings, Inc.
                         ├── Audit Committee ························┐ (functional line)
                         ├── Related-Party Transactions Committee   │
                         ├── Nomination & Compensation Committee    │
                         └── Risk Committee                         │
                                                                    │
        ┌───────────────────────────────────────────────────────────┘
        │
   CEO / PRESIDENT
   │
   ├── CFO ──────────────────────────── Finance & Accounting ···· Internal Audit & Risk (adm.)
   │                                      Treasury · Tax · FP&A     (functional → Audit Committee)
   │
   ├── COO ──────────────────────────── Store Operations ···· Supply Chain & Logistics
   │                                      (6 RM → 13 DM → 200       (S&OP/IBP · DC Ops · Procurement
   │                                       stores; +4 DCs)          · Fleet · Imports · Vendor Mgmt)
   │                                   Facilities & Real Estate ··· Quality Management
   │                                   Regional Loss Prevention ··· Customer Service
   │                                   Trade / Account Management
   │
   ├── CIO ──────────────────────────── Information Technology (9 domain + 7 platform product
   │                                      teams + CIO Office = 122 FTE; DPO administrative line)
   │
   ├── CMO ──────────────────────────── Marketing (brand · promo · loyalty · digital · retail
   │                                      media · insights) [+ GM, Digital Commerce Inc. — dotted]
   │
   ├── CHRO ─────────────────────────── Human Resources ···· Health, Safety & Environment
   │
   ├── VP LEGAL & COMPLIANCE ────────── Legal & Compliance (CorpSec · regulatory · contracts
   │                                      · MLRO · DPO functional line) ···· Sustainability / ESG
   │
   └── VP MERCHANDISING ─────────────── Merchandising & Buying (5 category pods · planning
                                          · pricing · private brand · master data)
        [+ Corporate Planning & Strategy — CEO office]
```

**Reading the chart.** Seven executives + CEO's strategy staff = Executive Office (7) plus a
strategy cell; 18 HQ departments total, exactly as the current baseline (profile §11.1) — the target state keeps
the current executive architecture (it is sound) and optimizes *below* it: sizing, sub-team
structure, field layer, governance bodies, and mandated-role protection.

### 3.1 Full department tree (3 reporting levels)

```
CEO
├── CFO
│   ├── VP Finance & Accounting / Corporate Controller ——— sub-teams §5.2
│   │     Technical Accounting · GL & Consolidation · AP · AR & Credit · Treasury · Tax ·
│   │     FP&A · Revenue Assurance · Logistics & Cost Finance
│   └── Head of Internal Audit & Risk ——— functional line to Board Audit Committee
│         Financial audit · IT/ERP audit · ERM · fraud & special investigations
├── COO
│   ├── VP Store Operations ——— Store Support Center + Field Layer (§7)
│   │     6 Regional Managers → 13 District Managers → 200 Store Managers
│   ├── VP Supply Chain & Logistics (dual-hat GM, BuildRight Logistics, Inc.)
│   │     S&OP/IBP sub-team (owns VS-127) · DC Operations (4 DCs) · Fleet & Logistics ·
│   │     Procurement/PO Execution · Imports & Customs · Vendor Management · Inventory Planning
│   ├── Director, Facilities & Real Estate (dual-hat GM, Property Mgmt Inc.)
│   │     Facilities engineering · maintenance coordination · lease & surety admin · energy mgmt
│   ├── Head of Quality Management — incoming inspection · vendor QA · metrology
│   ├── Director, Regional Loss Prevention — 20 field LP Officers · investigations · analytics
│   ├── Head of Customer Service — contact center · trade desk · ecommerce support
│   └── Head of Trade / Account Management — key accounts · trade professional program (VS-43)
├── CIO
│   └── IT product portfolio (see it-product-operating-model.md §3–§5)
│         Domain: MSC · WLI · SSP · CCP · FIN · CORP · PEO · OMO · TPS
│         Platform: IAP · INFRA · SEC · DP · SEP · AAP · FS (+ CIO Office)
├── CMO
│   └── VP Marketing — brand & creative · promotions · loyalty/CRM · digital ·
│         retail media & marketplace · insights · marketing ops
├── CHRO
│   ├── VP HR — talent acquisition · HRBPs (field) · comp & ben · payroll ops ·
│   │          HR shared services · L&D · labor relations · HRIS
│   └── Head of HSE — safety officers (regional) · company nurse · wellness
├── VP Legal & Compliance
│   ├── Corporate Secretary · contracts & commercial · litigation & IP ·
│   │   regulatory & government affairs · compliance & MLRO · privacy (DPO)
│   └── Head of Sustainability / ESG — environmental · social · governance reporting
└── VP Merchandising
    └── 5 Category-Manager pods (buyer + planner each) · pricing · assortment & space ·
        direct sourcing · private brand · promotions/vendor funding · merch ops & master data
```

---

## 4. Executive Remits

### 4.1 Span and department portfolio

| Executive | Direct reports (dept heads) | Target dept HC | Span verdict |
|---|---|---|---|
| CEO / President | 7 (six officers + VP Merchandising) + strategy cell | 47 (+ Exec Office 7) | ✅ at ceiling, by design |
| CFO | 2 + Controller org | 71 (Finance 62 + IA 9) | ✅ |
| COO | 7 | 155 (7 depts) | ✅ at ceiling — all operations under one P&L |
| CIO | 2 (Head of EA / portfolio, FinOps & vendor-portfolio) via CIO Office; 17 product teams | 122 | ✅ (platform-led span) |
| CMO | 1 + dotted GM Digital Commerce Inc. | 30 | ✅ light span absorbs retail-media growth |
| CHRO | 2 | 55 | ✅ |
| VP Legal & Compliance | 2 + CorpSec (statutory) | 24 | ✅ |
| **Total** | **18 departments + Executive Office** | **504 + 7 = 511** | |

### 4.2 Value-stream family ownership (gap-free)

| Value-stream family (188 VS total) | Accountable executive | Co-owner / delivery partners |
|---|---|---|
| **Plan & Source** | COO | VP Merchandising (assortment strategy), VP Supply Chain (S&OP/IBP chairs demand-supply consensus) |
| **Make & Move** | COO | VP Supply Chain (DC ops, fleet, inventory); Quality (incoming inspection) |
| **Sell & Serve** | COO | CMO (digital demand), VP Store Ops (store execution), Trade Acct Mgmt (B2B) |
| **Finance** | CFO | Controller (R2R), Treasury, Tax; S&OP finance partner |
| **People** | CHRO | HRBP field layer; HSE for workplace safety VS |
| **Asset & Infrastructure** | COO | Facilities & RE (property, construction); CFO (asset accounting, capex controls) |
| **Governance & Assurance** | VP Legal & Compliance (2nd line) + Head of IA (3rd line) | Embedded control owners in every 1st-line dept (808 controls, internal-controls-matrix.md) |
| **Technology & Data** | CIO | Business Product Owners in every department |

---

## 5. HQ Department Design

### 5.1 Target-state sizing summary (18 departments + Executive Office)

| # | Department | Current (baseline) | Reality-check band | **Target** | Primary workload driver |
|---|---|---|---|---|---|
| 1 | Executive Office | 7 | 7 | **7** | — |
| 2 | Finance & Accounting | 46 | 58–68 | **62** | ~9,000 AP invoices/mo; 5 entities; PFRS 15; monthly VAT ×5 |
| 3 | Merchandising & Buying | 40 | 40–45 | **43** | 35K active SKUs; 6 promo events/yr; competitive pricing (VS-57) |
| 4 | Supply Chain & Logistics | 40 | 42–50 | **46** | 800–1K vendors; 400–600 TEU/mo; VS-127 consensus cycle; 4 DCs |
| 5 | Information Technology | 50 | 65–130 | **122** | 17 product teams per it-product-operating-model.md §9.1 (authoritative — hybrid capability-sourcing + agentic-AI model, 2026-09-03) |
| 6 | Human Resources | 26 | 38–48 | **42** | 6,800+ staff; ~1,400 hires/yr; 13,400+ payslips/mo; CBA (VS-84) |
| 7 | Marketing | 25 | 28–34 | **30** | Loyalty 600K members; retail media (VS-48); marketplace (VS-95); ecom ramp 3→7% |
| 8 | Store Operations | 24 | 24 | **24** | 6 RM + 13 DM + store support center (VS-177) |
| 9 | Legal & Compliance | 14 | 18–24 | **20** | Highest role density: AML/ABC, DPA, SEC, multi-LGU (200 stores) |
| 10 | Internal Audit & Risk | 7 | 8–10 | **9** | 5-entity audit universe; ERM; TPRM; fraud investigations |
| 11 | Customer Service | 30 | 30–45 | **34** | Hybrid central contact center + store CSR network; B2B desk |
| 12 | Regional Loss Prevention | 20 | 25–30 | **27** | VS-23 exception monitoring; shrink < 1.5%; 20 field officers |
| 13 | Health, Safety & Environment | 10 | 12–15 | **13** | RA 11058/DO 198-18 safety officers; nurse; wellness |
| 14 | Quality Management | 4 | 5–6 | **5** | Incoming inspection (VS-31); recalls; metrology (catch-weight) |
| 15 | Facilities & Real Estate | 8 | 10–15 | **12** | 200 stores + 4 DCs + HQ; energy mgmt; VS-42 lease/surety admin |
| 16 | Sustainability / ESG | 3 | 3–4 | **4** | VS-25; DENR; ESG reporting cadence |
| 17 | Strategy / Corp Planning | 3 | 4–5 | **4** | Annual plan; CPM; competitive intelligence (VS-33) |
| 18 | Trade / Account Management | 5 | 6–8 | **7** | 5,200 trade accounts; VS-43 program; VS-107 key accounts |
| | **Total HQ** | **362** | **~440–515** | **511** | |
| | Store personnel | 5,800 | OK | **5,800** | 29/store affirmed (§13) |
| | DC personnel | 600 | OK | **600** | 150/DC affirmed (§13) |
| | **Total company** | **6,762** | | **6,911** | Revenue/employee ≈ PHP 9.01M |

> 511 lands inside the reality-check comfortable band (~440–515, as amended 2026-09-03) at
> its upper edge — the increment over ~470 is IT at 122 (hybrid capability-sourcing +
> agentic model), sized independently and authoritatively by the IT product operating model
> §9.2. The IT band was extended 65–80 → 65–130 and the HQ band ~440–470 → ~440–510 →
> ~440–515 by the 2026-09-03 hybrid + agentic decisions; all other department bands are
> unchanged.

### 5.2 Sub-team architecture (where structure changes, not just size)

**Finance & Accounting (62)** — the largest rebuild. Transaction automation (3-way match,
e-invoicing) lets clerks process 700–800 invoices/month, so the optimal shape adds
*analysis-heavy* capacity, not clerk capacity:

| Sub-team | HC | Mandate |
|---|---|---|
| Corporate Controller | 1 | Owns close (≤ 5 days), consolidation, control environment |
| Technical Accounting & Policy | 4 | PFRS 15 multi-element revenue, IFRS 16, policy memos |
| GL & Consolidation | 7 | GL accountant per entity (5) + consolidation/elimination (2) |
| Accounts Payable | 16 | Mgr + 2 sups + 13 clerks ≈ 8,500–9,500 invoices/mo |
| AR & Credit | 8 | Mgr + collections (3) + credit review/limits (4) for 5,400 accounts |
| Treasury & Banking | 6 | Daily sweeps, FX, LC funding, petty-cash control |
| Tax | 6 | VAT/WHT/income across 5 entities; BIR eFPS; LGU tax |
| FP&A | 7 | Annual plan linkage to Strategy; store P&L; S&OP finance partner |
| Revenue Assurance | 2 | VS-157 leak detection (promo/POS/pricing errors) |
| Logistics & Cost Finance | 4 | Intercompany service fees; landed cost; DC cost-to-serve |
| Payroll Accounting Liaison | 1 | Semi-monthly interface, 6,800+ staff |

**Supply Chain & Logistics (46 = current 40 + 6)** — the S&OP/IBP sub-team is preserved
exactly; growth goes to execution depth:

| Sub-team | HC (now → optimal) | Mandate |
|---|---|---|
| VP Supply Chain (dual-hat GM, Logistics Inc.) | 1 | P&L; reports to COO |
| S&OP/IBP sub-team (owns VS-127) | 5 → 5 (unchanged) | Lead + Sr Demand Planner + 2 Demand Planners + Supply & Allocation Planner |
| DC Operations | 8 → 10 | 2 coordinators per DC + load growth |
| Fleet & Logistics | 6 → 6 | 80% 3PL orchestration; inter-island freight |
| Procurement / PO Execution | 8 → 9 | ~18,000 PO lines/mo |
| Imports & Customs | 5 → 6 | 400–600 TEU/mo; in-house brokerage |
| Vendor Management | 4 → 4 | 800–1K vendors; scorecards |
| Inventory Planning | 3 → 5 | ROP/safety-stock policy; VS-136 multi-echelon |

**Human Resources (42)** — converts from transaction-centric to field-partnered:

| Sub-team | HC | Mandate |
|---|---|---|
| VP HR | 1 | Reports to CHRO |
| Talent Acquisition | 8 | ~1,200–1,600 hires/yr; store-level pipelines |
| HR Business Partners (field) | 6 | 1 per region, embedded with RMs |
| Compensation & Benefits | 4 | Grades, statutory benefits, CBA economics |
| Payroll Operations | 8 | 5 entities × 2 runs/mo; SSS/PhilHealth/Pag-IBIG/BIR remittance |
| HR Shared Services | 5 | Employee lifecycle admin; VS-103 people services |
| Learning & Development | 5 | Store onboarding at scale; POS/safety/product training |
| Labor Relations | 3 | CBA, grievance, DOLE matters (VS-84) |
| HRIS & Analytics | 2 | System of record; workforce analytics |

**Legal & Compliance (20)** — sub-disciplines that the workflows demand (§3.4 of the reality
check): Corporate Secretary (2) · Regulatory & Government Affairs (4, multi-LGU VS-22/76/104) ·
Contracts & Commercial (5) · Compliance & AML/MLRO (3) · Privacy/DPO (2) · Litigation & IP (2) ·
Customs & Trade liaison (1) · VP Legal (1).

**Marketing (30)** = canon 25 + retail media & marketplace (3, VS-48/VS-95) + digital/ecommerce
growth (2) as penetration ramps 3% → 7%.

**Customer Service (34)** — resolves the reality check's open decision: **hybrid model**.
Central contact center (24: 2 sups + 22 agents, tiered voice/chat/email for 2.8M transactions'
worth of inquiries + returns + BOPIS support), B2B/trade desk (4, aligned to Trade Acct Mgmt),
QA & workforce management (2), ecommerce fulfillment support (3), Head (1).

**Store Operations (24, unchanged)** = 6 Regional Managers + 13 District Managers + 5-person
Store Support Center (standards, communications VS-63, facilities coordination, OpEx/continuous
improvement, store-opening task force VS-37). Full field model per VS-177.

**Regional Loss Prevention (27)** = Director + 20 Regional LP Officers (field) + central
investigations (3) + exception-reporting analytics (3) — the VS-23 monitoring loop.

**HSE (13)** = Head + 10 Safety Officers (regional coverage model, 1 per region + mobile) +
Company Nurse + wellness coordinator. (Per-store safety duties are held by trained store staff
— the ASM holds the Safety Officer 1 duty per DO 198-18 tiering.)

**Quality (5) · Facilities & RE (12, incl. Energy Manager) · ESG (4) · Strategy (4) ·
Trade/Acct Mgmt (7)** — as profiled in §5.1; each closes a named-role gap from the reality
check (metrology, energy manager, competitive intelligence, key-account managers).

**Information Technology (122)** — governed by the IT product operating model, not restated
here: 9 stream-aligned domain products (7 configure / buy-and-integrate teams paired to
business owners + the two in-house **build** squads OMO and TPS), 7 platform teams
(integration, infra, security/GRC, data, engineering enablement, agentic enablement,
field services), CIO Office.
Target = 122 (authoritative steady-state sizing under the hybrid capability-sourcing +
agentic model, mid-band of the 65–130 hybrid need band).

---

## 6. Legal-Entity Overlay & Statutory Officers

One management team runs five entities; each entity retains its statutory organs:

| Legal entity | Management line | Statutory officers (RCC) | Notes |
|---|---|---|---|
| **BuildRight Holdings, Inc.** | CEO/President | Chair, VP Legal (CorpSec), Treasurer (CFO) | Board + 4 committees (§3) |
| **BuildRight Depot, Inc.** | COO (chief retail officer de facto) | President (CEO), Treasurer (CFO) | Owns all merchandise inventory chain-wide |
| **BuildRight Logistics, Inc.** | VP Supply Chain = **dual-hat GM** | GM + Treasurer (CFO) | Service-fee model, not goods resale |
| **BuildRight Digital Commerce, Inc.** | GM reporting to CMO (solid) / CEO (entity duties) | GM + Treasurer (CFO) | Collects online payments; revenue recognized at fulfillment |
| **BuildRight Property Mgmt, Inc.** | Director Facilities & RE = **dual-hat GM** | GM + Treasurer (CFO) | Leases sites to Depot Inc. at arm's length |

Rules: (a) all intercompany pricing is approved annually by the Related-Party Transactions
Committee; (b) each entity's books are kept by the per-entity GL accountants (Finance sub-team);
(c) dual-hat GMs carry explicit entity-duty objectives so service-entity obligations (BIR, SEC,
LGU) are never orphaned.

---

## 7. Field Organization

### 7.1 Retail field layer (VS-177 operating model)

```
COO → VP Store Operations
      ├── Regional Manager ×6          (NCR · North/Central Luzon · South Luzon · Visayas ·
      │      │                          Mindanao-split; each 25–40 stores)
      │      └── District Manager ×13   (each ~15 stores; visit cadence per VS-177)
      │             └── Store Manager ×200  (29 staff each — §7.2)
      ├── Regional LP Officers ×20     (dotted to Director, Regional Loss Prevention)
      ├── HRBP ×6                      (dotted to VP HR; embedded in regions)
      └── Store Support Center (5)
```

- **Spans**: RM → 2–3 DMs; DM → ~15 stores; SM → 8 direct (below).
- **Layer count, CEO → floor**: CEO → COO → VP Store Ops → RM → DM → SM → Dept Supervisor →
  Associate = **8 layers** ✅.
- LP Officers and HRBPs are **field-dotted**: they live in the region, report professionally
  to their HQ function — preserving independence (LP) and consistency (HR) without adding
  regional bureaucracy.

### 7.2 Store organization (29 per store — affirmed)

| Reports-to | Roles | Span |
|---|---|---|
| Store Manager | ASM; 4 Department Supervisors; Receiving pair (lead clerk + 1); Maintenance | 8 |
| Assistant Store Manager | 3 Cashiers; Customer Service Rep; Receiving lead (dotted); Maintenance (dotted); holds Safety Officer 1 duty | ~6 |
| Department Supervisor (×4: Lumber/Building, Plumbing/Electrical, Tiles/Flooring, Tools/Hardware) | 3 Sales Associates + 1 Stock Associate each | 4 |

### 7.3 DC organization (150 per DC — affirmed)

**Management line:** DC Manager → DC Operations Coordinator (HQ-side, in the Supply Chain
DC-Ops sub-team — 2 per DC, **not** part of the 150) → VP Supply Chain → COO.
**7 layers** CEO → DC floor ✅. Fleet drivers are excluded (80% 3PL, VS-06); gatehouse
security is contracted. DCs run two shifts (inbound-weighted morning, outbound-weighted
afternoon); DC3 (40,000 sqm) may split the AM roles into two each during peak.

| Function | Role | HC | Notes |
|---|---|---|---|
| **Management & support (9)** | DC Manager | 1 | Site P&L; span 6 |
| | Assistant DC Manager — Inbound | 1 | Receiving, putaway, cross-dock, special handling |
| | Assistant DC Manager — Outbound | 1 | Pick/pack, staging, dispatch |
| | Shift Supervisors | 4 | 2 per shift (VS-04 role) |
| | Safety & Compliance Coordinator | 1 | Functional line to HSE; OSH, hazmat, DENR permits |
| | DC Office Administrator | 1 | Timekeeping, HR liaison, records |
| **Inbound (51)** | Receiving Supervisor | 2 | VS-04 PA-04.1 |
| | Receiving Clerks | 14 | ~50 receipts/day/DC, ASN-driven |
| | Incoming Inspection Checkers | 4 | Dotted to Quality (VS-31) |
| | Putaway Staff | 10 | RF-directed |
| | Forklift Operators (inbound) | 15 | Reach/counterbalance |
| | Cross-Dock Team | 6 | Fast-mover sort & stage |
| **Outbound (50)** | Outbound/Shipping Supervisor | 2 | VS-04 PA-04.2 |
| | Order Pickers | 24 | RF-directed, full-case + each |
| | Packers / Load Builders | 14 | Multi-drop load consolidation (2–3 ROs/truck) |
| | Loaders / Staging | 8 | ~25 outbound trucks/day/DC |
| | Dispatch Coordinators | 2 | Routing, 3PL carrier handoff |
| **Special handling (19)** | Special Handling Lead | 1 | Reports to AM Inbound |
| | Lumber / Long-Length Crew | 8 | Manual + crane handling |
| | Tile & Heavy/Breakbulk Crew | 6 | Pallet integrity |
| | Certified Hazmat/Paint Handlers | 4 | Paint/chemicals; DENR-compliant storage |
| **Inventory control (15)** | Inventory Control Supervisor | 1 | Reports to DC Manager |
| | Cycle Counters | 9 | Weekly cycle count program (VS-05) |
| | Discrepancy Analysts | 2 | GR/IR variances < 24h resolution |
| | Returns Processors | 3 | Reverse logistics staging (VS-32) |
| **Maintenance (6)** | MHE Maintenance Technicians | 4 | Forklifts, dock doors, conveyors |
| | Facilities/Utility | 2 | Site upkeep |
| | **Total** | **150** | × 4 DCs = **600** |

> Roster is a target-state instantiation of the canon "~150 per DC" (profile §3.2), built
> from the VS-04 role vocabulary; per-DC mix flexes ±10% by size and cross-dock share,
> with the 150 total held.

---

## 8. Governance Bodies & Operating Cadence

| Body | Cadence | Chair | Core mandate |
|---|---|---|---|
| Executive Committee | Weekly | CEO | Cross-functional decisions; escalations |
| Executive S&OP / IBP review | Monthly | COO (+ CFO) | VS-127 consensus sign-off; demand-supply-inventory trade-offs |
| S&OP working cycle | Monthly (wk 1–3) | S&OP/IBP Lead | PA-127.1/127.2 cycle feeding exec review |
| Merchandising & Promo Council | Bi-monthly | VP Merchandising | Catalog events, markdowns, vendor funding |
| Pricing Exception Review Board | Weekly | VP Merchandising (CFO delegate) | Price-override / margin-exception approvals |
| Architecture Review Board | Bi-weekly | Head of EA (CIO) | VS-113; configuration & integration standards |
| Sourcing & Investment Board | Monthly + on demand | CIO | Configure/buy/build routing per the capability sourcing model; Capability Sourcing Register; agent autonomy ratifications |
| IT Product Council / QBR | Monthly / Quarterly | CIO | Product backlogs, KPIs, funding |
| Risk & Compliance Committee | Monthly | VP Legal & Compliance | ERM, AML/ABC, privacy, TPRM dashboard |
| Data Privacy Council | Quarterly | DPO (functional to VP Legal) | DPA/NPC posture, breach readiness |
| Board Audit Committee | Quarterly | Independent director | IA functional line; financial reporting; IC effectiveness |
| Related-Party Transactions Cttee | Semi-annual + as needed | Independent director | Arm's-length IC pricing (5 entities) |
| Crisis Management / BCP Team | On trigger + semi-annual drill | COO | VS-26; typhoon/response playbooks |

---

## 9. Span & Layer Discipline

| Level | Target span | Target TO value | Status |
|---|---|---|---|
| CEO → officers | ≤ 7 | 7 (+strategy cell) | ✅ |
| Officer → dept heads | 5–8 | CFO 2 · COO 7 · CIO 2 (via CIO Office) · CMO 1 · CHRO 2 · VP Legal 2 · VP Merch 1 | ✅ |
| Dept head → managers | 5–8 | 4–7 across §5.2 sub-teams | ✅ (min 4 is deliberate for specialist pods) |
| RM → DMs | 2–3 | 2–3 | ✅ |
| DM → stores | 10–15 | ~15 | ✅ |
| Store Manager | 6–10 | 8 | ✅ |
| Dept Supervisor (store) | 4–8 | 4 | ✅ |
| **Layers (CEO → associate)** | **≤ 8** | **8** | ✅ |
| **HQ : field ratio** | 6–10% | 511 : 6,400 = **8.0%** | ✅ |

Exceptions policy: any new box that violates band/layer rules needs ExCo sign-off with a
workload justification — the mechanism that prevents silent org creep between redesigns.

---

## 10. Mandated-Role Register (structurally protected)

| Role | Legal basis | Structural home | Protection |
|---|---|---|---|
| Data Protection Officer | RA 10173 (NPC) | Privacy sub-team, Legal & Compliance; **administrative** line to CIO, **functional** line to VP Legal/CEO | Cannot be bundled with marketing/IT delivery duties |
| MLRO / AML Compliance Officer | AMLA (as applied to covered services, VS-86) | Compliance & AML sub-team, Legal & Compliance | Direct access to CEO and Audit Committee |
| Corporate Secretary | Revised Corporation Code | Legal & Compliance | Board-facing; not subordinate to CFO |
| Head of Internal Audit | Corporate governance best practice (SEC Code) | IA & Risk | **Functional line to Board Audit Committee** — appointment/removal by Committee |
| Safety Officers (SO2/SO3) | RA 11058 · DOLE DO 198-18 | HSE (regional coverage) | DOLE-accredited; termination requires HSE Head review |
| Company Nurse / First-aiders | DOLE OSH standards | HSE + trained store first-aiders | 1 nurse centrally; first-aider per store among staff |
| Energy/Environmental focal | DENR interaction (VS-73) | Facilities (Energy Mgr) / ESG | Permits & reporting calendar owned |
| Tax liaison / accredited agent | BIR CAS & eFPS | Tax sub-team, Finance | Per-entity registration hygiene |

---

## 11. Sizing & Phasing — Current 362 → Target 511

The adopted target state is reached through three demand-triggered phases (no speculative
hiring; each phase has explicit triggers):

| Phase | Horizon | Moves | HC delta |
|---|---|---|---|
| **1 — Regulatory floor** | 0–6 mo | Legal 14→20 (MLRO cell, privacy staff, gov-affairs); HSE 10→13 (SO coverage + nurse); IA 7→9 | +18 |
| **2 — Transaction scale** | 6–18 mo | Finance 46→62 (tied to AP-automation threshold: ≤800 inv/clerk/mo); CS 30→34 (hybrid model decision) | +26 |
| **3 — Capability scale** | 18–36 mo | IT 50→122 (per the hybrid + agentic product-model sequencing, OM §9.3); HR 26→42 (field HRBPs as regions mature); SC 40→46; Merch 40→43; Marketing 25→30; LP 20→27; Facilities 8→12; Quality 4→5; ESG/Strategy/Trade top-ups | +105 |
| | | **Total** | **362 → 511 (+149)** |

**Guardrails.** Total HQ never exceeds the 440–515 band (as amended 2026-09-03 for the
hybrid + agentic IT model) at 200 stores; any phase that would
breach it defers into the next scaling review (§12). Store/DC staffing unchanged throughout.
Each phase promotion is recorded in [CHANGELOG.md](../CHANGELOG.md) and flips the affected
§5.1 row from *target* to *current* — the mechanism that keeps the two states honest.

---

## 12. Scaling Path — 200 → 300 Stores

| Dimension | At 200 stores | At ~300 stores | Rule |
|---|---|---|---|
| Stores | 200 | 300 (+10–15/yr ≈ 7 yrs) | — |
| Store staff | 5,800 | ~8,700 | linear, 29/store |
| DCs | 4 (DC4 oversized for growth) | 4–5 (add Visayas/Mindanao capacity if >260) | trigger: DC utilization > 85% sustained |
| Regions | 6 | 8 | trigger: >40 stores/region |
| Districts | 13 (~15 stores) | 20 | linear |
| Regional LP Officers | 20 | 30 | 1 per ~10 stores |
| Store Ops HQ | 24 | 30 | support-center grows sub-linearly |
| HR / CS / Finance / IT | 42 / 34 / 62 / 122 | 52 / 45 / 70 / 135 | HQ grows at ≤ half the store rate via ERP automation |
| **HQ total** | **511** | **~575** | discipline: ~8% → ~5% of company |
| **Company total** | **6,911** | **~9,900** | revenue/employee ≥ PHP 9M preserved |

---

## 13. What Deliberately Does NOT Change

1. **Store staffing model (29/store)** and **DC staffing (150/DC)** — reality check §6
   affirms both; peak coverage via flex pool, not base FTE.
2. **The 7-executive / 18-department architecture** — spans and ownership are sound; the
   optimal work happens below the executive layer. (Considered and rejected: merging
   Merchandising under a combined CMMO to trim CEO span — rejected because merchandising is
   the P&L core of big-box retail and deserves direct CEO access.)
3. **S&OP/IBP sub-team (5)** — exactly as stood up 2026-06-25; it is the template for
   principle #1 (single ownership of consensus programs).
4. **Inventory ownership chain-wide by Depot Inc.** and the service-fee intercompany model —
   org follows this, not vice versa.
5. **Internal Audit independence mechanics** (functional → Audit Committee) as codified in
   profile §11.1 note ¹.

---

## 14. Organizational Health Metrics (how we know the TO is working)

| Metric | Target |
|---|---|
| Span compliance (managers within band) | ≥ 90% |
| Layer count (deepest path) | ≤ 8 |
| HQ : field ratio | 6–8% |
| Manager : employee ratio (company-wide) | ~1 : 11 |
| Vacancy rate (critical roles: MLRO, DPO, Safety Officers, S&OP Lead) | 0% |
| Time-to-fill, frontline roles | < 45 days |
| Internal fill rate, DM/RM promotions | ≥ 60% |
| Value streams with named accountable owner | 100% (audited quarterly) |

---

## 15. Cross-References

| Document | Relationship |
|---|---|
| [`model-company-profile.md`](model-company-profile.md) §3.3/§11.1 | Current canonical TO (minimum-viable, HQ 362) this design optimizes |
| [`headcount-reality-check.md`](headcount-reality-check.md) | Need bands (§2 table) and named-role gaps (§4) driving optimal sizing |
| [`it-product-operating-model.md`](../07-methodology/it-product-operating-model.md) | Authoritative IT structure & sizing (122 FTE, 17 product teams) |
| `workflows/VS-177-…` | Field retail operating model (RM/DM cadence) this TO instantiates |
| `workflows/VS-127-…` | S&OP/IBP cycle owned by the Supply Chain sub-team |
| [`internal-controls-matrix.md`](internal-controls-matrix.md) | 808 controls embedded in 1st-line departments (three-lines model, §2 principle 4) |

---

*Document Version: 1.4 | Date: 2026-09-03 | **Agentic-AI extension** (with
`it-product-operating-model.md` v2.1): IT target 115 → 122 (17 product teams: +AI & Agent
Platform), target HQ 504 → 511 and company total 6,904 → 6,911; HQ band extended
~440–510 → ~440–515 (IT band 65–130 unchanged — 122 stays mid-band); §11 Phase 3 +98 →
+105 and total +142 → +149; §12 scaling rows re-based (IT 122 → ~135 at 300 stores; HQ
~575); §8 SIB row gains agent autonomy ratifications; revenue/employee ≈ PHP 9.01M.
Prior v1.3 (2026-09-03): hybrid capability-sourcing revision — IT 80 → 115 (16 teams), HQ
469 → 504 / 6,869 → 6,904, bands IT 65–130 / HQ ~440–510, §12 re-based, SIB added.
Prior v1.2 (2026-09-02): adopted as the BuildRight target-state TO; two-state framing
declared (§1); guardrails extended with CHANGELOG-recorded phase promotion (§11). v1.1
(consistency review #68): §7.3 DC-roster Outbound group-total label trued; §15
internal-controls cross-reference made mechanically resolvable. Under the permanent
regression guard of `07-methodology/audit-model-docs.py` (validator Check 59), including a
structural rule that re-derives every §7.3 roster group total from its own HC cells.
v1.0 (2026-09-02): initial issue. Current-state canon (model-company-profile.md §3.3/§4/§11.1
— HQ 362 / total 6,762) is unchanged; the deltas in §5.1/§11 define the target until each
phase trigger fires.*
