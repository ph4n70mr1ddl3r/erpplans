# Changelog

> Track major changes to the BuildRight Depot ERP Plans repository.
>
> **Note (2026-06-21):** This file was condensed from ~4,100 lines to improve navigation.
> Every dated entry and factual change is preserved below; verbose rationale that already
> lives in code comments, commit messages, or [`workflow-gap-analysis.md`](01-model-company/workflows/workflow-gap-analysis.md)
> was trimmed. The 30 repetitive gap-analysis passes are unified into a single summary table.

---

## 2026-06-26 — Consistency review #11: 4,618 TOC anchors broken on GitHub (collapsing-slugger bug); fix-toc-anchors.py v2 + Check 23 slugger correction

An independent whole-repo review (validator green at 0 errors / 3 informational warnings across all 25 checks; every headline figure re-derived independently — 188 VS directories / 569 PA files / 5,349 unique `## W` IDs with 0 duplicates / 733 unique requirement IDs with 0 true duplicates after letter-suffix disambiguation / 67 unique controls / root-README folder-tree counts vs disk / index per-VS rows vs disk / all 188 VS-README per-PA count tables & totals vs actual PA headers / all 3,434 relative .md links repo-wide resolving / all 26 non-PA intra-file anchors resolving / 733 matrix rows reconciling) found one systemic defect class invisible to every existing check: **PA TOC anchors that resolve under a collapsing slugger but not on GitHub.** Canonical totals unchanged: **188 value streams · 569 process areas · 5,349 workflows · 733 requirements · 67 controls**.

