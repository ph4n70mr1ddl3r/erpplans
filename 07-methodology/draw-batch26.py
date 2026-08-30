#!/usr/bin/env python3
"""draw-batch26.py — draw the batch-26 semantic-audit sample (consistency review #72).

Stratified draw mirroring the prior batches (#67-#71): 104 workflows,
13 per value-stream family (8 families), expansion-weighted within family
(slots allocated to value streams proportional to their UNAUDITED workflow
counts, largest-remainder), seed 7070, excluding the 2,657 W-ids already in
semantic-audit-coverage.txt.

Outputs the drawn W-ids grouped by family with their owning PA file paths.
"""
import glob, os, re, random
from collections import defaultdict

REPO = "/home/riddler/erpplans"
WF = os.path.join(REPO, "01-model-company", "workflows")
README = os.path.join(WF, "README.md")
COV = os.path.join(REPO, "07-methodology", "semantic-audit-coverage.txt")

SEED = 7070
PER_FAMILY = 13

# --- families: parse the 8 '### <Family> (N workflows)' sections from the README
fam_of_vs = {}          # vsnum -> family name
vs_slug = {}            # vsnum -> folder slug
cur = None
for line in open(README, encoding="utf-8"):
    m = re.match(r"^### (.+?) \(", line)
    if m:
        cur = m.group(1)
        continue
    m = re.match(r"^\| \[VS-(\d+)\]\((VS-\d+-[^/]+)/README\.md\) \|", line)
    if m and cur:
        fam_of_vs[int(m.group(1))] = cur
        vs_slug[int(m.group(1))] = m.group(2)

# --- audited W-ids to exclude
audited = set()
for line in open(COV, encoding="utf-8"):
    line = line.strip()
    if re.fullmatch(r"W\d+[A-Z]?", line):
        audited.add(line)

# --- harvest all W-ids from PA files (h2 '## W<num>' workflow blocks)
wid_pa = {}             # wid -> PA file path
wid_vs = {}             # wid -> vsnum
for path in sorted(glob.glob(os.path.join(WF, "VS-*", "PA-*.md"))):
    vm = re.search(r"/(VS-(\d+))-[^/]+/PA-", path)
    vsnum = int(vm.group(2))
    for m in re.finditer(r"^## (W\d+[A-Z]?)\b", open(path, encoding="utf-8").read(), re.M):
        wid = m.group(1)
        # a few W-ids appear in multiple PAs historically; first hit wins (registry convention)
        if wid not in wid_pa:
            wid_pa[wid] = path
            wid_vs[wid] = vsnum

# --- unaudited pool per family, split per VS (expansion weighting = proportional
#     to per-VS unaudited counts, largest-remainder over 13 slots)
fam_pool = defaultdict(lambda: defaultdict(list))   # family -> vsnum -> [wids]
for wid, vsnum in wid_vs.items():
    if wid in audited or wid not in wid_pa:
        continue
    fam = fam_of_vs.get(vsnum)
    if fam:
        fam_pool[fam][vsnum].append(wid)

rng = random.Random(SEED)
drawn = []
for fam in sorted(fam_pool):
    vs_counts = {vs: len(ws) for vs, ws in fam_pool[fam].items()}
    total = sum(vs_counts.values())
    # proportional allocation, largest remainder
    raw = {vs: PER_FAMILY * c / total for vs, c in vs_counts.items()}
    alloc = {vs: int(x) for vs, x in raw.items()}
    while sum(alloc.values()) < PER_FAMILY:
        vs = max(raw, key=lambda v: raw[v] - alloc[v])
        alloc[vs] += 1
    fam_drawn = []
    for vs in sorted(alloc):
        pool = sorted(fam_pool[fam][vs])
        k = min(alloc[vs], len(pool))
        fam_drawn += rng.sample(pool, k)
    fam_drawn.sort(key=lambda w: (wid_vs[w], int(re.sub(r"\D", "", w)), w))
    drawn.append((fam, fam_drawn))

print(f"Total W-ids in PAs: {len(wid_pa)}; audited: {len(audited)}; "
      f"unaudited pool: {len(wid_pa) - len(audited & set(wid_pa))}")
n = 0
for fam, ws in drawn:
    n += len(ws)
    print(f"\n== {fam} ({len(ws)}) ==")
    for w in ws:
        rel = os.path.relpath(wid_pa[w], REPO)
        print(f"{w}\tVS-{wid_vs[w]}\t{rel}")
print(f"\nTOTAL DRAWN: {n}")
