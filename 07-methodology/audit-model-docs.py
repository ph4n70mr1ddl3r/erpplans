#!/usr/bin/env python3
"""
audit-model-docs.py — root-level model-company document integrity guard.

Consistency review #41 (2026-08-29) audited the three root-level model-company
documents never before swept — mobile-app-strategy.md, data-migration-mapping.md,
assumptions-and-design-decisions.md — for figure agreement with the canonical
registers and internal cross-reference integrity. Findings: fully clean —

  * figures: 6,762 employees, ~800–1,000 vendors (§6.5), 35,000 active + 20,000
    inactive items, ~600,000 loyalty members, 29 per store, 200 stores + 4 DCs,
    14,000 POS/store/month (2.8M ÷ 200), ~PHP 9.22M revenue/employee, and the
    5,200+200 trade/corporate price records all match the registers;
  * cross-references: every W/VS-/CTL-/PA-/requirement-ID token resolves
    (5,363 W, 190 VS, 569 PA, 808 CTL, 728 requirement registers); the §-refs
    resolve doc-scoped — unqualified to the profile's 61 sections, named-doc
    refs like 'Technical Guidelines §2.1' to 07-methodology/technical-
    guidelines.md, and bare §N.N inside data-migration-mapping.md to its own
    section headers; no retired stale totals (6,757/6,715/5,3xx) appear.

Guard mode (--guard, validator Check 59) re-runs the whole audit on every
invocation: token resolution against the live registers, doc-scoped §-ref
resolution, and the retired-figure literal list. Any hit exits 1.

Consistency review #68 (2026-09-02) extended the guard to the two
organizational documents issued 2026-09-01/02 — optimal-table-of-organization.md
and 07-methodology/it-product-operating-model.md — which had shipped with zero
validator coverage. The review repaired three defects between them (TO §7.3
'Outbound (51)' vs role-sum 50; IT-model '~11 external integration clusters' vs
the canonical ten; a §13.3-for-§13.2 seasonal-calendar §-ref) plus an
unresolvable §2.4 self-reference, and added: doc-scoped retired literals, the
required corrected anchors (incl. the 171+17=188 / 4,864+499=5,363 IT-model
reconciliation sums and the TO's two-state 469/6,869 totals), and a structural
rule that re-derives every §7.3 DC-roster group total from its own HC cells.

2026-09-03 hybrid capability-sourcing revision: anchors re-based to OM v2.0 (adds the
66+49=115 sizing sum) and TO v1.3 (HQ 504 / total 6,904; IT = 115 / 16 product teams),
with the v1.x sizing/shape literals retired doc-scoped. See the CHANGELOG entry for
2026-09-03 and 07-methodology/capability-sourcing-and-engineering-model.md.

2026-09-03 agentic-AI extension: OM v2.1 sizing anchor re-based 66+49=115 → 66+56=122
(AI & Agent Platform +7); TO v1.4 anchors re-based to HQ 511 / total 6,911 (~440–515
band row; 504+7=511) with the 115-era literals retired.

2026-09-03 post-AAP consistency pass: the two remaining uncovered methodology documents —
capability-sourcing-and-engineering-model.md and technical-guidelines.md — join DOCS (the
sourcing doc had quoted the stale pre-confirmation tier trio 1,375/3,243/754 in its §12.1
autonomy ladder precisely because it shipped outside this guard). Two structural rules are
added: (a) sourcing_tier_hits — the §12.1 autonomy-ladder tier counts are re-derived from
the criticality register's Summary table on every run; (b) to_phase_hits — the TO's §11
phase rows must have each HC-delta cell equal the sum of its own named from→to moves, the
three deltas sum to the stated total, and that total equal target-minus-current HQ (the
pass found the cells internally inconsistent since adoption: −7/−6/+13 against their rows,
with each IT re-base bumping only the Phase 3 cell). The change-note exemption is also
fixed to strip the whole version-history footer (from the first '*Date:' or
'*Document Version:' line to end-of-file) instead of only up to its first ')'.

2026-09-03 index-trueness pass: the description surfaces OUTSIDE the 7 guarded docs can
also go stale, and 07-methodology/README.md had two such live defects — its OM row still
pinned '(v2.1' after the doc bumped to v2.2 (the §9.3 clarification pass), and its
validate-repo.sh row still described this guard's TO anchors as the superseded two-state
pair 469/6,869 after the v1.4 re-base to 511/6,911. New structural rule
methodology_index_hits: every '(vN.M' version pin on a row naming one of the versioned
methodology docs must equal that doc's own '*Document Version:' footer, and the retired
pair must not reappear. Teeth verified by synthetic injection (stale pin and retired pair
both caught, then restored clean). The root README's drifted 'merge note atop CHANGELOG'
pointer was also re-pointed to the 2026-09-02 branch-reconciliation entry — a
position-independent phrasing, so the class cannot recur there.

2026-09-03 description-trueness pass: three more live description-surface staleness spots
outside the 7 guarded docs — the executive summary's top footer still claimed
"updated counts: … 5,363 workflows" after the event-custody pass moved the canon to 5,364
(batch 5 had trued exactly this line; the W5511 re-point list missed it), the IT operating
model's footer 'Downstream:' pointer still pinned TO v1.4 / technical-guidelines v3.1 /
sourcing v1.1 after the post-AAP pass bumped all three (v1.5 / v3.2 / v1.2), and the
headcount reality-check STATUS banner still cited TO v1.4 / OM v2.1. All three trued, and
the new structural rule live_pin_hits pins every version pin on those surfaces to the
target docs' own '*Document Version:' footer and the executive-summary top footer to the
canonical register totals (index Grand Total; requirement row count). Teeth verified by
synthetic injection (stale OM pin, stale banner pin, and a regressed exec-summary count
all caught, then restored clean).

2026-09-03 consistency review pass: two more straggler classes found and trued, both
outside every previously-read surface. (a) The criticality register's '### Tier 2
Additions' sub-heading still claimed (495 Workflows) after the two 2026-09-03 gap-fill
passes appended six rows to that section (W5512–W5514 agentic, W5515–W5517 sourcing) —
the batch-7 pass had trued the top-level Tier-2 heading and Summary but not this
parenthetical. New structural rule register_heading_hits: every '(n Workflows)'
parenthetical in the register is re-derived from its data rows (direct rows for
family/Additions/history-pass/####-tier headings; the effective per-tier total for the
three '## Tier N' headings), and the effective per-tier totals must equal both the
heading claims and the ## Summary table's per-phase counts — closing the
rows → headings → Summary chain end-to-end. (b) The VS-24 and VS-87 README Process-Areas
tables still carried the pre-W239-move counts (PA-24.3 8/Total 27, PA-87.3 8/Total 24 —
the 03235a5 cascade re-pointed the index/root-README/dependency-map but missed both
README tables; now validator Check 67). Three stale live-body version pins in the
guarded docs also trued in place (sourcing-model header '(v2.0+)' and §13 row '(v2.1:'
re-pinned to OM v2.4; OM §13 row 'this v2.0 model' re-pinned to v2.4).
"""

