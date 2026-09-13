# CONVENTIONS: {{PROJECT_NAME}}

<!-- fill: the single pattern this project follows everywhere. The AI reads this every
     session, so when you say "add a feature" it builds in your style instead of
     inventing a new one each time. Fill the blanks for your stack and delete what
     doesn't apply. A convention you don't keep is a wish, so this stays short. -->

The single pattern this project follows everywhere.

## Naming

- **Files:** {{kebab-case? snake_case? Show one example.}}
- **{{Components / classes}}:** {{PascalCase? Show one example.}}
- **Functions and variables:** {{camelCase? snake_case?}}
- **Constants:** {{UPPER_SNAKE_CASE?}}
- **Booleans:** prefix with `is` / `has` / `should` so intent reads at a glance.

## Code patterns

<!-- fill: the recurring shape decisions for your stack. One line each. -->

- {{Your default unit: one component/module per file, named the same as the file?}}
- {{Where types or interfaces live relative to the code that uses them.}}
- {{When something gets split: "if describing it needs the word 'and', split it".}}
- {{Where shared code lives, and what earns promotion into it.}}

## Style

<!-- fill: these are common defaults, not law. Keep the ones that match how this
     project is actually written, delete the rest, add your own. The AI follows them
     literally, so don't state a rule you won't hold. (Working principles that apply to
     every project live in CLAUDE.md, not here.) -->

- One responsibility per function.
- No dead code, no commented-out blocks. Delete it; git remembers.
- Comments explain **why**, never **what**. The code already says what.
- Validate at the boundary (a form, a request, anything from outside); trust internal calls.
- {{Import grouping or ordering, if you care.}}
- {{Styling approach: utility classes, CSS modules, or something else.}}
