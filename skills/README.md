# skills/

Skills this template ships. A skill is a stateful, multi-step capability an agent runs by name, heavier than the one-shot `/apply` command, because it holds a conversation and orchestrates other skills.

| Skill | What it does |
|-------|--------------|
| [`spark`](../skills-experimental/spark/SKILL.md) | **Experimental, and it does not run on its own here:** it requires two skills that do not ship in this repo, `/harness-plan` and `/harness-unleash`. The greenfield on-ramp. Interviews you about the essence of a project you have in mind, distills it into a build brief, then hands off to `/harness-plan` and walks you through to `/harness-unleash`. |
| [`start-project`](start-project/SKILL.md) | The technical on-ramp. The mirror of `spark`: surveys the infrastructure up front (stack, database, cloud, CI/CD, deployment, testing), fills the docs layer plus a `SETUP.md` plan and guideline docs for deployment/CI-CD/testing, and verifies with a fresh evaluator. Can "point" at an existing project and copy its setup, or fall back to a built-in neutral skeleton (`example/`) when there's nothing to point at. |
| [`testify`](testify/SKILL.md) | Stands up the actual test suite and proves it catches bugs: the *doing* to start-project's *documenting*. Detects the stack, wires the runner, writes tests across the layers (unit / integration + happy-path / e2e), then verifies by breaking the code on purpose (a test that stays green on broken code is theater). Two modes: `full` (all layers + automated mutation + property tests) and `light` (the happy-path floor, hand-mutation verify). Reconciles `docs/TESTING.md` with what it built. |
| [`docs-gardener`](docs-gardener/SKILL.md) | Keeps the *why* layer current. At the end of a session it records only what was actually decided or discovered (the tradeoffs, connections and steering points that aren't recoverable from the code), appending dated entries to the decision log, editing the intent/architecture docs in place, and pruning what's gone stale. Never touches code-derivable facts; those belong to tests. Writes without asking, held to anti-bloat guardrails instead of an approval gate. |
| [`tester`](tester/SKILL.md) | The everyday complement to `testify`: tries to **fail one change**, not the world. Reads the conversation/PR diff, ranks the changed behaviors by what would hurt most if silently broken, writes the top 3–7 tests as attempts to break the code, and reports each attempt in one line: what it tried to fail, how it fails, severity. Hand-mutates the most important behavior, updates `docs/TESTING.md`. The art of covering enough without over-testing. |

## Using a skill

With the plugin installed (`/plugin install agentic-engineering@diamantai`) every skill in this folder is already available, namespaced `agentic-engineering:<name>`. Without the plugin, install or symlink a skill into your skills path (`~/.claude/skills/`) and invoke it by name. `spark` is not in this folder on purpose: it sits in `skills-experimental/` so the plugin does not load a skill whose dependencies do not ship here.

`spark` depends on the harness chain (`/harness-plan`, `/harness-unleash`) already being installed. It is the on-ramp, not the engine, so without those two skills it stops rather than improvising a build loop.
