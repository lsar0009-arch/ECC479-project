## Declaration  
 
This analysis is causal.
I aim to estimate the causal effect of crossing key AFL ladder thresholds on club membership. Two thresholds are evaluated:

Top 4 vs 5–8 (elite performance threshold)

5–8 vs 9–10 (finals qualification threshold)

Both are implemented using local linear regression discontinuity designs (RDDs), which treat crossing each threshold as a treatment and compare clubs immediately on either side.


## Econometric specification  


2.1 Descriptive specifications (correlations)
I estimate simple OLS regressions of membership on ladder position:


𝑚𝑒𝑚𝑏𝑒𝑟𝑠ℎ𝑖𝑝𝑖=𝛼+𝛿𝑙𝑎𝑑𝑑𝑒𝑟_𝑝𝑜𝑠𝑖𝑡𝑖𝑜𝑛𝑖+𝜀𝑖

These are run:
- on the full sample
- and separately within ladder bands (1–4, 5–8, 9–10, 11–18)

Functional form: linear
Regressors: ladder position only
Sample: varies by band
Error structure: HC3 robust standard errors

Justification:  
These regressions quantify first‑order associations between performance and membership. They are not interpreted causally.


2.2 Causal specifications (RDD models)
For each cutoff, I estimate a local linear RDD:

Model 1 — Top 4 vs 5–8 (cutoff at 4.5)
Define:
- 𝑡𝑜𝑝4𝑖 = 1 if 𝑙𝑎𝑑𝑑𝑒𝑟𝑖 ∈ {1,2,3,4}, 0 
- if 𝑙𝑎𝑑𝑑𝑒𝑟𝑖 ∈ {5,6,7,8} 𝑟𝑢𝑛𝑛𝑖𝑛𝑔𝑖^(4.5) = 𝑙𝑎𝑑𝑑𝑒𝑟𝑖−4.5

𝑚𝑒𝑚𝑏𝑒𝑟𝑠ℎ𝑖𝑝𝑖=𝛼1+𝜏1𝑡𝑜𝑝4𝑖+𝛽1(𝑙𝑎𝑑𝑑𝑒𝑟𝑖−4.5)+𝛾1[𝑡𝑜𝑝4𝑖⋅(𝑙𝑎𝑑𝑑𝑒𝑟𝑖−4.5)]+𝜀𝑖

Model 2 — 5–8 vs 9–10 (cutoff at 8.5)
Define:
- 𝑓𝑖𝑣𝑒_𝑡𝑜_𝑒𝑖𝑔ℎ𝑡𝑖= 1 if 𝑙𝑎𝑑𝑑𝑒𝑟𝑖∈{5,6,7,8}, 0 if 𝑙𝑎𝑑𝑑𝑒𝑟𝑖∈{9,10}
- 𝑟𝑢𝑛𝑛𝑖𝑛𝑔𝑖^(8.5) = 𝑙𝑎𝑑𝑑𝑒𝑟𝑖−8.5

𝑚𝑒𝑚𝑏𝑒𝑟𝑠ℎ𝑖𝑝𝑖=𝛼2+𝜏2𝑓𝑖𝑣𝑒_𝑡𝑜_𝑒𝑖𝑔ℎ𝑡𝑖+𝛽2(𝑙𝑎𝑑𝑑𝑒𝑟𝑖−8.5)+𝛾2[𝑓𝑖𝑣𝑒_𝑡𝑜_𝑒𝑖𝑔ℎ𝑡𝑖⋅(𝑙𝑎𝑑𝑑𝑒𝑟𝑖−8.5)]+𝜀𝑖

where 𝑖 indexes clubs and 𝑡 seasons.

Functional form
- Local linear regression
- Side‑specific slopes via interaction terms
- No higher‑order polynomials

Sample
- RDD 1: ladder positions 1–8
- RDD 2: ladder positions 5–10

Error structure
OLS with conventional standard errors (assignment baseline)

Justification
RDD is appropriate because:
- treatment status changes discretely at known thresholds
- clubs cannot precisely manipulate ladder position
- membership is continuous
- local windows increase comparability


## 3. Identification strategy (causal component)

Design: Regression Discontinuity Design (RDD)

Key assumption: continuity of potential outcomes
- In the absence of treatment, expected membership would evolve smoothly in ladder position around each cutoff:

