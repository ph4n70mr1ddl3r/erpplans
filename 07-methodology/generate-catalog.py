#!/usr/bin/env python3
"""Generate the machine-readable catalog/ projection of the workflow corpus.

Third generated tree alongside bpmn/ and dmn/. The markdown under
01-model-company/workflows/ remains the single source of truth; catalog/ is a
queryable projection (one JSON per PA + a master index) so the gap-analysis
sweeps, the capacity model, agent tooling and any future consumer can answer
"who owns X / what cites CTL-n / which workflows touch system Y" without
grepping 569 markdown files.

Extraction reuses generate-bpmn.py's own parser (parse_pa_file — the same
pattern Check 71's content mirror uses), so the catalog is consistent with the
BPMN tree by construction: same 5,450 workflow records (5,427 primary ## +
23 ###/#### sub-workflows), same fields/steps/sections derivation. On top of
the parsed block the generator adds:

  * level          — 2 for ## primary workflows, 3/4 for sub-workflows
  * tier           — the confirmed Tier 1/2/3 from the criticality register,
                     re-derived with the register's own section-context rules
                     (## Tier N headings, ### Tier N Additions, #### Tier N
                     overrides inside the classification passes)
  * ctl_refs       — every CTL-n token in the workflow's text
  * w_refs         — every other W-id token (cross-reference impact analysis)
  * req_refs       — requirement-ID tokens filtered to the defined
                     erp-requirements.md register (over-capture guard: only
                     IDs that exist are kept)

Outputs (deterministic; sort_keys serialization, trailing newline):
  catalog/VS-<slug>/PA-<slug>.json   — 569 files, one per PA
  catalog/index.json                 — 5,450 lean rows (id, name, tier, owner,
                                       pa, vs, level, parent)

Modes:
  (default)      regenerate the tree, validate, exit 1 on any failure
  --check ROOT   regenerate in memory only, compare byte-for-byte against the
                 shipped tree AND pin catalog/README.md's quick-stats table to
                 the regenerated counts; print CATALOG_TOTALS + BAD| lines;
                 exit 0 iff identical. This is the mode validate-repo.sh
                 Check 71 invokes, so a markdown edit without catalog
                 regeneration fails validation — the Check-71 seventeenth-wave
                 content-mirror doctrine one projection further.

Built-in validation (both modes): one JSON per PA file; 5,450 records
(5,427 + 23); every primary record carries the nine required fields; every
record's tier resolves; index/record id sets equal; README stats pinned.
"""

import importlib.util
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "01-model-company" / "workflows"
OUT = REPO / "catalog"
REQS = REPO / "01-model-company" / "erp-requirements.md"
CLS = SRC / "workflow-criticality-classification.md"

SCHEMA = "erpplans-catalog/1.0"

gen = None  # generate-bpmn module, loaded in build_all (parse/strip_md reuse)

REQUIRED_FIELDS = ("Trigger", "Frequency", "Volume", "Owner", "Participants")
REQUIRED_SECTIONS = ("System Touchpoints", "Time Estimate", "Pain Points / Risks")

HDR_LEVEL = re.compile(r"^(#{2,4}) (W\d+[A-Za-z]?)\. ")
STEPS_TABLE = re.compile(
    r"^\|\s*#\s*\|\s*Activity\s*\|\s*Role \(R\)\s*\|\s*Role \(A\)\s*\|\s*(?:Duration|Frequency|Latency)\s*\|\s*$",
    re.IGNORECASE,
)
W_TOKEN = re.compile(r"\bW\d+[A-Z]?\b")
CTL_TOKEN = re.compile(r"\bCTL-\d+\b")
REQ_TOKEN = re.compile(r"\b[A-Z]{2,4}-\d{1,4}[a-z]?\b")
REQ_ROW = re.compile(r"^\| ([A-Z]{2,4}-\d{1,4}[a-z]?) \|")


