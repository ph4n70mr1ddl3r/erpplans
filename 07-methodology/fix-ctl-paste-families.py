#!/usr/bin/env python3
"""fix-ctl-paste-families.py — re-map the 36 paste-family misdirected CTL citations
(batch-26 finding): expansion-era files where every workflow block's Controls section
cites one foreign core control with a per-line fabricated gloss ("- CTL-51: master-data
quality — links to VS-29 / W291; Operational: <Role> sign-off on the workflow output").

Repair per line: the leading "- CTL-NNN: <gloss>" becomes the file's OWN process-area
control in the canonical paren form "- CTL-OWN (ensure controlled execution — <PA name>
(PA-X.Y).)"; a following "Operational:" tail moves to its own "- operational:" line;
a gloss without an Operational tail is preserved as the operational clause (the gloss
carries the workflow-specific sign-off/gate content).
"""
import glob, os, re
from collections import defaultdict, Counter

REPO = "/home/riddler/erpplans/01-model-company"
own = {}
for line in open(f"{REPO}/internal-controls-matrix.md", encoding="utf-8"):
    m = re.match(r"\| (CTL-\d+) \| Ensure controlled execution — (.+?) \((PA-[\d.]+)\) \|", line)
    if m:
        own[m.group(3)] = (m.group(1), m.group(2))

byfile = defaultdict(Counter)
paths = {}
for path in sorted(glob.glob(f"{REPO}/workflows/VS-*/PA-*.md")):
    pa = re.search(r"(PA-[\d.]+)[^/]*\.md$", path).group(1)
    mine = own.get(pa)
    if not mine:
        continue
    for line in open(path, encoding="utf-8"):
        for m in re.finditer(r"- (CTL-\d+): ", line):
            if m.group(1) != mine[0]:
                byfile[(pa, m.group(1))][path] += 1
                paths[path] = pa

paste_pairs = {k for k, v in byfile.items() if sum(v.values()) >= 4}
changed = total = 0
for path, pa in sorted(paths.items()):
    mine = own[pa]
    fams = {ctl for (p, ctl) in paste_pairs if p == pa}
    if not fams:
        continue
    text = open(path, encoding="utf-8").read()
    out = []
    for line in text.split("\n"):
        m = re.match(r"^- (CTL-\d+): (.*)$", line)
        if m and m.group(1) in fams:
            total += 1
            rest = m.group(2)
            om = re.match(r"^(.*?); [Oo]perational: (.*)$", rest)
            if om and om.group(1).strip():
                gloss, tail = om.group(1).strip(), om.group(2).strip()
            elif om:
                gloss, tail = "", om.group(2).strip()
            else:
                gloss, tail = rest.strip(), ""
            canon = f"- {mine[0]} (ensure controlled execution — {mine[1]} ({pa}).)"
            if tail:
                newline = canon + "\n- operational: " + tail
            elif gloss:
                newline = canon + "\n- operational: " + gloss
            else:
                newline = canon
            out.append(newline)
            changed += 1
        else:
            out.append(line)
    open(path, "w", encoding="utf-8").write("\n".join(out))

print(f"paste-family lines re-mapped: {changed} (of {total} candidates)")
