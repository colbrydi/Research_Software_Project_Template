# Research Software AI Policy

## Purpose

This document is the canonical AI policy for this repository.

It applies to:

- Students
- Researchers
- Instructors
- Collaborators
- AI systems and coding agents

Use this policy with any AI tool, including GitHub Copilot, Claude, Gemini, Cursor, Codex, AITA, and future agent frameworks.

The goal is to improve learning, software quality, and research outcomes without turning AI into a gatekeeper.

## Scope

This policy applies to repository content and workflows that may include:

- Source code
- Documentation
- Configuration files
- Prompt files
- Notebooks
- Data descriptors and metadata

Assume AI-assisted workflows may expose repository context to external tools. Follow all project, legal, and institutional constraints before sharing context.

## Core Principles

All recommendations should support five principles:

1. Safe
2. Portable
3. Reproducible
4. Robust
5. Literate

### Safe

- Protect sensitive, regulated, confidential, proprietary, and restricted information.
- Do not store credentials, tokens, or secrets in the repository.
- Follow privacy, compliance, and governance requirements, including NDA, licensing, IRB, HIPAA, FERPA, sponsor agreements, and data use restrictions.
- Prefer conservative handling when uncertainty exists; escalate to project owners before disclosure.

### Portable

- Prefer relative paths and configuration over machine-specific assumptions.
- Avoid hard-coded usernames, local directories, and one-off environment hacks.
- Favor approaches that work across macOS, Linux, Windows, cloud, and HPC where feasible.

### Reproducible

- Document dependencies, parameters, and execution steps.
- Prefer scripted, repeatable workflows over manual steps.
- Capture assumptions, versions, and provenance needed for independent replication.

### Robust

- Prefer modular, testable designs with clear failure behavior.
- Minimize duplication and hidden coupling.
- Add or update tests for meaningful behavior changes.

### Literate

- Make intent clear in code, tests, and documentation.
- Explain what changed, why it changed, and how to validate it.
- Write for future contributors who did not author the original work.

## Roles For AI Systems

AI systems in this repository should behave as:

- Mentor: explain concepts and reasoning clearly.
- Reviewer: identify risks, defects, and maintainability issues.
- Debugger: isolate root causes and propose verifiable fixes.
- Technical writer: improve clarity, traceability, and documentation quality.
- Pair programmer: accelerate implementation while preserving understanding.

AI should help contributors learn and deliver, not block progress.

## Academic And Research Integrity

- Support academic integrity and course or project policies on AI usage.
- Encourage contributors to understand, explain, and modify generated work.
- Prefer transparent attribution when substantial AI assistance is used.
- Distinguish evidence from speculation in scientific discussion.

## Trust But Verify

Treat AI output as a draft hypothesis.

Before accepting generated code, analysis, or documentation:

1. Review for correctness and policy compliance.
2. Run relevant tests and checks.
3. Validate assumptions with data or references.
4. Confirm the contributor can explain the result.

## Responsible Data Stewardship

- Keep data governance explicit.
- Document how data is sourced, transformed, and constrained.
- Avoid committing restricted datasets unless policy explicitly permits it.
- Prefer metadata, schemas, and retrieval instructions over raw sensitive data.

## Working Style Expectations

- Explain reasoning for non-trivial recommendations.
- Balance educational value with practical productivity.
- Favor repository conventions and existing tooling over ad hoc alternatives.
- Choose maintainable solutions over short-lived cleverness.

## Repository Guidance Architecture

Use a layered structure to minimize duplication:

- Philosophy and policy: `RESEARCH_SOFTWARE_AI_POLICY.md` (this file, canonical)
- Operational agent behavior: `AGENTS.md`
- Tool-specific adapter(s): `.github/copilot-instructions.md` and future tool adapters

Tool-specific files should reference this document and add only tool mechanics.

## Tool Adapter Strategy (LLM-Independent)

Default stance: do not create per-tool policy files unless a tool requires a specific discovery filename or location.

When a tool-specific file is needed:

1. Keep it short.
2. Point to `RESEARCH_SOFTWARE_AI_POLICY.md`.
3. Add only tool mechanics and repository integration details.
4. Do not duplicate philosophy, compliance policy, or role definitions.

Practical examples:

- Keep `.github/copilot-instructions.md` because GitHub tooling expects it.
- Add files such as `CLAUDE.md` or `GEMINI.md` only if those tools require or strongly benefit from those filenames.
- If no requirement exists, use the canonical policy plus `AGENTS.md` and avoid extra files.

Current adapter locations in this repository:

- `.github/copilot-instructions.md`
- `.cursorrules`
- `CLAUDE.md`
- `CODEX.md`
- `GEMINI.md`

Not all tools reliably discover adapter files from subfolders. Keep active files in discovery-compatible locations.
