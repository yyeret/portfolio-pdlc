# Focused Jev classifiers for PDLC readiness

Use these as independent shadow judgments against one produced artifact or explicitly defined bundle. The human assessor still owns the verdict, evidence trail, recommendations, and uncertainty. Jev classifications are not labels of truth and do not establish the producing harness's behavior.

## Call contract

- Model: use a supported Jev model available to the caller. Record the resolved model and this rubric version (`pdlc-readiness-jev-v1`).
- Primitive: one `choice` question per row below, batched together for a single source item. Choice keeps evidence states and ordinal yield levels discrete and exposes a probability distribution for every label. Do not ask for a composite readiness score.
- Context: use only source text the caller has authorized for provider processing. Respect source sharing restrictions and remove credentials and unrelated private material first. For a bundle, identify each included artifact by title and role. If authorization or source limits require excerpts, preserve every section relevant to the rubric and disclose omissions; never summarize away evidence before asking Jev.
- Ask for the best-supported label based only on visible evidence, allow `unknown`/`not_needed` where defined, and require an answer for each stable ID. Retain the raw answer, full probabilities, confidence, model, source hash, and call date.
- Abstain when the choice is `unknown`/`not_needed` or confidence is below 0.75. Preserve distributions even for scored answers. Confidence is distribution concentration, not correctness.
- Do not average the seven dimensions or six controls. Do not translate them to a readiness percentage. A tie/close distribution is ambiguity, even if the provider emits one top choice.
- Compare Jev to the assessor's independently evidence-cited state/score. Flag any non-abstained difference for review; a `gap` versus `supported` or `0` versus `2` difference is especially consequential. Mark a top probability below 0.60 as ambiguous. Do not call agreement validation; adjudicate with evidence and retain unresolved differences.

## Classifiers

Each question is a separate classifier. Keep its scope narrow and apply the label descriptions as written.

### Evidence-state dimensions

All seven classifiers use `supported`, `partial`, `gap`, `unknown`, `not_needed` as options. Supported requires a concrete stage-appropriate contract tied to evidence, an owner and a decision. Partial means relevant intent exists but a critical link is weak or missing. Gap means the inspected scope lacks a necessary contract for its stated purpose/stage. Unknown means evidence needed to judge is inaccessible or scope cannot establish the behavior. Not needed requires a reasoned stage, risk, or scope exception.

| ID | Classifier question |
|---|---|
| `dimension.intent_outcome` | Does the artifact identify whose problem or capability changes, why it matters, the desired observable change, and boundaries, with requirements governed by that intent? |
| `dimension.assumptions_discovery` | Does it distinguish evidence from belief and address the uncertainty that could invalidate the investment through a proportionate probe or evidence-backed skip before major commitment? |
| `dimension.leading_indicators` | Are decision-relevant signals linked to the intended outcome/uncertainty, defined enough to interpret, and timed to inform a decision? |
| `dimension.commitment_decisions` | Is a responsible human assigned the invest/continue/pivot/stop decision, evidence/timing, and delegated-execution boundary, distinct from document completeness? |
| `dimension.delivery_verification` | Does intent trace into implementation slices, acceptance evidence, constraints, technical checks, and an explicit completion boundary? |
| `dimension.adoption_operation` | Does the artifact define the recipient, access/use or rollout handoff, proportionate support/guardrails, and accountable ongoing owner? |
| `dimension.outcome_adaptation` | Does an owner review real evidence at a stated time/event, compare it with assumptions or thresholds, decide a human response, and route learning into next work, operation, or closure? |

### Harness-yield controls

All six classifiers use `0`, `1`, `2`, `not_yet_due`, `unknown`. These are ordinal, independent ratings; `not_yet_due` requires an explicit stage/timing rationale and does not count as zero.

| ID | 0 | 1 | 2 | Classifier question |
|---|---|---|---|---|
| `yield.intent_carried` | No beneficiary problem or intended change | Product language exists but does not govern scope | Beneficiary problem, observable change, and boundaries shape requirements | How clearly does this output carry beneficiary intent into its plan/specification? |
| `yield.learning_signal` | Only outputs, activity, or technical checks | A plausible product signal exists without a usable definition or response | Signal tests an assumption, has collection/interpretation plan, and can change a decision | How strongly does the output define a decision-relevant learning signal? |
| `yield.adoption_handoff` | No recipient, trigger, or operating owner | Rollout/support is mentioned without accountable handoff | Recipient, access/use trigger, and proportionate ownership or linked process are clear | How clearly does the output hand the change to adoption and operation? |
| `yield.outcome_feedback` | Work ends at engineering completion | Outcome review is suggested but not routed to a decision | Owner, review timing/evidence, human response, and route into next work are explicit | How clearly does the output connect an outcome review to an owned decision and feedback? |
| `yield.delivery_verification` | No implementation/acceptance path | Tasks or tests exist without end-to-end trace | Requirements, units, acceptance evidence, and completion checks are linked | How clearly does the output connect its intent to delivery and verification? |
| `yield.lifecycle_continuity` | Work begins at implementation with no upstream intent source or later responsibility | A pre-spec source or downstream step is named, but trace breaks before in-use evidence and closure/continue decision | Same intent/hypothesis flows from upstream framing through specification, delivery, adoption, measurement, learning/adaptation, and human-owned closure or ongoing operation | How continuous is the evidence chain from upstream intent through product closure or continued operation? |

## Reporting

Show human judgment and Jev output in adjacent columns, not merged. For every classifier include the assessor's rating, top Jev label, confidence, and complete probability distribution; mark abstentions. State whether Jev ran against full source text or bounded excerpts. Summarize only evidenced disagreements; no claims about accuracy, improvement, causal root cause, or inter-rater reliability can be made from a single pass. Keep raw provider output with the saved assessment record where retention policy permits.