# ------------------------------------------------------------------ register

def load_tiers():
    """Re-derive the confirmed tier of every register row (5,450 ids).

    Section-context rules (the ones the register itself is built from, and the
    ones that foot exactly to the 1,396 / 3,296 / 758 canon):
      ## Tier N: heading      -> tier context for its curated rows
      ### Tier N Additions    -> tier context across its family H4s
      #### Tier N ...         -> tier context inside the classification passes
      any other ###           -> leaves the pass header context (H4 family
                                 headers inside Additions sections keep it)
    """
    tiers, counts = {}, {"Tier 1": 0, "Tier 2": 0, "Tier 3": 0}
    tier = sub = None
    for line in CLS.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^## Tier ([123]):", line)
        if m:
            tier, sub = f"Tier {m.group(1)}", None
            continue
        if re.match(r"^## ", line):
            tier = sub = None
            continue
        m = re.match(r"^### Tier ([123]) Additions", line)
        if m:
            sub = f"Tier {m.group(1)}"
            continue
        m = re.match(r"^#### Tier ([123])\b", line)
        if m:
            sub = f"Tier {m.group(1)}"
            continue
        if re.match(r"^### ", line):
            sub = None
            continue
        m = re.match(r"^\| (W\d+[A-Za-z]*) \|", line)
        if m:
            t = sub or tier
            assert t, f"register row without tier context: {line[:60]}"
            tiers[m.group(1)] = t
            counts[t] += 1
    assert counts == {"Tier 1": 1396, "Tier 2": 3296, "Tier 3": 758}, counts
    return tiers


def load_req_ids():
    ids = set()
    for line in REQS.read_text(encoding="utf-8").splitlines():
        m = REQ_ROW.match(line)
        if m:
            ids.add(m.group(1))
    assert len(ids) == 728, f"expected 728 requirement ids, found {len(ids)}"
    return ids


# ------------------------------------------------------------------ per-PA

def vs_slug(pa_path: Path) -> str:
    return pa_path.parent.name


def read_vs_name(pa_path: Path) -> str:
    readme = pa_path.parent / "README.md"
    for line in readme.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^# (VS-\d+): (.+?)\s*$", line)
        if m:
            return m.group(2)
    return vs_slug(pa_path)


def pa_header(pa_path: Path):
    for line in pa_path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^# (PA-[\d.]+) — (.+?)\s*$", line)
        if m:
            return m.group(1), m.group(2)
    raise AssertionError(f"no '# PA-<id> — <title>' H1 in {pa_path.name}")


def header_levels(pa_path: Path):
    levels = {}
    for line in pa_path.read_text(encoding="utf-8").splitlines():
        m = HDR_LEVEL.match(line)
        if m:
            levels[m.group(2)] = len(m.group(1))
    return levels


def split_blocks(pa_path: Path):
    """Same block split parse_pa_file uses: (id, name, lines) per W-header,
    stopping at the next W-header, the next ## heading, or the PA footer."""
    blocks, current = [], None
    for line in pa_path.read_text(encoding="utf-8").splitlines():
        m = gen.WF_HEADER.match(line)
        if m:
            if current:
                blocks.append(current)
            current = {"id": m.group(2), "name": m.group(3), "lines": []}
        elif current is not None:
            if re.match(r"^## (?!#)", line) or line.startswith("*Workflow Count"):
                blocks.append(current)
                current = None
            else:
                current["lines"].append(line)
    if current:
        blocks.append(current)
    return blocks


