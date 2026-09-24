# ORG.md

You are a coding agent. A manager has pointed you at a folder that holds their team's repositories, or at one large repository that many teams share, and wants one card for their team's part of it.

This is the kit's **org read**. It is the cold read of `RUN.md` step 2, run once per repository, and nothing else. It writes one file, at the folder root, and it writes nothing inside anybody's repository.

The single-repo run (`RUN.md`) is the thing that writes a docs layer. This one only measures. That is the point: a manager can run it on twenty repositories before lunch, because it changes none of them.

Follow these six steps in order.

## 1. Say what is about to happen

Do step 2 first, silently, so you know which of the two cases this is. Then print these four lines and keep going:

- Folder of repositories: I read every git repository directly under this folder. For each one: the top-level listing, the README, the other prose documents at the root, and the instruction file if there is one. Nothing else.
  Shared repository: I read the <P> folders of <repo> that belong to <whom>, found in <CODEOWNERS / the workspace manifest / your list>, each one as if it were a repository of its own: its listing, its README and prose documents, and the instruction files an agent working there would load. Nothing else.
  Print whichever of the two is true, filled in.
- I write one file, `ORG_MEMORY_CHECK.md`, here beside your repositories. I write nothing inside any repository, I change nothing, I commit nothing, I run no build.
- I never open a secret. Not `.env` or any `.env.*`, not a service-account file, not anything named like a key, a token or a credential, even when it sits at the root and even when it is an example.
- About two minutes per repository.

Those four lines are the contract. **This read is read-only by design.** If any step below would write, move or delete anything other than `ORG_MEMORY_CHECK.md` at this folder root, stop and tell the manager instead. When the folder is itself a shared repository, "beside" means its parent folder, never inside it.

## 2. Find what to read

What you read is a list of **units**. A unit is usually a repository. In a large shared repository that many teams work in, a unit is one team's folder inside it, because a score for the whole repository measures every other team's code too.

`$ARGUMENTS` may end with `--owner <handle>`, for example `--owner @acme/payments`. Take it off before reading the rest as paths.

**Case 1: `$ARGUMENTS` names paths.** Each path is a unit, whether it is a repository or a folder inside one. The folder is their common parent.

**Case 2: the folder is itself a git repository** (it holds a `.git`). That is a shared repository, and its units are folders inside it, found in this order:

1. **With `--owner`:** read the CODEOWNERS file (`CODEOWNERS`, `.github/CODEOWNERS`, `.gitlab/CODEOWNERS` or `docs/CODEOWNERS`, the first that exists). The units are the directories on lines whose owners include that handle, compared without case. A glob that matches directories (`/plugins/catalog-*`) expands to them with `ls -d`. A pattern that names files rather than a directory (`*.js`, `/Makefile`) is not a unit; skip it and count how many you skipped. A later CODEOWNERS line overrides an earlier one for the same path, so a directory whose last matching line names other owners is not theirs. If no directory is theirs, print one line saying so, with the handle as you read it, and stop.
2. **Without `--owner`:** the packages its workspace manifest declares: `pnpm-workspace.yaml`, the `workspaces` field of the root `package.json`, `lerna.json`, `go.work`, the `[workspace] members` of the root `Cargo.toml` or `pyproject.toml`, the `include` lines of `settings.gradle(.kts)`, or the `<modules>` of the root `pom.xml`. Expand a glob one level with `ls -d`.
3. **Neither exists:** the repository is one unit. Print one line saying that a team's own folders can be named as paths or with `--owner`, and read it as one.

CODEOWNERS and the workspace manifests are read only to find the units. Nothing in them is an answer in step 3.

**Case 3: otherwise** the folder is `$ARGUMENTS` if it names one, else the current directory, and the list is every **direct child** of that folder which is a git repository, meaning a child directory that holds a `.git`:

```bash
ls -d */.git 2>/dev/null
```

Do not go deeper than one level. A repository nested inside another repository is that repository's business, and a manager who wants it read will say so by name. A shared repository sitting in the folder is read as one unit here; to split it by team, point this at it directly.

If the list is empty, print one line saying that this folder holds no git repositories, name the folder, and stop. Do not go hunting.

Sort the list alphabetically so two runs of the same folder produce the same table.

## 3. The cold read, once per repository

For each unit in the list, answer these five questions. They are `RUN.md` step 2, word for word, and they have to stay that way: the whole value of the number is that it is the same question set the single-repo run is graded on.

1. Where does a new file of this project's main kind go, and what must it look like?
2. Name one tool in the stack and say why it was chosen over the obvious alternative.
3. What naming or code convention would a reviewer here flag first?
4. What is the one thing a change in this repo must never do?
5. What is this project for, in one sentence?

