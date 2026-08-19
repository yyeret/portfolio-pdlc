# Check — evidence check

**Verifies**: the exit of `research` and `angle-test`. **Independent of**: the runner that
built the pack (run it in a fresh context, with the sceptic's brief below).

## What it does

For each claim in the research pack:

1. Open the cited source. Read the passage, not the summary.
2. Answer: does the source say the claim, say something narrower, or not say it?
3. Mark: `supports` / `narrower` / `does not support` / `source unreadable`.

For the pack as a whole:

- Is there at least one primary source (a customer said it, a ticket shows it, product data
  measures it)?
- Are opinions labelled as opinions?
- Is any claim about our product outside `platform/context/product-truths.md`?

For an `angle-test` exit: is the probe dated and located, is the response recorded
including a null result, and is there an explicit proceed/drop call?

## Output

A findings table appended to the item's `## Exit evidence log`. **Findings of "none" must
still be recorded** — a check with no output is indistinguishable from a check that never ran.

## The sceptic's brief

You are not helping the writer. Your job is to find the claim that will embarrass us. If
you find nothing, say what you looked at, so the next reader can tell the difference between
a clean pack and a lazy check.
