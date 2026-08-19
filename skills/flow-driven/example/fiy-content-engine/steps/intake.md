---
id: intake
name: Triage the question
type: intake
intent: "Decide whether a recurring question from the field is worth finding out about"
delegate_rung: 2
run: prompt
run_ref: platform/prompts/intake-triage.md
context_packs: [audience-map]
inputs: [support themes, sales-call notes, community threads]
exit_evidence:
  - "Item card exists with a named source (person, ticket, or thread — not 'the team')"
  - "Outcome hypothesis written as a change in what a studio owner believes or does"
verify_with: ""
escalate_when: "the question is really about the product roadmap, not content"
escalate_to: Dana
budget: "15 agent-minutes; 5 human-minutes"
measures: [item-age, escalation-rate]
inner_graph: false
---

# Triage the question

## Intent

Most content dies here and should. This step exists to convert a vague "we should write
about X" into either a card with a named source and a hypothesis, or a "no" we can point
at later.

## Exit evidence

- The card names a source we could go back to: a ticket number, a call, a thread.
- The outcome hypothesis is about the reader, not about us. "Studio owners stop treating
  churn as a pricing problem" passes. "We establish thought leadership" does not.

## Run contract

- **Inputs**: last 30 days of support themes, the sales-call digest, the community digest.
- **Tools allowed**: read-only access to the digests; write access only to `items/`.
- **Guardrails**: never create more than three cards in one run — a flooded intake is how
  this stream stopped flowing last time.
- **Stop rule**: three candidates, or the digests are exhausted.
- **Artifacts written**: `items/<slug>/item.md`.

## Delegation & escalation

- **Why rung 2**: the agent is good at spotting recurring questions and bad at knowing
  which ones we have already answered badly. Dana keeps the final say for now.
- **What would promote it**: a context pack of everything we have already published, with
  how each performed. Then the agent could reject duplicates itself.
- **What demotes it**: two cards in a month that duplicate a published piece.

## Failure modes

Enthusiasm. The agent will find infinite candidate questions, all plausible. The named
source is the antidote: no source, no card.
