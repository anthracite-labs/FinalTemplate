---
name: requirements-specification
description: Convert confirmed intent and relevant evidence into an approved, implementation-neutral requirement contract. Define why the work exists, required capabilities, functional and non-functional requirements, constraints, non-goals, acceptance signals, assumptions, and blocking open questions without pre-implementing the solution.
---

# Requirements Specification

## Purpose

Use this skill to define what must become true before architecture, planning, or implementation begins.

Requirements own the behavior, outcomes, constraints, and acceptance boundary. They do not own implementation design, task decomposition, or code.

The specification should be only as detailed as necessary to make downstream decisions safe and testable.

## Use when

Use this skill when:

- a project or feature has confirmed intent but no approved requirements;
- vague goals need measurable success criteria;
- multiple stakeholders or concerns need a shared contract;
- a material change requires an explicit behavioral boundary before implementation;
- an existing requirement contract needs reconciliation or validation.

For trivial work, a few acceptance criteria may be sufficient. Do not create heavyweight specification ceremony for a tiny change.

## Inputs and authority

Use:

- confirmed discovery intent;
- relevant research and feasibility findings;
- accepted project decisions;
- existing project contracts and documentation;
- current code/configuration for brownfield constraints.

If the project already has a canonical specification or RFC system, use it. Do not create a parallel specification format merely because this skill exists.

## Core principles

1. Requirements describe **what** must be true, not unnecessary implementation detail.
2. Vague instructions must become observable success conditions.
3. Assumptions are surfaced before they become accidental requirements.
4. Constraints must actually constrain downstream choices.
5. Non-goals are explicit so downstream agents do not fill the vacuum.
6. Every material capability needs a success or acceptance signal.
7. Cross-cutting concerns are included when the product carries them, not because a template lists them.
8. The contract must preserve all load-bearing discovery and research inputs.
9. Planning and implementation are downstream.

## Workflow

### 1. Surface assumptions

Before drafting requirements, list any material assumptions that would otherwise be silently embedded.

Resolve blocking assumptions with the user or mark them explicitly.

Do not silently choose:

- platform;
- technology;
- storage;
- deployment model;
- authentication pattern;
- performance target;
- compatibility boundary;
- user role;
- workflow behavior.

unless those are already authoritative project facts or accepted decisions.

### 2. Establish why and who

State:

- the problem or opportunity;
- the user or stakeholder;
- the desired outcome;
- why the work matters.

Keep this concise. Discovery owns the deeper reasoning; requirements preserve only what downstream work needs.

### 3. Define capabilities and functional requirements

Describe what the system must allow, prevent, produce, or maintain.

Prefer user-visible or contract-visible behavior over implementation structure.

For larger scopes, group requirements by capability.

Stable identifiers are useful when downstream traceability will materially benefit from them. They are not mandatory for tiny work.

### 4. Define non-functional and cross-cutting requirements

Include only concerns the project actually carries, such as:

- performance;
- reliability or availability;
- security;
- privacy;
- accessibility;
- compliance;
- compatibility;
- scalability;
- observability;
- data retention;
- localization;
- operational constraints;
- public API or integration contracts.

Make them measurable where practical.

Do not add generic "must be scalable/secure/robust" language without an observable meaning.

### 5. Define constraints

Record decisions or external limits that materially restrict solution space.

Examples:

- existing platform or protocol that must remain compatible;
- regulatory requirement;
- approved dependency policy;
- migration limitation;
- supported environment;
- data residency;
- hard performance budget;
- repository or provider constraint.

A preference that rules out nothing is not a meaningful constraint.

### 6. Define non-goals

State what the work explicitly does not attempt to solve.

At least one non-goal is usually valuable for non-trivial work.

Do not invent arbitrary exclusions merely to satisfy a template.

### 7. Define acceptance and success signals

Translate each material requirement into evidence that can later be demonstrated, tested, inspected, or measured.

Examples of acceptable forms:

- observable user behavior;
- contract response;
- measurable threshold;
- successful integration behavior;
- preserved compatibility;
- explicit absence of prohibited behavior.

