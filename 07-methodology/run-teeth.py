#!/usr/bin/env python3
"""Permanent teeth harness for validate-repo.sh — the wave-teeth suite, codified.

Every consistency-review wave since the ninth verified its new guard by synthetic
injection: apply a fault to a throwaway copy, assert the specific check fires with
the specific diagnosis, restore byte-identical. Those injections were hand-built
per wave and discarded — which meant every validator refactor (most recently the
2026-10-07 prefetch rewrite) had to re-derive its teeth from scratch, and a guard
silently disarmed between waves would go unseen until the next review happened to
probe that exact class. This harness makes the suite permanent: one command that
re-fires every historical fault class against the current validator and fails
loudly if any of them slips through. When a new generated-tree guard or checker
joins the validator, add its fault class here as a new tooth (the catalog-
projection staleness class joined as tooth 13 with the 2026-09-10 catalog pass,
and the capacity-model staleness class as tooth 14 with the capacity pass).

Protocol (inherited from the fourteenth-wave lesson):
  * copy-based — the live working tree is NEVER touched. The repo is copied once
    (minus .git, which validate-repo.sh never invokes, and __pycache__/.github,
    which it does not read) into a temp dir; every injection happens there.
  * negative control — the pristine copy must validate green (exit 0,
    "Errors: 0, Warnings: 0") before any tooth fires, so a harness bug can never
    masquerade as a caught fault.
  * exact-diagnosis assertions — a tooth passes only if the run fails AND the
    output names the expected check's diagnosis (not merely "some error"): the
    wave-6 failure mode was a guard "passing" off its own stale history, and a
    bare exit-code check would reproduce it.
  * sha256-verified restore — after each tooth the injected files are restored
    from pre-injection snapshots and the restore is hash-verified, so tooth N+1
    always starts from the true baseline (a stray leftover from tooth N must fire
    as a harness error, not as someone else's guard).

Usage: python3 07-methodology/run-teeth.py [--keep]   (--keep preserves the work
dir for debugging; default cleans up). Exit 0 iff the negative control is green
and every tooth fired with its exact diagnosis.
"""

import argparse
import hashlib
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

ANSI = re.compile(r"\x1b\[[0-9;]*m")

# ---------------------------------------------------------------------------
# Injections. Each tooth: (name, diagnosis-line, paths touched, transform, expects)
#   paths    — repo-relative files the transform reads/writes (snapshot + restored)
#   transform— fn(text_by_path) -> new_text_by_path, applied to the copy
#   expects  — substrings that must appear in the (ANSI-stripped) validator output
# ---------------------------------------------------------------------------

PA1 = "01-model-company/workflows/VS-01-merchandise-strategy/PA-01.1-assortment-planning-and-product-lifecycle.md"
BPMN1 = "bpmn/VS-01-merchandise-strategy/PA-01.1-assortment-planning-and-product-lifecycle.bpmn"
CLS = "01-model-company/workflows/workflow-criticality-classification.md"
README = "README.md"
VS2 = "01-model-company/workflows/VS-02-supply-planning/README.md"
GUIDE = "07-methodology/ai-first-operating-guide.md"


def _one(path, old, new, count=1):
    def t(texts):
        s = texts[path]
        assert old in s, f"injection anchor not found in {path}: {old[:60]!r}"
        texts[path] = s.replace(old, new, count)
        return texts
    return t


def _ghost_header(texts):
    lines = texts[PA1].split("\n")
    for i, ln in enumerate(lines):
        if ln.startswith("## W") and i > 5:
            lines.insert(i, "## W9999. Test Ghost Workflow")
            lines.insert(i + 1, "")
            lines.insert(i + 2, "Body.")
            break
    else:
        raise AssertionError("no ## W header found")
    texts[PA1] = "\n".join(lines)
    return texts


def _drop_footer(texts):
    lines = [ln for ln in texts[PA1].split("\n")]
    while lines and not lines[-1].strip():
        lines.pop()
    assert lines[-1].startswith("*Workflow Count:"), "footer not where expected"
    lines.pop()
    texts[PA1] = "\n".join(lines) + "\n"
    return texts


