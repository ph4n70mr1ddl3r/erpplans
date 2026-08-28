#!/usr/bin/env python3
"""
finalize-time-estimates.py — Finalize the mechanical draft `### Time Estimate` sections.

`backfill-time-estimate.py` (2026-06-21) closed the Time-Estimate field gap by emitting,
for each workflow then missing the section, a bullet list of the workflow's own per-step
Durations plus an explicit draft marker ("Draft roll-up from per-step Durations … refine
to the per-step range + annual figure house style"). 407 of those drafts were still
pending finalization. This tool completes them WITHOUT inventing domain content: every
figure is derived from the workflow's own authored fields —

  * the per-occurrence roll-up sums the workflow's own per-step Durations
    (ranges summed low+low / high+high);
  * per-unit Durations ("15 min/store") are scaled only when the workflow's own
    Volume field carries a count for that unit ("tested in 10–20 stores"), and the
    scaling is shown explicitly;
  * the annual figure multiplies the roll-up by an occurrence count taken from the
    Frequency (explicit "N–M …/year" / "N×/year" forms and "every N–M years"
    renewals) — bare cadence words (monthly/weekly/daily) are NOT auto-multiplied,
    because per-step Durations of a mixed-cadence workflow may already carry their
    own cadence in the Activity prose (e.g. W624's weekly dashboard review inside a
    monthly-cycle workflow); those cases are adjudicated via the decisions file;
  * steps whose Duration marks them as elapsed-time, automated/negligible, or
    cross-referenced are reported, not summed.

Output is one house-style paragraph per workflow (the WORKFLOW-FORMAT-GUIDE form:
per-occurrence figure + scaling math + annual figure "where it drives headcount"),
replacing the draft bullets (which duplicated the Steps table) and the draft marker.

Pipeline:
    --workbench FILE   dump the adjudication workbench (one compact record per draft;
                       auto-decides the unambiguous cases, flags the rest)
    --apply FILE       render final paragraphs from a decisions JSON (workbench records
                       edited/extended with an "occ" field where auto is null) and write
    --check            exit 1 if any draft remains

Idempotent: only sections still carrying the draft marker are touched.
"""
import argparse, glob, json, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKFLOWS = os.path.join(REPO, "01-model-company", "workflows")
DRAFT_MARKER = "*Draft roll-up from per-step Durations"

BLOCK_SPLIT = re.compile(r"(?=^## W\d+[A-Z]?\. )", re.MULTILINE)

NUM = r"(\d[\d,]*(?:\.\d+)?)"
RANGE = r"(?:\u2013|\u2014|-|to)"

EFFORT_RE = re.compile(
    r"^~?\s*" + NUM + r"\s*(?:" + RANGE + r"\s*" + NUM + r"\s*)?"
    r"(hours?|hrs?|minutes?|mins?|seconds?|secs?)\b\s*"
    r"((?:/[A-Za-z][A-Za-z-]*|per [A-Za-z][A-Za-z-]*)*)\s*(?:\([^)]*\))?\s*$",
    re.I,
)
# mixed-unit ranges: "30 min–1 hour", "45 min - 2 hours"
MIXED_RANGE_RE = re.compile(
    r"^~?\s*" + NUM + r"\s*(?:minutes?|mins?)\s*" + RANGE + r"\s*" + NUM + r"\s*(hours?|hrs?)\s*(?:\([^)]*\))?\s*$",
    re.I,
)
ELAPSED_RE = re.compile(
    r"^~?\s*" + NUM + r"\s*(?:" + RANGE + r"\s*" + NUM + r"\s*)?"
    r"(days?|weeks?|months?)\b\s*"
    r"((?:/[A-Za-z][A-Za-z-]*|per [A-Za-z][A-Za-z-]*)*)\s*(?:\([^)]*\))?\s*$",
    re.I,
)
# cadence-only durations: the column carries a cadence/trigger, not an effort figure
CADENCE_ONLY_RE = re.compile(
    r"^(?:as needed|as-required|ongoing|continuous(?: during [a-z ]+)?|event-driven|variable|varies"
    r"|periodic|monthly|quarterly|semi-?annual(?:ly)?|annual(?: review)?|weekly|daily|per campaign"
    r"|per account|per transaction|per settlement|per change|per study|per assessment|per incident"
    r"|per event|per case|per project|per occurrence|per recall event|on dispute|on event"
    r"|on request|at board meeting|at reporting date|at project completion|at month-?end"
    r"|at year-?end|board meeting|overnight|campaign duration|vendor-dependent|pre-configured"
    r"|during (?:the )?(?:annual|quarterly|monthly|weekly|daily) [a-z ]+|during [a-z ]+ season"
    r"|full shift|continuous \(72h\)|per steps? [\d–-]+|see (?:the )?(?:above|below))$", re.I)
