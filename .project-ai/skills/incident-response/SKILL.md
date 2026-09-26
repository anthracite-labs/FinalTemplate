---
name: incident-response
description: Respond to active production incidents by establishing impact, stabilizing or containing harm, using live telemetry and recent-change evidence, applying reversible evidence-driven mitigations, verifying user-facing recovery, and handing durable learning to postmortem work.
---

# Incident Response

## Purpose

During an active incident, restore safe service and limit harm.

Perfect explanation can wait when users, data, security, or availability are actively at risk.

This skill is for live operational incidents, not ordinary local debugging.

Use debugging-recovery inside the incident when root-cause analysis needs a focused reproducer.

## Trigger

Use this skill when there is active or credible production impact such as:

- outage;
- severe degradation;
- elevated error rate;
- data integrity failure;
- queue or job failure affecting users;
- widespread integration failure;
- security compromise;
- material availability or latency breach;
- uncontrolled rollout impact.

A normal bug with no active operational impact belongs in debugging-recovery.

## Workflow

### 1. Confirm the incident

Establish:

- what is failing;
- who or what is affected;
- when it started or was detected;
- current user/business/security impact;
- whether impact is ongoing;
- evidence source.

Do not declare severity from emotion or one noisy metric.

### 2. Classify severity by impact

Use the project's existing incident taxonomy if one exists.

If none exists, reason from:

- user impact;
- data loss or corruption;
- security exposure;
- breadth/blast radius;
- duration;
- contractual or regulatory impact;
- available workaround.

Do not invent response-time commitments that the organization has not adopted.

### 3. Establish coordination appropriate to incident size

For material incidents, identify who is:

- coordinating decisions;
- performing technical investigation or mitigation;
- communicating status;
- handling security/legal/compliance escalation where relevant.

A tiny team may combine roles. Do not create role ceremony that slows response.

### 4. Establish live system state

Use actual observability and provider evidence.

Check as relevant:

- errors;
- latency;
- throughput;
- SLO or health state;
- queue depth or job failure;
- infrastructure saturation;
- dependency health;
- alerts;
- data integrity;
- recent deployments and configuration changes.

Compare to known baseline where possible.

Do not guess blast radius from one log line.

### 5. Stabilize or contain immediate harm

When harm is ongoing, prefer the safest bounded mitigation that can reduce impact quickly.

Examples:

- roll back a suspect deployment;
- disable a feature;
- shift traffic;
- stop a destructive job;
- isolate a compromised credential or component;
- reduce load;
- fail over;
- pause writes to protect integrity.

For each intervention, state:

- expected effect;
- signal that confirms it worked;
- recovery or reversal path where practical.

Random changes are not mitigation.

### 6. Preserve evidence when needed

For security, fraud, data corruption, or other forensic-sensitive incidents, preserve relevant evidence before destructive cleanup when doing so does not worsen active harm.

Coordinate with security engineering for security incidents.

Do not copy sensitive data into ad-hoc chat or logs.

### 7. Investigate enough root cause to guide mitigation

Form evidence-based hypotheses.

Correlate:

- recent changes;
- failing dependencies;
- error patterns;
- resource pressure;
- data changes;
- tenant or request characteristics.

The immediate goal is enough understanding to restore safe service.

Deep causal analysis can continue after stabilization.

### 8. Communicate impact and state

For incidents requiring stakeholder communication, keep updates factual:

- current status;
- user impact;
- mitigation in progress;
- known uncertainty;
- next update point if the organization uses one.

Do not speculate about cause before evidence supports it.

Do not bury active impact under implementation detail.

### 9. Verify recovery from user-facing signals

Recovery requires more than a command completing.

Verify:

- affected user or API path works;
- error rate returns toward expected baseline;
- latency/throughput recover where relevant;
- queues drain or jobs resume;
- data integrity is acceptable;
- no new critical alert indicates continued impact.

### 10. Monitor for recurrence

After immediate recovery, observe long enough to establish that the mitigation is stable according to project risk.

Do not use an arbitrary universal monitoring window.

### 11. Close active response

Close the active incident when:

- immediate impact is resolved or accepted degraded mode is stable;
- ongoing risks are known;
- temporary mitigations are documented or tracked;
- ownership of remaining work is clear;
- evidence needed for learning is preserved.

Then hand off to postmortem-learning when the event has meaningful learning value.

## Security incident branch

When compromise is suspected:

- invoke security-engineering;
- contain attacker access or exposed credentials;
- preserve evidence;
- identify affected principals/resources;
- avoid destroying forensic data unnecessarily;
- consider notification, privacy, legal, or regulatory obligations using appropriate authoritative guidance.

Security incidents may require stricter communication channels and access control than ordinary outages.

## Output contract

### Incident State

Active, mitigating, monitoring, or resolved.

### Impact

Affected users/systems/data and current blast radius.

### Evidence

Telemetry and operational facts supporting the assessment.

### Actions

Mitigations attempted, expected effect, and observed result.

### Current Hypothesis

Only as strong as evidence permits.

### Recovery Verification

Signals proving service is safe enough to leave active response.

### Remaining Risk

Temporary mitigations, degraded behavior, unresolved root cause, or follow-up.

### Handoff

Postmortem, security investigation, maintenance work, or ordinary debugging as appropriate.

## Red flags

- random changes without expected effect;
- chasing perfect root cause while damage continues;
- rollback performed without considering data or external side effects;
- one metric treated as full blast-radius evidence;
- speculative cause communicated as fact;
- sensitive evidence pasted into broad channels;
- incident closed when deploy succeeded but user signals remain bad;
- mandatory heavyweight incident roles for tiny events;
- ordinary bugs escalated into incident process without operational impact.

## Completion check

Before ending active response, confirm:

- impact and blast radius are evidence-based;
- ongoing harm is contained or resolved;
- mitigation effects were observed;
- user-facing/system health is verified;
- security evidence was preserved where required;
- temporary mitigations and residual risk are tracked;
- remaining diagnostic work has an owner;
- meaningful learning is handed to postmortem-learning.

## Provenance

Upstream mechanisms studied:

- wshobson/agents — plugins/incident-response/skills/incident-runbook-templates/SKILL.md — incident-runbook-templates — MIT
- tomzx/agents — skills/observe-production/SKILL.md — observe-production — MIT
- sickn33/agentic-awesome-skills — skills/incident-response/SKILL.md — incident-response — MIT; the skill declares a community source in BagelHole/DevOps-Security-Agent-Skills

This is a substantial Anthracite rewrite. Fixed severity response times, mandatory runbook templates, .sdlc context, vendor-specific commands, and security-only incident framing are intentionally not inherited.
