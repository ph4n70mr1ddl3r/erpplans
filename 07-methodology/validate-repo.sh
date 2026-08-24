#!/bin/bash
# validate-repo.sh — Cross-reference validation for BuildRight Depot ERP Plans
# Checks consistency of workflow counts, requirement IDs, cross-references, and table structure

set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ERRORS=0
WARNINGS=0

RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
NC='\033[0m'

error() { echo -e "${RED}ERROR${NC}: $1"; ERRORS=$((ERRORS + 1)); }
warn()  { echo -e "${YELLOW}WARN${NC}: $1"; WARNINGS=$((WARNINGS + 1)); }
ok()    { echo -e "${GREEN}OK${NC}: $1"; }

echo "=== BuildRight Depot ERP Plans — Validation ==="
echo ""

# --- Check 1: Workflow IDs in PA files that are NOT in criticality classification ---
echo "--- Check 1: Unclassified workflow headers ---"
# Primary workflows are ## (h2) headers; a small number of ### (h3) parent/summary
# sub-workflows (e.g. W9A) also receive their own classification row. The documented
# unclassified total = grand_total − classified table rows, used consistently repo-wide.
# We (a) report that documented figure and (b) verify every classified ID resolves to a
# real workflow header in a PA file (catching stale classification references).
CLASSIFIED=$(grep -oP '^\| (W\d+[A-Z]?) \|' "$REPO_ROOT"/01-model-company/workflows/workflow-criticality-classification.md | sed -E 's/^\| //;s/ \|$//' | sort -u)
CLASSIFIED_COUNT=$(echo "$CLASSIFIED" | grep -cP '^W' || true)
# Grand-total cell is comma-formatted (e.g. "4,596"); strip commas before arithmetic.
GRAND_TOTAL=$(grep 'Grand Total' "$REPO_ROOT"/01-model-company/workflows/value-stream-index.md | grep -oP '\d[\d,]*' | tail -1 | tr -d ',')
DOC_UNCLASS=$((GRAND_TOTAL - CLASSIFIED_COUNT))

ALL_HEADERS=$(grep -rohP '^#{2,3} W\d+[A-Z]?\.' "$REPO_ROOT"/01-model-company/workflows/VS-*/*.md 2>/dev/null | sed -E 's/^#{2,3} //;s/\.$//' | sort -u)
STALE_CLASSIFIED=$(comm -23 <(echo "$CLASSIFIED") <(echo "$ALL_HEADERS") | grep -cP '^W' || true)
SUB_CLASSIFIED=$(comm -12 <(grep -rohP '^### W\d+[A-Z]?\.' "$REPO_ROOT"/01-model-company/workflows/VS-*/*.md 2>/dev/null | sed -E 's/^### //;s/\.$//' | sort -u) <(echo "$CLASSIFIED") | grep -cP '^W' || true)

echo "  Classified register rows: $CLASSIFIED_COUNT (incl. $SUB_CLASSIFIED parent/summary sub-workflow rows → $((CLASSIFIED_COUNT - SUB_CLASSIFIED)) unique workflows classified) | Grand total (unique workflows): $GRAND_TOTAL"

if [ "$STALE_CLASSIFIED" -eq 0 ]; then
    ok "All $CLASSIFIED_COUNT classified workflow IDs resolve to a header in a PA file"
else
    error "$STALE_CLASSIFIED classified ID(s) do not match any workflow header in PA files"
fi

if [ "$DOC_UNCLASS" -gt 0 ]; then
  PROPOSED_FILE="$REPO_ROOT"/01-model-company/workflows/workflow-criticality-proposed.md
  # Real unclassified = ## headers not present in the confirmed register
  UNCLASSIFIED_IDS=$(comm -23 <(echo "$ALL_HEADERS") <(echo "$CLASSIFIED") | grep -P '^W' || true)
  UNCLASSIFIED_COUNT=$(echo "$UNCLASSIFIED_IDS" | grep -cP '^W' || true)
  if [ -f "$PROPOSED_FILE" ]; then
    PROPOSED_IDS=$(grep -oP '^\| W\d+[A-Z]? \|' "$PROPOSED_FILE" | sed -E 's/^\| //;s/ \|//' | sort -u)
    PROPOSED_COUNT=$(echo "$PROPOSED_IDS" | grep -cP '^W' || true)
    WITHOUT_PROPOSAL=$(comm -23 <(echo "$UNCLASSIFIED_IDS") <(echo "$PROPOSED_IDS") | grep -cP '^W' || true)
    warn "$UNCLASSIFIED_COUNT workflows remain unclassified in the confirmed register; $PROPOSED_COUNT have a keyword-driven proposed tier (workflow-criticality-proposed.md); $WITHOUT_PROPOSAL have no proposal yet"
    PROPOSED_DANGLING=$(comm -23 <(echo "$PROPOSED_IDS") <(echo "$ALL_HEADERS") | grep -cP '^W' || true)
    PROPOSED_DUP=$(comm -12 <(echo "$PROPOSED_IDS") <(echo "$CLASSIFIED") | grep -cP '^W' || true)
    if [ "$PROPOSED_DANGLING" -eq 0 ] && [ "$PROPOSED_DUP" -eq 0 ]; then
      ok "All $PROPOSED_COUNT proposed IDs resolve to headers and do not duplicate the confirmed register"
    else
      error "Proposed classification: $PROPOSED_DANGLING dangling, $PROPOSED_DUP duplicate(s) of confirmed register"
    fi
  else
    warn "$UNCLASSIFIED_COUNT workflows remain unclassified (pending criticality review)"
  fi
fi

# --- Check 2: Workflow counts per PA file match value-stream-index ---
echo "--- Check 2: PA workflow counts ---"
PA_FILES=$(find "$REPO_ROOT"/01-model-company/workflows -name "PA-*.md" -type f 2>/dev/null)
while IFS= read -r pafile; do
    HEADER_COUNT=$(grep -cP '^## W\d+[A-Z]?\.' "$pafile" 2>/dev/null || true)
    PA_NAME=$(basename "$pafile" .md)
    VS_NAME=$(basename "$(dirname "$pafile")")
    INDEX_COUNT=$(grep -P "\\Q$PA_NAME\\E" "$REPO_ROOT"/01-model-company/workflows/value-stream-index.md 2>/dev/null | grep -oP '\d+ workflows' | grep -oP '\d+' || echo "0")
    if [ "$HEADER_COUNT" != "$INDEX_COUNT" ] && [ "$INDEX_COUNT" != "0" ]; then
        warn "$VS_NAME/$PA_NAME: file has $HEADER_COUNT workflow headers, index says $INDEX_COUNT"
    fi
done <<< "$PA_FILES"
ok "PA workflow count checks complete"

# --- Check 3: Cross-reference key figures ---
echo "--- Check 3: Key figure consistency ---"
# Check total workflows in value-stream-index (cell is comma-formatted, e.g. "4,596")
TOTAL_VS=$(grep 'Grand Total' "$REPO_ROOT"/01-model-company/workflows/value-stream-index.md | grep -oP '\d[\d,]*' | tail -1 | tr -d ',')
README_TOTAL=$(grep -oP '1,\d{3}' "$REPO_ROOT"/README.md | head -1)
if [ -n "$TOTAL_VS" ]; then
    ok "Value stream index total: $TOTAL_VS workflows"
else
    error "Could not find grand total in value-stream-index.md"
fi

# Check requirement count
REQ_COUNT=$(grep -cP '^\| [A-Z]+-\d+' "$REPO_ROOT"/01-model-company/erp-requirements.md 2>/dev/null || true)
echo "  Requirements found in erp-requirements.md: $REQ_COUNT"

# Check controls count
CTL_COUNT=$(grep -cP '^\| CTL-' "$REPO_ROOT"/01-model-company/internal-controls-matrix.md 2>/dev/null || true)
echo "  Controls found in internal-controls-matrix.md: $CTL_COUNT"

# --- Check 4: Requirement IDs in matrix vs erp-requirements ---
echo "--- Check 4: Requirement-Workflow matrix consistency ---"
# Match only requirement IDs that begin a table row (|^REQ-XX |) so day-offset tokens
# like "T-7"/"T-14" or "VS-49" in footer prose are not mistaken for requirement IDs.
MATRIX_REQS=$(grep -ohP '^\| [A-Z]{2,}-\d+[a-z]? \|' "$REPO_ROOT"/01-model-company/requirement-workflow-matrix.md | sed -E 's/^\| //;s/ \|$//' | sort -u | wc -l)
REQ_DEFINED=$(grep -cP '^\| [A-Z]+-\d+' "$REPO_ROOT"/01-model-company/erp-requirements.md 2>/dev/null || true)
echo "  Requirement IDs in matrix table rows: $MATRIX_REQS | defined in erp-requirements.md: $REQ_DEFINED"

# --- Check 5: Empty process areas ---
echo "--- Check 5: Empty process areas ---"
EMPTY=$(grep -r "no workflows yet" "$REPO_ROOT"/01-model-company/workflows/ --include="*.md" 2>/dev/null || true)
if [ -z "$EMPTY" ]; then
    ok "No empty process areas found"
else
    warn "Empty process areas found:"
    echo "$EMPTY"
fi

# --- Check 6: W-numbers in requirement-workflow matrix that don't exist in PA files ---
echo "--- Check 6: Matrix workflow references ---"
# Include letter-suffixed sub-workflow IDs (W<number><letter>) via the [A-Z]? qualifier
MATRIX_WFS=$(grep -ohP '\bW\d{1,4}[A-Z]?\b' "$REPO_ROOT"/01-model-company/requirement-workflow-matrix.md | sort -u)
PA_ALL=$(grep -ohP '\bW\d{1,4}[A-Z]?\b' "$REPO_ROOT"/01-model-company/workflows/VS-*/*.md | sort -u)
MISSING=$(comm -23 <(echo "$MATRIX_WFS") <(echo "$PA_ALL") | head -20)
MISSING_COUNT=$(comm -23 <(echo "$MATRIX_WFS") <(echo "$PA_ALL") | wc -l)
if [ "$MISSING_COUNT" -le 5 ]; then
    ok "Only $MISSING_COUNT matrix W-references not found in PA files (parent/summary workflows)"
else
    warn "$MISSING_COUNT W-numbers in requirement-workflow matrix not found in PA file headers"
    echo "  First 10: $(echo "$MISSING" | head -10 | tr '\n' ' ')"
fi

# --- Check 7: Dangling workflow references in cross-reference docs ---
echo "--- Check 7: Dangling workflow references ---"
# All workflow IDs actually defined as a header (## or ###) in any PA file
DEFINED_WFS=$(grep -rohP '^#{2,3} W\d+[A-Z]?\.' "$REPO_ROOT"/01-model-company/workflows/VS-*/*.md 2>/dev/null | sed -E 's/^#{2,3} //;s/\.$//' | sort -u)
DANGLING_TOTAL=0
for doc in \
  "$REPO_ROOT"/01-model-company/workflows/workflow-dependency-map.md \
  "$REPO_ROOT"/01-model-company/workflows/workflow-system-touchpoint-map.md \
  "$REPO_ROOT"/01-model-company/requirement-workflow-matrix.md \
  "$REPO_ROOT"/01-model-company/internal-controls-matrix.md; do
  REFS=$(grep -ohP '\bW\d{1,4}[A-Z]?\b' "$doc" 2>/dev/null | sort -u)
  DANGLING=$(comm -23 <(echo "$REFS") <(echo "$DEFINED_WFS") | grep -P '^W' || true)
  DANGLING_COUNT=$(echo "$DANGLING" | grep -cP '^W' || true)
  DANGLING_TOTAL=$((DANGLING_TOTAL + DANGLING_COUNT))
  if [ "$DANGLING_COUNT" -eq 0 ]; then
    ok "$(basename "$doc"): no dangling workflow references"
  else
    error "$(basename "$doc"): $DANGLING_COUNT dangling workflow reference(s): $(echo "$DANGLING" | tr '\n' ' ')"
  fi
done

# --- Check 11: Dependency-map Tier-1 chain claims must be classified as Tier 1 ---
echo "--- Check 11: Dependency-map deepest-chain Tier-1 consistency ---"
# The dependency map declares a 'deepest dependency chain (all Tier 1)' with a stated
# total. Two reverse checks: (a) the count of unique workflow IDs in that block must
# equal the stated total; (b) every workflow in that block must be present in the
# Tier 1 section of the classification file. This catches drift like a Tier-1-claimed
# workflow that was never classified (regression that Check 1 cannot detect, because
# Check 1 only proves classified -> header, not dependency-claim -> classified).
DEPMAP="$REPO_ROOT"/01-model-company/workflows/workflow-dependency-map.md
TIER1_CHAIN=$(awk '/### Tier 1: Deepest Dependency Chain/{f=1;next} f&&/^### /{exit} f' "$DEPMAP" | grep -oP '\bW\d+[A-Z]?\b' | sort -u)
TIER1_CHAIN_COUNT=$(echo "$TIER1_CHAIN" | grep -cP '^W' || true)
STATED_TOTAL=$(grep -oP 'deepest dependency chain \(all Tier 1\)|Total\*\*: \K\d+(?= workflows in the deepest dependency chain)' "$DEPMAP" | head -1)
TIER1_SECTION=$(awk '/^## Tier 1: Core Operations/{f=1;next} f&&/^## Tier 2:/{f=0} f' "$REPO_ROOT"/01-model-company/workflows/workflow-criticality-classification.md)
TIER1_SECTION="$TIER1_SECTION\n$(awk '/^### Tier 1 Additions/{f=1;next} f&&/^### /{exit} f' "$REPO_ROOT"/01-model-company/workflows/workflow-criticality-classification.md)"
CHAIN_NOT_CLASSIFIED=$(echo "$TIER1_CHAIN" | while IFS= read -r w; do
  [ -n "$w" ] && grep -qP "^\| $w \|" <<< "$TIER1_SECTION" || echo "$w"
done)
CHAIN_NOT_CLASSIFIED_COUNT=$(echo "$CHAIN_NOT_CLASSIFIED" | grep -cP '^W' || true)
if [ -n "$STATED_TOTAL" ] && [ "$STATED_TOTAL" -eq "$TIER1_CHAIN_COUNT" ]; then
  ok "Deepest-chain total ($STATED_TOTAL) matches unique workflow count ($TIER1_CHAIN_COUNT)"
else
  error "Deepest-chain stated total ($STATED_TOTAL) != unique workflow count ($TIER1_CHAIN_COUNT)"
fi
if [ "$CHAIN_NOT_CLASSIFIED_COUNT" -eq 0 ]; then
  ok "All $TIER1_CHAIN_COUNT deepest-chain workflows are classified Tier 1"
else
  error "$CHAIN_NOT_CLASSIFIED_COUNT deepest-chain workflow(s) not classified Tier 1: $(echo "$CHAIN_NOT_CLASSIFIED" | tr '\n' ' ')"
fi

