# Performance intervention PDLC

One item is a bet on a measurable change in how a named group performs real work. It may change a policy, process, team practice, decision, skill, tool, or automation. The setting, affected group, and performance gap define the work. Scope the first test to one group and one outcome.

The intended result is a sustained improvement that an operating owner can maintain. A disconfirmed or superseded bet ends with a recorded decision and its evidence.

<!-- flow-config
id: performance-interventions
kind: performance-intervention
unit: one bounded intervention to improve a named group's performance in real work
unit_outcome: the affected group sustains a measured improvement and its operating owner can maintain it
steps: intake, triage, discovery, design, probe, pilot, rollout, adoption, outcome-review
optional_steps: probe
entry: intake
terminal: sustained, stopped, superseded
edges:
  intake -> triage
  triage -> discovery [when: in remit and worth discovery]
  triage -> stopped [when: sponsor or flow owner closes or redirects]
  discovery -> design [when: evidence justifies pursuing the opportunity]
  discovery -> stopped [when: sponsor declines further investment]
  design -> probe [when: a consequential uncertainty needs a cheap test]
  design -> pilot [when: sponsor approves a real-work trial and documents why a probe adds little]
  design -> stopped [when: sponsor declines the next investment]
  design -> superseded [when: sponsor approves a materially different bet]
  probe -> pilot [when: test supports proceeding and sponsor approves the trial]
  probe -> stopped [when: sponsor ends the bet]
  probe -> superseded [when: sponsor approves a materially different bet]
  pilot -> rollout [when: sponsor approves rollout on the strength of pilot evidence]
  pilot -> stopped [when: sponsor ends the trial and signs the closeout]
  pilot -> superseded [when: sponsor approves a materially different bet and signs the closeout]
  rollout -> adoption
  rollout -> stopped [when: sponsor ends a rollout and signs the closeout]
  rollout -> superseded [when: sponsor approves a materially different bet and signs the closeout]
  adoption -> outcome-review [when: the planned adoption window ends or a guardrail triggers review]
  outcome-review -> sustained [when: the outcome and adoption bars hold and the operating owner accepts handover]
  outcome-review -> stopped [when: sponsor ends the bet and signs the closeout]
  outcome-review -> superseded [when: sponsor approves a materially different bet and signs the closeout]
wip_limits: triage=5, discovery=3, design=3, probe=2, pilot=2, rollout=2, adoption=2, outcome-review=2
aging_thresholds: intake=14, triage=7, discovery=14, design=14, probe=14, pilot=28, rollout=21, adoption=35, outcome-review=14
decision_points: pilot, rollout
evidence_exits: intake, triage, discovery, design, probe, pilot, rollout, adoption, outcome-review
cadence: weekly flow review, on-demand investment decisions, monthly outcome and portfolio review
-->

## States and suggested skills

| State | Outcome someone can rely on | Suggested skill or method |
|---|---|---|
| [Intake](steps/intake.md) | A requester and affected group can point to a concrete gap in real work. | `intent-framing-chooser`, intake interview |
| [Triage](steps/triage.md) | Someone can explain whether the gap warrants discovery and who will own it. | Duplicate and existing-capability check, `sniff-test` for a developed initiative |
| [Discovery](steps/discovery.md) | Affected workers recognise the problem, and the sponsor can judge its size and plausible causes. | Work observation, process mapping, `intent-framing-chooser` |
| [Design](steps/design.md) | The team knows what change to try, what it could cost, and what evidence would change the decision. | Options comparison, causal hypothesis, measurement and test design |
| [Probe](steps/probe.md) | A cheap test has reduced uncertainty about the riskiest assumption. | Prototype, simulation, or process rehearsal |
| [Pilot](steps/pilot.md) | A bounded group has used the change in real work and the sponsor can judge the evidence. | Controlled trial, field observation, error and exception analysis |
| [Rollout](steps/rollout.md) | The intended group can use the change and knows where to get support. | Staged rollout, readiness review, rollback rehearsal |
| [Adoption](steps/adoption.md) | There is a defensible read on repeated use, gaps by cohort, and the team's ability to carry the change. | Adoption cohort analysis, workflow observation, teach-back |
| [Outcome review](steps/outcome-review.md) | The sponsor can decide on sustained operation, a bounded extension, a pivot, or a stop. | Outcome and cost review, `flow-driven-run` decision brief |
| Sustained / Stopped / Superseded | Ownership and monitoring are accepted, the work is closed, or a successor bet is ready for intake. | Decision log and handover or closeout record |

