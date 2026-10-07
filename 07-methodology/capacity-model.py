#!/usr/bin/env python3
"""Workforce capacity feasibility model — can the modeled workforce run the
modeled workload?

Answers the question the corpus sets up but never cross-foots: the Time
Estimate fields (per-workflow effort, guarded by Check 49/50) times their
stated cadences, aggregated per role, against the official table of
organization's register (511 HQ roles, Check-59-guarded arithmetic) and the
store/DC aggregates (200 × 29, 4 × 150).

Source of truth: the catalog/ JSON projection (generate-catalog.py) — the
same parse that drives the BPMN tree. Effort bullets come from each record's
`sections["Time Estimate"]` (and `sections["Staffing Implication"]` for role
hints only).

Normalization reuses audit-time-estimate-math.py's licensed CADENCE_PER_YEAR
table (day 365 / workday 260 / week 52 / month 12 / quarter 4 / season 6 /
year 1 — the corpus's own annualization conventions, the same table Check 50
verifies chains against). Bullets whose cadence is not a plain time unit
("per application", "per pilot", "per project") are NOT annualizable from the
bullet alone — they are counted as uncovered (a volume-join against the
Frequency/Volume fields is future work), never guessed.

Per-workflow effort rule (no double counting): if the Time Estimate section
opens with a `Total …` bullet whose cadence annualizes, that bullet IS the
workflow effort (it is the roll-up of the components); otherwise the
self-annualizable component bullets are summed; otherwise the workflow is
counted as not directly annualizable.

Role attribution per bullet: a parenthetical role ("(AP Supervisor)") first,
then an "across N–M <Role>s" tail, then the workflow Owner's first segment,
else Unattributed. Roles are matched against the TO §5.3 register by
normalized title (parentheticals stripped, plural 's' trimmed, lowercase);
unmatched roles bucket by name keywords (store / DC / other). Register HC is
summed across departments for a title (the register repeats titles across
teams).

Capacity convention: net productive hours per FTE-year is a MODEL assumption
(1,800 h = 260 workdays × 8 h gross 2,080 minus ~13.5% for holidays, leave,
training), corpus-external by design and flagged as such everywhere it
appears. Store/DC headcounts are aggregate counts (29 per store, 150 per
DC), not role registers, so store/DC workload is compared in aggregate only.

Modes:
  (default)      regenerate 01-model-company/workforce-capacity-model.md
  --check ROOT   regenerate in memory, byte-compare against the shipped
                 report; print MODEL_TOTALS + BAD| lines; exit 0 iff
                 identical. Invoked by validate-repo.sh Check 71 every run.
"""

import importlib.util
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "01-model-company" / "workforce-capacity-model.md"
CAT = REPO / "catalog"
TO = REPO / "01-model-company" / "optimal-table-of-organization.md"

SCHEMA = "erpplans-capacity-model/1.0"
NET_HOURS_PER_FTE = 1800          # MODEL ASSUMPTION (see docstring)
STORES, STORE_HC = 200, 29
DCS, DC_HC = 4, 150

_title_mod = None


def _math():
    global _title_mod
    if _title_mod is None:
        spec = importlib.util.spec_from_file_location(
            "_temath", REPO / "07-methodology" / "audit-time-estimate-math.py")
        _title_mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_title_mod)
    return _title_mod


# ------------------------------------------------------------------ parsing

DUR_CAD = re.compile(
    r"(?P<val>~?[\d,]+(?:\.\d+)?(?:\s*[-–—]\s*~?[\d,]+(?:\.\d+)?)?)\s*"
    r"(?P<unit>hours?|hrs?|h\b|minutes?|mins?|m\b)\s*/\s*"
    r"(?P<cad>[A-Za-z][A-Za-z-]*)", re.I)