def _doc_versions():
    """Current '*Document Version:' footer of each versioned doc (basename -> 'N.M')."""
    versions = {}
    for rel in ["optimal-table-of-organization.md",
                "model-company-profile.md",
                "../07-methodology/it-product-operating-model.md",
                "../07-methodology/capability-sourcing-and-engineering-model.md",
                "../07-methodology/technical-guidelines.md"]:
        m = re.search(r"^\*Document Version: (\d+\.\d+)",
                      open(os.path.join(MC, rel), encoding="utf-8").read(), re.M)
        if m:
            versions[os.path.basename(rel)] = m.group(1)
    return versions


def _pin_hits(segment, base_line, where, versions, names):
    """The LAST 'name' occurrence in the segment carries the live pin (both surfaces
    append newest-at-the-end / newest-on-top respectively, so the newest pin is the
    one adjacent to the last mention); it must equal the target doc's footer version,
    and a bare mention with no 'vN.M' within the pin window is itself a defect."""
    hits = []
    for name in names:
        want = versions.get(name)
        if want is None:
            hits.append((where, 0, f"{name} has no parseable '*Document Version:' footer"))
            continue
        pos = segment.rfind(name)
        if pos < 0:
            hits.append((where, 0, f"{name} not referenced in {where}"))
            continue
        line = base_line + segment[:pos].count("\n")
        # pin window ends at the next '.md' boundary so an adjacent doc's pin
        # can never be attributed to this name
        nxt = segment.find(".md", pos + len(name))
        window = segment[pos + len(name): nxt + 3 if nxt >= 0 else pos + len(name) + 120]
        m = re.search(r"v(\d+\.\d+)", window)
        if not m:
            hits.append((where, line,
                         f"{name} mentioned in {where} without a version pin "
                         f"(doc footer says v{want})"))
        elif m.group(1) != want:
            hits.append((where, line,
                         f"{name} pinned at v{m.group(1)} in {where} but the doc "
                         f"footer says v{want}"))
    return hits


