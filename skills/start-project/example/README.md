# example/: the fallback source

A neutral, stack-agnostic skeleton for the infrastructure docs `/start-project` produces. It exists for the case where you have **no existing project to point at** and don't want to answer every survey question from scratch: the skill copies these files into your repo's `docs/` (and `.github/`), then fills the `{{placeholders}}` from your survey answers.

It is a *skeleton*, not a working config: every `{{...}}` is a decision you still make. The structure (which docs exist, how they cross-reference) is the opinionated part; the contents are yours.

```
example/
├── docs/
│   ├── SETUP.md         ordered standup steps: clone → running → shipping
│   ├── DEPLOYMENT.md    where it runs and how a release ships
│   ├── CI_CD.md         pipeline guidelines: what runs when, the merge gate
│   └── TESTING.md       testing guidelines: the bar, the layers, conventions
└── .github/workflows/
    └── ci.yml           pipeline skeleton: check → build → deploy
```

These four docs are added on top of the base template (`OVERVIEW`, `ARCHITECTURE`, `TECH_STACK`, `CONVENTIONS`, `HANDOFFS`). When the skill writes any of them into a project, it also wires it into the `CLAUDE.md` "Project context" block and the `HANDOFFS.md` table: a doc nothing points to is a doc the model never reads.
