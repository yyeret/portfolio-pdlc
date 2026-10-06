# Executive brief contract

Write for a VPE, CTO, or head of AI adoption. Translate mechanism gaps into decisions about investment, adoption, learning speed, and accountability. The reader should not need to understand agents or prompt engineering.

## First screen

- **Title:** PDLC readiness — assessed name.
- **Verdict:** one of the rubric's labels plus one plain-language sentence.
- **Boundary:** “This approach reliably carries work through …; responsibility for … is …”. Bound reliability to the inspected written contract.
- **Scope line:** artifact/framework, stage, snapshot/date, confidence and a clear limitation.
- **Lifecycle strip:** Explore / Discover / Commit / Deliver / Adopt / Review outcomes / Adapt & operate, each labeled with a state. Show the return to Explore/Discover in text. Explain any aggregate step ratings using the dimension findings.
- **Keep:** two or three evidence-backed strengths.
- **First move:** the smallest useful intervention and the leadership decision it supports.

## Under the fold

1. **Dimension profile:** seven rows, state, one-sentence interpretation, evidence ID. Keep delivery separate from product steering. No numeric total.
2. **Up to three priority gaps:** state what is missing, evidence/counterevidence, likely consequence, proposed smallest repair, accountable role, and observable proof of improvement. Rank by decision impact, not ease of editing. Distinguish plausible consequences from observed results. Group related lower-level gaps; preserve the complete profile.
3. **Indicator read:** current measures by role, what they tell us and do not tell us, and one proposed repair if needed. Do not assume targets or baselines are agreed.
4. **Evidence and limits:** exact source paths with sections or verified lines, snapshot, coverage, exclusions, contradictory evidence, and missing inputs that would change the verdict. Use relative file links when portable; do not invent remote URLs for private/local-only commits.
5. **Next decision:** one recommendation, proposed owner, and the evidence that would show whether the repair worked. A recommendation is not a human decision already made.

Aim for roughly 600–900 words excluding source notes; shorten further when the evidence permits. Markdown and HTML must agree on all substantive claims, states, caveats, and citations. All material claims need source IDs; Unknown needs a named missing input instead of a pretend citation.

## Using the HTML asset

Copy `assets/report.html`, replace its example placeholders with the assessment, and repeat dimension rows / gap articles as needed. Keep the visual hierarchy, labeled states, mobile layout, and print styles. Remove unfilled placeholders. No JavaScript, external fonts, CDNs, or network dependencies are needed. Escape source-derived text before inserting it into HTML; quote attributes and allow only local paths or http(s) citation links. Do not embed executable content from assessed files.

The template's colors encode evidence states, not severity. Use `supported`, `partial`, `gap`, `unknown`, or `not-needed` for styling and always write the state in text. Display uncertainty prominently; gray does not mean failed.

If native rendering is available, inspect the top screen and full report at desktop and mobile widths. Check long paths, wrapping, status labels, gap cards, and expanded source notes. Print layout should retain evidence and meaning. Do not claim visual QA from HTML structure checks alone.
