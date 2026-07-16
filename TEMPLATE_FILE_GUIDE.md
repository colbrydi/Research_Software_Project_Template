# Template File Guide

This guide explains why each template file exists and whether it can be removed.

Decision labels:
- Keep: recommended for most student projects.
- Modify: keep the file path but replace or customize the content for your project.
- Optional: safe to remove if you are not using that workflow.
- Keep if used: remove only if your team confirms the feature is not needed.

## Core Files

| File | Why it exists | Can you delete it? |
|---|---|---|
| README.md | Main onboarding instructions and workflow overview. | Modify (replace for your project) |
| environment.yml | Reproducible conda environment setup. | Keep if using conda |
| makefile | Simple common commands for setup, test, lint, docs. | Keep |
| pyproject.toml | Central tool configuration (pytest, black, ruff, mypy). | Keep |
| mypackage/ | Starter Python package structure. | Modify (rename package and update modules) |
| mypackage/tests/ | Starter tests and testing patterns. | Modify (replace starter tests with project tests) |
| 00_START_HERE.ipynb | Guided walkthrough notebook for beginners. | Optional |
| LICENSE | Legal terms for use and sharing. | Modify (verify owner/year/license choice) |

## AI Guidance Layer

| File | Why it exists | Can you delete it? |
|---|---|---|
| RESEARCH_SOFTWARE_AI_POLICY.md | Canonical AI policy and quality principles. | Keep |
| AGENTS.md | Agent execution behavior tied to this repository. | Keep if using coding agents |
| AI_GUIDELINES.md | Backward-compatibility stub for older links/tools. | Optional |
| .github/copilot-instructions.md | GitHub Copilot-specific adapter file in expected location. | Keep if using Copilot |
| .cursorrules | Cursor adapter in expected discovery filename. | Keep if using Cursor |
| CLAUDE.md | Claude adapter. | Keep if using Claude |
| CODEX.md | Codex adapter. | Keep if using Codex |
| GEMINI.md | Gemini adapter. | Keep if using Gemini |

## Git/Automation Files

| File | Why it exists | Can you delete it? |
|---|---|---|
| .gitignore | Prevents accidental commits of generated files. | Keep |
| .pre-commit-config.yaml | Optional local checks before commit. | Optional |
| .secrets.baseline | Baseline for detect-secrets scanning. | Keep if using secrets scanning |
| .github/workflows/ci.yml | Automated test checks on push/PR. | Keep if using GitHub |
| .github/workflows/pages.yml | Optional automatic docs publishing. | Optional |
| .github/dependabot.yml | Optional automated dependency update PRs. | Optional |
| oryx-build-commands.txt | Optional build instructions for Oryx-based hosts. | Optional |
| .vscode/settings.json | Workspace-local VS Code setting. | Optional |

## Suggested Lean Profile (Minimal Starter)

If your class wants the smallest practical setup, keep these and remove the rest later as needed:
- README.md (modify immediately)
- environment.yml
- makefile
- pyproject.toml
- LICENSE (modify if needed)
- mypackage/ (rename and modify)
- mypackage/tests/ (modify)
- RESEARCH_SOFTWARE_AI_POLICY.md
- AGENTS.md
- .github/copilot-instructions.md (if using Copilot)
- .github/workflows/ci.yml (if using GitHub)

## Pass-By-Default Automation Notes

This template is set up so a fresh GitHub repository from template should pass CI without first-day debugging.

To keep that true after project renaming/customization, update these references together:
- package folder rename (`mypackage` -> your package name)
- [makefile](makefile): `MODULENAME`
- [pyproject.toml](pyproject.toml): `testpaths`
- [.github/workflows/pages.yml](.github/workflows/pages.yml): `pdoc ... mypackage` (if pages workflow is kept)

Recommended first validation after cloning/templating:
- run `make init`
- run `make test`