def live_pin_hits():
    """2026-09-03 description-trueness pass — pins the three live description surfaces
    outside the guarded docs (all three found stale in the same pass): the IT operating
    model's footer 'Downstream:' pointer, the headcount reality-check STATUS banner, and
    the executive summary's top footer count line (its only workflow/requirement-count
    claim). Version pins must equal the target docs' own '*Document Version:' footers,
    and the executive-summary counts must equal the canonical registers (index Grand
    Total row; requirement register row count)."""
    hits = []
    versions = _doc_versions()
    # (a) IT operating model footer 'Downstream:' pointer (last 'Downstream:' in the doc)
    om = open(os.path.join(MC, "..", "07-methodology", "it-product-operating-model.md"),
              encoding="utf-8").read()
    pos = om.rfind("Downstream:")
    if pos < 0:
        hits.append(("it-product-operating-model.md", 0,
                     "footer 'Downstream:' pointer not found"))
    else:
        hits.extend(_pin_hits(om[pos:], om[:pos].count("\n") + 1,
                              "it-product-operating-model.md (Downstream)",
                              versions,
                              ["optimal-table-of-organization.md",
                               "model-company-profile.md",
                               "technical-guidelines.md",
                               "capability-sourcing-and-engineering-model.md"]))
    # (b) headcount reality-check STATUS banner (first 10 lines — newest-last chain)
    rc = open(os.path.join(MC, "headcount-reality-check.md"), encoding="utf-8").read()
    banner_lines = rc.splitlines()[:10]
    banner = "\n".join(banner_lines)
    hits.extend(_pin_hits(banner, 1,
                          "headcount-reality-check.md (STATUS banner)", versions,
                          ["optimal-table-of-organization.md",
                           "it-product-operating-model.md"]))
    # (c) executive summary top footer counts vs the canonical registers
    ex = open(os.path.join(MC, "executive-summary.md"), encoding="utf-8").read()
    top = re.search(r"^\*Date: (.*)$", ex, re.M)
    if not top:
        hits.append(("executive-summary.md", 0, "no '*Date:' footer entry found"))
    else:
        ex_line = ex[:top.start()].count("\n") + 1
        idx = open(os.path.join(MC, "workflows", "value-stream-index.md"),
                   encoding="utf-8").read()
        mwf = re.search(r"\*\*Grand Total\*\* \| \*\*[\d,]+\*\* \| \*\*([\d,]+)\*\*", idx)
        reqs = open(os.path.join(MC, "erp-requirements.md"), encoding="utf-8").read()
        nreq = len(set(re.findall(r"^\| (?:\*\*)?[A-Z]+-\d+[a-z]?\b", reqs, re.M)))
        if not mwf:
            hits.append(("executive-summary.md", 0,
                         "value-stream-index Grand Total row not parseable"))
        elif f"{mwf.group(1)} workflows" not in top.group(0):
            hits.append(("executive-summary.md", ex_line,
                         f"top footer does not carry the canonical '{mwf.group(1)} workflows' "
                         f"(index Grand Total)"))
        if f"{nreq} requirements" not in top.group(0):
            hits.append(("executive-summary.md", ex_line,
                         f"top footer does not carry the canonical '{nreq} requirements' "
                         f"(requirement register row count)"))
    return hits


import argparse, glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MC = os.path.join(REPO, "01-model-company")

# Paths relative to MC (".."-prefixed entries live in 07-methodology).
# Consistency review #68 (2026-09-02) brought the two organizational documents
# issued 2026-09-01/02 under this guard — both had shipped with zero validator
# coverage, and the review found three figure/citation defects between them.
DOCS = ["mobile-app-strategy.md", "data-migration-mapping.md",
        "assumptions-and-design-decisions.md",
        "optimal-table-of-organization.md",
        "../07-methodology/it-product-operating-model.md",
        "../07-methodology/capability-sourcing-and-engineering-model.md",
        "../07-methodology/technical-guidelines.md"]
RETIRED_FIGURES = ["6,757", "6,715", "5,357", "5,362", "5,349", "5,341",
                   "80,000 SKU", "1,000 POS terminal"]

