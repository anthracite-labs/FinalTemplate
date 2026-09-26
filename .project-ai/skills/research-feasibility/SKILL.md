---
name: research-feasibility
description: Research material unknowns and assess whether a proposed project, feature, or technical direction is feasible. Ground external claims in current authoritative evidence, project claims in canonical project artifacts, expose uncertainty, compare alternatives, and produce an explicit viability outcome.
---

# Research and Feasibility

## Purpose

Use this skill when a decision should rest on evidence rather than assumption.

Research exists to support a decision. Feasibility determines whether the proposed direction can reasonably proceed under the project's technical, resource, economic, and operational constraints.

This skill does not own requirements, architecture, planning, or implementation.

## Use when

Use this skill when the work depends materially on unknowns such as:

- current technology or API behavior;
- market, domain, competitor, user, regulatory, or standards information;
- whether an external service or library can support a required capability;
- existing solutions or prior art;
- technical viability;
- significant cost, licensing, infrastructure, or vendor implications;
- operational burden or required expertise;
- risky assumptions that could invalidate the project or feature.

Do not run broad research merely because research is possible. Start from the decision that needs evidence.

## Evidence ownership

Use the source that owns the claim.

### External-world claims

Prefer current authoritative sources such as:

- official documentation;
- specifications and standards;
- primary research;
- source code;
- first-party APIs and datasets;
- regulator or government sources;
- vendor or project documentation.

Secondary sources may be useful for discovery, interpretation, community experience, or when no primary source exists, but do not casually substitute them for the authority that owns the fact.

### Project-state claims

Use canonical project evidence such as:

- source code;
- manifests and lockfiles;
- configuration;
- tests;
- CI workflows;
- deployment configuration;
- project-owned documentation;
- production telemetry;
- accepted project decisions.

Project assumptions may shape what to investigate. They do not prove external facts.

External sources may explain a technology. They do not override what this project actually contains.

## Core epistemic rules

1. Material conclusions require evidence gathered or supplied for this decision.
2. Model memory may suggest hypotheses and queries, but is not sufficient evidence for current external facts.
3. Every load-bearing factual claim should be traceable to a source or canonical project artifact.
4. Freshness is part of truth when the subject can change.
5. Conflicting evidence must be surfaced, not averaged away.
6. Thin evidence is reported as thin.
7. Absence of evidence can itself be a finding.
8. Do not create false precision from weak inputs.

## Workflow

### 1. State the decision

Write the exact decision the research must support.

Examples:

- whether to use a particular library;
- whether a proposed product direction is viable;
- whether an integration can meet the required contract;
- whether to build, adopt, extend, or defer.

A vague topic is not enough.

### 2. Identify decision-critical unknowns

List only the unknowns that could materially change the decision.

Classify them when useful as:

- technical;
- domain;
- market;
- competitive;
- user evidence;
- standards or regulatory;
- operational;
- cost or resource;
- comparative selection.

Avoid researching dimensions that cannot affect the decision.

### 3. Plan the evidence

For each material unknown, identify:

- the best source class;
- freshness requirements;
- whether one source is enough or corroboration is warranted;
- what would count as evidence against the current hypothesis.

For high-risk decisions, seek disconfirming evidence deliberately.

### 4. Gather and trace evidence

Retrieve or inspect the relevant sources.

Prefer primary or owning sources. Follow secondary claims back to the original where practical.

Keep the working context lean: extract decision-relevant findings rather than ingesting large source sets wholesale.

For each load-bearing finding, retain enough provenance to recover the source.

### 5. Synthesize without overclaiming

Separate:

- supported findings;
- conflicting evidence;
- uncertainty;
- evidence gaps;
- alternatives;
- assumptions that still require validation.

Do not turn a lack of evidence into a positive conclusion.

### 6. Assess feasibility

Evaluate the proposed direction across the dimensions that matter.

#### Technical feasibility

Consider:

- compatibility with the current or proposed stack;
- integration constraints;
- architecture implications known at this stage;
- performance or scale constraints where material;
- data or migration complexity;
- security or compliance blockers;
- unknowns that require a spike, prototype, benchmark, or experiment.