NEGLIGIBLE_RE = re.compile(r"^~?\s*<\s*\d+\s*(seconds?|secs?|sec|minutes?|mins?)\b", re.I)
NON_EFFORT_RE = re.compile(
    r"automat|non-?effort|^n/?a$|^\u2014$|^—$|absorbed|immediate|negligible|^none\b|"
    r"vendor-side|system-driven|no manual", re.I)
CROSSREF_RE = re.compile(r"^per (W\d|steps?|process|the above)|^see W\d", re.I)

TEMPORAL = {"week", "wk", "month", "mo", "day", "year", "yr", "quarter", "qtr",
            "bi-weekly", "biweekly", "semi-monthly", "semiweekly"}

PER_YEAR = {"week": 52.0, "wk": 52.0, "month": 12.0, "mo": 12.0, "day": 365.0,
            "year": 1.0, "yr": 1.0, "quarter": 4.0, "qtr": 4.0,
            "bi-weekly": 26.0, "biweekly": 26.0, "semi-monthly": 24.0, "semiweekly": 26.0}

DRAFT_SECTION = re.compile(
    r"(### Time Estimate\n)((?:- Step [\d.a-z]+: .*\n)+)(- \*Draft roll-up[^\n]*\*\n?)")

# Cadence markers in Activity prose that make a workflow mixed-cadence (its steps'
# Durations cannot all be read as per-occurrence effort).
CADENCE_PROSE = re.compile(
    r"\b(monthly|weekly|daily|quarterly|annually|annual|per week|per month|per day|"
    r"per quarter|per year|every week|every month|each month|each week|/week|/month)\b", re.I)


def num(s):
    return float(s.replace(",", ""))


def fmt_hours(minutes):
    if minutes < 60:
        v, unit = minutes, "min"
    else:
        v, unit = minutes / 60.0, "hours"
    if v == int(v):
        v = int(v)
    elif v < 10:
        v = round(v, 2)
    elif v < 100:
        v = round(v, 1)
    else:
        v = round(v)
    if isinstance(v, float) and v == int(v):
        v = int(v)
    s = f"{v:,}" if isinstance(v, int) else (f"{v:,.2f}".rstrip("0").rstrip(".") if v < 10 else f"{v:,.1f}")
    return f"{s} {unit}" if v != 1 else f"{s} {unit.rstrip('s')}"


def fmt_year(hours):
    v = round(hours) if hours >= 100 else (round(hours, 2) if hours < 10 else round(hours, 1))
    if isinstance(v, float) and v == int(v):
        v = int(v)
    s = f"{v:,}" if isinstance(v, int) else (f"{v:,.2f}".rstrip("0").rstrip(".") if v < 10 else f"{v:,.1f}")
    return f"{s} hours/year"


def _range(lo_hi_text):
    """'15.6 hours'–'31.2 hours' → '15.6–31.2 hours' (unit stated once)."""
    lo, hi = lo_hi_text
    ml, mh = re.match(r"([\d,.]+) (.*)", lo), re.match(r"([\d,.]+) (.*)", hi)
    if ml and mh and ml.group(2) == mh.group(2):
        return f"{ml.group(1)}–{mh.group(1)} {ml.group(2)}"
    return f"{lo}–{hi}"


