---
id: research
name: Build the evidence base
type: transform
intent: "Assemble what we actually know, and mark honestly what we only believe"
delegate_rung: 3
run: prompt
run_ref: platform/prompts/research-pack.md
context_packs: [audience-map, product-truths]
inputs: [item card, prior published pieces, customer calls, product data]
exit_evidence:
  - "Research pack at items/<slug>/research-pack.md with at least three sources"
  - "At least one primary source: a customer call, a ticket thread, or product data"
  - "Every claim we intend to make is mapped to a source, or marked as opinion"
verify_with: platform/checks/evidence-check.md
escalate_when: "the strongest claim rests only on our own prior content"
escalate_to: Dana
budget: "90 agent-minutes; 10 human-minutes"
measures: [step-cycle-time, evidence-coverage]
inner_graph: false
---

# Build the evidence base

## Intent

The difference between content that moves people and content that fills a calendar is
whether it says something the writer actually knows. This step is where knowing happens.

## Exit evidence

- `research-pack.md` exists, with a source table: claim → source → primary/secondary →
  date.
- Opinions are labelled `opinion`. An unlabelled opinion that reaches `draft` is the most
  expensive defect this stream produces, because it is invisible until a reader catches it.

## Run contract

- **Inputs**: the item card, the searchable archive of customer calls, the product metrics
  the `product-truths` pack points at.
- **Tools allowed**: read across the research corpus; write only into the item folder.
- **Guardrails**: never cite a source it has not read; never cite us as evidence for us.
- **Stop rule**: three sources including a primary, or 90 minutes, whichever comes first —
  then escalate with what it has.
- **Artifacts written**: `items/<slug>/research-pack.md`.

## Delegation & escalation

- **Why rung 3**: retrieval and mapping are genuinely good; the judgement of "is this
  enough to say that out loud" is not yet. The evidence check catches the common failure.
- **What would promote it**: an automated primary-source check plus 10 items with no
  claims added at `edit`.
- **What demotes it**: one published claim traced to a source that did not say it.

## Failure modes

The confident summary of a source that says something narrower. The check reads the source
and the claim side by side for exactly this reason.
