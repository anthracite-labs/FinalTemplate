---
name: maintenance-migration-retirement
description: Manage the long-term lifecycle of software: maintain, upgrade, replace, migrate, deprecate, remove, and retire. Measure real consumers, provide a working replacement before compulsory removal, stage compatibility changes, protect data migrations, and clean up obsolete code and supporting assets only after evidence shows they are no longer needed.
---

# Maintenance, Migration, and Retirement

## Purpose

Software has ongoing cost.

This skill helps decide when to maintain existing behavior, upgrade dependencies, replace an implementation, migrate consumers or data, deprecate a contract, remove obsolete assets, or retire a system safely.

End-of-life engineering is part of the lifecycle, not an afterthought.

## Use when

Use this skill for:

- legacy system decisions;
- major dependency or framework upgrades;
- API or contract deprecation;
- schema or data migrations;
- service replacement;
- feature retirement;
- dead code removal with real consumers;
- consolidation of duplicate implementations;
- infrastructure/provider migration;
- end-of-life cleanup.

## Core principles

### Measure before removing

"Probably unused" is not evidence.

Use as applicable:

- runtime usage;
- dependency graph;
- code search;
- API telemetry;
- configuration references;
- customer/consumer inventory;
- deployment inventory;
- data ownership records.

### Replacement before compulsory removal

If consumers still need the capability, provide a viable replacement before forcing migration unless emergency security or safety conditions make that impossible.

### Additive before destructive

Where compatibility matters, prefer introducing the new path before deleting the old one.

### Migration is not complete at cutover

Compatibility layers, flags, old schemas, credentials, dashboards, docs, CI jobs, infrastructure, and data may all need cleanup.

## Workflow

### 1. Decide the lifecycle action

Choose deliberately among:

- MAINTAIN;
- UPGRADE;
- REPLACE;
- MIGRATE;
- DEPRECATE;
- REMOVE;
- RETIRE.

Base the decision on:

- unique value;
- active consumers;
- maintenance cost;
- security risk;
- dependency health;
- operational burden;
- strategic direction;
- migration cost;
- replacement quality.

Do not assume newer is automatically better.

### 2. Inventory consumers and dependencies

Identify who or what depends on the current system:

- code call sites;
- services;
- users/customers;
- external API consumers;
- scheduled jobs;
- data pipelines;
- infrastructure;
- documentation;
- automation.

Unknown consumers increase removal risk.

### 3. Define the target state

State:

- replacement or upgraded version;
- compatibility expectations;
- data shape;
- consumer migration path;
- deadline only if one is justified;
- success evidence;
- rollback or forward-recovery strategy.

### 4. Choose advisory or compulsory deprecation

#### Advisory

Use when old behavior can remain safely for a period and consumers can migrate on their own schedule.

#### Compulsory

Use when continued operation creates unacceptable security, reliability, cost, compatibility, or delivery risk.

Compulsory deprecation should provide clear migration support and a justified timeline.

Do not force deadlines merely to make a roadmap neat.

### 5. Use expand-migrate-contract for compatibility-sensitive changes

When appropriate:

#### Expand

Introduce the new contract/schema/path alongside the old one.

Keep existing consumers working.

#### Migrate

Move consumers or data in bounded batches.

Verify each batch.

Measure remaining old-path usage.

#### Contract

Only after migration evidence shows the old form is no longer needed, remove compatibility code and old schema or interface.

This pattern applies beyond databases.

### 6. Handle dependency upgrades deliberately

For major upgrades:

- inspect release notes and migration guides;
- understand supported version combinations;
- identify breaking changes;
- map transitive/peer dependency constraints;
- stage upgrades when one large jump increases risk;
- verify at each stage;
- preserve lockfile consistency;
- avoid updating unrelated dependencies without reason.

Security upgrades may need faster action, but still require compatibility evidence.

### 7. Protect data migrations

Data changes deserve stronger safeguards than ordinary code because reverting application code does not necessarily revert data.

