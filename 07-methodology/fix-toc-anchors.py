#!/usr/bin/env python3
"""
fix-toc-anchors.py — Repair intra-file TOC anchors that don't resolve.

A gap-analysis generation artifact left markdown TOC entries across PA files whose
anchor (the `#...` part of `](#...)`) did not match the heading it targets — so
clicking the TOC link does nothing on GitHub. Two malformation patterns:

  1. Slug dropped hyphens ('Floor-Plan' -> 'floorplan' instead of 'floor-plan') and
     collapsed compound words ('stocking-list' -> 'stockinglist', 'out-of-trust' ->
     'outoftrust').
  2. A stale W-number in the anchor (display text says 'W4601' but the anchor says
     '#w4409-...') left over from a workflow renumber.

Scope confirms a single generator bug: 0 broken anchors in the Core block
(VS-01..VS-31); every broken anchor is in the gap-analysis block (VS-89+). No prior
validator check saw this: Checks 19/20 verify linked FILES resolve; none resolve
anchors. (A companion validator Check 23 now guards it.)

The display text of every affected entry is correct, so the fix is mechanical:
regenerate the anchor from the display text using GitHub's heading-slug rules. This is
deterministic and safe — verified that for every broken entry, the corrected slug
resolves to exactly one heading in the same file.

Safe rule (applied per `[display](#anchor)` pair whose anchor does NOT resolve):
  1. If gh_slug(display) is a heading slug in this file -> use it.            (1,923 cases)
  2. Else if display carries a W-number with exactly one matching ## heading
     -> use that heading's slug (handles truncated/typo'd display text).       (3 cases)
  3. Else skip and report (display text itself malformed; needs a human glance).

Idempotent: a resolved anchor is never rewritten, so re-running is a no-op.

Usage:
    python3 07-methodology/fix-toc-anchors.py           # write changes
    python3 07-methodology/fix-toc-anchors.py --check   # report only, exit 1 if pending
"""
import argparse, glob, os, re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(REPO, "01-model-company", "workflows")

# GitHub heading slug (github-slugger semantics): lowercase; remove every character
# that is not a unicode word char, space, hyphen or underscore; then replace EACH
# remaining space with '-' — WITHOUT collapsing adjacent hyphens. The non-collapsing
# step matters: spaced punctuation (' & ', ' / ') leaves TWO adjacent spaces after
# removal, and GitHub renders those as a DOUBLE hyphen ('Merchandise Planning &
# Assortment Review' -> '#w1-merchandise-planning--assortment-review'). The v1
# implementation collapsed '[\s_-]+' runs to one '-', which silently reproduced the
# generator's original bug for every heading containing spaced punctuation — 4,615
# anchors repo-wide that resolved under the collapsing rule but NOT on GitHub (found
# by consistency review #11; see CHANGELOG 2026-06-26). Duplicate slugs get GitHub's
# '-1', '-2'… disambiguation suffixes.
def gh_slug(s):
    s = s.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s, flags=re.UNICODE)
    return s.replace(' ', '-')


def heading_slug_set(headings):
    """GitHub-accurate anchor set for a file: each slug, with '-N' suffix on duplicates."""
    seen = {}
    out = set()
    for h in headings:
        s = gh_slug(h)
        n = seen.get(s, 0)
        seen[s] = n + 1
        out.add(s if n == 0 else f"{s}-{n}")
    return out

LINK_RE = re.compile(r'\[([^\]]+)\]\(#([^)]+)\)')
HEADING_RE = re.compile(r'^#+\s+(.+?)\s*$', re.MULTILINE)


def analyze_file(path):
    """Return (replacements, skipped, text).
    replacements: list of (old_anchor, new_anchor) for broken anchors with a
                  deterministic target.
    skipped:      list of display texts whose anchor is broken but no deterministic
                  target was found (needs human)."""
    text = open(path, encoding='utf-8', errors='replace').read()
    headings = HEADING_RE.findall(text)
    heading_slugs = heading_slug_set(headings)
    # W-number -> unique heading slug, only when exactly one heading has that W-num.
    wmap = {}
    for h in headings:
        wm = re.match(r'(W\d+[A-Z]?)', h)
        if wm:
            wmap.setdefault(wm.group(1), []).append(gh_slug(h))
    w_unique = {w: slugs[0] for w, slugs in wmap.items() if len(slugs) == 1}

    replacements = []
    skipped = []
    for display, anchor in LINK_RE.findall(text):
        if anchor in heading_slugs:
            continue  # already resolves — never touch
        new = gh_slug(display)
        if new not in heading_slugs:
            wm = re.match(r'(W\d+[A-Z]?)', display)
            if wm and wm.group(1) in w_unique:
                new = w_unique[wm.group(1)]
            else:
                skipped.append(display)
                continue
        if new != anchor:
            replacements.append((anchor, new))
    return replacements, skipped, text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true',
                    help='report pending changes without writing; exit 1 if any pending')
    args = ap.parse_args()

    files = sorted(glob.glob(os.path.join(WORKFLOWS, 'VS-*', 'PA-*.md')))
    total_fixed = 0
    files_changed = 0
    all_skipped = []
    for f in files:
        replacements, skipped, text = analyze_file(f)
        all_skipped.extend((f, s) for s in skipped)
        if not replacements:
            continue
        # Apply: replace '](#OLD)' with '](#NEW)'. Every occurrence of a given broken
        # anchor should become the same target, so plain replace is correct; de-dup the
        # pairs to avoid redundant passes.
        new_text = text
        for old, new in sorted(set(replacements)):
            new_text = new_text.replace('](#' + old + ')', '](#' + new + ')')
        if new_text != text:
            if not args.check:
                open(f, 'w', encoding='utf-8').write(new_text)
            files_changed += 1
            total_fixed += len(replacements)

    print(f"PA files scanned: {len(files)}")
    print(f"PA files with anchor fixes: {files_changed}")
    print(f"Broken anchors fixed: {total_fixed}")
    if all_skipped:
        print(f"Skipped (display text malformed — needs human): {len(all_skipped)}")
        for f, s in all_skipped:
            print(f"  {f.replace(REPO + '/', '')}: '{s[:70]}'")
    if args.check:
        raise SystemExit(1 if total_fixed else 0)


if __name__ == '__main__':
    main()
