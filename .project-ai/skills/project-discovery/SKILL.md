---
name: project-discovery
description: Clarify a project or materially underspecified request before research, requirements, planning, or implementation. Establish the real problem, affected users, desired outcome, success, constraints, non-goals, evidence of need, alternatives, assumptions, and whether the work should proceed.
---

# Project Discovery

## Purpose

Use this skill to turn a raw idea, requested solution, or ambiguous project ask into a confirmed statement of intent that downstream work can safely rely on.

Discovery owns understanding the need. It does not own research, requirements, architecture, planning, or implementation.

## Use when

Use this skill when one or more of these are unclear:

- who experiences the problem;
- what outcome is actually wanted;
- why the work matters now;
- what success means;
- which constraint is binding;
- what is explicitly out of scope;
- whether the proposed solution addresses a demonstrated need.

Also use it when the request jumps directly to a conventional solution such as "build a dashboard", "add AI", "make it scalable", or "create an app" without enough context to know why that solution is appropriate.

## Do not use when

Do not invoke this skill for:

- mechanical edits with an already clear outcome;
- pure factual or explanatory questions;
- an already approved and executable work contract;
- bounded implementation corrections whose requirements have not changed.

## Inputs and authority

Read existing authoritative project material before asking the user to repeat it.

For an existing project, prefer the artifacts that own the relevant facts: code, configuration, project documentation, accepted decisions, current issue or PR, and other canonical project sources.

For a greenfield project, unresolved choices are not facts. Ask or explicitly mark them as assumptions.

Do not treat chat convention, generic best practice, or model familiarity as project truth.

## Workflow

### 1. Form the current interpretation

State the current best understanding of the request in plain language.

Identify the load-bearing information still missing. Do not silently fill important gaps.

A useful working set is:

- problem;
- user or stakeholder;
- desired outcome;
- why now;
- success;
- binding constraints;
- non-goals.

A numeric confidence score is optional. The requirement is to make uncertainty visible, not to perform confidence theatre.

### 2. Clarify interactively

When interaction is available, ask one focused question at a time when the answer materially affects the next question.

Where useful, attach a concise best guess so the user can react to a concrete interpretation instead of generating every answer from scratch.

Do not lead the user toward fashionable or conventional answers. If the response is mostly signaling language such as "modern", "clean", "scalable", or "best practice", ask what observable outcome they actually care about.

Stop probing when the remaining uncertainty is not load-bearing for the next lifecycle step.

### 3. Establish the underlying need

Do not accept a requested feature as the problem statement.

Work backward from the proposed solution and establish:

- what problem exists;
- who experiences it;
- how severe or frequent it is;
- what evidence demonstrates it;
- what people do today;
- what happens if nothing changes.

Evidence can include project data, user requests, support patterns, observed workflow cost, business constraints, operational pain, or other relevant first-hand signals.

If evidence is weak, say so.

### 4. Challenge whether new software is required

Consider whether the need could be met through:

- existing project capability;
- configuration;
- better documentation;
- a process change;
- an existing internal or external solution;
- a smaller change than the proposed solution;
- doing nothing for now.

Discovery must permit the answer "do not build this".

### 5. Surface assumptions and unknowns

List assumptions the next stage would otherwise mistake for fact.

Separate:

- accepted facts;
- assumptions;
- open questions;
- external facts that need research;
- project facts that should be recovered from canonical artifacts.

### 6. Confirm intent

Before handoff, restate the discovered intent using the structure below.

The user should be able to correct any line independently.

Do not treat vague acquiescence as stronger than it is. If the restatement exposes a material ambiguity, resolve it before moving on.

## Output contract

Produce a compact discovery payload with these fields:

### Problem

What undesirable condition or unmet need exists.

### User / Stakeholders

Who experiences the problem, who benefits, and any materially affected parties.

### Desired Outcome

What should become true without prescribing implementation unnecessarily.

### Why Now

What makes the work relevant now.

### Success

Observable evidence that the outcome has been achieved.

### Constraints

Binding limits already known.

### Non-goals

What this effort is explicitly not trying to solve.

### Evidence of Need

What supports the claim that the problem is real.

### Existing Alternatives / Workarounds

How the need is addressed today and viable non-build alternatives.

### Assumptions

Unverified beliefs that materially affect direction.

### Open Questions

Unresolved questions that are safe to defer or must be answered next.

### Decision

Use one of:

- **PROCEED** — intent and need are clear enough for research and feasibility;
- **VALIDATE FURTHER** — the idea may be worthwhile, but evidence or intent is still too weak;
- **DO NOT BUILD** — current evidence does not justify new implementation.

## Persistence

This skill does not create a mandatory discovery document.

Persist its result only when the project needs durable continuity. Use the artifact that owns the work rather than creating a shadow source of truth.

Examples:

- a project-level accepted decision or project document for durable project intent;
- a GitHub Issue when the discovery result becomes executable work;
- an existing product/specification system when the project already uses one.

## Handoff

When the decision is **PROCEED**, hand off to research and feasibility when external facts, alternatives, or viability still need evidence.

If no material research is needed and the project already has enough evidence, requirements specification may follow directly.

Do not plan or implement from this skill.

## Red flags

- treating the requested feature as proof of the underlying need;
- asking questions already answered by authoritative project material;
- batching a long questionnaire when answers depend on earlier answers;
- accepting vague sophistication words as requirements;
- omitting non-goals;
- silently converting assumptions into facts;
- producing architecture, tasks, or code before intent is confirmed;
- forcing every project to produce the same discovery artifact.

## Completion check

Before handoff, confirm:

- the problem is stated independently of the proposed solution;
- affected users or stakeholders are known;
- the desired outcome and success signal are observable enough to guide later work;
- binding constraints and non-goals are explicit;
- evidence of need is identified or its absence is acknowledged;
- viable non-build alternatives were considered;
- assumptions and open questions are visible;
- the decision to proceed, validate further, or not build is explicit.

## Provenance

Upstream mechanisms studied:

- addyosmani/agent-skills — `skills/interview-me/SKILL.md` — `interview-me`
- bmad-code-org/BMAD-METHOD — `skills/bmad-product-brief/SKILL.md` — `bmad-product-brief`
- tomzx/agents — `skills/create-needs-assessment/SKILL.md` — `create-needs-assessment`

These repositories were MIT-licensed when this skill was authored.

This is an Anthracite-specific rewrite. Upstream framework-specific artifact, routing, orchestration, persistence, scoring, and workspace assumptions are intentionally not inherited.