# Consistency review #68 — doc-scoped retired literals (the exact defect forms
# the review repaired; matches on version-history footer lines are exempt) and
# required presence anchors (the corrected canonical forms must stay present).
RETIRED_LITERALS = {
    "it-product-operating-model.md": [
        # the canonical integration architecture (data-volumes-and-integrations.md
        # §2 diagram and §3 detail matrix) carries exactly ten external clusters
        "11 external integration clusters",
        # the profile's seasonal calendar is §13.2; §13.3 is Promotional Strategy
        "§13.3 seasonal calendar",
        # 2026-09-03 hybrid capability-sourcing revision (OM v2.0): the unified-model
        # sizing/shape literals are retired — 16 teams / 115 FTE is the canon
        "80-FTE steady-state sizing",
        "Phased build-up (50 → 80)",
        "80-FTE IT sizing",
        # 2026-09-03 agentic extension (OM v2.1): sizing 115 → 122 (AAP +7)
        "Steady-state design (115 IT FTE)",
        "Phased build-up (50 → 115)",
        "115-FTE IT sizing",
    ],
    "optimal-table-of-organization.md": [
        # §7.3 Outbound role HCs sum to 50 (the 150 grand total confirms)
        "Outbound (51)",
        # unresolvable subsection-style self-reference (§2 has no §2.4 heading)
        "three-lines model, §2.4",
        # 2026-09-03 hybrid revision (TO v1.3): target is HQ 504 / total 6,904 with
        # IT = 115 / 16 product teams — the v1.2 literals are retired
        "12 product teams per",
        "IT 50→80",
        "80 FTE, 12 product teams",
        # 2026-09-03 agentic extension (TO v1.4): target HQ 511 / total 6,911, IT = 122 / 17 teams
        "16 product teams per",
        "IT 50→115",
    ],
}
ANCHORS = {
    "it-product-operating-model.md": [
        "10 external integration clusters",
        "§13.2 seasonal calendar",
        "**171 + 17 = 188**",
        "**4,878 + 509 = 5,387**",
        # v2.0 hybrid sizing anchor (66 domain + platform/CIO = 115 FTE); v2.1 agentic
        # re-bases it to 122 (66 + 56, AAP +7)
        "**66 + 56 = 122**",
    ],
    "optimal-table-of-organization.md": [
        "Outbound (50)",
        "**511** | **6,911**",
        "**Total HQ** | **362** | **~440–515** | **511**",
        "**504 + 7 = 511**",
        "× 4 DCs = **600**",
    ],
}

# Consistency review #60: BIR Forms 1601-E/1601-F were discontinued by RR 11-2018
# (replaced by the quarterly 1601-EQ creditable / 1601-FQ final remittance
# returns). Guarded here in the two statutory-citation model docs (profile
# §10.5/§16 and erp-requirements FIN rows); the PA files are guarded by Check 62's
# legacy_form rule. Version-history footers are exempt — they legitimately name
# the retired form when describing the change.
LEGACY_FORM = re.compile(r"1601-[EF](?!Q)")
LEGACY_FORM_DOCS = ["model-company-profile.md", "erp-requirements.md"]


def legacy_form_hits(path):
    hits = []
    for i, line in enumerate(open(path, encoding="utf-8").read().splitlines(), 1):
        if line.startswith("*Document Version:"):
            continue
        for m in LEGACY_FORM.finditer(line):
            hits.append((os.path.basename(path), i,
                         f'retired BIR form "{m.group(0)}" '
                         f'(use 1601-EQ/1601-FQ per RR 11-2018)'))
    return hits


def load_registers():
    wids, vsids, paids, ctlids, reqids = set(), set(), set(), set(), set()
    for f in glob.glob(os.path.join(MC, "workflows", "VS-*", "PA-*.md")):
        text = open(f, encoding="utf-8").read()
        wids |= set(re.findall(r"^## (W\d+[A-Z]?)\.", text, re.M))
        m = re.match(r"(PA-\d+\.\d+)", os.path.basename(f))
        if m:
            paids.add(m.group(1))
    vsids |= set(re.findall(r"\bVS-\d+\b",
                            open(os.path.join(MC, "workflows", "value-stream-index.md"),
                                 encoding="utf-8").read()))
    ctlids |= set(re.findall(r"^\| (CTL-\d+) ",
                             open(os.path.join(MC, "internal-controls-matrix.md"),
                                  encoding="utf-8").read(), re.M))
    reqids |= set(re.findall(r"^\| ([A-Z]+-\d+) ",
                             open(os.path.join(MC, "erp-requirements.md"),
                                  encoding="utf-8").read(), re.M))
    return wids, vsids, paids, ctlids, reqids


def sections_of(path):
    return set(re.findall(r"^#{2,4} (\d+(?:\.\d+)*)[.\s]",
                          open(path, encoding="utf-8").read(), re.M))


