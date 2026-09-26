# Capability Routing

Classify work by what kind of reasoning or activity is required. Capability routing is separate from execution routing.

Use only these initial capabilities:

## understand

Use when the primary need is to recover facts, inspect the project, investigate relevant context, or establish what currently exists.

## decide

Use when alternatives, trade-offs, constraints, or accepted direction must be resolved.

## plan

Use when an accepted direction must be converted into an executable work boundary, including an Arena Issue contract.

Plan only deeply enough to make execution safe and unambiguous. Do not pre-implement the solution in prose.

## implement

Use when approved product changes must be made.

Normal ChatGPT does not normally perform product implementation. Approved implementation is dispatched to Arena through the GitHub Issue contract defined in `../execution/arena-dispatch.md`.

## review

Use when examining an implementation, change, evidence set, security concern, or contract compliance.

## diagnose

Use when a failure, regression, unexpected result, or blocked operation requires root-cause investigation.

## Cross-cutting concerns

Testing, security, documentation, research, UI work, deployment, migrations, performance, and similar concerns are not additional top-level capabilities by default. They operate within the six capabilities above.

Create a new capability only when separating it materially changes routing, procedure, authority, permissions, or acceptance.

A missing tool, runtime, package manager, network route, or hosted runner does not change the capability. Those are execution-routing concerns.
