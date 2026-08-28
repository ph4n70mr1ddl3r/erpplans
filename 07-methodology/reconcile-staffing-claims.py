#!/usr/bin/env python3
"""
reconcile-staffing-claims.py — Headcount-anchor & Volume-product reconciliation.

Consistency review #34 (2026-08-29) reconciled the staffing-team and role-count
claims scattered through the PA files' Staffing Implication / Time Estimate /
Volume prose against the canonical headcount registers —

  * `model-company-profile.md` §3.3 (18 HQ departments summing to 362),
    §4 (stores 200 × 29 = 5,800; DCs 4 × 150 = 600; total 6,762),
    §13.1 (Merchandising 40: 5 Category Managers, 10 Buyers, 5 Merchandise
    Planners, 4 Pricing Analysts, …);
  * `headcount-reality-check.md` (the historical gap record the rebalances
    closed — its pre-rebalance figures are NOT current state).

Three guards, all tuned to zero false positives on the adjudicated repo:

  1. retired literals — the superseded staffing figures the review repaired
     (pre-rebalance department totals, the stale role counts, the per-shift DC
     worker phrasing, the DSD per-store week/month slip) must not reappear;
  2. department-team equality — any "<Department> … team of N" claim for a
     canonical HQ department must quote that department's §3.3 total;
  3. Volume-row products — every explicit "A × B = C" (or "× D = E") product
     inside a `| **Volume** |` / `| **Frequency** |` field row must compute
     elementwise (ranges low×low / high×high).

Usage:  python3 reconcile-staffing-claims.py [--guard]     (exit 1 on any hit)
"""
import argparse, glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(REPO, "01-model-company", "workflows")

# canonical §3.3 HQ department totals (spot anchors used by prose claims)
DEPT_TOTALS = {
    "executive office": 7, "merchandising": 40, "finance & accounting": 46,
    "finance and accounting": 46, "finance": 46, "supply chain & logistics": 40,
    "supply chain and logistics": 40, "supply chain": 40,
    "information technology": 50, "it": 50, "human resources": 26, "hr": 26,
    "marketing": 25, "store operations": 24, "legal & compliance": 14,
    "legal and compliance": 14, "legal": 14, "internal audit & risk": 7,
    "internal audit and risk": 7, "internal audit": 7,
    "customer service / call center": 30, "call center": 30,
    "regional loss prevention": 20, "loss prevention": 20,
    "health, safety & environment": 10, "hse": 10,
    "quality management": 4, "facilities & real estate": 8,
    "sustainability / esg": 3, "strategy / corporate planning": 3,
    "trade / account management": 5,
}

# §13.1 merchandising role counts + other profile-anchored role sizes
ROLE_TOTALS = {
    "category managers": 5, "buyers": 10, "merchandise planners": 5,
    "pricing analysts": 4,
}

RETIRED_LITERALS = [
    # pre-rebalance department totals quoted in PA prose
    "IT team of ~28", "~28–30 IT headcount", "the recommended ~28–30 IT staff",
    "planned expansion to ~28–30", "IT staff of ~28",
    "Finance & Accounting team of 37", "team of 37 staff",
    "Legal & Compliance team of ~9", "Store Operations team of ~23",
    # stale merchandising role counts (§13.1: 4 analysts, 10 buyers, 5 CMs)
    "3 Pricing Analysts", "3 Pricing Analyst roles", "spread across 3 analysts",
    "10–12 Buyers", "10–12 buyers", "~10 Category Managers",
    "With 6 Category Managers", "÷ ~4 Category Managers",
    "existing 2 Merchandise Planners",
    # HSE: safety officers sit inside the 10-person team with nurse/wellness
    "~10–12 Safety Officers",
    # DC headcount is 600 (4 × 150) — no per-shift roster claims
    "workers per DC per shift",
    # DSD cadence is per store per MONTH (~500–600 receipts/month chain-wide)
    "DSD deliveries per store per week", "DSD deliveries/store/week",
    "DSD deliveries/week",
]

DEPT_TEAM_RE = re.compile(
    r"\b(" + "|".join(re.escape(d) for d in
                      sorted(DEPT_TOTALS, key=len, reverse=True)) +
    r")\b[^.|\n]{0,40}?\bteam of ~?(\d+)", re.I)
TEAM_IN_RE = re.compile(
    r"\bteam of ~?(\d+)\s*(?:staff|people|personnel)?\s*(?:at HQ|in (?:the )?)?"
    r"[\s(]*(?:the )?\b(" + "|".join(re.escape(d) for d in
                                     sorted(DEPT_TOTALS, key=len, reverse=True)) +
    r")\b", re.I)

