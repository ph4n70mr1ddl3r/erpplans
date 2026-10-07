#!/usr/bin/env python3
"""
audit-matrix-refs.py — matrix ghost-only rows, gap-analysis current-state figures,
and technical-guidelines anchor guard.

Consistency review #43 (2026-08-29) audited the three surfaces:

  * requirement-workflow-matrix.md cell-by-cell — all 724 rows' W tokens
    resolve (Checks 4/6 green); the letter-suffixed aliases (W5B, W9A, W2A…
    ~1,400 prose mentions) are the sanctioned POS-family sub-workflow
    shorthand resolved via prose. The defect class repaired: **8 rows were
    mapped ONLY to ghost aliases** (POS-004/011/012/017/018, RPT-007,
    NFR-003, NFR-015 — e.g. FIN-054/055's W9A) leaving the requirement
    untraceable to any real workflow header; each re-pointed to the real
    workflows that exercise it (W5, W463, W520, W528, W1282/W1485, W1425,
    W9, W14).
  * workflow-gap-analysis.md summary figures — the current-state declaration
    quotes 188 VS / 569 PA / 5,364 workflows and the fourteen post-catalog
    workflows plus the W5511 event-custody addition; the smaller totals (5,349…5,363)
    and the 6,757 headcount live
    inside per-pass historical notes, exempt per the change-note convention.
  * technical-guidelines.md quantitative claims — verified against current
    state: offline capacity 933 peak-day (= 467 avg × 2.0), event latency
    < 30 sec, price push ≤ 60 sec, offline ≥ 8 hours, bandwidth table
    (200 × 2 Mbps + 4 × 10 + 100 HQ = 540 Mbps aggregate, ~362 HQ staff,
    ~80 RF guns/DC, 205 sites), RTO ≤ 4 hours, 10-year retention.

Guard mode (--guard, validator Check 61):
  1. no requirement-matrix row may map only to ghost (non-header) W tokens;
  2. the gap-analysis current-state line must quote the canonical totals;
  3. technical-guidelines must carry its verified anchor figures;
  4. set-coverage rules (2026-09-10 coverage pass): every erp-requirements.md
     register ID carries a matrix row, every matrix row references >= 1
     workflow (the 'All' claim, now guarded), and the Coverage Validation
     section quotes the re-derived distinct-workflows-referenced count and
     the Tier-1 mapped share — the workflow-side gap (declared incremental
     by design, VS-53–VS-192 pending) stays a tracked metric until closed.
"""
import argparse, glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MC = os.path.join(REPO, "01-model-company")

TG_ANCHORS = ["~362 HQ staff (≈325 concurrent users)", "~540 Mbps aggregate",
              "≥ 8 hours", "933 peak-day transactions per store",
              "10 years"]
GA_ANCHOR = "**188 value streams · 569 process areas · 5,370 workflows**"


