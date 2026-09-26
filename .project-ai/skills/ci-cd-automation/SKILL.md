---
name: ci-cd-automation
description: Build and maintain project-appropriate CI/CD and automation that enforces real project commands, gives fast trustworthy feedback, protects privileged execution, and scales deployment rigor to actual release risk.
---

# CI/CD and Automation

## Purpose

CI/CD should automate project truth, not invent it.

Use this skill to turn project-owned build, test, analysis, security, packaging, and deployment behavior into reliable automated gates and delivery pipelines.

The workflow must be reproducible, proportionate, and secure.

## Use when

Use this skill when:

- establishing CI for a project;
- adding or changing automated quality gates;
- introducing packaging or artifact publication;
- designing deployment promotion;
- optimizing slow or wasteful CI;
- securing privileged automation;
- changing workflow triggers, permissions, environments, credentials, or release automation.

## Inputs and authority

Before designing automation, discover the project's actual:

- package/dependency manager;
- build commands;
- test commands;
- formatter/linter/static checks;
- generated-state checks;
- security checks;
- packaging/publishing commands;
- deployment mechanism;
- environment and provider constraints.

The actual project owns those commands.

CI invokes them. It does not create a parallel definition.

## Workflow

### 1. Define the automation objective

Identify what the workflow must prove or accomplish.

Examples:

- verify a pull request;
- build a release artifact;
- publish a package;
- deploy to an environment;
- run a scheduled maintenance check;
- enforce generated-state consistency.

Do not combine unrelated mutation and verification merely for convenience.

### 2. Order feedback from fast to expensive

Prefer a progression such as:

1. cheap static/configuration checks;
2. focused or unit tests;
3. broader integration/system tests;
4. build/package verification;
5. security or policy checks where justified;
6. environment/deployment checks;
7. terminal repository acceptance when appropriate.

The exact stages depend on the project.

Fail early on high-signal cheap failures.

### 3. Keep verification reproducible

Where practical, CI should execute the same project-owned commands available outside CI.

Pin or constrain toolchain versions enough to avoid unexplained environment drift.

Use committed lockfiles and immutable/frozen installation where the ecosystem supports it.

Do not let CI silently rewrite dependency or generated state during a verification job.

### 4. Separate verification from mutation

Read-only verification should be the default.

Write permissions belong only in workflows that genuinely need them, such as:

- release publication;
- deployment;
- automated versioning;
- approved repository mutation.

A verification workflow should not gain write privileges because another job in the same file needs them.

### 5. Protect untrusted execution

Treat pull-request-controlled code and metadata as untrusted.

For privileged workflow contexts:

- minimize token permissions;
- avoid executing untrusted code with elevated credentials;
- protect secrets and environment approvals;
- validate inputs to scripts and deployment parameters;
- pin third-party actions or tooling according to project/organization policy;
- prefer short-lived identity/OIDC over long-lived static cloud credentials where supported and appropriate.

Security depth follows workflow privilege.

### 6. Optimize without weakening the gate

Use efficiency mechanisms where they materially help:

- dependency/build caches with correct cache keys;
- cancellation of superseded runs;
- concurrency groups;
- path filtering when omitted paths truly cannot affect the check;
- matrix discipline;
- reuse of built artifacts rather than rebuilding identically;
- avoiding duplicate checks across workflows;
- selective expensive tests where project evidence supports it.

A faster workflow that silently stops testing affected behavior is not an optimization.

### 7. Control matrix growth

Every matrix dimension multiplies execution cost.

Add dimensions only when they represent supported compatibility or meaningful risk.

Do not test hypothetical environments the project does not support.

### 8. Design artifacts and promotion deliberately

For projects that ship deployable artifacts, prefer building an identifiable artifact once and promoting that candidate through environments where practical.

Avoid rebuilding different bits for staging and production when the delivery model should prove the same artifact.

Record provenance/version/commit enough to identify what was deployed.

### 9. Scale deployment rigor to risk

When deployment exists, decide whether the project needs:

- preview/staging;
- environment promotion;
- manual approval;
- canary;
- blue/green;
- feature flag;
- progressive rollout;
- zero-downtime techniques;
- automatic rollback.

None are universal requirements.

A small low-risk service and a high-risk payment migration should not inherit the same pipeline.

### 10. Define rollback or recovery

For changes where deployment failure can materially harm users or data, establish the recovery path before automation declares the rollout complete.

Rollback may mean:

- previous artifact;
- traffic shift;
- disabling a flag;
- configuration revert;
- forward-fix for irreversible data changes;
- restore from backup;
- provider-native rollback.

Do not claim all data migrations are safely reversible.

### 11. Measure the pipeline

Track enough to notice when automation becomes a tax:

- end-to-end duration;
- queue time;
- flaky failure rate;
- expensive jobs;
- cache effectiveness;
- duplicated work;
- failure-to-signal ratio.

Optimize recurring pain, not theoretical microseconds.

## Output contract

When designing or changing automation, define:

### Objective

What the workflow proves or performs.

### Triggers

Events or schedules that should run it.

### Permissions

Minimum required privileges.

### Stages / Gates

Ordered project-owned checks or actions.

### Artifacts

What is produced, consumed, or promoted.

### Environment / Promotion

Only if the project deploys.

### Failure and Recovery

What happens when a gate or deployment fails.

### Efficiency Controls

Caching, concurrency, filtering, matrices, reuse.

### Security Controls

Controls proportionate to privilege and untrusted input.

## Verification

Use `../../execution/verification.md`.

Workflow changes should be checked with the smallest useful local/static validation first, then provider execution where provider behavior itself is part of the change.

Do not use repeated remote CI runs as the primary debugging loop when the failure can be reproduced narrowly.

## Red flags

- CI invents different commands from local project truth;
- every job gets write permissions;
- privileged workflow executes untrusted PR code;
- generic matrix explosion;
- expensive full-suite work duplicated across jobs;
- cache keys that can return incompatible state;
- path filters that skip genuinely affected behavior;
- mandatory staging/canary/manual approval for every project;
- deployment success defined only as "workflow exited 0";
- rollback assumed possible for irreversible changes;
- automation that mutates candidate state during verification.

## Completion check

Before handoff, confirm:

- CI/CD is based on actual project commands;
- feedback is ordered for fast signal;
- verification and mutation privileges are separated;
- untrusted execution cannot casually reach privileged credentials;
- efficiency controls do not weaken coverage;
- deployment rigor matches risk;
- artifacts and deployed versions are identifiable where relevant;
- recovery is defined for material rollout failure.

## Provenance

Upstream mechanisms studied:

- addyosmani/agent-skills — `skills/ci-cd-and-automation/SKILL.md` — `ci-cd-and-automation` — MIT
- wshobson/agents — `plugins/cicd-automation/skills/deployment-pipeline-design/SKILL.md` — `deployment-pipeline-design` — MIT
- github/awesome-copilot — `skills/github-actions-efficiency/SKILL.md` — `github-actions-efficiency` — MIT

This is an Anthracite-specific rewrite. Provider-specific workflow syntax, mandatory environment topology, and fixed rollout strategies are intentionally not inherited.
