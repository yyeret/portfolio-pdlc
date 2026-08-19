---
id: amplify
name: Distribute and repeat
type: transform
intent: "Put the published piece in front of the audience more than once, in their formats"
delegate_rung: 4
run: tool
run_ref: platform/prompts/amplify-plan.md
context_packs: [house-voice, audience-map]
inputs: [published URL, audience map]
exit_evidence:
  - "A scheduled distribution plan with per-channel variants and dates"
  - "Amplify audit passed: no claim drift between the piece and any variant"
verify_with: platform/checks/amplify-audit.md
escalate_when: "a variant needs a claim that is not in the published piece"
escalate_to: Dana
budget: "30 agent-minutes; 0 human-minutes by design"
measures: [cost-per-item, throughput]
inner_graph: false
---

# Distribute and repeat

## Intent

Publishing once is not distribution. This step turns one piece into the six touches it
takes for a busy studio owner to notice it.

## Exit evidence

- The plan exists with dates and per-channel variants, scheduled — not "will schedule".
- The amplify audit compares every variant against the published piece and reports claim
  drift. A variant that overstates the piece is the failure mode this step actually has.

## Run contract

- **Inputs**: the published URL, the audience map, the house-voice pack.
- **Tools allowed**: the scheduling connector, write access to the plan file.
- **Guardrails**: never post outside the scheduled queue; never invent a statistic for a
  hook; never @-mention a customer without a human.
- **Stop rule**: the plan is scheduled and the audit is clean, or it escalates.

## Delegation & escalation

- **Why rung 4**: high volume, low blast radius, fully reversible in a minute, and an
  automated check that catches the one thing that goes wrong (claim drift). Promoted on
  2026-08-03 after 12 consecutive clean runs — the bet is recorded in
  `improvements/promote-amplify-to-checked/`.
- **What demotes it**: two audit escapes in a month, or one variant that made a claim the
  piece did not.

## Failure modes

Claim inflation in the hook. Short formats reward overstatement, and an agent optimising
for engagement will find that gradient on its own. The audit is the guardrail; watch it.
