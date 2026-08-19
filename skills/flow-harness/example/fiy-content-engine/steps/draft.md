---
id: draft
name: Draft the piece
type: transform
intent: "Turn the evidenced angle into a publishable draft in our voice"
delegate_rung: 2
run: prompt
run_ref: platform/prompts/draft.md
context_packs: [house-voice, product-truths]
inputs: [research pack, angle evidence]
exit_evidence:
  - "Draft at items/<slug>/draft.md where every claim traces to the research pack"
  - "House-voice check run, with its findings resolved or waived with a stated reason"
  - "Open questions for the editor listed explicitly rather than smoothed over"
verify_with: platform/checks/house-voice.md
escalate_when: "two rework passes without converging, or the angle stops holding up while writing"
escalate_to: Dana
budget: "60 agent-minutes; 30 human-minutes"
measures: [rework-rate, human-minutes-per-item]
inner_graph: true
---

# Draft the piece

## Intent

Writing is where the thinking finishes. If the draft cannot be written without inventing a
claim, the research was not done — and the honest move is the back-edge, not a smoother
sentence.

## Exit evidence

- Every claim is traceable. The draft carries inline markers to the source table.
- The house-voice check has been run *by the agent* and its findings are either fixed or
  waived with a reason a human can disagree with.
- The "open questions" list is not empty on a first draft. An empty list means the drafter
  smoothed over something.

## Inner graph

The step has three distinct failure modes — wrong structure, invented claims, wrong voice —
so it runs its own bounded loop rather than one long generation:

```
<!-- step-graph
nodes: outline, expand, self-critique, revise, citation-check
entry: outline
edges:
  outline -> expand
  expand -> self-critique
  self-critique -> revise      [when: findings exist]
  self-critique -> citation-check
  revise -> self-critique      [rework]
  citation-check -> exit
max_iterations: 2
-->
```

`max_iterations: 2` on the revise loop is not a budget cap, it is a truth cap: past two
passes the loop stops finding problems and starts polishing prose that nobody has agreed
is right yet. Two passes, then out to a human.

## Run contract

- **Inputs**: the research pack, the angle evidence, the `house-voice` pack.
- **Tools allowed**: read the item folder and the context packs; write only `draft.md`.
- **Guardrails**: no claim that is not in the research pack — if the draft needs one, stop
  and send the item back to `research` across the rework edge.
- **Stop rule**: the inner graph's `max_iterations`, or 60 minutes.
- **Artifacts written**: `items/<slug>/draft.md`.

## Delegation & escalation

- **Why rung 2**: the agent drafts well and edits itself badly. Dana is the editor of
  record, and that is the whole design.
- **What would promote it**: a house-voice check that catches what Dana catches — measured
  by comparing the check's findings against her edit findings over 10 items.
- **What demotes it**: a claim reaching `publish` that was not in the research pack.

## Failure modes

Fluency. A draft can be entirely well-formed, on-voice, and quietly wrong. The citation
markers exist so the editor reads *for sources*, not for style.