def fmt_dur(lo, hi):
    return fmt_hours(lo) if lo == hi else _range((fmt_hours(lo), fmt_hours(hi)))


def fmt_days(lo, hi):
    def weeks(d):
        w = d / 7.0
        w = round(w) if w >= 10 else round(w, 1)
        if isinstance(w, float) and w == int(w):
            w = int(w)
        return f"{w:,} weeks" if w != 1 else "1 week"

    def num_only(d, in_weeks):
        if in_weeks:
            w = d / 7.0
            w = round(w) if w >= 10 else round(w, 1)
            if isinstance(w, float) and w == int(w):
                w = int(w)
            return f"{w:,}", ("weeks" if w != 1 else "week")
        v = round(d) if d >= 10 else (int(d) if d == int(d) else round(d, 1))
        return f"{v:,}", ("days" if v != 1 else "day")
    in_weeks = hi >= 14  # one unit across the range
    if lo == hi:
        n, u = num_only(lo, in_weeks)
        return f"{n} {u}"
    nlo, ulo = num_only(lo, in_weeks)
    nhi, uhi = num_only(hi, in_weeks)
    return f"{nlo}–{nhi} {ulo}"


def fmt_num(v):
    v = round(v) if v >= 100 else v
    if v == int(v):
        return f"{int(v):,}"
    return f"{round(v, 1):,}"


def parse_duration(d):
    d = d.strip()
    m = MIXED_RANGE_RE.match(d)
    if m:
        lo_m, hi_m = num(m.group(1)), num(m.group(2)) * 60.0
        return {"kind": "effort", "verbatim": d, "lo": lo_m, "hi": hi_m}
    m = EFFORT_RE.match(d)
    if m:
        lo, hi, unit, quals = num(m.group(1)), num(m.group(2) or m.group(1)), m.group(3).lower(), m.group(4) or ""
        mins = 1.0 / 60.0 if unit.startswith("s") else (1.0 if unit.startswith("min") else 60.0)
        lo_m, hi_m = lo * mins, hi * mins
        quals = [q.lower().replace("per ", "", 1) for q in re.split(r"/|\bper ", quals.strip()) if q]
        if len(quals) > 1:
            return {"kind": "unparsed", "verbatim": d}  # per-X-per-Y composites: author by hand
        if quals and quals[0] in TEMPORAL:
            return {"kind": "recurring", "verbatim": d, "lo": lo_m, "hi": hi_m, "qual": quals[0]}
        if quals:
            return {"kind": "per-unit", "verbatim": d, "lo": lo_m, "hi": hi_m, "unit": quals[0]}
        return {"kind": "effort", "verbatim": d, "lo": lo_m, "hi": hi_m}
    m = ELAPSED_RE.match(d)
    if m:
        lo, hi, unit, quals = num(m.group(1)), num(m.group(2) or m.group(1)), m.group(3).lower(), m.group(4) or ""
        quals = [q.lower().replace("per ", "", 1) for q in re.split(r"/|\bper ", quals.strip()) if q]
        if quals:
            # "1 day/month", "1–2 weeks/store": elapsed at its own cadence/unit —
            # report verbatim, never sum into a per-occurrence timeline
            return {"kind": "cadence", "verbatim": d}
        days = {"day": 1.0, "wee": 7.0, "mon": 30.0}[unit[:3]]
        return {"kind": "elapsed", "verbatim": d, "lo": lo * days, "hi": hi * days}
    if CADENCE_ONLY_RE.match(d):
        return {"kind": "cadence", "verbatim": d}
    if NEGLIGIBLE_RE.match(d) or NON_EFFORT_RE.search(d):
        return {"kind": "excluded", "verbatim": d}
    if CROSSREF_RE.match(d):
        return {"kind": "crossref", "verbatim": d}
    return {"kind": "unparsed", "verbatim": d}