## Operating policy

**Intake and roles.** Pull from requests by affected workers, managers, or improvement champions, and from observed performance gaps with a named source. A named person owns the card from intake. The sponsor owns investment and stop decisions, the item owner carries the evidence, the operating owner takes responsibility for the practice in use, and the flow owner facilitates the weekly review. Affected workers judge whether the change works in practice. Roles can overlap. The verifier must be independent of the work being checked.

**Pull and review.** Walk the board right to left weekly, clear waiting decisions and blockers, and pull only into available capacity. Intake is an unbounded queue. WIP limits are starting counts and ages are review triggers in calendar days. Use on-demand sponsor decisions before exposing a cohort or spending on wider rollout. Review outcomes when their evidence windows mature or a guardrail trips. Review portfolio patterns and operational follow-ups monthly.

**Decision boundaries.** Before entering pilot or rollout, record today's date, the named sponsor, the exact transition approved, scope, evidence, guardrails, and the next decision date. Record a signed decision for any conditional edge, early stop, pivot, or sustain. The flow owner may close duplicates or out-of-remit requests at triage. When a decision is pending, keep the card at its current step, set `holder: waiting-decision`, and set `next_decision` with a date and person. A run card proposes a move. The operator checks the branch condition, current decision, and destination WIP before taking it.

**Selecting a move when work is waiting.** Keep verified receipts in the item's Exit evidence log when a decision, evidence window, or WIP slot is pending. Set the step's `evidence_exits_met` marker in the same move as the transition so the selector does not mistake a verified receipt for permission to advance. On a subsequent cycle, if a proposed card already has its waiting condition recorded and nothing has changed, rerun selection with `flow_next.py --skip <slug>` (repeat for other ineligible cards if needed, at most once per card in this cycle). The skip expires at cycle end. A newly overdue decision is itself the move: surface it and record it in the loop log. Keep it visible and use the skip only on later cycles while awaiting the same decision. Before moving any ready card, check the signed branch, capacity, and receipts. A recorded change in eligibility is a reason to consider the card again.

**Outcome review.** Sustain only after the agreed KPI, adoption threshold, and guardrails hold for the specified window and the operating owner can run, support, and monitor the change. An inconclusive result can earn a single bounded extension at this step with a named owner, missing observation, and new decision date. Keep the review exit open until there is a disposition. An effect without repeat use, or repeat use without effect, earns a decision on further evidence, pivot, or stop.

**Pivot or stop.** A pivot closes this hypothesis as `superseded` and links one successor at intake, so prior receipts stay with the bet they were generated for. The signed decision identifies the changed cohort, cause, or mechanism, the assumption worth testing next, and the successor's stable slug. Create or reuse the card at that slug with an empty evidence list and a reciprocal link. On retry, verify the link and finish any pending transition without creating another successor. A stop closes the bet as `stopped`, with the trigger, learning, and disposition of any exposure, changes, support, and costs. Before closing a live bet, record completed rollback or explicit acceptance of residual operation by the operating owner, with an owner and date for any follow-up. Take authorised containment action promptly when a guardrail trips and document it.

**Evidence on every exit.** A receipt can show an assumption failed, adoption lagged, or rollout was aborted. For an early stop or pivot, submit a disposition receipt in place of the normal completion readout: what was attempted or observed, the trigger and source, the evidence available, what could not be measured and why, the signed decision, and live closeout if applicable. An independent verifier checks the available evidence and the stated limits. This receipt permits only the signed stop or pivot edge. From adoption, take the outcome-review edge on a guardrail trip and use the same receipt to surface an early disposition there. Link the receipt from the card and update `evidence_exits_met` only when the current step's evidence exists. Mark an AI-enabled intervention's quality slices, override and fallback behaviour, and per-success cost in its design when relevant.

## Change log

- 2026-11-26 — Initial reusable definition. WIP, ages, and role names are starting defaults.
