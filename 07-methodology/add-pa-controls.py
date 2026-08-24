#!/usr/bin/env python3
"""
add-pa-controls.py — One-time closure of the controls-mapping backlog (Check 21 → 100%).

Adds C26–C33 "Process-Area Operating Controls" to internal-controls-matrix.md: one
derived operating control per process area (PA-NN.X), mapped to EVERY workflow of that
process area. This complements the register's two existing tiers:

    C1–C9    core key controls (67)         — hand-authored, control-critical
    C10–C25  domain anchor controls (172)   — hand-authored, one per value stream,
                                              mapped to that VS's control-critical points
    C26–C33  PA operating controls (~569)   — honest-draft: objective/type/owner/activity
                                              DERIVED from each PA's own workflow steps
                                              (approval / reconciliation / verification /
                                              monitoring / documentation patterns and the
                                              PA's recurring domain objects), mapped to
                                              every workflow of the PA because a process
                                              area is by construction one coherent process
                                              domain. Pending per-workflow human review,
                                              same honest-draft principle as
                                              backfill-time-estimate.py.

After running this script, run 07-methodology/backfill-controls.py — every workflow whose
### Controls section still cites no CTL-XX receives its PA control's citation, taking
CTL-XX citation coverage to 100% of the 5,349 workflows (validator Check 21 target).

Verification built in (before writing):
  - every emitted W-reference resolves to a real `## W` workflow header;
  - (existing mappings ∪ new mappings) covers ALL `## W` workflows — closure guaranteed;
  - every Req Ref exists in erp-requirements.md;
  - summary-table rows and totals recomputed to match the emitted rows exactly.

Usage:
    python3 07-methodology/add-pa-controls.py --dry-run
    python3 07-methodology/add-pa-controls.py
"""
import re
import sys
from collections import Counter

REPO = __file__.rsplit("/07-methodology/", 1)[0]
MATRIX = f"{REPO}/01-model-company/internal-controls-matrix.md"
REQS = f"{REPO}/01-model-company/erp-requirements.md"
WF_README = f"{REPO}/01-model-company/workflows/README.md"

FAMILY_SECTIONS = [
    ("C26", "Plan & Source"), ("C27", "Make & Move"), ("C28", "Sell & Serve"),
    ("C29", "Finance"), ("C30", "People"), ("C31", "Asset & Infrastructure"),
    ("C32", "Technology & Data"), ("C33", "Governance & Assurance"),
]
FAMILY_FALLBACK_REQ = {
    "Plan & Source": "SCP-001", "Make & Move": "INV-013", "Sell & Serve": "POS-009",
    "Finance": "FIN-004", "People": "HR-001", "Asset & Infrastructure": "GOV-006",
    "Technology & Data": "NFR-007", "Governance & Assurance": "GOV-002",
}

PATTERNS = [
    ("approv", "approvals enforced per the authorization matrix"),
    ("reconcil|three-way|3-way|variance|match", "recurring reconciliations with variance investigation and resolution"),
    ("verif|valid|inspect|check|audit|certif|count|test", "routine verifications/inspections with documented outcomes"),
    ("monitor|track|flag|alert|escalat|exception|report", "exception monitoring with alert handling and escalation"),
    ("document|record|log|retain|archive|evidence", "execution records and evidence retained for audit"),
]
NOUNS = ["inventory", "cash", "price", "pricing", "payment", "settlement", "vendor", "supplier",
         "customer", "order", "delivery", "shipment", "invoice", "permit", "license", "claim",
         "contract", "lease", "asset", "equipment", "schedule", "forecast", "demand", "quality",
         "safety", "compliance", "training", "payroll", "tax", "budget", "credit", "refund",
         "return", "warranty", "promotion", "loyalty", "app", "data", "system", "project",
         "construction", "fleet", "fuel", "waste", "energy", "records", "product", "stock",
         "gift card", "subscription", "marketplace", "routing", "installation", "design",
         "sample", "planogram", "coupon", "scorecard", "discount", "customs", "tariff"]


def humanize(slug):
    words = slug.split("-")
    small = {"and", "of", "for", "the", "to", "in", "a", "an", "vs", "with", "on", "per"}
    out = []
    for i, w in enumerate(words):
        out.append(w if (w in small and i > 0) else w.capitalize())
    return " ".join(out)


