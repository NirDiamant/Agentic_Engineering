# TESTING: {{PROJECT_NAME}}

<!-- fill: how this project tests, and the bar a change has to clear. Guidelines the
     agent follows when it writes or changes tests. The runner and lint rules are
     enforced by CI (see CI_CD.md); this doc is the intent behind the suite, not a
     restatement of the config. Delete these comments as you fill it in. -->

How this project tests, and the bar a change clears before it merges.

## The bar

- {{What must ship with a test: new behavior always; a bug fix starts with a regression test that reproduces it.}}
- CI runs the suite on every push; a red suite blocks the merge (see `CI_CD.md`).
- {{What's deliberately NOT tested: the glue you'd only be testing the framework for.}}

## Layers

- **Unit.** {{The smallest behavior, no I/O. The bulk of the suite; fast.}}
- **Integration.** {{Across a real boundary: the database, an HTTP call. The paths that actually break.}}
- **{{E2E / smoke}}.** {{The one critical flow, end to end. Few, and only the flows that must never break.}}

## Conventions

- **Runner:** {{vitest / pytest / go test / …}}.
- **Location:** {{co-located as `*.test.{{ext}}` next to the code, or a `tests/` mirror}}, one pattern, everywhere.
- **A test names the behavior, not the function:** `{{"rejects an expired token"}}`, not `{{"test auth"}}`.
- Test **behavior, not implementation**: a refactor that preserves behavior must not break a test.

## Constraints

- No network or real external services in unit tests: {{mock at the boundary}}.
- {{Coverage bar, if any. And stop chasing the number past the point it catches real bugs.}}