def volume_count(volume, unit):
    if not volume:
        return None
    plural = unit + "s"
    # allow one adjective word between the count and the noun ("20–30 store visits")
    m = re.search(NUM + r"\s*" + RANGE + r"\s*" + NUM + r"\s+(?:[A-Za-z][A-Za-z-]*\s+)?" + plural + r"\b", volume, re.I)
    if m:
        return num(m.group(1)), num(m.group(2))
    m = re.search(NUM + r"\s+(?:[A-Za-z][A-Za-z-]*\s+)?" + plural + r"\b", volume, re.I)
    if m:
        v = num(m.group(1))
        return v, v
    return None


def freq_counts_unit(freq, unit):
    """True when the Frequency field counts occurrences of exactly this unit noun
    ("~20–40 safety complaints/month" for unit 'complaint') — then a per-unit
    Duration ("30 min/complaint") is simply this workflow's per-occurrence effort."""
    if not freq:
        return False
    plural = unit + "s"
    return bool(re.search(NUM + r"\s*(?:" + RANGE + r"\s*" + NUM + r"\s*)?(?:[A-Za-z][A-Za-z-]*\s+)?"
                          + plural + r"\b", freq, re.I))


def parse_frequency(freq):
    """(occ_lo, occ_hi, explicit) from Frequency; explicit=False for bare cadence words."""
    f = " ".join((freq or "").split())
    fl = f.lower()
    if not fl:
        return None
    if re.search(r"per store\b", fl):
        return None

    def rng(pat, mult=1.0):
        m = re.search(pat, fl)
        if m:
            lo, hi = num(m.group(1)), num(m.group(2) if m.re.groups > 1 and m.group(2) else m.group(1))
            return lo * mult, hi * mult
        return None

    for pat, mult in [
        (r"(?<![\d,.])(\d+)\s*[\u00d7x]\s*/?\s*yea", 1.0),
        (NUM + r"\s*" + RANGE + r"\s*" + NUM + r"[^,;|]{0,40}?\s*(?:/\s*yea|per year|a year)", 1.0),
        (r"(?<![\d,.])" + NUM + r"\s*(?:\+)?\s*(?:\u2026|\.\.\.)?\s*[^,;|/]{0,40}?\s*(?:/\s*yea|per year)", 1.0),
        (NUM + r"\s*" + RANGE + r"\s*" + NUM + r"[^,;|]{0,40}?\s*(?:/\s*mon|per month)", 12.0),
        (r"(?<![\d,.])" + NUM + r"\s*(?:\+)?\s*(?:\u2026|\.\.\.)?\s*[^,;|/]{0,40}?\s*(?:/\s*mon|per month)", 12.0),
        (NUM + r"\s*" + RANGE + r"\s*" + NUM + r"[^,;|]{0,40}?\s*(?:/\s*wk|/\s*week|per week)", 52.0),
        (r"(?<![\d,.])" + NUM + r"\s*(?:\+)?\s*(?:\u2026|\.\.\.)?\s*[^,;|/]{0,40}?\s*(?:/\s*wk|/\s*week|per week)", 52.0),
        (NUM + r"\s*" + RANGE + r"\s*" + NUM + r"[^,;|]{0,40}?\s*(?:/\s*qtr|/\s*quar|per quarter)", 4.0),
        (r"(?<![\d,.])" + NUM + r"\s*(?:\+)?\s*(?:\u2026|\.\.\.)?\s*[^,;|/]{0,40}?\s*(?:/\s*day|per day)", 365.0),
    ]:
        m = rng(pat, mult)
        if m:
            return m[0], m[1], True
    m = re.search(r"every\s*" + NUM + r"\s*(?:" + RANGE + r"|\s+to\s+)" + NUM + r"\s*years?", fl)
    if m:
        lo, hi = num(m.group(1)), num(m.group(2))
        return 1.0 / hi, 1.0 / lo, True
    m = re.search(r"every\s*" + NUM + r"\s*years?", fl)
    if m:
        n = num(m.group(1))
        return 1.0 / n, 1.0 / n, True
    if re.search(r"semi-?annual|twice (?:a|per) year", fl):
        return 2.0, 2.0, False
    if re.search(r"(?<!semi-)annual(ly)?\b|once a year|yearly|1\s*[\u00d7x]\s*/?\s*yea", fl):
        return 1.0, 1.0, False
    if re.search(r"monthly|per month|/month", fl):
        return 12.0, 12.0, False
    if re.search(r"weekly|per week|/week", fl):
        return 52.0, 52.0, False
    if re.search(r"quarterly|per quarter", fl):
        return 4.0, 4.0, False
    if re.search(r"daily|per day|every day|each day", fl):
        return 365.0, 365.0, False
    return None


