---
name: security-engineering
description: Apply risk-triggered security design, hardening, review, and audit. Model trust boundaries and abuse cases early, trace real attacker-controlled paths before reporting vulnerabilities, and scale audit depth to the project's actual risk surface.
---

# Security Engineering

## Purpose

Security is a cross-cutting engineering concern, not a final checklist.

Use this skill to identify and control material security risk from architecture through implementation, review, release, and incident handling.

Security depth follows risk. Low-risk work should not inherit heavyweight ceremony. High-risk work must not be waved through with generic best-practice language.

## Trigger conditions

Invoke this skill when work materially involves any of:

- authentication or authorization;
- secrets, credentials, tokens, or key material;
- cryptography;
- untrusted input;
- uploads, parsers, document processing, or deserialization;
- network trust boundaries;
- webhooks, callbacks, or external-service responses;
- privileged operations or permissions;
- multi-tenancy;
- payments or money movement;
- personal, regulated, or otherwise sensitive data;
- dependency or supply-chain risk;
- privileged CI/CD behavior;
- code generation or execution from untrusted material;
- LLM or agent output used to drive tools, code, queries, files, or other effects.

Also invoke it when explicitly asked for a security review or audit.

## Operating modes

Choose the lightest mode that can safely answer the question.

### Design mode

Use during requirements or architecture.

Goal: identify assets, principals, trust boundaries, abuse cases, and required controls before implementation hardens the wrong design.

### Hardening mode

Use during implementation.

Goal: implement secure defaults and project-appropriate controls at actual boundaries.

### Review mode

Use on a specific change.

Goal: find high-confidence exploitable problems by tracing real data and authorization flows, not by pattern matching.

### Audit mode

Use only when explicitly requested or when the risk surface justifies a deeper review.

Goal: systematically inspect the relevant system for concrete trust-boundary violations, safe reproduction, impact, and smallest effective fixes.

Do not run full-audit ceremony on unrelated low-risk changes.

## Workflow

### 1. Establish security scope

State what is being secured and which security outcome matters.

Identify relevant:

- principals;
- assets;
- resources;
- trust boundaries;
- attacker capabilities;
- sensitive operations;
- externally controlled inputs;
- privileged outputs or effects.

Do not assume every boundary is HTTP or browser-based.

### 2. Model abuse cases

For each material use case, ask how it could be misused.

Consider as applicable:

- impersonation;
- authorization bypass;
- tampering;
- information disclosure;
- replay or duplicate effects;
- denial of service;
- privilege escalation;
- cross-tenant access;
- unsafe file or path handling;
- injection into interpreters, queries, templates, shells, or tool calls;
- supply-chain compromise.

Use threat-model frameworks such as STRIDE only when they help. The framework is a lens, not a required artifact.

### 3. Define controls at real boundaries

Prefer controls placed where trust changes.

Examples:

- authenticate principals at the appropriate boundary;
- authorize the specific action on the specific resource;
- validate externally controlled data before trusted use;
- parameterize interpreters and queries;
- encode or sanitize output in the context where it is rendered;
- minimize privileges;
- isolate secrets from source and logs;
- constrain externally triggered side effects;
- cap size, rate, time, concurrency, or recursion where abuse could exhaust resources;
- verify signatures or provenance where trust depends on them.

Do not duplicate validation mechanically inside already trusted internal paths.

### 4. Treat external and generated data as untrusted

Third-party APIs, queues, files, model output, job payloads, environment supplied by less-trusted actors, and other external material can be attacker-controlled even when they arrive through an internal-looking channel.

Trust follows who can influence a value, not the transport that delivered it.

### 5. Review authentication and authorization separately

Authentication answers who the principal is.

Authorization answers whether that principal may perform this action on this resource.

Do not treat successful authentication as authorization.

For multi-tenant systems, explicitly verify tenant isolation at data and action boundaries.

### 6. Handle secrets and sensitive data deliberately

As applicable:

- keep secrets out of source and logs;
- minimize collection of sensitive data;
- classify sensitive fields;
- define retention and deletion behavior where required;
- restrict access to least privilege;
- avoid copying sensitive data into telemetry or debugging artifacts;
- account for caches, backups, indexes, analytics, and downstream processors when deletion or residency matters.

A secret exposed to a remote system or public history should be treated as compromised according to the project's incident procedure.

### 7. Consider dependencies and supply chain

