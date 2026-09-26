---
name: observability-operations-design
description: Design and implement telemetry that makes production behavior diagnosable. Start from operator questions and user-visible reliability, choose logs/metrics/traces intentionally, define actionable alerts and SLOs where warranted, and avoid telemetry noise or sensitive-data leakage.
---

# Observability and Operations Design

## Purpose

Production behavior should be explainable from outside the process.

Observability is part of a production feature when operators need evidence that it is working, degrading, or failing.

Instrumentation should answer real questions. Telemetry without a question is noise.

## Use when

Use this skill when:

- a feature or service will run in production;
- adding external calls, queues, jobs, retries, or cross-service behavior;
- defining logs, metrics, traces, health checks, or alerts;
- reliability targets need SLIs/SLOs;
- a previous incident was hard to diagnose because evidence was missing;
- release criteria depend on production signals.

Do not add observability ceremony to static artifacts or purely local tooling with no operational need.

## Workflow

### 1. Start with operator questions

Before choosing telemetry, state the questions a responder should be able to answer.

Examples:

- Is the capability working for users?
- How often does it fail?
- What type of failure dominates?
- Is a dependency slow or unavailable?
- Is a queue backing up?
- Which request/job/tenant experienced the issue?
- Did a recent deployment change the behavior?

Every signal should help answer a question.

### 2. Identify critical paths and failure modes

Use requirements and architecture to identify:

- important user flows;
- state transitions;
- external dependencies;
- async boundaries;
- retries;
- queues;
- scheduled jobs;
- invariants whose violation matters.

Instrument the path, not every line.

### 3. Choose the correct signal

Use the signal whose shape matches the question.

#### Logs

Best for:

- specific event context;
- why one operation failed;
- state transition detail;
- diagnostic fields.

Prefer structured events with stable field names.

#### Metrics

Best for:

- rate;
- errors;
- duration;
- saturation;
- queue depth;
- aggregate business/operational counts.

Avoid unbounded label cardinality.

#### Traces

Best for:

- latency across boundaries;
- causal path through distributed work;
- dependency timing;
- one request/job across services.

Propagate trace/correlation context across async and network boundaries where useful.

### 4. Correlate operations

Use stable correlation identifiers for a single request, job, workflow, or other execution unit when cross-component reconstruction matters.

Do not use high-cardinality correlation IDs as metric labels.

For systems with several entry points, record enough structured context to distinguish how the operation started.

### 5. Protect telemetry

Telemetry is another data system.

Do not log:

- passwords;
- secrets;
- tokens;
- full payment data;
- unnecessary personal data;
- raw sensitive request/response bodies.

Prefer field allowlists.

Apply retention/access controls appropriate to telemetry sensitivity.

### 6. Define health signals

For request-driven behavior, consider rate/errors/duration.

For resources, consider utilization/saturation/errors.

For asynchronous work, consider:

- age of oldest item;
- queue depth;
- throughput;
- retry/dead-letter rates;
- completion latency.

Choose project-appropriate signals rather than blindly applying every framework.

### 7. Define SLIs before SLOs

When reliability objectives matter, define an SLI that reflects user-perceived success.

Examples:

- successful eligible requests / eligible requests;
- operations completed within latency target / total operations;
- durable successful writes / write attempts.

Avoid infrastructure proxies when they do not represent user outcome.

### 8. Set SLOs deliberately

An SLO should reflect:

- user expectations;
- business/contract requirements;
- current capability;
- cost of higher reliability;
- dependency limitations.

Do not default every service to "four nines".

SLA is an external agreement; SLO is an internal target; SLI is the measurement.

Do not conflate them.

### 9. Use error budgets where they change decisions

For services where SLOs govern reliability investment, error budgets can balance delivery and reliability work.

Do not add an error-budget process to a project that has no need for it.

If used, define what budget consumption changes:

- rollout risk;
- release pace;
- reliability priority;
- incident follow-up.

### 10. Define actionable alerts

An alert should lead to a useful response.

For each alert, specify:

- condition;
- duration/window;
- severity;
- user/system impact;
- first diagnostic action;
- runbook or response path;
- owner/escalation where applicable.

If nobody should act, prefer a dashboard or log over a page.

Alert on symptoms meaningful to users/services rather than every low-level fluctuation.

### 11. Add health/readiness checks where they have semantics

Health checks should answer a useful question.

Do not create an endpoint that returns 200 while the capability it claims to represent cannot function.

Separate liveness/readiness/dependency health only where the platform and failure model need it.

### 12. Verify telemetry

Instrumentation is not complete because code compiles.

Where practical, verify:

- expected log event appears;
- metric changes under controlled behavior;
- trace propagates across intended boundaries;
- alert expression can fire under test/simulation;
- sensitive fields are absent;
- dashboards/queries can answer the original operator questions.

Use `../../execution/verification.md`.

## Output contract

### Operator Questions

What must be diagnosable.

### Critical Paths / Failure Modes

What behavior needs visibility.

### Logs

Events and fields required.

### Metrics

SLIs and operational metrics.

### Traces

Boundaries requiring causal/latency visibility.

### Health Checks

Only where meaningful.

### SLO / Error Budget

Only where reliability policy requires them.

### Alerts / Runbooks

Actionable conditions and response.

### Data Handling

Telemetry privacy/security constraints.

### Verification

How the signals will be proven to exist and behave.

## Artifact ownership

Do not create a mandatory observability document or Prometheus file.

Put telemetry in the actual project:

- instrumentation code;
- telemetry configuration;
- dashboards;
- alert rules;
- runbooks;
- provider configuration;
- project documentation.

Use whatever system the project actually owns.

## Red flags

- "log everything";
- alerts with no action;
- user IDs/request IDs as metric labels;
- averages hiding tail latency;
- sensitive payloads in logs;
- instrumentation added only after production failure;
- dashboard metrics with no decision attached;
- SLO target chosen because it sounds professional;
- health endpoint that does not reflect meaningful readiness;
- vendor-specific observability architecture imposed on a provider-neutral project.

## Completion check

Before handoff, confirm:

- every telemetry signal answers a stated operator question;
- critical failure paths are diagnosable;
- signal type matches the question;
- correlation works where needed;
- sensitive data is excluded/minimized;
- SLOs reflect user-visible reliability when used;
- alerts are actionable;
- telemetry itself has verification evidence.

## Provenance

Upstream mechanisms studied:

- addyosmani/agent-skills — `skills/observability-and-instrumentation/SKILL.md` — `observability-and-instrumentation` — MIT
- tomzx/agents — `skills/create-observability/SKILL.md` — `create-observability` — MIT
- wshobson/agents — `plugins/observability-monitoring/skills/slo-implementation/SKILL.md` — `slo-implementation` — MIT

This is an Anthracite-specific rewrite. Prometheus/OpenTelemetry implementation examples, mandatory observability artifacts, fixed alert formats, and universal SLO/error-budget requirements are intentionally not inherited.