def compact(v):
    v = re.sub(r"\s*\([^)]*\)", "", v).strip()
    return re.sub(r"^~\s*", "~", v)


def short(text, n=70):
    text = " ".join(text.split())
    if len(text) <= n:
        return text
    t = text[: n - 1].rstrip(" ,;") + "…"
    # never ship a fragment with unbalanced parens (truncation inside a parenthetical)
    while t.count("(") > t.count(")"):
        t = t[: t.rfind("(")].rstrip(" ,;") + "…"
    return t


def extract_drafts():
    """Yield one record per remaining draft Time Estimate."""
    out = []
    for f in sorted(glob.glob(os.path.join(WORKFLOWS, "VS-*", "PA-*.md"))):
        text = open(f, encoding="utf-8", errors="replace").read()
        for m in DRAFT_SECTION.finditer(text):
            head, body = m.group(1), m.group(2)
            block_start = text.rfind("## W", 0, m.start())
            wline_end = text.index("\n", block_start)
            wid = re.match(r"## (W\d+[A-Z]?)\.", text[block_start:wline_end]).group(1)
            wblock = text[block_start:m.end()]
            fm = re.search(r"\|\s*\*\*Frequency\*\*\s*\|\s*(.+?)\s*\|", wblock)
            vm = re.search(r"\|\s*\*\*Volume\*\*\s*\|\s*(.+?)\s*\|", wblock)
            durs = [re.match(r"^- Step ([\d.a-z]+): (.+)$", ln) for ln in body.split("\n") if ln.startswith("- Step ")]
            # steps table rows for activity prose (cadence markers live there)
            steps_m = re.search(r"^### Steps\s*\n(.*?)(?=^### |^---|^## |\Z)", wblock, re.M | re.S)
            activities = {}
            if steps_m:
                for line in steps_m.group(1).split("\n"):
                    rm = re.match(r"^\|\s*([\d.]+[a-z]?)\s*\|", line)
                    if rm:
                        activities[rm.group(1)] = line
            steps = []
            for dm in durs:
                sid, dur = dm.group(1), dm.group(2)
                act = activities.get(sid, "")
                prose = re.sub(r"[|]", " ", act)[:180]
                steps.append({"n": sid, "dur": dur, "act": " ".join(prose.split())[:150]})
            out.append({
                "file": os.path.relpath(f, REPO), "wid": wid,
                "freq": fm.group(1) if fm else "", "vol": vm.group(1) if vm else "",
                "steps": steps,
            })
    return out


