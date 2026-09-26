---
name: architecture-interface-design
description: Define the durable architecture decisions and interface contracts that keep independently built parts of a system consistent. Establish ownership, dependency direction, state and data rules, meaningful seams, failure and compatibility behavior, and defer implementation detail that need not be fixed centrally.
---

# Architecture and Interface Design

## Purpose

Use this skill after requirements are sufficiently stable to define the structural decisions downstream implementation must share.

Architecture is a consistency contract, not a complete description of the codebase.

Record a decision centrally when independently built parts could otherwise make materially incompatible choices and the choice is not obvious from accepted project reality.

Interface design defines how meaningful parts communicate safely across those seams.

## Use when

Use this skill when:

- creating a greenfield architecture;
- introducing or changing material system boundaries;
- several independently implemented parts must remain consistent;
- defining a public or internal interface with compatibility consequences;
- changing ownership of data or state;
- choosing dependency direction;
- designing external integrations;
- restructuring a brownfield system where existing conventions must first be recovered.

Do not invoke it for every local code organization choice.

## Inputs and authority

Read:

- approved requirements;
- accepted project decisions;
- relevant feasibility evidence;
- existing architecture documentation;
- actual code/configuration for brownfield work;
- inherited interface contracts.

For brownfield work, inspect reality before proposing architecture. Ratify valid existing conventions rather than redrawing the system from imagination.

Inherited accepted architecture is a constraint unless the current work explicitly has authority to revise it.

## Architecture inclusion test

Before centralizing a design decision, ask:

> If two units one level down implemented this independently, could they choose incompatibly in a way that harms the system?

Record it as a durable architecture rule only when:

- the answer is yes;
- the difference would materially matter;
- the correct choice is not already obvious from canonical project artifacts;
- the decision is a real trade-off or invariant rather than transient implementation detail.

Otherwise defer it to implementation.

## Workflow

### 1. Establish architecture scope

State what level of the system this architecture controls:

- whole project;
- subsystem;
- feature slice;
- integration;
- library/public interface;
- migration boundary.

Do not solve unrelated architecture.

### 2. Recover existing reality

For brownfield work, identify:

- current modules/services/packages or equivalent project structures;
- dependency direction;
- current state and data ownership;
- external contracts;
- deployment/environment constraints relevant to the change;
- conventions already enforced by code or tooling.

Separate:

- **accepted invariant** — durable and intentionally binding;
- **current seed/state** — true today but owned by code/configuration and not necessarily architectural policy;
- **accidental structure** — may be changed;
- **unknown** — needs evidence or a decision.

Do not duplicate the current tree as architecture merely because it exists.

### 3. Identify responsibilities and ownership

Define which part owns each material responsibility.

For shared state or data, make ownership explicit.

Clarify:

- who may read;
- who may mutate;
- where authoritative state lives;
- where derived state may exist;
- how consistency is maintained when relevant.

Ambiguous ownership is a common source of hidden coupling.

### 4. Define dependency direction

State which parts may depend on which.

Prefer rules that prevent structural drift rather than exhaustive dependency maps.

Examples:

- domain logic may not depend on transport;
- product modules consume a shared contract rather than each other's internals;
- adapters depend inward on interfaces;
- an integration layer may depend on vendor SDKs while the domain does not.

Use terminology appropriate to the actual project. Do not force a foreign architecture vocabulary.

### 5. Define meaningful seams

A seam is a place where behavior can vary or be isolated behind a contract.

Create a seam when it provides real leverage, locality, testability, or replaceability.

Avoid speculative abstraction.

Useful checks:

- does the interface hide meaningful complexity;
- do callers need to know less because the module exists;
- would deleting the abstraction spread complexity back across callers;
- does more than one implementation or test substitute genuinely benefit from the seam;
- can callers and tests use the same public contract.

Prefer deep modules: substantial behavior behind a small, understandable interface.

### 6. Design the contract

For each material interface, define what consumers must know.

Depending on the interface type, include:

- inputs;
- outputs;
- invariants;
- ordering requirements;
- error semantics;
- failure behavior;
- retry behavior;
- idempotency where repeated side effects matter;
- configuration requirements;
- performance characteristics when contractually relevant;
- authentication/authorization expectations;
- trust validation;
- compatibility and versioning expectations;
- deprecation/migration expectations for public or widely consumed interfaces.

The contract applies broadly to interfaces such as:

- module/library interfaces;
- HTTP or RPC APIs;
- events and messages;
- queues;
- CLI contracts;
- files and schemas;
- external integrations.

Do not assume REST.

### 7. Validate at real trust boundaries

