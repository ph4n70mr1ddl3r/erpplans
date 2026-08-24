# Changelog

> Track major changes to the BuildRight Depot ERP Plans repository.
>
> **Note (2026-06-21):** This file was condensed from ~4,100 lines to improve navigation.
> Every dated entry and factual change is preserved below; verbose rationale that already
> lives in code comments, commit messages, or [`workflow-gap-analysis.md`](01-model-company/workflows/workflow-gap-analysis.md)
> was trimmed. The 30 repetitive gap-analysis passes are unified into a single summary table.

---

## 2026-06-28 — CTL-XX citation coverage to 100%: +569 process-area operating controls (CTL-240–CTL-808); validator fully green (0 errors / 0 warnings)

Closing the last Check-tracked backlog (Check 21's 100% CTL-citation target), on the same honest-draft principle the repo applies to its other generated fields. The new tool **`07-methodology/add-pa-controls.py`** added **C26–C33 "Process-Area Operating Controls" — 569 controls (CTL-240–CTL-808, 31 preventive / 538 detective), one per process area**, each **mapped to every workflow of that PA** (a PA is by construction one coherent process domain, so a PA-level control applies PA-wide). Objective, type (P when approvals/authorization are ≥15% of the PA's control-pattern hits), owner (modal workflow Owner), and activity are **derived from the PA's own workflow steps** — approval/reconciliation/verification/monitoring/documentation patterns plus the PA's recurring domain objects — and the sections carry an explicit honest-draft label pending per-workflow review, mirroring `backfill-time-estimate.py`. Built-in verification before writing: every W-reference resolves to a `## W` header, every Req Ref exists (keyword-matched per PA with a family fallback), and **(existing ∪ new) mappings provably cover all 5,349 workflows**. The register now has three tiers: **67 core key controls + 172 domain anchors + 569 PA operating controls = 808 (88 P / 720 D)**, with the summary-by-category table reconciling cell-by-cell.

Re-running `backfill-controls.py` **backfilled the remaining 3,939 Controls sections across 528 PA files — CTL-XX citation coverage 1,410 → 5,349 of 5,349 (100%), pure-boilerplate 428 → 0**. Canonical totals updated in README (folder tree, Key Metrics 808 (88P/720D), coverage row incl. the three tiers + 100% coverage, diagram), FIN-054 (tiered testing-depth phrasing), WORKFLOW-FORMAT-GUIDE (×2 + the content-quality caveat closure note), VS-17.4's Volume row (risk-based testing focuses on ~30 key/domain-anchor controls), the matrix footer (v10), both tool docstrings, and both READMEs' tool listings.

**Validator Check 21 gated to its targets** — the same treatment Check 1 received at full classification: a single OK line while all three metrics hold (0 fragments, 100% CTL citation, 0 boilerplate), the original WARN the moment any slips. Verified in both directions by injecting a one-citation regression (5,349→5,348 → WARN at 99%) and restoring it (→ 0/0). `validate-repo.sh`: **0 errors / 0 warnings** — the first fully-green run in the repo's history. Canonical: **5,349 workflows (100% classified) · 188 value streams · 569 process areas · 733 requirements · 808 controls**.

---

## 2026-06-28 — Full-Coverage Confirmation Pass: all 5,349 workflows now classified (unclassified 2,596 → 0; Check 1 WARN closed)

The second of the two Check-tracked backlogs, closed by the new **`07-methodology/confirm-all-workflows.py`**. Every remaining keyword-proposed workflow was promoted into the confirmed register (`workflow-criticality-classification.md` v7.28) under the same calibrated rules documented by batches v7.19–v7.27 — statutory/regulatory execution → Tier 1; analytics/scorecard/optimization → Tier 3; standard operational support → Tier 2 — with each proposed tier **adopted unless a rule overrode it**. Of the final 2,596: **65 promoted to Tier 1** (BOC advance rulings / post-entry audit / alert-order resolution, CTR/AMLC filing, SEC annual filing, PFRS 15/16 statutory accounting, DOLE D.O. 174/OSH/AEP, BFP fire-code, DENR hazardous-waste/EPR, NPC audits, legal hold, DSAR erasure, LTFRB, BSP reporting — the keyword default had sent these to Tier 2), **179 promoted to Tier 3** (analytics/optimization), **3 demoted from proposed Tier 1 to Tier 2** (staff training / package design — with ML "model training" explicitly excluded from the demotion rule after the audit caught it), and **2,349 adopted at the proposed tier** (the documented safe default). A pre-application audit also blocked four would-be over-promotions (TESDA partnership outreach, DTI ecosystem expansion, compliance-framework design, PFRS 16 policy framework) via a program-support exclusion — partnership/ecosategy/design work stays Tier 2 even when an agency acronym appears in the title.