1. **The defect.** GitHub's slugger (github-slugger) removes punctuation and then replaces *each* space with `-` WITHOUT collapsing adjacent hyphens, so spaced punctuation (` & `, ` / `) renders as a **double** hyphen: `W1. Merchandise Planning & Assortment Review` → `#w1-merchandise-planning--assortment-review`. The PA TOC generator (and, inadvertently, review #9's repairer and validator Check 23) collapsed `[\s_-]+` runs to one `-`, producing `#w1-merchandise-planning-assortment-review` — dead links on GitHub for every heading containing `&`, `/`, or similar spaced punctuation. A scan with a GitHub-accurate slugger flagged **4,618 such anchors across 554 PA files** (the whole gap-analysis block plus Expansion-block files; Core-block VS-01–VS-31 headings mostly lack `&`, so few were hit). Review #9's 1,926-anchor fix was real but incomplete: it repaired anchors that failed even the collapsing rule, while wrongly-collapsed ones kept passing Check 23 because the check shared the bug.
2. **`fix-toc-anchors.py` v2** — slugger corrected to github-slugger semantics (no run-collapsing; duplicate headings get GitHub's `-N` suffixes); docstring documents the defect class. Re-run repaired **4,618 anchors across 554 PA files, 0 skipped** (3 display-text typos resolved via the W-number fallback rule). Verified a **pure anchor swap**: every ± diff line identical modulo the `#w…` anchor, display text byte-identical.
3. **Validator Check 23 slugger corrected** to the same GitHub-accurate semantics (with duplicate-suffix handling), so the false-green class cannot recur. Still 25 checks; still 0 errors / 3 informational warnings post-fix, and an independent from-scratch checker confirms 0 unresolved intra-file anchors repo-wide.
4. Also verified clean this pass (no action needed): root-README tree counts, VS-README per-PA tables, index per-VS rows, cross-file fragment links (4/4 resolve), REQ/CTL/workflow-ID uniqueness, and no stale canonical figures (5,317 / 5,341 appear only inside versioned historical change-notes).

---

## 2026-06-26 — Consistency review #10: stale proposed/unclassified count (2,564 → 2,596); touchpoint-map Pass-30/PA-127.4 staleness; validator Check 25

An independent whole-repo review (validator green; every headline figure re-derived independently from file content — 733 requirements / 38 prefixes / 67 controls at P31-D36 / 188 VS directories / 569 PA files / 5,349 `## W` headers / W1–W5496 / 2,753 + 2,596 = 5,349 / headcount math 200×29 + 600 + 362) found the unclassified-count analogue of the drift class Check 24 Part B had guarded for headcount — plus two further same-class spots the deep-dive surfaced. Canonical totals unchanged: **188 value streams · 569 process areas · 5,349 workflows · 733 requirements · 67 controls**. `validate-repo.sh` reports **0 errors / 3 informational warnings** across all **25 checks**.

1. **Stale proposed/unclassified figure `2,564` (should be `2,596`) in 5 current-state spots.** The 2026-06-25 VS-127 PA-127.4 addition regenerated `workflow-criticality-proposed.md` (512/1,935/149 = 2,596) but left `workflow-criticality-classification.md`'s §Summary *Proposed classification* mirror at 507/1,912/145 = 2,564 — contradicting that same file's intro banner and Grand-Total coverage row (both already 2,596) — plus the mirror's own coverage-table row, the `WORKFLOW-FORMAT-GUIDE.md` Repository Layout line, and the `workflow-system-touchpoint-map.md` footer sentence. All corrected (v7.27 footer note on the classification doc); historical `X → Y` change-notes preserved.
2. **`workflow-system-touchpoint-map.md` was last fully reconciled at Pass 29 (v73.0)**: its footer still declared "Reconciled to 5,317 workflows across 187 value streams"; its §Statutory & Gap-Analysis summary section heading/table stopped at VS-191 with no VS-192 row; and the Pass 26–29 rows (VS-178–VS-191) sat header-less between the section heading and the intro note — a broken table invisible to Check 13, whose parser anchors on a header row. Fixed (v74.0): heading extended to VS-79–VS-192; VS-178–VS-191 merged into the table in VS order; VS-192 row added (Pass 30 — Fleet Management; Real Estate; Regulatory Operations; Reporting / Analytics); intro counts updated to 114 VS / 2,744 workflows incl. PA-127.4; footer reconciled to 5,349 / 188.
3. **Pre-Pass-30 enterprise totals in three workflow-body/cross-reference spots**: `VS-133 PA-133.1` and `PA-133.3` Volume rows ("~5,317 workflows across 187 value streams") and the `workflow-dependency-map.md` §7 VS-133 program row ("~5,341 workflows") → all now 5,349 / 188.
4. **Typo**: `VS-127 PA-127.4` trigger field "calamaty-readiness" → "calamity-readiness".
5. **Validator Check 25 (new)** — **(A, ERROR)** the classification doc's proposed-summary table (three tier rows, Proposed Total, coverage row) must equal `workflow-criticality-proposed.md`'s register header (itself verified against PA headers by Check 1) — the exact guard for defect 1's core spot; **(B, WARN)** stale canonical unclassified figure `2,564` scanned over current-state prose with the same SKIP-docs and `X → Y` exclusions as Check 24 Part B; **(C, ERROR)** `workflow-system-touchpoint-map.md` self-declared reconciliation must match canonical reality: the footer's "Reconciled to N workflows across M value streams" equals the index Grand Total and active-VS count, the §summary heading range ends at the index's max VS, and every VS from 79 through max has a primary-module row. Root and methodology READMEs' `24 checks` → `25 checks`. No repair script needed (the fixes were five hand-edits + one table merge).

---

## 2026-06-26 — Propagate 6,757→6,762 headcount into workflow catalog; reconcile workflows/README.md; add validator Check 24

A review found two consistency defects the validator's blind spots had let through. Both are classes of **prose/figure drift that no automated check guarded**: Check 18 covers criticality-classification prose only; Check 3 verifies the value-stream-index *grand* total only. Both fixed below, and a new check now guards both going forward. `validate-repo.sh` reports **0 errors / 3 informational warnings** across all **24** checks. Canonical totals unchanged: 188 value streams · 569 process areas · 5,349 workflows · 733 requirements · 67 controls.

**1. Headcount drift `6,757 → 6,762` not propagated to the workflow body.** The 2026-06-25 S&OP/IBP change moved total headcount **6,757 → 6,762** (and HQ **357 → 362**); the summary documents were updated but the per-workflow prose was not, leaving **96 workflow PA/README files + `workflow-dependency-map.md`** still citing `6,757` as the current workforce (**227 occurrences**; worst concentrations VS-19 Hire-to-Retire ~64, VS-27, VS-22, VS-102, VS-169, VS-83, VS-103, VS-134, VS-141). Also fixed 7 stale `357` HQ references (VS-72 PA-72.3, VS-138 PA-138.2, VS-22 PA-22.1 note, VS-169 README, VS-36 PA-36.3, VS-34 PA-34.1) and the `~357 HQ staff (≈320 concurrent users)` row in `07-methodology/technical-guidelines.md` §2.2 → `~362 HQ staff (≈325 concurrent users)` (v2.4 → v2.5). Legitimate historical `X → Y` change-notes and the labelled historical-record docs (`CHANGELOG.md`, `workflow-gap-analysis.md`, `headcount-reality-check.md`) were preserved.

**2. `workflows/README.md` family sections contradicted `value-stream-index.md` (and their own reconciliation footer).** The VS-127 row was stuck at `24` (should be `32` / 4 PAs after PA-127.4), the VS-192 row was missing from Make & Move entirely, and the two family headers `### Plan & Source (452 workflows)` / `### Make & Move (475 workflows)` were stale — so the visible body summed to 5,317 while the footer correctly read `… = 5,349`. Fixed: VS-127 row → `32`, VS-192 row added, headers → `(460 workflows)` / `(499 workflows)`. The body now sums to 5,349 and every family header matches its row-sum and the index subtotal.

**3. Validator Check 24 (new)** — `workflows/README.md` family reconciliation + stale-figure guard. **Part A (ERROR):** asserts each of the 8 family headers, its per-VS row-sum, and the `value-stream-index.md` family subtotal all agree (and the grand totals match) — the general structural guard that would have caught defect #2. **Part B (WARN):** scans current-state prose for the stale canonical figure `6,757`, skipping legitimate `X → Y` change-notes and the three historical-record docs — the guard that would have caught defect #1. New repair script **`07-methodology/fix-headcount-6757.py`** (companion to Part B); root and methodology READMEs' `22 checks` → `24 checks` (the count had already drifted to 23).

## 2026-06-26 — Fix 1,926 broken intra-file TOC anchors; add validator Check 23

Every PA file opens with a `## Workflows in This Process Area` navigation list whose entries link to the workflow headings below via GitHub heading anchors (`#slug`). A review using GitHub's exact slugger found **1,926 of these anchors malformed across 271 PA files** — every one in the gap-analysis block (VS-89+), zero in Core (VS-01–VS-31). Two malformation patterns from one generator bug: (a) the slugger dropped hyphens (`Floor-Plan` → `floorplan`; `stocking-list` → `stockinglist`); (b) a stale W-number survived a renumber (display text `W4601` but anchor `#w4409-…`). The TOC display text was always correct, so clicking the link did nothing on GitHub. No prior check saw this — Checks 19/20 verify linked *files* resolve; none resolved anchors.

1. **`fix-toc-anchors.py` (new)** — regenerates each broken anchor from its (correct) display text using GitHub's slug rules. Safe rule: for every `(#anchor)` that doesn't resolve, use `gh_slug(display)` if it matches a heading (1,923 cases), else fall back to the unique heading sharing the display's W-number (3 truncated/typo'd display-text cases). Idempotent (a resolved anchor is never rewritten). The fix is a pure in-place anchor swap — **+1,926 / −1,926 diff lines, 0 non-anchor lines changed**, display text byte-identical.
2. **Validator Check 23 (new)** — intra-file TOC anchor resolution. Computes each file's heading slugs and ERRORs on any `(#anchor)` matching no heading (an ERROR, consistent with the file-resolution checks 19/20, since a broken anchor is a broken navigational link). Verified to catch a deliberately-injected broken anchor.