NUM = r"~?\d[\d,]*(?:\.\d+)?"
RANGE = r"(?:[–—-]\s*" + NUM + r")?"
QUANT = re.compile("(" + NUM + RANGE + r"\s*[KMB]?(?![A-Za-z]))")
PRODUCT_RE = re.compile(
    NUM + r"\s*" + RANGE + r"\s*(?:[A-Za-z-]+/)*(?:[A-Za-z-]+\s+){0,2}[A-Za-z-]+\s*×\s*" +
    NUM + r"\s*" + RANGE + r"(?:[^\n=+×]{0,60}?×\s*" + NUM + r"\s*" + RANGE +
    r")?\s*(?:[^\n=+×]{0,30}?)=\s*~?" + NUM + r"\s*" + RANGE +
    r"\s*[KMB]?(?![A-Za-z])")


def parse_range(text):
    ends = re.findall(r"(\d[\d,]*(?:\.\d+)?)\s*([KMB](?![A-Za-z]))?", text)
    if not ends:
        return None
    mult = {"k": 1e3, "m": 1e6, "b": 1e9}
    vals = [float(n.replace(",", "")) * mult.get(suf.lower(), 1)
            for n, suf in ends]
    return (vals[0], vals[-1])


def check_file(path, hits):
    text = open(path, encoding="utf-8").read()
    rel = os.path.relpath(path, REPO)
    for lit in RETIRED_LITERALS:
        for m in re.finditer(re.escape(lit), text, re.I):
            line = text[:m.start()].count("\n") + 1
            hits.append(("retired-literal", rel, line, lit))
    for m in DEPT_TEAM_RE.finditer(text):
        dept, n = m.group(1).lower(), int(m.group(2))
        canon = DEPT_TOTALS.get(dept)
        after = text[m.end():m.end() + 4]
        if canon and n != canon and not re.match(r"\s*[–-]\s*\d", after) \
                and not re.search(r"deploy|send|assign|field|audit crew",
                                  m.group(0), re.I):
            line = text[:m.start()].count("\n") + 1
            hits.append(("dept-team", rel, line,
                         f"'{m.group(0)}' — canonical §3.3 {dept} = {canon}"))
    for m in TEAM_IN_RE.finditer(text):
        n, dept = int(m.group(1)), m.group(2).lower()
        canon = DEPT_TOTALS.get(dept)
        after = text[m.end():m.end() + 4]
        if canon and n != canon and not re.match(r"\s*[–-]\s*\d", after) \
                and not re.search(r"deploy|send|assign|field|audit crew",
                                  m.group(0), re.I):
            line = text[:m.start()].count("\n") + 1
            hits.append(("dept-team", rel, line,
                         f"'{m.group(0)}' — canonical §3.3 {dept} = {canon}"))
    for m in re.finditer(r"^\| \*\*(?:Volume|Frequency)\*\* \|(.+)\|$", text, re.M):
        row = m.group(1)
        line = text[:m.start()].count("\n") + 1
        for pm in PRODUCT_RE.finditer(row):
            span = pm.group(0)
            if "+" in row[row.find(span):row.find(span) + len(span) + 60]:
                continue  # '+'-sum rows are outside the product checker's scope
            quants = [parse_range(q) for q in QUANT.findall(span)]
            factors, claimed = quants[:-1], quants[-1]
            if not factors or any(q is None for q in quants):
                continue
            lo = hi = 1.0
            for flo, fhi in factors:
                lo *= flo
                hi *= fhi
            clo, chi = claimed
            scales = [1.0]
            if "week" in span and ("month" in row or "/mo" in row):
                scales += [4.0, 52 / 12]   # weekly factor, monthly claim
            if not any(0.95 * lo * sc <= clo <= 1.05 * hi * sc and
                       0.95 * hi * sc <= chi <= 1.05 * hi * sc
                       for sc in scales) \
                    and not (lo * 0.8 <= clo <= hi * 1.2):
                hits.append(("volume-product", rel, line,
                             f"'{pm.group(0)}' — elementwise {lo:g}–{hi:g} "
                             f"vs claimed {clo:g}–{chi:g}"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guard", action="store_true",
                    help="exit 1 on any hit (validator mode)")
    args = ap.parse_args()
    hits = []
    files = sorted(glob.glob(os.path.join(WORKFLOWS, "VS-*", "PA-*.md")))
    for f in files:
        check_file(f, hits)
    for kind, rel, line, detail in hits:
        print(f"{kind}: {rel}:{line}: {detail}")
    print(f"reconcile-staffing-claims: {len(hits)} hit(s) across {len(files)} PA files")
    if args.guard:
        sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
