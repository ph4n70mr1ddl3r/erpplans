#!/usr/bin/env python3
"""
Add Automation Opportunity and Controls fields to all workflows missing them.

Reads each PA file, splits into workflow blocks, and inserts workflow-specific
Automation Opportunity and Controls sections. Content is derived from each
workflow's Steps, System Touchpoints, and Pain Points text.
"""

import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
WORKFLOWS = REPO / "01-model-company" / "workflows"


# ── helpers ────────────────────────────────────────────────────────────

def read_file(path):
    with open(path) as f:
        return f.read()


def write_file(path, text):
    with open(path, 'w') as f:
        f.write(text)


# ── extractors ─────────────────────────────────────────────────────────

def extract_steps(block):
    """Extract step descriptions from the Steps table."""
    m = re.search(r'### Steps\s*\n(.*?)(?=\n### |\n## |\Z)', block, re.DOTALL)
    if not m:
        return []
    steps = []
    for line in m.group(1).split('\n'):
        m2 = re.match(r'\|\s*\d+[a-z]?\s*\|\s*(.+?)\s*\|', line)
        if m2:
            steps.append(m2.group(1).strip())
    return steps


def extract_pain_points(block):
    m = re.search(r'### Pain Points / Risks\s*\n(.*?)(?=\n### |\n## |\Z)', block, re.DOTALL)
    return m.group(1).strip() if m else ""


def extract_touchpoints(block):
    m = re.search(r'### System Touchpoints\s*\n(.*?)(?=\n### |\n## |\Z)', block, re.DOTALL)
    return m.group(1).strip() if m else ""


def extract_owner(block):
    m = re.search(r'\*\*Owner\*\*\s*\|?\s*(.+?)(?:\n|\|)', block)
    return m.group(1).strip() if m else ""


def workflow_name(block):
    m = re.match(r'## (W\d+[A-Za-z]?\. .+)', block)
    return m.group(1).strip() if m else ""


# ── content generators ─────────────────────────────────────────────────

MANUAL_VERBS = {
    'enter': 'auto-capture', 'manually': 'auto-capture', 'scan': 'auto-scan',
    'print': 'auto-generate', 'log': 'auto-log', 'record': 'auto-record',
    'document': 'auto-document', 'review': 'auto-review', 'check': 'auto-validate',
    'verify': 'auto-validate', 'validate': 'auto-validate', 'inspect': 'auto-inspect',
    'count': 'auto-count', 'calculate': 'auto-calculate', 'compile': 'auto-compile',
    'prepare': 'auto-generate', 'generate': 'auto-generate', 'create': 'auto-create',
    'file': 'auto-file', 'submit': 'auto-submit', 'send': 'auto-send',
    'notify': 'auto-notify', 'escalate': 'auto-escalate', 'route': 'auto-route',
    'dispatch': 'auto-dispatch', 'schedule': 'auto-schedule', 'assign': 'auto-assign',
    'track': 'auto-track', 'monitor': 'auto-monitor', 'reconcile': 'auto-reconcile',
    'match': 'auto-match', 'approve': 'rule-based auto-approval',
    'authorize': 'rule-based authorization', 'classify': 'auto-classify',
    'categorize': 'auto-categorize', 'allocate': 'auto-allocate',
    'distribute': 'auto-distribute', 'post': 'auto-post', 'update': 'auto-update',
    'sync': 'auto-sync', 'upload': 'auto-upload', 'extract': 'auto-extract',
    'import': 'auto-import', 'export': 'auto-export', 'report': 'auto-report',
    'analyze': 'auto-analyze', 'forecast': 'auto-forecast',
    'detect': 'auto-detect', 'identify': 'auto-identify', 'flag': 'auto-flag',
    'alert': 'auto-alert', 'remind': 'auto-remind', 'contact': 'workflow notification',
    'coordinate': 'workflow orchestration', 'communicate': 'auto-communication',
    'request': 'auto-request', 'collect': 'auto-collect', 'capture': 'auto-capture',
    'measure': 'auto-measure', 'test': 'auto-test', 'audit': 'continuous audit',
    'investigate': 'auto-flag for investigation', 'register': 'auto-register',
    'issue': 'auto-issue', 'renew': 'auto-renew',
    'reject': 'auto-reject outside tolerance',
}
# NOTE: 'approve' intentionally maps to 'rule-based auto-approval' (defined above). A previous
# version had a duplicate 'approve' key ('auto-approve within tolerance') that Python silently
# dropped; the single canonical mapping is retained here.


