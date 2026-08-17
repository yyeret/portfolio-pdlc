# Clarity Dimensions — Lean Product Canvas + DVF Risk Lens

A sniff test rates clarity across two aligned layers: the **Lean Product Canvas** framing (is the bet well-formed?) and the **Desirability / Viability / Feasibility** risk lens used in Discovery (are the assumptions tested?). Mark each: **clear** / **partial** / **question mark**, and tag whether it is **evidence-backed** or **opinion**.

## Layer 1 — Lean Product Canvas framing

| Element | The core question | Sniff for |
|---|---|---|
| **Business Problem** | What problem are we focused on, and why now? | Solution-first framing with no named problem; a "project" with no outcome behind it. |
| **Users** | Which users/customers and stakeholders are we focused on first? | "Everyone / the business" hand-waving; sponsors and end-users conflated; cross-functional stakeholders (EA, SecOps, data) unnamed. |
| **Business Outcomes** | How will we know we solved it? What will we measure? | Outcomes stated as activity or output; no measure; only lagging totals. |
| **User Outcomes & Benefits (JTBD)** | Why would the user seek this out — what changes for them? | Benefit asserted with no job-to-be-done; internal convenience mistaken for user value. |
| **Hypotheses** | "We believe [outcome] if [user] attains [benefit] with [feature]." | No falsifiable hypothesis; a plan with no belief to test. |
| **Questions / Assumptions & Learning Priorities** | What's most important to learn first, and how cheaply? | No riskiest-assumption call-out; a learning plan that validates the already-known. |

## Layer 2 — DVF risk lens (the Discovery assumption set)

| Dimension | The core question | Sniff for |
|---|---|---|
| **Desirability** | How much conviction do we have that the right users want this enough to "pay" (money, time, adoption)? | The classic discovery question. Confidence with no evidence; a stakeholder proxy standing in for the real user. |
| **Viability** | If they want it, can we make money / is the value exchange worth it? | Revenue/cost logic never sized; "we'll figure out the model later" on a Tier-1 bet. |
| **Feasibility** | Can we build it? Will it work? Can we run it safely? | Technical optimism with no spike; operational/run-time risk ignored. |
| **Architecture / Data / Security assumptions** | Have EA, data, and security risks been surfaced while there's still optionality? | EA/SecOps engaged late as gatekeepers instead of early as stakeholders; the PDLC≠SDLC line blurred. |

## Rating discipline

- **Evidence vs. opinion is the most important tag.** "We're confident users want this" is a **question mark** until there is evidence (interviews, a working slice used by real users, a signed commitment, usage data). Confident-but-unevidenced clarity is exactly how **watermelons** form — and exactly what turns the commit decision into a **rubber stamp**.
- **Partial is a real state.** "We know the user but not whether they'll adopt" = Users clear, Desirability question mark. Keep them separate.
- **The score is only meaningful against the stage.** A wall of question marks in Explore / Discovery is healthy. The same wall at Execute/Build is a red flag. Always read this with `lifecycle-clarity-rubric.md`.
- **Multiple question marks compound risk** and should weigh into the go/no-go, not just discovery planning.

## Aligning the derisking plan with the gaps

The discovery / assumption-burn-down plan should target the **question-mark dimensions**. The classic smell: a feasibility-focused prototype when the open questions are Users and Desirability ("who is this for and do they actually want it?"). If the plan is validating what's already clear, that's motion, not derisking — flag it.
