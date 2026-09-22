# ORG.md

You are a coding agent. A manager has pointed you at a folder that holds their team's repositories, and wants one card for all of them.

This is the kit's **org read**. It is the cold read of `RUN.md` step 2, run once per repository, and nothing else. It writes one file, at the folder root, and it writes nothing inside anybody's repository.

The single-repo run (`RUN.md`) is the thing that writes a docs layer. This one only measures. That is the point: a manager can run it on twenty repositories before lunch, because it changes none of them.

Follow these six steps in order.

## 1. Say what is about to happen

Print these four lines, then keep going:

- I read every git repository directly under this folder. For each one: the top-level listing, the README, the other prose documents at the root, and the instruction file if there is one. Nothing else.
- I write one file, `ORG_MEMORY_CHECK.md`, here beside your repositories. I write nothing inside any repository, I change nothing, I commit nothing, I run no build.
- I never open a secret. Not `.env` or any `.env.*`, not a service-account file, not anything named like a key, a token or a credential, even when it sits at the root and even when it is an example.
- About two minutes per repository.

Those four lines are the contract. **This read is read-only by design.** If any step below would write, move or delete anything other than `ORG_MEMORY_CHECK.md` at this folder root, stop and tell the manager instead.

## 2. Find the repositories

If `$ARGUMENTS` names repositories (one or more paths), that is the list, and the folder is their common parent.

Otherwise the folder is `$ARGUMENTS` if it names one, else the current directory, and the list is every **direct child** of that folder which is a git repository, meaning a child directory that holds a `.git`:

```bash
ls -d */.git 2>/dev/null
```

Do not go deeper than one level. A repository nested inside another repository is that repository's business, and a manager who wants it read will say so by name.

If the list is empty, print one line saying that this folder holds no git repositories, name the folder, and stop. Do not go hunting.

Sort the list alphabetically so two runs of the same folder produce the same table.

## 3. The cold read, once per repository

For each repository in the list, answer these five questions. They are `RUN.md` step 2, word for word, and they have to stay that way: the whole value of the number is that it is the same question set the single-repo run is graded on.

1. Where does a new file of this project's main kind go, and what must it look like?
2. Name one tool in the stack and say why it was chosen over the obvious alternative.
3. What naming or code convention would a reviewer here flag first?
4. What is the one thing a change in this repo must never do?
5. What is this project for, in one sentence?

**Answer from exactly this and nothing else:** the repository's top-level directory listing; its `README.md` and any other prose document at the root; and its instruction file, if it has one. Answer from all of it, not only from the instruction file. Most repositories have no instruction file and their agents read the README instead, so a missing one is not a reason to answer WOULD-HAVE-TO-LOOK five times.

The instruction file may be `CLAUDE.md`, `AGENTS.md`, `.cursor/rules` or `.github/copilot-instructions.md`. The last two sit below the root, so checking whether those two paths exist is the only look below the root you get.

Nothing else: no source file, no config, no other directory. **And never a secret, at any point in this run.** You do not read them, quote them or name their values.

Label each answer **SURE**, **GUESS** or **WOULD-HAVE-TO-LOOK**, the same three labels the single run uses.

`ls`, `cat` and `head` are all you need. Read the whole README only if it is short; the first 200 lines answer these questions or nothing does.

**The score for a repository is how many of the five it answers SURE.** GUESS and WOULD-HAVE-TO-LOOK both score zero, because both mean the agent working in that repository is filling the gap from its training data rather than from the project.

That number is a **ceiling**, and the card says so. The single-repo run grades these answers against the real code afterwards, and grading can only ever turn a SURE into a WRONG, never a GUESS into a right answer. So the true before score is this number or lower.

## 4. Count the contradictions you can see

A contradiction here is one thing only: **a claim in the instruction file or the README that the root listing itself disproves.** It names a file or a folder at the root, and the root listing says that file or folder is not there. A moved entry point, a script that is gone, a folder from a refactor that never happened.

You have not read the code, so that is the only class you can prove, and you count nothing else. No style differences, no stale prose, no suspicion. **Zero is a normal and honest answer**, and the line prints either way.

Keep the count per repository, and keep one short phrase for each one, because the manager page prints them.

This deliberately undercounts. The single-repo run reads the code and finds the rest, each with the file and the line. Say that in one line under the table rather than letting the number pass for the whole truth.

## 5. Write the card

Write `ORG_MEMORY_CHECK.md` at the folder root, and print the same thing to the terminal.

It holds two things: the per-repo table, then the org card.

The table, one row per repository, in this order:

```
| Repository | Score | Instruction file | Contradictions | Guessing about |
|---|---|---|---|---|
| <name> | <n> of 5 | <file name, or none> | <c> | <the questions it could not answer, short, semicolons between> |
```

Then the org card, in exactly this shape, with no code fence around it:

```
ORG MEMORY CHECK: <folder name>
Repos read:              <M>
Scoring 2 or below:      <N> of <M>
Guessing most about:     <the question that was WOULD-HAVE-TO-LOOK most often, in words>
Instruction files:       <k> of <M> repos have one
Contradictions on sight: <c>
Rules enforced:          0 (nothing here checks a hook, a test or CI; that is the course)
```

`<M>` is how many repositories you read. `<N>` is how many of them scored 2 or below. `<c>` is the sum of the per-repo contradictions. `<k>` is how many have an instruction file of any of the four names. The last line is a constant: you have checked no hook, no test and no CI gate, and no repository in this folder has been given one by this run.

`Guessing most about` is one of the five questions, said in words, not its number: the one that came back WOULD-HAVE-TO-LOOK in the most repositories. On a tie, take the lowest-numbered question of the tied set, so two runs of the same folder agree.

Under the card, in the file and on the terminal, put these three lines and nothing more:

- A repository's score is how many of the five questions its own visible files answer without a guess. It is a ceiling: the full run grades the answers against the code, and a SURE can come back wrong.
- Contradictions on sight are only the claims the root listing itself disproves. The full run reads the code and finds the rest.
- Nothing here was changed. This was a read.

## 6. Print the offer

Last, to the terminal only, written to no file:

```
Paste that card at https://p2p-course.diamant-ai.com/teams?utm_source=github&utm_medium=terminal&utm_campaign=org-card#card to get the manager page for it: the card, the table, and what a team licence costs.
```

Then stop. Do not offer to fix anything, do not start a single-repo run on your own, and do not write into a repository. If the manager wants the layer built, the command is `/agent-memory` inside that repository, or the line in `RUN.md`, and that run stops for their approval before it writes.
