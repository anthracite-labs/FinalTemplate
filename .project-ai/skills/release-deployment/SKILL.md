---
name: release-deployment
description: Move an accepted integrated change into its target environment or user population safely. Verify preconditions, identify the exact candidate, scale rollout rigor to risk, use observable advance or hold or rollback criteria, and distinguish merge, deployment, health, and release completion.
---

# Release and Deployment

## Purpose

Shipping is more than starting a deployment job.

A release is complete only when the intended candidate is in the intended environment or user population, required smoke and health evidence is good, and recovery remains understood.

Keep these states distinct:

MERGED is not DEPLOYED, DEPLOYED is not HEALTHY, and HEALTHY is not necessarily RELEASED TO ALL USERS.

## Use when

Use this skill for:

- production deployment;
- package or artifact release;
- infrastructure rollout;
- configuration rollout;
- feature enablement after deployment;
- data or service migration rollout;
- staged or progressive user exposure.

Do not use it to merge an implementation PR. Merge authority is owned elsewhere.

## Preconditions

Before release, establish:

- the exact accepted commit, tag, version, or artifact;
- target environment or registry;
- project deployment or publication mechanism;
- required approvals;
- material dependencies;
- observability signals;
- rollback or recovery path proportionate to risk;
- data migration constraints if any.

If the project requires human release approval, preserve it.

## Workflow

### 1. Identify the release candidate

Record the exact artifact or commit being released.

Avoid ambiguous states such as "latest main" when an immutable version can be identified.

Where the delivery model supports it, promote the same built artifact through environments rather than rebuilding materially different candidates.

### 2. Establish target state

State what should become true:

- environment receives version X;
- package registry exposes version Y;
- feature becomes available to population Z;
- traffic moves from old system to new system;
- configuration transitions from A to B.

Release criteria should describe the target state, not only the command to run.

### 3. Run preflight checks

Use project-appropriate checks such as:

- current environment health;
- dependency availability;
- capacity;
- required secrets/configuration;
- migration prerequisites;
- backups where recovery depends on them;
- provider/change-window constraints;
- observability availability;
- known incident status.

Do not manufacture preflight ceremony that does not change the release decision.

### 4. Define advance, hold, and recovery criteria

Before the rollout, identify the signals that mean:

- **ADVANCE** — continue rollout;
- **HOLD** — stop expansion and investigate;
- **RECOVER** — roll back, disable, fail over, or forward-fix according to the project's recovery strategy.

Use project baselines and requirements rather than generic percentage thresholds.

### 5. Deploy or publish

Use the project's real release mechanism.

Do not invent provider commands.

Track enough provenance to know what action was performed against which candidate and environment.

### 6. Smoke-test the deployed state

Immediately verify critical basics appropriate to the release:

- service or artifact is reachable/available;
- core dependency connections work;
- key user or API path succeeds;
- expected version is running;
- no obvious new critical error signal appears.

Prefer existing project smoke tests.

### 7. Observe health

Use observability defined by the project.

Check relevant:

- error rate;
- latency;
- throughput;
- queue or job health;
- data integrity;
- critical business/user signals;
- new alert types;
- external integration health.

Deployment process success does not prove application health.

### 8. Progressively expose when risk warrants it

Possible techniques include:

- internal users;
- canary population;
- traffic shifting;
- blue/green;
- feature flags;
- staged environment promotion.

Use them only when they reduce real risk.

Do not impose fixed percentages, waiting windows, or feature flags on every project.

### 9. Recover when criteria fail

Use the safest supported recovery method:

- redeploy previous artifact;
- shift traffic back;
- disable a feature flag;
- revert configuration;
- restore from backup;
- execute a tested data recovery;
- forward-fix an irreversible data change.

Do not assume rollback is available for every data migration or external side effect.

After recovery, verify the prior safe state is actually restored.

### 10. Complete the release

Release is complete when:

- intended candidate is in intended target;
- required rollout stage is reached;
- smoke verification is green;
- health signals meet release criteria;
- no unresolved material release failure remains;
- follow-up cleanup is tracked where needed.

Feature flag cleanup, temporary compatibility layers, or migration cleanup may become maintenance work rather than blocking the immediate release.

## Output contract

### Candidate

Commit, version, tag, or artifact.

### Target

Environment, registry, or population.

### Preflight

Material checks and results.

### Rollout

What was changed and how exposure progressed.

### Verification

Smoke and health evidence.

### Recovery

Available path and whether it was used.

### Status

Use one of:

- RELEASED
- HELD
- RECOVERED
- FAILED

### Follow-up

Only real cleanup, monitoring, or migration work that remains.

## Red flags

- releasing an unidentified mutable candidate;
- deployment workflow green treated as user health proof;
- no smoke check on a material production change;
- feature flags used by habit rather than risk;
- arbitrary universal canary percentages;
- rollback assumed safe without data or side-effect analysis;
- rebuilding different artifacts for each environment when artifact promotion should prove one candidate;
- releasing during an active unrelated incident without considering combined risk;
- declaring success while key health signals are unknown.

## Completion check

Before stating RELEASED, confirm:

- exact candidate and target are known;
- project-required approvals were preserved;
- preflight risks were checked;
- release criteria were defined before observation;
- deployment or publication completed;
- smoke checks passed;
- relevant health signals are good;
- recovery path is understood;
- no unresolved material release failure remains.

## Provenance

Upstream mechanisms studied:

- addyosmani/agent-skills — skills/shipping-and-launch/SKILL.md — shipping-and-launch — MIT
- tomzx/agents — skills/deploy-pr/SKILL.md — deploy-pr — MIT
- github/awesome-copilot — skills/devops-rollout-plan/SKILL.md — devops-rollout-plan — MIT

This is an Anthracite-specific rewrite. Fixed pre-launch checklists, universal feature flags, preset rollout percentages and wait times, GitHub-specific deployment commands, and blanket rollback assumptions are intentionally not inherited.
