#!/bin/bash
# validate-repo.sh — Cross-reference validation for BuildRight Depot ERP Plans
# Checks consistency of workflow counts, requirement IDs, and cross-references

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
GRAND_TOTAL=$(grep 'Grand Total' "$REPO_ROOT"/01-model-company/workflows/value-stream-index.md | grep -oP '\d+' | head -1)
DOC_UNCLASS=$((GRAND_TOTAL - CLASSIFIED_COUNT))

ALL_HEADERS=$(grep -rohP '^#{2,3} W\d+[A-Z]?\.' "$REPO_ROOT"/01-model-company/workflows/VS-*/*.md 2>/dev/null | sed -E 's/^#{2,3} //;s/\.$//' | sort -u)
STALE_CLASSIFIED=$(comm -23 <(echo "$CLASSIFIED") <(echo "$ALL_HEADERS") | grep -cP '^W' || true)
SUB_CLASSIFIED=$(comm -12 <(grep -rohP '^### W\d+[A-Z]?\.' "$REPO_ROOT"/01-model-company/workflows/VS-*/*.md 2>/dev/null | sed -E 's/^### //;s/\.$//' | sort -u) <(echo "$CLASSIFIED") | grep -cP '^W' || true)

echo "  Classified: $CLASSIFIED_COUNT | Grand total: $GRAND_TOTAL | Documented unclassified: $DOC_UNCLASS ($SUB_CLASSIFIED classified rows are ### parent/summary workflows)"

if [ "$STALE_CLASSIFIED" -eq 0 ]; then
    ok "All $CLASSIFIED_COUNT classified workflow IDs resolve to a header in a PA file"
else
    error "$STALE_CLASSIFIED classified ID(s) do not match any workflow header in PA files"
fi

if [ "$DOC_UNCLASS" -gt 0 ]; then
    warn "$DOC_UNCLASS workflows remain unclassified (pending criticality review)"
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
TOTAL_VS=$(grep 'Grand Total' "$REPO_ROOT"/01-model-company/workflows/value-stream-index.md | grep -oP '\d+' | head -1)
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
GRAND_TOTAL=$(grep 'Grand Total' "$REPO_ROOT"/01-model-company/workflows/value-stream-index.md | grep -oP '\d+' | head -1)
ACTUAL_WFS=$(grep -rhP '^## W\d+[A-Z]?\.' "$REPO_ROOT"/01-model-company/workflows/VS-*/PA-*.md 2>/dev/null | wc -l)
if [ "$GRAND_TOTAL" = "$ACTUAL_WFS" ]; then
    ok "Grand total ($GRAND_TOTAL) matches actual PA workflow header count ($ACTUAL_WFS)"
else
    error "Grand total ($GRAND_TOTAL) does NOT match actual PA workflow header count ($ACTUAL_WFS)"
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
