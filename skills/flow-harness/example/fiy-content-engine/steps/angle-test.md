---
id: angle-test
name: Probe the angle on real humans
type: verify
intent: "Find out whether the audience cares about this angle before we spend a draft on it"
delegate_rung: 1
run: human
run_ref: ""
context_packs: [audience-map]
inputs: [research pack, candidate angle]
exit_evidence:
  - "A dated probe: what was posted or asked, where, to whom"
  - "The recorded response — including 'nothing happened', which is a result"
  - "An explicit proceed / drop recommendation with the reason"
verify_with: platform/checks/evidence-check.md
escalate_when: "the probe response is ambiguous two attempts running"
escalate_to: Mary
budget: "30 agent-minutes to design the probe; 20 human-minutes to run it"
measures: [audience-signal, step-cycle-time]
inner_graph: false
---

# Probe the angle on real humans

## Intent

Optional, and skipping it is a decision. We added this step after two fully-drafted pieces
landed flat: the writing was fine, the angle was not wanted. A probe costs an afternoon; a
draft costs a week.

## Exit evidence

- The probe is *dated and located*: "posted in the studio-owners community on 2026-08-04",
  not "we tested it".
- A null result counts. `dropped` with a recorded probe is a cheap win and the meta-loop
  reads it as one.

## Run contract

- **Inputs**: the research pack and the candidate angle in one sentence.
- **Agent's part**: draft two or three probe formulations and the channel for each.
- **Human's part**: post it, talk to people, bring back what actually happened.
- **Guardrails**: never run a probe that reveals unreleased product plans.
- **Stop rule**: one week from posting.

## Delegation & escalation

- **Why rung 1**: the probe is a conversation with real people who know us. That stays
  human — not because an agent could not post, but because the reply is the point.
- **What would promote it**: nothing we want. This is a rung-1 step by choice.
- **What demotes it**: n/a.

## Failure modes

Reading enthusiasm from people who like us as evidence that the market cares. The
`audience-map` pack names who counts as a representative respondent.
