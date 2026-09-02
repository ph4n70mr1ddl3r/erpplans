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
"""
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
        "../07-methodology/it-product-operating-model.md"]
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
    ],
    "optimal-table-of-organization.md": [
        # §7.3 Outbound role HCs sum to 50 (the 150 grand total confirms)
        "Outbound (51)",
        # unresolvable subsection-style self-reference (§2 has no §2.4 heading)
        "three-lines model, §2.4",
    ],
}
ANCHORS = {
    "it-product-operating-model.md": [
        "10 external integration clusters",
        "§13.2 seasonal calendar",
        "**171 + 17 = 188**",
        "**4,864 + 499 = 5,363**",
    ],
    "optimal-table-of-organization.md": [
        "Outbound (50)",
        "**469** | **6,869**",
        "**Total HQ** | **362** | **~440–470** | **469**",
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
        body = re.sub(r"^\*Date:.*?\)$", "", text, flags=re.M | re.S)  # change-notes exempt
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
    for doc, line, detail in hits:
        print(f"model-doc: {doc}:{line}: {detail}")
    print(f"audit-model-docs: {len(hits)} hit(s) across {len(DOCS)} documents")
    if args.guard:
        sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
