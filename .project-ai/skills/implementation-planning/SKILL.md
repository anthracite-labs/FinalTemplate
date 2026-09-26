---
name: implementation-planning
description: Convert an approved requirement and architecture boundary into one or more executable implementation units. Prefer small vertical slices, explicit dependencies, acceptance evidence, and risk-first ordering while stopping before implementation detail is pre-written in prose.
---

# Implementation Planning

## Canonical execution contract

For Arena-dispatched product work, the canonical Issue contract and lifecycle live in:

`../../execution/arena-dispatch.md`

Read that file before producing an Arena plan.

This skill supplies decomposition and planning mechanics. It does not replace the Issue contract.

## Purpose

Plan only until approved work is safe and executable.

The planner should decide what the implementer cannot safely infer:

- objective;
- scope;
- constraints;
- acceptance boundary;
- dependencies;
- sequencing that genuinely matters;
- verification expectations;
- contract exceptions.

The planner should not write the implementation in prose.

## Use when

Use this skill when:

- accepted requirements need to become executable work;
- a project/feature is too large for one reviewable implementation unit;
- dependencies or blockers need ordering;
- work should be sliced into small vertical increments;
- risk or uncertainty should be moved earlier;
- an Arena Issue contract needs to be prepared.

Do not use it to re-decide requirements or architecture already accepted.

## Workflow

### 1. Load the accepted contract

Read the authoritative:

- objective and requirements;
- architecture constraints;
- security constraints;
- non-goals;
- relevant project artifacts;
- verification strategy;
- current project state only to the extent needed.

Do not plan from chat summaries when canonical repository artifacts exist.

### 2. Decide whether the work fits one implementation unit

A sensible implementation unit should:

- have one coherent objective;
- fit one reviewable branch/PR;
- have observable acceptance criteria;
- leave the repository in a valid state;
- not require the implementer to invent project-level decomposition.

If not, decompose before dispatch.

### 3. Prefer vertical slices

A vertical slice delivers a narrow, complete behavior through the layers it genuinely needs.

Prefer:

`small end-to-end capability → verify → next capability`

over:

`all database → all backend → all frontend → integrate at end`

unless the work is inherently a wide mechanical migration.

Each slice should be independently demonstrable or verifiable where practical.

### 4. Model real dependencies

For each proposed unit, identify blockers.

A dependency exists only when the later unit cannot safely begin or complete without the earlier one.

Do not make everything sequential merely because the plan is written in order.

Identify a frontier of work that can proceed independently.

### 5. Handle wide migrations explicitly

Some changes cannot be green as ordinary vertical slices because one contract is used everywhere.

For these, use an expand-migrate-contract shape where appropriate:

1. introduce compatible new form;
2. migrate consumers in bounded batches;
3. verify zero remaining consumers;
4. remove old form.

Do not force a cross-repository rename or shared-schema migration into fake vertical slices.

### 6. Put risk early

Move uncertainty forward when failure would invalidate later work.

Examples:

- prove an external integration;
- validate a migration strategy;
- benchmark a critical performance assumption;
- prove a security or platform constraint;
- establish a required compatibility seam.

Risk-first does not mean building speculative infrastructure. It means testing the assumption that could sink the plan.

### 7. Define each unit by outcome, not file list

For each implementation unit, define:

- objective;
- what it delivers;
- scope;
- out of scope;
- constraints;
- acceptance criteria;
- verification;
- dependencies;
- contract exceptions.

File paths may be included when they are authoritative and useful, but they are not the planning unit.

Avoid brittle plans that prescribe every function body before implementation begins.

### 8. Make handoff self-contained

The implementer should not need prior chat history to understand the unit.

Point to canonical repository references rather than copying entire documents.

Include enough context to understand why constraints exist.

Do not paste the whole project state into every Issue.

### 9. Stop at executable

Planning is complete when the next unit can be implemented safely without project-level invention.

Do not continue until the plan resembles code.

A useful test:

> Could a capable implementer make local implementation choices while remaining inside the contract?

If yes, stop planning.

### 10. Produce the Arena Issue contract when applicable

For Arena work, use exactly the canonical sections from `../../execution/arena-dispatch.md`:

- Objective
- Context & Authority
- Scope
- Out of Scope
- Constraints
- Acceptance Criteria
- Verification
- Contract Exceptions

One Issue maps to one Arena branch and one PR.

If multiple Issues are needed, each should still be independently coherent.

## Planning heuristics

Prefer units that:

- fit a focused implementation context;
- can be reviewed without reconstructing the entire project;
- have few acceptance criteria with high signal;
- keep unrelated refactoring out;
- preserve working state;
- expose blockers early.

Avoid arbitrary rules such as "five files maximum" when the project shape makes that meaningless.

## Output contract

### Decomposition

The ordered or partially ordered implementation units.

### Dependency Edges

Which units genuinely block which others.

### Risk-First Work

Any spike/proof that must happen before ordinary implementation.

### Per-Unit Contract

For Arena, the canonical Issue contract.

For non-Arena work, an equivalent bounded execution contract.

### Deferred Work

Valid follow-ups intentionally outside current scope.

## Red flags

- pseudo-code implementation masquerading as planning;
- giant plan files duplicating the spec;
- horizontal layer-by-layer slicing by default;
- no acceptance evidence per unit;
- dependencies inferred from list order rather than actual blocking;
- planning unrelated cleanup into a feature;
- one Issue containing several independently reviewable projects;
- implementer expected to recover intent from previous chat;
- planner resolving local implementation detail that the implementer can safely choose.

## Completion check

Before dispatch, confirm:

- each implementation unit has one coherent outcome;
- work fits one branch/PR per Arena Issue;
- dependencies are explicit and genuine;
- vertical slicing was preferred where appropriate;
- wide migrations use a safe compatible sequence where needed;
- high-risk unknowns appear early;
- acceptance criteria are observable;
- verification references project truth;
- contract exceptions identify material decisions that must return to the control plane;
- the plan stops before pre-implementing the solution.

## Provenance

Upstream mechanisms studied:

- addyosmani/agent-skills — `skills/planning-and-task-breakdown/SKILL.md` — `planning-and-task-breakdown` — MIT
- obra/superpowers — `skills/writing-plans/SKILL.md` — `writing-plans` — MIT
- mattpocock/skills — `skills/engineering/to-tickets/SKILL.md` — `to-tickets` — MIT

This is an Anthracite-specific rewrite. Mandatory local plan files, tracker configuration, worktree/subagent requirements, exact code-step transcripts, and foreign task-storage conventions are intentionally not inherited.
