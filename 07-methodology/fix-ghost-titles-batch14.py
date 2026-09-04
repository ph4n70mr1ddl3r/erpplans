#!/usr/bin/env python3
"""fix-ghost-titles-batch14.py — batch-14 ghost-title charter sweep (item A closure).

Closes the last open family on the batch-26 worklist (batch23-deferred-candidates.txt
item A): uncharted executive/director titles cited in workflow Owner/Participants/step
cells, unified on charted seats per the adopted target-state TO (§3/§3.1/§5.2) and the
corpus's own majority forms (the batch-24/batch-26 precedent). Each target passes the
two-sided test: the title is charted (or is the corpus's charted-seat short form) AND
its remit covers the ghost title's subject.

Families and targets (each measured corpus-wide before the sweep):

  1. "VP Innovation & Digital Transformation" (~2) + "VP Innovation" (~21) -> CIO
       — no innovation seat is charted; VS-30 (Innovation & Digital) is a Technology &
       Data-family VS carried by the CIO's platform estate (AAP/SEP; TO §3 chart), so
       the innovation-program seat is the CIO.
  2. "VP Sales & Trade Operations" (1) + "VP Sales" (~112) + "Sales Director" (~35) +
     "Commercial Director" (~27) -> Head of Trade / Account Management
       — the charted trade-sales seat (TO §3.1 COO org: "Head of Trade / Account
       Management — key accounts · trade professional program"; 7-HC Trade/Acct Mgmt
       sub-team §5.2). All four ghost forms sit in trade/B2B sales contexts (VS-01/09/
       11/13/28/66/107/139/140/185).
  3. "VP Govt Affairs" (~31) -> Government Affairs Manager
       — the corpus's 33-use form for the charted Regulatory & Government Affairs
       sub-team lead (TO §5.2, 4 HC under VP Legal & Compliance).
  4. "VP Ecommerce" (~26) + "VP Digital Commerce" (~14) + "Ecommerce Director" (~42) +
     "VP Omnichannel" (~15) -> GM, Digital Commerce Inc.
       — the charted ecommerce seat (TO §3: "GM, Digital Commerce Inc. — dotted" under
       CMO; IT model CCP partner "Digital Commerce Inc. GM"). The omnichannel ghost
       forms sit in VS-10/60/93/95/164 ecommerce-channel contexts.
  5. "VP Customer Experience" (~14) -> Head of Customer Service
       — the charted Customer Service department head (TO §3.1/§5.2, 34-HC hybrid
       contact-center + trade desk + ecommerce-support org).
  6. "VP Compliance" (~75) -> VP Legal
       — the corpus's 864-use short form of the charted "VP Legal & Compliance" (the
       same short-form convention as "VP Supply Chain" for "VP Supply Chain &
       Logistics"); compliance/MLRO/DPO all sit under that seat.
  7. "VP Property" (~74) + "VP Engineering" (~53) + "Engineering Director" (~9) +
     "Construction Director" (~5) + "Facilities Director" (~22) -> Director, Facilities
     & Real Estate
       — the charted dual-hat seat (TO §3.1: "Director, Facilities & Real Estate
       (dual-hat GM, Property Mgmt Inc.): facilities engineering · maintenance
       coordination · lease & surety admin · energy mgmt"). Site selection (VS-20),
       engineering & construction (PA-20.2), BERDE/green building (VS-25.2/VS-78),
       equipment masters (VS-29), PCAB licensing (VS-165) and facilities (VS-138/42/97)
       are all remits of that seat; "Head of Facilities" (56 uses) stays as the
       department's working-level role beneath it.
  8. "Supply Chain Director" (~56) -> VP Supply Chain
       — the 945-use corpus short form of the charted "VP Supply Chain & Logistics".
  9. "Sustainability Director" (~29) -> Sustainability/ESG Manager
       — the 218-use corpus form (batch-25 CSO precedent); the Head of Sustainability /
       ESG sub-team (TO §3.1, 4 HC §5.2).
 10. "VP IT Finance" (~111) -> FinOps Lead
       — the corpus's own form (existing Owner cells) for the CIO-Office FinOps
       function (TO §5.2: "CIO Office (EA, Portfolio Governance, FinOps, Vendor
       Portfolio)"; IT model §3.2). The A-column exec pairs ("CIO / CFO") are
       untouched — the VP-level IT-finance seat is uncharted by design.
 11. "Regional Operations Director" (~4) -> Regional Manager
       — the batch-26 rule-10 precedent (charted field layer, TO §7.1); VS-26 crisis
       regional commander.
 12. "Store Operations Director" (1 PA + 1 IT-model partner label) -> VP Store
       Operations — the charted seat (TO §3.1); also trues the SSP partner label in
       it-product-operating-model.md §3.2.
 13. "CISO" (~12) -> IT Security Manager
       — the corpus's security seat (8-use VS-27.3 Owner form; the SEC platform has no
       separately charted head). Includes the PA-167.2 executive-vetting trigger list.
 14. "SVP" (1, erp-requirements WSL-003) -> COO
       — the uncharted third tier of the wholesale-discount ladder trued onto the
       trade org's executive (COO owns Trade/Account Mgmt per TO §3), preserving the
       3-tier ladder Sales Manager < 5% → Head of Trade / Account Management < 10% →
       COO beyond.
"""
import glob, os, re

REPO = "/home/alden/erpplans/01-model-company"

