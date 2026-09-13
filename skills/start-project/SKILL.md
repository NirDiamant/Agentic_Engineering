---
name: start-project
description: The technical on-ramp to a fresh project. Where /spark draws out the ESSENCE and refuses to talk tech, start-project does the opposite. It surveys the technical infrastructure up front (existing setup, language, database, cloud/hosting, CI/CD, deployment, testing, package manager), turns the answers into the docs layer (CLAUDE.md + docs/) plus an ordered setup plan (docs/SETUP.md) and guideline docs for deployment, CI/CD, and testing (docs/DEPLOYMENT.md, docs/CI_CD.md, docs/TESTING.md), then verifies the result with a fresh evaluator. Supports "pointing" (aim it at an existing project on disk and it copies/adapts that project's stack, CI, and conventions) and ships a neutral skeleton (skills/start-project/example/) it falls back to when you have no project to point at. Trigger on "/start-project", "set up the docs and infrastructure", "scaffold the project", "start a project with this stack", "copy the setup from <project>", "I know my stack, lay it down".
metadata:
  author: roihala
  version: '0.1.0'
  tags: greenfield, on-ramp, infrastructure, survey, docs, scaffolding, pointing
---

# Start Project (stack + infra → docs, guided)

The repo has two front doors already. `/spark` starts from an idea in your head and deliberately refuses to talk tech. `/apply` starts from a codebase that already exists and documents it from the truth of the code. **Start-project is the third door: you're starting fresh, but you already have technical decisions to make** (a database, a cloud, a CI/CD stance, a testing approach). This is the mirror image of `/spark`: it puts the *technical infrastructure* front and center, surveys it deliberately, and lays down the docs and a setup plan so the build starts on solid ground.

You own the survey and the write. You do **not** write application code or provision live infrastructure: you capture the decisions, fill the docs, and produce an ordered setup checklist for the builder (human or agent) to execute.

## The one rule

**Capture decisions and reasons, not guesses.** Every stack line needs the reason behind it, because a choice without a reason gets "helpfully" swapped the first time the model has a different idea (`docs/TECH_STACK.md` says this too). Where the human hasn't decided, do not invent a decision. Write `<!-- unconfirmed: the open question -->`. A doc that states a confident wrong stack is worse than one that admits the gap.

## Phase 1: Pick the source

Before surveying, ask how they want to supply the answers. Four modes:

- **Survey**: answer the infrastructure questions from scratch (Phase 2).
- **Point**: aim at an existing project (*"copy the setup from `~/projects/foo`"*). Read that project's manifests/lockfiles, CI config, test setup, Dockerfiles, and its own `docs/`/`CLAUDE.md` if present. Extract its stack, conventions, and infra decisions and reuse them as the answers, adapted to this project's name and intent, not copied blindly.
- **Hybrid**: point for the parts that carry over (stack, CI, conventions), survey only what's different (this project's purpose, its database, its non-features).
- **Example**: no project to point at? Start from the built-in skeleton at `skills/start-project/example/` (a neutral `SETUP.md`, `DEPLOYMENT.md`, `CI_CD.md`, `TESTING.md`, and a `ci.yml`, all `{{placeholder}}`). Copy its files into the target's `docs/` and `.github/`, then fill the placeholders from a light survey. This is the fallback so nobody starts from a blank page.

If they name a path, default to Point/Hybrid and skip every question the reference project already answers; only ask what it can't tell you. If they have neither a source nor firm answers, offer Example. Play back what you mined or seeded before treating it as settled.

## Phase 2: The infrastructure survey

Ask in **two small batches**. Wait for batch one before sending batch two. Never dump it all at once, and never answer for the human. Skip any question already answered by a pointed-at project.

**Batch one, the ground it stands on:**

1. Do you have any existing infrastructure to build on (a repo, a cluster, a database, an account), or is this truly from zero?
2. Language, framework, and package manager: the exact tools, or "propose one" if you want a recommendation with the tradeoff stated.
3. Data: what database (or none), and where does it live?
4. Cloud / hosting: where does this run? A platform (Vercel, Fly, a VPS), a cloud (GCP, AWS), or local-only for now?

**Batch two, how it's built, shipped, and kept honest:**

5. CI/CD pipeline: how far does automation go? Checks (lint + type-check + test) on push, a build step, all the way to a deploy on merge? Which host (GitHub Actions, etc.)?
6. Deployment: where does a release land and what triggers it? Merge to `main`, a version tag, a manual promote? This is set up as part of the process, not deferred, so name the target even if it's "a VPS via SSH" or "not yet, but here's where."
7. Testing: preferred runner and the bar (smoke, unit, integration); any coverage gate?
8. Intent, so `OVERVIEW.md` isn't hollow: one-sentence tech-free pitch, who it's for, the non-features (what it refuses to be), and any hard constraints (one package manager only, no new deps without a reason).

## Phase 3: Play back the decisions

Turn the answers into a short **decision sheet** and show it before writing anything:

- **Stack**: one line per layer (language, framework, database, hosting, package manager, auth), each with its reason.
- **CI/CD**: how far the pipeline goes (checks → build → deploy) and the host.
- **Deployment**: the target and what triggers a release.
- **Testing**: runner and the bar.
- **Intent**: pitch, who for, non-features (feeds `OVERVIEW.md`).
- **Unknowns**: anything still undecided, marked as such rather than filled with a guess.

Get one "yes, that's it" before you write. A wrong read here becomes a stack of wrong docs.

## Phase 4: Write the docs and the setup plan

Fill the template from the decision sheet, derived from the survey, not invented:

