---
name: tester
description: Try to fail what just changed. The scoped, everyday complement to /testify. Reads the conversation or PR diff, picks the few behaviors most worth attacking (the art of covering enough without over-testing), writes tests that attempt to break them on the existing runner, summarizes each attempt with severity, and updates docs/TESTING.md. Trigger on "/tester", "test this", "add tests for this change", "cover this PR", "try to break this".
metadata:
  author: roihala
  version: '0.1.0'
  tags: testing, scoped, pr, minimal
---

# Tester (test the change, not the world)

Where `/testify` stands up a project's whole suite, tester covers **one change**: the diff or the work discussed in this session. The few tests that matter, then stop.

## Scope

What this conversation / PR changed. Not the whole repo, not existing untested code: that's `/testify`'s job.

## Infrastructure

`docs/TESTING.md` is the source of truth: read it first for the runner, conventions, and what's already covered. If it doesn't exist, detect the setup from the repo. No runner at all? Wire the minimal one for the stack (pytest / Vitest / Playwright, enough to run tests and nothing more), or hand off to `/testify` if the project deserves a real stand-up.

## Select

Rank the changed behaviors by *what would hurt most if silently broken*, and test only the top of that list, typically 3–7 tests:

- Core behavior: the thing the change exists to do, exercised through its real entrypoint.
- Edge that plausibly breaks: boundaries, empty/invalid input, the bug's exact repro (a fix gets a test that fails without it).
- Contract others rely on: response shape, return type, side effect.

Skip: trivial code (getters, config, framework glue), unreachable errors, permutations of the same logic, anything a type checker already guarantees.

## Write

- Follow the runner and conventions from Infrastructure; don't add frameworks beyond what that step wired.
- Test behavior through public entrypoints, not internals. Mock only what's genuinely external (network, clock, paid APIs).
- Attack, don't confirm: each test is an attempt to *fail* the code (hostile input, boundary, wrong order). Passing means the code survived the attempt.
- One assertion story per test; name it after the behavior.

## Finish

Run the tests, then hand-mutate the single most important behavior: break the code, watch a test go red, revert (a test that stays green on broken code is theater). Summarize results, one line per attempt: what you tried to fail, whether it broke, how it fails, and severity (critical / major / minor). A red test on a real bug is a finding: report it with its severity, don't quietly patch code the user didn't ask to change. Update `docs/TESTING.md` with what's now covered, creating it if absent, noting what you deliberately didn't test.

## Self-edit rule

THIS SKILL SHOULD BE AS MINIMALISTIC AS POSSIBLE. Before writing any change or making any edit, ask: **how can I do this with as few words as I possibly can?**

Applies to every future edit. New instruction? Find the line it belongs in and rewrite that line. Do not append. Fixing a failure? Cut the wording that allowed it rather than adding a warning next to it. Skill grew? It regressed.
