---
date: 2026-07-13
category: step-design
item: instructor-payroll-explainer
severity: significant
---

# A dropped piece with a recorded probe is a win, not a failure

**What happened.** `instructor-payroll-explainer` went to `angle-test` and the probe drew
two replies in a week, both from people who work here. We dropped it. Four hours spent
instead of the week a draft would have cost.

**What we now believe.** The `angle-test` step pays for itself on drops, not on proceeds.
Before it existed, that piece would have been written, edited, published, and quietly
ignored — and we would have recorded it as throughput.

**What the next cycle does differently.** `dropped` items get read in the meta-loop as
saved capacity, and the loop log records the drop with the probe attached. If a quarter
passes with zero drops at `angle-test`, that is the smell — it means we are probing to
confirm rather than to find out.
