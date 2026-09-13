# Why This Works

> The thinking under every template in this repo. Five minutes, and the spec layer stops being a folder of markdown and starts being an engineering decision.

## English is the new coding language. Minus three things.

You've heard the idea: describe what you want and the machine builds it. It's half true, and the missing half is the half that matters.

A real programming language gives you three things. **Grammar**: a line has exactly one way to be read. **Unambiguity**: one statement, one meaning. **Determinism**: same input, same result, every run. Those three are the entire reason software is reliable, and the English you type into an AI tool has none of them. Loose grammar, ambiguity by design, and the same sentence can produce two different programs on two runs.

That gap is why AI projects feel like magic for an hour and fall apart by midnight. Supplying the three properties back is a discipline, and the discipline has a name: **agentic engineering**, engineering the system around the agent, not only the prompts into it. The spec layer is that system's foundation.

## Context is the new code

The model has no memory of your project between sessions. It starts each one cold and rebuilds its whole picture from whatever is in its **context window** right now. So if your intent lives in English and the model writes the code, the thing you're actually building is the context. Watch how much one line does:

```
"store the users"
  → no context:   an in-memory array, fine for a demo
  → + one line:   "this is a production service, expect a million rows"
  → with context: a Postgres table, indexed on the lookup column
```

All three outputs are correct, and the model knows all three. Your context is the sentence that tells it which project it's in. The model has already seen every framework and every way a thing breaks; you're not teaching it, you're pruning its cloud of valid possibilities down to the one you meant. Which is why over-explaining backfires: a page explaining what React is prunes nothing and competes for attention with the lines that do. Encode only the choices that are yours. The model brings the rest.

## The spec leads

Two things define the new division of labor. You architect, the model writes the code. And when your spec and your code disagree, the spec is the truth. The naive move is to trust the code because it runs; then the spec rots, and soon nobody, including the model, knows what the project is supposed to do, only what it does. Here's the mechanical reason:

```js
function calculateTax(amount) {
  return amount * 0.05   // wrong: the rate should be 0.07
}

test("calculates tax", () => {
  expect(calculateTax(100)).toBe(5)   // passes. and it's wrong.
})
```

The test passes because its expected value was read off the broken code. You can't recover the goal from the code; the right value has to come from a statement of what the result *should* be. That statement is the spec, and the deterministic scaffolding that enforces it (rules, tests, gates) is the **harness**. It starts as plain files, which is what this repo gives you.

## Walls over freedom

The obvious move is one big instructions file, because more rules feel like more control. But an always-loaded file is re-read every turn, so the model reads your visual conventions while fixing a backend bug, and irrelevant rules compete with the ones that apply. The fix is counterintuitive: more walls, not more freedom. A wall is a boundary around one concern; every wall you raise is one more place the model no longer has to guess.

| File                    | What lives here                                   |
|-------------------------|---------------------------------------------------|
| `CLAUDE.md`             | how the AI should ACT: behavior, constraints      |
| `docs/DESIGN.md`        | how things should LOOK: visual language, layout   |
| `docs/HANDOFFS.md`      | how agents work together: handoffs, orchestration |
| `docs/context/log.md`   | what you discover: decisions, gotchas, facts      |

Those four are **the four walls**, the starting set, not the final list. The table is the shape of the method, not an inventory of your repo: a lean `/apply` run writes only two of them, the root instruction file and the log. You split along these lines because the concerns drift at different speeds (behavior hardens slowly, gotchas grow weekly), and lining the file boundary up with the change boundary means an edit to the fast concern can't quietly break the slow one. One caveat: when two walls disagree, neither outranks the other and the model picks the likelier reading, which is the non-determinism you're trying to remove. Set precedence yourself when it matters, in the wall that owns the decision.

## This has a name

Writing intent into files the model builds from is **spec-driven development**: the spec files are the source of truth, the code is generated from them. The four walls are your project's **constitution** (the durable rules every build obeys), and `OVERVIEW.md`, kept free of technology, is your **spec**. Keep the what/why apart from the how, because the what survives a stack change and the how gets rewritten the day you swap your database.

## Wire it in

The part people miss: a file sitting in your repo is not in the model's context window. A `DESIGN.md` nothing points to has zero effect, no matter how good it is. You wire each file in by reference from the one always-loaded file, and that wiring block in [`CLAUDE.md`](../CLAUDE.md) (its "Project context" section) is the difference between owning a pile of markdown and owning a working system.

So: grammar comes back by structuring what the model reads, unambiguity by pruning to the one thing you meant, and determinism, the hardest, you buy back with the harness, layer by layer, starting with these files. None of it expires with the next model release, because it's how these systems work underneath. Stop blaming the model. Start engineering the context.