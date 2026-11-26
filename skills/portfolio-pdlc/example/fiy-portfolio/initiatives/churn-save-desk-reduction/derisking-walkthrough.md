# De-risk the churn-save initiative

This walkthrough continues the [fictional starting card](initiative.md) in a practice
scenario. All results and decisions below are simulated. The shared sample board starts
before these events so you can still practice spotting the overdue decision.

## From assumption to test

On August 17, Dana brings the overdue decision to Mary. The starting card records
prototype usage and an August 4 readout that recommends a staged build. It has no
evidence that a pause option saves subscriptions without displacing full-price
renewals. That viability assumption is the one most likely to change what Mary is
willing to fund.

**Coaching question.** “Which renewals could a pause displace, and can we observe
that behavior before committing to a billing build?”

Dana narrows the test to studios that request cancellation at renewal. Mary authorizes
a manual trial for that group and sets August 31 as the next decision. The save desk can
offer a one-month paid pause using the existing billing process.

| Record in the Derisking plan | What Dana and Mary agree before the trial |
|---|---|
| Assumption | A paid pause retains some studios that request cancellation at renewal, without reducing observed full-price renewals in that group. |
| Small test | Dana randomly assigns 20 eligible studios, 10 to the usual save-desk offer and 10 to the same offer plus a paid pause. Use the existing desk and billing process through August 31. |
| Decision threshold | Recommend planning a targeted slice if the pause group has at least two more paid accounts at the end of the trial and at least as many full-price renewals as the usual-offer group. Count renewals and paid pauses as paid accounts. |
| Other results | If full-price renewals are lower, reconsider pause eligibility or price. If evidence is incomplete or the retention difference falls short, bring that result to Mary and leave the build decision open. An extension would require a new decision. |

## From result to human decision

**August 31 Evidence log.** Usual offer had 4 full-price renewals and 6 cancellations.
The pause group had 4 full-price renewals, 3 paid pauses and 3 cancellations. The test
met the agreed threshold within the pilot. The small sample and short window leave
longer-term retention and the effect of offering pause to other customers open.

**August 31 decision brief.** Dana recommends entering Plan/Commit for a targeted
pause slice for studios requesting cancellation. The decision is between planning
that slice, gathering more evidence first, or stopping the pause work. Rule out a
build commitment if the billing team cannot staff the slice or measure retention
after the pause ends. Bring a delivery estimate to the next funding decision.

**August 31 Decision log (fictional human decision).** Mary approves planning the
targeted slice and asks for the scoped build decision on September 7. The budget and
billing capacity for a build are still open.

To replay on a copy of the portfolio, record Mary's trial authorization and the
August 31 finding in the card, and set the August 31 review as `next_decision`.
The card stays in `discovery` while the brief is pending. After recording Mary's
August 31 decision, set `stage: plan-commit`, `stage_entered: 2026-08-31` and
`next_decision: "2026-09-07 — commit to targeted build? (Mary)"`. From the repo root,
run the board script against your practice copy and confirm the flow log gained
one transition from Discovery to Plan/Commit for this card.

```bash
python3 skills/portfolio-pdlc/scripts/portfolio_board.py /path/to/practice-copy --today 2026-08-31
```
