---
id: learn
name: Read the result
type: measure
intent: "Compare what the outcome hypothesis predicted against what actually happened"
delegate_rung: 3
run: prompt
run_ref: platform/prompts/learn-readout.md
context_packs: [audience-map]
inputs: [published piece, outcome hypothesis, channel analytics, replies]
exit_evidence:
  - "A dated readout: hypothesis vs what happened, with the numbers and the qualitative signal"
  - "An explicit call: confirmed, disconfirmed, or inconclusive — and what we would do differently"
  - "If the readout raises a new question, a new intake card exists (a NEW item, not this one)"
escalate_when: "the result contradicts something in the audience-map pack"
escalate_to: Dana
budget: "40 agent-minutes; 15 human-minutes"
measures: [throughput]
inner_graph: false
---

# Read the result

## Intent

Without this step the stream is a publishing calendar. With it, the stream learns — and the
`audience-map` context pack gets better, which makes every future item cheaper.

## Exit evidence

- The readout names the hypothesis it is testing, in the words the card used at intake.
- "Inconclusive" is a legitimate call and should be the answer more often than it is.
- A learning that changes what we believe about the audience updates `platform/context/
  audience-map.md` — that is the platform compounding, and it is the point.

## Run contract

- **Inputs**: analytics for the piece, replies and comments, the original card.
- **Tools allowed**: read analytics; write the readout and, with a human's nod, the
  audience-map update.
- **Guardrails**: never attribute a business outcome to one piece; say "consistent with"
  and mean it.
- **Stop rule**: 14 days after publication, whatever the data looks like.

## Delegation & escalation

- **Why rung 3**: reading numbers against a stated hypothesis is well within reach; deciding
  what it means for positioning is not.
- **What would promote it**: an independent check on the readout — which we have not built,
  and which is why the linter warns about this step. That warning is correct and we are
  leaving it visible.
- **What demotes it**: a readout that claimed a result the numbers did not support.

## Failure modes

Retrofitting the hypothesis to the result. The card's original wording is quoted verbatim
in the readout so the comparison stays honest.
