---
name: agent-memory
description: Give this repo a memory. Reads the real code, writes CLAUDE.md and a small docs layer from it, grades the repo 0 to 5 before and after, lists the claims in your own docs the code contradicts. Deletes nothing, overwrites nothing, stops once for approval. About fifteen minutes.
tags: [claude-md, memory, docs, setup]
---

You are running the Agentic Engineering kit on the repository you are already working in. The kit is installed as a plugin, so it is not a clone in a temp folder: it lives at `${CLAUDE_PLUGIN_ROOT}`.

Read `${CLAUDE_PLUGIN_ROOT}/RUN.md` and follow its seven steps in order on this repository, exactly as written, with one binding: every place RUN.md says `<this-kit>`, that path is `${CLAUDE_PLUGIN_ROOT}`. So the copy in step 3 is

```bash
cp -Rn ${CLAUDE_PLUGIN_ROOT}/docs ${CLAUDE_PLUGIN_ROOT}/.claude <their-repo>/
```

and the procedure in step 3 is `${CLAUDE_PLUGIN_ROOT}/.claude/commands/apply.md`, read in full.

Everything you write goes into this repository, never into the plugin folder. The contract in step 1 of RUN.md (what is written, that nothing of theirs is deleted or overwritten, the one stop for approval) holds here word for word. If $ARGUMENTS names a different repository path, run on that path instead of the current one.
