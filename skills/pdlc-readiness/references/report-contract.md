# Executive brief contract

Write for a VPE, CTO, or head of AI adoption. Translate mechanism gaps into decisions about investment, adoption, learning speed, and accountability. The reader should not need to understand agents or prompt engineering.

## First screen

- **Title:** PDLC readiness — assessed name.
- **Verdict:** one of the rubric's labels plus one plain-language sentence.
- **Boundary:** “This approach reliably carries work through …; responsibility for … is …”. Bound reliability to the inspected written contract.
- **Scope line:** artifact/framework, stage, snapshot/date, confidence and a clear limitation.
- **Lifecycle strip:** Explore / Discover / Commit / Deliver / Adopt / Review outcomes / Adapt & operate, each labeled with a state. Show the return to Explore/Discover in text. Explain any aggregate step ratings using the dimension findings.
- **Keep:** two or three evidence-backed strengths.
- **Benchmark (when available):** before recommendations, show a visual Output → / Outcome ↑ quadrant. Foreground the assessed spec with its 0–4 ordinal bands and explain their anchors; put dated, versioned framework paths in a subdued background. Source the benchmark and distinguish artifact evidence from framework documentation. If no defensible benchmark exists, show the artifact position alone or omit the quadrant rather than invent comparison points.
- **Leadership read:** the specific harness behavior this output suggests checking next. Avoid implying one artifact proves a systemic defect.

## Under the fold

1. **Harness yield scorecard (artifact mode):** five independent 0–2 demonstrated-control scores from the rubric, with the anchor legend and separate confidence for the observed output versus a systemic harness inference. No total.
2. **Dimension profile:** seven rows, state, one-sentence interpretation, evidence ID. Keep delivery separate from product steering.
3. **Recommendations for this spec:** up to three immediate repairs. State what is missing, evidence/counterevidence, likely consequence, proposed smallest repair, accountable role, and observable proof. These are edits or decisions about the current work, not reusable workflow changes.
4. **Prioritized recommendations for the producing harness:** up to three ranked change hypotheses. Link each score and evidence to a workflow-level intervention, business consequence, and black-box acceptance check on a new output. Rank by decision impact, not ease of editing. Inspect local harness instructions before treating the hypothesis as a root-cause finding; connect an existing process when it already supplies the contract. State how a few further outputs will test whether the pattern recurs.
5. **Indicator read:** current measures by role, what they tell us and do not tell us, and one proposed repair if needed. Do not assume targets or baselines are agreed.
6. **Evidence and limits:** exact source paths with sections or verified lines, snapshot, coverage, exclusions, contradictory evidence, and missing inputs that would change the verdict. Use relative file links when portable; do not invent remote URLs for private/local-only commits.
7. **Next decision:** one recommendation, proposed owner, and the evidence that would show whether the repair worked. A recommendation is not a human decision already made.

Aim for a two-minute executive read above the evidence; the two recommendation lists may require a longer brief. Markdown and HTML must agree on all substantive claims, states, caveats, scores, and citations. All material claims need source IDs; Unknown needs a named missing input instead of a pretend citation.

## Using the HTML asset

Copy `assets/report.html`, replace its example placeholders with the assessment, and repeat dimension rows / recommendation articles as needed. Put the benchmark ahead of both recommendation lists. Keep the visual hierarchy, labeled states, mobile layout, and print styles. Remove unfilled placeholders. No JavaScript, external fonts, CDNs, or network dependencies are needed. Escape source-derived text before inserting it into HTML; quote attributes and allow only local paths or http(s) citation links. Do not embed executable content from assessed files. A local SVG quadrant may be inlined for a self-contained view when its points come from cited data.

The template is artifact-first. In framework-only mode, omit the black-box yield scorecard and current-spec repair section; title the remaining recommendations for the inspected workflow configuration. Do not present a framework repository as if it were a produced spec.

The template's colors encode evidence states, not severity. Use `supported`, `partial`, `gap`, `unknown`, or `not-needed` for styling and always write the state in text. Display uncertainty prominently; gray does not mean failed.

If native rendering is available, inspect the top screen and full report at desktop and mobile widths. Check long paths, wrapping, status labels, gap cards, and expanded source notes. Print layout should retain evidence and meaning. Do not claim visual QA from HTML structure checks alone.