def auto_decide(rec):
    """Propose a decision for the unambiguous cases; else flag with reasons.

    Decision schema: {"occ": [lo, hi] or null, "occ_basis": str, "mode": "auto"}.
    Auto is allowed only when every Duration reads as per-occurrence effort (or is
    benignly reportable: elapsed / recurring-rate / cadence-only / automated) and the
    Frequency yields an occurrence count in the same unit — or the workflow is
    honestly event-driven with a quantified per-occurrence figure.
    """
    kinds = [parse_duration(s["dur"]) for s in rec["steps"]]
    flags = []
    n_effort = sum(1 for k in kinds if k and k["kind"] == "effort")
    n_elapsed = sum(1 for k in kinds if k and k["kind"] == "elapsed")
    n_recurring = sum(1 for k in kinds if k and k["kind"] == "recurring")
    quantifiable = n_effort + n_elapsed + n_recurring
    if quantifiable == 0:
        flags.append("no quantifiable duration — author by hand")

    per_units = [k for k in kinds if k and k["kind"] == "per-unit"]
    for k in per_units:
        if freq_counts_unit(rec["freq"], k["unit"]):
            continue  # per-occurrence effort of this very occurrence unit — safe to auto
        if volume_count(rec["vol"], k["unit"]):
            # a Volume-scaled per-unit step totals ACROSS the volume (50–100 accounts),
            # which must not then be multiplied by the Frequency's occurrence count
            # (W812: per-account effort × escalation-event count overstated 10×)
            flags.append("volume-scaled per-unit duration needs occurrence-unit adjudication: " + k["verbatim"])
        # unscaled per-unit steps are only reported at their own unit — safe to auto
    unparsed = [k["verbatim"] for k in kinds if k and k["kind"] == "unparsed"]
    if unparsed:
        flags.append("unparsed durations: " + ", ".join(unparsed)[:150])
    # cadence markers in Activity prose: steps may carry their own cadence in prose,
    # so the Duration column cannot be read as uniformly per-occurrence
    cad_steps = [s["n"] for s, k in zip(rec["steps"], kinds)
                 if k and k["kind"] in ("effort",) and CADENCE_PROSE.search(s["act"])]
    if cad_steps:
        flags.append("cadence words in step prose: " + "; ".join(cad_steps[:6]))

    # a bare cadence is auto-decided only when the Frequency is ONE pure cadence phrase —
    # compounds ("Weekly or as needed", "Daily monitoring; weekly execution",
    # "Annual company-wide; semi-annual for …") change meaning and are authored by hand
    SINGLE_CADENCE = re.compile(
        r"^(?:each |every )?(?:business |calendar )?(?:day|week|month|quarter|half-?year|year"
        r"|daily|weekly|biweekly|monthly|bi-?monthly|quarterly|semi-?annual(?:ly)?|annual(?:ly)?)"
        r"(?:\s*\([^)]*\))?$", re.I)
    freq_core = re.sub(r"\s*\([^)]*\)\s*$", "", rec["freq"] or "").strip()

    occ = parse_frequency(rec["freq"])
    if re.search(r"per store\b", (rec["freq"] or ""), re.I):
        flags.append("per-store frequency — chain math needs authoring")
    elif occ is not None:
        olo, ohi, explicit = occ
        if not explicit:
            if not SINGLE_CADENCE.match(freq_core):
                flags.append("compound/qualified bare cadence — author by hand")
            elif re.search(NUM + r"\s*" + RANGE + r"\s*" + NUM + r"\s+[\w-]+s\s*/\s*(?:month|week|day|year)", rec["vol"] or "", re.I):
                flags.append("bare cadence frequency but Volume carries a cadence-marked occurrence count")
        elif ohi > 500:
            flags.append("high occurrence count (>500/year) — verify occurrence unit by hand")

    if flags:
        return None, flags
    return {"occ": [occ[0], occ[1]] if occ else None, "occ_basis": short(rec["freq"]), "mode": "auto"}, []


