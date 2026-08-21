---
title: Changes ship without waiting on a human for the cases a check can settle
type: improvement-process
stage: watching
owner: Yuval
opened: 2026-08-21
benefit_hypothesis: "If an independent check gates merges, changes reach main without a human round-trip on the cases the check can settle, with no increase in escapes — because most of what a reviewer catches here is mechanical"
measures: [human-round-trips-per-change, escapes, rounds-to-clean]
baseline: "Before 2026-08-21, 100% of merges waited on a human: PR #1 sat mergeable-clean for ~26 hours across 20 check-ins with nothing to report"
kill_criteria: "One escape — a change merges that the repo owner would have blocked — and merge authority goes back to a human signature on every PR. Not a warning, a revert."
probe: "PRs #2 and #3 are the first two data points; read them after five merged PRs"
---

# Changes ship without waiting on a human for the cases a check can settle

## The signal

PR #1 was mergeable-clean with no CI, no review comments, and nothing to fix, for roughly
26 hours. Twenty scheduled check-ins each confirmed the same thing and re-armed. The human
was the only thing between a finished change and `main`, and there was nothing for the human
to actually decide — the questions a reviewer would have asked were all answerable by running
something.

## Benefit hypothesis

If merging is gated by an independent check rather than by a human's calendar, then
human-round-trips-per-change falls toward zero for mechanical work and escapes stay at zero,
**because** the failure modes that matter in this repo — a script that does not run, a
convention quietly broken, a claim the diff does not support — are all detectable by a fresh
context that runs the checks.

## Options considered

| Option | What changes | Effort | Risk | Reversible? |
|---|---|---|---|---|
| do nothing | — | — | finished work waits on a human's attention; check-ins burn cycles reporting "no change" | — |
| agent merges on its own say-so | no gate | none | the author grades their own work — the exact failure the framework warns about | yes, loudly |
| gate on an independent review | `docs/quality-bar.md` + a fresh-context reviewer | s | a weak bar lets something through | yes — revert the policy, revert the merge |
| branch protection + required CI | mechanical enforcement | m | real enforcement, but no CI exists here yet | yes |

## Probe

The policy's own PR (#2) was the first candidate: reviewed against the bar it adds, by a
context that did not write it. It came back **BLOCK** on two findings — a verification claim
in the PR body that did not reproduce (`exit 0` where the real code is 4), and the bootstrap
objection that a policy granting merge authority should not be its own first customer.

That is the probe result worth keeping: **the bar caught a false check result on the PR that
introduced the rule against false check results.** A gate that passes its own author's work
on the first try has not been tested.

## Adoption

`docs/quality-bar.md` and the "Shipping changes here" section of `AGENTS.md`, merged as
`a46667c`. Merging moves to rung 4 of the repo's own delegation ladder: agent runs it,
independent check gates it, §4 escalation list is the `escalate_when`.

## Watch

Read after five merged PRs. Escapes is the one that matters; the other two are diagnostics.

| Date | Measure | Value | Read |
|---|---|---|---|
| 2026-08-21 | human-round-trips-per-change | 1 (PR #2, by design — bootstrap) | expected; the policy could not approve itself |
| 2026-08-21 | escapes | 0 | one PR is not evidence |
| 2026-08-21 | rounds-to-clean | 1 review, 1 hand-back | the loop did not exist yet — see `bounded-review-loop` |

## Decision log

| Date | Decision | Who | Basis |
|---|---|---|---|
| 2026-08-21 | Adopt: agents may merge their own PRs here when an independent review clears them | Yuval | "I approve the policy. You can merge it." |
