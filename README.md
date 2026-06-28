# Scientific Software Starter Template

Starter repository for research teams and students who are new to software engineering.

## Overview of This Repository

- Purpose: Explain how to use the template with minimal overhead.
- Used by: Students, instructors, and collaborators onboarding to the project.
- Adds: A simple starting path plus optional tool adoption.
- Learn more: https://swcarpentry.github.io/

This template is designed to help make your first research code repository:

- Safe: simple checks catch common mistakes early.
- Portable: works across machines using a pinned conda environment.
- Reproducible: explicit dependencies and deterministic commands.
- Robust: tests first, then optional quality tools as you grow.
- Literate: optional API docs and notebooks for explainable workflows.
- Low overhead: use only the tools that fit your current needs.

## Quick Start

1. Create the environment:

	```bash
	make init
	```

2. Try the test command (optional):

	```bash
	make test
	```

3. Open the local import notebook example:

	- [local_import_demo.ipynb](local_import_demo.ipynb)

## What to Edit First

1. Rename `mypackage` to your project package name.
2. Replace [mypackage/example.py](mypackage/example.py) with your own module(s).
3. Update tests in [mypackage/tests/test_pytest.py](mypackage/tests/test_pytest.py).
4. Update this README with project goals, install instructions, and examples.

The test file already includes starter templates with short comments for:

- import/smoke tests
- fixtures
- parameterized tests
- exception tests
- regression tests

To get started writing your own tests, try this quick checklist:

1. Pick one function and write 3-5 known input/output examples.
2. Add one edge case (like zero, empty input, or boundary value).
3. Add one invalid input test with `pytest.raises(...)`.
4. Run `make test` and iterate.

More unit testing tutorials:

- Pytest getting started: https://docs.pytest.org/en/stable/getting-started.html
- Pytest examples: https://docs.pytest.org/en/stable/example/index.html
- Pytest good practices: https://docs.pytest.org/en/stable/explanation/goodpractices.html
- Python testing tutorial (Real Python): https://realpython.com/python-testing/

## Tool Overview

Use the tools you need, when you need them.

### Quick Definitions for Beginners

- Environment: A self-contained software workspace with a specific Python version and package list. It helps everyone run the same code with fewer "it works on my machine" problems.
- Unit test: A small automatic check for one behavior in your code.
- Linting: Automatic feedback about code quality and common mistakes.
- Type checking: Automatic checks that function inputs/outputs match expected types.
- CI (continuous integration): Cloud automation that runs checks after push/pull request.
- make test: Runs the automated tests for this project.

| Tool | What it helps with | How to run here | Files used in this repo | Learn more |
|---|---|---|---|---|
| Conda | Creates the software environment so everyone uses the same Python and packages. | `make init` | [environment.yml](environment.yml) | https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html |
| Pytest | Runs unit tests to check whether your code behavior is correct. | `make test` | [mypackage/tests/test_pytest.py](mypackage/tests/test_pytest.py), [pyproject.toml](pyproject.toml) | https://docs.pytest.org/en/stable/getting-started.html |
| Black | Rewrites code formatting automatically so style is consistent. | `make format` | [pyproject.toml](pyproject.toml) | https://black.readthedocs.io/en/stable/getting_started.html |
| Ruff | Finds common bugs/style issues quickly (linting). | `make lint` | [pyproject.toml](pyproject.toml) | https://docs.astral.sh/ruff/tutorial/ |
| MyPy | Checks type hints for mismatches before runtime errors occur. | `make type` | [pyproject.toml](pyproject.toml) | https://mypy.readthedocs.io/en/stable/getting_started.html |
| Pydocstyle | Checks whether docstrings follow a consistent style. | `make doclint` | [makefile](makefile) | https://www.pydocstyle.org/en/stable/ |
| pip-audit | Checks dependencies for known security vulnerabilities. | `make audit` | [makefile](makefile), [environment.yml](environment.yml) | https://pypi.org/project/pip-audit/ |
| detect-secrets | Scans code for accidentally committed secrets. | `make secrets` | [.pre-commit-config.yaml](.pre-commit-config.yaml), [.secrets.baseline](.secrets.baseline) | https://github.com/Yelp/detect-secrets |
| nbstripout | Removes notebook output and noisy metadata before commit. | `make nb-clean` | [.pre-commit-config.yaml](.pre-commit-config.yaml) | https://github.com/kynan/nbstripout |
| Pdoc | Builds simple API documentation pages from docstrings. | `make docs` | [makefile](makefile) | https://pdoc.dev/docs/pdoc.html |
| Pre-commit | Runs chosen checks before commit so issues are caught early. | `conda run --prefix ./envs pre-commit run --all-files` | [.pre-commit-config.yaml](.pre-commit-config.yaml) | https://pre-commit.com/ |
| GitHub Actions | Runs checks in the cloud after push/pull request (CI), including Python 3.11 and 3.12 matrix testing. | Automatic on GitHub | [.github/workflows/ci.yml](.github/workflows/ci.yml) | https://docs.github.com/actions/quickstart |
| Dependabot | Opens scheduled dependency update PRs for GitHub Actions and Python metadata. | Automatic on GitHub | [.github/dependabot.yml](.github/dependabot.yml) | https://docs.github.com/code-security/dependabot |
| JupyterLab | Lets you run notebook cells interactively for exploration and demos. | `conda run --prefix ./envs jupyter lab` | [local_import_demo.ipynb](local_import_demo.ipynb) | https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html |

