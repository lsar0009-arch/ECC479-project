## Main Result (substantive):  

Across 2012–2026, clubs that finish just inside the finals cutoff (6th–8th) experience a statistically significant increase in next‑season membership relative to clubs finishing just outside (9th–10th). The preferred specification estimates that qualifying for finals from the marginal positions increases membership by ≈ X% (or X members), conditional on club fixed effects, year fixed effects, and controls for stadium capacity, city population, and club age.

## Declaration:  

This is a causal claim. The empirical strategy treats finishing 6th–8th vs 9th–10th as a quasi‑random threshold, analogous to a local comparison around a cutoff. The claim is graded against a local causal effect: the membership impact of barely qualifying for finals.


## 2. Robustness Checks (AFL‑specific)
Below are the checks that genuinely stress‑test your identification strategy.

2.1 Alternative Control Sets
- No controls  
- Only finals‑qualification indicator. Tests whether the effect is entirely driven by controls.

Preferred controls  
- Club FE + year FE + stadium size + city population + club age.

Additional controls  
- Add lagged wins, percentage (for ladder strength), or home‑state GDP. Tests omitted‑variable bias.

2.2 Alternative Samples
- Drop outliers  
- Remove clubs with extreme membership changes (e.g., Hawthorn 2013–2015, Richmond 2017–2019).
- Tests whether dynasties drive the effect.

Restrict to 2015–2026  
- Period with stable membership reporting standards.

Exclude expansion clubs  
- Removes GWS and Gold Coast, whose membership dynamics differ structurally.

2.3 Alternative Functional Forms
- Log membership  
- Converts effect into elasticities.

IHS membership  
- Handles zeros and skewness.

Quadratic ladder position  
- Tests whether the effect is nonlinear around the cutoff.

2.4 Alternative Inference
- HC‑robust SEs

- Cluster at club level  
    - Justified because membership shocks are serially correlated within clubs.

- Cluster at state level  
     - Tests sensitivity to broader geographic correlation.



2.5 Identification‑Relevant Check (Required for Causal Claim)

Placebo Threshold Test
- Use 5th vs 11th, or 4th vs 12th, where finals qualification is not at stake.
- If the effect disappears, it supports the causal interpretation.

Bandwidth Sensitivity
- Estimate using only clubs finishing 7th–9th, then 6th–10th, then 5th–11th.
- A causal threshold effect should be strongest in the narrowest window.

Pre‑trend Check
- Test whether clubs finishing 6th–8th already had higher pre‑treatment membership growth.
- If pre‑trends are flat, the causal claim strengthens.



## 3. Robustness Table



## 4. Interpretation of Robustness Checks



## Final Credibility Statement
