# SETUP: {{PROJECT_NAME}}

<!-- fill: the ordered steps that take a fresh clone to a running, shipping project.
     Do them top to bottom. Stand up the test + CI guard early, before feature work,
     so there's a green baseline to build against. Delete these comments as you fill it in. -->

From a fresh clone to running and shipping. Do the steps in order.

## Prerequisites

- {{runtime + version, e.g. Node 20 / Python 3.12}}
- {{package manager}}
- {{accounts or CLIs needed for deploy (see DEPLOYMENT.md)}}

## Steps

```
[ ] install dependencies              {{cmd}}
[ ] copy env template, fill secrets   cp .env.example .env  → set {{VARS}}
[ ] add the test runner + one smoke test   {{cmd}}     # the guard: a green baseline
[ ] add CI (lint + type-check + test on push)   .github/workflows/ci.yml   # enforce on every commit
[ ] provision the database            {{cmd or console step}}
[ ] first feature slice               (now CI is watching)
[ ] wire deployment                   see DEPLOYMENT.md → {{cmd}}
```

## Verify it worked

- {{Dev server up at localhost:{{port}} / tests green locally / CI passing on the first PR.}}
