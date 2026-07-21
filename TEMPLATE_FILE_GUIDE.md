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
| makefile | Optional reference workflow with simple common commands for setup, test, lint, and docs. | Optional (or keep if your team uses `make`) |
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
- makefile (if your class uses `make`)
- pyproject.toml
- LICENSE (modify if needed)
- mypackage/ (rename and modify)
- mypackage/tests/ (modify)
- RESEARCH_SOFTWARE_AI_POLICY.md
- AGENTS.md
- .github/copilot-instructions.md (if using Copilot)
- .github/workflows/ci.yml (if using GitHub)

## Rename `mypackage` (Your First Customization)

In Python, a *package* is the folder that holds code you can import into a notebook, script, or test. The template calls this folder `mypackage` only as a placeholder. Choose a short, lowercase name that describes your project, such as `soil_analysis`.

For example, if you rename `mypackage` to `soil_analysis`, make these matching changes:

1. Rename the folder `mypackage/` to `soil_analysis/`. The `__init__.py` file stays inside that renamed folder; it tells Python to treat the folder as importable code.
2. Change imports wherever they occur. For example, change:

   ```python
   from mypackage import power_self
   ```

   to:

   ```python
   from soil_analysis import power_self
   ```

   In this template, check the test file and `00_START_HERE.ipynb` if you keep the notebook.
3. In [pyproject.toml](pyproject.toml), change `testpaths = ["mypackage/tests"]` to `testpaths = ["soil_analysis/tests"]`. This tells pytest where to look for your tests when it is run without a path.
4. If you use the optional [makefile](makefile), change `MODULENAME ?= mypackage` to `MODULENAME ?= soil_analysis`. `MODULENAME` is just a variable: it tells commands such as `make test`, `make lint`, and `make docs` which code folder they should use.
5. If you keep GitHub Pages documentation, change `mypackage` in [.github/workflows/pages.yml](.github/workflows/pages.yml) to `soil_analysis`. This tells pdoc which package to turn into documentation.
6. Search the repository for `mypackage` and replace any remaining student-facing examples, such as README text or notebook starter-file checks.

Why update all of these? If the folder and imports disagree, Python cannot find your code. If a configuration file still uses the old name, a tool may test, format, or document the wrong location.

To check the rename, run `make test` if your project uses Make. Otherwise, from the repository root, start Python and try `import soil_analysis`. A successful import confirms that Python can find the renamed package.

## Pass-By-Default Automation Notes

This template is set up so a fresh GitHub repository from template should pass CI without first-day debugging. Updating the matching references above keeps that true after customization.
