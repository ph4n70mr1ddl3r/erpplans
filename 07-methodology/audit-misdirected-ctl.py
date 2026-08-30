#!/usr/bin/env python3
"""audit-misdirected-ctl.py — measure the misdirected-CTL-citation family.

A PA file's Controls section may cite its OWN process-area control (the matrix row
whose name carries "(PA-X.Y)"), and may legitimately cross-reference specific core
controls by full canonical form. The expansion-era generator instead pasted
"- CTL-NNN: <fragment>; Operational: <Role> sign-off on the workflow output"
using random core-control numbers (CTL-51, CTL-13, CTL-09, CTL-21, ...). This
script maps every PA file to its own control and reports every colon-form
citation of a different control number, plus parenthetical-form citations whose
named PA differs from the file's PA.
"""
import glob, os, re
from collections import Counter

REPO = "/home/riddler/erpplans/01-model-company"
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
