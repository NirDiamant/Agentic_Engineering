---
description: Take this docs template to the current repo. Research it (including what is actually wired), plan the docs layer, write it, self-check every claim against the code, then verify
---

Target repo: $ARGUMENTS (if empty, the current repo).

You are adapting a **docs template** to a real repository. The template ships generic files full of `{{placeholders}}`. Your job is to replace them with the truth of *this* project, so an AI coding agent that reads `docs/` and `CLAUDE.md` builds like it already knows the codebase.

Two rules above all others. You never pad a placeholder into something the human didn't say, and you never present your own guess as their decision. And **every claim you write is scoped to code that actually runs**: a doc that describes dead code as the live path, or states a rule the code breaks, is worse than no doc, because the agent trusts it. Where you don't know, write `<!-- unconfirmed: the open question -->`.

**Budget.** Read the manifests, config, entry points and at most about 30 source files chosen across areas; write about nine files; one self-check pass; one fresh-evaluator round where your agent can spawn one. Measured on real repos: 20 to 45 minutes with two evaluator rounds, and the evaluators were more than half of it, so expect 15 to 30 with one. Do not read every file in a large repo; sample by area and say so.

Work in four phases. Do not skip to writing.

## Phase 1: Research

Read before you propose. Gather the truth the docs must reflect:

- **The lockfile and manifests** (`package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`, …). The real stack, not the assumed one. Note both the declared range and the locked version of anything you will name.
- **The entry points, then what they reach.** Find how the project is started and run: the manifest's scripts and `bin`, the server or `main` module, the CLI, the test runner, CI. Trace imports from each entry point, then reverse it: list every module and count its importers, because forward tracing can never prove a module unreached. Zero importers means **unwired only when nothing else reaches it by name**: a runner glob, file-system routing (Next.js `page`/`route`, serverless folders), a manifest or CI script, a bundler or `tsconfig` entry, an HTML `src`. Check those first, because a live endpoint written up as dead code is the worst doc in the layer. What survives the check is the unwired list. You will describe unwired code as unwired, or not at all. Never as "the path".
- **Real code.** Open a handful of representative files per area. What pattern repeats? What's the naming? How are modules shaped? When you think you have found a universal rule, look for the file that breaks it before you write it down.
- **Config.** Linter, formatter, CI, test setup. A rule a gate actually runs belongs to the gate, not the docs. A rule only configured, with nothing invoking it, is not enforced: it belongs in the docs, and say that nothing runs it. A linter config nothing invokes, or a `tests/` folder that does not exist, enforces nothing.
- **The gates.** If dependencies are installed, run the test, type-check and lint commands the manifest defines, and record the real result. If you cannot run them, say so in `CONTINUE_PROMPT.md` and never copy a count from prose as if you had verified it.
- **Existing context files.** A `CLAUDE.md`, `AGENTS.md`, `.cursor/rules`, `.cursorrules`, `.windsurfrules`, `.github/copilot-instructions.md`, a `README`, a wiki or journal, any `docs/`. These are **input, never something to silently overwrite.** Read them first; they carry the intent the code cannot. If the human moved their `CLAUDE.md` aside, read the copy.
- **Gotchas.** Every fact you verify that is not obvious from the code (a pinned version and why, a config section nothing reads, a route that behaves oddly) goes on a dated list. It seeds `docs/context/log.md`; the template's "leave the log almost empty" applies to invented content, not to what research proved.

If the repo is **empty** (an idea, not a codebase yet), you can't research code. Switch to a short interview: ask, in two small batches, what it is and who it's for, the MVP outcomes, the non-features, the stack (or "propose one"), and how the human wants to work with the agent. Then continue to Phase 2 with their answers as your source.

## Phase 2: Plan

1. **Play back what you found**, in a few lines, and let the human correct it. ("Stack looks like X on Y; entry points are A and B; code is organized as Z; the pattern I see is W; these modules are unwired.") This catches a wrong read before it becomes eight wrong files.
2. **Ask only what code can't answer**, the intent questions. Keep it to about five: the one-sentence pitch, who it's for, the non-features, any stack choice whose *reason* isn't obvious, and the permission tiers (what the agent may run freely / must ask about / must never do).
3. **Decide what exists already.** If the human has a journal, runbook or instruction file, say what stays where: the new `CLAUDE.md` is the always-loaded file and wins; `docs/` holds the durable picture; the human's journal stays as history and `docs/context/` is compressed from it; the README stays the human runbook. State that precedence in one line at the top of `CLAUDE.md`. Keep every rule of theirs that passes the delete test (remove it: does the agent do something different or worse?), move misplaced content to the wall that owns it, and show the human a summary of what you kept, moved and cut before finalizing.
4. **State the plan**: which docs you'll write, which you'll skip, and where anything's still unknown. `DESIGN.md` only if the project has a user-facing UI (screens, components, pages a user sees); operator pages or a rendered artifact do not qualify unless the human says so. Get one approval before writing.