def strip_footer(text):
    """Change-note exemption: everything from the first version-history footer line
    ('*Date: …' or '*Document Version: …') to end-of-file is a change-note and is
    exempt from the retired-literal / resolution checks. (The previous regex stripped
    only up to the footer's first ')' — which exempted almost nothing for the
    '*Document Version:'-style footers the 2026-09-03 org documents use.)"""
    m = re.search(r"^\*(?:Date|Document Version):", text, flags=re.M)
    return text[:m.start()] if m else text


def dc_roster_hits(path):
    """Consistency review #68 — structural guard for the target-state TO's §7.3
    DC roster: re-derives every group header's '(N)' from the HC cells beneath
    it, checks the group headers against the stated grand total, and checks the
    grand total against the '× 4 DCs = 600' chain-total anchor. (The review
    found the Outbound group labelled 51 while its roles sum to 50.)"""
    rel = "optimal-table-of-organization.md"
    hits = []
    lines = open(path, encoding="utf-8").read().splitlines()
    start = next((i for i, l in enumerate(lines)
                  if l.strip().startswith("| Function | Role | HC")), None)
    if start is None:
        return [(rel, 0, "DC roster table (§7.3) not found")]
    groups, cur, grand = [], None, None
    for ln, l in enumerate(lines[start + 1:], start + 2):
        if not l.strip().startswith("|"):
            break
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        m = re.fullmatch(r"\*\*(.+?) \((\d+)\)\*\*", cells[0])
        if m:
            cur = {"name": m.group(1), "declared": int(m.group(2)),
                   "sum": 0, "line": ln}
            groups.append(cur)
        if cur is not None and re.fullmatch(r"\d[\d,]*", cells[2]):
            cur["sum"] += int(cells[2].replace(",", ""))
        if cells[1] == "**Total**":
            mm = re.search(r"\d[\d,]*", cells[2])
            if mm:
                grand = int(mm.group(0).replace(",", ""))
    for g in groups:
        if g["sum"] != g["declared"]:
            hits.append((rel, g["line"],
                         f"DC roster group '{g['name']}' header says ({g['declared']}) "
                         f"but its HC cells sum to {g['sum']}"))
    declared_total = sum(g["declared"] for g in groups)
    if grand is None:
        hits.append((rel, 0, "DC roster grand-total row not found"))
    elif grand != declared_total:
        hits.append((rel, 0, f"DC roster grand total {grand} != sum of group "
                             f"headers {declared_total}"))
    if grand == 150 and not any("× 4 DCs = **600**" in l for l in lines):
        hits.append((rel, 0, "DC roster 150-grand-total anchor '× 4 DCs = **600**' missing"))
    return hits


def sourcing_tier_hits():
    """2026-09-03 post-AAP pass — structural guard for the sourcing model's §12.1
    autonomy ladder: its three tier counts are re-derived from the criticality
    register's Summary table on every run. (The pass found the ladder quoting the
    pre-confirmation trio 1,375/3,243/754 — the register as it stood before the
    2026-09-02 post-catalog confirmation — because the doc shipped outside this
    guard's doc set.)"""
    rel = "capability-sourcing-and-engineering-model.md"
    hits = []
    reg = open(os.path.join(MC, "workflows", "workflow-criticality-classification.md"),
               encoding="utf-8").read()
    canon = {}
    confirmed = re.search(r"### Confirmed classification.*?(?=^### |^## )", reg,
                          re.M | re.S)
    if confirmed:
        for m in re.finditer(r"^\| Phase (\d) \| [^|]+ \| ([\d,]+) \|", confirmed.group(0), re.M):
            canon[f"Tier {m.group(1)}"] = int(m.group(2).replace(",", ""))
    if len(canon) != 3:
        return [(rel, 0, "criticality register Summary table not parseable — "
                         "cannot derive canon tier counts")]
    src = open(os.path.normpath(os.path.join(MC, "..", "07-methodology", rel)),
               encoding="utf-8").read()
    body = strip_footer(src)
    quoted = {}
    for m in re.finditer(r"\*\*Tier (\d)\*\* \(([\d,]+)", body):
        quoted[f"Tier {m.group(1)}"] = int(m.group(2).replace(",", ""))
    if len(quoted) != 3:
        hits.append((rel, 0, f"autonomy-ladder tier counts incomplete: found "
                             f"{sorted(quoted)} — expected three '**Tier N** (n)' cells"))
    for tier, want in sorted(canon.items()):
        got = quoted.get(tier)
        if got != want:
            hits.append((rel, 0, f"autonomy ladder quotes {tier} = {got} but the "
                                 f"register Summary says {want}"))
    return hits


