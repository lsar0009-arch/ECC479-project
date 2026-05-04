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


## Identification strategy (if causal)
OLS-with-controls, FE, DiD, RDD, etc., plus required assumptions.



## Regression table  
Clean, formatted, not raw software output.



## Interpretation  
Direction, magnitude, units, what is held constant.




## Threats / limitations  
OVB, selection, reverse causality, measurement, sample selection.




## Reproducibility  
Pipeline: raw → clean → analysis → results.