# Check — amplify audit

**Verifies**: the exit of `amplify`, which runs at rung 4. This check is what makes rung 4
safe, so its failure is a demotion trigger, not a warning.

## What it does

For every scheduled variant:

1. Extract the claim the variant makes.
2. Find it in the published piece.
3. Report `matches` / `drifts stronger` / `not in the piece`.

Plus: no statistic absent from the piece; no customer @-mention; every item scheduled inside
the connector queue; dates inside the three-week window.

## Output

An audit table in `items/<slug>/amplify-plan.md`, and the pass/fail in the item's
`## Exit evidence log`.

## Escalation

Any `drifts stronger` or `not in the piece` finding: **do not schedule**. Escalate to Dana
with the variant and the finding. Two escapes in a month demotes `amplify` to rung 3 —
that rule is written in `steps/amplify.md` so nobody has to argue about it later.
