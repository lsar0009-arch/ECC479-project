## Declaration  

This is a causal analysis.  
I aim to estimate the causal effect of crossing the AFL finals qualification threshold on subsequent club membership tallies. Clubs finishing just inside the cutoff (6th–8th) are compared with clubs finishing just outside it (9th–10th). This design treats finals qualification as a treatment and uses near‑threshold comparisons to approximate a quasi‑experimental setting.


## Econometric specification  

I estimate a linear regression model of club membership on finals qualification status:

>membership_total𝑖𝑡 = 𝛼 + 𝛽Qualified𝑖𝑡 − 1+ 𝛾′𝑋𝑖𝑡−1 +𝜇𝑖 + 𝜆𝑡 + 𝜀𝑖𝑡 >
where 𝑖 indexes clubs and 𝑡 seasons.

Regressors

Qualified𝑖𝑡−1: Indicator equal to 1 if club 𝑖 qualified for finals in season 𝑡−1 (finished 1st–8th), 0 otherwise. This is the treatment variable of interest.

𝑋𝑖𝑡−1: Vector of lagged controls (e.g., ladder position, percentage, previous membership level) capturing underlying club strength and size.

𝜇𝑖: Club fixed effects, absorbing time‑invariant club characteristics (history, market size, brand).

𝜆𝑡: Year fixed effects, capturing league‑wide shocks (rule changes, macro conditions, AFL‑wide membership trends).

Sample  
The main specification restricts the sample to clubs finishing between 6th and 10th on the ladder in a given year. This focuses on teams near the finals threshold, improving comparability between treated (6th–8th) and control (9th–10th) clubs and aligning with the causal interpretation of a near‑cutoff design.

Error structure  
Standard errors are clustered at the club level to allow for arbitrary serial correlation and heteroskedasticity within clubs over time.

- Arbitrary serial correlation: The residuals for a given club may move together over time in any way, and we make no assumptions about the structure of that correlation.
- Heteroskedasticity: the spread of the residuals changes depending on the value of the predictors or across groups.


Brief justification  
A linear fixed‑effects model is appropriate because the outcome (membership totals) is continuous and we are interested in an average treatment effect of finals qualification. Club fixed effects control for time‑invariant differences across clubs, while year fixed effects absorb common shocks. Restricting the sample to 6th–10th placed clubs approximates a quasi‑experimental comparison around the finals cutoff, supporting a causal interpretation of 𝛽 as the effect of crossing the finals qualification threshold on subsequent membership.


## Identification strategy 

OLS-with-controls

With an OLS‑with‑controls design, we can estimate the causal effect by:
- Regressing the outcome on the treatment
- Adding control variables that absorb confounding variation
- Relying on a conditional exogeneity assumption to interpret the coefficient causally.

The treatment group consists of clubs finishing 6th–8th, and the control group consists of clubs finishing 9th–10th. By restricting the sample to this narrow window, the design approximates a quasi‑experimental comparison around the finals cutoff.

Key assumption (Conditional Exogeneity): after controlling for lagged performance, lagged membership, club fixed effects, and year fixed effects, finals qualification is uncorrelated with unobserved determinants of membership.

Why this assumption is plausible
- Clubs finishing 6th–10th are extremely similar in underlying strength, often separated by one win or percentage.
- Supporter sentiment and club fundamentals evolve smoothly with ladder position; nothing else jumps at the 8th‑place cutoff.
- Lagged controls absorb performance trends and club size.
- Club fixed effects remove time‑invariant differences (market size, supporter base, history).
- Year fixed effects remove league‑wide shocks.

Together, these features make conditional exogeneity credible.



## Regression table and its interpretation  

## Model: Membership ~ Ladder Position (full sample)

Interpretation
Direction: The coefficient is negative (–958.90), meaning worse ladder positions are associated with lower membership.

Magnitude: Each one‑place drop on the ladder is associated with ~959 fewer members.

Units: Members per ladder position.

Significance: Statistically significant (p = 0.0015).

