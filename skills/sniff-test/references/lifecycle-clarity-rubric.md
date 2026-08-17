# Lifecycle Clarity Rubric

The purpose of a sniff test: **find where an initiative's clarity is insufficient for its stage**, so the right investment/commit and derisking conversations happen. Clarity is read *relative to stage*. What's healthy in Discovery is a smell in Execute/Build.

> **Verify the stage first.** Don't trust the status label — corroborate it against evidence (downstream artifacts, shipped output, go-live state, git history, decision records). A stale label can invalidate the whole clarity-vs-stage read and is often the highest-signal finding. See the main skill's "Stage Is a Required, Verified Input."

## Lifecycle stages

The lifecycle is two macro-phases — **Explore & Define** (framing, testing assumptions) and **Build & Deliver** (delivering, realizing value) — then **BAU**:

**Explore → Discovery *(optional)* → Plan / Commit → Execute / Build → Rollout / Last Mile *(optional)* → Business as Usual (BAU)**

Key principles that shape the read:
- **Common language, not gates** — this is *not* a stage-gate process. Decision routing scales with risk and complexity, not a fixed gate.
- **Confidence grows throughout the lifecycle** — you're rating whether confidence has grown *enough for this stage*, not pass/fail.
- The risk lens is **Desirability – Viability – Feasibility (DVF)**.
- Two stages are **optional** (Discovery, Rollout/Last Mile) and scale with risk; their absence is only a smell when the risk warranted them.

**Language note:** in sponsor/leadership framing speak in **confidence and what you can rely on**, not "gates" or "exit criteria."

## Expected clarity, "what you can count on," smells, and watermelon risk by stage

### Explore  *(Explore & Define)*
- **Expected**: Framing the problem — "is this worth investigating?" A **Lightweight Product Canvas** takes shape (problem, research of solutions and value, resources/topology for the next phase). Significant uncertainty is normal. EA gets a Direction Review based on Explore insights.
- **What you can count on**: There's a real, framed problem worth investigating — not just a solution someone wants built. Marks the Explore/Define completion view.
- **Smell**: Solution-first framing with no problem/outcome; suspiciously high early clarity with no evidence (a watermelon in the making).
- **Conversation**: What's the riskiest assumption, and is this even worth investigating further?

### Discovery  *(optional, timeboxed)*
- **Expected**: Timebound, focused work to **reduce uncertainty** and support a real investment decision. *Code here is an experiment.* Proof-of-concept / lightweight prototype / vendor evaluation (RFP) to de-risk the approach; business requirements and assumption testing across DVF. Outcome: initial clarity on assumptions and a decision on **if/how to proceed**.
- **What you can count on**: The biggest unknowns have been deliberately tested enough to support an investment decision.
- **Smell**: Discovery aimed at what's already clear instead of the question marks; "skip to Execute" with open desirability; experiment code quietly hardening into committed scope; an assumption set full of confident opinion and no evidence. The cardinal smell: arriving at the commit decision with the answer pre-decided and nothing actually tested (the **rubber stamp**).
- **Conversation**: For each DVF question mark, what's the cheapest experiment that moves it before we invest?

### Plan / Commit  *(Explore & Define → commitment)*
- **Expected**: Confirm roadmap and resources — "should we build? how?" Produce an **Outcome-Oriented Roadmap with defined confidence**, a feature map, and a delivery estimate / resource forecast. High-level EA check-ins and impact assessments. Sets the **Target Initiative Completion Date**.
- **What you can count on**: There's a roadmap with an explicit confidence level and a resourced plan — the basis for committing.
- **Smell**: Committing with confidence asserted but unevidenced; a roadmap with no confidence range; risks carried forward from a skipped Discovery the risk warranted.
- **Conversation**: What evidence underwrites this confidence level, and what's still unproven as we commit?

### Execute / Build  *(Build & Deliver — committed scope)*
- **Expected**: **High, evidence-backed clarity.** Committed scope, delivered at scale; the **Committed Initiative Completion Date** (with a defined confidence range) is set here. Iterative/incremental delivery and validation of slices of value (demos, requirement detail, testing, feedback loops); EA and IS addressed iteratively; operational readiness (UAT) and pre-deployment EA review. The Plan/Commit → Execute transition is the practical point of last return — after it, change is expensive.
- **What you can count on**: The biggest unknowns were tested *before* commitment, not deferred into delivery.
- **Smell**: Still-open DVF question marks in committed work; clarity asserted but unevidenced; the roadmap never reaching high confidence.
- **Conversation**: What evidence backs each "clear" rating? What got committed that was never actually tested?

### Rollout / Last Mile  *(optional)*
- **Expected**: Staged rollout / wait step (can combine with Execute) — deploy, stabilize, enable adoption (phased rollout, hypercare). Stakeholder signoff on outcomes; handover to BAU. Achieving the initiative's value-realization goals.
- **What you can count on**: Value is being realized and adoption is real, with outcomes backed by evidence — not just "shipped."
- **Smell**: Go-live with outcome clarity still asserted rather than measured; scaling/adoption risks surfacing now that should have been Discovery work.
- **Conversation**: Are the outcome measures actually instrumented, or just promised?

### Business as Usual (BAU)
- **Expected**: Value realized; ongoing operations and support — **sustain and enhance**. Clarity backed by leading and lagging indicators. Domain-team prioritization; visibility to resource allocation between BAU and Tier-1 work.
- **Watermelon hunt**: Compare *baseline clarity across the lifecycle* against *actual results*; find initiatives rated clear/green throughout that turned out misplaced — the most valuable learning. Major surprises should loop back to Discovery, not hide inside BAU; honest loop-backs are a *good* signal.
- **Conversation**: Where were we confidently wrong, and what does that teach us about our sniffing — and about whether Discovery is doing its job?

## The watermelon principle

A **watermelon** is green outside, red inside — clarity that *looked* solid but proved wrong. The antidotes run through every stage: tag evidence vs. opinion, stress-test even "clear" dimensions, and review baseline-clarity-vs-actual-results in BAU. A lifecycle that never surfaces a watermelon usually isn't looking hard enough — and is at risk of rubber-stamping its commitments.
