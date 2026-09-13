# ARCHITECTURE: {{PROJECT_NAME}}

<!-- fill: how the project is put together and where things live, so the AI puts a new
     file in the right place instead of guessing, and reasons about the system instead
     of rediscovering it. A small project gets a small architecture. This grows only
     when it has to. Delete these comments as you fill it in. -->

How {{PROJECT_NAME}} is put together: the pieces, how they connect, and where things live.

## Components

<!-- fill: the main parts and what each owns. One line each. A reader should be able to
     name the moving parts after this section. -->

- **{{Component}}**: {{what it owns}}.
- **{{Component}}**: {{what it owns}}.

## Data flow

<!-- fill: how a request or an action moves through the system, start to finish.
     Keep it to the real path, not an idealized one. -->

{{Trace one representative action: what enters, what touches it, what comes out.}}

## Boundaries

<!-- fill: the lines that must not be crossed. What layer may call what. Where trust
     starts and stops. -->

- {{What talks to what, and what must never call across a boundary directly.}}

## Layout

<!-- fill: the top-level tree with one comment per folder. Only the folders that exist today. -->

```
{{project-name}}/
├── {{src or app}}/          {{What lives here}}
├── {{...}}/                 {{...}}
├── docs/                    the context layer (see docs/README.md)
└── CLAUDE.md                agent rules + wiring (repo root)
```

## What goes where

<!-- fill: one rule per kind of file. Phrase it as "a NEW X goes to Y", because that's
     the exact moment the model needs it. -->

- **{{A screen / a page}}** → {{where, and the naming pattern}}.
- **{{A reusable component}}** → {{where, and when something graduates to shared}}.
- **{{Backend logic}}** → {{where}}.
- **{{A helper that's neither UI nor data}}** → {{where}}.

If a new file has no obvious home here, the architecture is missing a place. Say so, and add one on purpose rather than dropping the file wherever.
