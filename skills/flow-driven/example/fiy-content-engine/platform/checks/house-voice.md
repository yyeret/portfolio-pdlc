# Check — house voice

**Verifies**: the exit of `draft`. **Independent of**: the drafting pass — fresh context,
rules only, no access to the drafter's reasoning.

## What it does

Reads `platform/context/house-voice.md` and the draft, and reports per rule:

| Rule | Finding | Location |
|---|---|---|
| Name the number or drop the claim | every "most/many/some studios" without a figure | line refs |
| Second person, present tense | passive or third-person passages | line refs |
| No throat-clearing | any opening that describes the industry | line refs |
| Concede the counter-argument | is the strongest objection answered in the body? | yes/no |
| Spelling, comma, no exclamation marks | mechanical | line refs |

## Output

Findings with dispositions on the item: **fixed**, or **waived with a reason**. A waiver is
legitimate; a silent dismissal is not.

## Known limitation

This check catches roughly what Dana catches on rules 1, 2, 3 and 5, and misses rule 4
about half the time. That gap is the reason `draft` is rung 2 rather than 3 — see
`improvements/promote-draft-to-run/`.