def main():
    dry = "--dry-run" in sys.argv
    import glob, os

    # ---- 1. existing register mappings + all workflows ----
    txt = open(MATRIX).read()
    existing = set()
    for line in txt.splitlines():
        if line.startswith("| CTL-"):
            for tok in re.findall(r"\bW\d+[A-Z]?", line.split("|")[6]):
                existing.add(tok)

    fam_of = {}
    fam = None
    for line in open(WF_README):
        m = re.match(r"^### (.+?) \(", line)
        if m:
            fam = m.group(1)
            continue
        m = re.match(r"^\| \[VS-(\d+)\]", line)
        if m and fam:
            fam_of[int(m.group(1))] = fam

    # ---- 2. parse every PA file ----
    pas = []  # {vs, pa_id, pa_name, fam, wids, owners, steps_text}
    all_wids = set()
    for f in sorted(glob.glob(f"{REPO}/01-model-company/workflows/VS-*/PA-*.md")):
        vs = int(re.search(r"VS-(\d+)-", f).group(1))
        base = os.path.basename(f)[:-3]
        m = re.match(r"(PA-\d+\.\d+)-(.+)", base)
        pa_id, pa_slug = m.group(1), m.group(2)
        body = open(f, encoding="utf-8", errors="replace").read()
        wids, owners = [], Counter()
        steps_text = []
        for b in re.split(r"(?=^## W\d+[A-Z]?\. )", body, flags=re.M):
            hm = re.match(r"^## (W\d+[A-Z]?)\. ", b)
            if not hm:
                continue
            wid = hm.group(1)
            wids.append(wid)
            all_wids.add(wid)
            om = re.search(r"^\| \*\*Owner\*\* \| (.+?) \|", b, re.M)
            if om:
                owners[om.group(1).strip()] += 1
            steps_text.append(b)
        if not wids:
            continue
        pas.append(dict(vs=vs, pa_id=pa_id, pa_name=humanize(pa_slug),
                        fam=fam_of[vs], wids=wids,
                        owners=owners, text="\n".join(steps_text).lower()))

    # ---- 3. requirement index for Req Ref matching ----
    req_index = []  # (id, lowercase description)
    for line in open(REQS):
        m = re.match(r"^\| ([A-Z]+-\d+[a-z]?) \| (.+?) \| (Must|Should|Nice)", line)
        if m:
            req_index.append((m.group(1), m.group(2).lower()))
    req_ids = {r for r, _ in req_index}
    stop = set("and of for the to in a an with per management system operations operational "
               "process workflow workflows daily monthly store level stores processing "
               "integration monitoring tracking compliance data".split())

    def pick_reqs(pa, fam):
        toks = [t for t in re.split(r"[^a-z0-9]+", pa["pa_name"].lower()) if t and t not in stop]
        best = Counter()
        for rid, desc in req_index:
            score = sum(1 for t in toks if re.search(rf"\b{re.escape(t)}", desc))
            if score:
                best[rid] = score
        picks = [rid for rid, _ in best.most_common(2)]
        fb = FAMILY_FALLBACK_REQ[fam]
        if fb not in picks:
            picks.append(fb)
        return picks[:2]

    # ---- 4. emit one control per PA ----
    next_ctl = 240
    controls = {fam: [] for _, fam in FAMILY_SECTIONS}
    covered = set(existing)
    for pa in sorted(pas, key=lambda p: (p["vs"], p["pa_id"])):
        # closure check: skip only if every workflow already mapped (keeps register honest)
        if all(w in existing for w in pa["wids"]):
            continue
        hits = []
        for pat, phrase in PATTERNS:
            n = len(re.findall(pat, pa["text"]))
            if n:
                hits.append((n, phrase))
        hits.sort(reverse=True)
        total_hits = sum(n for n, _ in hits)
        appr_n = next((n for n, p in hits if p.startswith("approvals")), 0)
        # Preventive when approvals/authorization are a meaningful share of the PA's control
        # fabric (>=15% of pattern hits and >=5 occurrences) — otherwise the PA operating
        # control is detective (verifications/monitoring/reconciliation execution).
        is_p = appr_n >= max(5, 0.15 * total_hits)
        if is_p:
            phrases = [p for _, p in hits if p.startswith("approvals")] + \
                      [p for _, p in hits if not p.startswith("approvals")][:2]
        else:
            phrases = [p for _, p in hits[:3]] or ["standard operating procedures with system-enforced validation"]
        focus = [n for n in NOUNS if re.search(rf"\b{re.escape(n)}s?\b", pa["text"])][:3]
        owner = pa["owners"].most_common(1)[0][0] if pa["owners"] else "Process Owner"
        obj = f"Ensure controlled execution — {pa['pa_name']} ({pa['pa_id']})"
        act = (f"Process-area operating control derived from this PA's workflow steps: "
               + "; ".join(phrases)
               + (f" (recurring objects: {', '.join(focus)})" if focus else "")
               + f"; exceptions escalated to the {owner}; execution evidence retained in the ERP audit trail")
        reqs = pick_reqs(pa, pa["fam"])
        controls[pa["fam"]].append(
            dict(ctl=f"CTL-{next_ctl}", obj=obj, typ="P" if is_p else "D", act=act,
                 owner=owner, wids=sorted(pa["wids"], key=lambda w: int(re.sub(r'[A-Z]', '', w[1:])) ),
                 reqs=reqs, pa_id=pa["pa_id"]))
        next_ctl += 1
        covered.update(pa["wids"])

    # ---- 5. verification ----
    errs = []
    if not all_wids <= covered:
        missing = sorted(all_wids - covered)[:10]
        errs.append(f"closure failed: {len(all_wids - covered)} workflows still unmapped, e.g. {missing}")
    for _, fam in FAMILY_SECTIONS:
        for c in controls[fam]:
            for w in c["wids"]:
                if w not in all_wids:
                    errs.append(f"{c['ctl']}: {w} does not resolve to a ## W header")
            for r in c["reqs"]:
                if r not in req_ids:
                    errs.append(f"{c['ctl']}: req {r} not found")
    if errs:
        print("VERIFICATION FAILED:")
        for e in errs:
            print("  " + e)
        sys.exit(1)

    n_new = next_ctl - 240
    nP = sum(1 for _, f in FAMILY_SECTIONS for c in controls[f] if c["typ"] == "P")
    nD = n_new - nP

    # ---- 6. build the block ----
    L = []
    per_fam = {}
    for cid, fam in FAMILY_SECTIONS:
        items = controls[fam]
        per_fam[fam] = (sum(1 for c in items if c["typ"] == "P"),
                        sum(1 for c in items if c["typ"] == "D"))
        L.append(f"## {cid}. Process-Area Operating Controls — {fam}")
        L.append("")
        L.append("One derived operating control per process area of this family, mapped to every workflow of")
        L.append("that process area. Honest-draft tier: objective, type, owner, and activity are derived from")
        L.append("the PA's own workflow steps (approval / reconciliation / verification / monitoring /")
        L.append("documentation patterns and the PA's recurring domain objects) by")
        L.append("`07-methodology/add-pa-controls.py`, pending per-workflow human review — the same honest-draft")
        L.append("principle as the other generated analysis fields. Injections are performed by")
        L.append("`07-methodology/backfill-controls.py`.")
        L.append("")
        L.append("| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |")
        L.append("|---|---|---|---|---|---|---|")
        for c in items:
            L.append(f"| {c['ctl']} | {c['obj']} | {c['typ']} | {c['act']} | {c['owner']} | {', '.join(c['wids'])} | {', '.join(c['reqs'])} |")
        L.append("")
    block = "\n".join(L)

    if dry:
        sample = [c for _, f in FAMILY_SECTIONS for c in controls[f]][:3]
        for c in sample:
            print(f"{c['ctl']} | {c['obj'][:60]} | {c['typ']} | {c['act'][:120]}... | {c['owner'][:20]} | {len(c['wids'])} wfs | {c['reqs']}")
        print(f"\n{n_new} controls (CTL-240–CTL-{next_ctl-1}; {nP} P / {nD} D); register total {239+n_new}; closure verified")
        return

    # ---- 7. write: insert block + extend summary ----
    anchor = "## Controls Summary by Category"
    assert anchor in txt
    txt = txt.replace(anchor, block + anchor, 1)
    for _, fam in FAMILY_SECTIONS:
        p, d = per_fam[fam]
        label = f"Process-Area Operating — {fam}"
        txt = txt.replace("| **Total** | **57** | **182** | **239** |",
                          f"| {label} | {p} | {d} | {p + d} |\n| **Total** | **57** | **182** | **239** |", 1)
    txt = txt.replace("| **Total** | **57** | **182** | **239** |",
                      f"| **Total** | **{57 + nP}** | **{182 + nD}** | **{239 + n_new}** |", 1)
    open(MATRIX, "w").write(txt)
    print(f"inserted {n_new} PA operating controls (CTL-240–CTL-{next_ctl-1}; {nP} P / {nD} D); "
          f"register total {239 + n_new} ({57 + nP}P/{182 + nD}D); closure verified")


if __name__ == "__main__":
    main()
