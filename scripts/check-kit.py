#!/usr/bin/env python3
"""Checks the kit itself, for the three ways it has actually broken.

Every check here exists because the thing it checks for really happened on
2026-09-13, not because it seemed like a good idea:

1. `skills/testify/SKILL.md` shipped with frontmatter that does not parse as
   YAML, so the skill could not load at all. It arrived that way in da4d9c3
   and nothing caught it for as long as it sat there.
2. The templates were built out of em dashes, so filling one faithfully wrote
   twelve of them into a visitor's repository. The rule against them lived in
   the procedure text while the templates quietly broke it.
3. The card gained a line and two sessions then disagreed about whether it has
   six or seven, which is one careless edit away from dropping the line.

It also checks that the four guarantees say the same thing in both places they
are written, because they are the product's whole trust mechanism and they are
duplicated, which is how promises drift.

No dependencies beyond the standard library. Run it from the repo root:

    python3 scripts/check-kit.py
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FAILURES = []
CHECKED = []


def fail(what, detail):
    FAILURES.append(f"{what}: {detail}")


def ok(what):
    CHECKED.append(what)


# Everything under these paths lands verbatim in a stranger's repository.
COPIED_INTO_VISITOR_REPO = ["docs", ".claude"]


def check_frontmatter():
    """A skill or command whose frontmatter does not parse cannot load."""
    files = sorted(ROOT.glob("skills/*/SKILL.md")) + sorted(
        ROOT.glob(".claude/commands/*.md")
    )
    if not files:
        fail("frontmatter", "found no SKILL.md or command files to check")
        return
    for f in files:
        text = f.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue  # commands may legitimately have no frontmatter
        parts = text.split("---", 2)
        if len(parts) < 3:
            fail("frontmatter", f"{f.relative_to(ROOT)} opens --- and never closes it")
            continue
        block = parts[1]
        try:
            import yaml  # type: ignore

            yaml.safe_load(block)
        except ImportError:
            # No PyYAML here, so check the one failure mode we have actually hit:
            # a plain (unquoted) scalar cannot contain ": ".
            for line in block.splitlines():
                m = re.match(r"^(\w[\w-]*):\s+(.*)$", line)
                if not m:
                    continue
                value = m.group(2)
                if value[:1] in "\"'|>[{":
                    continue  # quoted or block scalar, the colon is safe there
                if ": " in value:
                    fail(
                        "frontmatter",
                        f"{f.relative_to(ROOT)} key '{m.group(1)}' is a plain scalar "
                        f"containing ': ', which YAML rejects. Quote it or reword it.",
                    )
        except Exception as e:  # noqa: BLE001 - any parse error is the failure
            first = str(e).splitlines()[0]
            fail("frontmatter", f"{f.relative_to(ROOT)} does not parse: {first}")
    ok(f"frontmatter parses in {len(files)} skill and command files")


def check_no_em_dash():
    """Nir's standing rule, applied where it actually reaches a stranger."""
    targets = [ROOT / "RUN.md", ROOT / "README.md"]
    for d in COPIED_INTO_VISITOR_REPO:
        targets.extend(sorted((ROOT / d).rglob("*.md")))
    hits = []
    for f in targets:
        if not f.is_file():
            continue
        for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if "—" in line:
                hits.append(f"{f.relative_to(ROOT)}:{i}")
    if hits:
        fail(
            "em dash",
            f"{len(hits)} in files that land in a visitor's repo: "
            + ", ".join(hits[:5])
            + (" ..." if len(hits) > 5 else ""),
        )
    else:
        ok(f"no em dash in {len(targets)} files that reach a visitor")


def check_card_shape():
    """The card is the artifact. A dropped line is a silently weaker product."""
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    start = readme.find("AGENT MEMORY CHECK:")
    if start == -1:
        fail("card", "README.md has no example card at all")
        return
    end = readme.find("Still advisory", start)
    if end == -1:
        fail("card", "the card in README.md has no 'Still advisory' closing line")
        return
    card = readme[start:end].splitlines()
    required = [
        "AGENT MEMORY CHECK:",
        "Before the docs layer:",
        "After:",
        "It was guessing about:",
        "Contradictions found in your existing docs:",
        "Written:",
    ]
    for want in required:
        if not any(line.startswith(want) for line in card):
            fail("card", f"the card in README.md is missing its '{want}' line")
            return
    if len(card) != len(required):
        fail("card", f"the card has {len(card)} lines before 'Still advisory', expected {len(required)}")
        return
    ok("the card in README.md is the full seven-line shape")


def check_guarantees_match():
    """The four guarantees are written twice and must not drift apart."""

    def guarantees(path):
        """The four bullets ending in the one that promises the time.

        Found by structure, not by verb: RUN.md writes them in the first person
        ("I write") and README.md in the third ("It writes"), and the last one
        has no verb at all in the README ("About fifteen minutes."). Matching on
        verbs is how the first version of this check reported a drift that was
        not there.
        """
        lines = (ROOT / path).read_text(encoding="utf-8").splitlines()
        anchor = None
        for i, line in enumerate(lines):
            if line.lstrip().startswith("-") and "fifteen minutes" in line:
                anchor = i
                break
        if anchor is None:
            return []
        block = []
        i = anchor
        while i >= 0 and lines[i].lstrip().startswith("-"):
            block.insert(0, lines[i].lstrip("- ").strip())
            i -= 1
        return block

    run = guarantees("RUN.md")
    readme = guarantees("README.md")
    if len(run) != 4:
        fail("guarantees", f"RUN.md has {len(run)} of the 4 guarantee lines, not 4")
        return
    if len(readme) != 4:
        fail("guarantees", f"README.md has {len(readme)} of the 4 guarantee lines, not 4")
        return
    # Compare the load-bearing nouns rather than the wording, which differs by person.
    for i, (a, b) in enumerate(zip(run, readme), 1):
        for noun in ("docs/", ".claude/commands/", "scorecard", "approval", "fifteen minutes"):
            if (noun in a) != (noun in b):
                fail(
                    "guarantees",
                    f"guarantee {i} mentions '{noun}' in one file and not the other. "
                    f"RUN.md: {a!r} README.md: {b!r}",
                )
                return
    ok("the four guarantees agree between RUN.md and README.md")


def main():
    check_frontmatter()
    check_no_em_dash()
    check_card_shape()
    check_guarantees_match()

    for line in CHECKED:
        print(f"  ok    {line}")
    for line in FAILURES:
        print(f"  FAIL  {line}")
    if FAILURES:
        print(f"\n{len(FAILURES)} check(s) failed.")
        return 1
    print(f"\nAll {len(CHECKED)} checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