def _break_steps_row(texts):
    lines = texts[PA1].split("\n")
    in_steps = False
    for i, ln in enumerate(lines):
        if ln.startswith("### Steps"):
            in_steps = True
            continue
        if in_steps and re.match(r"^\| \d+ \| ", ln):
            lines[i] = ln[2:]  # drop the leading '| '
            texts[PA1] = "\n".join(lines)
            return texts
        if in_steps and ln.startswith("### "):
            break
    raise AssertionError("no steps-table data row found")


def _append_end(path, addition):
    def t(texts):
        texts[path] = texts[path] + addition
        return texts
    return t


TEETH = [
    (
        "stale-root-readme-total",
        "root-README tree total quotes the retired corpus total (Check 44/70 class)",
        [README],
        _one(README, "5,427 workflows", "5,426 workflows"),
        ["declares 5426 but the canonical figure is 5427"],
    ),
    (
        "tier-headline-drift",
        "classification Tier-1 heading disagrees with its own register rows (Check 18/59 class)",
        [CLS],
        _one(CLS, "## Tier 1: Core Operations (1,396 Workflows)",
             "## Tier 1: Core Operations (1,397 Workflows)"),
        ["Tier heading says 1,397 but following prose says 1,396",
         "register holds 1396 Tier-1 row(s)"],
    ),
    (
        "ghost-workflow-header",
        "unregistered ## W header in a PA file (Check 1/2/3 class)",
        [PA1],
        _ghost_header,
        ["file has 23 workflow headers, index says 22",
         "does NOT match actual PA workflow header count (5428)"],
    ),
    (
        "missing-pa-footer",
        "PA file loses its standardized footer (Check 16 class)",
        [PA1],
        _drop_footer,
        ["do not end with the standardized footer"],
    ),
    (
        "unregenerated-markdown-edit",
        "PA markdown field edited, generated BPMN not regenerated (Check 71 content mirror)",
        [PA1],
        _one(PA1, "**Volume**", "**Volume** STALE-EDIT"),
        ["Generated BPMN/DMN trees failed structural validation"],
    ),
    (
        "bpmn-xml-corruption",
        "generated BPMN file hand-corrupted (Check 71 structural class)",
        [BPMN1],
        _one(BPMN1, "<bpmn:documentation>", "<bpmn:documentationX>"),
        ["XML parse error"],
    ),
    (
        "broken-vs-readme-link",
        "VS README gains a dead relative link (Check 66 class)",
        [VS2],
        _append_end(VS2, "\nSee also [the missing companion](./no-such-companion-doc.md).\n"),
        ["broken relative link(s) outside PA files", "missing target"],
    ),
    (
        "inverted-version-chain",
        "document version dropped below its own Prior chain (Check 72 class)",
        [GUIDE],
        _one(GUIDE, "*Document Version: 1.10 |", "*Document Version: 0.9 |"),
        ["at/above the live version"],
    ),
    (
        "dangling-w-reference",
        "PA body cites a nonexistent workflow id (Check 33 class)",
        [PA1],
        _one(PA1, "### Pain Points / Risks",
             "### Pain Points / Risks\n- Escalation follows W8888 (teeth injection)."),
        ["Dangling workflow-ID citations found", "W8888"],
    ),
    (
        "dangling-requirement-citation",
        "root doc cites a nonexistent requirement id (Check 32 class)",
        [README],
        _append_end(README, "\nDangling-requirement injection probe: see GOV-999.\n"),
        ["Dangling requirement-ID citations found", "GOV-999"],
    ),
    (
        "steps-row-leading-pipe",
        "steps-table row loses its leading pipe (Check 48 class)",
        [PA1],
        _break_steps_row,
        ["Steps-table integrity violations found"],
    ),
    (
        "quoted-check-count",
        "self-description quotes a check count that is not implemented (Check 40 class)",
        [README],
        _one(README, "Cross-reference validation (76 checks)",
             "Cross-reference validation (77 checks)"),
        ["Quoted validator check counts disagree"],
    ),
    (
        "catalog-json-stale",
        "catalog/ JSON hand-edited (or markdown edited without catalog regeneration) — Check 71's --check mirror class",
        ["catalog/VS-01-merchandise-strategy/PA-01.1-assortment-planning-and-product-lifecycle.json"],
        _one("catalog/VS-01-merchandise-strategy/PA-01.1-assortment-planning-and-product-lifecycle.json",
             '"Owner": "Category Manager (Outdoor & Garden)"', '"Owner": "STALE EDIT"'),
        ["stale (differs from regeneration)",
         "catalog/VS-01-merchandise-strategy/PA-01.1-assortment-planning-and-product-lifecycle.json"],
    ),
    (
        "capacity-model-stale",
        "capacity model report hand-edited (or corpus/register edited without regeneration) — Check 71's --check mirror class",
        ["01-model-company/workforce-capacity-model.md"],
        _one("01-model-company/workforce-capacity-model.md",
             "1,800 h/FTE-year", "1,900 h/FTE-year"),
        ["stale (differs from regeneration)",
         "01-model-company/workforce-capacity-model.md"],
    ),
]


