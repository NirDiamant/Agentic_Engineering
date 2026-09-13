---
name: testify
description: Stand up a project's tests and prove they're worth anything. Where /start-project writes docs/TESTING.md (the intent, meaning the bar, the layers, the runner) but doesn't touch code, testify does the doing. It detects the stack, wires the runner, writes real tests across the layers (unit, integration + happy-path, e2e for UI), and then VERIFIES them by breaking the code on purpose. A test that stays green on broken code is theater. Runs in two modes, `full` (all layers + automated mutation testing + property tests) and `light` (the happy-path floor, meaning does it boot and respond, verified by hand-mutation, no automated gate). Reconciles docs/TESTING.md with what it actually built. Trigger on "/testify", "set up testing", "add tests to this project", "this project has no tests", "wire up the test suite", "write tests for this", "just make sure it runs".
metadata:
  author: roihala
  version: '0.1.0'
  tags: testing, mutation-testing, happy-path, verification, setup
---

# Testify (stand up the tests, prove they catch bugs)

The repo's other doors write *about* the project. `/start-project` surveys the stack and writes `docs/TESTING.md`, the **intent** behind a suite: the bar, the layers, the runner, where tests live. But it explicitly stops there; it doesn't write a line of test code. **Testify is the door that does the testing.** It wires the runner, writes the actual tests, and (the part that matters) proves they assert something by breaking the code and watching them fail. Then it reconciles `docs/TESTING.md` with what it really built.

This is the *how* to start-project's *why*, exactly the division this repo already draws: **CI and tests own the how; docs own the why.** A green suite is the artifact; `TESTING.md` is the reason it looks the way it does.

## The one rule

**A test that passes when the code is broken is worthless.** Coverage is the illusion: a generated suite can hit 100% of the lines and assert nothing. The only proof a test is real is that it goes **red** when the behavior it guards is broken. So testify never certifies itself on a coverage number; it certifies by *mutation*: flip a `>`, drop a branch, return the wrong value, and confirm a test fails. This is the same anti-self-grading stance the doc skills take with a fresh evaluator: **the thing that judges the work is not the thing that made it.** Here the judge is the broken code.

## Phase 1: Pick the mode

Not every project earns a full suite on day one. Decide up front:

- **`full`**: the whole pyramid, for a project worth the rigor. Unit + integration/happy-path + e2e (if UI), plus **automated** mutation testing and property-based tests. The suite is self-verifying in CI.
- **`light`**: the **happy-path floor**. The user wants proof the thing *runs and responds*, not a certified suite (a prototype, an early service, a "just make sure it works"). Wire the runner + the happy-path/integration smoke (+ unit tests on the few critical units), verify by **hand-mutation**, and stop. No automated gate, no property tests, no e2e.

If they didn't say, infer it: a serious, maintained project → `full`; "just check it runs" or a prototype → `light`. When it's genuinely ambiguous, ask one line: *full suite, or just the happy-path floor?* Record the mode in `docs/TESTING.md` so the next run knows where things stand and, for `light`, that the deeper layers are deferred, not missing by accident.

## Phase 2: Detect the stack

Read the manifests and lockfiles (`package.json`, `pyproject.toml`, `go.mod`, …), the tree, and a handful of real source files. Find: the language(s), the runner already present (if any), whether there's a **UI** (decides e2e), the **main entrypoints** (the routes, the CLI command, the primary workflow; this is what the happy-path tests hit), and where **input-range logic** lives (parsers, validators, money/date math, boundaries; this is what earns property tests).

If `docs/TESTING.md` already exists, **read it first**: it's the current intent and the record of any prior run. Augment toward it; don't clobber a suite that's already there.

## Phase 3: Wire the runner

Ensure the conventional runner is set up: **Vitest** (TS/JS), **pytest** (Python), `go test`, etc. If one's already there, keep it; don't switch a Jest project to Vitest mid-stream. One runner, one test-location pattern (co-located `*.test.ext` or a `tests/` mirror), matching what `docs/TESTING.md`/`CONVENTIONS.md` already say.

## Phase 4: Write the tests, by layer

- **Happy-path + integration (always, this is the floor).** Prove the service **boots, wires together, and responds**: the main endpoint returns the right status and shape (hit the *real* app with `httpx`/`TestClient` or `supertest`, not a wall of mocks), the CLI command runs and emits correct output, the primary workflow holds across its real components. This is the layer that catches "it compiled but doesn't run," and it's the one thing **every** project gets, backend and CLI included. It's the whole point of `light` mode and the base of `full`.
- **Unit.** The smallest behaviors, no I/O (the bulk of a `full` suite). In `light`, only the few genuinely critical units (the money/date/parse logic). Name the behavior, not the function: *"rejects an expired token,"* not *"test auth."* Test behavior, not implementation. A refactor that preserves behavior must not break a test.
- **E2E (UI projects only, `full`).** The one or two critical flows, end to end in a browser. Few by design. Skip entirely for backend-only projects.

Don't chase line coverage while writing: the next phase is what judges whether these tests are real.

## Phase 5: Verify (break the code on purpose)

This is the load-bearing step, and it's non-negotiable in both modes.

- **Hand-mutation (always).** For the 2–3 most important behaviors, break the code deliberately (flip a comparison, drop a branch, return a wrong value) and confirm a test goes **red**. If nothing fails, the test is theater: fix the test, then revert the code. This is the minimum proof, and it's all `light` needs.
- **Automated mutation (`full`).** Wire `Stryker` (JS/TS) / `mutmut` (Python) to run the same loop on every change: it mutates the code and fails when a mutant survives (a mutant that lives is a test asserting nothing). Judge on **mutants-killed, not coverage %.** On a large repo, scope it to the changed paths so it stays fast enough to run per-PR.
- **Property-based (`full`, where it fits).** For anything with a real input range (parsers, validators, money/currency, date/time, boundary checks), add `fast-check` (JS/TS) / `Hypothesis` (Python). You assert the invariant; the tool throws hundreds of adversarial inputs at exactly the boundaries generated tests miss.

Report the result honestly: in `full`, the mutants-killed score; in `light`, which behaviors you hand-verified. Never dress a coverage number up as certification.

## Phase 6: Reconcile docs/TESTING.md

Update `docs/TESTING.md` to match what you actually built: the mode, the layers present, the runner, the location pattern, how to run the suite and the mutation check, and (for `light`) that the deeper layers are deliberately deferred. If the doc didn't exist, create it from the intent your suite now embodies. Add it to the `CLAUDE.md` wiring block and the `HANDOFFS.md` context table if it isn't there. A doc nothing points to is one the agent never reads. Keep it the *why*, not a copy of the config: it says what the bar is and why, not every flag CI passes.

## What it owns, and what it delegates

- **Owns:** picking the mode, detecting the stack, wiring the runner, writing the tests across the layers, verifying them by mutation, and reconciling `docs/TESTING.md`.
- **Delegates:** the *intent* of the suite (the bar, the stack rationale) to `/start-project` and `/apply`, which write the docs; documenting an already-built codebase to `/apply`.
- **Does not:** invent behavior the code doesn't have, chase a coverage target for its own sake, or self-certify. The broken code is the judge.

## Requires

A repo with real code to test (for `light`, at least a runnable entrypoint). If the project uses this template's docs layer, `docs/TESTING.md` is where the intent lives; testify reads it and writes it back. The runner, mutation tool, and property-test library are per-stack; testify picks and installs them if they're missing.