Treat external input and third-party responses as untrusted where applicable.

Validate at system or trust boundaries rather than scattering duplicate validation throughout trusted internal paths.

Coordinate with security engineering when authentication, authorization, sensitive data, untrusted parsing, network boundaries, or other security triggers exist.

### 8. Design compatibility intentionally

Observable behavior can become a dependency even when undocumented.

Minimize unnecessary observable commitments.

Prefer additive evolution where appropriate.

Before changing an existing public or shared interface, identify consumers and migration implications.

Do not invent versioning machinery for interfaces with no compatibility requirement.

### 9. Define failure behavior

Failure semantics are part of the contract.

Clarify what consumers should expect for material failures:

- explicit errors;
- partial results;
- retries;
- duplicate requests;
- timeouts;
- unknown outcome after an external side effect;
- degraded mode;
- unavailable dependency.

For side-effecting operations, consider whether retries require idempotency and how duplicate/in-flight requests are handled.

### 10. Defer implementation detail

Explicitly leave open choices that do not need project-level consistency.

Examples:

- private helper structure;
- local algorithm choice;
- internal naming;
- private class decomposition;
- replaceable implementation details that do not affect consumers.

Architecture should preserve implementation judgment.

### 11. Preserve rationale selectively

The architecture contract should stay concise.

Persist rationale when losing it would likely cause unsafe reversal or repeated re-litigation.

Use the project's actual ADR or decision mechanism when one exists.

Do not create a control-plane shadow decision log.

## Output contract

### Architecture Scope

What this contract governs.

### Durable Invariants

The structural rules independent implementations must share.

### Responsibilities / Ownership

Material responsibility, state, and data ownership.

### Dependency Direction

Allowed and prohibited dependency relationships.

### Interfaces / Contracts

For each material seam:

- purpose;
- inputs;
- outputs;
- invariants;
- errors/failures;
- trust validation;
- compatibility;
- retry/idempotency behavior when relevant.

### Operational Constraints

Only constraints that materially shape architecture, such as environment, availability, deployment, or provider limits.

### Deferred Decisions

Implementation choices intentionally left open.

### Open Questions

Unresolved structural decisions, with blockers distinguished from safe deferrals.

### Rationale Requiring Durable Preservation

Only decisions whose rationale is costly to lose; persist them in the project's owning decision artifact.

## Persistence

Do not mandate an `ARCHITECTURE-SPINE.md`, memlog, diagram set, stable decision IDs, or separate architecture workspace.

Persist durable rules in the project's actual architecture or decision artifacts.

Where code/configuration already owns the fact, point to that truth instead of duplicating it.

Diagrams are optional. Use them when they communicate structure more clearly than prose.

## Handoff

Architecture informs:

- security engineering;
- greenfield project bootstrap;
- implementation planning;
- testing seams;
- observability design;
- later migration and deprecation decisions.

Do not turn this skill into implementation planning.

## Red flags

- documenting every directory as architecture;
- inventing greenfield conventions in a brownfield system without inspection;
- centralizing choices that implementation can safely make locally;
- speculative abstractions with no real variation or leverage;
- large interfaces exposing implementation complexity;
- unclear state/data ownership;
- interface contracts that omit failure behavior;
- treating third-party responses as trusted;
- changing observable behavior without compatibility analysis;
- mandatory diagrams or ADRs for ceremony;
- architecture prose that pre-implements the solution.

## Completion check

Before handoff, confirm:

- architecture scope is explicit;
- each durable invariant passes the architecture inclusion test;
- material responsibilities and ownership are clear;
- dependency direction is defined where independent work could diverge;
- state/data mutation ownership is explicit where material;
- meaningful interfaces define behavior and failure semantics;
- trust boundaries and external inputs are handled intentionally;
- compatibility and migration impact are considered for existing consumers;
- seams provide real leverage/locality/testability rather than speculative abstraction;
- implementation details that do not need central control remain deferred;
- durable rationale is preserved only where loss would matter.

## Provenance

Upstream mechanisms studied:

- bmad-code-org/BMAD-METHOD — `skills/bmad-architecture/SKILL.md` — `bmad-architecture`
- addyosmani/agent-skills — `skills/api-and-interface-design/SKILL.md` — `api-and-interface-design`
- mattpocock/skills — `skills/engineering/codebase-design/SKILL.md` — `codebase-design`

These repositories were MIT-licensed when this skill was authored.

This is an Anthracite-specific rewrite. Upstream architecture-workspace, memlog, decision-ID, diagram, starter, coaching-mode, vocabulary-policing, and protocol-specific assumptions are intentionally not inherited.
