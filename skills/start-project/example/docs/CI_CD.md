# CI_CD: {{PROJECT_NAME}}

<!-- fill: how code moves from a commit to production, automatically. These are the
     guidelines the agent follows whenever it touches the pipeline. Keep the deploy
     TARGET and secrets in DEPLOYMENT.md; keep the PIPELINE POLICY here. A rule the CI
     config already enforces doesn't need restating in prose. Delete these comments as you fill it in. -->

How code moves from a commit to production, automatically, and the rules that pipeline obeys.

## The merge gate

- CI must be **green before a branch merges**. No merge on red.
- What runs on every push and PR: {{lint, type-check, test}}, the checks that block a merge.
- {{What enforces the gate: branch protection on `main`, required status checks.}}

## Pipeline stages

1. **Check**: {{lint + type-check + test}}. Fast; runs on every push and PR.
2. **Build**: {{compile / bundle / build the image}}. Runs only after Check passes.
3. **Deploy**: {{on merge to `main`, deploy to the target}}. Target, envs, and secrets live in `DEPLOYMENT.md`.

## Branch & release strategy

- {{Trunk-based with short-lived PR branches? A `develop` → `main` promote?}}
- What triggers a production deploy: {{merge to `main` / a version tag / a manual approval step}}.
- {{Whether preview/staging deploys run on PRs.}}

## Constraints

- Secrets live in {{the CI secret store}}, never committed to the repo.
- A check that gates merges (lint, type-check, the test suite) must not be removed to make a build pass. Fix the code.
- {{Any required job that must always run, e.g. a security scan.}}