`validate-repo.sh`: **0 errors / 3 informational warnings** across all **23** checks. Canonical totals unchanged: 188 value streams · 569 process areas · 5,349 workflows · 733 requirements · 67 controls.

---

## 2026-06-25 — Close the S&OP/IBP ownership gap; add VS-127 PA-127.4 (PH-retail demand–supply dynamics)

Two related changes that together close the **S&OP/IBP "unowned-as-a-program"** finding the workflow catalog had been carrying (VS-127 README; `headcount-reality-check.md` §4 "S&OP Lead").

**1. Org closure — dedicated S&OP/IBP sub-team in Supply Chain & Logistics (Option B).** `model-company-profile.md` §3.3 Supply Chain & Logistics rebalanced **35 → 40**, carving out a 5-person **S&OP/IBP sub-team** (S&OP/IBP Lead + Senior Demand Planner + 2 Demand Planners + Supply & Allocation Planner) — the single accountable owner of the VS-127 monthly demand–supply consensus cycle, reporting to the COO via the VP Supply Chain. A new §3.3 "Supply Chain & Logistics Team Structure (40 total)" subsection documents the breakdown (mirrors §13.1 Merchandising). This closes the `headcount-reality-check.md` §4 "S&OP Lead" missing-role row (marked resolved) and partially relieves the Supply Chain 🔴 understaffing (31 vs 42–50), on the same minimum-resolves-the-gap principle as the 2026-06-20 rebalance. HQ **357 → 362**, total company **6,757 → 6,762**, revenue/employee ~PHP 9.22M; §4, §11.1 (COO row 126 → 131; total 350 + 7 = 357 → 355 + 7 = 362), and the footer reconciled.

**2. New PA-127.4 — Calamity, Seasonality & Philippine-Retail Demand–Supply Dynamics (+8 workflows, W5489–W5496).** The generic monthly S&OP/IBP cycle in PA-127.1–.3 is retail/country-agnostic; this process area specializes it for BuildRight's operating context: (W5489) typhoon/calamity demand-surge forecasting & pre-positioning, (W5490) ber-months seasonal ramp, (W5491) summer aircon/garden/dry-season-construction peak, (W5492) inter-island inventory rebalancing & allocation under disruption, (W5493) B2B/trade-project demand induction, (W5494) new-store-opening demand induction & initial-stock S&OP, (W5495) VMI/consignment S&OP integration, (W5496) government-mandated price events & RA 7581 calamity price-freeze response. Each is distinct from the generic W3905–W3928 set and from sibling value streams (VS-02 operational supply, VS-69 disaster response, VS-136 multi-echelon design, VS-37 store openings). VS-127 README flipped from "unowned" to "owned by the S&OP/IBP sub-team".