def render(rec, decision):
    """Render the final house-style paragraph from a record + decision."""
    if decision.get("text"):
        return decision["text"]
    parts_had_annual = False  # set when a recurring-only render already annualizes
    kinds = [parse_duration(s["dur"]) for s in rec["steps"]]
    efforts = [k for k in kinds if k and k["kind"] == "effort"]
    per_units = [k for k in kinds if k and k["kind"] == "per-unit"]
    recurring = [k for k in kinds if k and k["kind"] == "recurring"]
    cadence = [k for k in kinds if k and k["kind"] == "cadence"]
    elapsed = [k for k in kinds if k and k["kind"] == "elapsed"]
    crossrefs = [k for k in kinds if k and k["kind"] == "crossref"]
    unparsed = [k for k in kinds if k and k["kind"] == "unparsed"]

    scaled, unscaled, as_effort = [], [], []
    for k in per_units:
        if freq_counts_unit(rec["freq"], k["unit"]):
            as_effort.append(k)  # the Frequency counts THIS unit → per-occurrence effort
            continue
        c = volume_count(rec["vol"], k["unit"])
        (scaled if c else unscaled).append((k, c))
    efforts = efforts + as_effort
    per_units = [k for k, _ in scaled + unscaled]

    occ = decision.get("occ")
    occ_basis = decision.get("occ_basis") or short(rec["freq"])
    own = decision.get("own_cadence") or []  # [{lo, hi, per_year, text}] minutes at own cadence

    lo = sum(k["lo"] for k in efforts) + sum(k["lo"] * c[0] for k, c in scaled)
    hi = sum(k["hi"] for k in efforts) + sum(k["hi"] * c[1] for k, c in scaled)
    quantified = bool(efforts or scaled)

    parts = []
    if quantified:
        bits = []
        if efforts:
            lst = " + ".join(compact(k["verbatim"]) for k in efforts[:8])
            if len(efforts) > 8:
                more = len(efforts) - 8
                lst += " + %d further step%s" % (more, "" if more == 1 else "s")
            bits.append("per-step effort " + lst)
        for k, c in scaled:
            bits.append("%s × %s %s ≈ %s" % (
                compact(k["verbatim"]), fmt_num(c[0]) if c[0] == c[1] else fmt_num(c[0]) + "–" + fmt_num(c[1]),
                k["unit"] + ("s" if c[1] != 1 else ""), fmt_dur(k["lo"] * c[0], k["hi"] * c[1])))
        parts.append(fmt_dur(lo, hi) + " per occurrence (" + "; ".join(bits) + ")")
        if unscaled:
            parts.append("plus unit-priced steps at their own unit (" + ", ".join(compact(k["verbatim"]) for k, _ in unscaled) + ")")
    if elapsed:
        el = " + ".join(compact(k["verbatim"]) for k in elapsed[:6]) + (" …" if len(elapsed) > 6 else "")
        if quantified or parts:
            parts.append("elapsed timeline " + el)
        else:
            parts.append(fmt_days(sum(k["lo"] for k in elapsed), sum(k["hi"] for k in elapsed)) + " elapsed per occurrence (" + el + ")")
    if recurring and quantified:
        parts.append("recurring steps at their own cadence (" + ", ".join(compact(k["verbatim"]) for k in recurring[:3])
                     + (" …" if len(recurring) > 3 else "") + ")")
    elif recurring and not quantified and not elapsed:
        # effort lives only in recurring-rate steps — annualize at their own cadence
        ann = []
        for k in recurring:
            per_year = PER_YEAR.get(k["qual"])
            if per_year:
                ann.append((k, k["lo"] * per_year, k["hi"] * per_year))
        if ann:
            alo, ahi = sum(a[1] for a in ann), sum(a[2] for a in ann)
            joined = ", ".join(compact(k["verbatim"]) for k, _lo, _hi in ann[:4]) + (" …" if len(ann) > 4 else "")
            yearly = fmt_hours(alo) if alo == ahi else _range((fmt_hours(alo), fmt_hours(ahi)))
            parts.append("recurring effort " + joined + " ≈ " + yearly + "/year")
            occ = None  # already annualized; don't multiply again
            parts_had_annual = True
    if cadence:
        parts.append("cadence-carried steps as authored (" + ", ".join(compact(k["verbatim"]) for k in cadence[:3])
                     + (" …" if len(cadence) > 3 else "") + ")")
    if crossrefs:
        parts.append("effort per " + " / ".join(k["verbatim"].replace("Per ", "", 1).replace("per ", "", 1) for k in crossrefs[:2]))
    if unparsed:
        parts.append("remaining durations as authored (" + ", ".join(compact(k["verbatim"]) for k in unparsed[:3])
                     + (" …" if len(unparsed) > 3 else "") + ")")
    if own:
        parts.append("own-cadence steps " + "; ".join(o["text"] for o in own))
        occ = None  # annual figure already carried by the own-cadence items

    body = "; ".join(p for p in parts if p)

    if occ and quantified:
        olo, ohi = occ
        occ_txt = fmt_num(olo) if olo == ohi else fmt_num(olo) + "–" + fmt_num(ohi)
        tail = "at " + occ_basis + " ≈ " + occ_txt + " occurrence" + ("s" if ohi != 1 else "") + "/year"
        ylo, yhi = lo / 60.0 * olo, hi / 60.0 * ohi
        tail += " ≈ " + (fmt_year(ylo) if ylo == yhi else _range((fmt_year(ylo), fmt_year(yhi))))
        body += " — " + tail
    elif occ and elapsed and not quantified and not recurring:
        olo, ohi = occ
        occ_txt = fmt_num(olo) if olo == ohi else fmt_num(olo) + "–" + fmt_num(ohi)
        body += " — at " + occ_basis + " ≈ " + occ_txt + " occurrence" + ("s" if ohi != 1 else "") + "/year"
    elif not own and not parts_had_annual:
        body += " — cadence: " + occ_basis + "; annual effort is event-driven (annualize at realized volume)"

    return body + "."