def capture_steps(lines):
    """Superset of the BPMN parser's steps capture: same canonical 5-column
    table header, but ANY step-id form in the first column (W525's 'CS-1' …
    prefixed ids are silently dropped by generate-bpmn.py's bare-digit rule —
    rows the catalog must not lose). The id is kept verbatim as 'n'."""
    steps, in_table = [], False
    for raw in lines:
        line = raw.rstrip("\n")
        if STEPS_TABLE.match(line.replace("\\|", "\x00")):
            in_table = True
            continue
        if in_table:
            stripped = line.strip().replace("\\|", "\x00")
            if stripped.startswith("|"):
                cells = [c.strip() for c in stripped.strip("|").split("|")]
                if len(cells) >= 5 and not re.fullmatch(r"[-\s]*", cells[0] or "-"):
                    steps.append({
                        "n": cells[0],
                        "activity": cells[1],
                        "r": gen.strip_md(cells[2]) or "Unassigned",
                        "a": gen.strip_md(cells[3]) or "—",
                        "duration": gen.strip_md(cells[4]) or "—",
                    })
                continue
            in_table = False
    return steps


def refs_of(text: str, self_id: str, req_ids: set):
    w_refs = sorted({t for t in W_TOKEN.findall(text) if t != self_id})
    ctl_refs = sorted(set(CTL_TOKEN.findall(text)))
    req_refs = sorted({t for t in REQ_TOKEN.findall(text) if t in req_ids})
    return w_refs, ctl_refs, req_refs


def build_pa_doc(pa_path: Path, tiers, req_ids):
    pa_id, pa_title = pa_header(pa_path)
    levels = header_levels(pa_path)
    text = pa_path.read_text(encoding="utf-8")
    vs_name = read_vs_name(pa_path)

    records = []
    for block in split_blocks(pa_path):
        wid, name, lines = block["id"], block["name"], block["lines"]
        parsed = gen.parse_workflow_block(lines)
        my_steps = capture_steps(lines)
        level = levels[wid]
        flat = "\n".join(
            [f"{wid}. {name}"]
            + [f"{k}: {v}" for k, v in parsed["fields"].items()]
            + [f"{s['n']}|{s['activity']}|{s['r']}|{s['a']}|{s['duration']}" for s in my_steps]
            + [f"{s}: " + " ; ".join(v) for s, v in sorted(parsed["sections"].items())]
        )
        w_refs, ctl_refs, req_refs = refs_of(flat, wid, req_ids)
        rec = {
            "id": wid,
            "name": name,
            "level": level,
            "tier": tiers.get(wid),
            "parent": None,
            "fields": parsed["fields"],
            "steps": my_steps,
            "sections": {k: v for k, v in sorted(parsed["sections"].items())},
            "ctl_refs": ctl_refs,
            "w_refs": w_refs,
            "req_refs": req_refs,
        }
        records.append(rec)

    # parent linkage: a sub-workflow (level > 2) belongs to the nearest
    # preceding primary (level == 2) record
    last_primary = None
    for rec in records:
        if rec["level"] == 2:
            last_primary = rec["id"]
        else:
            rec["parent"] = last_primary

    return {
        "schema": SCHEMA,
        "source": str(pa_path.relative_to(REPO)),
        "value_stream": {
            "id": pa_path.parent.name.split("-")[0]
            + "-"
            + pa_path.parent.name.split("-")[1],
            "name": vs_name,
            "directory": vs_slug(pa_path),
        },
        "process_area": {"id": pa_id, "title": pa_title},
        "workflows": records,
    }