def to_phase_hits():
    """2026-09-03 post-AAP pass — structural guard for the target-state TO's §11
    phasing table: each phase row's HC-delta cell must equal the sum of the
    from→to moves named in its own Moves cell; the three deltas must sum to the
    stated total; and that total must equal target-minus-current HQ. (The pass
    found the cells internally inconsistent since adoption — −7/−6/+13 against
    their rows — because each IT re-base bumped only the Phase 3 cell.)"""
    rel = "optimal-table-of-organization.md"
    hits = []
    lines = open(os.path.join(MC, rel), encoding="utf-8").read().splitlines()
    start = next((i for i, l in enumerate(lines) if "Sizing & Phasing" in l), None)
    if start is None:
        return [(rel, 0, "§11 Sizing & Phasing section not found")]
    pair_re = re.compile(r"([A-Za-z][A-Za-z/&\- ]*?)\s*(\d[\d,]*)\s*[→-]>?\s*(\d[\d,]*)")
    # (the doc uses the unspaced '14→20' form; a spaced '14 -> 20' form is accepted too)
    deltas = []
    total_declared = None
    total_range = None
    for l in lines[start:start + 40]:
        if not l.strip().startswith("|"):
            if deltas and total_declared is None:
                break
            continue
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        if cells[2] == "**Total**" or (cells[0] == "" and "**Total**" in cells):
            mm = re.search(r"\*\*(\d[\d,]*)\s*→\s*(\d[\d,]*)\s*\(\+([\d,]+)\)\*\*",
                           cells[3] or "")
            if mm:
                total_range = (int(mm.group(1).replace(",", "")),
                               int(mm.group(2).replace(",", "")))
                total_declared = int(mm.group(3).replace(",", ""))
            continue
        if not re.match(r"\*\*\d", cells[0] or ""):
            continue
        moves, declared = cells[2], cells[3]
        moves, declared = cells[2], cells[3]
        mm = re.search(r"\+([\d,]+)", declared)
        if not mm:
            continue
        declared_n = int(mm.group(1).replace(",", ""))
        named = 0
        for a, b, c in pair_re.findall(moves):
            named += int(c.replace(",", "")) - int(b.replace(",", ""))
        phase = re.search(r"\*\*(\d)", cells[0]).group(1)
        if named != declared_n:
            hits.append((rel, start + 1,
                         f"§11 Phase {phase} delta cell says +{declared_n} but its named "
                         f"moves sum to {named:+d}"))
        deltas.append((phase, declared_n))
    if total_declared is None:
        hits.append((rel, 0, "§11 total row ('362 → 511 (+149)') not found"))
    else:
        if sum(d for _, d in deltas) != total_declared:
            hits.append((rel, 0, f"§11 phase deltas {[d for _, d in deltas]} do not sum "
                                 f"to the stated total +{total_declared}"))
        if total_range and total_range[1] - total_range[0] != total_declared:
            hits.append((rel, 0, f"§11 total row range {total_range[0]} → {total_range[1]} "
                                 f"implies +{total_range[1] - total_range[0]}, not "
                                 f"+{total_declared}"))
    return hits


def methodology_index_hits():
    """2026-09-03 index-trueness pass — the description surfaces outside the 7 guarded
    docs can go stale in exactly two ways, both found live in 07-methodology/README.md:
    a '(vN.M' version pin left behind by a doc bump (OM row said v2.1 after v2.2
    shipped), and a description of this guard's TO anchors quoting the superseded
    two-state pair (469/6,869 after the 511/6,911 re-base). Rule: every '(vN.M' pin on a
    row naming one of the versioned methodology docs must equal that doc's own
    '*Document Version:' footer, and the retired pair must not reappear."""
    rel = "README.md"
    hits = []
    index_path = os.path.join(REPO, "07-methodology", rel)
    versioned = {"it-product-operating-model.md",
                 "capability-sourcing-and-engineering-model.md",
                 "technical-guidelines.md"}
    current = {}
    for name in versioned:
        m = re.search(r"^\*Document Version: (\d+\.\d+)",
                      open(os.path.join(REPO, "07-methodology", name),
                           encoding="utf-8").read(), re.M)
        if m:
            current[name] = m.group(1)
    for ln, l in enumerate(open(index_path, encoding="utf-8").read().splitlines(), 1):
        if "469/6,869" in l:
            hits.append((rel, ln, 'retired TO-anchor pair "469/6,869" (the guard\'s '
                         'two-state anchors are 362/6,762 → 511/6,911)'))
        for name, ver in current.items():
            if name not in l:
                continue
            for m in re.finditer(r"\(v(\d+\.\d+)", l):
                if m.group(1) != ver:
                    hits.append((rel, ln, f"{name} pinned at v{m.group(1)} but the doc "
                                          f"footer says v{ver}"))
    return hits