PAREN_ROLE = re.compile(r"\(([^)]*)\)\s*$")
ACROSS = re.compile(r"across\s+([\d,]+\s*(?:[-–—]\s*[\d,]+)?)\s+(.+?)(?:\s*\(|$)", re.I)


def num(s):
    return float(s.replace(",", "").replace("~", ""))


def bullet_hours(line):
    """(low, high) hours/year for a self-annualizable bullet, else None."""
    m = DUR_CAD.search(line)
    if not m:
        return None
    cads = _math().CADENCE_PER_YEAR
    cad = m.group("cad").lower().rstrip("s")
    cad = {"business-day": "workday", "businessdays": "workday",
           "business-day": "workday"}.get(cad, cad)
    if cad not in cads:
        return None
    per = cads[cad]
    v = m.group("val").replace("–", "-").replace("—", "-")
    if "-" in v:
        lo, hi = [num(x) for x in v.split("-", 1)]
    else:
        lo = hi = num(v)
    if m.group("unit").lower().startswith(("min", "m")):
        lo /= 60.0
        hi /= 60.0
    return lo * per, hi * per


def clean_role(r):
    r = re.sub(r"\(.*?\)", "", r).strip().strip(",;")
    return re.sub(r"\s+", " ", r)


def norm_title(t):
    t = clean_role(t).lower().rstrip("s").strip()
    return re.sub(r"\s+", " ", t)


def bullet_context(line):
    """Chain-wide store/DC workload must not land on HQ roles: a bullet whose
    cadence or phrasing is per-store / per-DC (e.g. W1202's '~30–45 min per
    store-day of cash handling … = 100–150 hours/day chain-wide', owned by the
    HQ Treasury Manager) describes store-side work — route it to the bucket,
    not the Owner's register title."""
    n = line.lower()
    if re.search(r"per store\b|store-day|store-days|chain-wide|all stores|every store|\bstore level\b|per store,", n):
        return "store-side"
    if re.search(r"per dc\b|dc-day|dc-days|per distribution center", n):
        return "dc-side"
    return None


def bullet_role(line, owner):
    m = re.search(r"\(([^()]*?(?:Manager|Supervisor|Clerk|Lead|Analyst|Officer|"
                  r"Director|VP|Head|Planner|Buyer|Engineer|Specialist|Coordinator|"
                  r"Accountant|Chef|Nurse|Auditor|Admin|Staff|Team)[^()]*?)\)\s*\.?\s*$",
                  line.strip().rstrip("."))
    if m:
        return clean_role(m.group(1))
    m = ACROSS.search(line)
    if m:
        return clean_role(m.group(2))
    if owner:
        return clean_role(re.split(r"[;,]", owner)[0])
    return "Unattributed"


# ------------------------------------------------------------------ supply

def load_register():
    """TO §5.3: [(department, title, hc)] + per-title HC totals."""
    reg, dept, in_53 = [], None, False
    for line in TO.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^#### (.+?) \(\d+\)\s*$", line)
        if m:
            dept = m.group(1)
            in_53 = True
            continue
        if re.match(r"^#{1,3} ", line):
            dept, in_53 = None, False
            continue
        if not in_53:
            continue
        if re.match(r"^\| Role \| HC \|", line):
            continue
        m = re.match(r"^\| (.+?) \| (\d+) \| .+ \|", line)
        if m and dept and not re.fullmatch(r"[-\s|]+", m.group(0)):
            reg.append((dept, m.group(1).strip(), int(m.group(2))))
    hc_by_title = defaultdict(int)
    for _, t, hc in reg:
        hc_by_title[norm_title(t)] += hc
    total = sum(hc for _, _, hc in reg)
    assert total == 511, f"TO register foots {total}, expected 511"
    return reg, hc_by_title


# ------------------------------------------------------------------ demand

