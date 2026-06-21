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
    ok "Automation Opportunity and Controls are present on all $TOTAL_WF workflows (100%)"
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
if intro_m:
    unc=int(intro_m.group(1).replace(",","")); tot=int(intro_m.group(2).replace(",","")); cls=int(intro_m.group(3).replace(",",""))
    if tot-cls!=unc:
        errs.append(f"Intro banner arithmetic wrong: {tot:,} total − {cls:,} classified = {tot-cls:,}, but states {unc:,} unclassified")
    if gt_m:
        g=int(gt_m.group(1).replace(",","")); c=int(gt_m.group(2).replace(",","")); u=int(gt_m.group(3).replace(",",""))
        if tot!=g: errs.append(f"Intro banner grand total ({tot:,}) != Summary Grand Total unique ({g:,})")
        if cls!=c: errs.append(f"Intro banner classified ({cls:,}) != Summary Grand Total confirmed-unique ({c:,})")
        if unc!=u: errs.append(f"Intro banner unclassified ({unc:,}) != Summary Grand Total unclassified ({u:,})")
else:
    errs.append("Could not locate intro-banner 'An additional N workflows (M total − K classified)' sentence")
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
# all 565 PA files: VS-56 PA-56.1's header linked to '../value-stream.md' instead of
# '../value-stream-index.md'. No other check sees this — Check 2 compares header COUNTS, Check 7
# validates workflow-IDs, and Check 19 scopes only the index. This check resolves every
# relative (./ or ../) intra-repo .md link inside every PA file so the drift cannot recur.
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
    ok "All $PA_LINK_TOTAL relative links across all 565 PA files resolve to a file"
else
    error "$BROKEN_PA_COUNT PA-file relative link(s) do not resolve to a file:"
    echo "$BROKEN_PA_BODY" | sed 's/^/    /'
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