def _step_summary(step_text, verb, max_len=80):
    """Return a clean, boundary-respecting snippet of a step around `verb`.

    The previous implementation took a fixed +/-2..4 word window that routinely cut off
    mid-phrase (e.g. 'auto-review (account manager reviews application: (a) verify)'),
    producing bullets that fail the quality bar in WORKFLOW-FORMAT-GUIDE.md. This version
    extends to the next sentence/clause boundary (`.`, `;`, `:` followed by space, or a
    closing paren) and trims to max_len on a word boundary, so every emitted bullet is a
    complete, readable phrase.
    """
    s = step_text.strip()
    # prefer the clause containing the verb
    idx = s.lower().find(verb)
    if idx < 0:
        snippet = s
    else:
        # walk forward from the verb to the next boundary
        end = len(s)
        for b in ('. ', '; ', ': ', ')'):
            j = s.find(b, idx)
            if j != -1:
                end = min(end, j + (0 if b == ')' else 1))
        snippet = s[idx:end] if end > idx else s[idx:]
    snippet = snippet.strip().strip(',;:')
    # Strip markdown formatting that would render as stray/broken emphasis when the
    # snippet is re-quoted: bold (**), code spans (`), and stray leading/trailing italics (*).
    # This prevents the 'auto-review of "Review & Planning**"' artifact that arose when a
    # step's bold-marker closer fell inside the captured snippet without its opener.
    snippet = snippet.replace('**', '').replace('`', '').strip('* ')
    # Balance parentheses: the boundary walk may cut at ':'/'.'/';' inside an open paren,
    # leaving a dangling '(T-4 months' fragment. Drop the trailing unbalanced '(' segment
    # (and any leading unmatched ')') so the re-quoted snippet reads as a complete phrase.
    while snippet.count('(') > snippet.count(')'):
        snippet = snippet[:snippet.rfind('(')].rstrip()
    while snippet.count(')') > snippet.count('('):
        snippet = snippet[snippet.find(')') + 1:].lstrip()
    if len(snippet) > max_len:
        snippet = snippet[:max_len].rsplit(' ', 1)[0] + '…'
    return snippet


def generate_automation(steps, touchpoints, pain_points, wf_name, step_numbers=None):
    """Generate workflow-specific Automation Opportunity from step analysis.

    Emits COMPLETE sentences (capitalized, period-terminated) of the form
    'System {auto-action} {step summary} (replaces manual Step N).' These are DRAFT
    opportunities pending human refinement — the quality bar in WORKFLOW-FORMAT-GUIDE.md
    expects a human to sharpen them to the specific module/object/integration. They must
    nonetheless read as sentences, never as broken mid-phrase fragments.
    """
    opportunities = []
    seen = set()
    step_numbers = step_numbers or range(1, len(steps) + 1)

    for n, step in zip(step_numbers, steps):
        step_lower = step.lower()
        for verb, auto in MANUAL_VERBS.items():
            if verb in step_lower and auto not in seen:
                snippet = _step_summary(step, verb)
                if not snippet:
                    continue
                opportunities.append(
                    f"System {auto} of \"{snippet}\" (replaces manual Step {n})."
                )
                seen.add(auto)
                break
        if len(opportunities) >= 3:
            break

    if not opportunities:
        # Derive from touchpoints or workflow name (these are already complete sentences)
        tp = touchpoints.lower()
        name_lower = wf_name.lower()
        if 'integration' in tp or 'api' in tp:
            opportunities.append("Real-time integration with auto-synced source data.")
        if 'report' in tp or 'dashboard' in tp or 'analytics' in name_lower:
            opportunities.append("Auto-generated report with scheduled distribution.")
        if 'approval' in tp or 'workflow' in tp:
            opportunities.append("Rule-based workflow routing with auto-approval within tolerance.")
        if not opportunities:
            opportunities.append(
                "System-driven processing with exception-based manual intervention (draft — refine to the specific module/object)."
            )

    return '\n'.join(f"- {o}" for o in opportunities[:3])