#### Resource and economic feasibility

Consider when relevant:

- engineering effort at an appropriately coarse level;
- infrastructure cost;
- licensing or vendor cost;
- third-party service cost;
- opportunity cost;
- whether the expected value justifies the burden.

Do not invent detailed estimates without sufficient evidence.

#### Operational feasibility

Consider:

- deployment and support burden;
- required expertise;
- ongoing maintenance;
- monitoring and incident implications;
- team or organizational constraints;
- vendor or external-service dependence;
- lifecycle burden.

### 7. Promote risky assumptions

If the decision depends on an unverified assumption with meaningful downside, make it explicit.

Where practical, specify the cheapest useful validation method:

- targeted research;
- prototype;
- technical spike;
- benchmark;
- load test;
- contract test;
- user validation;
- vendor confirmation.

### 8. Decide

Use one of:

- **FEASIBLE** — evidence supports proceeding under known constraints;
- **FEASIBLE WITH CONDITIONS** — proceed only if stated conditions are satisfied;
- **NOT CURRENTLY FEASIBLE** — a material blocker or disproportional burden prevents proceeding now.

"Not currently feasible" is not necessarily permanent. State what would need to change.

## Output contract

Produce a concise decision-grade result:

### Decision Being Supported

The concrete choice this work informs.

### Key Findings

For each load-bearing finding:

- finding;
- source or canonical project evidence;
- date/freshness when relevant.

### Alternatives Considered

Viable alternatives and material trade-offs.

### Conflicting Evidence

Material disagreements between credible sources, if any.

### Uncertainty / Evidence Gaps

What remains unknown.

### Assumptions Requiring Validation

Risky assumptions and the preferred validation method.

### Feasibility

#### Technical

Verdict and reasons.

#### Resource / Economic

Verdict and reasons when material.

#### Operational

Verdict and reasons when material.

### Conditions

Requirements that must be satisfied before or during execution.

### Outcome

One of:

- FEASIBLE
- FEASIBLE WITH CONDITIONS
- NOT CURRENTLY FEASIBLE

## Persistence

Do not create a mandatory research workspace, digest directory, feasibility file, or background-agent artifact.

Persist research when:

- downstream decisions will need to cite it later;
- the evidence is expensive to recover;
- the decision is durable or high stakes;
- the project already has a canonical research/RFC/ADR system.

Use existing project conventions when they exist.

## Handoff

Feed only decision-relevant findings, conditions, constraints, and unresolved assumptions into requirements specification.

Do not pass a raw source dump downstream.

If feasibility depends on a technical spike, the spike should answer the specific unknown and then return here or to the controlling decision before requirements are finalized.

## Red flags

- researching a topic without stating the decision;
- relying on training memory for current external facts;
- citing secondary summaries when the primary source is readily available;
- treating project assumptions as external evidence;
- treating external docs as proof of project state;
- collecting links without synthesizing what they change;
- hiding conflicting evidence;
- inventing precise cost or schedule estimates;
- producing a go decision despite an unresolved material blocker;
- mandatory research files that duplicate canonical project truth.

## Completion check

Before handoff, confirm:

- the decision is explicit;
- material unknowns were investigated rather than broad background gathered;
- load-bearing external claims trace to authoritative evidence;
- project-state claims trace to canonical project artifacts;
- uncertainty and conflicting evidence are visible;
- technical feasibility was assessed;
- resource/economic and operational feasibility were assessed where material;
- risky assumptions have a validation path;
- the outcome and any conditions are explicit.

## Provenance

Upstream mechanisms studied:

- bmad-code-org/BMAD-METHOD — `skills/bmad-deep-recon/SKILL.md` — `bmad-deep-recon`
- mattpocock/skills — `skills/engineering/research/SKILL.md` — `research`
- tomzx/agents — `skills/create-feasibility/SKILL.md` — `create-feasibility`

These repositories were MIT-licensed when this skill was authored.

This is an Anthracite-specific rewrite. Upstream workspace, script, memlog, background-agent, issue-mutation, and artifact-storage conventions are intentionally not inherited.
