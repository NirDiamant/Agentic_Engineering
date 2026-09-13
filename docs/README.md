# docs/: how this folder works

This is the project's **context layer**: the files an AI coding agent reads before it writes code. The agent starts every session with no memory of this project. These files are that memory, in writing, so the agent builds like it already knows the codebase.

Think of it as the briefing a new teammate reads on day one. Not every doc, every time: the right doc for the work in front of them.

## The structure

Long-lived docs live at the top of `docs/`. Working docs live in subfolders. Before adding a new top-level folder, check whether one of these already fits. If this project already has its own convention, a `todos/` folder for instance, that convention wins: match the repo, not this table.

| Path | What lives here |
|------|-----------------|
| `docs/` | Long-lived docs, the stable picture of the project. `OVERVIEW.md`, `ARCHITECTURE.md` and `CONVENTIONS.md` are written by every run; `TECH_STACK.md`, `HANDOFFS.md` and `DESIGN.md` (UI projects only) are written by `/apply-airtight`. |
| `docs/context/` | The captain's log. `log.md` (decisions, gotchas, and contradictions found in the existing docs) is written by every run; `CONTINUE_PROMPT.md` (where we are, what's next) by `/apply-airtight`. Short entries, skimmable in 30 seconds. |
| `docs/plans/` | PRDs, implementation plans, migration strategies. One file per plan. |
| `docs/research/` | Research outputs and findings. One file per investigation. |
| `docs/changelog/` | Notable changes and decisions worth a permanent record. Reverse-chronological. |

A lean `/apply` run writes four files and deletes the templates for the rest, so a name above that is not in this repo is one that run skipped. That keeps this index true after either run, with nothing to edit.

`CLAUDE.md` stays at the **repo root**, not here. It's the one file the agent loads on every turn, and it points into this folder (its "Project context" block is the wiring). A doc nothing points to is a doc the model never reads. If your tool reads `AGENTS.md` instead, that root file is the same thing under another name, and it is not `docs/HANDOFFS.md`, which is the map of how work is handed off between agents.

## Create late, not upfront

Don't scaffold empty folders. `docs/plans/`, `docs/research/`, and `docs/changelog/` come into being the first time you have a real plan, a real finding, or a change worth recording. An empty `docs/context/` skeleton helps no one.

The long-lived docs are the exception: `/apply` writes them once, from your actual codebase, because they're the briefing.

## Keeping docs current

- When a change alters documented behavior, update the doc **in the same task** as the code, not as a follow-up. A stale doc is worse than a missing one: it lies with authority.
- Before finishing a task, check whether any doc, plan, or note is now out of date.
- Summarize, don't archive. When `context/` grows, compress it down rather than adding more files. Brief narrative, not raw history.

## The build cycle

For anything non-trivial, work in this order: **Absorb → Discuss → Align → Document → Build.**

1. **Absorb**: read the relevant docs and code before proposing anything.
2. **Discuss**: surface questions, tradeoffs, and choices as a back-and-forth.
3. **Align**: converge on scope, contracts, and boundaries. What it does and does *not* do.
4. **Document**: write the decisions down (here) before writing the implementation.
5. **Build**: now write the code, informed by the four steps above.

If you're unsure mid-build, steps 2-3 were incomplete. Stop, resolve it, update the doc, continue. The builder should never be more than one step ahead of the documented decision.

## Suggested docs, and when to add them

Add these when the trigger fires, not before:

| Doc | Add it when |
|-----|-------------|
| `TERMINOLOGY.md` | You've had to define the same project-specific term twice. |
| `SETUP.md` | First-time setup took more than three non-obvious steps. |
| `DEPLOYMENT.md` | Deploy steps came up but aren't written down. |
| `CI_CD.md` | You have an automated pipeline and want its policy (gates, stages, triggers) written down. |
| `TESTING.md` | The project has a test bar worth stating: what to test, the layers, the runner. |
| `API.md` | The project exposes endpoints or contracts to other systems. |
| `TODO.md` | More than two future items surfaced and nothing tracks them. |