**Answer from exactly this and nothing else:** the repository's top-level directory listing; its `README.md` and any other prose document at the root; and its instruction file, if it has one. Answer from all of it, not only from the instruction file. Most repositories have no instruction file and their agents read the README instead, so a missing one is not a reason to answer WOULD-HAVE-TO-LOOK five times.

The instruction file may be `CLAUDE.md`, `AGENTS.md`, `.cursor/rules` or `.github/copilot-instructions.md`. The last two sit below the root, so checking whether those two paths exist is the only look below the root you get.

**A unit that is a folder inside a repository** is read the same way from its own root: its listing, the `README.md` and other prose documents in it, and its own instruction file if it has one. Add the `CLAUDE.md` or `AGENTS.md` of every folder above it up to the repository root, because an agent working in that folder loads those too. The repository's root README is not one of them: it describes the whole repository, not this team's part of it.

Nothing else: no source file, no config, no other directory. **And never a secret, at any point in this run.** You do not read them, quote them or name their values.

Label each answer **SURE**, **GUESS** or **WOULD-HAVE-TO-LOOK**, the same three labels the single run uses.

`ls`, `cat` and `head` are all you need. Read the whole README only if it is short; the first 200 lines answer these questions or nothing does.

**The score for a repository is how many of the five it answers SURE.** GUESS and WOULD-HAVE-TO-LOOK both score zero, because both mean the agent working in that repository is filling the gap from its training data rather than from the project.

That number is a **ceiling**, and the card says so. The single-repo run grades these answers against the real code afterwards, and grading can only ever turn a SURE into a WRONG, never a GUESS into a right answer. So the true before score is this number or lower.

## 4. Count the contradictions you can see

A contradiction here is one thing only: **a claim in the instruction file or the README that the root listing itself disproves.** It names a file or a folder at the root, and the root listing says that file or folder is not there. A moved entry point, a script that is gone, a folder from a refactor that never happened.

You have not read the code, so that is the only class you can prove, and you count nothing else. No style differences, no stale prose, no suspicion. **Zero is a normal and honest answer**, and the line prints either way.

For a folder unit, the claims are the ones in the files at the folder's own root, and the listing is the folder's. An instruction file above it is shared by every folder below it, so its claims are counted in none of them.

Keep the count per repository, and keep one short phrase for each one, because the manager page prints them.

This deliberately undercounts. The single-repo run reads the code and finds the rest, each with the file and the line. Say that in one line under the table rather than letting the number pass for the whole truth.

## 5. Write the card

Write `ORG_MEMORY_CHECK.md` at the folder root, and print the same thing to the terminal. When the folder is itself a shared repository (step 2, case 2), write it in the repository's parent folder instead, because the folder root is inside the repository. If that write is refused, write no file at all: print the card, and say in one line that it was printed only.

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

For a folder unit, the Repository cell is `<repository>/<path to the folder>`, and the Instruction file cell names the nearest one it loads, with `(from <folder>)` after it when it sits above the unit.

The folder name in the first line is the folder's own name. With `--owner`, it is `<repository> (<handle>)`, so the manager page names the team.

`<M>` is how many units you read, repositories or folders; the card's words stay the same either way so the manager page can read it. `<N>` is how many of them scored 2 or below. `<c>` is the sum of the per-repo contradictions. `<k>` is how many have an instruction file of any of the four names. The last line is a constant: you have checked no hook, no test and no CI gate, and no repository in this folder has been given one by this run.

`Guessing most about` is one of the five questions, said in words, not its number: the one that came back WOULD-HAVE-TO-LOOK in the most repositories. On a tie, take the lowest-numbered question of the tied set, so two runs of the same folder agree.

Under the card, in the file and on the terminal, put these three lines and nothing more:

- A repository's score is how many of the five questions its own visible files answer without a guess. It is a ceiling: the full run grades the answers against the code, and a SURE can come back wrong.
- Contradictions on sight are only the claims the root listing itself disproves. The full run reads the code and finds the rest.
- Nothing here was changed. This was a read.

When the units were folders inside a shared repository, add one more line: `The <M> units are folders inside <repo>, taken from <CODEOWNERS for <handle> / its workspace manifest / your list>, each read as if it were a repository of its own.` With `--owner`, and only when you skipped file patterns, end it with `<n> file patterns were skipped.`

## 6. Print the offer

Last, to the terminal only, written to no file:

```
Paste that card at https://p2p-course.diamant-ai.com/teams?utm_source=github&utm_medium=terminal&utm_campaign=org-card#card to get the manager page for it: the card, the table, and what a team licence costs.
```

Then stop. Do not offer to fix anything, do not start a single-repo run on your own, and do not write into a repository. If the manager wants the layer built, the command is `/agent-memory` inside that repository, or the line in `RUN.md`, and that run stops for their approval before it writes.
