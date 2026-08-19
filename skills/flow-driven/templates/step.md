---
id: <step-id>
name: <Human-readable step name>
type: transform          # intake | transform | decision | verify | wait | measure
intent: "<what this step is for, in one sentence>"
delegate_rung: 1         # 0 human only · 1 assists · 2 drafts · 3 runs · 4 checked · 5 automated
run: human               # skill | prompt | script | tool | human | external
run_ref: ""              # the skill name, prompt file, script path, tool, or system
context_packs: []        # platform/context/<pack>.md — what the runner needs to know
inputs: []               # what must exist before this step can start
exit_evidence:
  - "<the artifact or observation you can rely on when an item leaves here>"
verify_with: ""          # a check independent of the runner — script > second agent > nothing
escalate_when: "<the condition under which the runner stops and asks a human>"
escalate_to: <name>
budget: "<agent time/cost and human time this step is worth>"
measures: []             # ids from measures.md
inner_graph: false
---

# <Step name>

## Intent

<Why this step exists in the flow. What would go wrong if items skipped it — and if the
answer is "nothing", delete the step.>

## Exit evidence

Each line is checkable by someone who did not do the work:

- <artifact exists at a named place, containing a named thing>
- <a check was run and its findings are recorded — including "none">

Anti-evidence, for calibration: "reviewed", "looks good", "done", "no issues found" with
nothing showing what was looked at.

## Inner graph

<Delete this section unless `inner_graph: true`. A step earns an inner graph when it has
more than one distinct failure mode, or when its verify is separable from its work.>

```
<!-- step-graph
nodes: <a>, <b>, <c>
entry: <a>
edges:
  <a> -> <b>
  <b> -> <c>          [when: findings exist]
  <c> -> <b>          [rework]
  <b> -> exit
max_iterations: 2
-->
```

## Run contract

- **Inputs**: <what the runner reads>
- **Tools allowed**: <the smallest set that works>
- **Guardrails**: <what it must not do — write to production, contact a customer, spend
  beyond budget>
- **Stop rule**: <iteration cap, budget cap, or the falsifiable condition that ends the run>
- **Artifacts written**: <where output lands>

## Delegation & escalation

- **Why this rung**: <blast radius, reversibility, and the evidence we have so far>
- **What would promote it**: <the check, context pack, or track record that makes the next
  rung safe>
- **What demotes it**: <the escape rate or failure that sends it back down — write this
  before you need it>

## Failure modes

<How this step lies to you. Fluent output with no substance; a check that always passes;
an input that is silently stale; a human rubber-stamp. Name them so the meta-loop can look
for them.>
