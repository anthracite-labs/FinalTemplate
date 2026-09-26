---
name: pr-integration-correction
description: Iterate on an existing PR by evaluating review feedback and CI evidence, reproducing failures narrowly, fixing bounded implementation defects on the same branch, and escalating contract changes instead of silently expanding scope. Never merge from this skill.
---

# PR Integration and Correction

## Authority

For Arena product PRs, use the branch, correction, contract-revision, review, acceptance, and merge boundaries in ../../execution/arena-dispatch.md.

This skill owns the technical correction loop inside those boundaries.

It never authorizes merge.

## Purpose

Bring a PR from a technically failing or review-defective state to a new finished candidate without using remote CI as the primary debugger, blindly accepting review comments, changing the contract in secret, opening replacement PRs for ordinary corrections, or crossing human acceptance and merge gates.

## Use when

Use this skill when an existing PR has:

- failing actionable CI;
- contract-review corrections;
- substantive code-review findings;
- reviewer feedback requiring technical evaluation;
- flaky or infrastructure checks that need classification;
- a bounded implementation defect discovered after review.

## Workflow

### 1. Identify the PR and active contract

Establish repository, PR number and branch, current head commit, active Issue contract or revision when applicable, current verification state, and review findings already resolved versus still open.

Do not act on stale feedback from an older head without checking whether it still applies.

### 2. Collect actionable evidence

Gather failing check names and logs, review comments and findings, contract-review outcome, current diff, and relevant project commands.

Separate human or merge gates from technical failures.

### 3. Classify each item

#### Implementation defect

Code, test, or configuration fails the valid contract.

Correct on the same branch.

#### Test defect

The test is wrong relative to accepted behavior.

Correct the test only with evidence from the contract and implementation semantics.

#### Review misunderstanding

Feedback does not apply after inspecting code and project reality.

Respond with technical evidence; do not implement it merely to satisfy the comment.

#### Infrastructure or transient failure

A network, provider, or flaky environment failure not caused by the candidate.

Re-run or report according to project policy rather than changing product code.

#### Contract exception

Feedback or failure exposes a need to change requirements, architecture, scope, security boundary, dependency policy, data contract, or another material decision.

Return to the control plane under ../../execution/arena-dispatch.md.

### 4. Evaluate review feedback before implementing

For each substantive comment:

1. read it completely;
2. restate the technical requirement internally;
3. verify it against codebase reality;
4. check accepted requirements and architecture;
5. determine whether it is correct for this project;
6. implement only if valid.

External reviewers are useful evidence, not automatic authority.

If a comment conflicts with an accepted project decision, escalate rather than silently following it.

### 5. Reproduce CI failures narrowly

For each actionable failure:

1. read the actual failing log;
2. identify the assertion, error, or rule;
3. create or run the smallest local reproducer where practical;
4. state the root cause before editing;
5. correct the root cause;
6. run the focused check locally.

CI should confirm the correction, not serve as the only edit-run loop.

### 6. Keep corrections bounded

Ordinary corrections remain on the same branch and PR.

Do not create a fresh PR for each fix, mix unrelated cleanup, refactor broadly because review exposed nearby debt, or change the active contract to make tests pass.

If correction reveals broader project work, capture it separately.

### 7. Verify each correction

Use ../debugging-recovery/SKILL.md for root-cause failures, ../test-driven-development/SKILL.md when behavior needs regression protection, and ../../execution/verification.md for check selection.

Regain targeted green before pushing another candidate.

### 8. Push a new candidate and re-evaluate

After bounded corrections, update the branch, let relevant provider checks run, inspect new high-signal feedback, and ensure previous fixes still hold.

If the same failure recurs after reasonable root-cause attempts, report the blocker instead of blindly looping.

### 9. Stop at technical readiness

When actionable CI is green or appropriately explained, required review corrections are resolved, post-correction verification is fresh, and only human approval or merge gates remain, stop and report the current state.

Do not mark ready, approve, or merge unless that separate action was explicitly authorized and permitted by canonical policy.

## Output contract

### PR Candidate

PR and head being corrected.

### Resolved Items

Failure or review item → root cause → correction → focused evidence.

### Unresolved Items

Including infrastructure or ambiguous feedback.

### Contract Exceptions

Material changes returned to the control plane.

### Verification State

Fresh targeted and terminal evidence as applicable.

### Remaining Gates

Human review, acceptance, merge, provider gate, or other non-technical state.

## Red flags

- changing code from a CI failure without reading the log;
- repeated push-and-pray CI cycles;
- reviewer comment implemented without checking codebase reality;
- performative agreement replacing technical evaluation;
- low-priority style suggestion treated as contract requirement;
- correction branch expanded with unrelated cleanup;
- material architecture or requirements change hidden in a fix;
- opening a new PR for an ordinary implementation miss;
- merging because checks are green.

## Completion check

Before handing the PR back, confirm:

- current head and active contract are known;
- every actionable failure or comment is classified;
- code failures were reproduced narrowly where practical;
- root causes, not symptoms, were corrected;
- valid feedback was implemented and invalid feedback was technically rejected;
- corrections stayed within scope;
- contract exceptions were escalated;
- fresh verification applies to the current head;
- merge and acceptance gates remain separate.

## Provenance

Upstream mechanisms studied:

- getsentry/skills — skills/iterate-pr/SKILL.md — iterate-pr — Apache-2.0
- tomzx/agents — skills/handle-pr-ci/SKILL.md — handle-pr-ci — MIT
- obra/superpowers — skills/receiving-code-review/SKILL.md — receiving-code-review — MIT

This is an Anthracite-specific rewrite. Bundled PR scripts, fixed polling loops, foreign reviewer buckets, mandatory user approval before each technical commit, and automatic merge or readiness behavior are intentionally not inherited.
