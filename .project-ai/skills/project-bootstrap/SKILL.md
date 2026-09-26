---
name: project-bootstrap
description: Operationalize FinalTemplate's canonical project bootstrap and reconciliation procedure. Establish missing foundations deliberately, preserve valid existing choices, surface inconsistencies, and make quality and repository governance executable without creating shadow project state.
---

# Project Bootstrap

## Canonical owner

The canonical bootstrap and reconciliation procedure is:

`../../bootstrap/project.md`

Read and follow that file first.

This skill does not replace or duplicate that procedure. It supplies the operating method used while executing it.

If this skill and `../../bootstrap/project.md` ever conflict, the bootstrap procedure wins.

## Purpose

Turn a blank, partial, or adopted repository into a usable project foundation without normalizing it back into the template.

Bootstrap should leave real project artifacts owning real project facts.

It must not create a parallel project profile, permanent bootstrap report, or framework-specific shadow state.

## Use when

Use this skill when:

- turning FinalTemplate into a real new project;
- adopting an existing repository into this control plane;
- reconciling a partially bootstrapped project;
- repairing inconsistent foundation choices before normal engineering proceeds.

Do not use it for ordinary feature work after the project foundation is established.

## Operating principles

### Greenfield: decide deliberately

An empty repository cannot reveal choices that do not exist.

For greenfield work, establish project choices explicitly from accepted requirements, architecture, feasibility evidence, and human decisions.

Do not infer a stack because it is popular.

### Brownfield: discover before deciding

For an existing repository, inspect real artifacts before asking or changing anything.

Preserve valid established choices.

Bootstrap establishes missing foundations; it does not normalize a real project back into the template.

### Every fact has an owner

Examples:

- runtime and dependencies → manifests and lockfiles;
- build/test/lint commands → real project scripts/configuration;
- CI behavior → workflow/provider configuration;
- deployment → actual deployment configuration;
- repository enforcement → GitHub/provider settings;
- project purpose and usage → actual project documentation.

The control plane points to project truth. It does not become project truth.

## Workflow

### 1. Classify current foundations

For each relevant foundation, classify it using the canonical four states:

- **ESTABLISHED**
- **MISSING**
- **INCONSISTENT**
- **NEEDS DECISION**

Do not change an ESTABLISHED choice merely to match a preferred template convention.

### 2. Establish identity and scope

Ensure the actual project has enough identity to operate:

- name;
- purpose;
- intended users/consumers;
- scope and non-goals;
- relationship to other systems when material.

Replace template-facing README content with project-facing content when the project is established.

### 3. Reconcile technology choices

Use accepted architecture and project constraints to establish only what is needed:

- language/runtime;
- framework;
- dependency/package manager;
- lockfile strategy;
- build system;
- source/test layout;
- persistence/data approach;
- generated artifacts.

Do not choose technology merely because bootstrap needs something to write.

### 4. Create the smallest runnable baseline

Where applicable, establish a minimal state that can be:

- installed or restored reproducibly;
- built or compiled;
- started or exercised;
- tested;
- statically checked.

Prefer the smallest real baseline over a large scaffold full of unused choices.

### 5. Establish an executable quality bar

Translate accepted engineering constraints into project-owned checks where possible.

Examples as applicable:

- test command;
- formatter check;
- lint/static analysis;
- type checking;
- build/compile;
- generated-state verification;
- security-specific checks;
- accessibility or performance checks when part of the project contract.

Do not encode a quality rule twice when one executable project check can own it.

### 6. Establish ignore and environment handling from actual artifacts

Create ignore rules only for artifacts the chosen stack actually produces.

Define environment/configuration handling according to project need.

Do not commit secrets.

Do not introduce a generic multi-language ignore file for a project that uses one stack.

### 7. Establish CI only after local project truth exists

CI should call the project's real commands.

Do not invent CI-only commands that developers cannot reproduce where practical.

Do not add generic workflows merely because they are common.

When provider-native organization policy already solves the problem, prefer it over copied repository files.

### 8. Establish repository governance conditionally

Determine whether the repository actually needs:

- issue forms;
- PR templates;
- labels;
- CODEOWNERS;
- branch protections/rulesets;
- required checks;
- merge policy;
- Actions permissions;
- security settings.

Repository governance is conditional, not a checklist.

Enforcement belongs in the provider that enforces it.

### 9. Establish release/deployment only when the project ships

If the project deploys or publishes, define the minimum required:

- artifact/version strategy;
- target environment or registry;
- secrets/environment handling;
- deployment path;
- rollback/recovery expectations.

Libraries, experiments, internal tools, and deployable services may need different foundations.

### 10. Verify the baseline

Use `../../execution/verification.md`.

A bootstrapped repository should have fresh evidence that its established project-owned commands and foundational workflows work.

Do not claim a clean baseline from configuration inspection alone.

### 11. Reconcile project state after acceptance

Only after accepted bootstrap work lands on `main`, update `../../PROJECT_STATE.md` when durable project reality changed.

Bootstrap activity itself is not state.

## Output contract

Bootstrap is complete when:

- required foundations are established or explicitly blocked on a decision;
- contradictory foundation choices are resolved or surfaced;
- the repository is a usable starting state for actual work;
- project facts live in their real owning artifacts;
- project-owned verification commands exist where applicable;
- repository/provider governance is established only where needed;
- no permanent bootstrap report or shadow project profile was created.

## Red flags

- copying a preferred stack into an empty repo without a decision;
- rewriting an established brownfield structure to resemble the template;
- storing package manager, build, or deployment facts in a second control-plane profile;
- generic CI before local commands exist;
- default CODEOWNERS, issue forms, labels, Dependabot, or release automation with no project need;
- quality requirements that exist only as prose despite an obvious executable check;
- creating `.gitignore` before the stack is known;
- treating provider settings as Markdown policy instead of enforcing them at the provider;
- writing PROJECT_STATE before the underlying work is accepted.

## Provenance

Upstream mechanisms studied:

- tomzx/agents — `skills/create-project/SKILL.md` — `create-project` — MIT
- github/awesome-copilot — `skills/repo-standardizer/SKILL.md` — `repo-standardizer` — MIT
- addyosmani/agent-skills — `skills/constraint-driven-development/SKILL.md` — `constraint-driven-development` — MIT

This is a substantial Anthracite rewrite. The canonical bootstrap procedure remains `../../bootstrap/project.md`; upstream `.sdlc`, GitHub-standardization defaults, and separate project-profile assumptions are intentionally not inherited.
