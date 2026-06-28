# Overview:
# - Purpose: Define simple, repeatable project commands.
# - Used by: The `make` command run by students and CI.
# - Adds: One-command workflows for setup, testing, and optional tooling.
# - Learn more: https://www.gnu.org/software/make/manual/make.html#Introduction
MODULENAME ?= mypackage
ENV_PREFIX ?= ./envs
CONDA_RUN = conda run --prefix $(ENV_PREFIX)

help:
	@echo ""
	@echo "Scientific software helper targets"
	@echo ""
	@echo "Bootstrap"
	@echo "  make init          Create/update environment at $(ENV_PREFIX)"
	@echo ""
	@echo "Quality"
	@echo "  make test          Run pytest with coverage"
	@echo "  make format        Run black"
	@echo "  make lint          Run ruff"
	@echo "  make type          Run mypy"
	@echo "  make doclint       Run pydocstyle"
	@echo "  make audit         Run dependency vulnerability scan"
	@echo "  make secrets       Run secret scan (working tree)"
	@echo "  make nb-clean      Strip notebook outputs/metadata"
	@echo "  make check-full    Run full quality suite"
	@echo ""
	@echo "Docs"
	@echo "  make docs          Build API docs in ./docs"
	@echo ""

init:
	conda env create --prefix $(ENV_PREFIX) --file environment.yml || conda env update --prefix $(ENV_PREFIX) --file environment.yml --prune

format:
	$(CONDA_RUN) black $(MODULENAME)

lint:
	$(CONDA_RUN) ruff check $(MODULENAME)

type:
	$(CONDA_RUN) mypy $(MODULENAME)

doclint:
	$(CONDA_RUN) pydocstyle $(MODULENAME)

audit:
	$(CONDA_RUN) pip-audit

secrets:
	$(CONDA_RUN) pre-commit run detect-secrets --all-files

nb-clean:
	$(CONDA_RUN) nbstripout --install
	find . -name "*.ipynb" -not -path "./envs/*" -print0 | xargs -0 -r $(CONDA_RUN) nbstripout

test:
	$(CONDA_RUN) pytest -v --cov=$(MODULENAME) --cov-report=term-missing $(MODULENAME)/tests

docs:
	rm -rf docs
	$(CONDA_RUN) pdoc --docformat google -o docs $(MODULENAME)

check-full: lint type doclint test

check: test

clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache .coverage htmlcov docs
	find . -type d -name __pycache__ -exec rm -rf {} +

.PHONY: help init format lint type doclint test docs check-full check clean