def register_heading_hits():
    """2026-09-03 consistency review pass — structural guard for the criticality
    register's own section-heading counts. Every '(n Workflows)' parenthetical is
    re-derived from the data rows beneath it (nested sub-heading rows roll up):
    family/Additions/history-pass/####-tier headings hold their subtree rows; the
    three '## Tier N' headings (checked at end-of-file) must equal the effective
    per-tier total — original + Additions + history-pass '#### Tier N' blocks — and
    that total must also equal the ## Summary table's per-phase counts (the canon
    source that sourcing_tier_hits re-derives from — with this rule the
    rows -> headings -> Summary chain is closed end-to-end). The pass found
    '### Tier 2 Additions (495 Workflows)' holding 501 rows after the two 2026-09-03
    gap-fill passes appended six rows without bumping the parenthetical — exactly the
    straggler class that survived because the Summary table was trued while the
    intermediate heading was not."""
    rel = "workflow-criticality-classification.md"
    hits = []
    lines = open(os.path.join(MC, "workflows", rel), encoding="utf-8").read().splitlines()
    tier_rows = {1: 0, 2: 0, 3: 0}
    tier_heading_claim = {}
    summary_claim = {}
    cur = None                      # effective tier attribution context
    stack = []                      # [level, text, line_no, rows]

    def close_top():
        level, text, ln, rows = stack.pop()
        if re.match(r"^Tier \d:", text):
            return                  # '## Tier N' totals checked at end-of-file
        m = re.search(r"\(([\d,]+)\s*[Ww]orkflows?\)", text)
        if m and int(m.group(1).replace(",", "")) != rows:
            hits.append((rel, ln, f"heading '{text[:70]}' claims ({m.group(1)}) "
                                  f"but holds {rows} row(s)"))
        if stack:
            stack[-1][3] += rows    # roll up into the enclosing heading

    for ln, l in enumerate(lines, 1):
        m = re.match(r"^(#{1,4}) (.*)", l)
        if m:
            level = len(m.group(1))
            text = m.group(2)
            while stack and stack[-1][0] >= level:
                close_top()
            tm = re.match(r"^Tier (\d):", text)
            am = re.match(r"^Tier (\d) Additions", text)
            t4 = re.match(r"^Tier (\d)", text)
            if tm:
                cur = int(tm.group(1))
                tier_heading_claim[int(tm.group(1))] = (text, ln)
            elif am:
                cur = int(am.group(1))
            elif level == 4 and t4:
                cur = int(t4.group(1))
            elif level <= 2:
                cur = None
            stack.append([level, text, ln, 0])
            continue
        sm = re.match(r"^\| Phase (\d) \|[^|]+\|\s*([\d,]+)\s*\|", l)
        if sm and stack and stack[-1][1].startswith("Confirmed classification"):
            summary_claim[int(sm.group(1))] = int(sm.group(2).replace(",", ""))
            continue
        if re.match(r"^\| (W\d+[A-Z]?) \| ", l):
            if stack:
                stack[-1][3] += 1
            if cur:
                tier_rows[cur] += 1
    while stack:
        close_top()

    for n in (1, 2, 3):
        claim = tier_heading_claim.get(n)
        if claim is None:
            hits.append((rel, 0, f"## Tier {n} heading not found"))
            continue
        text, ln = claim
        m = re.search(r"\(([\d,]+)\s*[Ww]orkflows?\)", text)
        declared = int(m.group(1).replace(",", "")) if m else None
        if declared != tier_rows[n]:
            hits.append((rel, ln, f"## Tier {n} heading claims ({declared}) but the "
                                  f"register holds {tier_rows[n]} Tier-{n} row(s)"))
        want = summary_claim.get(n)
        if want is not None and want != tier_rows[n]:
            hits.append((rel, ln, f"## Summary Phase {n} count {want} != the register's "
                                  f"{tier_rows[n]} Tier-{n} row(s)"))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guard", action="store_true",
                    help="exit 1 on any unresolved reference or retired figure")
    args = ap.parse_args()
    wids, vsids, paids, ctlids, reqids = load_registers()
    prof_secs = sections_of(os.path.join(MC, "model-company-profile.md"))
    tg_secs = sections_of(os.path.join(REPO, "07-methodology", "technical-guidelines.md"))
    dv_secs = sections_of(os.path.join(MC, "data-volumes-and-integrations.md"))
    # review #68: the two organizational docs also cite the headcount reality
    # check and the IT operating model — both join the bare-§ fallback union
    rc_secs = sections_of(os.path.join(MC, "headcount-reality-check.md"))
    it_secs = sections_of(os.path.join(REPO, "07-methodology",
                                       "it-product-operating-model.md"))
    hits = []
    for rel in DOCS:
        doc = os.path.basename(rel)
        path = os.path.normpath(os.path.join(MC, rel))
        text = open(path, encoding="utf-8").read()
        body = strip_footer(text)
        for m in re.finditer(r"\b(W\d+[A-Z]?|VS-\d+|CTL-\d+|PA-\d+\.\d+|[A-Z]{2,4}-\d{3})\b", body):
            tok = m.group(1)
            line = body[:m.start()].count("\n") + 1
            # review #68: dispatch prefixed namespaces FIRST — the generic
            # requirement pattern would otherwise swallow 3-digit VS-1xx/CTL-1xx
            # tokens (e.g. VS-101 fullmatches [A-Z]{2,4}-\d{3})
            if re.fullmatch(r"W\d+[A-Z]?", tok):
                if tok not in wids:
                    hits.append((doc, line, f"unresolved {tok}"))
            elif tok.startswith("VS") and tok not in vsids:
                hits.append((doc, line, f"unresolved {tok}"))
            elif tok.startswith("CTL") and tok not in ctlids:
                hits.append((doc, line, f"unresolved {tok}"))
            elif tok.startswith("PA") and tok not in paids:
                hits.append((doc, line, f"unresolved {tok}"))
            elif re.fullmatch(r"[A-Z]{2,4}-\d{3}", tok) and not re.match(r"(?:VS|CTL|PA)-", tok):
                # (namespace-prefixed tokens that RESOLVED above must not
                # fall through into the requirement register check —
                # VS-177 fullmatches the generic requirement shape)
                if tok not in reqids:
                    hits.append((doc, line, f"unresolved requirement {tok}"))
        for m in re.finditer(r"(Technical Guidelines|technical-guidelines)\s*§(\d+(?:\.\d+)?)", body):
            if m.group(2) not in tg_secs:
                hits.append((doc, body[:m.start()].count("\n") + 1,
                             f"unresolved technical-guidelines §{m.group(2)}"))
        for m in re.finditer(r"(?<!Guidelines )(?<!guidelines )§(\d+(?:\.\d+)?)", body):
            sec = m.group(1)
            own = sections_of(path)
            if sec not in prof_secs and sec not in own and sec not in dv_secs \
                    and sec not in rc_secs and sec not in it_secs:
                hits.append((doc, body[:m.start()].count("\n") + 1,
                             f"unresolved §{sec}"))
        for lit in RETIRED_LITERALS.get(doc, []):
            for m in re.finditer(re.escape(lit), body):
                line_start = body.rfind("\n", 0, m.start()) + 1
                if body[line_start:line_start + 20].startswith(("*Date:", "*Document Version:")):
                    continue  # version-history footer
                hits.append((doc, body[:m.start()].count("\n") + 1,
                             f'retired literal "{lit}"'))
        for anc in ANCHORS.get(doc, []):
            if anc not in body:
                hits.append((doc, 0, f'missing required anchor "{anc}"'))
        for lit in RETIRED_FIGURES:
            for m in re.finditer(re.escape(lit), body):
                hits.append((doc, body[:m.start()].count("\n") + 1,
                             f"retired figure {lit}"))
    for doc in LEGACY_FORM_DOCS:
        for d, line, detail in legacy_form_hits(os.path.join(MC, doc)):
            hits.append((d, line, detail))
    hits.extend(dc_roster_hits(os.path.join(MC, "optimal-table-of-organization.md")))
    hits.extend(to_phase_hits())
    hits.extend(sourcing_tier_hits())
    hits.extend(register_heading_hits())
    hits.extend(methodology_index_hits())
    hits.extend(live_pin_hits())
    for doc, line, detail in hits:
        print(f"model-doc: {doc}:{line}: {detail}")
    print(f"audit-model-docs: {len(hits)} hit(s) across {len(DOCS)} documents")
    if args.guard:
        sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