def build_workflow_to_controls():
    """Reverse internal-controls-matrix.md into {workflow_base_id: [(CTL-XX, objective), ...]}.

    Lazy-loaded and cached. Returns {} if the matrix is unavailable so generation still
    produces a (boilerplate) Controls line rather than failing.
    """
    cache = getattr(build_workflow_to_controls, "_cache", None)
    if cache is not None:
        return cache
    from collections import defaultdict
    # REPO is the repository root (parent of 07-methodology/); the matrix lives under
    # 01-model-company/. See module-level REPO/WORKFLOWS definitions.
    matrix = REPO / "01-model-company" / "internal-controls-matrix.md"
    wf_to_ctl = defaultdict(list)
    if matrix.exists():
        ctl_obj = {}
        for line in open(matrix, encoding="utf-8"):
            m = re.match(r"^\|\s*(CTL-\d+)\s*\|\s*(.+?)\s*\|\s*[PD]\s*\|", line)
            if not m:
                continue
            cid, obj = m.group(1), m.group(2).strip().rstrip(";").strip()
            ctl_obj[cid] = obj
            for tok in re.findall(r"W\d+[A-Z]?(?:\.\d+[a-z]?)?", line):
                base = re.match(r"(W\d+[A-Z]?)", tok).group(1)
                wf_to_ctl[base].append((cid, obj))
    build_workflow_to_controls._cache = wf_to_ctl
    return wf_to_ctl


def generate_controls(pain_points, wf_name, steps, owner, wf_id=None):
    """Generate Controls from CTL-XX mapping, pain-point mitigations, and step patterns.

    Preference order: (1) explicit CTL-XX references from the internal-controls matrix
    for this workflow id (the auditable, traceable source); (2) mitigating controls named
    in the pain points ('mitigated by …'); (3) a step-pattern-derived operational control.
    The CTL-XX branch is what closes the loop with the 67-control register; without a
    mapping the output is a clearly-labelled draft.
    """
    controls = []

    # (1) CTL-XX mapping from the controls register (authoritative)
    if wf_id:
        wf_to_ctl = build_workflow_to_controls()
        refs = wf_to_ctl.get(wf_id)
        if refs:
            seen, parts = set(), []
            for cid, obj in refs:
                if cid in seen:
                    continue
                seen.add(cid)
                o = obj[:90].rstrip('.') + '.'
                parts.append(f"{cid} ({o[0].lower() + o[1:]})")
            controls.append("- " + "; ".join(parts))

    # (2) Extract mitigating controls from pain points
    if pain_points:
        for line in pain_points.split('\n'):
            m = re.search(r'mitigated by\s+(.+?)(?:[.;]|$)', line, re.IGNORECASE)
            if m:
                ctrl = m.group(1).strip()
                if len(ctrl) > 5 and f"operational: {ctrl}" not in controls:
                    controls.append(f"operational: {ctrl}")

    # (3) Derive from step patterns
    if len(controls) < 2:
        has_approval = any('approv' in s.lower() or 'review' in s.lower() for s in steps)
        has_reconcile = any('reconcil' in s.lower() for s in steps)
        if has_approval and has_reconcile:
            controls.append(f"operational: {owner or 'designated role'} review-and-approval gate; periodic reconciliation against source documents")
        elif has_approval:
            controls.append(f"operational: {owner or 'designated role'} review and approval gate")
        elif has_reconcile:
            controls.append("operational: periodic reconciliation against source documents")
        if len(controls) < 2:
            controls.append("operational: standard operating procedures; system-enforced validation rules")

    return '\n'.join(controls[:4])


# ── insertion logic ────────────────────────────────────────────────────

