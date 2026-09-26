# Project Bootstrap and Reconciliation

Use this procedure when turning FinalTemplate into a real project or when reconciling an existing/partially established repository.

The procedure is project-neutral. It establishes decisions deliberately; it does not prescribe a language, framework, package manager, CI provider, test framework, database, deployment platform, security product, or release method.

## Principles

- The repository root belongs to the actual project.
- `.project-ai/` is the committed internal AI control plane.
- Existing valid project choices are preserved.
- Missing foundations are established deliberately.
- Inconsistencies are surfaced rather than silently normalized.
- Material changes to established choices require an explicit decision.
- Bootstrap produces the project itself, not a permanent bootstrap report.

## 1. Determine repository state

Classify relevant foundations as:

- **ESTABLISHED** — a valid project choice already exists;
- **MISSING** — the project needs a foundation that does not yet exist;
- **INCONSISTENT** — repository artifacts disagree materially;
- **NEEDS DECISION** — more than one valid direction exists and a human/project decision is required.

Do not reset an existing project toward the template.

## 2. Establish project identity

Determine as appropriate:

- project name;
- purpose;
- intended users/consumers;
- scope and non-goals;
- repository visibility;
- relationship to other repositories/services where relevant.

Replace the root `README.md` skeleton with the actual project's README.

The root README describes the project, not the internal AI control plane.

## 3. Licensing

Make an explicit project licensing decision.

“No root license yet” is a legitimate choice for a private or not-yet-distributed project.

Do not inherit a license merely because the repository came from a template.

## 4. Technology and repository structure

Establish only what the actual project needs, such as:

- language/runtime;
- framework;
- package/dependency manager;
- dependency-locking strategy;
- build system;
- source/test layout;
- database or persistence approach;
- generated artifacts/contracts.

Project facts remain canonical in actual project artifacts. Do not create a parallel `.project-ai` project profile.

## 5. Ignore rules

Create a root `.gitignore` only after the actual project produces artifacts that should be ignored.

Do not use a generic multi-language ignore file merely because the template could support many stacks.

`.project-ai/` is intentionally version-controlled.

## 6. Tests, formatting, and quality checks

Establish the project's actual:

- test strategy;
- test commands;
- formatter/linter;
- static analysis;
- build/compile checks;
- generated-state verification where required.

These project-owned commands are what `execution/verification.md` will rely on.

## 7. CI and repository automation

Add repository workflows only when the actual project requires them.

Do not add generic CI, Dependabot, CodeQL workflows, release automation, or provider configuration merely because they are common.

Where organization-level GitHub features already provide a genuine organization-wide policy, prefer the native organization feature instead of copying files into every repository.

When GitHub Actions are introduced, prefer:

- explicit least-privilege permissions;
- immutable action pins where practical/required by policy;
- read-only verification by default;
- write permission only for explicit mutation workflows;
- no unsafe execution of untrusted pull-request-controlled code under privileged events.

## 8. Security

Determine security requirements from the actual project's risk surface.

Increase security depth when the project involves areas such as:

- authentication/authorization;
- secrets/credentials;
- cryptography;
- untrusted input;
- uploads/parsers;
- network trust boundaries;
- permissions or multi-tenancy;
- payments or sensitive data;
- dependency/supply-chain risk;
- privileged CI/CD behavior.

Security depth follows risk, not ritual.

## 9. GitHub governance

Determine the repository governance the real project needs, including as appropriate:

- default branch;
- rulesets/branch protections;
- review requirements;
- required checks;
- merge methods;
- force-push/deletion policy;
- Actions permissions;
- secret scanning/push protection;
- security configuration.

Enforcement lives in GitHub settings. Do not maintain a shadow copy of every setting in `.project-ai/`.

## 10. Release and deployment

If the project ships or deploys, deliberately establish:

- release/versioning strategy;
- deployment target;
- artifact publishing;
- rollback expectations;
- environment/secrets handling.

Do not manufacture release infrastructure for projects that do not need it.

## 11. Durable project documentation

Create project/product/architecture documentation only when the real project needs it.

Durable technical decisions belong to the actual project.

Use ADRs only when preserving the rationale materially improves future engineering decisions. Do not create `.project-ai/DECISIONS.md`.

## 12. Initialize or reconcile project state

Update `.project-ai/PROJECT_STATE.md` to reflect accepted durable reality:

- phase;
- current objective;
- accepted decisions affecting active work;
- durable blockers;
- latest accepted milestone;
- next authorized action;
- authoritative references.

Do not record temporary setup activity, command logs, or chat history.

## Completion

Bootstrap/reconciliation is complete when the repository is a usable starting state for the actual project, its required foundations are either established or explicitly blocked on a decision, and `PROJECT_STATE.md` accurately reflects accepted durable reality.

Do not create a separate bootstrap report.
