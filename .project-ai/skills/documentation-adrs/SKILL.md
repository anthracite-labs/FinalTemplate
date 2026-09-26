---
name: documentation-adrs
description: Keep project documentation aligned with accepted reality and preserve durable decision rationale only when losing it would materially harm future engineering. Choose the right documentation type, follow existing project conventions, and avoid duplicating facts already owned by code or configuration.
---

# Documentation and ADRs

## Purpose

Documentation should reduce future uncertainty that code, configuration, tests, or version history cannot answer cheaply.

The most valuable documentation explains how to accomplish a task, what a public contract means, how a system concept works, or why a durable technical decision was made.

Do not document for ceremony.

## Use when

Use this skill when:

- user or developer behavior needs explanation;
- a public API or interface changes;
- setup or operational behavior changes;
- a feature requires onboarding or task guidance;
- a durable technical decision has rationale worth preserving;
- the same non-obvious explanation is repeatedly needed;
- accepted work makes existing documentation stale.

Do not invoke it solely to comment self-explanatory code.

## Core ownership rule

Document from accepted project reality.

Where a fact already has a canonical machine-readable owner, point to or derive from it rather than creating a second mutable source.

Examples:

- commands are owned by project scripts and configuration;
- API shapes are owned by actual schemas and contracts;
- dependency versions are owned by manifests and lockfiles;
- deployment behavior is owned by deployment configuration;
- repository enforcement is owned by provider settings.

Documentation explains and connects project truth. It should not silently become a competing truth.

## Workflow

### 1. Identify the reader's job

Establish who is reading, what they need to accomplish or understand, what prior knowledge they have, and what project artifacts are authoritative.

Do not write one generic document for every audience.

### 2. Choose the documentation type

Use the type that matches the reader's need.

#### Tutorial

Use when the reader needs guided learning from a starting point.

#### How-to

Use when the reader knows the basics and needs to accomplish a concrete task.

#### Reference

Use when the reader needs precise facts such as commands, public interfaces, configuration, options, schemas, or supported behavior.

#### Explanation

Use when the reader needs concepts, trade-offs, architecture, or rationale.

Do not mix all four shapes into one page unless the project has a compelling reason.

### 3. Inspect existing conventions

Before creating a new location or structure, inspect existing docs, README or CONTRIBUTING, docs sites, API documentation systems, ADRs, and project instructions.

Match established location, naming, format, numbering, headings, and tooling.

Do not start a second ADR or documentation convention.

### 4. Write only what earned permanence

Good durable content includes non-obvious user workflows, setup details that cannot be inferred safely, public interface behavior, operational procedures, compatibility constraints, design reasoning likely to be re-litigated, important gotchas, and migration guidance.

Avoid comments that restate code, prose descriptions of every directory, speculative future architecture, copied configuration tables that will drift, implementation diaries, and obvious TODO commentary.

### 5. Comment the why, not the what

Inline comments are appropriate when intent is non-obvious and local to the code.

Prefer explaining why a surprising constraint exists over paraphrasing what the next line does.

Delete commented-out code; version control owns history.

### 6. Keep public documentation aligned

When changing a public interface or user-visible behavior, inspect documentation that consumers rely on.

Update affected examples, API or reference material, setup instructions, migration notes, error behavior, and deprecation notices.

A code change that knowingly leaves public docs false is incomplete when documentation is part of the contract.

### 7. Decide whether an ADR is warranted

Write an ADR or equivalent durable decision record when:

- the decision is expensive to reverse;
- several plausible alternatives existed;
- future engineers are likely to question the choice;
- rationale cannot be recovered cheaply from code;
- forgetting constraints could cause a harmful reversal.

Do not write an ADR for every dependency, helper, naming choice, or ordinary implementation detail.

### 8. Preserve decision context

A useful durable decision record contains, in the project's existing format:

- context or problem;
- relevant constraints;
- decision;
- material alternatives considered;
- consequences and trade-offs;
- status;
- links to superseded or superseding decisions when relevant.

Implementation notes belong only when they help interpret the decision rather than becoming a task plan.

### 9. Evolve decisions rather than erasing history

When an accepted durable decision changes, follow the project's ADR or update convention, preserve enough history to understand why the current state differs, and mark supersession or deprecation where applicable.

Do not silently rewrite historical rationale as if the previous decision never existed.

### 10. Verify documentation against reality

Where practical, run code examples, verify commands, check links and paths, compare reference docs to actual interfaces and configuration, and validate migration instructions against the supported path.

Documentation correctness requires evidence too.

## Output contract

Produce only the artifacts actually needed.

For documentation, identify audience, documentation type, canonical sources, and right-sized content.

For an ADR or decision record, preserve context, decision, material alternatives, consequences, and status according to project convention.

## Artifact ownership

Use the actual project's documentation and ADR structure.

If none exists, create the smallest appropriate structure only when the need is real.

Do not create a .project-ai decision archive for product architecture.

Control-plane policy decisions remain in the control-plane files that own them.

## Red flags

- writing docs before accepted behavior exists;
- documentation that manually duplicates package or configuration facts;
- one giant README for tutorials, reference, explanation, and runbooks;
- mandatory ADRs for trivial choices;
- inventing a new ADR scheme alongside an existing one;
- comments that paraphrase the next line;
- stale code examples;
- historical ADRs deleted to make the current choice look inevitable;
- speculative docs describing features not accepted or implemented.

## Completion check

Before handoff, confirm:

- reader and purpose are explicit;
- documentation type matches the job;
- project conventions were reused;
- content derives from accepted reality;
- machine-owned facts are not needlessly duplicated;
- ADRs exist only where rationale is materially valuable;
- public behavior changes have corresponding docs when required;
- examples, commands, and reference facts are verified where practical.

## Provenance

Upstream mechanisms studied:

- addyosmani/agent-skills — skills/documentation-and-adrs/SKILL.md — documentation-and-adrs — MIT
- tomzx/agents — skills/create-documentation/SKILL.md — create-documentation — MIT
- github/awesome-copilot — skills/create-architectural-decision-record/SKILL.md — create-architectural-decision-record — MIT

This is an Anthracite-specific rewrite. Fixed documentation locations, mandatory ADR templates, coded bullet formats, and .sdlc documentation artifacts are intentionally not inherited.
