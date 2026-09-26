---
name: postmortem-learning
description: Turn resolved incidents, significant near-misses, releases, features, or project work into evidence-based learning. Reconstruct what happened without blame, identify systemic causes and contributing conditions, preserve practices worth repeating, and create concrete tracked improvements only where they add value.
---

# Postmortem and Learning

## Purpose

Learning work should change future behavior, systems, or decisions.

A postmortem is not an incident transcript and not a blame exercise.

A retrospective does not require an outage; meaningful feature, release, migration, or project work can also justify structured learning.

Do not run a ceremony when there is no useful lesson to preserve.

## Use when

Use this skill after:

- a material incident;
- a near-miss with meaningful systemic learning;
- a difficult migration or release;
- a feature or project with surprising outcomes;
- repeated rework or process failure;
- a technical decision that produced important evidence;
- unusually successful practices worth repeating.

## Workflow

### 1. Establish the event and learning purpose

State:

- what event or body of work is being reviewed;
- why learning is worthwhile;
- which evidence sources exist.

Do not begin with who made a mistake.

### 2. Reconstruct the timeline from evidence

Prefer:

- logs;
- alerts;
- deployment history;
- commits;
- issue/PR timestamps;
- incident chat;
- provider events;
- monitoring data.

Human recollection can fill context, but distinguish memory from timestamped evidence.

Do not invent exact times not supported by evidence.

### 3. Quantify impact honestly

For incidents, capture as available:

- duration;
- affected users or traffic;
- failed/degraded capabilities;
- data loss or corruption;
- security/privacy impact;
- contractual/SLA impact;
- business impact.

For project/release retrospectives, impact may instead be:

- schedule or scope variance;
- rework;
- defects;
- operational burden;
- achieved outcome;
- abandoned assumptions.

If a quantity is unknown, say unknown rather than fabricating precision.

### 4. Identify root/systemic causes

Ask why the system allowed the event, not which person should have been better.

Potential systemic causes include:

- missing guardrail;
- ambiguous ownership;
- unsafe default;
- architecture flaw;
- insufficient test coverage of a behavior class;
- observability gap;
- deployment gap;
- dependency behavior;
- documentation or runbook gap;
- incentive/process mismatch.

"Human error" is not a useful terminal root cause when the system could reasonably have prevented, detected, or limited the mistake.

Use Five Whys only when it helps. Stop when a correctable systemic gap is clear.

### 5. Separate contributing factors

Not every worsening condition is the root cause.

Identify factors such as:

- alert delay;
- high load;
- missing fixture;
- unusual tenant/data shape;
- unclear runbook;
- simultaneous change;
- slow escalation.

This makes action selection more precise.

### 6. Capture detection and response learning

Ask:

- how was the problem first detected;
- what should have detected it;
- what made diagnosis slow or fast;
- which mitigation worked;
- which action created noise or risk;
- whether communication or ownership was clear.

Feed observability and incident-response improvements to their owning artifacts.

### 7. Capture what worked

Do not produce a failure-only document.

Preserve practices worth repeating:

- tests that caught regressions;
- architecture that contained blast radius;
- rollout controls that reduced damage;
- clear ownership;
- effective tooling;
- useful runbooks;
- successful user validation.

Learning includes amplification, not only correction.

### 8. Create concrete actions selectively

Each action should address a demonstrated cause or valuable improvement.

A strong action has:

- clear deliverable;
- owner or owning system/team according to project practice;
- priority;
- due date or revisit condition when useful;
- tracking location.

Avoid vague items such as "be more careful", "improve monitoring", or "write more tests".

Do not create action items merely to make the postmortem look complete.

### 9. Put follow-up in the real tracker

Action items belong in the project's actual work-tracking system.

Do not rely on a postmortem document as the only place work is tracked.

For this template, GitHub Issues and PRs own executable work unless the actual project establishes another approved tracker.

### 10. Preserve the learning where it belongs

Possible durable outputs:

- postmortem document in existing project convention;
- ADR update;
- runbook change;
- test;
- alert rule;
- architecture correction;
- project documentation;
- GitHub Issue for follow-up.

Do not create a .project-ai learning archive.

## Output contract

### Summary

What happened or what work was reviewed.

### Impact / Outcome

What changed for users, systems, or project delivery.

### Timeline

Evidence-based when relevant.

### Root/Systemic Causes

Correctable underlying conditions.

### Contributing Factors

Conditions that amplified impact.

### Detection / Response Learning

What helped or hindered understanding and recovery.

### What Worked

Practices worth preserving.

### Actions

Concrete tracked improvements only where justified.

### Durable Learnings

Technical or process insights worth carrying forward.

## Blameless does not mean vague

It is valid to state that a person or command performed an action when that is factual.

The analysis should ask why the system made the action possible, hard to detect, or disproportionately damaging.

Avoid moral judgment and hindsight framing.

## Red flags

- naming a person as the root cause;
- invented timestamps or impact estimates;
- "human error" as the final explanation;
- action item "be more careful";
- every postmortem ends with "add monitoring";
- dozens of low-value follow-ups;
- lessons kept only inside a document with no tracked action;
- postmortem performed for every tiny bug;
- only failures captured while effective practices are ignored.

## Completion check

Before closing learning work, confirm:

- timeline and impact distinguish evidence from recollection;
- systemic causes are deeper than blame;
- contributing factors are separated;
- detection and response gaps are captured;
- useful practices are preserved;
- action items are concrete and tied to real causes;
- follow-up work is tracked in the project system;
- durable learning is stored in the artifact that owns it.

## Provenance

Upstream mechanisms studied:

- wshobson/agents — plugins/incident-response/skills/postmortem-writing/SKILL.md — postmortem-writing — MIT
- github/awesome-copilot — skills/incident-postmortem/SKILL.md — incident-postmortem — MIT
- tomzx/agents — skills/create-learnings/SKILL.md — create-learnings — MIT

This is an Anthracite-specific rewrite. Fixed postmortem paths, mandatory templates, mandatory personal owners or dates for every action, .sdlc learning stores, and ritualized Five Whys are intentionally not inherited.
