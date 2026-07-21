# Agent Operations Guide

This file defines repository-specific execution behavior for coding agents.

Can I delete this?
- Keep if you use coding agents.
- If removed, preserve equivalent workflow guidance in another clearly discoverable file.

Canonical philosophy, policy, and governance live in `guides/ai-policy.md`.

## Defaults

1. Follow `guides/ai-policy.md`.
2. Prefer existing project tooling and conventions.
3. Keep changes minimal, testable, and maintainable.
4. Improve contributor understanding while preserving productivity.

## Workflow

For non-trivial work:

1. Clarify objective, constraints, and assumptions.
2. Read relevant files before editing.
3. Implement the smallest coherent change.
4. Validate proportionately using enabled tools or a small manual check.
5. Report what changed, why, and how it was verified.

## Validation

- Treat repository tools as optional unless the contributor or course has enabled them.
- When tests or checks are in use, add or update the smallest relevant validation for meaningful behavior changes.
- When they are not in use, suggest one small manual check the contributor can perform.
- Use existing `make` targets when the project uses `make`: `make test`, `make format`, `make lint`, `make type`, `make docs`, `make check-full`.
- If validation is skipped, state what was skipped and why.

## Repo Practices

- Keep code modular and close tests to behavior.
- Preserve documentation quality in `README.md`, module docstrings, and notebooks.
- Keep notebooks focused and move reusable logic to modules.

## Ownership

- Update `guides/ai-policy.md` for philosophy or policy changes.
- Update `AGENTS.md` for operational workflow changes.
- Update `.github/copilot-instructions.md` only for GitHub-specific adapter behavior.
