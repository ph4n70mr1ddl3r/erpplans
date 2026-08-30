#!/usr/bin/env python3
"""classify-isolated-ctl.py — classify the remaining isolated colon-form CTL citations
(batch-26 worklist item B). For each '- CTL-NNN: <gloss>' line citing a control that is
NOT the file's own PA control, score the gloss against the cited control's real matrix
description (content-token overlap). High overlap => deliberate cross-reference
(legitimate); low overlap => fabricated gloss (misdirected paste artifact).

Read-only: prints a classification table for the repair pass; changes nothing.
"""
import glob, os, re
from collections import Counter

REPO = "/home/riddler/erpplans/01-model-company"
STOP = set("the a an and or of to for in on with by ensure ensure controlled execution "
           "process area operating control derived from this pa s workflow steps routine "
           "verifications inspections documented outcomes exception monitoring alert "
           "handling escalation approvals enforced per authorization matrix recurring "
           "objects inventory pricing payment exceptions escalated evidence retained erp "
           "audit trail management review approval gate operational is are be".split())

own, defn = {}, {}
for line in open(f"{REPO}/internal-controls-matrix.md", encoding="utf-8"):
    m = re.match(r"\| (CTL-\d+) \| (.+?) \| [DP] \|", line)
    if m:
        defn[m.group(1)] = m.group(2)
    m = re.match(r"\| (CTL-\d+) \| Ensure controlled execution — (.+?) \((PA-[\d.]+)\) \|", line)
    if m:
        own[m.group(3)] = m.group(1)

def toks(s):
    return {w for w in re.findall(r"[a-z]{3,}", s.lower()) if w not in STOP}

rows = []
for path in sorted(glob.glob(f"{REPO}/workflows/VS-*/PA-*.md")):
    pa = re.search(r"(PA-[\d.]+)[^/]*\.md$", path).group(1)
    mine = own.get(pa)
    for i, line in enumerate(open(path, encoding="utf-8"), 1):
        m = re.match(r"^- (CTL-\d+): (.*)$", line)
        if not m or (mine and m.group(1) == mine):
            continue
        cited, gloss = m.group(1), m.group(2)
        dt = toks(defn.get(cited, ""))
        gt = toks(gloss)
        overlap = len(dt & gt) / max(1, min(len(dt), len(gt))) if dt and gt else 0
        rows.append((overlap, pa, cited, os.path.relpath(path, REPO), i, gloss[:90]))

rows.sort()
fab = [r for r in rows if r[0] < 0.15]
mid = [r for r in rows if 0.15 <= r[0] < 0.40]
leg = [r for r in rows if r[0] >= 0.40]
print(f"total isolated: {len(rows)}  fabricated(<0.15): {len(fab)}  uncertain(0.15-0.40): {len(mid)}  deliberate(>=0.40): {len(leg)}")
print("\n== FABRICATED (candidates for own-PA re-map) ==")
for r in fab:
    print(f"  {r[1]} {r[2]} {r[3].split('/')[-1][:40]} L{r[4]} :: {r[5]}")
print("\n== UNCERTAIN (need hand read) ==")
c = Counter((r[2]) for r in mid)
print("  by control:", dict(c.most_common()))
for r in mid[:25]:
    print(f"  {r[1]} {r[2]} {r[3].split('/')[-1][:40]} L{r[4]} :: {r[5]}")
