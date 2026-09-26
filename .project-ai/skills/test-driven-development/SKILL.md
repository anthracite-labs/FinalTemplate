---
name: test-driven-development
description: Drive behavior changes and bug fixes through a real red-green-refactor loop at an intentional public seam. Require the test to fail for the expected reason before implementation, minimize implementation coupling, and preserve useful regression evidence.
---

# Test-Driven Development

## Purpose

Tests are executable behavioral evidence.

Use this skill to design and implement behavior through a disciplined red-green-refactor loop rather than writing code first and backfilling tests afterward.

TDD is an implementation technique inside incremental implementation, not a separate project phase.

## Use when

Use TDD for:

- new logic or behavior;
- bug fixes;
- behavior changes;
- edge-case handling;
- public contract changes;
- refactoring where existing behavior must be preserved.

Do not force TDD onto:

- documentation-only changes;
- static content with no behavior;
- mechanical configuration changes where another verification mechanism is more direct;
- generated files whose behavior is owned by their generator.

## Discover the repository first

Before the first test, discover:

- project test framework;
- focused-test command;
- broader test command;
- existing test locations and conventions;
- public seams used by neighboring tests;
- fixtures and test infrastructure;
- CI commands that actually gate the project.

Never assume a language, framework, or default command.

## Choose the test seam deliberately

Prefer the most stable observable interface that proves the required behavior.

A useful seam is:

- public enough that refactoring internals does not break the test;
- narrow enough to give fast, clear feedback;
- representative of real caller behavior;
- under project control.

Examples:

- public function/module interface;
- API route;
- CLI command;
- state transition;
- integration boundary;
- user flow when lower-level tests cannot prove the behavior.

When interface shape itself is under design, use architecture/interface design first.

## Avoid implementation-coupled tests

Prefer tests that assert observable behavior.

Avoid tests that primarily assert:

- private method calls;
- internal call order with no contract significance;
- mock interactions that merely mirror the implementation;
- values calculated using the same production logic being tested;
- snapshots so broad that failures provide no diagnosis.

Mocks and fakes are tools for boundaries, not evidence that internal wiring happened exactly one way.

## The loop

### 1. RED — specify one behavior

Write the smallest test that demonstrates the next required behavior.

The test should express:

- input or precondition;
- action;
- observable expected result.

Keep one behavioral reason for failure.

### 2. Run it and observe failure

The test must actually fail before implementation.

Confirm it fails for the expected reason.

A test that:

- passes immediately;
- crashes in setup unrelated to the behavior;
- fails for a typo or fixture bug;

has not yet established a useful RED state.

Fix the test or setup until the failure represents the missing/incorrect behavior.

### 3. GREEN — implement the minimum

Write the smallest reasonable production change that makes the failing test pass.

Do not solve hypothetical future cases during GREEN.

Run the focused test and observe it pass.

### 4. REFACTOR

With the behavior green:

- improve naming;
- remove duplication;
- simplify control flow;
- deepen a module where real leverage exists;
- remove temporary implementation scaffolding.

Run the relevant tests after refactoring.

Behavior must remain unchanged.

### 5. Repeat vertically

Add the next meaningful behavior through another red-green-refactor cycle.

Prefer tracer-bullet progress through the capability rather than building every low-level helper before one complete path works.

## Bug-fix pattern

For a reported regression:

1. reproduce the original failure in a test at the best available public seam;
2. observe RED for the actual bug;
3. diagnose root cause if it is not already known;
4. implement the smallest root-cause fix;
5. observe GREEN;
6. retain the test as regression protection;
7. verify the original real-world scenario when practical.

A test that never demonstrated the bug is weak regression evidence.

## Test quality checks

Ask:

- would this test fail if the required behavior broke;
- could the implementation be substantially refactored without rewriting the test;
- does the expected value come from independent reasoning;
- is the failure message/locality useful;
- are important boundary cases represented;
- is the test at the correct level;
- are mocks hiding the behavior we actually need confidence in.

Coverage percentage is not a substitute for these questions.

## External systems

For boundaries outside project control:

- use contract/integration tests when the real boundary can be exercised safely and economically;
- use fakes/stubs for deterministic local loops where appropriate;
- keep the adapter contract narrow;
- avoid mocking so deeply that the test proves only the mock setup.

## Verification relationship

During the TDD loop, run the focused test.

Do not repeatedly run terminal repository acceptance.

When the implementation unit is finished, follow `../../execution/verification.md` and `../verification-before-completion/SKILL.md`.

## Red flags

- production behavior implemented before the test;
- test passes on first run and is accepted as proof;
- RED fails for an unrelated setup error;
- test duplicates implementation logic;
- private internals become the stable test contract;
- every dependency mocked;
- huge end-to-end test used when a focused public seam would prove the behavior faster;
- test written after the fix but never shown to reproduce the regression;
- refactor performed while tests are red;
- coverage target used as the primary definition of quality.

## Completion check

For each TDD behavior, confirm:

- the seam was intentionally chosen;
- the test was written before the production behavior;
- RED was observed for the expected reason;
- GREEN was observed after minimal implementation;
- refactoring retained green behavior;
- bug fixes keep a regression test;
- tests assert behavior rather than incidental implementation;
- final candidate verification still follows the canonical verification strategy.

## Provenance

Upstream mechanisms studied:

- addyosmani/agent-skills — `skills/test-driven-development/SKILL.md` — `test-driven-development` — MIT
- mattpocock/skills — `skills/engineering/tdd/SKILL.md` — `tdd` — MIT
- obra/superpowers — `skills/test-driven-development/SKILL.md` — `test-driven-development` — MIT

This is an Anthracite-specific rewrite. Framework examples, harness-specific invocation, and absolute test-layout assumptions are intentionally not inherited.