**Reconciled counts** across `model-company-profile.md`, both `README.md` files, `WORKFLOW-FORMAT-GUIDE.md`, `headcount-reality-check.md`, `requirement-workflow-matrix.md`, `executive-summary.md`, `assumptions-and-design-decisions.md`, `data-migration-mapping.md`, `erp-requirements.md`, `value-stream-index.md`, `workflow-criticality-classification.md`, `workflow-dependency-map.md`, `workflow-gap-analysis.md`, and `07-methodology/technical-guidelines.md`: **188 value streams · 569 process areas · 5,349 workflows** (Plan & Source 46→47 PAs / 452→460 workflows; VS-127 3→4 PAs / 24→32 workflows); unclassified **2,588 → 2,596** (Tier 1 509→512 / Tier 2 1,930→1,935 / Tier 3 149), `workflow-criticality-proposed.md` regenerated via `07-methodology/classify-workflows.py`; total headcount **6,757 → 6,762** (7 `erp-requirements.md` employee-count figures + W10 payroll + technical-guidelines updated). W5489–W5496 are a post-Pass-30 extension (not a 31st gap pass) — the Pass-1–30 progression tables in `workflow-gap-analysis.md` §4 are left unadjusted as the historical record. `validate-repo.sh`: 0 errors.

---

## 2026-06-21 — Pass 30: One new value stream (VS-192; W5465–W5488; +24 workflows)

