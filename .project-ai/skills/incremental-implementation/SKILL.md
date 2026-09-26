---
name: incremental-implementation
description: Execute approved work in thin, verifiable increments while keeping the repository working, preserving scope, and escalating material contract discoveries instead of silently redesigning the project during implementation.
---

# Incremental Implementation

## Authority

For Arena product work, `../../execution/arena-dispatch.md` owns the implementation authority, branch/PR boundary, contract exceptions, and correction lifecycle.

This skill governs how implementation proceeds *inside* that approved boundary.

It never expands implementation authority.

## Purpose

Build one complete, meaningful increment at a time.

Each increment should reduce uncertainty, leave the candidate in a coherent state, and produce evidence before the next slice begins.

Avoid large unverified code drops.

## Use when

Use this skill for:

- multi-file feature work;
- implementation from an approved plan or Issue;
- refactoring required by an approved change;
- migrations that can be decomposed safely;
- any task large enough that a single unverified edit would hide too much failure surface.

For a truly mechanical atomic edit, the full slicing ceremony may be unnecessary.

## Preconditions

Before implementation:

- the active execution contract is identifiable;
- scope and non-goals are known;
- material architecture constraints are accepted;
- acceptance criteria are observable;
- project-owned verification commands can be discovered.

If these are not true, return to planning or the control plane rather than inventing them.

## Workflow

### 1. Read the active contract

Identify:

- objective;
- allowed scope;
- prohibited scope;
- constraints;
- acceptance criteria;
- required verification;
- contract exceptions.

Load only the project context needed for the current slice.

Do not reconstruct intent from old chat when the Issue or repository owns it.

### 2. Choose the next smallest meaningful slice

Prefer a slice that:

- delivers one complete behavior;
- crosses only the layers required for that behavior;
- can be tested or demonstrated;
- leaves the repository coherent;
- exposes important risk early.

Avoid horizontal batches such as "all models", then "all APIs", then "all UI" unless the work is an inherently wide migration.

### 3. Keep implementation simple

Implement the simplest correct behavior that satisfies the current contract.

Avoid:

- abstractions for hypothetical future use;
- opportunistic modernization;
- unrelated cleanup;
- broad renames not required by the slice;
- new features that merely seem useful.

If adjacent debt is discovered, record it as follow-up rather than silently expanding scope.

### 4. Use TDD for behavior changes

When behavior can be tested first, use `../test-driven-development/SKILL.md`.

For a bug fix, reproduce the failure before correcting it.

For configuration or other work where a behavioral test is not the right tool, use the smallest meaningful verification that can prove the change.

### 5. Verify the slice narrowly

Use `../../execution/verification.md`.

Prefer:

1. exact focused test or reproducer;
2. affected module/component;
3. affected subsystem only when needed.

Do not run terminal full-repository acceptance after every small edit.

### 6. Keep the repository coherent

After a completed slice:

- relevant focused checks are green;
- temporary scaffolding is removed or intentionally retained;
- incomplete behavior is safely hidden or structurally non-user-facing if partial landing is allowed;
- existing behavior outside scope remains intact.

Feature flags are one option, not a universal requirement.

### 7. Treat implementation discoveries correctly

Classify discoveries.

#### Local implementation detail

Examples:

- helper shape;
- local function decomposition;
- internal naming;
- small refactor needed to satisfy the contract.

Proceed within the approved scope.

#### Implementation defect

The contract is valid but the code or test is wrong.

Diagnose and correct within the same branch/PR.

#### Contract exception

The implementation reveals a material need to change:

- scope;
- architecture;
- accepted requirements;
- user-visible behavior;
- security/trust boundaries;
- major dependencies/tooling;
- data model or external contract.

Stop and report according to `../../execution/arena-dispatch.md`.

Do not hide a contract change inside "implementation detail".

### 8. Continue slice by slice

Each successful slice becomes the foundation for the next.

Do not restart reasoning from scratch when accepted earlier slices still hold.

Keep enough implementation evidence in commits, tests, and the PR to make the final candidate understandable without an implementation diary.

### 9. Produce a finished candidate

When all approved slices are complete:

- run affected-scope verification;
- remove temporary diagnostics;
- reconcile documentation required by the change;
- ensure the diff remains inside scope;
- prepare for terminal verification.

Then use `../verification-before-completion/SKILL.md`.

## Output contract

Implementation should leave:

- working code/configuration inside approved scope;
- focused tests or other regression protection where appropriate;
- targeted verification evidence;
- no silent contract expansion;
- explicit contract exception evidence if implementation cannot proceed safely;
- a coherent finished candidate ready for terminal verification and review.

## Red flags

- hundreds of lines written before any meaningful check;
- implementing the whole feature before exercising one path;
- unrelated cleanup mixed into the slice;
- broad refactor justified only as "while we're here";
- changing requirements to fit the implementation;
- swallowing a security or architecture discovery as local detail;
- repeated full-suite/CI runs instead of a focused feedback loop;
- leaving the branch knowingly broken between ordinary slices;
- declaring completion before fresh terminal verification.

## Completion check

Before handoff, confirm:

- every approved behavior has an implemented slice;
- slices remained within the active contract;
- focused verification was used during the loop;
- implementation defects were corrected without changing the contract;
- material contract discoveries were escalated;
- unrelated cleanup was excluded;
- the finished candidate is coherent and ready for terminal verification.

## Provenance

Upstream mechanisms studied:

- addyosmani/agent-skills — `skills/incremental-implementation/SKILL.md` — `incremental-implementation` — MIT
- obra/superpowers — `skills/executing-plans/SKILL.md` — `executing-plans` — MIT
- bmad-code-org/BMAD-METHOD — `skills/bmad-build/SKILL.md` — `bmad-build` — MIT

This is an Anthracite-specific rewrite. Superpowers worktree/ledger/subagent orchestration, BMAD runtime scripts, mandatory commit cadence, and foreign execution workspaces are intentionally not inherited.
