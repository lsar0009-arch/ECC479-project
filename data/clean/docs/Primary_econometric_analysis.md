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