def has_automation(block):
    return '### Automation Opportunity' in block


def has_controls(block):
    return '### Controls\n' in block or '### Controls\r' in block


def insert_fields(block):
    """Insert Automation Opportunity and Controls after Pain Points, or after Steps if no PP."""
    steps = extract_steps(block)
    touchpoints = extract_touchpoints(block)
    pain_points = extract_pain_points(block)
    owner = extract_owner(block)
    wf_name = workflow_name(block)
    wf_id_match = re.match(r'W\d+[A-Z]?', wf_name)
    wf_id = wf_id_match.group(0) if wf_id_match else None

    auto_text = generate_automation(steps, touchpoints, pain_points, wf_name)
    ctrl_text = generate_controls(pain_points, wf_name, steps, owner, wf_id=wf_id)
    insertion = f"\n### Automation Opportunity\n{auto_text}\n\n### Controls\n{ctrl_text}\n\n"

    # Strategy 1: Insert after Pain Points section
    pp_hdr = re.search(r'^### Pain Points / Risks\s*$', block, re.MULTILINE)
    if pp_hdr:
        all_hdrs = list(re.finditer(r'^### .+$', block, re.MULTILINE))
        pp_idx = next((i for i, h in enumerate(all_hdrs) if 'Pain Points' in h.group()), None)
        if pp_idx is not None and pp_idx + 1 < len(all_hdrs):
            pos = all_hdrs[pp_idx + 1].start()
            return block[:pos] + insertion + block[pos:]

    # Strategy 2: Insert after Steps table (before next workflow separator '---' or '## W')
    steps_hdr = re.search(r'### Steps\s*\n', block)
    if steps_hdr:
        after = block[steps_hdr.end():]
        # Find the end of the Steps TABLE: the last '|' row before a blank line + '---' or next header
        # We find all table rows (lines starting with '|') and take the last one before a non-table line
        lines = after.split('\n')
        last_table_line = -1
        in_table = False
        for i, line in enumerate(lines):
            if line.startswith('|'):
                in_table = True
                last_table_line = i
            elif in_table and line.strip() == '':
                # End of table found
                break
        if last_table_line >= 0:
            # Insert after the last table row
            # Count characters up to and including that line
            char_pos = sum(len(l) + 1 for l in lines[:last_table_line + 1])
            pos = steps_hdr.end() + char_pos
            return block[:pos] + '\n' + insertion + block[pos:]

    return block


# ── file processor ─────────────────────────────────────────────────────

def process_file(filepath):
    content = read_file(filepath)
    original = content

    # Split into blocks on '## W' workflow headers
    raw_blocks = re.split(r'(?=^## W\d+[A-Za-z]?\. )', content, flags=re.MULTILINE)
    if len(raw_blocks) <= 1:
        return False

    modified = False
    new_blocks = [raw_blocks[0]]

    for block in raw_blocks[1:]:
        if has_automation(block) and has_controls(block):
            new_blocks.append(block)
        else:
            new_block = insert_fields(block)
            if new_block != block:
                modified = True
            new_blocks.append(new_block)

    if modified:
        write_file(filepath, ''.join(new_blocks))
        return True
    return False


# ── main ────────────────────────────────────────────────────────────────

def main():
    files = sorted(WORKFLOWS.glob("VS-*/PA-*.md"))
    total = len(files)
    updated = 0
    skipped = 0
    errors = []

    for i, f in enumerate(files, 1):
        try:
            if process_file(f):
                updated += 1
                print(f"[{i}/{total}] UPDATED: {f.name}")
            else:
                skipped += 1
        except Exception as e:
            errors.append((f.name, str(e)))
            print(f"[{i}/{total}] ERROR: {f.name} — {e}")

    print(f"\n=== Done ===")
    print(f"Total files: {total}")
    print(f"Updated: {updated}")
    print(f"Skipped (already have both): {skipped}")
    if errors:
        print(f"Errors: {len(errors)}")
        for name, err in errors:
            print(f"  {name}: {err}")


if __name__ == "__main__":
    main()