def apply_decisions(decisions, write=True):
    files = {}
    for f in sorted(glob.glob(os.path.join(WORKFLOWS, "VS-*", "PA-*.md"))):
        text = open(f, encoding="utf-8", errors="replace").read()
        if DRAFT_MARKER not in text:
            continue
        out, last, applied = [], 0, 0
        for m in DRAFT_SECTION.finditer(text):
            block_start = text.rfind("## W", 0, m.start())
            wline_end = text.index("\n", block_start)
            wid = re.match(r"## (W\d+[A-Z]?)\.", text[block_start:wline_end]).group(1)
            rec = decisions.get(wid)
            if rec is None:
                continue
            wblock = text[block_start:m.end()]
            fm = re.search(r"\|\s*\*\*Frequency\*\*\s*\|\s*(.+?)\s*\|", wblock)
            vm = re.search(r"\|\s*\*\*Volume\*\*\s*\|\s*(.+?)\s*\|", wblock)
            durs = [dm.group(2) for dm in
                    (re.match(r"^- Step ([\d.a-z]+): (.+)$", ln) for ln in m.group(2).split("\n") if ln.startswith("- Step "))
                    if dm]
            frec = {"file": os.path.relpath(f, REPO), "wid": wid,
                    "freq": fm.group(1) if fm else "", "vol": vm.group(1) if vm else "",
                    "steps": [{"n": dm.group(1), "dur": dm.group(2)} for dm in
                              (re.match(r"^- Step ([\d.a-z]+): (.+)$", ln) for ln in m.group(2).split("\n") if ln.startswith("- Step "))
                              if dm]}
            para = render(frec, rec)
            out.append(text[last:m.start()])
            out.append(m.group(1) + para + "\n")
            last = m.end()
            applied += 1
        out.append(text[last:])
        new = "".join(out)
        if write and applied and new != text:
            open(f, "w", encoding="utf-8").write(new)
        files[os.path.relpath(f, REPO)] = applied
    return files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workbench", metavar="FILE", help="dump adjudication workbench JSON")
    ap.add_argument("--apply", metavar="FILE", help="apply decisions JSON")
    ap.add_argument("--check", action="store_true", help="exit 1 if drafts remain")
    args = ap.parse_args()

    if args.workbench:
        recs = extract_drafts()
        wb = []
        for r in recs:
            dec, flags = auto_decide(r)
            wb.append({**r, "decision": dec, "flags": flags})
        json.dump(wb, open(args.workbench, "w"), indent=1)
        auto = sum(1 for w in wb if w["decision"])
        print(f"workbench: {len(wb)} drafts ({auto} auto-decided, {len(wb) - auto} flagged for authoring) → {args.workbench}")
        fl = [f for w in wb for f in w["flags"]]
        return

    if args.apply:
        decisions = {}
        for w in json.load(open(args.apply)):
            if w.get("decision") or "occ" in w or "text" in w:
                decisions[w["wid"]] = w.get("decision") or w
        res = apply_decisions(decisions)
        n = sum(res.values())
        print(f"finalized {n} draft sections across {len([k for k, v in res.items() if v])} files")

    drafts = extract_drafts()
    print(f"drafts remaining: {len(drafts)}")
    if args.check and drafts:
        sys.exit(1)


if __name__ == "__main__":
    main()
