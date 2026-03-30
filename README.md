# ECC3479-project
Research Question: Does crossing the AFL finals qualification threshold — comparing clubs finishing 6th–8th versus 9th–10th — generate a measurably different impact on club membership tallies?

Why is it economically relevant?

Membership is one of the main sources, if not the main source of revenue for AFL clubs.
Revenue for AFL teams directly contributes to;
- Financial stability
- Club operations
- Investment in facilities, staP, and players
If found to be true, it demonstrates how on-field performance translates to an economic payoff.


Data:

Membership data
- Total club membership numbers, year on year
- Total membership number, year on year
Team performance data
- Did the team play finals?
- Ladder position
- Number of wins
Control variables
- Stadium size
- City populations
- Teams’ years in league (history)
Time
- Last 15 years (2012-2026)

Afltables.com.au

AFL.com.au

Empirical Strategy
This project estimates whether crossing the AFL finals qualification threshold causes a measurable change in club membership numbers by comparing teams that finish just inside the cutoff (6th–8th) with those that finish just outside it (9th–10th). Because clubs near the threshold are typically similar in underlying quality, resources, and supporter engagement, their relative position around the cutoff can be treated as quasi‑random. This creates a natural experiment where qualifying for finals acts as the “treatment” and narrowly missing out serves as the “control.” By analysing differences in subsequent membership tallies—using simple comparisons and regression‑based adjustments—we aim to isolate the causal impact of finals participation on fan behaviour and club revenue.



REPOSITORY STRUCTURE

README.md
data/raw/ <- source files, never edited
data/clean/ <- cleaned versions produced by code
src/ <- all analysis scripts
outputs/ <- tables, figures
docs/ <- notes and documentation


## Software Requirements
- Python 3.14.3
- Required packages:
  - pip
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - statsmodels

Install all packages with:
pip install -r requirements.txt


Raw Data Sources


Ladder data: manually transcribed from AFL.com.au into Excel, then exported to CSV (ladder_raw.csv) and placed in data/raw/