---
name: code-review
description: Review a change on two independent axes: contract compliance and engineering quality. Verify that the change implements the accepted behavior without scope drift, then inspect correctness, simplicity, architecture, tests, security, performance, compatibility, and operational side effects using evidence rather than taste.
---

# Code Review

## Canonical contract review

For Arena product PRs, contract-review states and authority are owned by ../../execution/arena-dispatch.md.

The only Arena contract-review outcomes are:

- CONTRACT-COMPLIANT
- CORRECTION REQUIRED
- CONTRACT EXCEPTION

Human acceptance remains separate.

This skill supplies the review method used to reach an evidence-backed result and to identify engineering findings.

## Purpose

A change can fail in two fundamentally different ways:

1. it implements the wrong thing;
2. it implements the right thing poorly.

Review both independently.

Do not let clean code hide a missed requirement.

Do not let requirement compliance hide a correctness, security, or maintainability defect.

## Preconditions

Understand the active Issue or requirement contract, architecture constraints, diff or candidate being reviewed, verification evidence, and project conventions relevant to the changed area.

Do not invent requirements that are absent from the accepted contract.

## Review axis 1 — Contract

Ask:

- does every acceptance criterion have corresponding implementation and evidence;
- is required behavior present;
- is prohibited or out-of-scope behavior absent;
- are constraints preserved;
- are non-goals respected;
- did implementation silently change user-visible behavior;
- did a material contract exception emerge;
- does verification actually prove the relevant criteria.

Classify gaps correctly.

### Implementation miss

The contract is still valid, but the candidate fails it.

Result: CORRECTION REQUIRED.

### Contract flaw or new material decision

The evidence shows the active contract itself must change.

Result: CONTRACT EXCEPTION.

### Satisfied contract

The candidate meets the active contract with sufficient evidence.

Result: CONTRACT-COMPLIANT.

## Review axis 2 — Engineering

Review engineering quality independently from the contract verdict.

### Correctness

Look for wrong logic, edge cases, invalid assumptions, races or concurrency problems, partial failure handling, error propagation, state consistency, resource lifecycle bugs, and serialization, timezone, or encoding problems where relevant.

Trace actual execution rather than only scanning syntax.

### Tests

Read tests early because they reveal intended behavior.

Ask whether tests cover changed behavior, prove behavior rather than implementation details, cover important failure paths, would fail if behavior regressed, and avoid mocks that hide the real boundary.

Coverage percentage is not a substitute for these questions.

### Simplicity and readability

Ask whether there is a simpler implementation, abstractions earn their complexity, unrelated concerns are entangled, control flow is understandable, types and invariants are explicit, and the change added unnecessary pass-through layers or conditionals.

Prefer structural remedies that remove concepts over moving complexity around.

### Architecture

Check accepted ownership, dependency direction, module and interface boundaries, state and data mutation rules, public contracts, canonical helpers, and feature-specific logic leaking into shared infrastructure.

Do not introduce a new architecture preference unless the change exposes a material problem.

### Security

When the diff touches a security trigger, invoke or apply ../security-engineering/SKILL.md.

Do not file speculative vulnerabilities without tracing attacker control and exploitability.

### Performance

Review performance when the changed path makes it relevant.

Look for unbounded work, multiplicative I/O, large hot-path allocations, blocking I/O, missing bounds or pagination, repeated computation, and pathological retry loops.

Do not demand optimization without evidence or a credible scale risk.

### Compatibility and side effects

Check whether the change alters public API behavior, schema or data format, events or messages, configuration, migration behavior, external integrations, supported platform or runtime, or observable errors, order, or timing consumers may rely on.

Compatibility is part of correctness when consumers exist.

### Operations

For production behavior, inspect as relevant logging, metrics, traces, failure diagnostics, retry behavior, feature-flag lifecycle, deployment assumptions, migration safety, and rollback or recovery implications.

Do not require operational machinery the project does not need.

## Evidence standard

A finding should include location or surface, concrete behavior, why it matters, supporting evidence, and required correction or recommended structural remedy.

Separate blocking correctness, contract, or security defects from material engineering improvements and optional nits.

Do not use style preference as a blocker when the project has no relevant standard.

## Review boundaries

Do not:

- reimplement the PR while reviewing it;
- add new product requirements;
- expand scope because neighboring cleanup is attractive;
- demand a different style solely because you prefer it;
- repeat automated lint output as manual insight unless it affects interpretation;
- mark a candidate accepted or merge it.

## Output contract

### Contract Review

For Arena work, exactly one of CONTRACT-COMPLIANT, CORRECTION REQUIRED, or CONTRACT EXCEPTION, with evidence tied to the active contract.

### Engineering Findings

For each material finding: category, location, evidence, impact, and required or recommended correction.

### Verification Gaps

Behavior changed but not adequately proven.

### Review Notes

Areas the human should inspect closely.

### Acceptance Boundary

Explicitly state that review or contract compliance is not human acceptance or merge authorization.

## Red flags

- code quality review without reading the contract;
- spec review without reading implementation and tests;
- this feels wrong findings with no concrete failure;
- nitpicks overwhelming material defects;
- speculative security findings;
- reviewer inventing features;
- forcing large refactors into a bounded correction;
- tests assumed good because they exist;
- VERIFIED treated as CONTRACT-COMPLIANT;
- CONTRACT-COMPLIANT treated as ACCEPTED.

## Completion check

Before finishing review, confirm:

- contract and engineering axes were considered separately;
- every contract finding cites the active contract;
- material engineering findings explain concrete impact;
- security and performance concerns are evidence-based;
- compatibility and operational side effects were considered where relevant;
- verification gaps are explicit;
- the result does not imply human acceptance.

## Provenance

Upstream mechanisms studied:

- mattpocock/skills — skills/engineering/code-review/SKILL.md — code-review — MIT
- getsentry/skills — skills/code-review/SKILL.md — code-review — Apache-2.0
- addyosmani/agent-skills — skills/code-review-and-quality/SKILL.md — code-review-and-quality — MIT

This is an Anthracite-specific rewrite. Upstream tool restrictions, organization-specific review rules, fixed change-size thresholds, and repository-specific style preferences are intentionally not inherited.