## Phase 3: Execute

Write the layer, derived from the repo, not invented:

- `CLAUDE.md` at the repo **root**. Lean rules, the permission tiers, and the wiring block that points into `docs/`. Its **"How to work here" section is the project's own loop, not generic hygiene**: the exact commands that must be green before finishing, and up to three working rules specific to this codebase. Delete the template's generic lines; lines that would read the same in any repo earn nothing here.
- `docs/OVERVIEW.md`: what and why. The test is **no implementation technology**: no framework, library, database, language or host; move those to `TECH_STACK.md`. Carve-out: a platform that IS the product, not a way to build it (a WhatsApp bot, a browser extension), is named.
- `docs/ARCHITECTURE.md`, `docs/TECH_STACK.md`, `docs/CONVENTIONS.md`: filled from the real code and config. Unwired code is named as unwired, in one place, with the open question of what to do with it.
- `docs/DESIGN.md`: only if the plan kept it. If the plan skipped it, delete the template copy under `docs/` and drop its line from the wiring block: a placeholder left behind is a false doc. (This is the one file the procedure may delete; it is the kit's own template, not the human's.)
- `docs/HANDOFFS.md`: how work splits and is handed off; keep it a map, not a second rulebook. (It is not the root `AGENTS.md` some tools read: that name is the instruction file itself.) Describe roles that exist; don't invent a review process the repo has no trace of.
- `docs/context/CONTINUE_PROMPT.md` and `docs/context/log.md`: seed the anchor with current state and the real gate results (or "not run, because"); seed the log with the dated gotchas research verified, each citing its file.

Rules of evidence while writing:
- Every claim names the file it comes from, or you don't make it. The one exception is `OVERVIEW.md`, which names no files and no technology: its claims come from the human, the README, or the manifests' own descriptions, and one line at its end says which.
- A rule stated as universal has been checked against the code. If the code has exceptions, either name them ("known exceptions, do not extend: A, B") or scope the rule to new code. A flat "never" the code already breaks is a false doc.
- A version is the declared range **and** the locked version, or neither.
- A command you list exists in the manifest under that exact name, and its description matches what it runs.
- State a count only when it changes what the agent does: a cap, a limit, the number of places that must agree. Any count you state was made in this run, on this tree. Do not count things for their own sake (style violations, line lengths, leftover characters); those become findings nobody acts on.
- Replace every `{{placeholder}}`. Where you genuinely don't know, write `<!-- unconfirmed: the open question -->`.
- Keep `CLAUDE.md` lean. If it passes ~100 lines, you're restating things that belong in a `docs/` file or in the linter. Don't restate a rule the tooling already enforces, and don't restate a `docs/` section; point at it.
- No em dashes anywhere in a file you hand over, template headings and bullets included, not just prose you composed. Commas, colons or parentheses.

## Phase 4: Verify

**4a. Self-check, always, in every agent.** You wrote it, so you don't get to say it's done, but you do get to check it. Go through every doc claim by claim against the source, with this list, and fix what fails:

1. Every described path, module, component and route is reached from an entry point or by name, or is labelled unwired.
2. Every universal rule survived a search for the file that breaks it, or names its exceptions.
3. Every version matches the lockfile; every command matches the manifest; every path exists.
4. Every count was made on this tree.
5. `OVERVIEW.md` names no implementation technology, only a platform that is the product itself.
6. The wiring block in `CLAUDE.md` and the files on disk match exactly: every project-context doc that exists is referenced, every reference points to a doc that exists.
7. No `{{placeholder}}` survives; no em dash survives; `CLAUDE.md` has no generic hygiene line; `DESIGN.md` exists only if the plan kept it; `log.md` carries the research gotchas.
8. No doc contradicts another or the code.

**4b. Fresh evaluator, where your agent can spawn one.** Launch **one fresh evaluator sub-agent** (its own context, a harsh prompt). Hand it only the repo and the eight criteria above as the definition of done. Tell it to read the written docs, spot-check each claim against the actual files, and report issues (not causes): pass/fail per criterion with the exact file and line, and to rank them: a finding that would change what an agent builds first, a precision slip last. Do **not** give it your reasoning. Re-read each finding against the file before you act on it, fix what is real, and list every fix in your report as **unverified by an evaluator**. One evaluator is the cap; a second costs as much as the first and, measured, finds precision slips.

If your agent cannot spawn a sub-agent, say so in the report; the self-check is then the verification, and the report says which claims were checked by you alone.

## Report

Finish with a short report: what you wrote (files and line counts); what you kept, moved and cut from the human's existing files; the gate results or why they were not run; what the evaluator caught and which fixes are unverified; every `<!-- unconfirmed -->` marker still waiting on the human; and the list of unwired code with the open question it raises.
