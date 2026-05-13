## Declaration 

My declared ambition is causal.
Using two Regression Discontinuity Designs (RDDs), I tested whether crossing key AFL ladder thresholds — entering the Top 4 or qualifying for finals (5–8) — causes a jump in club membership.

## Main result:  
Across both cutoffs, the estimated discontinuities are small, statistically insignificant, and visually absent.
This suggests that crossing these performance thresholds does not cause a meaningful increase in membership.


## 2. Robustness Checks 


1. Bandwidth Sensitivity (Main → Narrow → Wide)

What it is
This is the RDD‑specific robustness check that tests whether your estimated discontinuity is sensitive to how much data you include around the cutoff.

Three versions:
- Main bandwidth → your preferred window
- Narrow bandwidth → zooms in very close to the cutoff
- Wide bandwidth → includes more observations further away

Why it matters
- RDD identification relies on the assumption that units just above and below the cutoff are comparable.
- But the choice of bandwidth is subjective.

So this check asks: Does the estimated jump remain stable when we change the bandwidth?


2. Alternative Sample Windows (Top‑4 vs Finals Cutoff)

What it is
RDD ran at two different meaningful thresholds:
- Top‑4 cutoff (4 vs 5)
- Finals cutoff (8 vs 9)
These represent two different causal stories:
- Top‑4 → home finals advantage, prestige
- Finals → making the postseason

Why it matters:
- If membership truly responds to ladder success, you might expect:
    - a jump at one threshold but not the other
    - or at least consistent directionality


3. Alternative Cutoff (Placebo 6–7)

What it is
A placebo RDD where you pretend the cutoff is at a point where no treatment actually occurs.

Using the 6/7 ladder position — a threshold with no meaning for finals or home advantage.

Why it matters
- A valid RDD should only show a jump at the true cutoff.
- If you see a jump at a fake cutoff, it means your model is generating spurious discontinuities.

So this check asks: Does the model falsely detect a jump where none should exist?


## 3. Robustness Table

| Specification        | Estimate | Std. Error |
|----------------------|----------|------------|
| **Top‑4 Cutoff**     |          |            |
| Main (1–8)           | 4,049.5  | 8,292.0    |
| Narrow (3–6)         | -12,970.9| 13,157.2   |
| Wide (1–10)          | 2,848.7  | 7,423.6    |
| **Finals Cutoff**    |          |            |
| Main (5–10)          | -9,738.2 | 10,201.1   |
| Narrow (7–10)        | 5,295.1  | 12,294.3   |
| Wide (5–12)          | -1,847.7 | 8,270.1    |
| **Placebo (6–7)**    | -4,271.5 | 6,267.6    |


## 4. Interpretation of Robustness Checks

The robustness checks reinforce the main RDD finding: there is no evidence of a causal jump in club membership at either the Top‑4 or Finals qualification thresholds. Across all bandwidths, the estimated treatment effects vary in sign and magnitude, and all are imprecisely estimated with large standard errors. Narrow windows (3–6 and 7–10) do not reveal any local discontinuity, and widening the bandwidth does not stabilise the estimates. The placebo test at the non‑meaningful 6/7 cutoff also produces a noisy, insignificant estimate, suggesting the design does not mechanically generate false discontinuities. Taken together, these results indicate that membership does not respond discontinuously to crossing either ladder threshold, and the null effect is robust to alternative specifications.

In other words:

Fans don’t sign up in a sudden jump just because their team finishes 4th instead of 5th, or 8th instead of 9th.

Membership changes are driven by longer‑term factors, not these specific ladder thresholds.




## Final Credibility Statement

Across all three robustness checks, the main null result consistently held. The Top‑4 cutoff estimates were unstable across bandwidths—changing sign and magnitude while remaining imprecise—which is exactly the pattern you see when there is no underlying discontinuity, strengthening confidence that finishing 4th rather than 5th does not causally shift membership. The Finals cutoff behaved the same way: across main, narrow, and wide windows, the estimates again flipped sign and remained statistically weak, showing that the null result is not specific to one threshold but generalises across different definitions of “treatment,” which increases credibility. Finally, the placebo cutoff produced a noisy, insignificant estimate, as a valid design should; the absence of a fake jump at a meaningless threshold confirms that the RDD is not spuriously generating discontinuities. Taken together, the surviving pattern across all checks reinforces the credibility of the main finding: there is no causal membership jump at any ladder threshold.
