# Definition of Workflow — FlowImpact Yoga

Started from the framework's default lifecycle; FIY owns it from here. Common language, not gates.

## Stages

| Stage | (Narrative) | Intent | What you can count on |
|---|---|---|---|
| explore | (Think It) | Frame the problem | A real problem worth investigating, not a solution seeking a sponsor |
| discovery *(optional, timeboxed)* | (De-risk It) | Test the riskiest assumptions | Biggest unknowns deliberately tested enough for a real go/no-go |
| plan-commit | | Decide to build | Outcome-oriented roadmap with a confidence range and resourcing |
| execute | (Build It) | Deliver committed scope | Unknowns were tested before commitment; slices validate in flight |
| rollout *(optional)* | (Ship It) | Deploy and drive adoption | Value realization measured, not just shipped |
| bau | (Tweak It) | Sustain and learn | Outcomes read against hypothesis; surprises loop back honestly |

## Flow boundaries

- Start: when a bet needs cross-team attention or portfolio money — at framing, not at
  "engineering, please build."
- End: outcome measured and handed to the operational roadmap.

## Policies

1. Right-to-left reviews; finishing beats starting.
2. Discovery-or-skip is an explicit, dated decision for high-risk cards.
3. Entering plan-commit and execute requires a dated human decision.
4. Measure-and-learn questions on every in-flight card at review.
5. Freeze/kill is respectable and recorded: double down / de-risk further / kill-pause.
6. Architecture & security: direction read at explore, formal touch at discovery exit and
   pre-rollout.

## Review cadence

Monthly portfolio review (right-to-left, decisions first) + quarterly deep-dive on 1–2
bets. Tier-2 work appears on one awareness slide.

## Service Level Expectations

TBD — flow history is ~3 completed initiatives; revisit after two more quarters.

<!-- board-config
stages: explore, discovery, plan-commit, execute, rollout, bau
optional_stages: discovery, rollout
wip_limits: plan-commit=3, execute=4
aging_thresholds: explore=30, discovery=45, plan-commit=30, execute=120, rollout=45
decision_boundaries: plan-commit, execute
-->