# --- Check 8: Placeholder/skeleton workflow content ---
echo "--- Check 8: Placeholder workflow content ---"
# Detect auto-generated placeholder workflows. Markers (any one indicates a stub):
#   - H1 header starting with "# PA-X.Y](..."  (broken markdown from a failed generator run)
#   - Generic workflow title pattern "Workflow NNNN — N Process N"
#   - Generic trigger "Process trigger"
#   - Generic 3-step body "Execute standard process step"
#   - Generic pain point "Standard operational risks mitigated by procedural controls"
PLACEHOLDER_FILES=$(grep -rlP '^# PA-\d+\.\d+\]\(|Workflow \d+ — \d+ Process \d|\*\*Trigger\*\* \| Process trigger \|Execute standard process step|Standard operational risks mitigated by procedural controls' "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null || true)
PLACEHOLDER_COUNT=$(echo -n "$PLACEHOLDER_FILES" | grep -cP 'PA-' || true)

if [ "$PLACEHOLDER_COUNT" -eq 0 ]; then
    ok "No placeholder/skeleton workflow files detected"
else
    error "$PLACEHOLDER_COUNT PA file(s) contain placeholder workflow content:"
    echo "$PLACEHOLDER_FILES" | sed 's/^/    /' | head -20
fi

# --- Check 9: Grand total in value-stream-index matches actual PA file count ---
echo "--- Check 9: Grand total vs actual workflow count ---"
# Grand-total cell is comma-formatted (e.g. "4,596"); strip commas before comparison.
GRAND_TOTAL=$(grep 'Grand Total' "$REPO_ROOT"/01-model-company/workflows/value-stream-index.md | grep -oP '\d[\d,]*' | tail -1 | tr -d ',')
ACTUAL_WFS=$(grep -rhP '^## W\d+[A-Z]?\.' "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null | wc -l)
if [ "$GRAND_TOTAL" = "$ACTUAL_WFS" ]; then
    ok "Grand total ($GRAND_TOTAL) matches actual PA workflow header count ($ACTUAL_WFS)"
else
    error "Grand total ($GRAND_TOTAL) does NOT match actual PA workflow header count ($ACTUAL_WFS)"
fi

# --- Check 10: Boilerplate analysis fields (regression guard) ---
echo "--- Check 10: Boilerplate analysis fields ---"
# The Expansion block (VS-53..VS-78) was originally generated from a template whose three
# value-delivering analysis fields — Pain Points, System Touchpoints, and Time Estimate — were
# verbatim boilerplate copied across every workflow. A 2026-06-20 rework rewrote all 22
# templated value streams to workflow-specific content, so this check now passes; it is
# retained as a regression guard that surfaces any boilerplate reintroduced by a future
# generation artifact. See WORKFLOW-FORMAT-GUIDE.md "Quality bar for the three analysis fields".
BP_MARKER='Operational variability mitigated by standard procedures and system controls'
BP_FILES=$(grep -rlF "$BP_MARKER" "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null || true)
BP_INSTANCES=$(grep -rhF "$BP_MARKER" "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null | wc -l | tr -d ' ' || true)
if [ "$BP_INSTANCES" -eq 0 ]; then
    ok "No boilerplate analysis fields detected"
else
    BP_FILE_COUNT=$(echo -n "$BP_FILES" | grep -cP 'PA-' || true)
    BP_VS_LIST=$(echo "$BP_FILES" | sed -E 's#.*/(VS-[0-9]+-[^/]+)/.*#\1#' | sort -u)
    BP_VS_COUNT=$(echo -n "$BP_VS_LIST" | grep -cP '^VS-' || true)
    warn "$BP_INSTANCES workflows across $BP_FILE_COUNT PA files in $BP_VS_COUNT value streams use verbatim boilerplate for Pain Points / System Touchpoints / Time Estimate (regression — the 2026-06-20 Expansion-block rework removed all known boilerplate; see WORKFLOW-FORMAT-GUIDE.md):"
    echo "$BP_VS_LIST" | sed 's/^/    /'
fi

# --- Check 12: Automation Opportunity + Controls field adoption ---
echo "--- Check 12: Automation Opportunity & Controls field adoption ---"
# Per WORKFLOW-FORMAT-GUIDE.md these are now standard analysis fields for any fully-detailed
# workflow. Each should appear as an ### subsection under its workflow. Adoption is tracked
# (not enforced as an error) so progress across the Core, Statutory, and early gap-analysis
# (VS-89–VS-132) blocks — which predate these fields — can be measured against the VS-73
# reference implementation.
TOTAL_WF=$(grep -rhP '^## W\d+[A-Z]?\.' "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null | wc -l | tr -d ' ')
AUTO_COUNT=$(grep -rohP '^### Automation Opportunity$' "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null | wc -l | tr -d ' ')
CTRL_COUNT=$(grep -rohP '^### Controls$' "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null | wc -l | tr -d ' ')
if [ "$AUTO_COUNT" -eq "$TOTAL_WF" ] && [ "$CTRL_COUNT" -eq "$TOTAL_WF" ]; then
    ok "Automation Opportunity and Controls headers are present on all $TOTAL_WF workflows (100% presence — content quality tracked by Check 21)"
else
    warn "Automation Opportunity present on $AUTO_COUNT / $TOTAL_WF workflows ($(awk "BEGIN{printf \"%.0f\", ($AUTO_COUNT/$TOTAL_WF)*100}")%); Controls present on $CTRL_COUNT / $TOTAL_WF workflows ($(awk "BEGIN{printf \"%.0f\", ($CTRL_COUNT/$TOTAL_WF)*100}")%). Target: 100% on all workflows (see WORKFLOW-FORMAT-GUIDE.md 'Standard analysis fields')"
    echo "  Note: Check W641–W647 formatting in VS-19 if any are missing or deviate from the standard '###' header structure."
fi

# --- Check 13: Markdown table structural integrity ---
echo "--- Check 13: Markdown table structural integrity ---"
# Two regressions that silently garble rendered tables without breaking any plain-text count
# elsewhere in this script:
#  (a) a table data row whose opening '|' is preceded by whitespace (e.g. '  | [VS-136]...')
#      shifts every column right by one — this corrupted 27 value-stream-index.md architecture
#      rows in the gap-analysis block before detection. Repo convention: every table row starts
#      at column 0 with '|'.
#  (b) within a table, a data row whose unescaped-pipe count differs from the header row
#      (missing/extra trailing pipe, a step number merged into the description cell, or an
#      unescaped '|' inside a cell). '\|' is treated as a literal escaped pipe, per CommonMark.
SUMMARY_DOCS="$REPO_ROOT/README.md $REPO_ROOT/01-model-company/*.md $REPO_ROOT/01-model-company/workflows/*.md $REPO_ROOT/07-methodology/*.md"
LEADING_WS=$(grep -rlP '^ +\|' $SUMMARY_DOCS 2>/dev/null || true)
LEADING_WS_COUNT=$(echo -n "$LEADING_WS" | grep -cP '\.md' || true)
if [ "$LEADING_WS_COUNT" -eq 0 ]; then
    ok "No table rows with leading whitespace before the opening '|' (column-shift risk)"
else
    error "$LEADING_WS_COUNT doc(s) have table rows with leading whitespace before '|' (column-shift risk):"
    echo "$LEADING_WS" | sed 's/^/    /'
fi
COL_MISMATCH=$(awk '
FNR==1{intable=0;hdr=0;prev=""}
function ncells(s){ t=s; gsub(/\\[|]/,"",t); return gsub(/[|]/,"",t)-1 }
{
  if ($0 ~ /^[|]/) {
    if ($0 ~ /^\|[[:space:]:|-]+\|$/) { hdr=ncells(prev); intable=1; next }
    if (intable) { c=ncells($0); if(hdr>0 && c!=hdr) printf "%s:%d header=%d row=%d: %.50s\n",FILENAME,FNR,hdr,c,$0 }
    prev=$0; next
  }
  intable=0; hdr=0; prev=""
}' $SUMMARY_DOCS 2>/dev/null)
COL_MISMATCH_COUNT=$(echo -n "$COL_MISMATCH" | grep -cP ':' || true)
if [ "$COL_MISMATCH_COUNT" -eq 0 ]; then
    ok "All summary-doc table rows match their header column count"
else
    error "$COL_MISMATCH_COUNT summary-doc table row(s) have a column count differing from their header:"
    echo "$COL_MISMATCH" | sed 's/^/    /' | head -20
fi

# --- Check 14: Templated doubled-word pain-point labels ("X-risk risk") ---
echo "--- Check 14: Templated doubled-word pain-point labels ---"
# A content-generation artifact left 12 Pain Points bullets of the form
#   - **<Word>-risk risk**: ...
# across the gap-analysis block (VS-99/107/114/116/121/123/130/135): the template appended
# the noun "risk" after a descriptor that already ended in "-risk". The sibling bullets in
# every affected file use the form "**<compound-modifier> risk**:" (e.g. "Strategy-misalignment
# risk"), so this regex catches the drift unambiguously with no false positives (proper nouns
# like the Philippine "Build Build Build" program are excluded by the required "-risk risk"
# / " risk risk" suffix). Scans every PA file's bold pain-point label.
DOUBLED_RISK=$(grep -rnP '\*\*[A-Za-z][A-Za-z-]*[- ]risk risk\b' "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null || true)
DOUBLED_RISK_COUNT=$(echo -n "$DOUBLED_RISK" | grep -cP 'PA-' || true)
if [ "$DOUBLED_RISK_COUNT" -eq 0 ]; then
    ok "No templated '**X-risk risk**' pain-point labels detected"
else
    error "$DOUBLED_RISK_COUNT PA file(s) contain a templated '**<word>-risk risk**' pain-point label:"
    echo "$DOUBLED_RISK" | sed 's/^/    /' | head -20
fi

# --- Check 15: Analysis-field header canonicalization ---
echo "--- Check 15: Analysis-field header canonicalization ---"
# WORKFLOW-FORMAT-GUIDE.md canonicalizes the analysis subsection headers. This check guards the
# three that have NO legitimate variant form in the repo, so the Check 12 adoption counts stay
# trustworthy and the typo/synonym class cannot recur undetected:
#   '### Automation Opportunity'  — guarded (a 2026-06-20 review found 8 VS-161 '### Automation Option' typos)
#   '### Controls'                — guarded
#   '### Pain Points / Risks'     — guarded (a 2026-06-20 review found 2 VS-10 '### Risks & Exceptions' synonyms)
# NOT guarded: '### Steps', '### System Touchpoints', '### Time Estimate', '### Cross-references' — these have
# legitimate parenthetically-qualified sub-forms (e.g. '### System Touchpoints (Yard)') used as per-sub-area
# labels inside complex workflows; normalizing them would create duplicate headers and destroy semantics.
BAD_AUTO=$(grep -rnP '^### Automation(?! Opportunity$)' "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null || true)
BAD_CTRL=$(grep -rnP '^### Control(?!s$)' "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null || true)
BAD_RISK=$(grep -rnP '^### .*Risk' "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null | grep -vP '### Pain Points / Risks( \(|$)' || true)
BAD_COUNT=$(echo -n "$BAD_AUTO"$'\n'"$BAD_CTRL"$'\n'"$BAD_RISK" | grep -cP 'PA-' || true)
if [ "$BAD_COUNT" -eq 0 ]; then
    ok "All Automation/Controls/Pain-Points analysis-field headers use the canonical exact form"
else
    error "$BAD_COUNT non-canonical analysis-field header(s) (should be '### Automation Opportunity' / '### Controls' / '### Pain Points / Risks') — invisible to Check 12's adoption count:"
    echo "$BAD_AUTO" | sed 's/^/    /' | head -20
    echo "$BAD_CTRL" | sed 's/^/    /' | head -20
    echo "$BAD_RISK" | sed 's/^/    /' | head -20
fi

# --- Check 16: PA file footer format ---
echo "--- Check 16: PA file footer format ---"
# WORKFLOW-FORMAT-GUIDE.md and the established convention (493+ PA files) require every PA file to
# END with the standardized navigation footer:
#   *Workflow Count: N · Back to **[VS-NN: <Name>](./README.md)** · [Value Stream Index](../value-stream-index.md)*
# A 2026-06-20 review found 30 PA files in VS-168–VS-177 (Pass 21–25) that deviated — 18 had a
# simpler '*Back to [VS-NN README]*' footer and 12 had NO footer at all — and 50 Core-block files
# (VS-01–VS-31) with duplicate (2–3) mid-file footer lines from a generation artifact. This check
# flags any PA whose last non-empty line is not the standardized footer, so the format cannot drift.
BAD_FOOTER=$(for pafile in "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md; do
  last=$(grep -vE '^[[:space:]]*$' "$pafile" | tail -1)
  echo "$last" | grep -qP '^\*Workflow Count: \d+ · Back to \*\*\[VS-\d+: .+\]\(\./README\.md\)\*\* · \[Value Stream Index\]\(\.\./value-stream-index\.md\)\*$' || echo "$pafile"
done)
BAD_FOOTER_COUNT=$(echo -n "$BAD_FOOTER" | grep -cP 'PA-' || true)
if [ "$BAD_FOOTER_COUNT" -eq 0 ]; then
    ok "All PA files end with the standardized navigation footer"
else
    error "$BAD_FOOTER_COUNT PA file(s) do not end with the standardized footer (*Workflow Count: N · Back to... · Value Stream Index*):"
    echo "$BAD_FOOTER" | sed 's#.*/workflows/##' | sed 's/^/    /' | head -20
fi

# --- Check 17: Orphan workflow bodies (ghost workflows) ---
echo "--- Check 17: Orphan workflow bodies (ghost workflows) ---"
# A ghost workflow is a complete workflow body (Trigger/Owner/Steps table) sitting inside a ## W
# block with NO introducing ### header — neither a '### W<num><letter>.' sub-workflow header nor
# a named narrative sub-process header (e.g. '### IC Invoice Dispute Resolution'). Legitimate
# multi-Trigger workflows always introduce each extra body with a ### header, so an orphan
# Trigger table (one whose nearest preceding header is a field-section header like '### Steps'
# or another field table) signals a workflow whose ## W header was lost in generation — making
# it invisible to every count, the index, the classification, and the dependency map.
# A 2026-06-20 scan found exactly one: VS-12 PA-12.2 W1376 (a 'Tool Rental Reservation, Waitlist
# & Scheduling' body). Reported as a WARN (not ERROR): the fix requires allocating a new W-number
# and updating the 4,980 grand total + index + classification + cross-reference docs — a
# substantive change with cascading impacts, not a mechanical normalization.
GHOST=$(python3 - "$REPO_ROOT" <<'PY'
import os,re,sys
ROOT=sys.argv[1]+"/01-model-company/workflows"
FIELD={'### Steps','### System Touchpoints','### Pain Points / Risks','### Time Estimate','### Cross-references','### Controls','### Automation Opportunity','### Staffing Implication','### Background'}
def is_field_section(h):
    return re.sub(r' \(.*$','',h) in FIELD
out=[]
for d in sorted(os.listdir(ROOT)):
    if not d.startswith("VS-"): continue
    for f in sorted(os.listdir(f"{ROOT}/{d}")):
        if not (f.startswith("PA-") and f.endswith(".md")): continue
        last=None; cur=None; tc=0
        for ln in open(f"{ROOT}/{d}/{f}").read().split("\n"):
            if re.match(r'^## W\d+[A-Z]?\. ', ln): cur=ln; tc=0; last=ln; continue
            if re.match(r'^### ', ln): last=ln; continue
            if '| **Trigger** |' in ln:
                tc+=1
                if tc==1: continue
                if last is None or is_field_section(last.strip()):
                    out.append(f"{d}/{f}: orphan Trigger table inside {cur[:55]}")
print("\n".join(out))
PY
)
GHOST_COUNT=$(echo -n "$GHOST" | grep -cP 'PA-' || true)
if [ "$GHOST_COUNT" -eq 0 ]; then
    ok "No orphan workflow bodies (ghost workflows) detected"
else
    warn "$GHOST_COUNT orphan workflow body/bodies (Trigger table with no introducing ### header — a workflow missing its ## W header; invisible to counts/index/classification; needs W-number allocation to fix):"
    echo "$GHOST" | sed 's/^/    /'
fi

# --- Check 18: Criticality-classification prose counts vs headings ---
echo "--- Check 18: Criticality-classification prose counts vs headings ---"
# validate-repo.sh's table-row checks (Check 1, 9) and the §Summary table proved trustworthy, but
# the file's free-prose counts drifted: across six 2026-06-20 classification batches (v7.19→v7.25)
# the per-tier body sentence 'These <N> workflows ...' under each '## Tier N: ... (M Workflows)'
# heading froze at the v7.19 counts (440/499/229 = 1,168) while the headings correctly advanced to
# 684/1,354/402 (= 2,440); the intro banner likewise held stale '2,684 unclassified (4,981 − 2,297)'
# against a correct 2,564. Both contradicted the file's own Summary table. A table-row check cannot
# see prose, so this check asserts the two stable prose invariants the Summary already encodes:
#   (a) each tier heading's '(M Workflows)' == that section's 'These <N> workflows' sentence, and
#   (b) the intro-banner arithmetic 'X unclassified = grand_total − classified' is self-consistent
# and matches the §Summary totals. Errors here mean a future classification batch updated the
# Summary table but forgot the surrounding prose — the exact v7.19→v7.25 regression.
CLASS_FILE="$REPO_ROOT"/01-model-company/workflows/workflow-criticality-classification.md
PROSE_DRIFT=$(python3 - "$CLASS_FILE" <<'PY'
import re,sys
f=open(sys.argv[1]).read()
lines=f.split("\n")
errs=[]
# (a) heading count vs 'These N workflows' body sentence
for i,ln in enumerate(lines):
    m=re.match(r'^## Tier [123]: .*\(([0-9,]+) Workflows\)', ln)
    if not m: continue
    head=int(m.group(1).replace(",",""))
    body=None
    for j in range(i+1, min(i+6,len(lines))):
        bm=re.match(r'^These ([0-9,]+) workflows', lines[j])
        if bm:
            body=int(bm.group(1).replace(",","")); break
        if lines[j].strip() and not lines[j].startswith('>'):
            # first non-blank non-quote prose line reached without a 'These N' sentence
            break
    if body is not None and body!=head:
        errs.append(f"Tier heading says {head:,} but following prose says {body:,}: {ln[:55]}")
# (b) intro-banner arithmetic self-consistency + match to the Grand Total row.
# The Grand Total row states all three UNIQUE-count figures in one cell
# ('4,981 unique ## workflows (2,417 confirmed + 2,564 unclassified)'); the intro banner uses
# the same unique-count frame, so it must agree with THAT row — not the 'Confirmed Total'
# (2,440) row, which counts register rows incl. 23 parent/summary sub-workflows.
intro_m=re.search(r'An additional ([0-9,]+) workflows \(([0-9,]+) total . ([0-9,]+) classified\)', f)
gt_m=re.search(r'\| \*\*Grand Total\*\* \| \*\*([0-9,]+)\*\* unique .##. workflows \(([0-9,]+) confirmed \+ ([0-9,]+) unclassified', f)
# Since the 2026-06-28 Full-Coverage Confirmation Pass the intro banner declares full
# coverage ('Classifies all 5,349 unique ... Zero workflows remain unclassified'). That
# form is accepted and cross-checked against the Grand Total row instead (confirmed ==
# unique, unclassified == 0).
full_m=re.search(r'^> Classifies all ([0-9,]+) unique operational workflows', f, re.M) and re.search(r'^> .*Zero workflows remain unclassified', f, re.M)
if full_m and not intro_m:
    if gt_m:
        g=int(gt_m.group(1).replace(",","")); c=int(gt_m.group(2).replace(",","")); u=int(gt_m.group(3).replace(",",""))
        if c!=g: errs.append(f"Grand Total confirmed-unique ({c:,}) != unique total ({g:,}) under full coverage")
        if u!=0: errs.append(f"Grand Total unclassified ({u:,}) must be 0 under the full-coverage banner")
    else:
        errs.append("cannot find Grand Total row to cross-check the full-coverage intro banner")
elif intro_m:
    unc=int(intro_m.group(1).replace(",","")); tot=int(intro_m.group(2).replace(",","")); cls=int(intro_m.group(3).replace(",",""))
    if tot-cls!=unc:
        errs.append(f"Intro banner arithmetic wrong: {tot:,} total − {cls:,} classified = {tot-cls:,}, but states {unc:,} unclassified")
    if gt_m:
        g=int(gt_m.group(1).replace(",","")); c=int(gt_m.group(2).replace(",","")); u=int(gt_m.group(3).replace(",",""))
        if tot!=g: errs.append(f"Intro banner grand total ({tot:,}) != Summary Grand Total unique ({g:,})")
        if cls!=c: errs.append(f"Intro banner classified ({cls:,}) != Summary Grand Total confirmed-unique ({c:,})")
        if unc!=u: errs.append(f"Intro banner unclassified ({unc:,}) != Summary Grand Total unclassified ({u:,})")
else:
    errs.append("Could not locate intro-banner (either the pre-2026-06-28 'An additional N workflows (M total − K classified)' form or the full-coverage 'Zero workflows remain unclassified' form)")
print("\n".join(errs))
PY
)
PROSE_DRIFT_COUNT=$(echo -n "$PROSE_DRIFT" | grep -cP '.' || true)
if [ "$PROSE_DRIFT_COUNT" -eq 0 ]; then
    ok "Criticality-classification prose counts (tier bodies + intro arithmetic) match headings/Summary"
else
    error "$PROSE_DRIFT_COUNT criticality-classification prose count(s) disagree with their heading or the Summary table:"
    echo "$PROSE_DRIFT" | sed 's/^/    /'
fi

# --- Check 19: PA/VS link resolution in value-stream-index.md ---
echo "--- Check 19: PA/VS link resolution in value-stream-index.md ---"
# The index's 'Detailed Value Stream Map' lists every value stream and process area as a
# markdown link to its README / PA file (./VS-NN-.../(README|PA-NN.X-...).md). A 2026-06-21
# review found 12 such links stale for VS-178/179/180/181: the hrefs used slugs with an extra
# 'and' conjunction (e.g. ...-and-title-consolidation.md) while the files on disk omit it
# (...-title-consolidation.md) — a drift no other check sees (Check 2 compares header COUNTS,
# not link TARGETS; Check 7 validates workflow-ID references, not file paths). This check
# resolves every intra-repo markdown link in the index to its target file so the drift cannot
# recur. (Scope is the index; the cross-reference docs' W-references are covered by Checks 6/7.)
INDEX="$REPO_ROOT"/01-model-company/workflows/value-stream-index.md
BROKEN_INDEX_LINKS=""
TOTAL_INDEX_LINKS=$(grep -oP '\]\(\K\./VS-[^)]+\.md' "$INDEX" 2>/dev/null | wc -l | tr -d ' ')
while IFS= read -r link; do
    # link is relative to the index's own directory (workflows/)
    [ -f "$REPO_ROOT"/01-model-company/workflows/"$link" ] || BROKEN_INDEX_LINKS="$BROKEN_INDEX_LINKS$link"$'\n'
done < <(grep -oP '\]\(\K\./VS-[^)]+\.md' "$INDEX" 2>/dev/null || true)
BROKEN_INDEX_COUNT=$(echo -n "$BROKEN_INDEX_LINKS" | grep -cP '\.md' || true)
if [ "$BROKEN_INDEX_COUNT" -eq 0 ]; then
    ok "All $TOTAL_INDEX_LINKS PA/VS links in value-stream-index.md resolve to a file"
else
    error "$BROKEN_INDEX_COUNT link(s) in value-stream-index.md do not resolve to a file:"
    echo "$BROKEN_INDEX_LINKS" | sed 's/^/    /'
fi

# --- Check 20: PA-file relative-link resolution ---
echo "--- Check 20: PA-file relative-link resolution ---"
# Every PA file carries two navigation links (a 'Part of **[VS-NN: ...](./README.md)** ...'
# header line and a '*... · [Value Stream Index](../value-stream-index.md)*' footer) plus
# occasional in-body cross-reference links. A 2026-06-21 review found exactly one stale across
# all PA files (565 at the time of that review): VS-56 PA-56.1's header linked to '../value-stream.md' instead of
# '../value-stream-index.md'. No other check sees this — Check 2 compares header COUNTS, Check 7
# validates workflow-IDs, and Check 19 scopes only the index. This check resolves every
# relative (./ or ../) intra-repo .md link inside every PA file so the drift cannot recur.
PA_FILE_COUNT=$(find "$REPO_ROOT"/01-model-company/workflows -name 'PA-*.md' -type f | wc -l | tr -d ' ')
BROKEN_PA_LINKS=$(python3 - "$REPO_ROOT" <<'PY'
import os,re,sys,glob
ROOT=sys.argv[1]
out=[]
total=0
for f in sorted(glob.glob(f"{ROOT}/01-model-company/workflows/VS-*/PA-*.md")):
    dirn=os.path.dirname(f)
    txt=open(f,encoding='utf-8',errors='replace').read()
    for m in re.finditer(r'\]\((\./|\.\.\/)[^)]*?\.md(?:\s+"[^"]*")?\)', txt):
        target=m.group(0)[2:-1].split('"')[0].strip()  # strip ']( ... )' and any title attr
        # ignore fragment-only links (no file before '#')
        path_part=target.split('#')[0]
        if not path_part: continue
        total+=1
        resolved=os.path.normpath(os.path.join(dirn,path_part))
        if not os.path.exists(resolved):
            out.append(f"{f.replace(ROOT+'/','')}: -> {target}")
print(total, "\n".join(out), sep='\n')
PY
)
# First line of output is the total count; remainder are the broken links
PA_LINK_TOTAL=$(echo "$BROKEN_PA_LINKS" | head -1)
BROKEN_PA_BODY=$(echo "$BROKEN_PA_LINKS" | tail -n +2)
BROKEN_PA_COUNT=$(echo -n "$BROKEN_PA_BODY" | grep -cP 'PA-' || true)
if [ "$BROKEN_PA_COUNT" -eq 0 ]; then
    ok "All $PA_LINK_TOTAL relative links across all $PA_FILE_COUNT PA files resolve to a file"
else
    error "$BROKEN_PA_COUNT PA-file relative link(s) (of $PA_FILE_COUNT) do not resolve to a file:"
    echo "$BROKEN_PA_BODY" | sed 's/^/    /'
fi

# --- Check 21: Automation/Controls content quality (draft-field tracker) ---
echo "--- Check 21: Automation/Controls content quality ---"
# Checks 10/12/15 guard the analysis fields' PRESENCE and one legacy boilerplate string,
# but a 2026-06-21 review found the bulk of the machine-generated `### Automation Opportunity`
# and `### Controls` bodies (added repo-wide by add-automation-controls.py) are low-quality
# DRAFT content: Automation bullets were emitted as mid-phrase fragments like
#   '- auto-review (account manager reviews application: (a) verify)'
# and ~89% of Controls sections cited no CTL-XX from the internal-controls register.
# This check reports three live quality metrics. The backlog was fully closed on
# 2026-06-28: fragments were repaired by defragment-automation.py (2026-06-21), and CTL-XX
# citation coverage reached 100% when the register gained process-area operating controls
# (C26–C33, CTL-240–CTL-808 — one derived control per process area mapped to every workflow
# of that PA, via 07-methodology/add-pa-controls.py + backfill-controls.py). The check is
# retained as the regression guard: it WARNs (as before) if any metric slips off target —
# fragments > 0, CTL citation < 100%, or boilerplate > 0 — and prints a single OK otherwise.
# Metrics:
#   (a) Automation bullets that are broken fragments (auto-X (lowercase fragment, no period)
#   (b) Controls sections citing >=1 real CTL-XX  (coverage of the controls register)
#   (c) Controls sections that are pure boilerplate (no CTL-XX AND one of two known strings)
QUALITY=$(python3 - "$REPO_ROOT" <<'PY'
import glob, os, re, sys
ROOT = sys.argv[1]
files = glob.glob(f"{ROOT}/01-model-company/workflows/VS-*/PA-*.md")
BOILERPLATE = {
    "operational: standard operating procedures; system-enforced validation rules",
    "operational: periodic reconciliation against source documents",
}
frag = 0; auto_bullets = 0
ctrl_total = 0; ctrl_with_ctl = 0; ctrl_boiler = 0
# Broad fragment detector: any bullet emitted by add-automation-controls.py in its legacy
# fragment form. Matches every verb prefix in the generator's MANUAL_VERBS vocabulary
# ('auto-X', 'rule-based auto-X', 'workflow notification', 'continuous audit', etc.)
# followed by an opening paren — the signature of a mid-phrase snippet. The narrow regex
# used at Check 21's introduction under-counted (it missed 'rule-based'/'workflow'/'continuous'
# prefixes and nested parens); this broad form is aligned with defragment-automation.py and
# catches every generator-fragment form so the metric is an honest regression guard.
# Complete sentences (hand-written like VS-73, or regenerated '- System ...' drafts) never match.
frag_re = re.compile(r'^- (?:auto-\w+|rule-based auto-\w+|rule-based authorization|workflow (?:notification|orchestration)|continuous audit|auto-flag for investigation) [\(\)]')
for f in files:
    txt = open(f, encoding="utf-8", errors="replace").read()
    for m in re.finditer(r'^### Automation Opportunity\n(.*?)(?=^### |^---|^## |\Z)', txt, re.M | re.S):
        for line in m.group(1).split("\n"):
            line = line.strip()
            if line.startswith("- "):
                auto_bullets += 1
                if frag_re.match(line):
                    frag += 1
    for m in re.finditer(r'^### Controls\n(.*?)(?=^### |^---|^## |\Z)', txt, re.M | re.S):
        ctrl_total += 1
        body = m.group(1).strip()
        has_ctl = bool(re.search(r'\bCTL-\d+', body))
        if has_ctl:
            ctrl_with_ctl += 1
        elif any(b in body for b in BOILERPLATE) and '\n' not in body.strip():
            ctrl_boiler += 1
pct_ctl = (100 * ctrl_with_ctl // ctrl_total) if ctrl_total else 0
print(f"{frag}|{auto_bullets}|{ctrl_with_ctl}|{ctrl_total}|{pct_ctl}|{ctrl_boiler}")
PY
)
FRAG_BULLETS=$(echo "$QUALITY" | cut -d'|' -f1)
AUTO_TOTAL=$(echo "$QUALITY" | cut -d'|' -f2)
CTRL_WITH_CTL=$(echo "$QUALITY" | cut -d'|' -f3)
CTRL_TOTAL=$(echo "$QUALITY" | cut -d'|' -f4)
CTRL_PCT=$(echo "$QUALITY" | cut -d'|' -f5)
CTRL_BOILER=$(echo "$QUALITY" | cut -d'|' -f6)
if [ "$FRAG_BULLETS" -eq 0 ] && [ "$CTRL_WITH_CTL" -eq "$CTRL_TOTAL" ] && [ "$CTRL_BOILER" -eq 0 ]; then
    ok "Automation/Controls quality targets met: 0/$AUTO_TOTAL fragment bullets; $CTRL_WITH_CTL/$CTRL_TOTAL Controls sections cite a CTL-XX ($CTRL_PCT%); $CTRL_BOILER pure-boilerplate. (Register: 67 core + 172 domain anchors + 569 process-area operating controls = 808; PA controls are honest-draft derived mappings pending per-workflow review — see WORKFLOW-FORMAT-GUIDE.md 'Quality bar'. This check remains the regression guard for all three metrics.)"
else
    warn "Automation/Controls draft-field quality: $FRAG_BULLETS/$AUTO_TOTAL Automation bullets are mid-phrase fragments (target 0); $CTRL_WITH_CTL/$CTRL_TOTAL Controls sections cite a CTL-XX ($CTRL_PCT% — target 100%); $CTRL_BOILER are pure-boilerplate (target 0). See WORKFLOW-FORMAT-GUIDE.md 'Quality bar'; run defragment-automation.py / backfill-controls.py as appropriate."
fi

# --- Check 22: Required-field completeness (WORKFLOW-FORMAT-GUIDE 9 fields) ---
echo "--- Check 22: Required-field completeness ---"
# WORKFLOW-FORMAT-GUIDE.md lists 9 required fields per workflow. No prior check enforces them
# (Check 12 covers only Automation/Controls); a 2026-06-21 scan found ~1,105 missing-field
# instances across ~480 workflows (the affected set spans 27 value streams — chiefly
# VS-15..18/27/31..40/48 plus VS-53..63 and singletons — wider than first reported). The
# backlog was fully closed by the 2026-06-27 completeness pass: Participants rows were
# mechanically derived from each workflow's own Steps roles (backfill-participants.py),
# and System Touchpoints / Pain Points were authored per-workflow from step content.
# This check is retained as the regression guard so a future generation artifact that
# ships workflows missing required fields is caught. Reports any gap as a WARN (same
# treatment as Check 21's draft-quality tracker).
#   Five fields are table-row form ('| **Field** |'): Trigger, Frequency, Volume, Owner, Participants.
#   Three are ### sections: Steps, System Touchpoints, Pain Points / Risks.
#   Time Estimate accepts either form (all 5,349 workflows now use the ### form; 11 of
#   them also retain a legacy table row — the dual form is harmless and accepted).
# Each field is counted present if it appears in EITHER form within its workflow block.
FIELDS=$(python3 - "$REPO_ROOT" <<'PY'
import glob, os, re, sys
ROOT = sys.argv[1]
TABLE = ["Trigger", "Frequency", "Volume", "Owner", "Participants"]
HEADER = ["Steps", "System Touchpoints", "Time Estimate", "Pain Points / Risks"]
TIME_OK = True  # Time Estimate accepts either form
missing = {f: 0 for f in TABLE + HEADER}
worst_vs = {}
total = 0
for f in glob.glob(f"{ROOT}/01-model-company/workflows/VS-*/PA-*.md"):
    vs = re.search(r"VS-(\d+)", f).group(1)
    txt = open(f, encoding="utf-8", errors="replace").read()
    for m in re.finditer(r"^## (W\d+[A-Z]?)\..*?(?=^## W|\Z)", txt, re.M | re.S):
        block = m.group(0)
        total += 1
        for field in TABLE:
            if not re.search(r"^\| \*\*" + re.escape(field) + r"\*\*", block, re.M):
                missing[field] += 1
                worst_vs.setdefault(field, {}).setdefault(vs, 0)
                worst_vs[field][vs] += 1
        # Steps: present if '### Steps' (exact or qualified) header OR any table with the
        # '| # |' column header (every steps table uses it, regardless of whether the step
        # IDs are bare numbers, '1a', or alpha-prefixed 'CS-1'/'NR-1'). Catches all
        # legitimate forms: canonical flat table, multi-trigger '### Steps (...)',
        # phase-grouped '### <Phase>' tables, cadence-grouped '### Daily/Weekly' tables,
        # and non-numeric step-ID schemes. A strict 5-column-header or bare-number check
        # would false-flag the qualified/phase/cadence/alpha-prefix forms.
        if not (re.search(r"^### Steps(?: \([^)]*\))?\s*$", block, re.M) or
                re.search(r"^\| # \|", block, re.M)):
            missing["Steps"] += 1
            worst_vs.setdefault("Steps", {}).setdefault(vs, 0)
            worst_vs["Steps"][vs] += 1
        # System Touchpoints / Pain Points: accept exact OR '### Field (qualifier)'
        # (parenthetically-qualified sub-forms are legitimate per WORKFLOW-FORMAT-GUIDE.md).
        for field in ("System Touchpoints", "Pain Points / Risks"):
            if not re.search(r"^### " + re.escape(field) + r"(?: \([^)]*\))?\s*$", block, re.M):
                missing[field] += 1
                worst_vs.setdefault(field, {}).setdefault(vs, 0)
                worst_vs[field][vs] += 1
        # Time Estimate: accept either ### header (exact or qualified) or table row.
        if not (re.search(r"^### Time Estimate(?: \([^)]*\))?\s*$", block, re.M) or
                re.search(r"^\| \*\*Time Estimate\*\*", block, re.M)):
            missing["Time Estimate"] += 1
            worst_vs.setdefault("Time Estimate", {}).setdefault(vs, 0)
            worst_vs["Time Estimate"][vs] += 1
total_missing = sum(missing.values())
worst_vs_str = max(worst_vs, key=lambda k: sum(worst_vs[k].values())) if worst_vs else "-"
# Emit: total_missing|total|per-field counts|worst-vs
parts = [str(total_missing), str(total)]
for field in TABLE + HEADER:
    parts.append(f"{field}:{missing[field]}")
parts.append(f"worst:{worst_vs_str}")
print("|".join(parts))
PY
)
FIELD_TOTAL_MISSING=$(echo "$FIELDS" | cut -d'|' -f1)
FIELD_TOTAL_WF=$(echo "$FIELDS" | cut -d'|' -f2)
FIELD_DETAIL=$(echo "$FIELDS" | cut -d'|' -f3-)
if [ "$FIELD_TOTAL_MISSING" -eq 0 ]; then
    ok "All $FIELD_TOTAL_WF workflows have all 9 required fields"
else
    warn "$FIELD_TOTAL_MISSING missing required-field instance(s) across $FIELD_TOTAL_WF workflows (WORKFLOW-FORMAT-GUIDE.md 'Required fields'). Per-field: $(echo "$FIELD_DETAIL" | sed 's/|/, /g'). All 5,349 workflows carried all 9 fields after the 2026-06-27 completeness pass (Participants derived from Steps; System Touchpoints / Pain Points authored) — any reading above zero is a regression from a new generation artifact."
fi

# --- Check 23: Intra-file TOC anchor resolution ---
echo "--- Check 23: Intra-file TOC anchor resolution ---"
# Every PA file opens with a '## Workflows in This Process Area' navigation list whose
# entries link to the workflow headings below via GitHub heading anchors (#slug). A
# gap-analysis generator bug left 1,926 such anchors malformed across 271 PA files —
# the slugger dropped hyphens ('Floor-Plan' -> 'floorplan') and stale W-numbers survived
# a renumber (display 'W4601' but anchor '#w4409-...') — so the TOC links resolved to
# nothing on GitHub. No prior check saw this: Checks 19/20 verify linked FILES resolve;
# none resolve anchors. This check computes each file's heading slugs (GitHub slugger)
# and reports any '(#anchor)' link that matches no heading. Treated as an ERROR (a
# broken navigational link), consistent with the file-resolution checks 19/20. Repaired
# by `07-methodology/fix-toc-anchors.py`; this check guards against regression.
ANCHORS=$(python3 - "$REPO_ROOT" <<'PY'
import glob, os, re, sys
ROOT = sys.argv[1]
def gh_slug(s):
    # github-slugger semantics (consistency review #11 correction): lowercase, remove
    # non-word/space/hyphen chars, then replace EACH space with '-' — do NOT collapse
    # runs. GitHub turns the two adjacent spaces left by removed spaced punctuation
    # (' & ', ' / ') into a DOUBLE hyphen; the previous collapsing rule wrongly accepted
    # single-hyphen anchors that are broken on GitHub (4,618 repo-wide, repaired by
    # fix-toc-anchors.py v2). Duplicates get '-1', '-2'… suffixes.
    s = s.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s, flags=re.UNICODE)
    return s.replace(' ', '-')
files_bad = {}
for f in sorted(glob.glob(f"{ROOT}/01-model-company/workflows/VS-*/PA-*.md")):
    txt = open(f, encoding='utf-8', errors='replace').read()
    heads = set(); _seen = {}
    for h in re.findall(r'^#+\s+(.+?)\s*$', txt, re.M):
        s = gh_slug(h); n = _seen.get(s, 0); _seen[s] = n + 1
        heads.add(s if n == 0 else f"{s}-{n}")
    bad = sorted({anchor for _disp, anchor in re.findall(r'\[([^\]]+)\]\(#([^)]+)\)', txt)
                  if anchor not in heads})
    if bad:
        files_bad[f.replace(ROOT + '/', '')] = bad
print(f"{len(files_bad)}|{sum(len(v) for v in files_bad.values())}")
for f, bad in files_bad.items():
    sample = bad[0] + (f" (+{len(bad)-1} more)" if len(bad) > 1 else "")
    print(f"{f}: #{sample}")
PY
)
BAD_ANCHOR_FILES=$(echo "$ANCHORS" | head -1 | cut -d'|' -f1)
BAD_ANCHOR_TOTAL=$(echo "$ANCHORS" | head -1 | cut -d'|' -f2)
BAD_ANCHOR_SAMPLES=$(echo "$ANCHORS" | tail -n +2)
if [ "$BAD_ANCHOR_TOTAL" -eq 0 ]; then
    ok "All intra-file TOC anchors resolve to a heading"
else
    error "$BAD_ANCHOR_TOTAL intra-file TOC anchor(s) across $BAD_ANCHOR_FILES PA file(s) do not resolve to any heading (run 07-methodology/fix-toc-anchors.py to repair):"
    echo "$BAD_ANCHOR_SAMPLES" | sed 's/^/    /' | head -20
fi

# --- Check 24: workflows/README.md family reconciliation + stale canonical-figure guard ---
echo "--- Check 24: workflows/README.md family reconciliation & stale-figure guard ---"
# Two-part guard added 2026-06-26 after a review found (a) workflows/README.md family
# headers/rows had drifted out of sync with value-stream-index.md (a VS-127 row stuck at
# 24, a missing VS-192 row, and two stale family-header totals) and (b) a headcount
# change (6,757 -> 6,762) had been applied to summary docs but not propagated to ~97
# workflow files. No prior check saw either: Check 3 verifies the index GRAND total
# only; Check 18 covers criticality-classification prose only. Part A is a structural
# ERROR (count reconciliation, same class as Check 2/9); Part B is a WARN (editorial
# figure consistency) scoped to skip the labelled historical-record docs and any
# 'X -> Y' change-note. Repair scripts: fix-headcount-6757.py (Part B) + hand-edit (A).
CHECK24=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, sys
ROOT = sys.argv[1]
errors, stale = [], []

# ---- Part A: workflows/README.md family sections reconcile with value-stream-index.md ----
idx = open(f"{ROOT}/01-model-company/workflows/value-stream-index.md", encoding='utf-8').read().splitlines()
readme = open(f"{ROOT}/01-model-company/workflows/README.md", encoding='utf-8').read().splitlines()

idx_sub, cur = {}, None
fam_row = re.compile(r'^\| ([A-Za-z][^|]*?) \| \[VS-')
for line in idx:
    m = fam_row.match(line)
    if m:
        cur = m.group(1).strip(); continue
    if '**Subtotal**' in line and cur:
        nums = re.findall(r'\*\*([\d,]+)\*\*', line)
        if nums:
            idx_sub[cur] = int(nums[-1].replace(',', ''))
        cur = None

hdr = re.compile(r'^### (.+?) \(([0-9,]+) workflows\)')
vs_row = re.compile(r'^\| \[VS-\d+\]\([^)]*\) \| .* \| (\d+) \|$')
readme_fam, cur = {}, None
for line in readme:
    m = hdr.match(line)
    if m:
        cur = m.group(1).strip(); readme_fam[cur] = {'header': int(m.group(2).replace(',', '')), 'sum': 0}; continue
    m = vs_row.match(line)
    if m and cur:
        readme_fam[cur]['sum'] += int(m.group(1))

idx_total = sum(idx_sub.values()); readme_total = sum(f['sum'] for f in readme_fam.values())
for fam, idx_n in idx_sub.items():
    if fam not in readme_fam:
        errors.append(f"family '{fam}' in value-stream-index.md but has no section in workflows/README.md"); continue
    h = readme_fam[fam]['header']; s = readme_fam[fam]['sum']
    if not (idx_n == h == s):
        errors.append(f"{fam}: index subtotal={idx_n}, README header={h}, README row-sum={s}")
if idx_total != readme_total:
    errors.append(f"grand total: index={idx_total}, README row-sum={readme_total}")

# ---- Part B: stale canonical total-headcount figure '6,757' in current-state prose ----
SKIP = {'CHANGELOG.md', 'workflow-gap-analysis.md', 'headcount-reality-check.md'}
pat = re.compile(r'(?<!\d)6,757(?!\d)')
for dirpath, _d, files in os.walk(ROOT):
    if os.sep + '.git' in dirpath: continue
    for fn in files:
        if not fn.endswith('.md') or fn in SKIP: continue
        path = os.path.join(dirpath, fn)
        txt = open(path, encoding='utf-8', errors='replace').read()
        for m in pat.finditer(txt):
            lo = max(0, m.start()-25); hi = min(len(txt), m.end()+25)
            if '->' in txt[lo:hi] or '\u2192' in txt[lo:hi]:
                continue  # legitimate historical 'X -> Y' change-note
            line_no = txt.count('\n', 0, m.start()) + 1
            stale.append(f"{os.path.relpath(path, ROOT)}:{line_no}")

print(f"A_ERRS={len(errors)}")
for e in errors: print(f"A_ERR|{e}")
print(f"B_STALE={len(stale)}")
for s in stale[:12]: print(f"B_STALE|{s}")
print(f"GRAND={readme_total}")
PY
)
A_ERRS=$(echo "$CHECK24" | sed -n 's/^A_ERRS=//p')
B_STALE=$(echo "$CHECK24" | sed -n 's/^B_STALE=//p')
GRAND=$(echo "$CHECK24" | sed -n 's/^GRAND=//p')
if [ "$A_ERRS" -eq 0 ]; then
    ok "workflows/README.md family headers & per-VS row sums reconcile with value-stream-index.md subtotals (8 families, grand total $GRAND workflows)"
else
    error "workflows/README.md does not reconcile with value-stream-index.md ($A_ERRS family mismatch(es)) — family header / row-sum / index-subtotal must all agree:"
    echo "$CHECK24" | grep '^A_ERR|' | sed 's/^A_ERR|/    /'
fi
if [ "$B_STALE" -eq 0 ]; then
    ok "No stale total-headcount figure '6,757' in current-state prose (canonical figure is 6,762; historical 'X -> Y' notes and CHANGELOG/workflow-gap-analysis/headcount-reality-check excluded)"
else
    warn "Stale total-headcount figure '6,757' appears $B_STALE time(s) in current-state prose (canonical figure is now 6,762 — run 07-methodology/fix-headcount-6757.py to repair):"
    echo "$CHECK24" | grep '^B_STALE|' | sed 's/^B_STALE|/    /'
fi

# --- Check 25: criticality proposed-register mirror + touchpoint-map reconciliation claims ---
echo "--- Check 25: proposed-register mirror & touchpoint-map reconciliation ---"
# Added 2026-06-26 after an independent review found the 2026-06-25 VS-127 PA-127.4 regeneration
# of workflow-criticality-proposed.md (unclassified 2,588 -> 2,596) had NOT been propagated into
# (a) workflow-criticality-classification.md's §Summary 'Proposed classification' mirror (still
#     2,564 / 507-1,912-145 — contradicting that same file's intro banner and Grand-Total row),
# (b) three further current-state prose spots citing the stale figure 2,564 (format-guide layout
#     line, touchpoint-map footer sentence), and
# (c) workflow-system-touchpoint-map.md, last fully reconciled at Pass 29: its footer still
#     declared 'Reconciled to 5,317 workflows across 187 value streams', its §summary section
#     stopped at VS-191 with no VS-192 row, and the Pass 26–29 rows (VS-178–VS-191) sat
#     header-less between the section heading and the intro note — a broken table invisible to
#     Check 13, whose parser anchors on a header row.
# No prior check saw any of these: Check 18 verifies tier-body counts only; Check 3 verifies the
# index grand total only; Check 24 Part B guards one hard-coded headcount figure. Parts:
#   A (ERROR): the classification doc's proposed-summary table (three tier rows, Proposed Total,
#      coverage row) must equal workflow-criticality-proposed.md's register header (itself
#      verified against PA headers by Check 1).
#   B (WARN): stale canonical unclassified figure '2,564' in current-state prose — same
#      SKIP-docs and 'X -> Y' exclusions as Check 24 Part B.
#   C (ERROR): touchpoint-map self-declared reconciliation must match canonical reality —
#      footer 'Reconciled to N workflows across M value streams' equals the index Grand Total
#      and active-VS count; the §summary heading range ends at the index's max VS; every
#      VS from 79 through max VS has a primary-module row.
CHECK25=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, sys
ROOT = sys.argv[1]
errors, stale = [], []
WF = f"{ROOT}/01-model-company/workflows"

# ---- Part A: proposed-register mirror in workflow-criticality-classification.md ----
prop = open(f"{WF}/workflow-criticality-proposed.md", encoding='utf-8').read()
m = re.search(r'\*\*Workflow coverage:\*\* ([\d,]+) unclassified workflows · Tier 1: ([\d,]+) · Tier 2: ([\d,]+) · Tier 3: ([\d,]+)', prop)
if not m:
    errors.append("cannot parse '**Workflow coverage:**' register header in workflow-criticality-proposed.md")
else:
    reg_total = int(m.group(1).replace(',', ''))
    tiers = [int(m.group(i).replace(',', '')) for i in (2, 3, 4)]
    if sum(tiers) != reg_total:
        errors.append(f"register header inconsistent: T1+T2+T3={sum(tiers)} != total {reg_total}")
    cls = open(f"{WF}/workflow-criticality-classification.md", encoding='utf-8').read()
    def grab(pat, label):
        mm = re.search(pat, cls, re.M)
        if not mm:
            errors.append(f"classification doc: cannot find {label}")
            return None
        return int(mm.group(1).replace(',', ''))
    t1 = grab(r'^\| Phase 1 \| Go-Live Critical \(Tier 1\) \u2014 proposed \| ([\d,]+) \|$', 'proposed Tier-1 row')
    t2 = grab(r'^\| Phase 2 \| Operational Excellence \(Tier 2\) \u2014 proposed \| ([\d,]+) \|$', 'proposed Tier-2 row')
    t3 = grab(r'^\| Phase 3 \| Innovation & Optimization \(Tier 3\) \u2014 proposed \| ([\d,]+) \|$', 'proposed Tier-3 row')
    tot = grab(r'^\| \*\*Proposed Total\*\* \| \| \*\*([\d,]+)\*\* \|$', 'Proposed Total row')
    cov = grab(r'^\| Proposed \(keyword, pending review\) \| ([\d,]+) \|$', 'coverage-table Proposed row')
    for got, want, label in ((t1, tiers[0], 'Tier 1'), (t2, tiers[1], 'Tier 2'), (t3, tiers[2], 'Tier 3'), (tot, reg_total, 'Proposed Total'), (cov, reg_total, 'Coverage Proposed')):
        if got is not None and got != want:
            errors.append(f"classification proposed-summary {label} = {got:,} but register = {want:,}")

# ---- Part B: stale canonical unclassified figure in current-state prose ----
# '2,564' was the pre-Pass-26–29 figure; '2,596' became stale itself when the 2026-06-28
# Full-Coverage Confirmation Pass closed the backlog to zero. Both are guarded with the
# same SKIP-docs / 'X -> Y' change-note exclusions.
SKIP = {'CHANGELOG.md', 'workflow-gap-analysis.md', 'headcount-reality-check.md'}
for pat_src in (r'(?<!\d)2,564(?!\d)', r'(?<!\d)2,596(?!\d)'):
    pat = re.compile(pat_src)
    for dirpath, _d, files in os.walk(ROOT):
        if os.sep + '.git' in dirpath: continue
        for fn in files:
            if not fn.endswith('.md') or fn in SKIP: continue
            path = os.path.join(dirpath, fn)
            txt = open(path, encoding='utf-8', errors='replace').read()
            for m in pat.finditer(txt):
                lo = max(0, m.start()-25); hi = min(len(txt), m.end()+25)
                if '->' in txt[lo:hi] or '\u2192' in txt[lo:hi]:
                    continue  # legitimate historical 'X -> Y' change-note
                line_no = txt.count('\n', 0, m.start()) + 1
                stale.append(f"{os.path.relpath(path, ROOT)}:{line_no}")

# ---- Part C: touchpoint-map self-declared reconciliation vs canonical reality ----
idx = open(f"{WF}/value-stream-index.md", encoding='utf-8').read()
vs_nums = {int(n) for n in re.findall(r'\[VS-(\d+)\]\(', idx)}
max_vs = max(vs_nums) if vs_nums else 0
n_vs = len(vs_nums)
gm = re.search(r'^\|[^\n]*\*\*Grand Total\*\*[^\n]*$', idx, re.M)
if not gm:
    errors.append("cannot parse Grand Total row in value-stream-index.md")
else:
    nums = re.findall(r'\*\*([\d,]+)\*\*', gm.group(0))
    if len(nums) < 2:
        errors.append("Grand Total row does not carry two bold figures (PAs, workflows)")
    else:
        idx_pas, idx_wfs = int(nums[-2].replace(',', '')), int(nums[-1].replace(',', ''))
tmap_path = f"{WF}/workflow-system-touchpoint-map.md"
tmap = open(tmap_path, encoding='utf-8').read()
fm = re.search(r'Reconciled to ([\d,]+) workflows across (\d+) value streams', tmap)
if not fm:
    errors.append("touchpoint map: cannot find the self-declared 'Reconciled to N workflows across M value streams' footer claim")
elif 'idx_wfs' in dir():
    n_wfs, n_declared_vs = int(fm.group(1).replace(',', '')), int(fm.group(2))
    if n_wfs != idx_wfs or n_declared_vs != n_vs:
        errors.append(f"touchpoint map footer declares {n_wfs:,} workflows / {n_declared_vs} value streams but index says {idx_wfs:,} / {n_vs}")
hm = re.search(r'^## Statutory & Gap-Analysis Value Streams \(VS-\d+\u2013VS-(\d+)\)', tmap, re.M)
if not hm:
    errors.append("touchpoint map: cannot find the '## Statutory & Gap-Analysis Value Streams (VS-a\u2013VS-b)' section heading")
elif int(hm.group(1)) != max_vs:
    errors.append(f"touchpoint map section heading ends at VS-{hm.group(1)} but the index max is VS-{max_vs}")
rows = {int(n) for n in re.findall(r'^\| VS-(\d+) \| ', tmap, re.M)}
missing = [v for v in range(79, max_vs + 1) if v not in rows]
if missing:
    errors.append(f"touchpoint map primary-module rows missing for: {', '.join('VS-' + str(v) for v in missing)}")

print(f"A_ERRS={len(errors)}")
for e in errors: print(f"A_ERR|{e}")
print(f"B_STALE={len(stale)}")
for s in stale[:12]: print(f"B_STALE|{s}")
print(f"MAX_VS={max_vs}")
PY
)
A_ERRS=$(echo "$CHECK25" | sed -n 's/^A_ERRS=//p')
B_STALE=$(echo "$CHECK25" | sed -n 's/^B_STALE=//p')
MAX_VS=$(echo "$CHECK25" | sed -n 's/^MAX_VS=//p')
if [ "$A_ERRS" -eq 0 ]; then
    ok "Proposed-register mirror & touchpoint-map reconciliation claims match canonical figures (register tiers/total; footer 'Reconciled to' == index grand totals; section range ends at VS-$MAX_VS with full VS-row coverage)"
else
    error "Criticality proposed-register mirror / touchpoint-map reconciliation mismatch ($A_ERRS):
"
    echo "$CHECK25" | grep '^A_ERR|' | sed 's/^A_ERR|/    /'
fi
if [ "$B_STALE" -eq 0 ]; then
    ok "No stale unclassified-workflow figure '2,564'/'2,596' in current-state prose (register at full coverage — 0 unclassified — since 2026-06-28; historical 'X -> Y' notes and CHANGELOG/workflow-gap-analysis/headcount-reality-check excluded)"
else
    warn "Stale unclassified-workflow figure '2,564'/'2,596' appears $B_STALE time(s) in current-state prose (register at full coverage since 2026-06-28 — use an 'X -> Y' change-note or drop the figure):"
    echo "$CHECK25" | grep '^B_STALE|' | sed 's/^B_STALE|/    /'
fi

# --- Check 26: dependency-map §8 cross-cutting-block reconciliation ---
echo "--- Check 26: dependency-map §8 block reconciliation ---"
# The dependency map's §8 mines inline 'VS-NN' references across the Statutory + gap-analysis
# block's PA and README files and self-declares its coverage: the section heading range
# (VS-79–VS-NN), the intro's block size (N value streams / M workflows), the §8.1 anchor
# top-10 table, and §8.4's per-program anchor-edge rows. Consistency review #14 (2026-06-28)
# found this block frozen at the v4.4 snapshot — heading/§8.1/§8.4 all ended at VS-191, the
# intro still said 113 value streams / 2,712 workflows (excluding both VS-192's +24 and the
# PA-127.4 extension's +8), and the v4.4 footer itself flagged 'VS-192 incorporation pending
# the next consistency review' — a pending item three reviews (#10–#13) shipped without
# action because no check guarded §8; the §8.1 table had also drifted (v4.3 counts, and a
# top-10 that omitted VS-91 while listing VS-100). All parts ERROR (the doc's claims are
# machine-verifiable):
#   A: §8 heading range end == index max active VS.
#   B: §8.4's last '| VS-NN |' program row == max VS (full block coverage).
#   C: §8 intro's declared 'N value streams / M workflows' == actual block content on disk
#      (VS-79..max directories; ## W headers in their PA files).
#   D: §8.1's anchor table == the live top-10 recomputed from PA+README reference mining
#      (membership AND counts) — enforcing the table's own 'freshly recomputed' claim, so
#      any content change that shifts reference counts must refresh the table.
CHECK26=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, sys
ROOT = sys.argv[1]
WF = f"{ROOT}/01-model-company/workflows"
errors = []
idx = open(f"{WF}/value-stream-index.md", encoding='utf-8').read()
vs_nums = {int(n) for n in re.findall(r'\[VS-(\d+)\]\(', idx)}
max_vs = max(vs_nums) if vs_nums else 0
dep = open(f"{WF}/workflow-dependency-map.md", encoding='utf-8').read()

# ---- A: §8 heading range end == index max active VS ----
hm = re.search(r'^## 8\. Cross-Cutting Program Dependencies \(VS-79\u2013VS-(\d+)\)', dep, re.M)
if not hm:
    errors.append("cannot find the '## 8. Cross-Cutting Program Dependencies (VS-79\u2013VS-N)' heading")
elif int(hm.group(1)) != max_vs:
    errors.append(f"\u00a78 heading range ends at VS-{hm.group(1)} but the index max active VS is VS-{max_vs}")

# ---- B: §8.4's last program row == max VS ----
m84 = re.search(r'^### 8\.4 .*?\n(.*?)(?=^>|\Z)', dep, re.M | re.S)
if not m84:
    errors.append("cannot find the '### 8.4' program-anchor table section")
else:
    rows = [int(n) for n in re.findall(r'^\| VS-(\d+) \| ', m84.group(1), re.M)]
    if not rows:
        errors.append("\u00a78.4 has no '| VS-NN |' program rows")
    elif rows[-1] != max_vs:
        errors.append(f"\u00a78.4's last program row is VS-{rows[-1]} but the index max active VS is VS-{max_vs} (block coverage incomplete)")

# ---- C: §8 intro's declared block size == disk ----
# The intro is a wrapped markdown blockquote ('> ... \n> ...'), so normalize newlines and
# quote markers to single spaces before parsing the 'added N value streams / M workflows' claim.
intro_flat = re.sub(r'\s+', ' ', re.sub(r'[\n>]+', ' ', dep[hm.start():dep.find('### 8.1')] if hm else dep))
block_dirs = []
for d in sorted(os.listdir(WF)):
    m = re.match(r'VS-(\d+)-', d)
    if m and 79 <= int(m.group(1)) <= max_vs and os.path.isdir(os.path.join(WF, d)):
        block_dirs.append(d)
wf_disk = 0
for d in block_dirs:
    for fn in sorted(os.listdir(os.path.join(WF, d))):
        if fn.startswith("PA-") and fn.endswith(".md"):
            txt = open(os.path.join(WF, d, fn), encoding='utf-8', errors='replace').read()
            wf_disk += len(re.findall(r'^## W\d+[A-Z]?\.', txt, re.M))
im = re.search(r'added (\d+) value streams / ([\d,]+) workflows', intro_flat)
if not im:
    errors.append("cannot parse the §8 intro's 'added N value streams / M workflows' claim")
else:
    decl_vs, decl_wf = int(im.group(1)), int(im.group(2).replace(',', ''))
    if (decl_vs, decl_wf) != (len(block_dirs), wf_disk):
        errors.append(f"§8 intro declares {decl_vs} value streams / {decl_wf:,} workflows but the block on disk holds {len(block_dirs)} / {wf_disk:,}")

# ---- D: §8.1 anchor table == live top-10 recomputed from PA+README mining ----
counts = {}
for d in block_dirs:
    files = [os.path.join(WF, d, "README.md")] + [os.path.join(WF, d, fn) for fn in sorted(os.listdir(os.path.join(WF, d))) if fn.startswith("PA-") and fn.endswith(".md")]
    for fp in files:
        if not os.path.exists(fp):
            continue
        for mm in re.finditer(r'VS-(\d{1,3})(?![0-9])', open(fp, encoding='utf-8', errors='replace').read()):
            counts[mm.group(1)] = counts.get(mm.group(1), 0) + 1
want = sorted(counts.items(), key=lambda kv: (-kv[1], int(kv[0])))[:10]
m81 = re.search(r'^### 8\.1 .*?\n(.*?)(?=^### )', dep, re.M | re.S)
if not m81:
    errors.append("cannot find the '### 8.1' anchor table section")
else:
    got = [(k, int(v.replace(',', ''))) for k, v in re.findall(r'^\| VS-(\d+) \| [^|]+ \| ([\d,]+) \|$', m81.group(1), re.M)]
    if got != want:
        errors.append(f"§8.1 anchor table is not the live top-10 (freshly recomputed from VS-79\u2013VS-{max_vs} PA+README mining): table={[(('VS-'+k), v) for k, v in got]} live={[(('VS-'+k), v) for k, v in want]}")

print(f"A_ERRS={len(errors)}")
for e in errors: print(f"A_ERR|{e}")
print(f"MAX_VS={max_vs}")
print(f"BLOCK_VS={len(block_dirs)}")
print(f"BLOCK_WF={wf_disk}")
PY
)
C26_ERRS=$(echo "$CHECK26" | sed -n 's/^A_ERRS=//p')
C26_MAXVS=$(echo "$CHECK26" | sed -n 's/^MAX_VS=//p')
C26_VS=$(echo "$CHECK26" | sed -n 's/^BLOCK_VS=//p')
C26_WF=$(echo "$CHECK26" | sed -n 's/^BLOCK_WF=//p')
if [ "$C26_ERRS" -eq 0 ]; then
    ok "Dependency-map §8 block reconciliation: heading/§8.4 end at VS-$C26_MAXVS, intro block size ($C26_VS value streams / $C26_WF workflows) matches disk, and the §8.1 anchor table equals the live top-10 (freshly recomputed from PA+README reference mining)"
else
    error "Dependency-map §8 self-declared coverage does not reconcile ($C26_ERRS mismatch(es)) — the block tables must be re-mined/recomputed:"
    echo "$CHECK26" | grep '^A_ERR|' | sed 's/^A_ERR|/    /'
fi

# --- Check 27: stale register-row figures + unclassified-workflow claims ---
echo "--- Check 27: stale register-row figures & unclassified-workflow claims ---"
# Two guards closed by consistency review #15 (2026-06-28):
#   (A) the Full-Coverage Confirmation Pass updated the register's Summary table to 5,372 rows
#       (5,349 unique) but left three current-state prose figures frozen at the pre-pass state:
#       the root README's folder-tree '(2,776 rows)', the register's own Summary note 'the
#       remaining 2,753 are canonical ## workflows', and the §Domain Breakdown 'breakdown of
#       the 2,776 classified workflows'. '2,776' was the v7.26 register-row total; '2,753' its
#       unique-workflow complement (2,776 - 23 parents). Both are guarded with the same
#       SKIP-docs / 'X -> Y' change-note exclusions as Checks 24B and 25B (canonical: 5,372
#       rows / 5,349 unique).
#   (B) the dependency map's §8 coverage note still claimed 'VS-192 remains unclassified
#       pending criticality review' — true when v4.5 shipped, superseded the same day by the
#       Full-Coverage Confirmation Pass. With all 5,349 workflows classified, any
#       unclassified-workflow claim in workflow-dependency-map.md is stale by definition (the
#       register's own dated 2026-06-14 addition notes are the historical record and stay
#       exempt — this map carries no such dated-note convention).
CHECK27=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, sys
ROOT = sys.argv[1]
stale = []
errs = []
# ---- Part A: stale register-row figures '2,776' / '2,753' in current-state prose ----
SKIP = {'CHANGELOG.md', 'workflow-gap-analysis.md', 'headcount-reality-check.md'}
for fig in ('2,776', '2,753'):
    pat = re.compile(r'(?<!\d)' + fig + r'(?!\d)')
    for dirpath, _d, files in os.walk(ROOT):
        if os.sep + '.git' in dirpath: continue
        for fn in files:
            if not fn.endswith('.md') or fn in SKIP: continue
            path = os.path.join(dirpath, fn)
            txt = open(path, encoding='utf-8', errors='replace').read()
            for m in pat.finditer(txt):
                lo = max(0, m.start()-25); hi = min(len(txt), m.end()+25)
                if '->' in txt[lo:hi] or '\u2192' in txt[lo:hi]:
                    continue  # legitimate historical 'X -> Y' change-note
                line_no = txt.count('\n', 0, m.start()) + 1
                stale.append(f"{os.path.relpath(path, ROOT)}:{line_no} ({fig})")
# ---- Part B: unclassified-workflow claims in workflow-dependency-map.md ----
DEP = os.path.join(ROOT, '01-model-company', 'workflows', 'workflow-dependency-map.md')
dep = open(DEP, encoding='utf-8', errors='replace').read()
for i, ln in enumerate(dep.split('\n'), 1):
    if 'remains unclassified' in ln or 'pending criticality review' in ln:
        errs.append(f"workflow-dependency-map.md:{i} asserts an unclassified/pending state, but all 5,349 workflows have been classified since the 2026-06-28 Full-Coverage Confirmation Pass")
print(f"A_STALE={len(stale)}")
for s in stale[:12]: print(f"A_STALE|{s}")
print(f"B_ERRS={len(errs)}")
for e in errs: print(f"B_ERR|{e}")
PY
)
C27_STALE=$(echo "$CHECK27" | sed -n 's/^A_STALE=//p')
C27_ERRS=$(echo "$CHECK27" | sed -n 's/^B_ERRS=//p')
if [ "$C27_STALE" -eq 0 ]; then
    ok "No stale register-row figure '2,776'/'2,753' in current-state prose (canonical figures are 5,372 rows / 5,349 unique since the 2026-06-28 Full-Coverage Confirmation Pass; historical 'X -> Y' notes and CHANGELOG/workflow-gap-analysis/headcount-reality-check excluded)"
else
    warn "Stale register-row figure '2,776'/'2,753' appears $C27_STALE time(s) in current-state prose (canonical figures are 5,372 rows / 5,349 unique — use an 'X -> Y' change-note or update the figure):"
    echo "$CHECK27" | grep '^A_STALE|' | sed 's/^A_STALE|/    /'
fi
if [ "$C27_ERRS" -eq 0 ]; then
    ok "No unclassified-workflow claims in workflow-dependency-map.md (all 5,349 workflows classified since 2026-06-28)"
else
    error "workflow-dependency-map.md carries unclassified-workflow claims that the 2026-06-28 Full-Coverage Confirmation Pass superseded ($C27_ERRS):"
    echo "$CHECK27" | grep '^B_ERR|' | sed 's/^B_ERR|/    /'
fi

# --- Check 28: requirements-TOC letter-suffixed-ID claims + proposed-register description staleness ---
echo "--- Check 28: requirements-TOC letter-suffixed IDs & proposed-register descriptions ---"
# Two guards closed by consistency review #16 (2026-06-28):
#   (A) the erp-requirements.md TOC's R5 row claimed '(incl. POS-014a, POS-022a)' but no
#       POS-022a exists anywhere — the four letter-suffixed IDs are NFR-022a, POS-014a,
#       PUR-025a/b. The TOC's 'incl.' claims must all exist as defined rows AND must cover
#       every letter-suffixed ID defined in the doc (phantom claims and omissions both fail).
#   (B) with the proposed register at 0 rows since the 2026-06-28 Full-Coverage Confirmation
#       Pass, navigation descriptions of workflow-criticality-proposed.md must not assert a
#       'remaining unclassified' population (stale current-state prose) and must carry the
#       'currently empty' marker; if the register ever repopulates (new workflows shipping
#       unclassified), the guard flips and demands the descriptions stop claiming emptiness.
CHECK28=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, sys
ROOT = sys.argv[1]
errs = []
warns = []
# ---- Part A: TOC letter-suffixed-ID claims vs defined letter-suffixed IDs ----
REQ = os.path.join(ROOT, '01-model-company', 'erp-requirements.md')
txt = open(REQ, encoding='utf-8', errors='replace').read()
toc_end = txt.find('\n## R1.')
toc = txt[:toc_end] if toc_end != -1 else txt
claimed = set()
for m in re.finditer(r'\(incl\.\s+([^)]*)\)', toc):
    for tok in re.finditer(r'([A-Z]{2,4}-\d+)((?:[a-z])(?:/[a-z])*)', m.group(1)):
        base, suffixes = tok.group(1), tok.group(2)
        for suf in [s for s in suffixes.split('/') if s]:
            claimed.add(base + suf)
defined = set(m.group(1) for m in re.finditer(r'^\|\s*([A-Z]{2,4}-\d+[a-z])\s*\|', txt, re.M))
for phantom in sorted(claimed - defined):
    errs.append(f"erp-requirements.md TOC claims letter-suffixed ID {phantom}, but no such requirement row exists")
for missing in sorted(defined - claimed):
    errs.append(f"erp-requirements.md defines letter-suffixed ID {missing}, but the TOC's '(incl. ...)' claims omit it")
# ---- Part B: proposed-register description staleness in navigation docs ----
PROP = os.path.join(ROOT, '01-model-company', 'workflows', 'workflow-criticality-proposed.md')
prop = open(PROP, encoding='utf-8', errors='replace').read()
m = re.search(r'\*\*Workflow coverage:\*\*\s*(\d+) unclassified workflows', prop)
coverage = int(m.group(1)) if m else -1
if coverage == -1:
    warns.append("workflow-criticality-proposed.md: cannot parse the '**Workflow coverage:** N unclassified workflows' banner line")
else:
    spots = [
        ('README.md', 'tree'),
        (os.path.join('01-model-company', 'workflows', 'README.md'), 'nav table'),
        (os.path.join('01-model-company', 'workflows', 'WORKFLOW-FORMAT-GUIDE.md'), 'Related Documents table'),
    ]
    for rel, kind in spots:
        path = os.path.join(ROOT, rel)
        lines = open(path, encoding='utf-8', errors='replace').read().split('\n')
        for i, ln in enumerate(lines, 1):
            if 'workflow-criticality-proposed.md' not in ln:
                continue
            if 'validate-repo' in ln or ln.lstrip().startswith('#') or ln.lstrip().startswith('*'):
                continue  # tool rows, headings, and dated version-note footers are not current-state descriptions
            if coverage == 0:
                if re.search(r'remaining unclassified', ln, re.I):
                    warns.append(f"{rel}:{i} still describes workflow-criticality-proposed.md as holding 'the remaining unclassified workflows', but the register has stood at 0 rows since the 2026-06-28 Full-Coverage Confirmation Pass")
                elif 'empty' not in ln.lower():
                    warns.append(f"{rel}:{i} describes workflow-criticality-proposed.md without any emptiness marker while the register stands at 0 rows")
            else:
                if 'currently empty' in ln:
                    warns.append(f"{rel}:{i} claims workflow-criticality-proposed.md is 'currently empty', but the register holds {coverage} unclassified workflows")
print(f"A_ERRS={len(errs)}")
for e in errs: print(f"A_ERR|{e}")
print(f"B_WARNS={len(warns)}")
for w in warns: print(f"B_WARN|{w}")
PY
)
C28_ERRS=$(echo "$CHECK28" | sed -n 's/^A_ERRS=//p')
C28_WARNS=$(echo "$CHECK28" | sed -n 's/^B_WARNS=//p')
if [ "$C28_ERRS" -eq 0 ]; then
    ok "erp-requirements.md TOC '(incl. ...)' letter-suffixed-ID claims match the defined letter-suffixed requirement rows exactly (no phantom IDs, no omissions)"
else
    error "erp-requirements.md TOC letter-suffixed-ID claims do not match the defined letter-suffixed requirement rows ($C28_ERRS):"
    echo "$CHECK28" | grep '^A_ERR|' | sed 's/^A_ERR|/    /'
fi
if [ "$C28_WARNS" -eq 0 ]; then
    ok "Navigation descriptions of workflow-criticality-proposed.md (root README tree, workflows/README.md, WORKFLOW-FORMAT-GUIDE.md) match the register's current state (0 unclassified rows — descriptions carry the 'currently empty' marker)"
else
    warn "Navigation descriptions of workflow-criticality-proposed.md drifted from the register's current state ($C28_WARNS):"
    echo "$CHECK28" | grep '^B_WARN|' | sed 's/^B_WARN|/    /'
fi

# --- Check 29: repo-wide markdown table structural integrity (delimiter + data rows) ---
echo "--- Check 29: repo-wide table delimiter/data-row column integrity ---"
# Consistency review #17 (2026-06-28) found 18 table defects no prior check saw:
# Check 13 scans only the summary docs and only compares DATA rows to the header — the
# delimiter (separator) row was never validated, and the 569 PA files were never scanned
# for either. GFM requires the delimiter row to match the header cell count or the table
# is NOT RECOGNIZED AT ALL (the block renders as plain text on GitHub). Defect classes
# found & repaired by 07-methodology/fix-table-structure.py (companion script):
#   (a) 9 delimiter rows missing columns (5-col Steps tables with 4-cell delimiters;
#       a 2-col Field/Detail table with a 1-cell delimiter) — VS-09 x3, VS-11, VS-13,
#       VS-20, VS-28, VS-29 x2;
#   (b) 7 delimiter rows with excess columns (2-col Field/Detail tables carrying a
#       4/5-cell steps-delimiter) — VS-105 x5, VS-133, VS-170;
#   (c) a doubled delimiter line under one header — VS-29 PA-29.2;
#   (d) a stray 1-cell '| **Steps** |' data row inside a 2-col Field/Detail table —
#       VS-162 PA-162.3.
# This check re-scans ALL .md files (code-fence aware, escaped-pipe aware — '\|' is a
# literal, not a cell separator, per CommonMark) for delimiter-vs-header mismatches and
# data-row-vs-header mismatches, so neither class can ship silently again. It subsumes
# Check 13's second half over a wider scope (13 is retained for its leading-whitespace
# guard and its focused summary-doc reporting).
CHECK29=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, sys
ROOT = sys.argv[1]
SEP = re.compile(r'^\|[\s:|-]+\|\s*$')
def ncells(s):
    return re.sub(r'\\\|', '', s).count('|') - 1
sep_bad, row_bad = [], []
for dirpath, _d, files in os.walk(ROOT):
    if os.sep + '.git' in dirpath or '__pycache__' in dirpath: continue
    for fn in sorted(files):
        if not fn.endswith('.md'): continue
        path = os.path.join(dirpath, fn)
        rel = os.path.relpath(path, ROOT)
        lines = open(path, encoding='utf-8', errors='replace').read().split('\n')
        fence = False; hdr = None
        for i, ln in enumerate(lines):
            if ln.startswith('```'): fence = not fence; hdr = None; continue
            if fence: continue
            if ln.startswith('|'):
                if SEP.match(ln):
                    if hdr is not None and ncells(ln) != hdr:
                        sep_bad.append(f"{rel}:{i+1} delimiter {ncells(ln)} cells vs header {hdr}: {ln[:50]}")
                    continue
                nxt = lines[i+1] if i+1 < len(lines) else ''
                if SEP.match(nxt):
                    hdr = ncells(ln); continue
                if hdr is not None and ncells(ln) != hdr:
                    row_bad.append(f"{rel}:{i+1} data row {ncells(ln)} cells vs header {hdr}: {ln[:50]}")
            else:
                hdr = None
print(f"SEP={len(sep_bad)} ROW={len(row_bad)}")
for x in sep_bad: print(f"SEP|{x}")
for x in row_bad: print(f"ROW|{x}")
PY
)
C29_SEP=$(echo "$CHECK29" | sed -n 's/^SEP=\([0-9]*\).*/\1/p')
C29_ROW=$(echo "$CHECK29" | sed -n 's/.*ROW=\([0-9]*\)$/\1/p')
if [ "${C29_SEP:-1}" -eq 0 ] && [ "${C29_ROW:-1}" -eq 0 ]; then
    ok "All markdown tables repo-wide (779 .md files incl. 569 PA files) have delimiter and data rows matching their header column count (code-fence & escaped-pipe aware)"
else
    error "Markdown table structural defects found (delimiter: $C29_SEP, data-row: $C29_ROW) — GFM will not recognize tables whose delimiter row mismatches the header; run 07-methodology/fix-table-structure.py:"
    echo "$CHECK29" | grep -E '^(SEP\||ROW\|)' | sed 's/^SEP|/    /; s/^ROW|/    /' | head -25
fi

# --- Check 30: PA TOC hygiene (completeness, duplicates, stray fragments) ---
echo "--- Check 30: PA-file TOC completeness & stray-fragment guard ---"
# Consistency review #18 (2026-06-28) found a defect class Check 23 cannot see: Check 23
# verifies every TOC ANCHOR resolves to a heading, but never asks whether the TOC is
# complete, de-duplicated, or free of debris. Found & repaired by
# 07-methodology/fix-toc-completeness.py (companion script):
#   (a) stray mid-file TOC fragments — nav lists left inside the workflow body when
#       appended workflows were merged (VS-04 PA-04.2: 6 lines; VS-06 PA-06.2: 2 lines);
#   (b) duplicate TOC entries (the ID-level symptom of (a));
#   (c) a shipped workflow heading with NO TOC entry (VS-12 PA-12.2: W1318 — invisible
#       in the file's navigation).
# Convention (WORKFLOW-FORMAT-GUIDE.md): the TOC indexes '## W…' (h2) workflows only —
# '### W…' parent/summary sub-workflows are deliberately not TOC-indexed.
CHECK30=$(python3 - "$REPO_ROOT" <<'PY'
import glob, os, re, sys
ROOT = sys.argv[1]
WF = os.path.join(ROOT, "01-model-company", "workflows")
TOC_LINE = re.compile(r"^- \[(W[^\]]+)\]\(#([^)]+)\)")
H2 = re.compile(r"^## (W\d+[A-Z]?(?:\.\d+[a-z]?)?)\. ")
stray = dup = missing = 0
for path in sorted(glob.glob(os.path.join(WF, "VS-*", "PA-*.md"))):
    rel = os.path.relpath(path, ROOT)
    lines = open(path, encoding="utf-8").read().split("\n")
    seen_first_wf = False
    toc, heads = [], []
    for i, ln in enumerate(lines, 1):
        if H2.match(ln):
            seen_first_wf = True
            heads.append(H2.match(ln).group(1))
        m = TOC_LINE.match(ln)
        if m:
            toc.append(re.match(r"(W\d+[A-Z]?(?:\.\d+[a-z]?)?)", m.group(1)).group(1))
            if seen_first_wf:
                stray += 1
                print(f"STRAY|{rel}:{i}: TOC line after first workflow heading")
    for w, c in __import__("collections").Counter(toc).items():
        if c > 1:
            dup += 1
            print(f"DUP|{rel}: TOC entry {w} listed {c}x")
    for w in heads:
        if w not in toc:
            missing += 1
            print(f"MISS|{rel}: workflow {w} has no TOC entry")
print(f"TOTALS stray={stray} dup={dup} missing={missing}")
PY
)
C30_TOTALS=$(echo "$CHECK30" | sed -n 's/^TOTALS stray=\([0-9]*\) dup=\([0-9]*\) missing=\([0-9]*\)$/\1 \2 \3/p')
C30_STRAY=$(echo "$C30_TOTALS" | cut -d' ' -f1); C30_DUP=$(echo "$C30_TOTALS" | cut -d' ' -f2); C30_MISS=$(echo "$C30_TOTALS" | cut -d' ' -f3)
if [ "${C30_STRAY:-1}" -eq 0 ] && [ "${C30_DUP:-1}" -eq 0 ] && [ "${C30_MISS:-1}" -eq 0 ]; then
    ok "All 569 PA-file TOCs are complete (every ## workflow indexed), duplicate-free, and free of stray mid-file fragments"
else
    error "PA TOC hygiene defects found (stray: $C30_STRAY, duplicate: $C30_DUP, missing: $C30_MISS) — run 07-methodology/fix-toc-completeness.py:"
    echo "$CHECK30" | grep -E '^(STRAY\||DUP\||MISS\|)' | sed 's/^[A-Z]*|/    /' | head -25
fi

# --- Check 31: PA-name 3-way consistency (H1 vs VS-README row vs index bullet) ---
echo "--- Check 31: PA-name 3-way consistency ---"
# Consistency review #18 (2026-06-28) found 38 name drifts across the three places a
# process-area name is stated (PA file H1, VS README 'Process Areas' row, value-stream-index
# bullet) — 37 H1s that had drifted from the canonical index/README name (mostly
# Expansion-block shortenings like 'Coupon & Voucher Creation' vs 'Coupon & Voucher
# Creation & Distribution', 'and'/'&' and ':'/'—' variants) plus one VS README outlier
# (PA-69.1). Repaired by 07-methodology/fix-pa-names.py; canonical source = index bullet.
CHECK31=$(python3 - "$REPO_ROOT" <<'PY'
import glob, os, re, sys
ROOT = sys.argv[1]
WF = os.path.join(ROOT, "01-model-company", "workflows")
idx = open(os.path.join(WF, "value-stream-index.md"), encoding="utf-8").read()
idx_pa = {m.group(1): (m.group(2), m.group(3)) for m in re.finditer(
    r"^- \*\*(PA-\d+\.\d+)\*\* \[([^\]]+)\]\(([^)]+)\) — (\d+) workflows", idx, re.M)}
bad = 0
for vsdir in sorted(glob.glob(os.path.join(WF, "VS-*"))):
    vrd = open(os.path.join(vsdir, "README.md"), encoding="utf-8").read()
    vr = {m.group(1): (m.group(3).strip(), m.group(2)) for m in re.finditer(
        r"^\| \[(PA-\d+\.\d+)\]\(([^)]+)\) \| ([^|]+) \| \d+ \|", vrd, re.M)}
    for p in sorted(glob.glob(os.path.join(vsdir, "PA-*.md"))):
        pid = re.match(r"(PA-\d+\.\d+)-", os.path.basename(p)).group(1)
        rel = os.path.relpath(p, ROOT)
        h1 = open(p, encoding="utf-8").read().split("\n", 1)[0]
        if pid not in idx_pa:
            bad += 1; print(f"BAD|{rel}: PA absent from value-stream-index bullets"); continue
        cname, clink = idx_pa[pid]
        if h1 != f"# {pid} — {cname}":
            bad += 1; print(f"BAD|{rel}: H1 {h1!r} != canonical '# {pid} — {cname}'")
        if pid in vr:
            rname, rlink = vr[pid]
            if rname != cname:
                bad += 1; print(f"BAD|{os.path.relpath(vsdir, ROOT)}/README.md: {pid} row name {rname!r} != canonical {cname!r}")
            if os.path.basename(p) != rlink:
                bad += 1; print(f"BAD|{os.path.relpath(vsdir, ROOT)}/README.md: {pid} links {rlink!r} != file {os.path.basename(p)!r}")
        else:
            bad += 1; print(f"BAD|{os.path.relpath(vsdir, ROOT)}/README.md: {pid} has no Process Areas row")
print(f"TOTALS bad={bad}")
PY
)
C31_BAD=$(echo "$CHECK31" | sed -n 's/^TOTALS bad=\([0-9]*\)$/\1/p')
if [ "${C31_BAD:-1}" -eq 0 ]; then
    ok "All 569 process-area names agree 3-way (PA-file H1 == VS-README row == value-stream-index bullet, canonical = index)"
else
    error "PA-name drift found ($C31_BAD location(s)) — run 07-methodology/fix-pa-names.py (canonical source: value-stream-index.md):"
    echo "$CHECK31" | grep -E '^BAD\|' | sed 's/^BAD|/    /' | head -25
fi

# --- Check 32: Dangling requirement-ID citations in workflow/PA and summary docs ---
echo "--- Check 32: Requirement-ID citation resolution (workflow catalog) ---"
CHECK32=$(python3 - "$REPO_ROOT" <<'PY'
import re, os, glob, collections, sys
ROOT = os.path.join(sys.argv[1], "01-model-company")
# Canonical requirement IDs from erp-requirements.md table rows
defined = set()
for line in open(os.path.join(ROOT, "erp-requirements.md"), encoding="utf-8"):
    m = re.match(r"^\| ([A-Z]{2,5}-\d+[a-z]?) \|", line)
    if m:
        defined.add(m.group(1))
# Non-requirement tokens that match the ID shape: standards, laws, shift times,
# project codes, intra-file sub-step labels (NR-10/11), dependency-map row IDs (CIRC-xxx)
EXEMPT = {"ISPM-15", "EAN-13", "COVID-19", "DOLE-174", "ITF-14", "GTIN-13", "GTIN-14",
          "NR-10", "NR-11", "PM-10", "RG-59", "BRD-001", "PFRS-15"}
prefixes = ("VS-", "PA-", "CTL-", "CIRC-")
pat = re.compile(r"\b([A-Z]{2,5}-\d{2,3}[a-z]?)\b")
bad = collections.Counter()
where = collections.defaultdict(set)
files = [os.path.join(ROOT, "erp-requirements.md"), os.path.join(ROOT, "requirement-workflow-matrix.md")]
files = [f for f in files if os.path.exists(f)]
scan = set(glob.glob(os.path.join(ROOT, "workflows", "**", "*.md"), recursive=True)) - set(files)
# Review #23: also scan the surfaces outside the workflow catalog — the controls
# matrix (five shipped dangling citations of review #22-removed IDs lived in its
# Req Ref column) plus the summary/methodology docs and the root README.
scan |= {os.path.join(ROOT, f) for f in (
    "internal-controls-matrix.md", "model-company-profile.md", "executive-summary.md",
    "assumptions-and-design-decisions.md", "data-migration-mapping.md",
    "data-volumes-and-integrations.md", "mobile-app-strategy.md",
    "headcount-reality-check.md") if os.path.exists(os.path.join(ROOT, f))}
for extra in (os.path.join(sys.argv[1], "README.md"),
              os.path.join(sys.argv[1], "07-methodology", "technical-guidelines.md")):
    if os.path.exists(extra):
        scan.add(extra)
for f in sorted(scan):
    for m in pat.finditer(open(f, encoding="utf-8").read()):
        rid = m.group(1)
        if rid in defined or rid in EXEMPT or rid.startswith(prefixes):
            continue
        if re.fullmatch(r"W\d+[a-z]?", rid):
            continue
        bad[rid] += 1
        where[rid].add(os.path.relpath(f, ROOT))
for rid in sorted(bad):
    print(f"BAD|{rid} x{bad[rid]} in {sorted(where[rid])[:4]}")
print(f"TOTALS ids={len(bad)} refs={sum(bad.values())} defined={len(defined)}")
PY
)
C32_IDS=$(echo "$CHECK32" | sed -n 's/^TOTALS ids=\([0-9]*\) refs=.*/\1/p')
if [ "${C32_IDS:-1}" -eq 0 ]; then
    ok "All requirement-ID citations across the workflow catalog resolve to a defined erp-requirements.md row"
else
    error "Dangling requirement-ID citations found ($C32_IDS distinct ID(s)) — remap to the canonical requirement ID (see Check 4 for the matrix equivalent):"
    echo "$CHECK32" | grep -E '^BAD\|' | sed 's/^BAD|/    /' | head -25
fi

# --- Check 33: Workflow-reference resolution inside PA bodies & VS READMEs ---
echo "--- Check 33: Workflow-reference resolution (PA bodies & VS READMEs) ---"
# Checks 6/7 validate W-references in the four cross-reference docs only; nothing
# previously verified the citations inside the 569 PA files themselves or the 188
# VS READMEs (review #20 found 19 dangling tokens there: zero-padded W01/W03/W05,
# a PA reference written in the W namespace (W03.4), phantom W413/W1593/W6796 and
# PA-file-slug citations W05.2). Every \bW\d{1,4}[A-Z]?\b token outside workflow
# headings must resolve to a '##'/'###' workflow header ID defined anywhere in the
# catalog (sub-step refs like W14.8 and sub-workflow refs like W13.9a reduce to their
# base id W14/W13 by the \b boundary).
CHECK33=$(python3 - "$REPO_ROOT" <<'PY'
import re, os, glob, collections, sys
ROOT = os.path.join(sys.argv[1], "01-model-company")
defined = set()
pa_files = []
for f in glob.glob(os.path.join(ROOT, "workflows", "VS-*", "PA-*.md")):
    pa_files.append(f)
    for line in open(f, encoding="utf-8"):
        m = re.match(r"^#{2,3} (W\d+[A-Z]?)\.", line)
        if m:
            defined.add(m.group(1))
bad = collections.Counter()
where = collections.defaultdict(set)
scan = set(glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True))
for f in sorted(scan):
    for i, line in enumerate(open(f, encoding="utf-8"), 1):
        if re.match(r"^#{2,3} W\d", line):
            continue
        for m in re.finditer(r"\b(W\d{1,4}[A-Z]?)\b", line):
            w = m.group(1)
            if w not in defined:
                bad[w] += 1
                where[w].add(os.path.relpath(f, ROOT) + f":{i}")
for w in sorted(bad):
    print(f"BAD|{w} x{bad[w]} e.g. {sorted(where[w])[:3]}")
print(f"TOTALS ids={len(bad)} refs={sum(bad.values())} defined={len(defined)}")
PY
)
C33_IDS=$(echo "$CHECK33" | sed -n 's/^TOTALS ids=\([0-9]*\) refs=.*/\1/p')
if [ "${C33_IDS:-1}" -eq 0 ]; then
    ok "All workflow-ID citations across the model-company docs (PA bodies, VS READMEs, summary docs) resolve to a defined workflow header"
else
    error "Dangling workflow-ID citations found ($C33_IDS distinct ID(s)) — remap to the canonical workflow/VS id (see fix-pa-wrefs.py for the review #20 precedent):"
    echo "$CHECK33" | grep -E '^BAD\|' | sed 's/^BAD|/    /' | head -25
fi

# --- Check 34: CTL-240–808 PA-control objective names match canonical PA names ---
echo "--- Check 34: PA-control objective canonical-name agreement ---"
# add-pa-controls.py derived objective names from PA file slugs (mangling proper nouns:
# S&OP->Sandop, DENR->Denr, ERP->Erp, DC->Dc, B2B->B2b) and backfill-controls.py
# truncated them to 90 chars mid-word; fix-ctl-pa-names.py (review #20) canonicalized
# both surfaces to the value-stream-index bullet names. This guard verifies:
#   (a) every matrix row 'Ensure controlled execution — <name> (PA-XX.Y)' carries the
#       canonical index name of its PA;
#   (b) every PA-body 'CTL-NNN (ensure controlled execution — ...)' parenthetical is
#       the exact canonical rendering of its register row.
CHECK34=$(python3 - "$REPO_ROOT" <<'PY'
import re, os, glob, collections, sys
ROOT = os.path.join(sys.argv[1], "01-model-company")
canon = {}
for m in re.finditer(r"- \*\*(PA-\d{2,3}\.\d)\*\* \[([^\]]+)\]\(",
                     open(os.path.join(ROOT, "workflows", "value-stream-index.md"), encoding="utf-8").read()):
    canon[m.group(1)] = m.group(2)
row = re.compile(r"^\| (CTL-\d{3}) \| Ensure controlled execution — (.+?) \((PA-\d{2,3}\.\d)\) \|")
ctl2pa = {}
rows = 0
bad_matrix = []
for line in open(os.path.join(ROOT, "internal-controls-matrix.md"), encoding="utf-8"):
    m = row.match(line.rstrip("\n"))
    if not m:
        continue
    rows += 1
    ctl2pa[m.group(1)] = m.group(3)
    if m.group(2) != canon.get(m.group(3)):
        bad_matrix.append(f"{m.group(1)}: '{m.group(2)}' != canonical '{canon.get(m.group(3))}' (PA {m.group(3)})")
bad_body = collections.Counter()
where = collections.defaultdict(list)
bpat = re.compile(r"(CTL-\d{3}) \(ensure controlled execution — .*?\.\)")
for f in glob.glob(os.path.join(ROOT, "workflows", "VS-*", "PA-*.md")):
    text = open(f, encoding="utf-8").read()
    for m in bpat.finditer(text):
        ctl = m.group(1)
        pa = ctl2pa.get(ctl)
        want = f"{ctl} (ensure controlled execution — {canon[pa]} ({pa}).)" if pa else None
        if m.group(0) != want:
            key = f"{ctl}: '{m.group(0)[:70]}...' != canonical" if pa else f"{ctl}: not a register PA-control row"
            bad_body[key] += 1
            where[key].append(os.path.relpath(f, ROOT))
for k in sorted(bad_matrix):
    print(f"BAD-MATRIX|{k}")
for k in sorted(bad_body):
    print(f"BAD-BODY|{k} x{bad_body[k]} e.g. {where[k][0]}")
print(f"TOTALS matrix_rows={rows} matrix_bad={len(bad_matrix)} body_bad={sum(bad_body.values())} pa_controls={len(ctl2pa)}")
PY
)
C34_BAD=$(echo "$CHECK34" | sed -n 's/^TOTALS matrix_rows=[0-9]* matrix_bad=\([0-9]*\) body_bad=\([0-9]*\).*/\1 \2/p')
C34_MBAD=$(echo "$C34_BAD" | cut -d' ' -f1)
C34_BBAD=$(echo "$C34_BAD" | cut -d' ' -f2)
if [ "${C34_MBAD:-1}" -eq 0 ] && [ "${C34_BBAD:-1}" -eq 0 ]; then
    ok "All 569 PA-control objectives (matrix + PA-body parentheticals) carry their canonical process-area name from value-stream-index.md"
else
    error "PA-control objective-name drift (matrix: $C34_MBAD, PA bodies: $C34_BBAD) — re-run 07-methodology/fix-ctl-pa-names.py:"
    echo "$CHECK34" | grep -E '^BAD-' | sed 's/^BAD-MATRIX|/    /; s/^BAD-BODY|/    /' | head -25
fi

# --- Check 35: VS-number citation resolution (catalog & summary docs) ---
echo "--- Check 35: Value-stream-number citation resolution ---"
# Checks 19/20 resolve link TARGETS and Checks 6/7/33 validate W… tokens, but nothing
# validated the VS… namespace itself. Consistency review #21 found 87 citations across
# 25 PA files of the form "(links to VS-469 DTI)" where 469 is not a value stream at
# all — it is workflow W469's number (Customer Complaint DTI Escalation), i.e. a
# workflow reference written in the VS namespace. Every phantom number matched an
# existing workflow whose title matched the surrounding gloss (VS-228→W228 sales
# commissions, VS-245→W245 vendor chargebacks, VS-289→W289 pricing master,
# VS-399→W399 asset register, VS-4398→W4398 wayfinding, …); all repaired by the new
# 07-methodology/fix-vs-wrefs.py. This check enforces the invariant that fixed:
# every `VS-<n>` token in every current-state doc must denote an ACTIVE value stream
# (or be a `VS-NN.M` process-area reference, or one of the two sanctioned retired-
# number forms — the 'VS-49–VS-52' range phrase and the 'former VS-49/VS-52' gap
# notes; CHANGELOG/workflow-gap-analysis are exempt as labelled historical records).
CHECK35=$(python3 - "$REPO_ROOT" <<'PY'
import os, re, glob, collections, sys
ROOT = sys.argv[1]
WF = os.path.join(ROOT, "01-model-company", "workflows")
active = {int(re.match(r"VS-(\d+)-", d).group(1))
          for d in os.listdir(WF) if re.match(r"VS-\d+-", d)
          and os.path.isdir(os.path.join(WF, d))}
SKIP = {"CHANGELOG.md", "workflow-gap-analysis.md"}
bad = collections.Counter()
where = collections.defaultdict(list)
for dirpath, _d, files in os.walk(ROOT):
    if os.sep + ".git" in dirpath or "__pycache__" in dirpath: continue
    for fn in sorted(files):
        if not fn.endswith(".md") or fn in SKIP: continue
        path = os.path.join(dirpath, fn)
        rel = os.path.relpath(path, ROOT)
        txt = open(path, encoding="utf-8", errors="replace").read()
        txt = re.sub(r"`[^`]*`", "", txt)  # inline-code spans are illustrative examples, not citations
        for m in re.finditer(r"\bVS-(\d{1,4})\b(?!\.\d)", txt):
            n = int(m.group(1))
            if n in active: continue
            ctx = txt[max(0, m.start() - 24):m.end() + 24]
            if re.search(r"VS-49\s*[\u2013\u2014-]+\s*(VS-)?52", ctx): continue  # retirement range-note
            if re.search(r"former\s+VS-(?:49|52)\b", ctx): continue             # 'filled the former VS-n gap' note
            bad[f"VS-{n}"] += 1
            where[f"VS-{n}"].append(f"{rel}:{txt.count(chr(10), 0, m.start()) + 1}")
print(f"TOTALS ids={len(bad)} refs={sum(bad.values())}")
for k in sorted(bad, key=lambda x: int(x[3:])):
    print(f"BAD|{k} x{bad[k]} e.g. {sorted(where[k])[:3]}")
PY
)
C35_IDS=$(echo "$CHECK35" | sed -n 's/^TOTALS ids=\([0-9]*\) refs=.*/\1/p')
if [ "${C35_IDS:-1}" -eq 0 ]; then
    ok "All VS-number citations across the model-company docs resolve to an active value stream (no workflow references written in the VS namespace)"
else
    error "Dangling/misnamespaced VS-number citations found ($C35_IDS distinct id(s)) — remap to the canonical workflow id (see fix-vs-wrefs.py for the review #21 precedent):"
    echo "$CHECK35" | grep -E '^BAD\|' | sed 's/^BAD|/    /' | head -25
fi

# --- Check 36: duplicate requirement titles in erp-requirements.md ---
echo "--- Check 36: Duplicate requirement titles (erp-requirements.md register) ---"
# Consistency review #22 (2026-08-24) found five exact-duplicate requirement rows no prior
# check saw: Checks 4/28/32 validate requirement ID *tokens* and TOC claims, but never the
# titles. PUR-015 duplicated FIN-019 (same title, same primary workflow W27), WSL-002
# duplicated CRM-012 + CRM-013 (W103; its extra scope is CRM-013), and WMS-009–011
# duplicated WHL-001–003 (same titles, same primary workflows W584/W585/W586). Two IDs for
# one capability is an ambiguity defect: any consumer citing the capability cannot tell
# which ID is canonical, and the duplicate rows drifted independently (priorities differed:
# WHL-001 S vs WMS-009 M, WMS-011 S vs WHL-003 M). All five rows were removed (total
# 733 -> 728; see erp-requirements.md v24.0 note); this check enforces title uniqueness so
# a future authoring round cannot re-register an existing capability under a new prefix.
CHECK36=$(python3 - "$REPO_ROOT" <<'PY'
import collections, re, sys
path = sys.argv[1] + "/01-model-company/erp-requirements.md"
titles = collections.defaultdict(list)
for line in open(path, encoding="utf-8"):
    m = re.match(r"^\| ([A-Z]{2,5}-\d+[ab]?) \| (.+?) \|", line)
    if m:
        titles[m.group(2).strip().lower()].append(m.group(1))
dups = {t: ids for t, ids in titles.items() if len(ids) > 1}
n = sum(len(v) for v in dups.values())
for t, ids in sorted(dups.items()):
    print(f"DUP|{' / '.join(sorted(ids))}: {t}")
print(f"TOTALS dup_titles={len(dups)} dup_rows={n}")
PY
)
C36_DUPS=$(echo "$CHECK36" | sed -n 's/^TOTALS dup_titles=\([0-9]*\) dup_rows=[0-9]*/\1/p')
if [ "${C36_DUPS:-1}" -eq 0 ]; then
    ok "All 728 erp-requirements.md requirement titles are unique across all 38 prefix categories (no capability registered twice under different IDs)"
else
    error "Duplicate requirement titles found ($C36_DUPS distinct title(s)) — merge into one canonical row and remap citations (see erp-requirements.md v24.0 note for the review #22 precedent):"
    echo "$CHECK36" | grep -E '^DUP\|' | sed 's/^DUP|/    /'
fi

# --- Check 37: Requirement priority-split figures vs the erp-requirements.md register ---
echo "--- Check 37: Priority-split figure agreement ---"
# Review #22 removed five requirement rows (733 -> 728; 429 Must / 293 Should / 6 Nice)
# but two prose surfaces kept quoting the pre-removal split (431/296): the classification
# doc's Classification Rules intro and the root-README Key Metrics table. No prior check
# compared quoted priority counts against the register itself, so this check derives the
# canonical split from the register rows and validates every quoted figure against it.
CHECK37=$(python3 - "$REPO_ROOT" <<'PY'
import re, os, glob, sys
ROOT = sys.argv[1]
counts = {"Must Have": 0, "Should Have": 0, "Nice to Have": 0}
for line in open(os.path.join(ROOT, "01-model-company", "erp-requirements.md"), encoding="utf-8"):
    m = re.match(r"^\| [A-Z]{2,5}-\d+[ab]? \| .+? \| (Must Have|Should Have|Nice to Have) \|", line)
    if m:
        counts[m.group(1)] += 1
derived = (counts["Must Have"], counts["Should Have"], counts["Nice to Have"])
bad = []
def note(where, label, got):
    if tuple(got) != derived:
        bad.append(f"{where}: {label} figures {tuple(got)} != register {derived}")
def ints(m):
    return tuple(int(x.replace(",", "")) for x in m.groups())
tiers = ("Must Have", "Should Have", "Nice to Have")
# Surface 1: classification doc 'Classification Rules' '**X requirements** (N)' claims
text = open(os.path.join(ROOT, "01-model-company/workflows/workflow-criticality-classification.md"), encoding="utf-8").read()
got = []
for tier in tiers:
    m = re.search(r"\*\*" + tier + r" requirements\*\* \(([\d,]+)\)", text)
    got.append(int(m.group(1).replace(",", "")) if m else -1)
note("workflow-criticality-classification.md Classification Rules", "priority-split", got)
# Surface 2: root-README Key Metrics '| X Requirements | N |' rows
text = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
got = []
for tier in tiers:
    m = re.search(r"\| " + tier + r" Requirements \| ([\d,]+) \|", text)
    got.append(int(m.group(1).replace(",", "")) if m else -1)
note("root README Key Metrics", "priority-split", got)
# Surface 3: repo-wide 'A Must / B Should / C Nice' numeric triples (historical records excluded)
for f in glob.glob(ROOT + "/**/*.md", recursive=True):
    rel = os.path.relpath(f, ROOT)
    if rel.startswith("CHANGELOG") or "workflow-gap-analysis" in rel:
        continue
    for m in re.finditer(r"\b(\d[\d,]*) Must[^.\n]*?\b(\d[\d,]*) Should[^.\n]*?\b(\d[\d,]*) Nice\b", open(f, encoding="utf-8").read()):
        trip = ints(m)
        if trip != derived:
            note(rel, "'N Must / M Should / K Nice'", trip)
print(f"TOTALS derived={derived} mismatches={len(bad)}")
for b in bad:
    print("BAD|" + b)
PY
)
C37_BAD=$(echo "$CHECK37" | sed -n 's/^TOTALS derived=.* mismatches=\([0-9]*\)/\1/p')
if [ "${C37_BAD:-1}" -eq 0 ]; then
    ok "All quoted requirement priority-split figures match the erp-requirements.md register (429 Must / 293 Should / 6 Nice)"
else
    error "Quoted priority-split figures disagree with the erp-requirements.md register (see BAD lines for derived counts):"
    echo "$CHECK37" | grep -E '^BAD\|' | sed 's/^BAD|/    /'
fi

# --- Check 38: Requirements-TOC count-column agreement vs the register rows ---
echo "--- Check 38: Requirements-TOC count-column agreement ---"
# Review #22 updated R3 (45 -> 44) and R16 (8 -> 7) in the erp-requirements.md TOC
# when it removed five duplicate rows, but missed R4: retiring WMS-009–011 shrank
# R4's defined complement 26 -> 23 while its Count cell stayed at 26, so the Count
# column summed to 731 against the doc's own 'Total: 728' line. No prior check
# compared the TOC's per-section Counts against the register rows themselves.
CHECK38=$(python3 - "$REPO_ROOT" <<'PY'
import re, os, sys
ROOT = sys.argv[1]
path = os.path.join(ROOT, "01-model-company", "erp-requirements.md")
lines = open(path, encoding="utf-8").read().splitlines()
# actual defined rows per prefix
cnt = {}
for line in lines:
    m = re.match(r"^\| ([A-Z]{2,5}-\d+[a-z]?) \|", line)
    if m:
        pre = m.group(1).split("-")[0]
        cnt[pre] = cnt.get(pre, 0) + 1
bad = []
sum_counts = 0
for line in lines:
    if not line.startswith("| [R") and not line.startswith("| — | Additional"):
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) < 4 or not cells[3].isdigit():
        continue
    claimed = int(cells[3])
    sum_counts += claimed
    # prefixes from the Req IDs cell (skip cells without ID tokens, e.g. 'Various')
    prefixes = sorted({t.split("-")[0] for t in re.findall(r"\b[A-Z]{2,5}-\d+", cells[2])})
    if not prefixes:
        continue
    actual = sum(cnt.get(p, 0) for p in prefixes)
    if actual != claimed:
        bad.append(f"{cells[1]} ({', '.join(prefixes)}): Count {claimed} != {actual} defined rows")
# Total line vs actual register size vs Count-column sum
mtot = re.search(r"\*\*Total: ([\d,]+) unique requirements\*\*", "\n".join(lines))
total_line = int(mtot.group(1).replace(",", "")) if mtot else -1
if total_line != len([k for k in cnt for _ in range(cnt[k])]):
    bad.append(f"Total line {total_line} != {sum(cnt.values())} defined register rows")
if sum_counts != total_line:
    bad.append(f"Count column sums to {sum_counts} != Total-line figure {total_line}")
print(f"TOTALS total_line={total_line} defined={sum(cnt.values())} count_col_sum={sum_counts} mismatches={len(bad)}")
for b in bad:
    print("BAD|" + b)
PY
)
C38_BAD=$(echo "$CHECK38" | sed -n 's/^TOTALS .* mismatches=\([0-9]*\)/\1/p')
if [ "${C38_BAD:-1}" -eq 0 ]; then
    ok "erp-requirements.md TOC Count column agrees with the register (per-row and 728-total)"
else
    error "Requirements-TOC Count column disagrees with the erp-requirements.md register:"
    echo "$CHECK38" | grep -E '^BAD\|' | sed 's/^BAD|/    /'
fi

# --- Check 39: Namespace & listing integrity (dup W headers, VS listings, CTL/PA citations, cross-file anchors) ---
echo "--- Check 39: Namespace & listing integrity ---"
# Regression guards for invariants verified manually in reviews #22/#23 but never
# codified: unique workflow headers across PA files (the 5,372-header / 5,349-unique
# register complement); repo-wide CTL-ID and PA-N.N citation resolution; cross-file
# markdown anchor links resolving to a heading. (VS READMEs aggregate workflows by
# process-area count rather than enumerating W-numbers — that count agreement is
# already guarded by Checks 2, 24 and 31.)
CHECK39=$(python3 - "$REPO_ROOT" <<'PY'
import re, os, glob, collections, sys
ROOT = os.path.join(sys.argv[1], "01-model-company")
bad = []
# A. duplicate W headers across PA files
wdef = collections.Counter(); where = {}
hdr = re.compile(r"^#{2,4} (W\d+[A-Za-z]?)[\.\s]")
for f in glob.glob(os.path.join(ROOT, "workflows", "**", "PA-*.md"), recursive=True):
    for line in open(f, encoding="utf-8"):
        m = hdr.match(line)
        if m:
            wdef[m.group(1)] += 1; where.setdefault(m.group(1), f)
dups = {k: v for k, v in wdef.items() if v > 1}
if dups:
    bad.append(f"duplicate workflow headers: {dict(list(dups.items())[:5])}")
# B. CTL-ID citation resolution repo-wide
ctl = set()
for line in open(os.path.join(ROOT, "internal-controls-matrix.md"), encoding="utf-8"):
    m = re.match(r"^\| (CTL-\d+) \|", line)
    if m: ctl.add(m.group(1))
scan = glob.glob(ROOT + "/**/*.md", recursive=True) + [
    os.path.join(sys.argv[1], "README.md"),
    os.path.join(sys.argv[1], "07-methodology", "technical-guidelines.md")]
dang_ctl, dang_pa = [], []
padef = {re.match(r"(PA-\d+\.\d+)-", os.path.basename(f)).group(1)
         for f in glob.glob(os.path.join(ROOT, "workflows", "**", "*.md"), recursive=True)
         if re.match(r"(PA-\d+\.\d+)-", os.path.basename(f))}
for f in scan:
    txt = re.sub(r"```.*?```", "", open(f, encoding="utf-8").read(), flags=re.S)
    rel = os.path.relpath(f, ROOT)
    for m in re.finditer(r"\b(CTL-\d+)\b", txt):
        if m.group(1) not in ctl: dang_ctl.append(f"{rel}:{m.group(1)}")
    for m in re.finditer(r"\b(PA-\d+\.\d+)\b", txt):
        if m.group(1) not in padef: dang_pa.append(f"{rel}:{m.group(1)}")
if dang_ctl:
    bad.append(f"dangling CTL citations: {sorted(set(dang_ctl))[:5]} ({len(dang_ctl)} refs)")
if dang_pa:
    bad.append(f"dangling PA-number citations: {sorted(set(dang_pa))[:5]} ({len(dang_pa)} refs)")
# D. cross-file markdown anchor resolution
def slug(h):
    s = h.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    return re.sub(r"\s+", "-", s)
broke = 0; broke_ex = []
for f in glob.glob(sys.argv[1] + "/**/*.md", recursive=True):
    if os.sep + ".git" + os.sep in f: continue
    base = os.path.dirname(f)
    txt = re.sub(r"```.*?```", "", open(f, encoding="utf-8").read(), flags=re.S)
    for m in re.finditer(r"\]\(([^)#\s]+\.md)(#[^)\s]+)?\)", txt):
        tp = os.path.normpath(os.path.join(base, m.group(1)))
        if not os.path.exists(tp) or not m.group(2):
            continue
        heads = set()
        for line in open(tp, encoding="utf-8"):
            hm = re.match(r"^#+\s+(.*)", line)
            if hm: heads.add(slug(hm.group(1)))
            em = re.search(r'<a name="([^"]+)"', line)
            if em: heads.add(em.group(1).lower())
        if m.group(2)[1:].lower() not in heads:
            broke += 1
            if len(broke_ex) < 5:
                broke_ex.append(f"{os.path.relpath(f, ROOT)} -> {m.group(1)}{m.group(2)}")
if broke:
    bad.append(f"broken cross-file anchors: {broke} (e.g. {'; '.join(broke_ex)})")
print(f"TOTALS headers={len(wdef)} problems={len(bad)}")
for b in bad:
    print("BAD|" + b)
PY
)
C39_BAD=$(echo "$CHECK39" | sed -n 's/^TOTALS .* problems=\([0-9]*\)/\1/p')
if [ "${C39_BAD:-1}" -eq 0 ]; then
    C39_HDRS=$(echo "$CHECK39" | sed -n 's/^TOTALS headers=\([0-9]*\) .*/\1/p')
    ok "Namespace integrity: ${C39_HDRS} workflow headers unique; all CTL & PA-N.N citations resolve; all cross-file anchors resolve"
else
    error "Namespace/listing integrity violations found:"
    echo "$CHECK39" | grep -E '^BAD\|' | sed 's/^BAD|/    /'
fi

echo ""
echo "=== Validation Complete ==="
echo "Errors: $ERRORS, Warnings: $WARNINGS"
if [ "$ERRORS" -eq 0 ]; then
    echo -e "${GREEN}All checks passed (warnings are informational)${NC}"
else
    echo -e "${RED}Some checks failed — review errors above${NC}"
    exit 1
fi
