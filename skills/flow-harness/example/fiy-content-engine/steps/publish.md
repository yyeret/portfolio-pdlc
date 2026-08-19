---
id: publish
name: Decide and publish
type: decision
intent: "Make the deliberate call to put our name on this, then ship it"
delegate_rung: 1
run: human
run_ref: ""
context_packs: [audience-map]
inputs: [edited piece, edit verdict, distribution slot]
exit_evidence:
  - "A dated Decision-log entry naming who said publish"
  - "URL, publication date, and channel recorded on the item"
  - "Pre-flight check output attached: links, claims, disclosure, formatting"
verify_with: platform/checks/publish-preflight.md
escalate_when: "the piece touches a customer name, a competitor, or an unreleased feature"
escalate_to: Mary
budget: "20 human-minutes"
measures: [step-cycle-time, throughput]
inner_graph: false
---

# Decide and publish

## Intent

Publishing is a decision, not a task. This step exists so the decision is visible, dated,
and attributable — and so nothing gets published because it happened to be next in a queue.

## Exit evidence

- The Decision log entry names a human. `publish` is a decision point: an item may not
  enter this step without one, and the linter enforces it.
- The pre-flight output is attached. It is boring and it catches the embarrassing things.

## Run contract

- **Agent's part**: assemble the package — final copy, metadata, the pre-flight check
  output, the one-paragraph "what we are claiming and on what basis" summary — and set
  `next_decision` with a date and a name.
- **Human's part**: read the summary, say yes or no, sign the Decision log.
- **Guardrails**: the agent never publishes; the CMS credential is not in its tool set.
- **Stop rule**: n/a — the item waits at `waiting-decision` until a human moves it.

## Delegation & escalation

- **Why rung 1**: not a capability judgement. Our name, our reputation, and a decision that
  a person should be accountable for. This stays human on purpose, and we will not be
  promoting it.
- **What would promote it**: nothing. Say so out loud, so nobody treats it as backlog.

## Failure modes

Decision starvation: the piece sits here, perfectly ready, because the decision forum is
weekly and nobody surfaced it. That is why the loop's first rule is "overdue decision" —
an unmade decision blocks more value than any unstarted piece.