**VS-192 Green Fleet Transition, Electric Vehicle (EV) Fleet Operations & Sustainable Transportation** (Make & Move). A genuinely-uncovered emerging discipline: the defining terms 'fleet electrification', 'electric fleet', 'EV fleet', 'green fleet', and 'fleet decarbonization' each appeared in **zero** PA files as dedicated workflow headers, and the capability was in fact self-acknowledged as a forward-referenced need inside VS-163 PA-163.1 step 1 (*"BuildRight's own EV-fleet charging need (VS-06/VS-61 green-fleet transition)") without an owning value stream. Driven by RA 11667 (EVIDA, 2022) — the Philippine EV Industry Development Act whose IRR includes commercial/fleet adoption — and by BuildRight's stated ESG decarbonization posture (VS-25), rooftop-solar prosumer program (VS-108), and existing EV-charging host network (VS-163). The value stream owns the multi-year decarbonization of BuildRight's own goods-moving and service fleet (the ~20% owned share of the outbound-distribution fleet VS-06, plus the rental fleets VS-162/VS-186, jobsite-delivery VS-74, and employee shuttles VS-141) and the charging/alt-fuel infrastructure, route-network redesign, and EVIDA/DOE/LTO compliance the transition requires. Distinct from VS-06 (operates the current diesel fleet — this transitions it), VS-61 (diesel fuel/cost — this owns electricity/alt-fuel energy), VS-163 (hosts customer EV charging — this owns charging for BuildRight's own fleet), VS-108 (own-generation solar — this matches fleet charging load to it), and VS-25 (reports the footprint — this reduces it). (See Gap Analysis table below.)

**Reconciled counts** across `value-stream-index.md`, both `README.md` files, `WORKFLOW-FORMAT-GUIDE.md`, `headcount-reality-check.md`, `requirement-workflow-matrix.md`, `workflow-dependency-map.md`, `workflow-system-touchpoint-map.md`, and `workflow-criticality-classification.md`: **188 value streams · 568 process areas · 5,341 workflows** (Make & Move 475→499); unclassified **2,564 → 2,588**, all carrying a proposed tier (`workflow-criticality-proposed.md` regenerated via `07-methodology/classify-workflows.py`). The 24 new workflows remain unclassified pending a follow-up criticality review, exactly as prior batches.

## 2026-06-21 — Required-field completeness: validator Check 22, backfill 410 Time Estimates, fix W2796 Volume

A scan against the 9 required fields in `WORKFLOW-FORMAT-GUIDE.md` found **1,105 missing-field instances** across ~1,000 workflows — a generation artifact where whole VS batches (VS-27/37/38/39/40/53/56/58/60/63) shipped missing analysis sections, undetected because no prior check enforced required-field completeness (Check 12 covered only Automation/Controls). All structural/mechanically-derivable gaps are closed below; the content-field remainder is tracked as the honest backlog. `validate-repo.sh` now reports **0 errors / 3 informational warnings** across all **22** checks.

**Canonical totals (unchanged):** 187 value streams · 565 process areas · 5,317 workflows · 733 requirements · 67 controls · W1–W5464.

1. **Validator Check 22 (new)** — required-field completeness. Reports missing instances per field as a WARN. Detector accepts all legitimate forms: parenthetically-qualified section headers (`### Steps (...)`, `### System Touchpoints (Yard)`), phase/cadence-grouped step tables (`### Daily`/`### Weekly`), non-canonical columns, and alpha-prefixed step IDs (`CS-1`/`NR-1`) — verified that 16 initial "missing Steps" flags were all false positives on richly-structured workflows. Final reading: **645 missing** (all content fields — Participants 224, System Touchpoints 175, Pain Points 246; structural fields all 0).
2. **`backfill-time-estimate.py` (new)** — mechanically derived **410 `### Time Estimate` sections** from each workflow's own per-step Durations, explicitly labelled a draft pending human annualization. Honest-draft principle: values come from already-authored step Durations; no fabricated throughput math (receipts/year etc. is domain content). Insertion lands inside the workflow body before the `---` separator, so Check 16 (PA-footer) is unaffected. Idempotent. Time Estimate gap: 410 → **0**.
3. **Fixed 1 genuine structural defect** — `W2796` (VS-80 PA-80.3) was missing its `| **Volume** |` row (a dropped table row); restored from the Frequency field's "~600 terminals". Volume gap: 1 → **0**.
4. **Deferred (content fields, require human authoring):** Participants (224), System Touchpoints (175), Pain Points / Risks (246) — **645 instances** across ~1,000 workflows in VS-27/37/38/39/40/53/56/58/60/63. These are the format guide's workflow-specific content fields ("name the specific module/object", "named specifically, with the mitigating control"); bulk-generating them would repeat the draft-content-claimed-as-complete mistake the prior reviews corrected. Check 22 now tracks this backlog measurably.

---

## 2026-06-21 — Quality review: Automation/Controls draft fields, backfill CTL-XX, repo hygiene, validator Check 21

A whole-repo **quality** review (distinct from the prior consistency reviews, which validated cross-reference *integrity*). The Automation/Controls fields were added repo-wide by a first-pass generator whose output was overwhelmingly draft quality, yet docs/validator reported it as "100% complete" — overstating maturity. All corrected below. `validate-repo.sh` now reports **0 errors / 2 informational warnings** across all **21** checks.

**Canonical totals (unchanged):** 187 value streams · 565 process areas · 5,317 workflows · 733 requirements · 67 controls · W1–W5464.

1. **Validator Check 21 (new)** — reports Automation/Controls *content quality* (fragment-bullet count, CTL-XX coverage %, pure-boilerplate count) as a WARN, making the quality bar measurable rather than aspirational.
2. **Honest-ized "100%" → "100% presence, draft content"** in `WORKFLOW-FORMAT-GUIDE.md`, Check 12's OK message, and both READMEs.
3. **`backfill-controls.py` (new)** — reverses `internal-controls-matrix.md` into a workflow→control map; injected real CTL-XX refs into **60 Core workflows** (555→615), and normalized **3,235** Controls sections missing the blank line before the next `###` (0 remain).
4. **Hardened `add-automation-controls.py`** — fixed duplicate `'approve'` dict key; `generate_automation()` now emits complete period-terminated sentences; `generate_controls()` is CTL-map-aware.
5. **`defragment-automation.py` (new)** — one-time repair regenerating **3,319** Automation sections (9,071 fragment bullets) into complete `- System {action} of "{step}" (replaces manual Step N).` sentences. Verified zero hand-written content destroyed (all co-existing bullets were also fragments).
6. **Repo hygiene** — added `.gitignore`; un-tracked committed `__pycache__/*.pyc` + `.antigravitycli/*.json`; cleared `+x` on 14 docs.

---

## 2026-06-21 — Consistency review #9: fix 1 stale PA-file nav link (VS-56) + add validator Check 20

Fixed 1 broken PA-file navigation link in `VS-56 PA-56.1` (`../value-stream.md` → `../value-stream-index.md`); a whole-repo scan of all 7,134 links confirmed it was the only genuinely-broken navigational link. Added **Check 20** (PA-file relative-link resolution — resolves all 2,262 relative links across 565 PA files).

## 2026-06-21 — Consistency review #8: fix 12 stale PA links in the value-stream index + add validator Check 19

Fixed 12 broken PA-file links in `value-stream-index.md` for **VS-178/179/180/181** (Pass 26 — hrefs used slugs with an extra `and` conjunction). Fixed stale pending-mapping range in `requirement-workflow-matrix.md` (VS-53–VS-177 → VS-53–VS-191). Added **Check 19** (PA/VS link resolution in the index — resolves all 752 links).

## 2026-06-20 — Consistency review #7: close Pass 26–29 criticality confirmation + dependency-map §8 extension

1. **Pass 26–29 criticality confirmation** (`workflow-criticality-classification.md` v7.26): 336 workflows (VS-178–VS-191; W5129–W5464) promoted from the keyword proposal after tier review — **117 → Tier 1** (statutory/regulatory execution), **24 → Tier 3** (analytics), **195 → Tier 2**. Confirmed **2,440 → 2,776 rows (2,417 → 2,753 unique)**; unclassified **2,900 → 2,564** (51.8%). **All 103 gap-analysis VSs (VS-89–VS-191) now confirmed.**
2. Dependency-map §8.2 (Tier-1 statutory programs) extended with VS-178/179/180/187/188/189/190/191.

## 2026-06-20 — Consistency review #6: stale aggregate-count reconciliation + gap-analysis Pass 27 completeness

Reconciled stale summary-prose counts across `workflow-criticality-classification.md`, `workflow-dependency-map.md`, `workflow-system-touchpoint-map.md`, and `workflow-gap-analysis.md`. Added the missing §3 rows for **VS-182–VS-185 (Pass 27, W5225–W5320)** and a Pass 26–29 family-subtotal progression table in `workflow-gap-analysis.md` §4 (now carrying totals through Pass 29 = 5,317).

## 2026-06-20 — Consistency review #5: W641–W647 standard formatting, 100% field adoption, validator Check 18

1. Re-formatted **W641–W647** (VS-19) to standard tables/subheadings, bringing Automation/Controls field **adoption to 100%** of all workflows.
2. Added **Check 18** (criticality-classification prose counts vs headings — catches the v7.19→v7.25 regression where tier-body sentences froze while headings advanced).

## 2026-06-20 — Consistency review #4: cash-float conflict, stale adoption claim, stale counts, validator Check 17

1. Corrected a factual POS opening cash-float conflict (PHP 3,000 vs PHP 2,500) in `VS-07 PA-07.1`.
2. Removed stale "Automation/Controls adoption pending" claims (the fields were already at 100%).
3. Added **Check 17** (orphan-workflow-body / ghost detection — found and flagged the VS-12 PA-12.2 W1318 ghost).

## 2026-06-20 — Consistency review #3: stale prose counts in criticality-classification, validator Check 16

Corrected 5 stale prose counts in `workflow-criticality-classification.md` and 2 stale grand-total citations in VS-133 PA files. Added **Check 16** (PA-file footer format — every PA must end with the standardized `*Workflow Count: N · Back to...*` footer; caught 30 deviating files in VS-168–VS-177 and 50 duplicate-footers in Core).

## 2026-06-20 — Consistency review #2: PA-subtotal correction, README folder-tree completeness

Corrected `value-stream-index.md` family PA subtotals (drifted during gap-analysis additions); added the missing `07-methodology/` scripts to the root README folder tree.

## 2026-06-20 — Consistency review #1: stale Expansion-block status, validator overlap-note, dept count

Corrected stale "Expansion-block pending rework" claims (the 2026-06-20 rework had completed); removed a validator Check 12 note that contradicted Check 10; corrected HQ department count drift.

## 2026-06-20 — Restore VS-12 ghost workflow W1318

Restored the missing `## W1318. Tool Rental Reservation, Waitlist & Scheduling` header in `VS-12 PA-12.2` (the workflow body existed but its `## W` header was lost in generation, making it invisible to every count/index/classification — Check 17). Count cascade **4,980 → 4,981** across current-state citations.

## 2026-06-20 — Defect-class exhaustion audit + validator Check 15

Added **Check 15** (analysis-field header canonicalization). Found and fixed VS-161's 8 `### Automation Option` typos and VS-10's 2 `### Risks & Exceptions` synonyms to the canonical forms.

## 2026-06-20 — Cross-reference consistency review: stale Pass-19 snapshots, touchpoint-map VS-162 gap

Updated `workflow-system-touchpoint-map.md` (gap-analysis module table was 16 value streams behind); corrected stale enterprise-process-volume figures in VS-133 PA files and a stale Pass-19 snapshot.

## 2026-06-20 — Profile consistency: org-chart ownership, Merchandising role mix, headcount

Mapped all 18 HQ departments to a C-suite owner (`model-company-profile.md` §11.1); fixed Merchandising team breakdown to sum to 40 (§13.1).

## 2026-06-20 — HQ headcount rebalance (minimum workflow-coverage): HQ 315 → 357; total 6,715 → 6,757

Cross-referenced stated HQ department headcounts against the actual roles implied by workflow coverage; rebalanced to the minimum defensible HQ staffing. See [`headcount-reality-check.md`](01-model-company/headcount-reality-check.md).

## 2026-06-20 — Whole-repo consistency review: stale counts (3,595/172/675), missing VS-170–VS-177 links

Corrected stale unclassified-workflow count **3,595 → 3,835** and stale value-stream count **172 → 173**; added missing VS-170–VS-177 links across the cross-reference layer.

## 2026-06-20 — Criticality hand-confirmation batch 3: 8 operational-support VSs (192 workflows)

**VS-40/43/55/63/64/65/83/84.** 21 → Tier 1 (PFRS capex capitalization, DOLE occupational-health/labor-relations mandatory steps); 30 → Tier 3 (analytics); 141 → Tier 2. Confirmed 1,552 → 1,744 rows.

## 2026-06-20 — Criticality hand-confirmation batch 2: 8 support & governance VSs (192 workflows)

**VS-100/104/112/113/126/129/133/139.** 14 → Tier 1 (statutory execution the keyword rules missed); 29 → Tier 3 (analytics/optimization); 149 → Tier 2. Confirmed 1,360 → 1,552 rows.

## 2026-06-20 — Criticality hand-confirmation batch 1: 8 wholly-statutory VSs (192 workflows)

**VS-79/85/89/91/114/117/118/125.** 154 → Tier 1 (statutory execution); 32 → Tier 2 (program support); 6 → Tier 3 (analytics). Confirmed 1,168 → 1,360 rows. Prompted by "can the 2 validator warnings be fixed mechanically?" — they cannot (the unclassified majority need genuine tier review).

## 2026-06-20 — Pass 29: Two new value streams (VS-190–VS-191; W5417–W5464; +48 workflows)

VS-190 Operational Technology (OT)/ICS Cybersecurity; VS-191 Customer Construction Debris & Site Cleanup. (See Gap Analysis table below.)

## 2026-06-20 — Pass 28: Four new value streams (VS-186–VS-189; W5321–W5416; +96 workflows)

VS-186 Compact/Heavy Equipment Rental; VS-187 Household Hazardous Waste Take-Back; VS-188 Trade Reseller Floor-Plan Financing; VS-189 Trade Receivables Factoring. (See Gap Analysis table below.)

---

## Workflow Gap Analysis (2026-06-14 → 2026-06-21)

Thirty passes identified genuinely-unowned operational capabilities (defining terms appearing in **zero** PA files) and authored full value-stream directories, PA files, and cross-reference updates for each. **Totals: 104 value streams (VS-89–VS-192) · 2,496 workflows (W2993–W5488)** added, growing the active inventory from 84 to 188 value streams. The retired placeholder VS-49–VS-52 (see 2026-06-14 entry below) left gaps partly filled by these passes. Per-pass candidate/ID-allocation detail lives in [`workflow-gap-analysis.md`](01-model-company/workflows/workflow-gap-analysis.md) §3–§4.

| Pass | Date | Value Streams | Workflows | W-range |
|---|---|---|---|---|
| 1 | 2026-06-14 | VS-89–VS-92 | 96 | W2993–W3088 |
| 2 | 2026-06-14 | VS-93–VS-96 | 96 | W3089–W3184 |
| 3 | 2026-06-14 | VS-97–VS-100 | 96 | W3185–W3280 |
| 4 | 2026-06-14 | VS-101–VS-104 | 96 | W3281–W3376 |
| 5 | 2026-06-14 | VS-105–VS-108 | 96 | W3377–W3472 |
| 6 | 2026-06-14 | VS-109–VS-112 | 96 | W3473–W3568 |
| 7 | 2026-06-14 | VS-113–VS-116 | 96 | W3569–W3664 |
| 8 | 2026-06-14 | VS-117–VS-120 | 96 | W3665–W3760 |
| 9 | 2026-06-14 | VS-121–VS-124 | 96 | W3761–W3856 |
| 10 | 2026-06-15 | VS-125–VS-128 | 96 | W3857–W3952 |
| 11 | 2026-06-15 | VS-129–VS-132 | 96 | W3953–W4048 |
| 12 | 2026-06-15 | VS-133–VS-136 | 96 | W4049–W4144 |
| 13 | 2026-06-16 | VS-137–VS-140 | 96 | W4145–W4240 |
| 14 | 2026-06-16 | VS-141–VS-142 | 48 | W4241–W4288 |
| 15 | 2026-06-17 | VS-143–VS-146 | 96 | W4289–W4384 |
| 16 | 2026-06-17 | VS-147–VS-150 | 96 | W4385–W4480 |
| 17 | 2026-06-17 | VS-151–VS-156 | 144 | W4481–W4624 |
| 18 | 2026-06-18 | VS-157–VS-161 | 120 | W4625–W4744 |
| 19 | 2026-06-19 | VS-162–VS-164 | 72 | W4745–W4816 |
| 20 | 2026-06-19 | VS-165–VS-167 | 72 | W4817–W4888 |
| 21 | 2026-06-19 | VS-168–VS-169 | 48 | W4889–W4936 |
| 22 | 2026-06-19 | VS-170–VS-172 | 72 | W4937–W5008 |
| 23 | 2026-06-20 | VS-173 | 24 | W5009–W5032 |
| 24 | 2026-06-20 | VS-174–VS-176 | 72 | W5033–W5104 |
| 25 | 2026-06-20 | VS-177 | 24 | W5105–W5128 |
| 26 | 2026-06-20 | VS-178–VS-181 | 96 | W5129–W5224 |
| 27 | 2026-06-20 | VS-182–VS-185 | 96 | W5225–W5320 |
| 28 | 2026-06-20 | VS-186–VS-189 | 96 | W5321–W5416 |
| 29 | 2026-06-20 | VS-190–VS-191 | 48 | W5417–W5464 |
| 30 | 2026-06-21 | VS-192 | 24 | W5465–W5488 |
| **Total** | | **VS-89–VS-192** | **2,496** | **W2993–W5488** |

---

## 2026-06-19 — Whole-repo consistency reviews (5 passes)

A series of top-to-bottom reads of every summary/cross-reference document and high-traffic PA files. Findings and fixes:

- **Broken anchor links** (factual defects) and **Goods Receipts scope ambiguity** (`model-company-profile.md` §15.1).
- **BIR record retention canonicalized to 10 years** (TRAIN/NIRC) across all documents (was inconsistent 7 vs 10 years).
- **Volume-unit consistency** — monthly figures mislabeled as daily; corrected.
- **Operational bank list reconciled to 4** (BDO, BPI, Metrobank, China Bank) and minor figure drift fixed.
- **Documentation hygiene** — number-format drift, TOC count drift, stale POS/documented-workflow counts.

## 2026-06-19 — Cross-document figure consistency review (bank list, headcount, POS figures)

Reconciled stale figures (bank-account count, headcount totals, POS transaction volumes) across overview and high-traffic workflow documents.

## 2026-06-18 — Data-volumes AP figure reconciliation & cross-reference housekeeping

Resolved the outstanding AP-figures cross-reference ambiguity; corrected stale figures and broken references accumulated behind the gap-analysis block. Content pass on payroll dates, bank list, stale ranges, and the W40 category.

## 2026-06-18 — Gap-analysis structural consistency: restore missing Pass 12 table

Restored the missing Pass 12 table in `workflow-gap-analysis.md` §3; fixed family counts and two small cross-reference issues.

## 2026-06-17 — Consistency reviews (3 passes)

- Corrected **unclassified-workflow count 2,972 → 2,995** (reported inconsistently in five places) and collapsed the related prose.
- Corrected stale **requirement total 730 → 733** in `erp-requirements.md` v21.0 footer.
- Reconciled Pass 13/14 (VS-137–VS-142) across cross-reference docs.

## 2026-06-15 — Workflow review implementation (5-commit program)

1. **(1/5) Structural-integrity fixes** — bounded set of PA-file format/structural fixes + validator hardening.
2. **(2/5) Keyword-driven classification pass** — addressed 2,659 workflows (70%) with no criticality tier; generated `workflow-criticality-proposed.md` via `classify-workflows.py`.

## 2026-06-15 — Workflow documentation review: format guide, index, validator

Reviewed value-stream/workflow documentation; updated `WORKFLOW-FORMAT-GUIDE.md`, the value-stream index, and the validator.

## 2026-06-14 — Consistency review: decision tree, matrix counts & validator accuracy

Full-repository review (then 84 VS / 256 PA / 2,844 workflows) reconciling every cross-document count.

## 2026-06-14 — Repo review: retire VS-49/50/51/52 placeholder content, harden validator

Identified 4 value streams (VS-49–VS-52) whose workflow files contained only auto-generated placeholder content; retired them (96 placeholder workflows removed; numbers remain unused). The resulting capability gaps were filled across the gap-analysis passes above.

## 2026-06-14 — Repo review: fix dangling W5G reference & harden validator

Full-repository review; investigated flagged items, narrowed to real defects, fixed the dangling W5G reference and hardened the validator.

## 2026-06-14 — Add 10 new value streams (240 workflows, W2753–W2992)

Identified 10 business capabilities not yet organized as value streams; authored each with 3 process areas / 24 workflows.

## 2026-06-14 — Consistency review: requirement-ID dedup & criticality summary fix

Removed 19 mislabeled duplicate requirement-ID rows from `requirement-workflow-matrix.md`; fixed the criticality summary.

## 2026-06-13 — Consistency reviews (3 passes)

- **Eliminated all 15 duplicate workflow IDs** (IDs must be unique per `WORKFLOW-FORMAT-GUIDE.md`).
- **Standardized all 238 PA file footers** to the `*Workflow Count: N · Back to...*` convention.
- **Reconciled all cross-document counts**; deduplicated CHANGELOG (removed 13 identical copies of one entry).

## 2026-06-12 — Add 4 new value streams with 96 workflows (W1830–W1925)

VS-41 Private Label; VS-42 Property & Lease Admin; VS-43 Trade Professional Program; VS-44 Consumer Insights.

## 2026-06-12 — Add 40 new workflows across 39 process areas (W1485–W1552)

Two batches (W1485–W1504, W1533–W1552) of model-company-relevant workflows across store, DC, supply, and finance process areas.

## 2026-06-11 — Consistency review: reconcile all workflow counts

Reconciled workflow counts across all 30 VS READMEs, `value-stream-index.md`, and the root README.

## 2026-06-10 — Add 65 new workflows (W1298–W1414)

Four batches of model-company-relevant workflows: fleet/vehicle management (W1348–W1414), customer PDC/trade-account processing (W1380–W1399), consignment/intercompany (W1298–W1317), tool rental (W1318–W1327).

## 2026-06-09 — Add workflows & post-review cleanup

- Added **WHL-001/002/003** to `erp-requirements.md` (DC/warehouse management requirements referenced in workflows).
- Added 77 new workflows across multiple batches (W1167–W1277) including reverse logistics, DSD receiving, e-wallet settlement, and post-disaster demand fulfillment.
- Fixed VS-16 workflow count (17 → 23) and related cross-reference issues.
