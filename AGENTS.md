# Agent Operations Guide

This file defines repository-specific execution behavior for coding agents.

Canonical philosophy, policy, and governance live in `RESEARCH_SOFTWARE_AI_POLICY.md`.

## Defaults

1. Follow `RESEARCH_SOFTWARE_AI_POLICY.md`.
2. Prefer existing project tooling and conventions.
3. Keep changes minimal, testable, and maintainable.
4. Improve contributor understanding while preserving productivity.

## Workflow

For non-trivial work:

1. Clarify objective, constraints, and assumptions.
2. Read relevant files before editing.
3. Implement the smallest coherent change.
4. Validate with relevant checks.
5. Report what changed, why, and how it was verified.

## Validation

- Use existing `make` targets where possible: `make test`, `make format`, `make lint`, `make type`, `make docs`, `make check-full`.
- Add or update tests when behavior changes.
- If validation cannot be run, state what was skipped and why.

## Repo Practices

- Keep code modular and close tests to behavior.
- Preserve documentation quality in `README.md`, module docstrings, and notebooks.
- Keep notebooks focused and move reusable logic to modules.

## Ownership

- Update `RESEARCH_SOFTWARE_AI_POLICY.md` for philosophy or policy changes.
- Update `AGENTS.md` for operational workflow changes.
- Update `.github/copilot-instructions.md` only for GitHub-specific adapter behavior.
