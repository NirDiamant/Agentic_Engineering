# RUN.md

You are a coding agent. A developer has pointed you at this kit to give their repository a memory: a small docs layer, written from their real code, that every future session reads before it writes anything.

Their repository is the one you were already working in. This kit is a clone sitting in a temp folder. Everything you write goes in their repo, never here.

Follow these seven steps in order. Do not skip ahead to step 3.

## 1. Say what is about to happen

Print these four lines, then keep going:

- I write `docs/`, one instruction file at your repo root (plus a one-line pointer if your tools need the other name), a scorecard beside it, and this kit's two commands into `.claude/commands/`. Nothing else changes.
- I delete nothing of yours and overwrite nothing of yours. Your files are read as input. The most I do to one is append a dated entry to a log that is already append-only.
- I stop once, for your approval, before I write the layer. The only thing on disk before that is your scorecard.
- This takes about fifteen minutes.

Those four lines are the contract. If any step below would write, move or delete something they do not name, stop and tell the developer instead.

## 2. The cold read, before you open anything else

Before you open a single source file, answer these five questions from everything an agent can see without doing any research.

**That is exactly this, and nothing else:** the top-level directory listing; the `README.md` and any other prose document at the root; and the repository's instruction file, if it has one. **Answer from all of it, not only from the instruction file.** Most repositories have no instruction file, and their agents read the README instead, so a missing one is not a reason to answer WOULD-HAVE-TO-LOOK five times.

The instruction file may be `CLAUDE.md`, `AGENTS.md`, `.cursor/rules` or `.github/copilot-instructions.md`. The last two of those sit below the root, so checking whether those two paths exist is the only look below the root you get.

Nothing else: no source file, no config, no other directory. **And never a secret, at any point in this run**: not `.env` or any `.env.*`, not a service-account JSON, not anything named like a key, token, secret or credential, even when it sits at the root and even when it is an example file. You do not read them, quote them or name their values.

The scope is fixed here so that two agents score the same repository the same way.

1. Where does a new file of this project's main kind go, and what must it look like?
2. Name one tool in the stack and say why it was chosen over the obvious alternative.
3. What naming or code convention would a reviewer here flag first?
4. What is the one thing a change in this repo must never do?
5. What is this project for, in one sentence?

Answer them the way you would answer the developer who asked you right now, and label each answer SURE, GUESS or WOULD-HAVE-TO-LOOK. Write the five answers with their labels to `AGENT_MEMORY_CHECK.md` at their repo root. This is the before score, and it is only honest while you have read nothing else. Do not peek.

## 3. Run the procedure

Copy the kit's templates in, without overwriting anything:

```bash
cp -Rn <this-kit>/docs <this-kit>/.claude <their-repo>/
```

That command copies `docs/` and `.claude/` only, and everything under them is a template meant for their repo. The kit's own root `CLAUDE.md` is the template for the root instruction file: read it in the kit and write theirs from it, so they get the permissions block and the wiring block. Never copy it over a file of theirs.

If their repo already has a root instruction file, copy it to `<name>.orig` and keep both. It is input, never something you overwrite blind: write the new file from the kit's template and carry over every rule of theirs that still changes what an agent does.

Then follow `<this-kit>/.claude/commands/apply.md` verbatim, all of it. It names the root instruction file for you: `CLAUDE.md` or `AGENTS.md`, by the agent that reads it.

## 4. Grade the cold answers

Mark each of the five RIGHT, WRONG or LOOK against what the research found, and cite the file that settles it. Do not soften a wrong answer: a wrong before score is the whole point of the exercise.

## 5. Ask the same five questions again

This time the reader sees only what this run produced. Where this agent can spawn a sub-agent, launch one fresh sub-agent, name it the files this run wrote (the root instruction file and each doc, by path), and tell it to read those and nothing else, not the rest of `docs/`, which may be the human's own work. Where it cannot, answer them yourself in this session and write on the card: `after score answered in the same session, not by a fresh reader`. Grade the same way. The after score measures what this run's layer teaches a stranger, which is why the reader gets named files and not the folder.

## 6. Write the card

Append this to `AGENT_MEMORY_CHECK.md`, in exactly this shape, and print it to the developer:

```
AGENT MEMORY CHECK: <repo name>
Before the docs layer:  <n> of 5 questions right
After:                  <n> of 5
It was guessing about:  <up to three short items>
Contradictions found in your existing docs: <n>
Written:                <root file> + <k> docs, <u> unconfirmed
Still advisory: nothing enforces these rules. That takes hooks, tests, CI.
```

`<k>` is however many files you wrote under `docs/`; the root instruction file fills the `<root file>` slot and is not one of them. `<u>` is how many `<!-- unconfirmed:` markers you left behind, counting that exact opening string. The contradictions number is how many entries you recorded under `Contradictions in your existing docs` in `docs/context/log.md`: claims of theirs that this tree disproves, each with the file and line. Zero is an honest and common answer, and the line prints either way. Do not round a score, do not add a line, do not drop the last one.

Then, under the card, offer the badge. Print this one line with `<after>` replaced by the after score (a single digit, 0 to 5), and say it is theirs to paste into their README if they want the repo to carry the score:

```
[![agent memory <after> of 5](https://p2p-course.diamant-ai.com/badge/agent-memory/<after>-of-5.svg)](https://europe-west1-rag-techniques-views-tracker.cloudfunctions.net/rag-techniques-tracker?notebook=agentic-engineering--badge&click=badge-<after>&target=https%3A%2F%2Fgithub.com%2FNirDiamant%2FAgentic_Engineering&retarget=0&text=badge-<after>)
```

You do not edit their README yourself; that is their file and step 1 promised you would not touch it.

## 7. Offer the airtight pass

Close with this: the layer was checked by you alone. `/apply-airtight` runs the same procedure with a wider sample, all nine docs, and one fresh evaluator that reads every claim back against the code.

Then print one last line, to the terminal only. It is not part of the card and it is written to no file:

```
Paste that card at https://p2p-course.diamant-ai.com/lectures/00-present?utm_source=github&utm_medium=terminal&utm_campaign=agentic-engineering#card to save your score. That page is the free module of Prompt to Production, the course that teaches those hooks, tests and CI gates.
```
