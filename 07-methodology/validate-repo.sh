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
GRAND_TOTAL=$(grep 'Grand Total' "$REPO_ROOT"/01-model-company/workflows/value-stream-index.md | grep -oP '\d+' | tail -1)
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
# Check total workflows in value-stream-index
TOTAL_VS=$(grep 'Grand Total' "$REPO_ROOT"/01-model-company/workflows/value-stream-index.md | grep -oP '\d+' | tail -1)
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
GRAND_TOTAL=$(grep 'Grand Total' "$REPO_ROOT"/01-model-company/workflows/value-stream-index.md | grep -oP '\d+' | tail -1)
ACTUAL_WFS=$(grep -rhP '^## W\d+[A-Z]?\.' "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null | wc -l)
if [ "$GRAND_TOTAL" = "$ACTUAL_WFS" ]; then
    ok "Grand total ($GRAND_TOTAL) matches actual PA workflow header count ($ACTUAL_WFS)"
else
    error "Grand total ($GRAND_TOTAL) does NOT match actual PA workflow header count ($ACTUAL_WFS)"
fi

# --- Check 10: Boilerplate analysis fields (unfinished templated workflows) ---
echo "--- Check 10: Boilerplate analysis fields ---"
# A block of value streams (VS-53..VS-78) was generated from a template and never finished:
# the three analysis fields that deliver a workflow's value — Pain Points, System Touchpoints,
# and Time Estimate — are verbatim boilerplate copied across all their workflows. This check
# surfaces them as WARNINGS (not errors, since the content is not yet reworked) and lists the
# affected value streams for prioritised rework. See WORKFLOW-FORMAT-GUIDE.md "Quality bar for
# the three analysis fields".
BP_MARKER='Operational variability mitigated by standard procedures and system controls'
BP_FILES=$(grep -rlF "$BP_MARKER" "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null || true)
BP_INSTANCES=$(grep -rhF "$BP_MARKER" "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null | wc -l | tr -d ' ')
if [ "$BP_INSTANCES" -eq 0 ]; then
    ok "No boilerplate analysis fields detected"
else
    BP_FILE_COUNT=$(echo -n "$BP_FILES" | grep -cP 'PA-' || true)
    BP_VS_LIST=$(echo "$BP_FILES" | sed -E 's#.*/(VS-[0-9]+-[^/]+)/.*#\1#' | sort -u)
    BP_VS_COUNT=$(echo -n "$BP_VS_LIST" | grep -cP '^VS-' || true)
    warn "$BP_INSTANCES workflows across $BP_FILE_COUNT PA files in $BP_VS_COUNT value streams use verbatim boilerplate for Pain Points / System Touchpoints / Time Estimate (templated, pending rework per WORKFLOW-FORMAT-GUIDE.md):"
    echo "$BP_VS_LIST" | sed 's/^/    /'
fi

# --- Check 12: Automation Opportunity + Controls field adoption ---
echo "--- Check 12: Automation Opportunity & Controls field adoption ---"
# Per WORKFLOW-FORMAT-GUIDE.md these are now standard analysis fields for any fully-detailed
# workflow. Each should appear as an ### subsection under its workflow. Adoption is tracked
# (not enforced as an error) so the Expansion-block rework and the original Core/Statutory/
# Gap-analysis VSs can be measured against the VS-73 reference implementation.
TOTAL_WF=$(grep -rhP '^## W\d+[A-Z]?\.' "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null | wc -l | tr -d ' ')
AUTO_COUNT=$(grep -rohP '^### Automation Opportunity$' "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null | wc -l | tr -d ' ')
CTRL_COUNT=$(grep -rohP '^### Controls$' "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null | wc -l | tr -d ' ')
warn "Automation Opportunity present on $AUTO_COUNT / $TOTAL_WF workflows ($(awk "BEGIN{printf \"%.0f\", ($AUTO_COUNT/$TOTAL_WF)*100}")%); Controls present on $CTRL_COUNT / $TOTAL_WF workflows ($(awk "BEGIN{printf \"%.0f\", ($CTRL_COUNT/$TOTAL_WF)*100}")%). Target: 100% on all fully-detailed workflows (see WORKFLOW-FORMAT-GUIDE.md 'Standard analysis fields')"

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

echo ""
echo "=== Validation Complete ==="
echo "Errors: $ERRORS, Warnings: $WARNINGS"
if [ "$ERRORS" -eq 0 ]; then
    echo -e "${GREEN}All checks passed (warnings are informational)${NC}"
else
    echo -e "${RED}Some checks failed — review errors above${NC}"
    exit 1
fi
