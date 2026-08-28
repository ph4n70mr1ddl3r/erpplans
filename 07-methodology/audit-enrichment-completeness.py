#!/usr/bin/env python3
"""
audit-enrichment-completeness.py — mitigation-clause & Trigger-richness guard.

The 2026-08-29 enrichment pass closed the two backlogs quantified by
consistency review #40:

  * mitigation clauses — the 231 risk bullets that stated a risk without any
    mitigation semantics were enriched with 'mitigated by …' clauses derived
    by affinity-matching each bullet against its OWN workflow's Controls
    section (the operational '<Role> review and approval gate' where it fits,
    else the PA-level CTL-XXX execution control). Every clause is grounded —
    no control is cited that is not in that workflow's Controls section. The
    repo-wide census is now 7,066/7,066 bullets carrying mitigation content.
  * Trigger richness — the 38 cadence-only Trigger values outside the
    Check-52 shared-event allowlist ('Monthly', 'Quarterly analysis',
    'Monthly reporting'…) were enriched with their workflow's own title
    subject ('Monthly analytics cycle — Sales Per Square Meter'), keeping the
    event noun and cadence intact. The other short triggers ('Breach
    confirmed', 'Retention expiry', 'Order split'…) were adjudicated
    already-specific event names.

Guard mode (--guard, validator Check 58): errors on (a) any risk bullet with
no mitigation semantics under the review's refined net (mitigat-/controlled
by/validated by/requires approval/system blocks/per W…), and (b) any
cadence-only Trigger value outside the Check-52 allowlisted files.
"""
import argparse, glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(REPO, "01-model-company", "workflows")

ANYMIT = re.compile(r"mitigat|controlled by|prevented by|offset by|minimized by|reduced by|"
                    r"guard\w* by|addressed by|managed by|monitored|deterr\w+|validated by|"
                    r"verified by|checked by|reviewed by|requires? (?:approval|review|sign|dual)|"
                    r"system (?:blocks|prevents|requires|enforces|flags|alerts)|approval (?:gate|required)|"
                    r"must be (?:approved|reviewed|validated|verified|reconciled|documented|recorded)|"
                    r"per W\d|per CTL", re.I)
CADENCE_ONLY = re.compile(r"^(Monthly|Quarterly|Weekly|Annual(ly)?|Semi-annual|Bi-annual|Daily)"
                          r"(;|\s+(reporting|analysis|analytics|review|survey|close|dashboard|"
                          r"calendar|update|benchmarking|comprehensive|report|cadence))?$", re.I)
ALLOW_SUBSTR = ["PA-130.2-transaction", "PA-130.3-integration", "PA-183.3-dts",
                "PA-21.1-audit", "PA-21.3-specialized", "PA-33.1-annual",
                "PA-37.1-new", "PA-59.1-store", "PA-60.3-fulfillment",
                "PA-61.2-toll", "PA-61.3-fleet", "PA-64.3-post",
                "PA-69.1-typhoon", "PA-75.3-digital", "PA-82.2-micro",
                "PA-85.3-tax", "PA-86.1-kyc"]


def check_file(path, hits):
    text = open(path, encoding="utf-8").read()
    rel = os.path.relpath(path, REPO)
    for sm in re.finditer(r"^### Pain Points / Risks\s*$", text, re.M):
        rest = text[sm.end():]
        stop = re.search(r"^### ", rest, re.M)
        body = rest[:stop.start()] if stop else rest
        for line in body.splitlines():
            ls = line.strip()
            if not ls.startswith("- **") or "risk" not in ls.split(":")[0].lower():
                continue
            if not ANYMIT.search(ls):
                line_no = text[:sm.start() + rest.find(ls)].count("\n") + 1 if ls in rest else 0
                hits.append(("bare-mitigation", rel, line_no, ls[:80]))
    if not any(a in path for a in ALLOW_SUBSTR):
        for m in re.finditer(r"^\| \*\*Trigger\*\* \| (.+?) \|$", text, re.M):
            if CADENCE_ONLY.match(m.group(1).strip()):
                line = text[:m.start()].count("\n") + 1
                hits.append(("cadence-only-trigger", rel, line, m.group(1).strip()))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guard", action="store_true",
                    help="exit 1 on any bare mitigation clause or cadence-only trigger")
    args = ap.parse_args()
    hits = []
    files = sorted(glob.glob(os.path.join(WORKFLOWS, "VS-*", "PA-*.md")))
    for f in files:
        check_file(f, hits)
    for kind, rel, line, detail in hits:
        print(f"{kind}: {rel}:{line}: {detail}")
    print(f"audit-enrichment-completeness: {len(hits)} hit(s) across {len(files)} PA files")
    if args.guard:
        sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
