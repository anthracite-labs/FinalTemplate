Work from the connected GitHub repository for this project.

The repository is the canonical source of project continuity. Prior chats, summaries, and memory may help with context, but they must not silently override current repository state.

At the start of each new substantive project chat:

1. Read `.project-ai/PROJECT_STATE.md` from the current `main` branch.
2. Recover the current accepted project position from the repository rather than assuming prior chat context is current.
3. Load only the additional control-plane files relevant to the present task:
   - `.project-ai/routing/capabilities.md` when classifying the kind of work.
   - `.project-ai/routing/route.md` when deciding where or how an operation should execute.
   - `.project-ai/execution/arena-dispatch.md` when preparing, reviewing, correcting, accepting, or closing Arena work.
   - `.project-ai/execution/verification.md` when verification strategy or execution evidence matters.
   - `.project-ai/bootstrap/project.md` only for project bootstrap or reconciliation.
   - relevant `.project-ai/skills/*/SKILL.md` only when a skill actually applies.
4. Read actual project artifacts whenever they own the fact in question. Do not maintain an AI-side mirror of stack, commands, architecture, dependencies, or other project facts.
5. When repository sources conflict, prefer the canonical owner of the fact and repair stale projections such as `PROJECT_STATE.md` rather than treating the projection as superior.
6. Do not promote brainstorming, transient failures, workflow status, or implementation activity into durable project state.
7. Persist a decision only after it is accepted and only in its proper owning artifact.
8. Use GitHub Issues and pull requests for active work. Do not create a parallel task database under `.project-ai/`.

Operating boundary:

- Normal ChatGPT changes the control plane and prepares/reviews execution contracts.
- Arena changes the product inside an approved contract.
- Human acceptance authorizes merge.
