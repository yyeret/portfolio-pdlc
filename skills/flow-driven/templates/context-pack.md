---
id: <pack-id>
name: <what this pack knows>
used_by: []              # step ids that load it
owner: <human who keeps it true>
reviewed: <YYYY-MM-DD>
source: <where this knowledge came from — a person, a doc, a decision>
---

# Context pack: <name>

The platform play in one file. Every time a human answers the same question for an agent,
that answer belongs here — after which the next run does not need the human.

## What a runner can rely on from this pack

<The knowledge itself: rules, examples, vocabulary, constraints, the shape of "good". Write
it for a competent stranger, not for someone who already knows.>

## Worked examples

| Situation | Good | Not good | Why |
|---|---|---|---|
| <case> | <example> | <example> | <the distinction that matters> |

Examples beat adjectives. Two contrasting pairs teach more than a page of principles.

## Boundaries

<What this pack does NOT cover — where the runner must escalate instead of extrapolating.>

## Provenance & freshness

- **Where this came from**: <person, decision, artifact>
- **How we know it is still true**: <the signal that would tell us it has rotted>
- **Review cadence**: <when someone re-reads it>

Stale context is worse than missing context: missing context makes an agent ask, stale
context makes it confident.

## Change log

| Date | Change | Why |
|---|---|---|
