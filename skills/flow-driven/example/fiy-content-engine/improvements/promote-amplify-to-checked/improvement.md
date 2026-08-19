---
title: Amplify runs unattended, audited rather than watched
type: improvement-delegation
stage: watching
owner: Dana
opened: 2026-07-06
benefit_hypothesis: "If amplify runs at rung 4 behind a claim-drift audit, human-minutes-per-item drops by ~40 with no increase in escapes"
measures: [human-minutes-per-item, cost-per-item, escape-rate]
baseline: "human-minutes-per-item = 180 as of 2026-06-30; amplify escapes = 0 of 9"
kill_criteria: "Two audit escapes in a month, or one variant claiming something the piece did not — demote to rung 3"
probe: "Shadow-run: the agent produced the plan and the audit for 12 pieces while Dana still wrote the variants; compare"
---

# Amplify runs unattended, audited rather than watched

## The signal

Dana spent ~40 minutes per piece writing channel variants, and the meta-loop's
human-touch probe showed `amplify` as the single largest human-minute sink that produced no
judgement — every variant she wrote was a mechanical restatement of the piece.

## Benefit hypothesis

If we promote `amplify` to rung 4 behind `platform/checks/amplify-audit.md`, then
human-minutes-per-item falls by ~40 with no rise in escape-rate, because the one real
failure mode of the step — claim drift in the hook — is mechanically detectable.

## Options considered

| Option | What changes | Effort | Risk | Reversible? |
|---|---|---|---|---|
| do nothing | — | — | 40 min/piece of Dana's attention on mechanical work | — |
| promote to rung 3 | agent drafts variants, Dana checks each | s | keeps a human in a loop that adds nothing | yes |
| promote to rung 4 with an audit | agent runs it; the audit gates scheduling | m | claim drift ships unnoticed if the audit is weak | yes — unschedule in a minute |

## Probe

Twelve pieces shadow-run: the agent produced plan + audit while Dana still wrote and
scheduled the variants. Compared audit findings against her rewrites.

- **Timebox**: 2026-07-06 → 2026-08-01
- **Proceed if**: the audit finds every drift Dana corrects, over ≥10 pieces
- **Stop if**: the audit misses one drift she catches

Result: 12 of 12 clean; the audit caught two drifts she had missed herself.

## Adoption

`steps/amplify.md` moved to `delegate_rung: 4` with `verify_with:
platform/checks/amplify-audit.md`, recorded in the `workflow.md` change log on 2026-08-03.

## Watch

| Date | Measure | Value | Read |
|---|---|---|---|
| 2026-08-19 | human-minutes-per-item | ~150 (est.) | moving, but Dana is still hand-writing variants on `voice-of-studio-owner-digest` — the promotion is on paper, not in the habit |
| 2026-08-19 | escape-rate | 0 | holding |

The board flags that hand-holding as a leverage leak. A promotion nobody actually uses is
worth less than one nobody made — watch it for two more pieces before calling it adopted.

## Decision log

| Date | Decision | Who | Basis |
|---|---|---|---|
| 2026-07-06 | Run the shadow probe | Dana | human-touch probe finding |
| 2026-08-03 | Adopt rung 4 for `amplify` | Mary | 12/12 clean shadow runs |
