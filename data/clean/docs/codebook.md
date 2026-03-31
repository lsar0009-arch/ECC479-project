1. team
Type: string

Meaning: AFL club name

Construction: Copied directly from ladder_raw.csv and matched to membership dataset

2. year
Type: integer

Meaning: Season year

Construction: Extracted from raw ladder and membership files

3. ladder_position
Type: integer (1–18)

Meaning: Final ladder rank

Construction: Manually transcribed from AFL.com.au

4. membership_total
Type: integer

Meaning: Total club membership for that year

Construction: Combined from FootyIndustry (2012–2024) + AFL.com.au (2025)

5. finals_qualified
Type: binary (1 = yes, 0 = no)

Meaning: Whether the club made finals

Construction: 1 if ladder_position ≤ 8

6. treatment_group
Type: binary

Meaning: Clubs finishing 6th–8th

Construction: 1 if 6 ≤ ladder_position ≤ 8

7. control_group
Type: binary

Meaning: Clubs finishing 9th–10th

Construction: 1 if 9 ≤ ladder_position ≤ 10