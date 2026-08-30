#!/usr/bin/env python3
"""fix-ghost-roles-batch26.py — batch-26 ghost-role adjudication sweep (consistency
review #72), extending the batch-24 precedent (uncharted executive-title families
unified on charted/majority owners per profile §11.1/§3.3/§13.1).

Families and targets (each measured corpus-wide before the sweep):
  1. "VP Finance"   (~148) -> CFO        — the finance-exec seat: the corpus's own
       approval ladders ("≤PHP 500K Finance Controller, ≤PHP 5M Finance VP, >PHP 5M
       CEO" INS-008/CCR-001; "PHP 500K–5M: Finance VP approves" PA-26.3) seat Finance
       VP between the Controller and the CEO, which is exactly the CFO's seat in
       §11.1's closed 7-exec chart; no VP Finance is charted in any register.
  2. "Finance VP"   (~71)  -> CFO        — inverted form of the same seat.
  3. "Finance Director" (~100) -> Finance Controller — the §3.3 Finance & Accounting
       department head ("Controller"); "Finance Controller" is the 478-use corpus
       majority form. EXCLUDES "Developer Finance Director" (external party, PA-181.2).
  4. "VP HR"        (~42)  -> CHRO       — §11.1 charts the CHRO over HR.
  5. "VP Internal Audit" (~31) -> Head of Internal Audit — the batch-24 target for
       this department (CRO/CAE/Internal Audit Director already unified there).
  6. "Merchandising VP" (~14) -> VP Merchandising — §13.1 majority form (1,614 uses).
  7. "Marketing VP" (3) -> VP Marketing; 8. "Supply Chain VP" (3) -> VP Supply Chain;
     9. "HR VP" (1) -> CHRO — inverted variants of charted majority forms.
 10. "Regional Ops Director" (9) -> Regional Manager — the charted field layer
       (~6, §12.1); PA-26.2's own step text already says "COO or Regional Manager".
 11. "Store Ops Dir" (16) -> VP Store Operations — the retired Store-Ops-Director
       family's abbreviation form (batch-24 decision).
 12. "Supply Chain Mgr" (8) -> VP Supply Chain — approval/escalation A-columns
       (DC-expansion trigger, emergency rerouting, ROP policy) = the department-head
       seat charted at profile §3.3 (VP Supply Chain, reports to COO).

Post-sweep hand-trues (same-cell CFO duplications and ladder collapses) are listed
in the batch-26 notes and applied separately.
"""
import glob, os, re

REPO = "/home/riddler/erpplans/01-model-company"

RULES = [
    (re.compile(r"\bVP Finance\b"), "CFO"),
    (re.compile(r"\bFinance VP\b"), "CFO"),
    (re.compile(r"(?<!Developer )\bFinance Director\b"), "Finance Controller"),
    (re.compile(r"\bVP HR\b"), "CHRO"),
    (re.compile(r"\bVP Internal Audit\b"), "Head of Internal Audit"),
    (re.compile(r"\bMerchandising VP\b"), "VP Merchandising"),
    (re.compile(r"\bMarketing VP\b"), "VP Marketing"),
    (re.compile(r"\bSupply Chain VP\b"), "VP Supply Chain"),
    (re.compile(r"\bHR VP\b"), "CHRO"),
    (re.compile(r"\bRegional Ops Director\b"), "Regional Manager"),
    (re.compile(r"\bStore Ops Dir\b"), "VP Store Operations"),
    (re.compile(r"\bSupply Chain Mgr\b"), "VP Supply Chain"),
]

total = 0
per_rule = {r.pattern: 0 for r, _ in RULES}
for path in sorted(glob.glob(os.path.join(REPO, "**", "*.md"), recursive=True)):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    orig = text
    for rx, rep in RULES:
        text, n = rx.subn(rep, text)
        per_rule[rx.pattern] += n
    if text != orig:
        total += sum(1 for a, b in zip(orig.splitlines(), text.splitlines()) if a != b)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)

print(f"lines changed: {total}")
for rx, n in per_rule.items():
    print(f"{n:5d}  {rx.pattern}")
