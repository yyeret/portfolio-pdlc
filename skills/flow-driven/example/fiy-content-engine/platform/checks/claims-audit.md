# Check — claims audit

**Verifies**: the exit of `edit`. **Independent of**: whoever wrote the draft, and it may
not be resolved by the agent that produced the claims.

## What it does

1. Extract every factual claim in the edited piece — including the ones inside hooks,
   captions, and the summary.
2. Trace each to a row in the research pack's source table.
3. Report: `traced` / `traced but overstated` / `untraced`.
4. Separately list every claim about our product and check it against
   `platform/context/product-truths.md`, including expiry dates.

## Output

The full table attached to the item, plus a one-line count in the `## Exit evidence log`.
The editor's verdict (publish / rework / drop) goes next to it.

## Why this one is strict

`edit` is the last step where a wrong claim is cheap. `traced but overstated` is the most
common finding and the easiest to wave through: the source says "in a sample of 340
studios", the piece says "studios". Those are different sentences.