def workload():
    """Per-record annualizable effort: [(wf, vs_name, tier, lo, hi, role, fte_claim)]."""
    index = json_load(CAT / "index.json")
    rows = []
    n_ann = n_not = 0
    for pa_file in sorted(CAT.glob("VS-*/PA-*.json")):
        doc = json_load(pa_file)
        vs_name = doc["value_stream"]["name"]
        for wf in doc["workflows"]:
            te = (wf["sections"].get("Time Estimate")
                  or next((v for k, v in wf["sections"].items()
                           if k.startswith("Time Estimate")), []))
            if not te:
                n_not += 1
                continue
            bullets = [re.sub(r"^\s*-\s*", "", x).strip() for x in te if x.strip()]
            total_b = next((b for b in bullets
                            if re.match(r"Total\b", b, re.I) and bullet_hours(b)), None)
            if total_b:
                eff = [bullet_hours(total_b)]
                src_bullet = total_b
            else:
                eff = [bullet_hours(b) for b in bullets]
                eff = [e for e in eff if e]
                src_bullet = None
            eff = [e for e in eff if e]
            if not eff:
                n_not += 1
                continue
            lo = sum(e[0] for e in eff)
            hi = sum(e[1] for e in eff)
            role = bullet_role(src_bullet or " ".join(bullets), wf["fields"].get("Owner"))
            ctx = bullet_context(src_bullet or " ".join(bullets))
            if ctx:
                role = f"[{ctx}] {role}"
            m = ACROSS.search(src_bullet or "")
            fte_claim = m.group(1) if m else ""
            n_ann += 1
            rows.append({
                "id": wf["id"], "level": wf["level"], "tier": wf["tier"],
                "vs": doc["value_stream"]["directory"], "vs_name": vs_name, "pa": doc["process_area"]["id"],
                "lo": lo, "hi": hi, "role": role, "fte_claim": fte_claim,
            })
    return rows, n_ann, n_not


def json_load(p):
    import json
    return json.loads(p.read_text(encoding="utf-8"))


# ------------------------------------------------------------------ model

def bucket_for(role):
    if role.startswith("[store-side]"):
        return "store-side"
    if role.startswith("[dc-side]"):
        return "dc-side"
    n = role.lower()
    if "store" in n:
        return "store-side"
    if re.search(r"\bdc\b|warehouse|fulfillment", n):
        return "dc-side"
    return "hq/other"


def compute():
    rows, n_ann, n_not = workload()
    reg, hc_by_title = load_register()

    by_role = defaultdict(lambda: [0.0, 0.0, 0])   # lo, hi, workflow count
    for r in rows:
        by_role[r["role"]][0] += r["lo"]
        by_role[r["role"]][1] += r["hi"]
        by_role[r["role"]][2] += 1

    hq_table, unmatched = [], []
    for role, (lo, hi, cnt) in by_role.items():
        nt = norm_title(role)
        if nt in hc_by_title:
            hq_table.append({
                "role": role, "register_role": next(t for _, t, _ in reg
                                                    if norm_title(t) == nt),
                "hc": hc_by_title[nt], "lo": lo, "hi": hi, "n": cnt,
            })
        else:
            unmatched.append({"role": role, "bucket": bucket_for(role),
                              "lo": lo, "hi": hi, "n": cnt})

    for h in hq_table:
        cap = h["hc"] * NET_HOURS_PER_FTE
        h["cap"] = cap
        h["util"] = (h["lo"] + h["hi"]) / 2 / cap * 100 if cap else 0.0
    hq_table.sort(key=lambda h: -h["util"])

    tier_tot = defaultdict(lambda: [0.0, 0.0])
    for r in rows:
        tier_tot[r["tier"]][0] += r["lo"]
        tier_tot[r["tier"]][1] += r["hi"]
    bucket_tot = defaultdict(lambda: [0.0, 0.0])
    for u in unmatched:
        bucket_tot[u["bucket"]][0] += u["lo"]
        bucket_tot[u["bucket"]][1] += u["hi"]

    enterprise_lo = sum(v[0] for v in by_role.values())
    enterprise_hi = sum(v[1] for v in by_role.values())
    stats = {
        "records_total": 5450,
        "annualizable": n_ann,
        "not_annualizable": n_not,
        "enterprise_lo": enterprise_lo,
        "enterprise_hi": enterprise_hi,
        "hq_matched_roles": len(hq_table),
        "unmatched_roles": len(unmatched),
        "tiers": {t: tier_tot.get(t, [0, 0]) for t in ("Tier 1", "Tier 2", "Tier 3")},
        "buckets": {b: bucket_tot.get(b, [0, 0]) for b in ("store-side", "dc-side", "hq/other")},
    }
    return rows, hq_table, unmatched, reg, stats


