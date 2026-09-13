# DEPLOYMENT: {{PROJECT_NAME}}

<!-- fill: where this runs and how a release gets there. The pipeline that automates it
     lives in CI_CD.md; this doc is the TARGET, the environments, the secrets, and the
     manual escape hatches (first deploy, rollback). Delete these comments as you fill it in. -->

Where {{PROJECT_NAME}} runs and how a release ships.

## Target

- **Runs on:** {{platform / cloud / VPS}}.
- **URL / region:** {{...}}.

## Environments

- {{prod / staging / dev: what each is for, and how they differ (data, scale, who sees them)}}.

## Config & secrets

- {{Where env vars and secrets live: the platform's secret store / CI secrets. Never in the repo.}}
- {{The vars a deploy needs: name them here; the values live in the secret store.}}

## How a release ships

- **Trigger:** {{merge to `main` → CI deploys / a version tag / a manual promote}}. The pipeline is in `CI_CD.md`.
- **First / manual deploy:** {{the command or console steps to ship by hand when you need to.}}

## Rollback

- {{How to undo a bad release: redeploy the previous tag / the platform's rollback button / revert + redeploy.}}
