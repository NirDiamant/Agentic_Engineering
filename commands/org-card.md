---
name: org-card
description: One card for a whole team. Points at a folder of repositories, reads each one cold (the same five questions the single-repo check asks), and prints one org card: how many repos score 2 or below, what your agents guess about most, how many claims in your docs the root listing already disproves. Read-only, writes nothing inside any repository. About two minutes per repo.
tags: [claude-md, memory, docs, org, audit]
---

You are running the Agentic Engineering kit's **org read** across a folder of repositories.

The folder is `$ARGUMENTS` if it names one, else the current working directory. If `$ARGUMENTS` names repositories rather than a folder, those are the list and their common parent is the folder.

## Find the kit's files

The kit ships with this plugin at `${CLAUDE_PLUGIN_ROOT}`. Try to read `${CLAUDE_PLUGIN_ROOT}/ORG.md` first.

If that read is refused (a sandbox or a permission rule that keeps this session inside the folder), do not ask for the permission and do not stop. Clone the kit into the folder instead, where you are allowed to read:

```bash
git clone --depth 1 https://github.com/NirDiamant/Agentic_Engineering <the-folder>/.agentic-engineering-kit
```

Whichever of the two worked is `<this-kit>` below. Say which one you used in one line.

## Run it

Read `<this-kit>/ORG.md` and follow its six steps in order, exactly as written.

The contract in step 1 holds here word for word: every repository is read, none is written to, the only file this command creates is `ORG_MEMORY_CHECK.md` at the folder root, and no secret is opened in any repository at any point.

**Stop before anything that writes into a repository.** The org card is read-only by design. No `cp`, no docs layer, no `AGENT_MEMORY_CHECK.md` inside a repo, no branch, no commit. If the manager wants the layer built in one of these repositories, that is `/agent-memory` inside it, and that run stops for their approval first.

## Clean up

If you cloned the kit into `<the-folder>/.agentic-engineering-kit`, delete that folder after step 6 and say so. It is the kit's own clone, and it is the only thing you delete.
