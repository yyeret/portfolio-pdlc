# PDLC readiness — Spec Kit · local discovery extension

**PDLC-aware, loop incomplete**

The inspected workflow supports learning-oriented planning and verified implementation. It provides a separate value-validation command, but does not make adoption and an owned outcome review part of the completion path. [E2–E5]

Framework assessment · 2026-10-05 · preserved branch spec-kit-yuval-pdlc · cb644d4 · clean checkout · medium confidence. This is the customized local version, not a verdict on upstream Spec Kit or team practice.

## Lifecycle coverage

Explore: **Supported** | Discover: **Supported** | Commit: **Partial** | Deliver: **Supported** | Adopt: **Gap** | Review outcomes: **Partial** | Adapt & operate: **Partial**

Adaptation should return evidence to Explore or Discover. Supported means an explicit contract; Partial an incomplete connection; Gap missing in inspected scope; Unknown unavailable evidence; Not needed a justified exception.

## Keep what works

- User value and measurable success criteria are explicit requirements, with prioritized, independently testable journeys. [E1, E2]

- Low or medium confidence changes the planning strategy toward learning and telemetry. A validation command can recommend pivoting or stopping. [E3, E5]

- Implementation completion checks the result against the specification and technical plan. Keep this delivery discipline. [E4]

## First move

Connect implementation to one owned outcome review. Before a learning slice is approved, name its target users, primary signal, evidence window, and human decision owner. Reuse the existing validation command. [E3–E5]

## What you can rely on

| Dimension | Evidence state | Read and rationale |
|---|---|---|
| Intent and outcome | Supported | Specification instructions require user value, business needs, and measurable user-focused success criteria. This is documented support, not proof of useful outcomes. [E1, E2] |
| Assumptions and discovery | Supported | Assumptions span value, usability, feasibility, and viability. Planning branches on confidence and directs low-confidence work toward learning. [E1, E3] |
| Leading indicators | Partial | Telemetry and leading indicators are requested, but the core templates do not require a cohort, baseline plan, review threshold, or measurement owner. [E1, E3] |
| Commitment and decisions | Partial | Validation recommends pivot, persevere, or kill; the contract does not name the human who decides or the evidence threshold for commitment. [E5] |
| Delivery and verification | Supported | The completion contract checks tasks, feature conformance, tests, coverage, and technical-plan alignment. [E4] |
| Adoption and operation | Gap | The inspected planning and completion contracts do not assign user adoption, ongoing ownership, or an explicit handoff to another process. Extension hooks could add these, but no configured installation was assessed. [E3, E4] |
| Outcome review and adaptation | Partial | The validation command consumes real evidence and can route back to specification. Invocation depends on user-supplied evidence; no default post-delivery trigger or accountable review owner is specified. [E4, E5] |

## Where the gaps affect decisions

### 1 · The outcome loop depends on someone remembering

The validation capability exists, but implementation completion does not require an owned review or handoff. [E4, E5]

**Impact:** A team can finish the planned software while a weak product result never changes the next investment. This is a plausible risk, not an observed result.

**Smallest repair:** Add a review event and human decision owner to the learning slice. Route its evidence into validation and record expand, revise, stop, or gather-more-evidence as a decision.

**Owner and evidence:** Product or initiative owner. Proof: one pilot produces an evidence-backed decision and a corresponding change or explicit continuation.

### 2 · Metrics are named before their decision use is defined

The templates ask for measurable success and learning telemetry without specifying how early signals will change a decision. [E1, E3]

**Impact:** Teams may instrument what is easy to count, then discover too late that the data cannot settle the riskiest assumption.

**Smallest repair:** Before build commitment, define one primary signal with population, source, baseline or baseline plan, observation window, proposed threshold, and response to inconclusive evidence.

**Owner and evidence:** Product owner with engineering support. Proof: the next spec can explain which decision the signal changes and when the evidence arrives.

### 3 · Getting the change into use has no assigned owner

The inspected core path ends at implementation validation without adoption or operating ownership. [E3, E4]

**Impact:** Working software can remain unused, or its support burden can remain invisible when success is declared.

**Smallest repair:** For the next pilot, identify intended users, how they receive the change, who supports it, and the conditions for expansion or rollback. Link an existing rollout process if one exists.

**Owner and evidence:** Product and engineering leads. Proof: a named cohort uses the slice and evidence reaches the review owner.

## Are the indicators useful?

The spec template includes task completion time and task success, which can be useful capability signals; concurrency is a capacity/quality measure, while support-ticket reduction may be a later outcome. Their role depends on the feature and decision horizon. Example targets in a template are not agreed targets for a real initiative. [E1]

The analyzer intentionally excludes post-launch outcome metrics from buildable-work coverage. That is reasonable for an engineering check, but a separate owner must keep those measures in the product review. [E6]

Illustrative repair: for an onboarding pilot, track successful first-task completion within seven days for the intended cohort; establish the baseline before the pilot and agree an expansion threshold. Review support demand as a guardrail. These are proposed measures, not facts or approved targets.

## Evidence and limits

Coverage: core specification, planning, task generation, analysis, implementation and validation instructions; spec and plan templates; local commit history. Optional third-party extensions and organizational processes were not assessed. The local history records discovery additions in 4a8cf6a and cb644d4. The source is preserved unchanged in the spec-kit-yuval-pdlc worktree at cb644d4ed8fb1555761c366f4d3646e90c743bb6. Its common ancestor with latest upstream is 3028a00b6e7b6ba568e49dcb816655894b5a633a; the customized branch has not been rebased. An enabled handoff to an existing product operating process could improve the adoption and review ratings. No workflow was executed and no real business impact was measured.

- **E1** — `templates/spec-template.md` — Success Criteria; Conviction & Leap of Faith Assumptions. Source: Spec Kit local snapshot above.

- **E2** — `templates/commands/specify.md` — Specification Quality Validation; Success Criteria Guidelines. Source: Spec Kit local snapshot above.

- **E3** — `templates/commands/plan.md` — Outline, step 3; quickstart guidance for Learning-Oriented Plan. Source: Spec Kit local snapshot above.

- **E4** — `templates/commands/implement.md` — Completion validation, step 9; extension hooks, step 10. Source: Spec Kit local snapshot above.

- **E5** — `templates/commands/validate.md` — Outline; evidence intake, validation summary, Refine Specification handoff. Source: Spec Kit local snapshot above.

- **E6** — `templates/commands/analyze.md` — Build Semantic Models: requirement inventory excludes post-launch outcome metrics. Source: Spec Kit local snapshot above.

## Next decision

Pilot one connected outcome loop before standardizing additional process. Ask the initiative owner to approve the signal, review event, and decision responsibility for one upcoming learning slice. Reassess after that review has produced a recorded decision; preserve the existing delivery checks.

Assessment of documented support, not certification or proof of achieved outcomes.
