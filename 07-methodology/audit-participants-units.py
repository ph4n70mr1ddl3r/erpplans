#!/usr/bin/env python3
"""
audit-participants-units.py — Participants-field hygiene & per-unit volume
coherence guard.

Consistency review #38 (2026-08-29) audited the surfaces named in the review
#37 close-out:

  * data-volumes-and-integrations.md vs PA Volume/Frequency at scale — the
    nine canonical §1.1 anchors (POS 93,333/day, DC goods receipts 200/day =
    6,000/month, POs 40–50/day, AP ~300/day, ecommerce ~1,430/day, DSD ~20/day,
    …) were normalized to monthly bands and checked against every PA
    Volume/Frequency figure naming those quantities: agreement is remarkably
    clean — subset and per-store figures (5% of ecommerce, 36% of POS card
    share, BOPIS/delivery mix) verify internally, W867's portal-invoice volume
    coheres with the ~800–1,000 vendor base as a portal share of W7's 6,715
    merchandise invoices, and the single defect repaired was W3's per-DC
    arithmetic (6,000 ÷ 4 = 1,500/DC, not ~1,200/DC and ~40/day).
  * Participants-field role vocabulary — 35 rows carried stray RACI markers
    '(R)'/'(A)'/'(R/A)' duplicating the Steps tables (stripped; the other
    5,350 rows use plain names per the format guide); the 'Analytics Mgr'
    abbreviation unified to 'Analytics Manager' (68 spots incl. VS READMEs);
    plural/case variants normalized (AP Clerks, AR Clerks/Managers, 3PL
    carrier).
  * steps-table Duration unit vocabulary — spell-clean: min/hours/days/weeks
    dominate, the hrs/minutes/sec abbreviation variety is established house
    usage, and the apparent 'hors'/'das' hits were substrings of
    Authors/horsepower/anchors. Nothing to repair; nothing retired.

Guard mode (--guard, validator Check 55):
  1. Participants rows must not carry RACI markers;
  2. the 'Analytics Mgr' abbreviation must not reappear (PA files + VS
     READMEs);
  3. same-row per-unit coherence — any Volume/Frequency row pairing a
     chain-wide total for DCs or stores with a per-unit figure must satisfy
     units × per-unit ≈ total within ±30% (W3's 1,200/DC vs 6,000 class).
"""
import argparse, glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(REPO, "01-model-company", "workflows")

PARTICIPANTS_RE = re.compile(r"^\| \*\*Participants\*\* \| .+\|$", re.M)
ROW_RE = re.compile(r"^\| \*\*(?:Volume|Frequency)\*\* \| (.+?) \|$", re.M)
UNIT_COUNT = {"dc": 4, "store": 200}


def tof(s):
    return float(s.replace(",", "").replace("~", ""))


def check_file(path, hits):
    text = open(path, encoding="utf-8").read()
    rel = os.path.relpath(path, REPO)
    for m in PARTICIPANTS_RE.finditer(text):
        if re.search(r"\((?:R|A|R/A)\)", m.group(0)):
            line = text[:m.start()].count("\n") + 1
            hits.append(("raci-marker", rel, line,
                         "Participants row carries a (R)/(A) marker"))
    if "Analytics Mgr" in text:
        line = text[:text.find("Analytics Mgr")].count("\n") + 1
        hits.append(("retired-literal", rel, line, "Analytics Mgr"))
    for m in ROW_RE.finditer(text):
        row = m.group(1)
        for unit_word, units in UNIT_COUNT.items():
            tot = re.search(r"~?([\d,]+)(?:[–—-]~?([\d,]+))?\s+[\w/-]+(?:\s+[\w/-]+){0,3}?"
                            r"(?:\s*/|\s+per\s|\s+across\s(?:all\s)?)" + unit_word, row, re.I)
            per = re.search(r"~?([\d,]+)(?:[–—-]~?([\d,]+))?\s*/\s*" + unit_word +
                            r"\b|~?([\d,]+)(?:[–—-]~?([\d,]+))?\s+per\s+" + unit_word +
                            r"\b", row, re.I)
            if not tot or not per:
                continue
            t_vals = [tof(x) for x in tot.groups() if x]
            p_groups = [g for g in per.groups() if g]
            p_vals = [tof(x) for x in p_groups]
            if not t_vals or not p_vals:
                continue
            t_lo, t_hi = min(t_vals), max(t_vals)
            p_lo, p_hi = min(p_vals), max(p_vals)
            prod_lo, prod_hi = p_lo * units, p_hi * units
            if prod_hi < t_lo * 0.7 or prod_lo > t_hi * 1.3:
                line = text[:m.start()].count("\n") + 1
                hits.append(("per-unit-coherence", rel, line,
                             f"{unit_word}s: per-unit {p_lo:g}–{p_hi:g} × {units} = "
                             f"{prod_lo:g}–{prod_hi:g} vs stated total {t_lo:g}–{t_hi:g}"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guard", action="store_true",
                    help="exit 1 on any hit (validator mode)")
    args = ap.parse_args()
    hits = []
    files = sorted(glob.glob(os.path.join(WORKFLOWS, "VS-*", "PA-*.md")))
    files += sorted(glob.glob(os.path.join(WORKFLOWS, "VS-*", "README.md")))
    for f in files:
        check_file(f, hits)
    for kind, rel, line, detail in hits:
        print(f"{kind}: {rel}:{line}: {detail}")
    print(f"audit-participants-units: {len(hits)} hit(s) across {len(files)} files")
    if args.guard:
        sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
