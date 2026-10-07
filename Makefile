# erpplans — validation & generation entry points
#
# The markdown corpus under 01-model-company/workflows/ is the single source of
# truth; bpmn/ and dmn/ are generated projections. The canonical loop is:
#
#     edit markdown  ->  make generate  ->  make validate
#
# `make check` runs everything the CI workflow (.github/workflows/validate.yml)
# runs, in the same order. `make idempotent` assumes bpmn/ and dmn/ are clean
# at the start (true on a fresh checkout / in CI); with local uncommitted tree
# changes, commit first or judge the diff by hand.

PYTHON ?= python3

.PHONY: help validate validate-sync generate idempotent teeth check

help:
	@echo "erpplans entry points"
	@echo "  make validate       run the 76-check cross-reference validator (prefetch mode, ~8s)"
	@echo "  make validate-sync  run the validator in synchronous mode (VALIDATE_NO_PREFETCH=1)"
	@echo "  make generate       regenerate bpmn/ and dmn/ from the workflow markdown"
	@echo "  make idempotent     generate, then fail if bpmn/ or dmn/ drifted (needs a clean tree)"
	@echo "  make teeth          fault-injection suite for the validator itself (~2 min; never touches the live tree)"
	@echo "  make check          everything CI runs: validate + idempotent + teeth"

validate:
	bash 07-methodology/validate-repo.sh

validate-sync:
	VALIDATE_NO_PREFETCH=1 bash 07-methodology/validate-repo.sh

generate:
	$(PYTHON) 07-methodology/generate-bpmn.py
	$(PYTHON) 07-methodology/generate-dmn.py

idempotent: generate
	@git diff --exit-code -- bpmn dmn && echo "generators idempotent: bpmn/ and dmn/ byte-identical after regeneration"

teeth:
	$(PYTHON) 07-methodology/run-teeth.py

check: validate idempotent teeth
	@echo "check: validator green, generators idempotent, all teeth fired"