def validate_pa_doc(doc, pa_path, bad):
    """Presence is validated at the FAMILY level (primary + its direct
    sub-workflows) — the corpus's own umbrella convention: '## W2' holds only
    its children (### W2A/B/C carry the fields), and '## W22' shares its
    System Touchpoints / Time Estimate sections with '### W22A'. A primary
    passes when the union of the family carries the nine required fields;
    per-record JSON stays faithful to what each block actually holds."""
    prim = [w for w in doc["workflows"] if w["level"] == 2]
    children = {}
    for w in doc["workflows"]:
        if w["parent"]:
            children.setdefault(w["parent"], []).append(w)

    def has_section(prefix, keys):
        return any(k == prefix or k.startswith(prefix + " (") for k in keys)

    for w in prim:
        fam = [w] + children.get(w["id"], [])
        union_fields = {}
        union_sections = set()
        any_steps = False
        for m in fam:
            union_fields.update(m["fields"])
            union_sections.update(m["sections"])
            any_steps = any_steps or bool(m["steps"])
        miss = [f for f in REQUIRED_FIELDS if f not in union_fields]
        miss += [s for s in REQUIRED_SECTIONS if not has_section(s, union_sections)]
        if not any_steps and not has_section("Steps", union_sections):
            miss.append("Steps")
        if miss:
            bad.append(f"{pa_path.name}: {w['id']} missing required: {', '.join(miss)}")
    for w in doc["workflows"]:
        if w["tier"] is None:
            bad.append(f"{pa_path.name}: {w['id']} has no register tier")
        if w["level"] > 2 and not w["parent"]:
            bad.append(f"{pa_path.name}: sub-workflow {w['id']} has no parent")
    return len(prim), len(doc["workflows"]) - len(prim), sum(len(w["steps"]) for w in doc["workflows"])


# ------------------------------------------------------------------ emission

def dump(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=1, sort_keys=True) + "\n"


def build_all():
    """Parse the corpus; return (pa_docs, index_doc, stats). No I/O to OUT."""
    global gen
    gen = _load_bpmn_gen()
    tiers = load_tiers()
    req_ids = load_req_ids()
    bad = []
    pa_files = sorted(SRC.glob("VS-*/PA-*.md"))
    docs, index_rows = [], []
    n_prim = n_subs = n_steps = 0
    for pa in pa_files:
        doc = build_pa_doc(pa, tiers, req_ids)
        p, s, st = validate_pa_doc(doc, pa, bad)
        n_prim += p
        n_subs += s
        n_steps += st
        for w in doc["workflows"]:
            index_rows.append({
                "id": w["id"], "name": w["name"], "tier": w["tier"],
                "owner": w["fields"].get("Owner"),
                "level": w["level"], "parent": w["parent"],
                "pa": doc["process_area"]["id"], "pa_title": doc["process_area"]["title"],
                "vs": doc["value_stream"]["directory"], "vs_name": doc["value_stream"]["name"],
            })
        docs.append((pa, doc))

    ids = [r["id"] for r in index_rows]
    if len(ids) != len(set(ids)):
        bad.append("duplicate workflow ids across the corpus")
    if len(docs) != len(pa_files):
        bad.append("PA doc count mismatch")
    stats = {
        "pa_files": len(pa_files),
        "records": len(index_rows),
        "primary": n_prim,
        "subs": n_subs,
        "steps": n_steps,
        "tiers": {t: sum(1 for r in index_rows if r["tier"] == t)
                  for t in ("Tier 1", "Tier 2", "Tier 3")},
    }
    if (stats["primary"], stats["subs"]) != (5427, 23):
        bad.append(f"record split {stats['primary']}+{stats['subs']} != 5427+23")
    index_doc = {
        "schema": SCHEMA,
        "generated_by": "07-methodology/generate-catalog.py",
        "counts": stats,
        "workflows": sorted(index_rows, key=lambda r: (r["level"], r["id"])),
    }
    return docs, index_doc, stats, bad


def rel_json_path(pa_path: Path) -> Path:
    return OUT / vs_slug(pa_path) / (pa_path.stem + ".json")


def write_tree(docs, index_doc):
    written = set()
    for pa, doc in docs:
        out = rel_json_path(pa)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(dump(doc), encoding="utf-8")
        written.add(out)
    (OUT / "index.json").write_text(dump(index_doc), encoding="utf-8")
    written.add(OUT / "index.json")
    return written


# ------------------------------------------------------------------ check

