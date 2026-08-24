#!/usr/bin/env python3
"""
fix-toc-completeness.py — Repair the '## Workflows in This Process Area' TOC lists in PA files.

Consistency review #18 (2026-06-28) found a defect class no prior check could see:
validator Check 23 verifies that every TOC ANCHOR resolves to a heading, but never asked
whether the TOC is complete, de-duplicated, or free of debris. Three sub-classes found:

  (a) STRAY MID-FILE TOC FRAGMENTS — navigation lists left inside the workflow body when
      appended workflows were merged (an edit added the entries to the header TOC but left
      the duplicate block behind): VS-04 PA-04.2 (6 lines) and VS-06 PA-06.2 (2 lines);
  (b) DUPLICATE TOC ENTRIES — the visible symptom of (a) at ID level;
  (c) MISSING TOC ENTRIES — a shipped workflow heading with no TOC line at all
      (VS-12 PA-12.2: W1318 was invisible in the file's navigation).

This tool repairs all three, idempotently:
  1. deletes any '- [W…](#…)' line appearing AFTER the first '## W' workflow heading
     (TOC lines only belong in the header navigation block);
  2. keeps only the FIRST occurrence of each TOC entry (by W-id);
  3. inserts a TOC line for every '## W…' workflow heading that lacks one
     ('### W…' parent/summary sub-workflows are deliberately not TOC-indexed by repo
     convention — see WORKFLOW-FORMAT-GUIDE.md), positioned to match the file's heading
     order, with the anchor regenerated from the heading text using GitHub's slug rules
     (github-slugger semantics, non-collapsing — same gh_slug() as fix-toc-anchors.py).

Usage:
    python3 07-methodology/fix-toc-completeness.py           # write changes
    python3 07-methodology/fix-toc-completeness.py --check   # report only, exit 1 if pending
"""
import argparse, glob, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(REPO, "01-model-company", "workflows")

WF_HEADING = re.compile(r"^## (W\d+[A-Z]?(?:\.\d+[a-z]?)?)\. +(.+?)\s*$", re.MULTILINE)
TOC_LINE = re.compile(r"^- \[(W[^\]]+)\]\(#([^)]+)\)\s*$")

# NOTE: by repo convention the PA TOC lists ONLY '## W…' (h2) workflows — '### W…' (h3)
# parent/summary sub-workflows (e.g. W2A, W5B) are deliberately NOT TOC-indexed (see
# WORKFLOW-FORMAT-GUIDE.md); this script's completeness logic therefore tracks h2 only.

# GitHub heading slug (github-slugger semantics, non-collapsing) — identical to
# fix-toc-anchors.py gh_slug(); see that script for the double-hyphen rationale.
def gh_slug(s):
    s = s.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    return s.replace(" ", "-")


def heading_slug_set(headings):
    seen, out = {}, set()
    for h in headings:
        s = gh_slug(h)
        n = seen.get(s, 0)
        seen[s] = n + 1
        out.add(s if n == 0 else f"{s}-{n}")
    return out


def repair_file(path, write=True):
    """Return number of repair actions applied (0 = clean)."""
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")
    actions = 0

    # Locate first workflow heading and all workflow headings (id -> display text, order).
    first_wf_idx = None
    headings = []  # (wid, display)
    for i, ln in enumerate(lines):
        m = re.match(r"^## (W\d+[A-Z]?(?:\.\d+[a-z]?)?)\. +(.+?)\s*$", ln)
        if m:
            if first_wf_idx is None:
                first_wf_idx = i
            headings.append((m.group(1), f"{m.group(1)}. {m.group(2)}"))

    # 1. Stray TOC lines after the first workflow heading (and their orphaned '---' fence
    #    when the stray block was the only thing between two fences).
    if first_wf_idx is not None:
        kept = lines[:first_wf_idx + 1]
        skip_sep = 0
        for ln in lines[first_wf_idx + 1:]:
            if skip_sep > 0 and ln.strip() == "---":
                skip_sep -= 1
                actions += 1
                continue
            if TOC_LINE.match(ln):
                actions += 1
                # A stray entry directly fenced by '---' lines: also drop the fences.
                if kept and kept[-1].strip() == "---":
                    skip_sep = 1
                    kept.pop()
                continue
            kept.append(ln)
        lines = kept

    # 2. De-duplicate TOC entries by W-id (keep first).
    seen_ids, deduped, in_toc_zone, removed_dup = set(), [], False, 0
    for ln in lines:
        m = TOC_LINE.match(ln)
        if m:
            in_toc_zone = True
            wid = re.match(r"(W\d+[A-Z]?(?:\.\d+[a-z]?)?)", m.group(1)).group(1)
            if wid in seen_ids:
                removed_dup += 1
                continue
            seen_ids.add(wid)
        elif in_toc_zone and ln.startswith("## "):
            in_toc_zone = False
        deduped.append(ln)
    lines, actions = deduped, actions + removed_dup

    # 3. Insert missing TOC entries, in heading order.
    if headings:
        slugs = heading_slug_set([h for _, h in headings])
        toc_inserts = [(wid, disp) for wid, disp in headings if wid not in seen_ids]
        if toc_inserts:
            # Rebuild the TOC zone preserving existing lines' order/anchors, then splice
            # each missing entry after the last preceding known TOC entry (or at zone top).
            start = next((i for i, ln in enumerate(lines) if ln.startswith("## Workflows in This Process Area")), None)
            if start is None:
                start = next(i for i, ln in enumerate(lines) if TOC_LINE.match(ln))
            toc_end = start
            while toc_end + 1 < len(lines) and TOC_LINE.match(lines[toc_end + 1]):
                toc_end += 1
            existing = [re.match(r"(W\d+[A-Z]?(?:\.\d+[a-z]?)?)", TOC_LINE.match(l).group(1)).group(1)
                        for l in lines[start + 1: toc_end + 1]]
            order = {w: k for k, w in enumerate(existing)}
            def rank(w):
                # position among headings; missing entries splice near their neighbours
                hs = [h[0] for h in headings]
                return hs.index(w)
            for wid, disp in sorted(toc_inserts, key=lambda t: rank(t[0])):
                anchor = gh_slug(disp)
                if anchor not in slugs:  # duplicate-slug disambiguation fallback
                    base = anchor
                    for n in range(1, 8):
                        anchor = f"{base}-{n}"
                        if anchor in slugs:
                            break
                entry = f"- [{disp}](#{anchor})"
                # insert after the TOC line of the closest preceding heading present in TOC
                pos = start
                for j, w in enumerate([h[0] for h in headings]):
                    if w == wid:
                        for pw in reversed([h[0] for h in headings][:j]):
                            if pw in order:
                                pos = start + 1 + existing.index(pw)
                                break
                        else:
                            pos = start
                        break
                lines.insert(pos + 1, entry)
                existing.insert(pos - start, wid)
                order = {w: k for k, w in enumerate(existing)}
                actions += 1

    if actions and write:
        open(path, "w", encoding="utf-8").write("\n".join(lines))
    return actions


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="report only; exit 1 if pending")
    args = ap.parse_args()
    total, files = 0, 0
    for path in sorted(glob.glob(os.path.join(WORKFLOWS, "VS-*", "PA-*.md"))):
        n = repair_file(path, write=not args.check)
        if n:
            files += 1
            total += n
            print(f"{'PENDING' if args.check else 'FIXED'}: {os.path.relpath(path, REPO)} ({n} action(s))")
    verb = "pending" if args.check else "applied"
    print(f"\n{total} repair action(s) {verb} across {files} PA file(s).")
    if args.check and total:
        sys.exit(1)


if __name__ == "__main__":
    main()
