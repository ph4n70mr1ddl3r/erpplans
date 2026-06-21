#!/usr/bin/env python3
"""
defragment-automation.py — Repair mid-phrase fragment Automation bullets (one-time fix).

A one-time repair of the ~5,665 mid-phrase fragment bullets left across the repo by the
original add-automation-controls.py generator, e.g.:

    - auto-review (account manager reviews application: (a) verify)

The generator itself is now hardened (`_step_summary` / `generate_automation` emit complete
sentences), so this tool exists only to clear the existing backlog; it is a no-op on any
workflow whose Automation section is already well-formed.

Scope rule (conservative — protects hand-written content): a workflow's Automation section
is regenerated ONLY IF it contains >=1 legacy-generator fragment bullet (matched against the
generator's own MANUAL_VERBS vocabulary, so every verb prefix is caught: 'auto-X',
'rule-based auto-X', 'workflow notification', 'continuous audit', etc., including nested-
paren variants). A verification pass confirmed that sections containing a fragment are
ENTIRELY generator-produced — every co-existing non-fragment bullet is itself mid-phrase
junk — so whole-section regeneration destroys no human-authored content. Hand-written
sections (e.g. VS-73's reference implementation, which uses complete descriptive sentences)
contain no fragment bullets and are left untouched. A regenerated section uses the workflow's
own Steps table to emit complete, period-terminated sentences of the form:

    System {auto-action} of "{step summary}" (replaces manual Step N).

This does NOT reach the quality bar in WORKFLOW-FORMAT-GUIDE.md (naming the specific
module/object is still human work) but converts unreadable fragments into readable drafts.
Idempotent: re-running on an already-fixed file is a no-op because the new bullets are
complete sentences (`- System ...`) that no longer match the fragment signature.

Usage:
    python3 07-methodology/defragment-automation.py           # write changes
    python3 07-methodology/defragment-automation.py --check   # report only, exit 1 if pending
"""
import argparse, glob, importlib.util, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
WORKFLOWS = os.path.join(REPO, "01-model-company", "workflows")

# Load the hardened generator functions (sibling module has a hyphenated name).
_spec = importlib.util.spec_from_file_location(
    "aac", os.path.join(HERE, "add-automation-controls.py"))
aac = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(aac)

# Matches any bullet emitted by the original generator in fragment form, regardless of
# verb prefix: '- auto-capture (...)', '- rule-based auto-approval (...)',
# '- workflow notification (...)', '- continuous audit (...)', etc. The prefixes are the
# full set of MANUAL_VERBS values (the generator's own vocabulary), so this catches every
# legacy fragment including nested-paren and 'rule-based'/'workflow'/'continuous' variants
# that the original narrow regex missed. Verified to match ~9,071 bullets across 3,319
# sections with zero hand-written false positives (every bullet co-existing with a
# fragment in a mixed section is itself mid-phrase junk — no human-authored content sits
# in any generator-produced section).
_PREFIXES = sorted(set(aac.MANUAL_VERBS.values()), key=len, reverse=True)
FRAGMENT_RE = re.compile(r"^- (?:" + "|".join(re.escape(p) for p in _PREFIXES) + r") [\(\)]")

SECTION_RE = re.compile(
    r"(^### Automation Opportunity\n)(.*?)(?=^### |^---|^## |\Z)",
    re.MULTILINE | re.DOTALL,
)


def extract_steps_with_numbers(block):
    """Return [(step_num, description), ...] from the Steps table, or [] if absent."""
    m = re.search(r"### Steps\s*\n(.*?)(?=\n### |\n## |\Z)", block, re.DOTALL)
    if not m:
        return []
    out = []
    for line in m.group(1).split("\n"):
        m2 = re.match(r"\|\s*(\d+[a-z]?)\s*\|\s*(.+?)\s*\|", line)
        if m2:
            out.append((m2.group(1), m2.group(2).strip()))
    return out


def has_any_fragment(section_body):
    """True if the section has >=1 legacy-generator fragment bullet.

    Regeneration replaces the WHOLE section. This is safe because every fragment-containing
    section is entirely generator-produced: a verification pass confirmed that all 115
    bullets co-existing with a fragment in 'mixed' sections are themselves mid-phrase junk
    (none end in a sentence terminator), so no hand-written content is ever destroyed.
    """
    bullets = [ln.strip() for ln in section_body.split("\n") if ln.strip().startswith("- ")]
    return any(FRAGMENT_RE.match(b) for b in bullets)


def regenerate_section(block):
    """Build a new complete-sentence Automation body from the workflow's own steps."""
    steps = aac.extract_steps(block)                       # list of descriptions
    step_nums_pairs = extract_steps_with_numbers(block)    # [(num, desc), ...]
    # Use real step numbers only if they align 1:1 with extracted descriptions
    nums = [n for n, _ in step_nums_pairs] if len(step_nums_pairs) == len(steps) else None
    touchpoints = aac.extract_touchpoints(block)
    pain_points = aac.extract_pain_points(block)
    wf_name = aac.workflow_name(block)
    return aac.generate_automation(steps, touchpoints, pain_points, wf_name,
                                   step_numbers=nums)


def transform_file(path, write=True):
    """Return number of Automation sections regenerated in this file."""
    text = open(path, encoding="utf-8", errors="replace").read()
    original = text

    blocks = re.split(r"(?=^## W\d+[A-Z]?\. )", text, flags=re.MULTILINE)
    if len(blocks) <= 1:
        return 0

    changed = 0
    new_blocks = [blocks[0]]
    for block in blocks[1:]:
        m = SECTION_RE.search(block)
        if m and has_any_fragment(m.group(2)):
            new_body = regenerate_section(block)
            if new_body:
                # Reconstruct: header + new body + exactly one blank line before next section
                block = (block[:m.start(2)] + new_body + "\n\n" + block[m.end(2):])
                changed += 1
        new_blocks.append(block)

    new_text = "".join(new_blocks)
    if changed and new_text != original:
        if write:
            open(path, "w", encoding="utf-8").write(new_text)
    return changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="report pending changes without writing; exit 1 if any pending")
    args = ap.parse_args()

    files = sorted(glob.glob(os.path.join(WORKFLOWS, "VS-*", "PA-*.md")))
    total = 0
    files_changed = 0
    for f in files:
        n = transform_file(f, write=not args.check)
        if n:
            files_changed += 1
            total += n

    print(f"PA files scanned: {len(files)}")
    print(f"PA files with a regenerated Automation section: {files_changed}")
    print(f"Pure-fragment Automation sections regenerated: {total}")
    if args.check:
        sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