## API Docs Quick Start (pdoc)

If you add clear docstrings, pdoc can turn them into browsable HTML docs quickly.

Try:

```bash
make init
make docs
```

Docstring features already demonstrated in [mypackage/example.py](mypackage/example.py):

- `Args`, `Returns`, and `Raises` sections
- `Examples` that readers can copy/paste
- `Notes` and `See Also` sections

Publishing tutorial:

- [GITHUB_PAGES_TUTORIAL.md](GITHUB_PAGES_TUTORIAL.md)
- Automated workflow: [.github/workflows/pages.yml](.github/workflows/pages.yml)
- pdoc docs: https://pdoc.dev/docs/pdoc.html
- GitHub Pages docs: https://docs.github.com/pages/getting-started-with-github-pages/creating-a-github-pages-site

To enable automatic publication, set GitHub Pages source to GitHub Actions in repository settings.

## Typical Workflow

```bash
make test         # optional

# other tools you can run when useful:
make format
make lint
make type
make audit
make secrets
make check-full
```

## Sharing Changes (Optional)

If students are using branches and pull requests, keep this simple:

1. Create/update environment:

	```bash
	make init
	```

2. Run checks before sharing (if your team uses them):

	```bash
	make test
	```

3. If advanced tools are enabled in your course, run:

	```bash
	make check-full
	```

## Is CI Helpful?

Yes, when kept minimal. This template runs tests in CI (`make test`) so students get value without heavy setup burden.

Progressive unlock option:

- The CI workflow in [.github/workflows/ci.yml](.github/workflows/ci.yml) includes commented lines for `make lint`, `make type`, and `make doclint`.
- Keep them commented for beginner classes.
- Uncomment one line at a time as students are ready.

## Beginner Guidance

- Start with `make init`, then try whichever `make` commands are helpful.
- Add optional tools only after your team sees recurring problems they can solve.
- Prefer consistency over complexity. A small workflow used every week is better than a large workflow used rarely.

## Notes for Reproducibility

- Keep `environment.yml` updated as tooling needs evolve.
- Add random seeds for stochastic experiments.
- Record key parameters and software versions in outputs.
- Avoid hidden local state and relative paths outside repo root.
- Prefer relative paths in code and notebooks (avoid machine-specific absolute paths).
- Avoid hard-coded algorithm settings when possible; use function arguments and sensible defaults.

## Repository Habits (Consistency Add-On)

These are selected practices aligned with the course-level repository rules:

- Keep repositories text-first when possible: code, Markdown, and config files are preferred over frequently changing binary files.
- Use `.gitignore` intentionally and review what is staged before each commit.
- Avoid storing raw/input/intermediate/output datasets directly in the code repository; document how to fetch or mount data instead.
- Keep interfaces layered: library/API first, command-line tools second, and GUI work last.
- Favor modular design and avoid copy/paste duplication across code and docs.
- Keep README as the onboarding entry point: install, run, and validate in as few steps as possible.
- For notebooks, include a top Markdown title/description cell and clear outputs before commit when practical.
- If AI/LLM tools contribute meaningfully, note usage briefly in commit messages (for example: `LLM: drafted initial test cases, then simplified manually`).

Full reference:

- [Rules for Repos](https://colbrydi.github.io/Research_guidelines/Rules_for_Repos.html)

