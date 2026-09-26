---
name: debugging-recovery
description: Diagnose failures by first creating a tight reproducible signal, then testing falsifiable hypotheses until the root cause is established. Correct the root cause, add regression protection, verify recovery, and remove temporary diagnostic scaffolding.
---

# Debugging and Recovery

## Purpose

Debugging is evidence-driven diagnosis, not a sequence of guesses.

The first goal is not to edit code. It is to create a reliable feedback loop that distinguishes "failure present" from "failure absent".

Then use that loop to locate root cause and prove recovery.

## Use when

Use this skill for:

- reproducible bugs;
- failing tests;
- local or CI failures;
- regressions;
- unexpected behavior;
- integration failures;
- performance anomalies where the first need is diagnosis rather than optimization;
- blocked implementation where the cause is technical failure.

For an active production outage or material live degradation, use incident response first to stabilize the system. Debugging may operate inside the incident once immediate harm is controlled.

## Workflow

### 1. Describe the symptom precisely

Record:

- expected behavior;
- observed behavior;
- environment/context;
- frequency;
- earliest known occurrence;
- known recent changes if relevant.

Separate observation from theory.

"API returns 500 for request X" is a symptom.

"The ORM is broken" is a hypothesis.

### 2. Build the tightest reliable reproducer

Choose the cheapest loop that can reliably show the failure:

- focused automated test;
- command-line invocation;
- curl/API request;
- small script/harness;
- browser reproduction;
- trace query;
- minimal data fixture;
- benchmark;
- differential comparison;
- bisect.

A useful reproducer is:

- repeatable;
- fast enough for iteration;
- narrow enough to isolate evidence;
- close enough to the real failure to remain valid.

If reproduction is intermittent, first improve observability or collect enough runs to characterize it.

### 3. Confirm the reproducer

Run it before fixing anything.

Verify:

- it actually fails;
- the failure matches the reported symptom;
- failure is not caused by the harness itself.

No reliable failure signal means the fix loop is not ready.

### 4. Minimize the failing surface

Reduce variables where possible:

- smallest input;
- smallest environment;
- smallest affected module;
- one dependency at a time;
- known-good vs failing version;
- one configuration difference.

Do not minimize so aggressively that you remove the real trigger.

### 5. Form falsifiable hypotheses

For each plausible cause, state:

- hypothesis;
- evidence that would support it;
- evidence that would reject it;
- cheapest next observation.

Prefer experiments that eliminate whole classes of causes.

Do not change multiple independent things at once.

### 6. Instrument only where evidence is missing

Add temporary diagnostics when existing telemetry cannot answer the hypothesis.

Examples:

- structured logging;
- assertions;
- trace spans;
- counters;
- state snapshots;
- timing measurements.

Avoid indiscriminate log flooding.

Do not expose secrets or sensitive data while debugging.

### 7. Trace to root cause

Keep asking why the failure occurs until the explanation identifies the source condition that should change.

Distinguish:

- **symptom location** — where the failure is visible;
- **propagation path** — how bad state travels;
- **root cause** — the earliest correctable condition that produces the failure.

Do not patch a downstream symptom when an upstream invariant is broken.

### 8. Correct minimally

Change the smallest source behavior that removes the root cause while preserving unrelated behavior.

If the required fix would materially alter the active implementation contract, treat it as a contract exception rather than silently expanding scope.

### 9. Add regression protection

Where practical, keep a test or other deterministic check that would fail if the root cause returned.

For a bug fix, prefer the reproducer itself becoming the regression test.

### 10. Verify recovery

Use the canonical verification strategy:

`../../execution/verification.md`

At minimum:

- original reproducer is green;
- affected-scope checks are green;
- original user/system scenario works where practical;
- no known new failure was introduced.

### 11. Remove temporary diagnostics

Remove temporary:

- debug logs;
- probes;
- breakpoints;
- test-only hacks;
- local feature switches;

unless they have earned a permanent observability role.

### 12. Capture durable learning only when useful

If root cause reveals:

- missing invariant;
- architecture flaw;
- observability gap;
- recurring test gap;
- runbook gap;

route that improvement to the owning lifecycle artifact.

Do not create a permanent debugging diary.

## Recovery after destructive or stateful failures

Some failures require restoring state, not only fixing source.

Before recovery:

- understand what state may be partial or corrupt;
- preserve evidence where security/data integrity matters;
- identify the last known-good state;
- distinguish rollback from forward repair;
- verify the recovered state independently.

Do not assume application-code rollback reverses database or external side effects.

## Output contract

### Symptom

Observed vs expected.

### Reproducer

Exact focused mechanism proving the failure.

### Root Cause

Evidence-backed explanation.

### Fix

Minimal source correction.

### Regression Protection

Test/check that catches recurrence.

### Recovery

State restoration or operational action if needed.

### Verification

Fresh evidence from reproducer and affected scope.

### Follow-up

Only durable gaps that belong to another lifecycle owner.

## Red flags

- editing before reproducing when reproduction is feasible;
- shotgun fixes;
- multiple unrelated changes in one experiment;
- "probably" accepted as root cause;
- fixing symptom location without tracing origin;
- CI used as the only debugging loop for a locally reproducible failure;
- temporary logs left permanently by accident;
- secrets/PII copied into debug output;
- application rollback assumed to undo stateful side effects;
- debugging used to silently rewrite requirements.

## Completion check

Before declaring recovery, confirm:

- the failure was reproduced or the inability to reproduce is explicitly explained;
- root cause is supported by evidence;
- the fix targets root cause;
- regression protection exists where practical;
- the original reproducer is green;
- affected-scope verification is green;
- state recovery is verified when applicable;
- temporary diagnostics are cleaned up;
- contract changes, if needed, were escalated rather than hidden.

## Provenance

Upstream mechanisms studied:

- mattpocock/skills — `skills/engineering/diagnosing-bugs/SKILL.md` — `diagnosing-bugs` — MIT
- obra/superpowers — `skills/systematic-debugging/SKILL.md` — `systematic-debugging` — MIT
- addyosmani/agent-skills — `skills/debugging-and-error-recovery/SKILL.md` — `debugging-and-error-recovery` — MIT

This is an Anthracite-specific rewrite. Harness-specific debugging tools, fixed phase rituals, and foreign artifact storage are intentionally not inherited.