def run_validator(root: Path, timeout=600):
    t0 = time.time()
    p = subprocess.run(
        ["bash", "07-methodology/validate-repo.sh"],
        cwd=str(root), capture_output=True, text=True, timeout=timeout,
        env={**__import__("os").environ, "VALIDATE_JOBS": "8"},
    )
    out = ANSI.sub("", p.stdout) + ANSI.sub("", p.stderr)
    return p.returncode, out, time.time() - t0


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--keep", action="store_true", help="keep the temp work dir")
    args = ap.parse_args()

    work = Path(tempfile.mkdtemp(prefix="erpplans-teeth."))
    copy = work / "repo"
    print(f"teeth: copying repo (minus .git/__pycache__/.github) to {work}")
    t0 = time.time()
    shutil.copytree(
        REPO, copy,
        ignore=shutil.ignore_patterns(".git", "__pycache__", ".github"),
        symlinks=True,
    )
    print(f"teeth: copy ready in {time.time() - t0:.1f}s")

    failures = []

    # -- negative control ---------------------------------------------------
    rc, out, dt = run_validator(copy)
    if rc == 0 and "Errors: 0, Warnings: 0" in out:
        print(f"negative-control: PASS (clean copy green, {dt:.1f}s)")
    else:
        print("negative-control: FAIL — the pristine copy does not validate green;")
        print("  the teeth cannot adjudicate faults on a broken baseline.")
        tail = out.strip().splitlines()[-8:]
        print("\n".join("    " + l for l in tail))
        return 1

    # -- teeth ---------------------------------------------------------------
    for i, (name, blurb, paths, transform, expects) in enumerate(TEETH, 1):
        snaps = {p: (copy / p).read_text(encoding="utf-8") for p in paths}
        try:
            texts = dict(snaps)
            transform(texts)
            for p, s in texts.items():
                (copy / p).write_text(s, encoding="utf-8")
        except AssertionError as e:
            failures.append((name, f"injection construction failed: {e}"))
            print(f"[{i:2d}/{len(TEETH)}] {name}: FAIL — {e}")
            continue

        rc, out, dt = run_validator(copy)

        problems = []
        if rc == 0:
            problems.append("validator exited 0 — fault NOT caught")
        for exp in expects:
            if exp not in out:
                problems.append(f"expected diagnosis missing: {exp!r}")

        # restore + verify
        for p, s in snaps.items():
            (copy / p).write_text(s, encoding="utf-8")
        for p in paths:
            if hashlib.sha256(snaps[p].encode("utf-8")).hexdigest() != sha256(copy / p):
                problems.append(f"restore hash mismatch: {p}")

        if problems:
            failures.append((name, "; ".join(problems)))
            print(f"[{i:2d}/{len(TEETH)}] {name}: FAIL — {'; '.join(problems)}")
            if rc != 0 and not any("diagnosis missing" in x for x in problems):
                pass
            for pr in problems:
                if "diagnosis missing" in pr:
                    tail = out.strip().splitlines()[-25:]
                    print("\n".join("      " + l for l in tail))
        else:
            print(f"[{i:2d}/{len(TEETH)}] {name}: PASS ({dt:.1f}s) — {blurb}")

    print()
    if failures:
        print(f"teeth: {len(failures)} of {len(TEETH)} teeth FAILED:")
        for name, why in failures:
            print(f"  - {name}: {why}")
        if not args.keep:
            shutil.rmtree(work, ignore_errors=True)
        return 1
    print(f"teeth: all {len(TEETH)} teeth fired with exact diagnoses; negative control green; "
          f"restores sha256-verified.")
    if not args.keep:
        shutil.rmtree(work, ignore_errors=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