def coverage_rules():
    """2026-09-10 coverage pass — set-closure + pinned-coverage metrics for
    requirement-workflow-matrix.md. Re-derives everything from the register,
    the matrix, and the catalog index every run; the doc must quote the
    re-derived figures (change forces a conscious re-point, the Check-74
    deferred-anchor pattern)."""
    hits = []
    matrix = open(os.path.join(MC, "requirement-workflow-matrix.md"),
                  encoding="utf-8").read()
    reqs = open(os.path.join(MC, "erp-requirements.md"), encoding="utf-8").read()
    reg_ids = set(re.findall(r"^\| ([A-Z]{2,4}-\d{1,4}[a-z]?) \|", reqs, re.M))
    rows = re.findall(
        r"^\| ([A-Z]{2,4}-\d{1,4}[a-z]?) \|[^|]+\|[^|]+\| (.*?) \| (.*?) \|$",
        matrix, re.M)
    matrix_ids = {rid for rid, _, _ in rows}
    wtok = re.compile(r"\bW\d+[A-Z]?\b")
    no_wf = [rid for rid, prim, supp in rows
             if not (wtok.search(prim) or wtok.search(supp))]
    missing = sorted(reg_ids - matrix_ids)
    if missing:
        hits.append(("coverage-register-id-unmapped",
                     "requirement-workflow-matrix.md", 0,
                     f"{len(missing)} register ID(s) have no matrix row: "
                     f"{missing[:6]}"))
    if no_wf:
        hits.append(("coverage-zero-ref-row",
                     "requirement-workflow-matrix.md", 0,
                     f"{len(no_wf)} matrix row(s) reference no workflow: {no_wf[:6]}"))
    wfs = set()
    for _, prim, supp in rows:
        wfs.update(wtok.findall(prim))
        wfs.update(wtok.findall(supp))
    idx_path = os.path.join(REPO, "catalog", "index.json")
    try:
        import json
        idx = json.load(open(idx_path, encoding="utf-8"))
        live = {r["id"] for r in idx["workflows"]}
        t1 = {r["id"] for r in idx["workflows"] if r["tier"] == "Tier 1"}
    except Exception as e:
        hits.append(("coverage-index-unreadable", "catalog/index.json", 0, str(e)))
        return hits
    unres = sorted(wfs - live)
    if unres:
        hits.append(("coverage-unresolvable-wf",
                     "requirement-workflow-matrix.md", 0,
                     f"{len(unres)} referenced W id(s) are not live workflow "
                     f"headers: {unres[:6]}"))
    t1_cov = wfs & t1
    prim_ids = {r["id"] for r in idx["workflows"] if r["level"] == 2}
    for anchor in (
        f"**Distinct workflows referenced**: {len(wfs):,} of {len(prim_ids):,} "
        f"({len(wfs & prim_ids)} primary + {len(wfs - prim_ids)} sub-workflows)",
        f"**Tier-1 workflows mapped**: {len(t1_cov):,} of {len(t1):,}",
    ):
        if anchor not in matrix:
            hits.append(("coverage-anchor-missing",
                         "requirement-workflow-matrix.md", 0,
                         f"Coverage Validation must quote '{anchor}' — "
                         "re-derive and re-point (Check-74 deferred-anchor pattern)"))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guard", action="store_true")
    args = ap.parse_args()
    hits = []
    headers = set()
    for f in glob.glob(os.path.join(MC, "workflows", "VS-*", "PA-*.md")):
        headers |= set(re.findall(r"^## (W\d+[A-Z]?)\.",
                                  open(f, encoding="utf-8").read(), re.M))
    matrix = open(os.path.join(MC, "requirement-workflow-matrix.md"),
                  encoding="utf-8").read()
    for line in matrix.splitlines():
        m = re.match(r"^\| ([A-Z]{2,4}-\d{3}) \|", line)
        if not m:
            continue
        ws = re.findall(r"\b(W\d+[A-Z]?)(?:\.\d+[a-z]?)?\b", line)
        real = [w for w in ws if w in headers]
        ghosts = sorted({w for w in ws
                         if w not in headers and re.fullmatch(r"W\d+[A-Z]", w)})
        if ghosts and not real:
            hits.append(("ghost-only-row", "requirement-workflow-matrix.md", 0,
                         f"{m.group(1)} maps only to ghost aliases {ghosts}"))
    ga = open(os.path.join(MC, "workflows", "workflow-gap-analysis.md"),
              encoding="utf-8").read()
    if GA_ANCHOR not in ga:
        hits.append(("gap-analysis-current-state", "workflow-gap-analysis.md", 0,
                     f"missing canonical totals line '{GA_ANCHOR}'"))
    tg = open(os.path.join(REPO, "07-methodology", "technical-guidelines.md"),
              encoding="utf-8").read()
    for a in TG_ANCHORS:
        if a not in tg:
            hits.append(("tg-anchor", "technical-guidelines.md", 0,
                         f"missing anchor '{a}'"))
    coverage_hits = coverage_rules()
    hits.extend(coverage_hits)
    for kind, rel, line, detail in hits:
        print(f"{kind}: {rel}:{line}: {detail}")
    print(f"audit-matrix-refs: {len(hits)} hit(s)")
    if args.guard:
        sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
