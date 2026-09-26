---
name: verification-before-completion
description: Enforce fresh evidence before any completion claim. Trace acceptance criteria to observable proof, follow FinalTemplate's canonical narrow-to-broad verification strategy, and keep technical verification distinct from contract compliance, human acceptance, and merge state.
---

# Verification Before Completion

## Canonical owner

Universal verification strategy is owned by ../../execution/verification.md.

Read and follow that file.

This skill is the completion gate layered on top of that strategy. It does not redefine command selection, feedback-loop depth, or terminal acceptance.

If this skill and the canonical verification file conflict, the canonical verification file wins.

## Core rule

No completion claim without fresh evidence.

A belief that work should pass is not evidence.

A previous run against an older candidate is not evidence for the current candidate.

A green unit test is not evidence that every acceptance criterion is satisfied.

## Use when

Use this skill before saying that work is complete, fixed, passing, ready for review, technically verified, or safe to hand off as a finished candidate.

Also use it when reviewing whether a PR has evidence for its acceptance criteria.

## State separation

Keep these states distinct:

VERIFIED is not CONTRACT-COMPLIANT, which is not ACCEPTED, which is not MERGED.

- VERIFIED means required technical evidence for the candidate is fresh and sufficient.
- CONTRACT-COMPLIANT means normal ChatGPT has reviewed the candidate against the active contract.
- ACCEPTED means the human has given final acceptance.
- MERGED means GitHub history contains the accepted integration.

This skill establishes only verification.

## Workflow

### 1. Identify the candidate

Verification applies to a concrete candidate state.

Identify branch, commit, diff or working candidate, active Issue or requirement contract, relevant generated state, and environment if runtime behavior is part of the proof.

Any source or required generated-state change after terminal acceptance invalidates that acceptance evidence.

### 2. Identify what must be proven

Read the acceptance criteria and required verification.

Create a mental or explicit evidence map:

criterion → implementation surface → proof

Each material criterion needs evidence appropriate to its behavior.

### 3. Distinguish traceability from runtime proof

#### Static traceability

Can the reviewer point to implementation or configuration intended to satisfy the criterion?

#### Runtime or behavioral proof

Can the required behavior actually be exercised, tested, inspected, or measured?

Not every criterion requires a literal runtime demo, but every material criterion needs observable proof.

### 4. Run the smallest meaningful checks during the loop

Follow ../../execution/verification.md.

Do not rerun full repository acceptance merely because one focused test failed.

If a narrow failure exists:

1. leave terminal acceptance;
2. reproduce narrowly;
3. diagnose and correct;
4. regain focused green;
5. produce a new finished candidate.

### 5. Run terminal repository acceptance on the finished candidate

Only when implementation is finished, run the complete project-defined terminal acceptance required for that candidate.

Use actual project commands.

Do not invent generic commands.

Read the entire relevant result: exit status, failures, skipped or unavailable checks when material, and any mutation of candidate state.

A verification process that changes the candidate may require acceptance to run again against the resulting state.

### 6. Verify acceptance criteria explicitly

After technical commands are green, revisit each material acceptance criterion.

Ask which evidence proves it, whether that evidence applies to the current candidate, whether the proof exercises the actual contract rather than an implementation proxy, and whether any criterion remains unverified.

Tests passing does not automatically mean the requirements are satisfied.

### 7. Scale extra depth to risk

For high-risk, poorly specified, cross-cutting, security-sensitive, migration, or user-critical changes, deepen verification where the ordinary project suite does not prove enough.

Possible additions include a focused integration scenario, contract test, browser or user-flow proof, migration dry run, security-specific check, performance benchmark, generated-state comparison, or compatibility check.

Do not add heavyweight quality theater to every tiny change.

### 8. Report evidence, not optimism

A verification report should state what was run, which candidate it applied to, the result, acceptance criteria proved, checks unavailable or unresolved, and limitations.

If a check could not run, say so.

Do not infer PASS from absence of evidence.

## Verification outcome

Use one of:

### VERIFIED

All required technical verification and acceptance evidence for the current candidate is fresh and sufficient.

### NOT VERIFIED

One or more required checks failed, are unavailable, are stale, or do not prove the acceptance boundary.

Do not use VERIFIED to imply contract compliance or human acceptance.

## Artifact ownership

Verification evidence normally belongs in the PR completion report, CI or provider result, test output, or project-owned evidence artifact when required.

Do not create a permanent parallel verification database.

## Red flags

- should pass;
- looks good before running checks;
- relying on an old run after source changed;
- trusting an implementation agent's success statement;
- partial suite presented as full acceptance;
- lint presented as build proof;
- tests presented as proof of every requirement without criteria review;
- coverage percentage presented as behavioral verification;
- full CI repeatedly used as the local debugging loop;
- hidden unavailable checks;
- VERIFIED used as a synonym for ACCEPTED.

## Completion check

Before stating VERIFIED, confirm:

- candidate identity is clear;
- required focused evidence is current;
- terminal repository acceptance ran on the finished candidate;
- every material acceptance criterion maps to evidence;
- runtime or observable proof exists where static traceability is insufficient;
- unavailable verification is disclosed;
- source or generated state did not change after terminal acceptance;
- no claim exceeds the evidence.

## Provenance

Upstream mechanisms studied:

- obra/superpowers — skills/verification-before-completion/SKILL.md — verification-before-completion — MIT
- tomzx/agents — skills/verify-pr/SKILL.md — verify-pr — MIT
- github/awesome-copilot — quality-playbook skill and supporting references — quality-playbook — MIT

This is an Anthracite-specific rewrite. Recording and demo tooling, worktree requirements, multi-agent quality orchestration, and heavyweight universal audit passes are intentionally not inherited.