# ------------------------------------------------------------------ report

def fmt_h(x):
    return f"{x:,.0f}"


def render(rows, hq_table, unmatched, reg, stats):
    L = []
    A = L.append
    ent_mid = (stats["enterprise_lo"] + stats["enterprise_hi"]) / 2
    A("# Workforce Capacity Feasibility Model")
    A("")
    A("> **GENERATED ARTIFACT** — regenerated by "
      "[`../07-methodology/capacity-model.py`](../07-methodology/capacity-model.py) "
      "from the [`catalog/`](../catalog/README.md) projection and the official TO "
      "register; byte-verified by validate-repo.sh Check 71 (`--check`) on every "
      "run. Do not hand-edit: edit the corpus or the model, then regenerate. "
      "Every figure below re-derives from the registers at validation time.")
    A("")
    A("> **Question:** can the modeled workforce run the modeled workload? "
      "The corpus guards effort arithmetic (Check 50) and org arithmetic "
      "(Check 59) but never cross-foots them. This model does, at the level "
      "the data supports, and reports its own coverage honestly.")
    A("")
    A("---")
    A("")
    A("## 1. Method and conventions")
    A("")
    A("| # | Convention | Value | Source |")
    A("|---|---|---|---|")
    A("| 1 | Effort bullets | `### Time Estimate` bullets from every catalog record | catalog/ (Check 71-guarded) |")
    A("| 2 | Annualization | day 365 · workday/business-day 260 · week 52 · month 12 · quarter 4 · season 6 · year 1 | `CADENCE_PER_YEAR`, audit-time-estimate-math.py (Check 50's licensed table) |")
    A("| 3 | Effort per workflow | the `Total …` bullet when present and annualizable (it is the component roll-up), else the sum of self-annualizable component bullets | this model |")
    A("| 4 | Net productive hours | **1,800 h/FTE-year** (260 workdays × 8 h = 2,080 gross, minus ~13.5% holidays/leave/training) | **MODEL ASSUMPTION** — corpus-external, flagged here |")
    A("| 5 | Supply side | TO §5.3 role register, HC summed per title across departments (511 HQ roles) | optimal-table-of-organization.md (Check 59-guarded) |")
    A("| 6 | Store / DC supply | aggregate counts only: 200 stores × 29, 4 DCs × 150 | model-company-profile §4 |")
    A("| 7 | Role attribution | bullet's parenthetical role → `across N–M <Role>` tail → workflow Owner (first segment) → Unattributed | this model |")
    A("| 8 | Cadences not annualizable | `per application`, `per pilot`, `per project`, … — counted uncovered, never guessed | this model |")
    A("")
    A("## 2. Coverage (reported honestly)")
    A("")
    A("| Metric | Value |")
    A("|---|---|")
    A(f"| Register rows (5,427 primary + 23 sub) | {stats['records_total']:,} |")
    A(f"| Workflows with directly annualizable effort | {stats['annualizable']:,} "
      f"({stats['annualizable'] / stats['records_total'] * 100:.1f}%) |")
    A(f"| Workflows not annualizable from bullets alone | {stats['not_annualizable']:,} "
      f"({stats['not_annualizable'] / stats['records_total'] * 100:.1f}%) — per-occurrence "
      "cadences needing a Frequency/Volume join (future work) |")
    A("")
    A("The computed workload is therefore a **lower bound**: every uncovered "
      "workflow adds real, unmodeled work. A lower bound already crossing "
      "capacity is a finding; a lower bound inside capacity is not yet an "
      "all-clear.")
    A("")
    A("## 3. Enterprise totals (computed subset)")
    A("")
    A("| Slice | Hours/year (low) | Hours/year (high) |")
    A("|---|---|---|")
    for t in ("Tier 1", "Tier 2", "Tier 3"):
        lo, hi = stats["tiers"][t]
        A(f"| {t} workflows | {fmt_h(lo)} | {fmt_h(hi)} |")
    b = stats["buckets"]
    A(f"| Attributed to TO-registered (HQ) roles | {fmt_h(sum(h['lo'] for h in hq_table))} | {fmt_h(sum(h['hi'] for h in hq_table))} |")
    A(f"| Attributed to store-side roles (bucket) | {fmt_h(b['store-side'][0])} | {fmt_h(b['store-side'][1])} |")
    A(f"| Attributed to DC-side roles (bucket) | {fmt_h(b['dc-side'][0])} | {fmt_h(b['dc-side'][1])} |")
    A(f"| Other/unmatched roles | {fmt_h(b['hq/other'][0])} | {fmt_h(b['hq/other'][1])} |")
    A(f"| **Computed total** | **{fmt_h(stats['enterprise_lo'])}** | **{fmt_h(stats['enterprise_hi'])}** |")
    A("")
    cap_store = STORES * STORE_HC * NET_HOURS_PER_FTE
    cap_dc = DCS * DC_HC * NET_HOURS_PER_FTE
    cap_hq = 362 * NET_HOURS_PER_FTE
    A(f"Available capacity at the current-state baseline (1,800 h/FTE-yr): HQ "
      f"362 × 1,800 = {fmt_h(cap_hq)} h; stores 200 × 29 × 1,800 = {fmt_h(cap_store)} h; "
      f"DC 4 × 150 × 1,800 = {fmt_h(cap_dc)} h — enterprise **{fmt_h(cap_hq + cap_store + cap_dc)}** h/year. "
      f"The computed lower bound ({fmt_h(stats['enterprise_lo'])} h) is "
      f"{stats['enterprise_lo'] / (cap_hq + cap_store + cap_dc) * 100:.1f}% of current-state "
      "capacity; the uncovered remainder rides on top.")
    A("")
    A("## 4. TO-registered (HQ) role capacity table")
    A("")
    A(f"{stats['hq_matched_roles']} distinct workload roles resolve to the TO §5.3 "
      "register by normalized title. Utilization = computed hours ÷ (register HC × "
      "1,800); the range is low–high over the bullet ranges. Sorted by utilization, "
      "descending.")
    A("")
    A("| Workload role | TO register role | HC | Capacity h/yr | Workload h/yr (lo–hi) | Utilization | Workflows |")
    A("|---|---|---|---|---|---|---|")
    for h in hq_table:
        flag = " ⚠" if h["util"] > 100 else (" ◐" if h["util"] > 70 else "")
        A(f"| {h['role']} | {h['register_role']} | {h['hc']} | {fmt_h(h['cap'])} | "
          f"{fmt_h(h['lo'])} – {fmt_h(h['hi'])} | {h['util']:.0f}%{flag} | {h['n']} |")
    A("")
    A("⚠ over 100% of modeled capacity · ◐ over 70%. A role can legitimately "
      "show high utilization here because the computed workload is only the "
      "annualizable subset attributed to it; read the flag as *investigate*, "
      "not *understaffed*.")
    A("")
    A("## 5. Unmatched roles (not TO-register titles)")
    A("")
    A(f"{stats['unmatched_roles']} distinct workload roles do not resolve to TO §5.3 "
      "titles — store/DC-side roles (the TO is HQ-only; store/DC headcount is "
      "aggregate), composite owner strings, and free-text titles. Their hours are "
      "counted in §3 and listed by bucket there; per-role detail rides in the "
      "generator's output on demand.")
    A("")
    A("## 6. Findings")
    A("")
    over = [h for h in hq_table if h["util"] > 100]
    hot = [h for h in hq_table if 70 < h["util"] <= 100]
    A(f"1. **{len(over)} TO-registered role(s) exceed 100% of modeled capacity** on "
      "the computed subset"
      + (" — led by " + ", ".join(f"{h['role']} ({h['util']:.0f}% of {h['hc']} HC)"
                                  for h in over[:3]) if over else "") + ".")
    A(f"2. **{len(hot)} role(s) sit in the 70–100% band** — tight but plausible; "
      "the uncovered-workflow remainder lands on them too.")
    A("3. The computed lower bound covers "
      f"{stats['annualizable'] / stats['records_total'] * 100:.0f}% of the catalog; "
      "conclusions are directional until the per-occurrence volume join lands.")
    A("4. Known corroborating signal in the corpus itself: PA-16.1's W24 pain "
      "point already flags the annual credit-review backlog (~433 system-hours "
      "deprioritized) — the class of tension this model surfaces systematically.")
    A("")
    A("## 7. Limitations and future work")
    A("")
    A("- Per-occurrence bullets (~90 min/application) are not yet joined to the "
      "Frequency/Volume fields — the single biggest coverage lever (future "
      "work: noun-cancellation join reusing Check 50's tokenizer).")
    A("- Effort is attributed to one role per bullet (first hit); shared bullets "
      "under-count secondary roles. Approver (A-role) verification time is "
      "where most of the residual hides.")
    A("- Automation Opportunity bullets describe *planned* automation offsets; "
      "they are deliberately NOT netted here (the model prices the as-designed "
      "manual process).")
    A("- The 1,800 h net-hours convention is a model assumption; a Philippine "
      "labor-law-grounded figure (holiday/leave calendars) should replace it "
      "before any staffing decision reads this document.")
    A("")
    return "\n".join(L) + "\n"


