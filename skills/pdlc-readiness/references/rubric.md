# PDLC readiness rubric

Assess the mechanism, not the headings. These are judgment anchors, not a certification or a maturity model validated against business results.

## Evidence states

Use these labels on each dimension and lifecycle step:

| State | Artifact mode | Framework mode |
|---|---|---|
| **Supported** | A concrete, stage-appropriate contract ties evidence to an owner and decision. Later work can be planned, with its trigger and ownership explicit. | The normal path, or an explicit risk-based branch, requires this behavior and passes its output to a named consumer. A separate responsible team counts when the handoff is explicit. |
| **Partial** | Relevant intent exists but a critical link is weak or missing. | Templates prompt it or a useful command exists, but execution, routing, ownership, or response is optional/unspecified. |
| **Gap** | The inspected scope lacks a necessary contract for its claimed purpose/stage, or explicitly contradicts it. | The inspected workflow ends or hands off without providing a necessary responsibility for the claimed lifecycle. State the search boundary. |
| **Unknown** | Required evidence is unavailable or the scope cannot establish the behavior. | The relevant configuration, external process, or execution evidence cannot be inspected. |
| **Not needed** | A reasoned stage/risk/scope exception applies. | An explicit conditional policy makes the behavior unnecessary for this class of work. |

Give each judgment a short rationale and a path plus section/line reference. For a Gap cite the inspected completion contract or owner files and the missing connection. For Unknown identify what would resolve it. Report confidence separately (high/medium/low) based on evidence completeness and directness, not the number of green cells. “Supported” means documented support, not proven organizational execution.

## Seven dimensions

| Dimension | What earns Supported | Why a gap matters |
|---|---|---|
| **1. Intent and outcome** | Names whose problem/capability changes, why it matters, desired observable change, and boundaries. Work traces to that intent; requirements do not prematurely lock the solution without a reason. | A team can build exactly what was requested while leaving the problem unchanged. |
| **2. Assumptions and discovery** | Separates evidence from belief; identifies the uncertainty that could invalidate the investment; uses a proportionate probe or evidence-backed decision to skip discovery. Results can change scope or stop work before major commitment. | Faster delivery can increase investment in an untested bet. Technical research alone will not settle desirability or viability. |
| **3. Leading indicators** | Uses a small set of decision-relevant signals linked to the outcome and uncertainty, at the right altitude, with a measurement and response contract below. | Leaders see activity or late results without an early opportunity to adjust. |
| **4. Commitment and decisions** | A responsible human owns invest/continue/pivot/stop choices, the evidence and timing required, and the boundary of delegated execution. Authorization is distinct from document completeness. | A “ready” spec can become an implicit commitment that nobody has re-evaluated against the evidence. |
| **5. Delivery and verification** | Intent survives into slices, acceptance evidence, constraints, and technical quality checks; implementation completion is explicit. | Even a good outcome hypothesis may produce software that does not satisfy its requirements. |
| **6. Adoption and operation** | Specifies who receives the change, how intended users gain access and use it, proportionate enablement/support/rollout and guardrails, and accountable ongoing ownership. Explicit external handoffs count. | Deployed software can remain unused or create operational costs that outweigh its value. |
| **7. Outcome review and adaptation** | An owner reviews real evidence at a time/event, compares it to thresholds and assumptions, records a human decision, and routes learning into scope, a new experiment, scale, stop, or ongoing operation. | Work closes at delivery; weak results neither challenge the original bet nor redirect the next investment. |

Do not demand full portfolio topology from a feature spec. A linked parent outcome and decision owner may be sufficient. A low-risk repair can justify minimal discovery and a lightweight outcome check. An early Explore spec can have open assumptions and provisional targets; judge whether it supports the next decision and makes later responsibilities visible, not whether it already contains post-launch evidence.

## Leading-indicator test

Assess what the measure **does**, not whether it contains a number. Classify every material signal:

- **Delivery/quality:** task completion, PR count, test pass rate, service reliability. Useful for delivery confidence; product evidence only with a justified link to the intended outcome.
- **Leading product/learning signal:** observable behavior or capability that can change a decision before the desired impact is known.
- **Lagging outcome/impact:** realized retention, savings, revenue, or another final result for this particular decision horizon.
- **Guardrail:** an adverse effect that constrains success (errors, support burden, cost, safety).

The same metric can play different roles in different contexts. Avoid a universal list of “good” and “bad” metrics.

For a decision-ready indicator look for:

1. **Causal relevance:** why this signal tests the riskiest assumption or predicts the desired outcome; distinguish plausible hypothesis from established correlation.
2. **Altitude:** observable change for the beneficiary, linked to initiative intent. Engineering flow may be the product outcome for an internal developer platform; do not force revenue proxies onto it.
3. **Definition:** population/cohort, behavior, denominator where relevant, and window. A qualitative probe can use explicit evidence criteria rather than a percentage.
4. **Interpretation:** baseline or a plan to establish it, target/threshold, and uncertainty/sample adequacy. No fabricated baselines or unjustified precision.
5. **Timeliness:** collection source, when evidence becomes available relative to the next investment decision, and a feasible learning slice.
6. **Response:** owner, review trigger, what changes if the signal improves/fails/is inconclusive, and a guardrail where relevant.

Prefer one primary learning signal plus only the supporting measures needed for the current decision, often one to three. More metrics do not earn a higher rating. A missing baseline need not block an Explore-stage spec if establishing it is the next bounded action.

**Illustrative repair (not an agreed target):** replace “ship onboarding and pass tests” with “In the pilot cohort, observe first successful task completion within seven days; compare with a baseline collected before the pilot. The product owner reviews after the pilot window and chooses expand, revise, or stop using agreed thresholds, with support demand as a guardrail.” Supply a numeric target only with evidence or label it proposed. Do not remove the engineering tests.

## Verdict rules: no averaging

Report the full dimension profile; an excellent delivery score cannot cancel a missing outcome loop.

- **PDLC-ready for the stated scope:** dimensions 1, 3, 4, 6, and 7 are Supported, with a traceable intent → signal → owned review → decision → next action chain. Discovery and delivery must be Supported or explicitly Not needed for the scope/stage. Readiness is a documented contract, not proof of achieved outcomes.
- **PDLC-aware, loop incomplete:** meaningful outcome/discovery mechanisms exist, but one or more essential connections above are Partial or Gap. Name the break and give delivery discipline separate credit.
- **SDLC-focused:** the inspected completion path is implementation, testing, PR, or deployment, and outcome steering beyond that boundary is absent or merely aspirational. A product-oriented introduction alone does not change this verdict. This may be entirely appropriate for the workflow's intended engineering scope.
- **Insufficient evidence:** unresolved Unknowns could materially change the verdict. State the provisional boundary you can see and the smallest missing evidence needed. Do not use this label merely because real-world adoption has not been audited.

For framework distributions with independent optional workflows, state which path the verdict covers. Credit an optional route separately, including any stronger human decision or discovery support. A default-path rating must not erase available capability; an available extension must not silently upgrade the default path.

For mixed inputs (framework plus produced spec), rate them separately. Do not generalize one artifact's omissions to every framework user, or infer actual practice from the framework's potential.