Avoid acceptance criteria that merely restate implementation steps.

### 8. Capture open questions

Classify open questions as:

- **blocking** — architecture or implementation would be unsafe or materially ambiguous without an answer;
- **deferred** — can safely remain unresolved until a later lifecycle point.

Resolve blockers before approval.

### 9. Preservation check

Walk the confirmed discovery and relevant research findings.

Ensure every load-bearing requirement, constraint, risk condition, and non-goal appears in the contract or is explicitly rejected/deferred.

Do not silently lose qualitative constraints because they do not fit a template section.

### 10. Approval

The requirement contract must be understandable enough for the human to approve or correct without reading an implementation plan.

Approval means the behavior boundary is accepted. It does not approve architecture or implementation choices that have not yet been made.

## Output contract

Use the following lean kernel.

### Objective / Why

What must change and why.

### User Outcome

Who benefits and what outcome they need.

### Capabilities / Functional Requirements

What behavior or capability must exist.

### Non-functional / Cross-cutting Requirements

Only applicable concerns.

### Constraints

Binding limits on downstream design.

### Non-goals

Explicit exclusions.

### Acceptance Criteria / Success Signals

Observable proof for the material requirements.

### Assumptions

Unverified beliefs still carried by the contract.

### Open Questions

Blocking and safely deferred questions.

## Optional detail

Add these only when they materially clarify the contract:

- user journeys;
- external interface requirements;
- compliance requirements;
- data requirements;
- migration requirements;
- performance budgets;
- availability targets;
- accessibility requirements;
- compatibility matrices.

Do not create sections merely because they are available.

## Boundaries

Where useful, express operational boundaries as:

- **Always** — actions or invariants downstream work must preserve;
- **Ask first** — material choices requiring explicit approval;
- **Never** — prohibited actions.

Do not use this pattern to duplicate control-plane policy already owned elsewhere.

## Artifact ownership

This skill does not mandate `SPEC.md`, a PRD, a spec folder, or a tasks directory.

Put the approved contract where the work is canonically owned.

Examples:

- GitHub Issue for an executable implementation unit;
- existing RFC/specification system;
- actual project documentation for durable project-level requirements;
- a concise in-context contract for trivial work when no durable artifact is required.

Avoid shadow requirement stores.

## Handoff

After approval:

- architecture and interface design resolves durable structural decisions;
- security engineering applies where risk triggers exist;
- project bootstrap establishes a greenfield repository after foundational choices are accepted;
- implementation planning later converts the accepted contract into executable slices.

Do not perform those jobs inside this skill.

## Red flags

- coding before any clear acceptance boundary exists;
- translating requirements into a detailed implementation plan;
- silently choosing architecture or technology;
- mandatory large specs for trivial work;
- vague success language;
- constraints that do not constrain;
- missing non-goals on broad work;
- treating assumptions as accepted facts;
- losing research conditions during specification;
- duplicating project facts already owned by code/configuration;
- creating task lists from this skill.

## Completion check

Before handoff, confirm:

- objective and user outcome are clear;
- material capabilities are specified without unnecessary implementation detail;
- applicable non-functional requirements are included and observable where possible;
- constraints materially restrict downstream choices;
- non-goals bound the scope;
- acceptance criteria prove the required behavior;
- assumptions are explicit;
- blocking questions are resolved;
- load-bearing discovery and research inputs were preserved;
- the human has approved the behavioral contract.

## Provenance

Upstream mechanisms studied:

- addyosmani/agent-skills — `skills/spec-driven-development/SKILL.md` — `spec-driven-development`
- bmad-code-org/BMAD-METHOD — `skills/bmad-prd/SKILL.md` — `bmad-prd`
- bmad-code-org/BMAD-METHOD — `skills/bmad-spec/SKILL.md` — `bmad-spec`

These repositories were MIT-licensed when this skill was authored.

This is an Anthracite-specific rewrite. Upstream spec-folder, PRD, memlog, capability-ID, task-file, ticketing, subagent, and workspace conventions are intentionally not inherited.