For new or materially changed dependencies:

- identify the owning package manager and lockfile;
- inspect provenance and maintenance signals;
- understand install/build scripts and privileged hooks;
- review relevant advisories;
- assess reachability before escalating advisory severity;
- avoid forced broad upgrades without compatibility review;
- preserve reproducible dependency state.

Do not equate "audit tool is green" with "dependency is safe".

### 8. Review by tracing data flow

When reviewing code, investigate before reporting.

For each candidate finding, establish:

- where the input or action originates;
- whether an attacker can control it;
- validation, authorization, sanitization, or framework protections already present;
- configuration that changes exploitability;
- whether the vulnerable path is reachable;
- the affected principal or resource;
- the concrete security consequence.

Do not report a vulnerability based only on a suspicious-looking API call.

### 9. Grade confidence separately from impact

A high-impact theory with weak exploit evidence is not a high-confidence finding.

Classify findings as:

- **CONFIRMED** — concrete vulnerable path and attacker control are established;
- **NEEDS VERIFICATION** — plausible material risk but one or more exploit conditions remain unproven;
- **DEFENSE IN DEPTH** — improvement with no demonstrated exploit path.

Do not inflate defense-in-depth advice into vulnerability findings.

### 10. Deep-audit a real trust-boundary violation

For full audit mode, each material finding should identify:

- attacker capability;
- attacker-controlled input or action;
- crossed trust boundary;
- affected principal/resource;
- security outcome;
- safe reproduction or evidence;
- severity rationale;
- smallest effective fix;
- verification for the fix.

Avoid unsafe reproduction that could damage data, systems, or users.

### 11. Re-verify after correction

Security fixes require targeted verification of the original exploit condition and relevant regression coverage.

Use the canonical verification strategy in `../../execution/verification.md`.

## Output contract

### Security Scope

What was assessed and why security depth was triggered.

### Assets / Principals / Trust Boundaries

Only the material ones.

### Abuse Cases

Relevant misuse paths and required controls.

### Required Controls

Controls that architecture or implementation must preserve.

### Findings

For each finding:

- status: CONFIRMED / NEEDS VERIFICATION / DEFENSE IN DEPTH;
- affected path or surface;
- attacker preconditions;
- evidence;
- impact;
- smallest effective fix;
- verification requirement.

### Residual Risk

Known risk that remains accepted, deferred, or outside scope.

### Escalation

Material security decisions that require control-plane or human approval.

## Interaction with other lifecycle skills

- requirements specification captures security requirements that are part of product behavior;
- architecture-interface-design establishes trust and ownership boundaries;
- project-bootstrap establishes project-specific security foundations when needed;
- ci-cd-automation protects privileged automation and supply chain;
- code-review may invoke security review for changed risk surfaces;
- incident-response handles active security incidents;
- maintenance-migration-retirement removes obsolete vulnerable surfaces and dependencies.

Security does not become a seventh top-level capability. It operates within understand, decide, plan, implement, review, and diagnose.

## Red flags

- "security later";
- generic OWASP checklist with no project threat model;
- authentication without resource-level authorization;
- trusting third-party or model output because it came through an internal service;
- vulnerability claims based only on pattern matching;
- reporting theoretical issues as confirmed exploits;
- logging secrets or sensitive payloads for debugging;
- forced dependency remediation without compatibility analysis;
- full penetration-test ceremony for low-risk documentation or mechanical changes;
- suppressing a material security concern to preserve delivery scope.

## Completion check

Before handoff, confirm:

- security depth matches the risk surface;
- material trust boundaries and assets are known;
- abuse cases were considered where relevant;
- required controls are tied to real boundaries;
- review findings trace attacker control to concrete impact;
- uncertainty is not reported as confirmed vulnerability;
- residual risk is explicit;
- security fixes have targeted verification requirements.

## Provenance

Upstream mechanisms studied:

- addyosmani/agent-skills — `skills/security-and-hardening/SKILL.md` — `security-and-hardening` — MIT
- getsentry/skills — `skills/security-review/SKILL.md` — `security-review` — Apache-2.0
- cloudflare/security-audit-skill — `skills/security-audit/SKILL.md` — `security-audit` — MIT

This is an Anthracite-specific rewrite. Upstream web-framework defaults, tool lists, reference layouts, report formats, and audit orchestration are intentionally not inherited.
