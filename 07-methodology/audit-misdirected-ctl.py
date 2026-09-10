#!/usr/bin/env python3
"""audit-misdirected-ctl.py — measure (and, with --guard, enforce) the
misdirected-CTL-citation family.

A PA file's Controls section may cite its OWN process-area control (the matrix row
whose name carries "(PA-X.Y)"), and may legitimately cross-reference specific core
controls by full canonical form. The expansion-era generator instead pasted
"- CTL-NNN: <fragment>; Operational: <Role> sign-off on the workflow output"
using random core-control numbers (CTL-51, CTL-13, CTL-09, CTL-21, ...). This
script maps every PA file to its own control and reports every colon-form
citation of a different control number, plus parenthetical-form citations whose
named PA differs from the file's PA.

Guard mode (2026-09-10, eighteenth consistency review): the paste-family class was
re-mapped in batches 26/27 (195 lines across 38 PA files + 11 composites) and the
residual isolated colon-form population was hand-adjudicated citation-by-citation
at batch 13 (2026-09-04, recorded in CHANGELOG and the gap-analysis batch note):
all 170 remaining citations read as verbatim-objective restatements or
definition-matched paraphrases of the cited control — deliberate cross-references.
The guard re-derives the census every run and enforces (a) zero paren-form
citations naming a different PA (the unambiguous wrong-PA defect class), and
(b) the adjudicated colon-form population — total, per-PA and per-cited-CTL
distributions — unchanged, so any new paste, re-map, or deletion fires and forces
a conscious re-adjudication with this baseline re-pointed (the Check-74
deferred-anchor pattern). Report mode (no flag) is unchanged.
"""
import glob, os, re, sys
from collections import Counter

REPO = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "01-model-company")
MATRIX = os.path.join(REPO, "internal-controls-matrix.md")

# own-control per PA id, from matrix rows "CTL-NNN | ... (PA-X.Y) | ..."
own = {}
for line in open(MATRIX, encoding="utf-8"):
    m = re.match(r"\| (CTL-\d+) \| Ensure controlled execution — (.+?) \((PA-[\d.]+)\) \|", line)
    if m:
        own[m.group(3)] = (m.group(1), m.group(2))

colon_hits = []
paren_hits = []
for path in sorted(glob.glob(os.path.join(REPO, "workflows", "VS-*", "PA-*.md"))):
    pa_id = re.search(r"(PA-[\d.]+)[^/]*\.md$", path).group(1)
    mine = own.get(pa_id)
    for i, line in enumerate(open(path, encoding="utf-8"), 1):
        for m in re.finditer(r"- (CTL-\d+): ", line):
            if not mine or m.group(1) != mine[0]:
                colon_hits.append((pa_id, m.group(1), os.path.relpath(path, REPO), i,
                                   line.strip()[:120]))
        for m in re.finditer(r"- (CTL-\d+) \(ensure controlled execution — .+?\((PA-[\d.]+)\)\.\)", line):
            if m.group(2) != pa_id:
                paren_hits.append((pa_id, m.group(1), m.group(2),
                                   os.path.relpath(path, REPO), i))

