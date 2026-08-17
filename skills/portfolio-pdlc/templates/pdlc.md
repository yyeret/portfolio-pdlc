# Definition of Workflow — <Portfolio Name>

This is OUR portfolio workflow. It started from the framework's default lifecycle and we own it from here: try, inspect, adapt. It is a **common
language, not gates** — decisions route by risk and confidence, not by ceremony.

## Stages

Leadership narrative names in parentheses — use whichever language lands with your sponsors
(the Think It / De-risk It / Build It / Ship It / Tweak It naming is the same lifecycle).

| Stage | (Narrative) | Intent | What you can count on when a card sits here | Typical artifacts |
|---|---|---|---|---|
| explore | (Think It) | Frame the problem: worth investigating? | A real, framed problem — not a solution looking for a sponsor | Lightweight Product Canvas; architecture Direction Review |
| discovery *(optional, timeboxed)* | (De-risk It) | Reduce the biggest unknowns before investing | The riskiest DVF assumptions were deliberately tested enough to support a real go/no-go | Derisking plan + evidence; PoC/prototype/RFP; code here is an experiment |
| plan-commit | | Should we build, and how? | An Outcome-Oriented Roadmap with an explicit confidence range and a resourced plan | Roadmap + feature map; Target Completion Date; delivery estimate |
| execute | (Build It) | Deliver committed scope — the point of last return | The biggest unknowns were tested BEFORE commitment; slices ship and get validated | Committed Completion Date (with confidence range); demos; iterative EA/security touchpoints |
| rollout *(optional)* | (Ship It) | Deploy, stabilize, drive adoption | Value realization is being measured, not just "shipped" | Phased rollout plan; hypercare; stakeholder signoff |
| bau | (Tweak It) | Sustain, enhance, and learn | Outcomes read against the original hypothesis; surprises loop back to discovery honestly | Value Realization Report; watermelon retro |

Skipping an optional stage is a **decision, not a default** — record who chose to skip
discovery and on what risk basis (see policies).

## Flow boundaries

- **Start**: <when do we start tracking? at idea? at "business asks technology"?>
- **End**: when the outcome is achieved and measured — the card leaves the board to the
  operational roadmap. "We're done treating this as a high-profile investment."

## Policies

1. **Right-to-left reviews.** Walk the board rollout→explore. Finishing outranks starting.
2. **Discovery-or-skip is explicit.** High-risk cards entering plan-commit without a
   discovery record need a dated skip decision in their Decision log.
3. **Decision boundaries.** Entering `plan-commit` and `execute` requires a dated human
   decision (invest / commit). Framed as confidence, recorded as a decision.
4. **Measure-and-learn in flight.** For every in-flight card on cadence: Have we achieved
   the outcome hypothesis? What do the metrics teach? Diminishing returns? Still a business
   constraint?
5. **Freeze/kill is respectable.** `frozen` and killed cards are recorded decisions with
   reasons — de-risk further / double down / kill-pause is the decision vocabulary.
6. **Architecture & security ride along.** Direction Review at explore; formal touchpoints
   at discovery exit and pre-rollout — iterative during execute, never a surprise audit.

## Review cadence

<e.g., monthly portfolio review (right-to-left, decisions-first) + quarterly investment
council: state of the union → deep-dive "sparring pit" on 1–2 bets → double down /
de-risk further / kill-pause decisions. Sub-threshold work appears on one
"for awareness only" slide.>

## Service Level Expectations

<Fill from flow-log percentiles once history exists; until then mark TBD rather than guessing.>

<!-- board-config
stages: explore, discovery, plan-commit, execute, rollout, bau
optional_stages: discovery, rollout
wip_limits: plan-commit=3, execute=4
aging_thresholds: explore=30, discovery=45, plan-commit=30, execute=120, rollout=45
decision_boundaries: plan-commit, execute
-->
