# CLAUDE.md: {{PROJECT_NAME}}

<!-- This is the one file the agent reads on every turn. It defines how the agent should
     ACT: behavior, permissions, and pointers to the docs that carry the detail. Keep it
     lean. Every line here competes for the model's attention on every single request, so
     a line that changes nothing about the output doesn't belong here. Save it at the repo
     root under the name your agent reads: CLAUDE.md in Claude Code, AGENTS.md in Codex and
     Cursor. If the repo already has one of those two names, that is the name. Only when you
     cannot tell, keep this as CLAUDE.md and leave a one-line AGENTS.md pointing at it, rather
     than two full files to keep in sync. Delete these comments as you fill it in. -->

{{One or two sentences: what this project is. The full what/why lives in docs/OVERVIEW.md. This file is how you, the agent, should work inside this project.}}

## How to work here

<!-- fill: this project's own loop, not generic hygiene. A line that would read the same in
     any repo earns nothing here. -->

- Before finishing: {{the exact commands that must be green, e.g. `npm test`, `npm run build`, `npm run sim`}}.
- {{A working rule specific to this codebase, e.g. "a new flow step ships with its sim scenario in the same change".}}
- {{At most two more. Delete the rest.}}

## Behavior rules

<!-- fill: 5-10 rules specific to THIS project. Each earns its place. Rules a linter can
     enforce belong in the linter, not here. -->

- {{A language or typing rule, e.g. "TypeScript everywhere; never generate a .js file in src/".}}
- {{An export/import or module rule.}}
- One feature at a time. Don't bundle a refactor, a fix, and a new feature into one pass.
- Match the existing pattern before inventing a new one.

## Permissions

<!-- fill: three tiers. Be explicit; the agent can't read your comfort level. -->

- **Run freely:** {{dev server, linter, formatter, test runner, reading any file}}.
- **Ask first:** {{new dependencies, schema changes, deleting files, rewriting git history}}.
- **Never:** {{commit secrets, push to main, run a destructive database command}}.

## Keep the docs current

The docs in `docs/` are the project's memory. When a change alters documented behavior, update the doc **in the same task** as the code, not later. A stale doc lies with authority. Before finishing, check whether any doc is now out of date, and update `docs/context/` if the state moved (a lean run writes only `log.md` there).

## Project context

Before you work, read the doc that owns the kind of work you're doing. A doc you don't load has zero effect.

<!-- Lean mode writes OVERVIEW, ARCHITECTURE, CONVENTIONS and context/log.md. Delete the
     lines below for the docs this run did not write: a pointer to a file that isn't there
     costs the agent a lookup and teaches it the wiring lies. -->

- `docs/OVERVIEW.md`: what this is and who it's for. The source of truth for intent.
- `docs/ARCHITECTURE.md`: how it's built and where files go. Read before creating a file.
- `docs/TECH_STACK.md`: the chosen tools and why. Read before adding or swapping a dependency.
- `docs/CONVENTIONS.md`: code style and patterns. Read before writing code.
- `docs/DESIGN.md`: visual language. Read before any UI work.
- `docs/HANDOFFS.md`: how work is split across agents and handed off.
- `docs/context/CONTINUE_PROMPT.md`: where the project stands right now. Read at the start of a session.
- `docs/context/log.md`: decisions and gotchas. Check it when something surprises you; add to it when you learn something the hard way.

For how the docs folder itself works, see `docs/README.md`; for the reasoning behind this whole layer, `docs/why_this_works.md`. Those two are about the system, not this project, so you don't read them per task.
