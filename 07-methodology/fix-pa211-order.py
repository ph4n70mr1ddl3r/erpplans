#!/usr/bin/env python3
"""fix-pa211-order.py — batch-27 repair: canonicalize the scrambled section order in
PA-21.1's generation-era blocks (W342–W351, W361–W363, W466 per audit pass 2).

Target order per the corpus convention: header table → Steps → System Touchpoints →
Pain Points / Risks → Automation Opportunity → Controls → (Staffing Implication) →
Time Estimate → (Cross-references). Chunks are moved verbatim; a block's section set
is asserted identical before/after.
"""
import re

P = "/home/riddler/erpplans/01-model-company/workflows/VS-21-internal-audit-risk/PA-21.1-audit-planning-and-execution.md"
AFFECTED = {"W342","W343","W345","W347","W349","W350","W351","W361","W362","W363","W466"}
ORDER = ["### Steps", "### System Touchpoints", "### Pain Points / Risks", "### Automation Opportunity",
         "### Controls", "### Staffing Implication", "### Time Estimate", "### Cross-references"]

text = open(P, encoding="utf-8").read()
lines = text.split("\n")
out, i, fixed = [], 0, []
while i < len(lines):
    m = re.match(r"^## (W\d+)\.", lines[i])
    if m and m.group(1) in AFFECTED:
        j = i + 1
        while j < len(lines) and not lines[j].startswith("## "):
            j += 1
        block = lines[i:j]
        # split into head (up to first ###) + sections
        k = next((x for x, l in enumerate(block) if l.startswith("### ")), len(block))
        head, rest = block[:k], block[k:]
        secs = {}
        cur = None
        for l in rest:
            if l.startswith("### "):
                cur = l.strip()
                secs[cur] = []
            elif cur is not None:
                secs[cur].append(l)
        names = list(secs)
        target = [n for n in ORDER if n in secs]
        reordered = list(head)
        for n in target:
            chunk = [n] + secs[n]
            while chunk and chunk[-1] == "":
                chunk.pop()
            reordered += chunk + [""]
        while reordered and reordered[-1] == "":
            reordered.pop()
        assert sorted(names) == sorted(target), (m.group(1), names, target)
        if block != reordered:
            fixed.append(m.group(1))
        out += reordered + [""]
        i = j
    else:
        out.append(lines[i]); i += 1

open(P, "w", encoding="utf-8").write("\n".join(out))
print("blocks reordered:", fixed)
