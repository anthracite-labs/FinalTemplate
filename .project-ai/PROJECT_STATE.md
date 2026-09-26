# Project State

This file is a bounded snapshot of accepted, durable project reality.

Record only the current project position. Do not use it as a diary, backlog, CI log, architecture document, changelog, project profile, or chat history.

Update it only when accepted reality materially changes. Activity alone is not state. A pull request opening, a test failing, Arena starting work, a workflow running, or an implementation commit does not by itself justify an update.

Reconcile this file after accepted work has landed on `main`. It describes accepted reality, never anticipated reality.

## Phase

Uninitialized.

## Current Objective

Bootstrap this repository into its actual project using `.project-ai/bootstrap/project.md`.

## Accepted Decisions

- The repository root belongs to the actual project.
- Internal AI collaboration infrastructure lives under `.project-ai/`.
- GitHub Issues and pull requests own executable work and transient execution state.
- Normal ChatGPT owns understanding, decisions, planning, dispatch, control-plane maintenance, and contract review.
- Arena owns product implementation inside an approved GitHub Issue contract.
- Human acceptance remains the final authority before merge.
- Full repository acceptance is terminal verification, not the implementation feedback loop.
- Project facts remain canonical in the actual project artifacts; this file is only a compressed current-state projection.

## Durable Blockers

None.

## Latest Accepted Milestone

FinalTemplate control-plane baseline established.

## Next Authorized Action

Run project bootstrap/reconciliation when creating or adopting a real project.

## Authoritative References

- `.project-ai/bootstrap/project.md`
- `.project-ai/routing/capabilities.md`
- `.project-ai/routing/route.md`
- `.project-ai/execution/arena-dispatch.md`
- `.project-ai/execution/verification.md`