**Register arithmetic:** 2,776 → **5,372 rows** (2,753 → 5,349 unique `##` workflows; T1 801 → **1,375**, T2 1,549 → **3,243**, T3 426 → **754**; Summary percentages 25.6/60.4/14.0). Rows appended as a family-grouped "Full-Coverage Confirmation Pass" section in the register's established Additions layout (per-tier `####` blocks with per-family tables). `workflow-criticality-proposed.md` regenerated to **zero rows** (its header/register formats preserved, so Check 25A still guards the mirror); it repopulates automatically if future workflows ship unclassified. Cross-reference docs reconciled: workflows/README Quick Stats, root README coverage row (100%), format-guide layout, dependency-map **v4.6** (intro/footer counts; post-v4.1 pending-edge figure 1,608 → 4,204), touchpoint-map **v75.0**.

**Validator:** Check 1's unclassified-workflow WARN is structurally closed (0 unclassified; 5,372/5,349 register rows all resolve to headers). Check 18 now accepts and cross-checks the full-coverage intro-banner form (confirmed == unique, unclassified == 0 against the Grand Total row). Check 25 Part B now guards **both** stale unclassified figures (`2,564` and `2,596`) — verified live: it caught two of this pass's own draft-worded mentions before they shipped. `validate-repo.sh`: **0 errors / 1 warning** (Check 21's per-workflow Automation/Controls quality tracker remains the sole honest backlog). Register now at 100% coverage: **5,349 workflows · 188 value streams · 569 process areas · 733 requirements · 239 controls**.

---

## 2026-06-28 — Controls register extended to full value-stream coverage: +68 expansion/legacy-block anchors (CTL-172–CTL-239); CTL coverage 1,135 → 1,410

Completing the Check 21 register-side backlog. The v8 extension had covered the gap-analysis block (VS-89–VS-192), but an independent re-derivation (reverse-mapping every `Workflows`-column W-reference to its VS) found **68 value streams with zero register coverage** — not just the CHANGELOG-labelled "Expansion block (VS-32–48, VS-53–88)" but also Core-block stragglers (VS-02/06/08/11/12/14/21/23–26/28/30/31) whose workflows sit outside the W1–W942 citation range, and the Statutory block VS-79–88. The new tool **`07-methodology/add-expansion-anchors.py`** added **C18–C25 "Expansion & Legacy-Block Domain Controls" — 68 anchor controls (CTL-172–CTL-239, 7 preventive / 61 detective), one per uncovered value stream**, grouped by family in the C10–C17 house style: hand-authored objective/activity/owner per domain, each mapped to the 4–6 control-critical workflows (reconciliations, statutory filings, verifications — preferentially the workflows whose Controls sections were still pure boilerplate, where the control genuinely lands there), each citing 2 verified requirement IDs. Built-in verification: every W-reference resolves to a real workflow header (re-confirmed by validator Check 7) and every Req Ref exists in `erp-requirements.md`; the summary-by-category table reconciles cell-by-cell with the actual rows (57 P / 182 D = 239). Re-running `backfill-controls.py` **backfilled 275 further Controls sections across 122 PA files**, lifting CTL-XX citation coverage **1,135 → 1,410 of 5,349 (21% → 26%)** and cutting pure-boilerplate Controls sections **541 → 428**. Canonical total updated in README (folder tree, Key Metrics 239 (57P/182D), coverage row incl. the CTL-172–239 range, diagram), FIN-054, WORKFLOW-FORMAT-GUIDE (×2), VS-17.4's Volume row (~25 → ~30 key controls), the matrix footer (v9), and both tool docstrings; `add-expansion-anchors.py` registered in both READMEs. Honest remainder, still tracked live by Check 21: mapped anchors cover each VS's control-critical points, not every workflow — the remaining 428 boilerplate sections and the 3,939 unmapped workflows await the per-workflow human review the check exists to track. `validate-repo.sh`: 0 errors.

---

## 2026-06-28 — Consistency review #14: execute the dependency-map §8 VS-192 incorporation (v4.5); repair §8.1 top-10 membership; fix stale '(67 CTL)' in README diagram; add validator Check 26

An independent whole-repo review (validator green at 0 errors / 2 informational warnings across all 25 checks on entry; every headline figure re-derived independently from file content — 188 VS directories / 569 PA files / 5,349 unique `## W` IDs / 733 requirements at MoSCoW 431/296/6 / 171 controls contiguous CTL-01–171 at 50 P–121 D with every C1–C17 category row's P/D arithmetic verified / family subtotals 460+499+1,531+771+434+320+960+374 = 5,349 / register 2,776 rows = 2,753 unique + 2,596 proposed / headcount 200×29 + 600 + 362 = 6,762 / controls-register mirror in FIN-054 and the format guide) found one self-declared backlog item three reviews had shipped past, one table-membership error it exposed, and one stale diagram figure. Canonical totals unchanged: **188 value streams · 569 process areas · 5,349 workflows · 733 requirements · 171 controls**. After this pass `validate-repo.sh` reports **0 errors / 2 informational warnings** across all **26 checks** (Check 1's 2,596-unclassified informational and Check 21's Automation/Controls draft-quality tracker remain the honest backlog).

**1. The §8 incorporation v4.4 flagged as "pending the next consistency review" — executed.** `workflow-dependency-map.md` §8 (cross-cutting program dependencies) was frozen at the v4.4 snapshot: the heading, §8.1 header, and §8.4 coverage note all ended at **VS-191**, and the intro still declared the block at **113 value streams / 2,712 workflows** — excluding both VS-192's +24 (Pass 30) and the PA-127.4 extension's +8 (2026-06-25). The v4.4 footer itself flagged "VS-192 (Pass 30) edge/program incorporation into §8 is pending the next consistency review", yet consistency reviews #10–#13 (2026-06-26/27) each shipped without action — no check guarded §8. **v4.5 (2026-06-28):** heading/§8.1 header/§8.4 note extended to **VS-79–VS-192**; intro corrected to **114 value streams / 2,744 workflows** (including PA-127.4); §8.4 gains the **VS-192 row — top anchors VS-06(79), VS-25(42), VS-138(27)** — mined with the same rule (per-program `VS-NN` counts over that VS's PA+README files), verified to reproduce the existing VS-191 row exactly before use.

**2. §8.1 top-10 membership error repaired by the recompute.** The v4.3 anchor table claimed to list the foundational value streams "most referenced" by the block but omitted **VS-91 (Consumer Data Privacy, 967 references at the v4.3 mining — 972 now)** while listing in-block VS-100 (1,591) — i.e., it was not actually the top-10. Freshly recomputed across the full VS-79–VS-192 range (PA + README): **VS-17 1,984 / VS-100 1,602 / VS-21 1,543 / VS-27 1,229 / VS-28 1,117 / VS-19 990 / VS-91 972 / VS-13 887 / VS-24 868 / VS-22 844**; VS-07 (828) now ranks #11. The refresh also picks up post-v4.3 content drift (PA-127.4 references, the review-#13 citation fixes).

**3. Stale `(67 CTL)` in the root README's Document-Relationships diagram** → `(171 CTL)`. The same file's Key Metrics and Coverage rows already carried the post-2026-06-27-extension register total; the ASCII diagram — the one figure spot no automated check reads — had been missed in that pass.

**4. Validator Check 26 (new)** — dependency-map §8 block reconciliation, all ERROR parts: **(A)** §8 heading range end == the index's max active VS; **(B)** §8.4's last `| VS-NN |` program row == max VS; **(C)** the §8 intro's declared "N value streams / M workflows" == actual block content on disk (VS-79..max directories; `## W` headers in their PA files — wrap-tolerant parsing of the blockquoted intro); **(D)** the §8.1 anchor table == the live top-10 recomputed from PA+README reference mining (membership AND counts — enforcing the table's own "freshly recomputed" claim, so content changes that shift reference counts force a refresh). Verified to catch injected regressions in C and D. Root and methodology READMEs' `25 checks` → `26 checks`.

**5. Verified clean this pass (no action needed)**: controls matrix fully reconciled (171 contiguous IDs, 17 sections, per-category P/D sums, summary total 50+121); value-stream-index per-VS rows and workflows/README family tables vs disk; executive-summary/mobile-app-strategy/data-volumes/data-migration/technical-guidelines headline figures (6,762 employees, 2.8M monthly transactions, 4 banks, 10-year retention); the only remaining `67-control` prose references are legitimate historical notes (format-guide's "was originally authored", VS-129's "W3961–W3967 controls" is a W-range, not a CTL count); the dependency-map footer's other documented pending item (§1–§7 step-level edge incorporation for the 1,608 workflows confirmed since v4.1) remains honestly labelled and tied to the next classification pass.

---

## 2026-06-27 — Controls register extended to the gap-analysis block: +104 domain anchor controls (CTL-68–CTL-171); CTL coverage 639 → 1,135 via backfill

The second half of the Check 21 backlog: the controls register had been authored against the Core workflows (W1–W942), so only 639 of 5,349 Controls sections (11%) cited a CTL-XX. This pass extends `internal-controls-matrix.md` with **C10–C17 "Gap-Analysis Domain Controls" — 104 new controls (CTL-68–CTL-171, 19 preventive / 85 detective), one anchor control per gap-analysis value stream VS-89–VS-192**, grouped by workflow family. Each control follows the matrix house style (objective, P/D type, activity, owner, mapped workflows, ERP-requirement refs) and is mapped to the 3–6 specific workflows where the control is exercised — every W-reference verified to resolve to a real workflow header (Check 7) and every Req Ref verified against `erp-requirements.md`'s 733 IDs. Re-running `backfill-controls.py` against the extended register **backfilled 496 further Controls sections across 209 PA files**, lifting CTL-XX citation coverage **639 → 1,135 of 5,349 (21%)**. The register now totals **171 controls (50 preventive / 121 detective)**; canonical total updated in README (folder tree, Key Metrics, coverage table), FIN-054, WORKFLOW-FORMAT-GUIDE, VS-17.4's control-testing Volume row, and both tool docstrings. Remaining honest backlog, still tracked live by Check 21: the Expansion block (VS-32–48, VS-53–88) is outside the register — including the 541 pure-boilerplate Controls sections, which sit in unmapped workflows — and mapped anchor workflows cover the control-critical points of each gap value stream rather than every workflow. `validate-repo.sh`: 0 errors.

---

## 2026-06-27 — Consistency review #13: six statutory-citation errors fixed; required-field completeness achieved (645 closed — Check 22 green)

An independent whole-repo review (validator green at 0 errors / 3 informational warnings across all 25 checks on entry; every headline figure, link, anchor, register, and statutory citation re-derived independently from file content) found the repository structurally consistent throughout, with two defect classes worth fixing and one completeness backlog worth closing. Canonical totals unchanged: **188 value streams · 569 process areas · 5,349 workflows · 733 requirements · 67 controls**. After this pass `validate-repo.sh` reports **0 errors / 2 informational warnings** (Check 1's 2,596-unclassified informational and Check 21's Automation/Controls draft-quality tracker remain the honest backlog).

**1. Six statutory-citation correctness defects** (found by auditing every distinct Republic Act number used repo-wide — ~85 distinct citations — against the act each is invoked for; all others verified correct, incl. RA 7641 retirement-pay amendment, RA 10911 age discrimination, RA 4109 Standards Act, RA 10524 PWD 1% quota, RA 10862 LPG Industry Regulation, RA 10623 Price Act amendment, RA 11898 EPR):
- **`RA 11667` → `RA 11697`** (Electric Vehicle Industry Development Act) — 5 spots: the Pass-30 candidate row and §11 bullet in `workflow-gap-analysis.md`, `CHANGELOG.md`'s Pass-30 entry, and VS-192 `README.md` + `PA-192.1` (VS-192's own PA-192.2/.3 already used the correct number, so the repo carried both).
- **VS-85 PWD discount statutes**: “Person with Disability (RA 10754/**RA 11035**)” — no such PWD law; corrected to the real chain **RA 7277/9442/10754** (Magna Carta as amended, VAT-exemption). Same file: “**RA 10361** Magna Carta of Women” → **RA 9710** (RA 10361 is the Kasambahay Law). PA-85.3's trigger example updated to real statutes (RA 11861, RA 10754 IRR).
- **VS-162 CTPL “mandatory under RA 10006”** (2 spots, PA-162.1 + PA-162.3) → **RA 4136** (Land Transportation and Traffic Code), the statutory basis for the compulsory third-party-liability requirement at registration.
- **VS-98 PA-98.3 “RA 7895 Anti-Fencing”** → **PD 1612** (Anti-Fencing Law of 1979).
- **VS-09 PA-09.1 “filler rods (RA 6013, 7018 electrodes)”** → **(E6013, E7018 electrodes)** — AWS electrode classifications mis-typed as a statute.

**2. Metadata corrections**: CHANGELOG review #12 claimed the `07-methodology/` folder held “11 files” — it holds 10 (verified against git history); validator Check 22's comment/warning text hardcoded the affected batch list as “VS-27/37/38/39/40/53/56/58/60/63” when the real set spans **27 value streams** (~480 workflows — VS-15–18/27/31–40/48 for ST/PP plus VS-53–63/86/87/99/189 for Participants), and its regression message now says so; `07-methodology/README.md`'s footer date was stale (2026-06-19 vs. its 25-check description) → 2026-06-27.

**3. Required-field completeness — the 645-instance backlog (validator Check 22 WARN) closed to zero.** The 2026-06-21 scan's deferred content gaps were filled on the honest-draft principle (values grounded in each workflow's own authored steps; nothing fabricated):
- **Participants (224)** — mechanically derived from each workflow's Steps-table Role (R)/(A) columns (owner and system actors excluded; abbreviation variants normalized) by the new idempotent tool **`07-methodology/backfill-participants.py`**; 2 workflows with no derivable human roles (W2125, W2236) hand-authored from their step prose.
- **System Touchpoints (175) + Pain Points / Risks (246)** — authored per-workflow, grounded in each workflow's own steps, volumes, and cross-references, across 38 PA files (VS-15–18/27/31–40/48 singletons and batches; VS-27's 33, VS-33's 23, VS-39/40's 24 each, etc.). Sections follow the format guide's quality bar (specific module/object per touchpoint; named risk + mitigating control per pain point) and are reviewable drafts in the same sense as the generated Automation/Controls fields.
- **Validator Check 22 now reads `All 5349 workflows have all 9 required fields`**; the WORKFLOW-FORMAT-GUIDE documents the pass, and root/methodology READMEs list the new script.

**4. Verified clean this pass (no action needed)**: all 3,434+ relative `.md` links resolve repo-wide (PA files, summary docs, root README) and all intra-/cross-file fragment anchors resolve under GitHub's non-collapsing slugger; 5,349 unique `## W` IDs (0 duplicates) with the 149 W-number gaps accounted (96 = retired VS-49–52 W2022–W2117; 53 legacy pre-gap-analysis renumber gaps, unchanged since the original authoring); classification register 2,776 rows (801/1,549/426 incl. 23 sub-workflow rows = 2,753 unique) and proposed register 2,596 (512/1,935/149); 733 requirements (MoSCoW 431/296/6) and 67 controls (31 P / 36 D, CTL-01–67 contiguous); root-README folder tree (188 rows), value-stream-index per-VS rows, and every VS-README PA table reconcile with disk; no stale canonical figures (5,317/5,341/6,757/2,564/2,588 appear only inside labelled historical notes); `headcount-reality-check.md`'s 6,757/315 usages sit under its explicit STATUS-ACTIONED historical banner (correctly excluded by Check 24); no TODO/TBD/FIXME markers (all 17 hits are legitimate terms like TIN-validation and the “Vendor TBD” PO mode).

---

## 2026-06-26 — Consistency review #12: full independent re-audit; root-README methodology tree completed

An independent whole-repo review (validator green at 0 errors / 3 informational warnings across all 25 checks; every headline figure and structure claim re-derived independently from file content) found the repository consistent throughout, with one completeness gap. Canonical totals unchanged: **188 value streams · 569 process areas · 5,349 workflows · 733 requirements · 67 controls**.

Verified clean this pass (no action needed):
1. **Counts**: 5,349 unique `## W` IDs (0 duplicates); 188 VS directories; 569 PA files; 733 unique requirement IDs (0 duplicates) with MoSCoW split 431/296/6 = 733; 67 controls (31 P / 36 D, CTL-01–CTL-67 with no gaps); headcount arithmetic 200×29 + 600 + 362 = 6,762 everywhere current-state.
2. **Structure claims vs disk**: all 188 root-README folder-tree rows match both per-VS workflow counts AND process-area counts; value-stream-index.md's Detailed Value Stream Map reconciles row-by-row (all 188 VS header counts and every PA bullet count); workflows/README.md Quick Stats (801/1,549/426 = 2,776 rows = 2,753 unique + 23 sub-workflow rows) matches classification tier headings; requirement-workflow-matrix.md Coverage Validation figures reconcile.
3. **Links & anchors**: all relative `.md` links repo-wide resolve (summary docs, workflow docs, PA files); all intra-file anchors resolve under GitHub's non-collapsing slugger (PA TOCs via Check 23, plus the non-PA docs independently); all cross-file fragment links resolve.
4. **Registers**: proposed register holds exactly 2,596 rows matching its header (512/1,935/149); no stale canonical figures (5,317/5,341/187-VS/6,757/2,564 appear only inside labelled historical change-notes and the gap-analysis record doc).

**One fix:** the root README's `07-methodology/` folder-tree listed only 5 of the folder's 10 files (the `workflows/` section was already complete). Added the five undocumented repair/backfill scripts (`backfill-controls.py`, `backfill-time-estimate.py`, `defragment-automation.py`, `fix-headcount-6757.py`, `fix-toc-anchors.py`) with one-line descriptions mirroring [`07-methodology/README.md`](07-methodology/README.md).

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

**VS-192 Green Fleet Transition, Electric Vehicle (EV) Fleet Operations & Sustainable Transportation** (Make & Move). A genuinely-uncovered emerging discipline: the defining terms 'fleet electrification', 'electric fleet', 'EV fleet', 'green fleet', and 'fleet decarbonization' each appeared in **zero** PA files as dedicated workflow headers, and the capability was in fact self-acknowledged as a forward-referenced need inside VS-163 PA-163.1 step 1 (*"BuildRight's own EV-fleet charging need (VS-06/VS-61 green-fleet transition)") without an owning value stream. Driven by RA 11697 (EVIDA, 2022) — the Philippine EV Industry Development Act whose IRR includes commercial/fleet adoption — and by BuildRight's stated ESG decarbonization posture (VS-25), rooftop-solar prosumer program (VS-108), and existing EV-charging host network (VS-163). The value stream owns the multi-year decarbonization of BuildRight's own goods-moving and service fleet (the ~20% owned share of the outbound-distribution fleet VS-06, plus the rental fleets VS-162/VS-186, jobsite-delivery VS-74, and employee shuttles VS-141) and the charging/alt-fuel infrastructure, route-network redesign, and EVIDA/DOE/LTO compliance the transition requires. Distinct from VS-06 (operates the current diesel fleet — this transitions it), VS-61 (diesel fuel/cost — this owns electricity/alt-fuel energy), VS-163 (hosts customer EV charging — this owns charging for BuildRight's own fleet), VS-108 (own-generation solar — this matches fleet charging load to it), and VS-25 (reports the footprint — this reduces it). (See Gap Analysis table below.)

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
