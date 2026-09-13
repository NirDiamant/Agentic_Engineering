# HANDOFFS: {{PROJECT_NAME}}

<!-- fill: how agents work together in this project: roles, handoffs, and where each
     kind of work finds its context. This file is a MAP, not a second rulebook. The
     rules live in CLAUDE.md and CONVENTIONS.md; this file points each kind of work at
     the context it needs. It is named HANDOFFS and not AGENTS on purpose: a root
     AGENTS.md is the cross-tool instruction file Codex and Cursor read (how the agent
     ACTS), and this file is how work is handed off. Delete these comments as you fill
     it in. -->

{{One short paragraph: how work is split in this project. Solo with one agent most of the time? Parallel agents on UI and data? A review pass before merges? Say what's true today, not what you imagine at scale.}}

## Agent roles

<!-- fill: one line per role. Each role names what it owns and what it reads first.
     Start with the roles you actually use; add more when you truly split work that way. -->

- **Builder**: the default. Writes features end to end. Reads `CONVENTIONS.md` and whichever doc owns the work at hand (see the table below).
- **Reviewer**: a read-only pass before merging. Reads everything, writes nothing except review notes. Never grades its own build (see why_this_works.md).
- **{{Another role, if you have one}}**: {{when it's used, what it owns, what it reads first}}.

## Handoffs

<!-- fill: the order of operations when work is split, and how one agent leaves the
     trail for the next. -->

- {{Which work lands first when two streams depend on each other.}}
- {{What a finishing agent writes down for the next one: one line of what changed and what's open.}}
- Anything one agent discovered the hard way goes into `context/log.md`, not a code comment the next agent won't see.

## Where context lives

| Kind of work | Read first |
|--------------|-----------|
| What and why | `OVERVIEW.md` |
| How it's built | `ARCHITECTURE.md` |
| Tech choices | `TECH_STACK.md` |
| Code style | `CONVENTIONS.md` |
| Anything visual | `DESIGN.md` |
| Current state | `context/CONTINUE_PROMPT.md` |
| Decisions and gotchas | `context/log.md` |

If a piece of work has no obvious owner above, it's a builder job and it reads `CONVENTIONS.md`.