Holding constant: Again, nothing is held constant — simple OLS with HC3 robust errors.

Meaning
Across the full league, better‑performing teams tend to have higher membership — but the effect is small (R² = 0.044). Performance explains only ~4% of membership variation.



## Model: Membership ~ Ladder Position (positions 1–4 only)

Interpretation
Direction: The coefficient is negative (–858), meaning worse ladder positions are associated with lower membership.

Magnitude: A one‑place drop corresponds to ~858 fewer members.

Units: Members per ladder position.

Significance: Not significant (p = 0.771).

Holding constant: Nothing — simple OLS with HC3 robust errors.

Meaning
Among top‑performing clubs, ladder position has no meaningful relationship with membership. These clubs already have large, stable supporter bases.



## Model: Membership ~ Ladder Position (positions 5–8 only)

Interpretation
Direction: The coefficient on ladder position is positive (+350.77), meaning that worse ladder positions (higher numbers) are associated with slightly higher membership — but this is almost certainly noise.

Magnitude: A one‑place drop on the ladder is associated with +351 members, on average.

Units: Membership is measured in number of members; ladder position is measured in rank places.

Significance: Not significant (p = 0.890). This is pure noise; the model explains 0% of variation (R² ≈ 0.0004).

Holding constant: Nothing is held constant — this is a simple bivariate OLS with HC3 robust errors.


## Model: Membership ~ Ladder Position (positions 9–10 only)

Interpretation
Direction: The coefficient is negative (–10,223), meaning worse ladder positions are associated with lower membership.

Magnitude: A one‑place drop is associated with ~10,223 fewer members.

Units: Members per ladder position.

Significance: Not significant (p = 0.192).

Holding constant: Nothing — simple OLS with HC3 robust errors.

Meaning
Among clubs finishing 9th–10th, there is no statistically reliable relationship between ladder position and membership. The large coefficient is unstable due to the tiny sample (28 obs).


## Model: Membership ~ Ladder Position (positions 11–18 only)

Interpretation
Direction: The coefficient is negative (–2,018), meaning worse ladder positions are associated with lower membership.

Magnitude: Each one‑place drop corresponds to ~2,018 fewer members.

Units: Members per ladder position.

Significance: Marginal (p = 0.081).

Holding constant: Nothing — simple OLS with HC3 robust errors.

Meaning
Among lower‑ranked teams, there is a weak negative relationship between performance and membership, but it is not statistically strong.



## Threats / limitations  

Most plausible threat: Omitted variable bias from unobserved club momentum  
A key threat is that clubs finishing 6th–8th may have underlying positive momentum (e.g., improving list quality, coaching stability, rising supporter sentiment) that is not fully captured by lagged ladder position or lagged membership.

Sign of the bias: This would bias the estimated treatment effect upwards.
If momentum both increases the probability of qualifying for finals and independently boosts next‑year membership, then part of the estimated effect of finals qualification would actually reflect underlying momentum rather than the treatment itself.

What to do about it:
- restricted the sample to 6th–10th, where clubs are extremely similar in underlying strength, reducing variation in momentum.
- include a lagged ladder position to absorb performance trends.
- include a lagged membership to absorb supporter‑base trends.
- use club fixed effects to remove time‑invariant differences (market size, supporter base, history).
- use year fixed effects to absorb league‑wide shocks.

These steps reduce, but cannot fully eliminate, the risk that unobserved momentum drives both finals qualification and membership growth.


Secondary Threats

Reverse causality (unlikely but possible)  
Membership cannot affect past ladder position, but strong membership bases may indirectly support better performance (via resources, facilities, recruitment).
- Sign: Would bias the estimate downwards if large clubs tend to finish higher but also have less room to grow membership.
- Mitigation: Using lagged membership and restricting to 6th–10th reduces this channel.

Measurement error in membership  
AFL membership definitions vary slightly across clubs and years.
- Sign: Likely attenuates effects towards zero.
- Mitigation: Using official AFL‑published totals and year fixed effects reduces inconsistency.