RULES = [
    (re.compile(r"VP Innovation & Digital Transformation"), "CIO"),
    (re.compile(r"VP Sales & Trade Operations"), "Head of Trade / Account Management"),
    (re.compile(r"VP Govt Affairs"), "Government Affairs Manager"),
    (re.compile(r"VP Digital Commerce"), "GM, Digital Commerce Inc."),
    (re.compile(r"VP Digital"), "GM, Digital Commerce Inc."),
    (re.compile(r"VP Omnichannel"), "GM, Digital Commerce Inc."),
    (re.compile(r"VP Ecommerce"), "GM, Digital Commerce Inc."),
    (re.compile(r"Ecommerce Director"), "GM, Digital Commerce Inc."),
    (re.compile(r"VP Customer Experience"), "Head of Customer Service"),
    (re.compile(r"VP Compliance"), "VP Legal"),
    (re.compile(r"VP Property"), "Director, Facilities & Real Estate"),
    (re.compile(r"VP Engineering"), "Director, Facilities & Real Estate"),
    (re.compile(r"Engineering Director"), "Director, Facilities & Real Estate"),
    (re.compile(r"Construction Director"), "Director, Facilities & Real Estate"),
    (re.compile(r"Facilities Director"), "Director, Facilities & Real Estate"),
    (re.compile(r"Supply Chain Director"), "VP Supply Chain"),
    (re.compile(r"Sustainability Director"), "Sustainability/ESG Manager"),
    (re.compile(r"Commercial Director"), "Head of Trade / Account Management"),
    (re.compile(r"Sales Director"), "Head of Trade / Account Management"),
    (re.compile(r"VP Sales"), "Head of Trade / Account Management"),
    (re.compile(r"VP IT Finance"), "FinOps Lead"),
    (re.compile(r"Regional Operations Director"), "Regional Manager"),
    (re.compile(r"Store Operations Director"), "VP Store Operations"),
    (re.compile(r"\bCISO\b"), "IT Security Manager"),
    (re.compile(r"\bVP Innovation\b"), "CIO"),
    (re.compile(r"\bSVP\b"), "COO"),
    # --- batch-14 extension: the batch-28/29-measured residual families (item A tail) ---
    (re.compile(r"Director of Real Estate"), "Director, Facilities & Real Estate"),
    (re.compile(r"Legal Head"), "VP Legal"),
    (re.compile(r"IT Director"), "CIO"),
    (re.compile(r"HR Director"), "CHRO"),
    (re.compile(r"Chief Transformation Officer"), "CHRO"),
    (re.compile(r"VP OCM"), "CHRO"),
    (re.compile(r"VP Operational Excellence"), "COO"),
    (re.compile(r"VP OpEx"), "COO"),
    (re.compile(r"VP of Store Operations"), "VP Store Operations"),
]

total_lines = 0
files_changed = 0
per_rule = {r.pattern: 0 for r, _ in RULES}
for path in sorted(glob.glob(os.path.join(REPO, "**", "*.md"), recursive=True)):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    orig = text
    for rx, rep in RULES:
        text, n = rx.subn(rep, text)
        per_rule[rx.pattern] += n
    if text != orig:
        files_changed += 1
        total_lines += sum(1 for a, b in zip(orig.splitlines(), text.splitlines()) if a != b)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)

# companion true-up outside the REPO glob: the IT model's SSP partner label
it_model = "/home/alden/erpplans/07-methodology/it-product-operating-model.md"
with open(it_model, encoding="utf-8") as f:
    t = f.read()
t2, n = re.subn(r"Store Operations Director", "VP Store Operations", t)
if n:
    per_rule["Store Operations Director"] += n
    with open(it_model, "w", encoding="utf-8") as f:
        f.write(t2)

print(f"files changed: {files_changed}; lines changed: {total_lines}")
for rx, n in per_rule.items():
    print(f"{n:5d}  {rx}")

# --- post-sweep hand-trues (the batch-26 'same-cell duplication & ladder collapse'
# practice): repair same-cell executive duplications CREATED by the mapping ---
TRUES = [
    # '| **Owner** | VP OpEx / COO Office |' -> 'COO / COO Office' duplication
    ("| **Owner** | COO / COO Office |", "| **Owner** | COO Office (OpEx CoE) |"),
    # '| **Owner** | Chief Transformation Officer / VP OCM |' -> 'CHRO / CHRO'
    ("| **Owner** | CHRO / CHRO |", "| **Owner** | CHRO |"),
    # R-cell 'Facilities Manager / IT Director' against A-cell 'CIO' -> 'CIO | CIO'
    ("| Facilities Manager / CIO | CIO |", "| Facilities Manager / IT Infrastructure Lead | CIO |"),
    # step R-cell duplication created by the VP OpEx mapping (PA-133.1 step 1)
    ("| COO / COO Office | CEO / COO |", "| COO Office (OpEx CoE) | CEO / COO |"),
    # R-cell 'VP OCM / CHRO' pairs collapse to CHRO alone (both map to the same seat)
    ("| VP OCM / CHRO | CEO | Annual |", "| CHRO | CEO | Annual |"),
    ("| OCM / HR-EX / People Analytics | VP OCM / CHRO |", "| OCM / HR-EX / People Analytics | CHRO |"),
]
trued = 0
for path in sorted(glob.glob(os.path.join(REPO, "**", "*.md"), recursive=True)):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    orig = text
    for old, new in TRUES:
        if old in text:
            text = text.replace(old, new)
            trued += 1
    if text != orig:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
print(f"hand-trues applied: {trued}")