def check(docs, index_doc, stats, bad):
    """--check: byte-compare the regeneration against the shipped tree and pin
    the README quick-stats. Never writes."""
    for pa, doc in docs:
        out = rel_json_path(pa)
        if not out.exists():
            bad.append(f"missing: {out.relative_to(REPO)}")
            continue
        if out.read_text(encoding="utf-8") != dump(doc):
            bad.append(f"stale (differs from regeneration): {out.relative_to(REPO)}")
    idx = OUT / "index.json"
    if not idx.exists():
        bad.append("missing: catalog/index.json")
    elif idx.read_text(encoding="utf-8") != dump(index_doc):
        bad.append("stale (differs from regeneration): catalog/index.json")
    for p in sorted(OUT.rglob("*.json")):
        if p not in {rel_json_path(pa) for pa, _ in docs} and p != idx:
            bad.append(f"unexpected file: {p.relative_to(REPO)}")
    bad += pin_readme(stats)
    return bad


def pin_readme(stats):
    """catalog/README.md's Quick-Stats table must quote the regenerated counts
    (the hand-maintained README pattern of bpmn/ and dmn/, pinned the
    Check-74 way but inside the generator so --check covers it)."""
    readme = OUT / "README.md"
    if not readme.exists():
        return ["missing: catalog/README.md"]
    text = readme.read_text(encoding="utf-8")
    bad = []
    pins = {
        "PA JSON files": f"{stats['pa_files']}",
        "workflow records": f"{stats['records']:,}",
        "primary workflows": f"{stats['primary']:,}",
        "sub-workflows": f"{stats['subs']}",
        "step rows": f"{stats['steps']:,}",
        "Tier 1 records": f"{stats['tiers']['Tier 1']:,}",
        "Tier 2 records": f"{stats['tiers']['Tier 2']:,}",
        "Tier 3 records": f"{stats['tiers']['Tier 3']:,}",
    }
    for label, want in pins.items():
        m = re.search(r"\| " + re.escape(label) + r" \| ([\d,]+) \|", text)
        if not m:
            bad.append(f"catalog/README.md: no quick-stats row for '{label}'")
        elif m.group(1) != want:
            bad.append(f"catalog/README.md: '{label}' quotes {m.group(1)}, "
                       f"regeneration holds {want}")
    return bad


# ------------------------------------------------------------------ main

def main() -> int:
    global REPO, SRC, OUT, CLS, REQS
    check_only = "--check" in sys.argv
    roots = [a for a in sys.argv[1:] if not a.startswith("--")]
    root = Path(roots[0]).resolve() if roots else REPO
    if root != REPO:
        REPO = root
        SRC = REPO / "01-model-company" / "workflows"
        OUT = REPO / "catalog"
        CLS = SRC / "workflow-criticality-classification.md"
        REQS = REPO / "01-model-company" / "erp-requirements.md"
    if not (REPO / "07-methodology" / "generate-bpmn.py").exists():
        print("CATALOG_TOTALS errors=1")
        print(f"BAD|{REPO} is not an erpplans checkout (no 07-methodology/generate-bpmn.py)")
        return 1

    docs, index_doc, stats, bad = build_all()

    if check_only:
        bad = check(docs, index_doc, stats, bad)
    else:
        if bad:
            print("CATALOG_TOTALS errors=%d" % len(bad))
            for b in bad:
                print("BAD|" + b)
            return 1
        write_tree(docs, index_doc)
        stale = check(docs, index_doc, stats, [])
        assert not stale, stale

    print(f"CATALOG_TOTALS files={stats['pa_files']} records={stats['records']} "
          f"primary={stats['primary']} subs={stats['subs']} steps={stats['steps']} "
          f"errors={len(bad)}")
    for b in bad:
        print("BAD|" + b)
    return 1 if bad else 0


def _load_bpmn_gen():
    spec = importlib.util.spec_from_file_location(
        "_genbpmn", REPO / "07-methodology" / "generate-bpmn.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


if __name__ == "__main__":
    sys.exit(main())