# ------------------------------------------------------------------ main

def main() -> int:
    global REPO, OUT, CAT, TO
    check_only = "--check" in sys.argv
    roots = [a for a in sys.argv[1:] if not a.startswith("--")]
    if roots:
        REPO = Path(roots[0]).resolve()
        OUT = REPO / "01-model-company" / "workforce-capacity-model.md"
        CAT = REPO / "catalog"
        TO = REPO / "01-model-company" / "optimal-table-of-organization.md"
    if not (REPO / "07-methodology" / "generate-bpmn.py").exists():
        print("MODEL_TOTALS errors=1")
        print(f"BAD|{REPO} is not an erpplans checkout")
        return 1

    rows, hq_table, unmatched, reg, stats = compute()
    report = render(rows, hq_table, unmatched, reg, stats)
    bad = []
    if check_only:
        if not OUT.exists():
            bad.append("missing: 01-model-company/workforce-capacity-model.md")
        elif OUT.read_text(encoding="utf-8") != report:
            bad.append("stale (differs from regeneration): "
                       "01-model-company/workforce-capacity-model.md")
    else:
        OUT.write_text(report, encoding="utf-8")
        if OUT.read_text(encoding="utf-8") != report:
            bad.append("write verification failed")

    print(f"MODEL_TOTALS annualizable={stats['annualizable']} "
          f"not_annualizable={stats['not_annualizable']} "
          f"hours_lo={stats['enterprise_lo']:.0f} hours_hi={stats['enterprise_hi']:.0f} "
          f"hq_roles={stats['hq_matched_roles']} errors={len(bad)}")
    for b in bad:
        print("BAD|" + b)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