# ---- guard baseline (see docstring). Derived 2026-09-10 from the corpus;
# ---- re-point ONLY after a hand-adjudicated citation change.
ADJUDICATED_TOTAL = 170
ADJUDICATED_BY_PA = {
    "PA-53.1": 4, "PA-55.2": 2, "PA-55.3": 2, "PA-56.1": 1, "PA-56.2": 1,
    "PA-56.3": 1, "PA-57.3": 1, "PA-58.1": 2, "PA-59.1": 2, "PA-59.2": 2,
    "PA-59.3": 2, "PA-60.2": 1, "PA-60.3": 1, "PA-61.2": 1, "PA-62.1": 5,
    "PA-62.2": 3, "PA-62.3": 1, "PA-64.1": 3, "PA-64.2": 1, "PA-64.3": 1,
    "PA-66.2": 1, "PA-67.1": 4, "PA-67.2": 5, "PA-67.3": 4, "PA-68.2": 2,
    "PA-72.1": 1, "PA-72.2": 1, "PA-72.3": 1, "PA-73.1": 3, "PA-73.2": 1,
    "PA-73.3": 1, "PA-76.1": 5, "PA-76.2": 2, "PA-77.1": 1, "PA-77.2": 1,
    "PA-78.1": 1, "PA-78.2": 2, "PA-182.1": 2, "PA-182.2": 8, "PA-182.3": 7,
    "PA-183.1": 3, "PA-183.2": 2, "PA-183.3": 5, "PA-184.1": 6, "PA-184.2": 4,
    "PA-184.3": 6, "PA-185.2": 5, "PA-186.1": 7, "PA-186.2": 8, "PA-186.3": 6,
    "PA-187.1": 6, "PA-187.2": 3, "PA-187.3": 2, "PA-188.1": 1, "PA-188.2": 3,
    "PA-188.3": 2, "PA-189.1": 4, "PA-189.3": 2, "PA-190.2": 2, "PA-190.3": 1,
    "PA-191.3": 2,
}
ADJUDICATED_BY_CTL = {
    "CTL-01": 2, "CTL-02": 2, "CTL-05": 2, "CTL-06": 13, "CTL-07": 1,
    "CTL-12": 4, "CTL-13": 2, "CTL-14": 3, "CTL-15": 4, "CTL-19": 4,
    "CTL-20": 6, "CTL-21": 4, "CTL-22": 1, "CTL-23": 2, "CTL-24": 4,
    "CTL-25": 4, "CTL-26": 5, "CTL-27": 3, "CTL-28": 1, "CTL-29": 1,
    "CTL-30": 3, "CTL-31": 4, "CTL-32": 1, "CTL-34": 4, "CTL-35": 2,
    "CTL-37": 6, "CTL-39": 10, "CTL-41": 12, "CTL-42": 1, "CTL-44": 1,
    "CTL-48": 5, "CTL-50": 2, "CTL-51": 10, "CTL-100": 1, "CTL-104": 7,
    "CTL-109": 1, "CTL-151": 3, "CTL-153": 2, "CTL-159": 1, "CTL-171": 1,
    "CTL-176": 1, "CTL-178": 1, "CTL-179": 4, "CTL-185": 1, "CTL-195": 1,
    "CTL-197": 1, "CTL-198": 4, "CTL-208": 1, "CTL-212": 2, "CTL-213": 1,
    "CTL-219": 3, "CTL-227": 1, "CTL-311": 1, "CTL-349": 3,
}

def _diff(label, got, want):
    bad = []
    for k in sorted(set(got) | set(want)):
        g, w = got.get(k, 0), want.get(k, 0)
        if g != w:
            bad.append(f"  {label} {k}: live {g} vs adjudicated {w}")
    return bad

def run_guard():
    violations = []
    if paren_hits:
        violations.append(f"paren-form citations naming a different PA: {len(paren_hits)} "
                          f"(the unambiguous wrong-PA defect class; re-map to the file's own control)")
        for h in paren_hits[:10]:
            violations.append(f"  {h[0]} cites {h[1]} but names {h[2]} ({h[3]} L{h[4]})")
    if len(colon_hits) != ADJUDICATED_TOTAL:
        violations.append(f"colon-form non-own census: live {len(colon_hits)} vs adjudicated "
                          f"{ADJUDICATED_TOTAL} (batch-13 hand-adjudicated population changed — "
                          f"re-adjudicate and re-point the baseline)")
    violations += _diff("PA", Counter(h[0] for h in colon_hits), ADJUDICATED_BY_PA)
    violations += _diff("CTL", Counter(h[1] for h in colon_hits), ADJUDICATED_BY_CTL)
    if violations:
        print("MISDIRECTED-CTL GUARD VIOLATIONS:")
        for v in violations:
            print(v)
        raise SystemExit(1)
    print(f"misdirected-ctl guard clean: 0 wrong-PA paren citations; colon-form census "
          f"{len(colon_hits)} == adjudicated baseline (per-PA and per-CTL distributions exact)")
    raise SystemExit(0)

if "--guard" in sys.argv:
    run_guard()

print(f"PA files: {len(glob.glob(os.path.join(REPO, 'workflows', 'VS-*', 'PA-*.md')))}; "
      f"PAs with own control: {len(own)}")
print(f"\ncolon-form citations of non-own controls: {len(colon_hits)}")
c = Counter(h[1] for h in colon_hits)
print("by control:", dict(c.most_common(15)))
c2 = Counter(h[0] for h in colon_hits)
print("by PA (top):", dict(c2.most_common(15)))
print("\nparen-form citations naming a different PA:", len(paren_hits))
for h in paren_hits[:15]:
    print("  ", h)
print("\nsample colon hits:")
for h in colon_hits[:12]:
    print("  ", h[0], h[1], h[2].split('/')[-1][:44], f"L{h[3]}", h[4][:80])