lim 𝑥↓𝑐𝐸[𝑚𝑒𝑚𝑏𝑒𝑟𝑠ℎ𝑖𝑝∣𝑙𝑎𝑑𝑑𝑒𝑟=𝑥]=lim𝑥↑𝑐𝐸[𝑚𝑒𝑚𝑏𝑒𝑟𝑠ℎ𝑖𝑝∣𝑙𝑎𝑑𝑑𝑒𝑟=𝑥]

Why plausible
- Clubs cannot precisely target 4th or 8th place.
- Supporter sentiment and club fundamentals evolve smoothly with performance.
- Nothing structural changes exactly at the cutoff except the treatment definition.
- Narrow windows (1–8, 5–10) increase comparability.

Under this assumption, any discontinuity at the cutoff is a causal effect.



### 4. Regression Discontinuity Results

| Variable                               | (1) Top 4 vs 5–8      | (2) 5–8 vs 9–10       |
|----------------------------------------|------------------------|------------------------|
| **Treatment effect**                   | 4049.5                | -9738.2               |
|                                        | (8292.0)              | (10200.0)             |
| **Running variable**                   | 350.8                 | -10220.0              |
|                                        | (2559.0)              | (7656.8)              |
| **Interaction term**                   | -1208.9               | 10570.0               |
|                                        | (3618.9)              | (8030.5)              |
| **Constant**                           | 57240.0               | 68380.0               |
|                                        | (5863.4)              | (8560.6)              |
| **N**                                  | 112                   | 84                    |
| **R²**                                 | 0.02                  | 0.022    

Interpretation of main coefficients

RDD 1 — Top 4 vs 5–8
- Direction: positive
- Magnitude: +4,050 members
- Units: members
- Significance: p = 0.626 (not significant)
- Holding constant: distance from cutoff and side‑specific slopes

Interpretation:  
No evidence that entering the Top 4 causes an increase in membership.


RDD 2 — 5–8 vs 9–10
- Direction: negative
- Magnitude: –9,738 members
- Units: members
- Significance: p = 0.343 (not significant)
- Holding constant: distance from cutoff and side‑specific slopes

Interpretation:  
No evidence that qualifying for finals (5–8) causes an increase in membership.


Overall interpretation

Across both thresholds:
- no discontinuities
- no visible jumps in the plots
- very low R²
- slopes do not differ meaningfully

Conclusion:  
There is no causal evidence that marginal improvements in ladder position generate membership growth.


## Threats / limitations  

Most plausible threat: Unobserved club fundamentals and momentum
A key threat to the RDD design is that clubs with strong underlying fundamentals—large supporter bases, strong brands, improving list quality, coaching stability, or rising supporter sentiment—are both more likely to finish above the cutoff and more likely to attract higher membership, independent of the treatment.

Sign and direction of bias:  
This threat would bias the estimated treatment effect upwards.
If stronger clubs are disproportionately on the “treated” side of the cutoff (Top 4 or 5–8), any observed jump in membership could reflect club strength, not the causal effect of crossing the threshold.

What to do about it:
- Use narrow windows around each cutoff (1–8 and 5–10), ensuring clubs on either side are highly comparable in underlying strength.
- Allow separate slopes on each side of the cutoff, reducing functional‑form bias.
- Verify visually that membership trends are smooth in ladder position except at the threshold.
- Check that no visible jump appears in the scatterplots, supporting the continuity assumption.

These steps reduce (but cannot fully eliminate) the risk that unobserved fundamentals drive both ladder position and membership.

Secondary threats

Reverse causality (conceptual but limited here)
Membership cannot affect past ladder position, but clubs with large supporter bases may indirectly support better performance (via resources, facilities, recruitment).
- Sign: would bias estimates upwards, making treated clubs appear to have higher membership even without a causal effect.
- Mitigation: RDD focuses on clubs very close to the cutoff, where small performance differences are plausibly quasi‑random, limiting this channel.

Measurement error in membership
AFL membership definitions vary slightly across clubs and years (e.g., counting 3‑game vs 11‑game packages).
- Sign: likely attenuates any true effect towards zero, making discontinuities harder to detect.
- Mitigation: RDD relies on sharp jumps, not fine‑grained levels, so small definitional inconsistencies are less problematic.