- `CLAUDE.md` (repo **root**): lean rules, permission tiers, and the wiring block into `docs/`. Keep it under ~150 lines.
- `docs/OVERVIEW.md`: what and why, **tech-free**. If it names a framework or database, it leaks; move that to `TECH_STACK.md`.
- `docs/TECH_STACK.md`: every layer with its reason and the hard constraints. This is the heart of a start-project run; fill it completely.
- `docs/ARCHITECTURE.md`: components, data flow, boundaries, and the layout tree (only folders that will actually exist).
- `docs/CONVENTIONS.md`: the naming and code patterns for the chosen stack. Don't restate rules a linter/formatter will enforce.
- `docs/HANDOFFS.md`: how work splits and is handed off; a map, not a second rulebook.
- `docs/context/CONTINUE_PROMPT.md`: seed the anchor with "scaffolded, not yet built; next step is the setup plan." Leave `docs/context/log.md` near-empty (correct, it earns content later).
- `docs/DESIGN.md`: keep only if the project has a UI; otherwise delete it **and** remove its wiring line from `CLAUDE.md` and the `HANDOFFS.md` table.

Then the four infrastructure docs. These aren't in the base template; copy their skeletons from `skills/start-project/example/` and fill them from the decision sheet:

- `docs/DEPLOYMENT.md`: where a release runs and how it ships. The target, the environments, the secrets, the manual first-deploy and rollback. Deployment is decided *now*, not deferred: name the target even if it's "a VPS via SSH."
- `docs/CI_CD.md`: the pipeline guidelines. What runs on push/PR, the merge gate, the stages (check → build → deploy), branch/release strategy. Points at `DEPLOYMENT.md` for the target; doesn't restate it.
- `docs/TESTING.md`: the testing guidelines. The bar, the layers (unit / integration / e2e), the runner and where tests live. The *intent* behind the suite, not a copy of the config CI enforces.
- `docs/SETUP.md`: the ordered standup checklist (below).

### The setup plan

Write the actionable checklist in `docs/SETUP.md`: ordered, one real command per step, a `[ ]` box. Stand up the **test + CI guard early**, before feature work, so there's a green baseline to build against instead of quality bolted on at the end. Deployment is a step in this plan, not an afterthought:

```
[ ] init the repo / package manager        <cmd>
[ ] add the test runner + first smoke test <cmd>          # the guard: a green baseline
[ ] add CI: lint + type-check + test on push  .github/workflows/ci.yml
[ ] provision the database                 <cmd or console step>
[ ] first feature slice
[ ] wire deployment                        see DEPLOYMENT.md → <cmd>
```

### The division of labor to encode

- **CI + tests own the *how***: the code-derivable facts that drift silently. Once CI enforces a rule (formatting, lint, type-check, test pass), `CONVENTIONS.md` *points* to it instead of restating it (that doc says so itself).
- **The docs own the *why***: decisions a reader can't recover from the code. Keep the *reasons* (which CI host, which runner, which deploy target, and why) in `TECH_STACK.md` and the three guideline docs; keep the *ordered actions* in `SETUP.md`.

When you write any of `SETUP.md`, `DEPLOYMENT.md`, `CI_CD.md`, or `TESTING.md`, add it to the `CLAUDE.md` wiring block and the `HANDOFFS.md` "where context lives" table: a doc nothing points to is a doc the model never reads.

Rules while writing: replace every `{{placeholder}}`; where a decision is genuinely open, write `<!-- unconfirmed: … -->` rather than a confident guess; don't restate what the tooling already enforces.

## Phase 5: Verify (no self-grading)

You wrote it, so you don't get to say it's done. Launch **one fresh evaluator sub-agent** (Agent tool, harsh prompt, its own context). Hand it only the repo and this definition of done:

*Every doc reflects the surveyed decisions; `OVERVIEW.md` names no technology; `TECH_STACK.md` gives a reason for every stack line; `SETUP.md` is an ordered, runnable checklist that matches the stack and includes a deployment step; `DEPLOYMENT.md`, `CI_CD.md`, and `TESTING.md` each exist, are filled, and cross-reference correctly (CI_CD points at DEPLOYMENT for the target, doesn't restate it); the wiring block in `CLAUDE.md` and the docs on disk match exactly: every project-context doc that exists is referenced (the two guides, `README.md` and `why_this_works.md`, count as referenced via the "further reading" line), and every reference points to a doc that exists (a skipped `DESIGN.md` must not still be listed); no `{{placeholder}}` survives; `CLAUDE.md` is lean; no doc contradicts another.*

Tell it to read the docs, check each claim, and report issues (not causes): pass/fail per criterion with the exact file and line. Do **not** give it your reasoning. Then reflect, fix, and re-verify. Cap at ~2-3 rounds; if something's stuck, stop and surface it. Finish with a short report: what you wrote, what the evaluator caught, and any `<!-- unconfirmed -->` markers still waiting on the human.

## What it owns, and what it delegates

- **Owns:** the source choice (survey / point / hybrid / example), the infrastructure survey, the decision playback, filling the docs template, and writing the setup plan plus the deployment/CI-CD/testing guideline docs.
- **Delegates:** the essence-first ideation to `/spark`, documenting an *already-built* codebase to `/apply`, and the actual execution of `SETUP.md` (running the commands, provisioning infra) to the builder, human or agent.
- **Does not:** write application code, provision live infrastructure, or grade its own docs. It sets the project up to be built; it doesn't build it.

## Requires

The docs template (`CLAUDE.md` + `docs/`) must be present in the target repo: start-project fills it, it doesn't ship it. If the repo has no template, copy it in first (`cp -r docs CLAUDE.md .claude your-repo/`), then run this. The four infrastructure docs (`SETUP`, `DEPLOYMENT`, `CI_CD`, `TESTING`) are not in the base template; their skeletons live in this skill's `example/` folder and get copied in on demand. Pointing at a reference project needs that project readable on disk.