As applicable:

- make schema changes backward-compatible first;
- separate schema expansion, application migration, backfill, cutover, and contraction;
- make backfills restartable/idempotent where practical;
- bound batch size and load;
- measure progress;
- verify data invariants;
- account for mixed-version application deployments;
- take backups or snapshots when they materially improve recovery;
- define forward repair when reversal is unsafe or impossible.

Do not require a "down migration" when reversing would destroy newer valid data.

### 8. Migrate consumers incrementally

For each bounded consumer set:

1. identify touchpoints;
2. update to the target;
3. verify behavior;
4. observe production or integration health where relevant;
5. remove consumer-specific old references;
6. update migration inventory.

Avoid a big-bang migration unless the system genuinely requires one and risk is accepted.

### 9. Verify zero old-path usage

Before destructive removal, prove as appropriate:

- zero active calls;
- no remaining code references;
- no configured consumers;
- no queued/retry traffic that can return later;
- no external contractual consumers;
- required retention windows have passed.

Consider delayed retries, dead-letter queues, offline clients, and long-lived integrations.

### 10. Remove the old system comprehensively

Retirement may require removal of:

- source code;
- tests;
- compatibility adapters;
- feature flags;
- dependencies;
- configuration;
- secrets;
- CI jobs;
- deployment resources;
- dashboards and alerts;
- runbooks;
- documentation;
- data, subject to retention/legal requirements;
- external integrations;
- access grants.

Do not leave zombie infrastructure supporting code that no longer exists.

### 11. Verify the target state

Use ../../execution/verification.md.

Confirm:

- migrated consumers work;
- old path is no longer used;
- data invariants hold;
- removal did not break hidden dependencies;
- new system is observable and supportable;
- cleanup is complete enough to stop carrying old-system cost.

## Output contract

### Lifecycle Decision

Maintain, upgrade, replace, migrate, deprecate, remove, or retire.

### Current Consumers

Known dependencies and uncertainty.

### Target State

Replacement/version/schema/contract.

### Compatibility Strategy

How old and new coexist during transition.

### Migration Plan

Bounded stages and evidence.

### Data Safety

Backfill, recovery, invariants, retention.

### Deprecation Policy

Advisory or compulsory, with rationale.

### Removal Evidence

Proof old consumers are gone.

### Cleanup

Code, data, infrastructure, configuration, docs, and operational assets removed or deliberately retained.

### Residual Risk

Anything remaining after transition.

## Red flags

- removal based on code search alone when runtime consumers may exist;
- deprecation announced before a replacement exists;
- big-bang upgrade of many unrelated dependencies;
- destructive schema change before application compatibility exists;
- rollback plan that ignores data already written in the new format;
- universal insistence on reversible down migrations;
- feature flag left indefinitely after migration;
- old secrets or infrastructure left after retirement;
- public contract removed without consumer inventory;
- maintenance work used as a pretext for unrelated modernization.

## Completion check

Before declaring migration or retirement complete, confirm:

- lifecycle decision is explicit;
- consumers were measured;
- target state is working;
- compatibility strategy protected active consumers;
- data migration has evidence and recovery strategy;
- destructive removal happened only after old usage was cleared;
- obsolete supporting assets were cleaned up;
- project documentation and operations reflect the new state;
- final verification applies to the post-cleanup candidate.

## Provenance

Upstream mechanisms studied:

- addyosmani/agent-skills — skills/deprecation-and-migration/SKILL.md — deprecation-and-migration — MIT
- wshobson/agents — plugins/framework-migration/skills/dependency-upgrade/SKILL.md — dependency-upgrade — MIT
- wshobson/agents — plugins/framework-migration/skills/database-migration/SKILL.md — database-migration — MIT

This is an Anthracite-specific rewrite. Package-manager-specific commands, ORM-specific examples, fixed canary percentages, and universal reversible-down-migration assumptions are intentionally not inherited.
