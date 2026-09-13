---
name: spark
description: The human on-ramp to the agent-harness. Turn an idea that only exists in your head into a running build, without writing a spec yourself. Leads you through a short interview about the ESSENCE of what you're making (the purpose, the image in your mind, the core behavior), then distills it into a build brief and hands off to /harness-plan, walking you through the gates to /harness-unleash, and closes the arc by documenting the finished build with /apply. Trigger on "/spark", "start a fresh project", "I have an idea for", "help me start building X", "new project from scratch", "I want to make X".
metadata:
  author: roihala
  version: '0.1.0'
  tags: greenfield, on-ramp, interview, harness, ideation, single-prompt
---

> **Experimental.** This skill does not run on its own from this repository. It hands off to
> `/harness-plan` and `/harness-unleash`, two skills that do not ship here and must already be
> installed in your skills path. Without them, stop and say so.

# Spark (idea to build, guided)

The harness chain (`/harness-plan` → `/harness-unleash`) can take a project from a one-line prompt to a finished build. But it starts from a prompt you have to write, and a vague prompt makes a vague build. **Spark is the front door**: it draws the real idea out of your head first, then feeds the harness something worth building against.

You own the interview and the distillation. You do **not** re-plan or build: that's the harness's job. Your output is a tight build brief and a clean handoff.

## The one rule

**Capture the essence, not the tech.** Ask about what the thing *is*, how it should *feel*, and the one behavior it lives or dies on. Do not pin down a database, a framework, or an API shape: one over-specified detail here cascades and magnifies across a multi-hour build. If you catch the human reaching for tech, gently steer back to intent. The technical detail is the contract's job, negotiated later.

## Phase 1: The essence interview

Ask in **two small batches**. Wait for the answers to batch one before sending batch two. Never dump all seven at once, and never answer for the human.

**Batch one, the spark and the essence:**

1. In a sentence or two: what are you making, and what made you want it to exist?
2. Who is it for, and what moment are they in when they reach for it? One person, one concrete situation.
3. Picture someone using it and it just works. What's the one thing they do? Walk me through that core moment, start to finish.
4. What will it refuse to be? Name the tempting things it is *not*. This answer saves the most time later.

**Batch two, the image and the core:**

5. The image in your head: how should it feel to use? A mood, not a tech choice (calm, fast, playful, dead serious). If a product, site, or object captures the feel, name it.
6. The core: what's the one mechanism or interaction the whole thing hinges on? If that one thing feels like magic, you have a product.
7. While it's built: do you want to review each milestone, or set the direction and let it run to a finished draft?

## Phase 2: Distill and play back

Turn the answers into a short **build brief** and show it to the human for correction before anything scaffolds:

- **Pitch**: one line, what it is and for whom.
- **Core**: the one mechanism the build must nail (from Q6).
- **Feel**: the mood and any reference (from Q5). This is the creative direction the harness carries.
- **Not**: the non-goals (from Q4).
- **Autonomy**: review-each-milestone vs run-to-draft (from Q7).

Play it back in a few lines. Get one "yes, that's it" before you hand off. A wrong read here becomes a wrong build.

## Phase 3: Hand to /harness-plan (the gate)

Invoke **`/harness-plan` in GATE mode**, feeding it the build brief as the creative direction and one-line prompt. It writes a high-level `spec.md` (sprints + direction) and scaffolds the project, then stops.

**Walk the human through the gate:** tell them plainly that `spec.md` is theirs to review and edit now. This is the seam they own before anything builds. Don't rush past it.

## Phase 4: Walk to /harness-unleash

Once the human is happy with `spec.md`, invoke **`/harness-unleash`**. Narrate the gates as they come so it never feels like a black box:

- It negotiates the **contract** (what "done" means), then opens a one-pager that *explains the plan and its complexity*, the last human-legible checkpoint before the build loop.
- Then the generator↔evaluator loop runs in fresh context windows until the contract passes.

Warn once that this is a long, unattended, potentially expensive run, checkpointed via git. If the human chose "review each milestone" in Q7, prefer stepping through manually (`/harness-build` → `/harness-eval`) instead of a full unleash.

## Phase 5: Document the finished build (the close)

A build that passes its contract but has no `docs/` layer is a project the next session (human or agent) has to reverse-engineer. Spark's journey isn't done until the build documents itself, so close the loop rather than leaving it to the human to remember.

Once the contract passes and the build settles, invoke **`/apply`** on the finished repo. It researches the real code, plays back what it found, fills the docs template (`CLAUDE.md` + `docs/`) from the truth of the codebase, and verifies with a fresh evaluator, so the project ships already knowing itself.

Narrate it as the natural end of the arc: *the thing is built and green; now it gets its memory.* If the human chose "review each milestone" in Q7, walk `/apply`'s playback gate with them; if they chose run-to-draft, let it run and surface any `<!-- unconfirmed -->` markers it leaves for them at the end.

## What Spark owns, and what it delegates

- **Owns:** the interview, the distillation, the handoff narration, matching autonomy to what the human asked for, and closing the arc with the docs write.
- **Delegates:** planning (`/harness-plan`), the done-definition (`/harness-contract`), building and grading (`/harness-unleash` / `/harness-build` + `/harness-eval`), and the docs write itself (`/apply`).
- **Does not:** reimplement any of the above inline. Spark orchestrates the journey end to end (idea → plan → build → documented), but each stage is executed by the skill that owns it.

## Requires

`/harness-plan` and `/harness-unleash` must be installed (they live in `~/.claude/skills/`). Spark is only the on-ramp; it assumes the harness chain is present. If it isn't, stop and say so rather than improvising a build loop.

`/apply` (Phase 5) should be installed for the docs close. If it isn't, don't improvise the docs layer; finish at the passing build and tell the human to run the docs write when `/apply` is available.
