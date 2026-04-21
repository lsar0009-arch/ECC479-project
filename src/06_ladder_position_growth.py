import pandas as pd
import numpy as np

# Load the merged dataset
df = pd.read_csv('/Users/luissari/Desktop/Ecc3479/ECC479-project/data/clean/merged_data_2012_2025.csv')

# Sort by club and year to calculate growth rates
df_sorted = df.sort_values(['club', 'year']).reset_index(drop=True)

# Calculate year-to-year membership growth within each club
df_sorted['membership_growth'] = df_sorted.groupby('club')['membership'].diff()
df_sorted['membership_growth_rate'] = (df_sorted['membership_growth'] / df_sorted.groupby('club')['membership'].shift()) * 100

# For each ladder position, calculate average growth rate (excluding NaN from first year of each club)
growth_by_position = df_sorted[df_sorted['membership_growth_rate'].notna()].groupby('ladder_position').agg({
    'membership_growth_rate': ['mean', 'median', 'std', 'count'],
    'membership': 'mean'
}).round(2)

growth_by_position.columns = ['Avg Growth Rate (%)', 'Median Growth Rate (%)', 'Std Dev (%)', 'Count', 'Avg Membership']

print("MEMBERSHIP GROWTH RATE BY LADDER POSITION (2012-2025)")
print("=" * 80)
print(growth_by_position.sort_index())
print("\n")

# Also create a detailed view
print("DETAILED GROWTH STATISTICS BY POSITION")
print("=" * 80)
for pos in sorted(df_sorted['ladder_position'].unique()):
    subset = df_sorted[df_sorted['ladder_position'] == pos]
    growth_subset = subset[subset['membership_growth_rate'].notna()]
    
    if len(growth_subset) > 0:
        print(f"\nPosition {pos}:")
        print(f"  Observations: {len(growth_subset)}")
        print(f"  Average Growth Rate: {growth_subset['membership_growth_rate'].mean():.2f}%")
        print(f"  Median Growth Rate: {growth_subset['membership_growth_rate'].median():.2f}%")
        print(f"  Std Dev: {growth_subset['membership_growth_rate'].std():.2f}%")
        print(f"  Min Growth: {growth_subset['membership_growth_rate'].min():.2f}%")
        print(f"  Max Growth: {growth_subset['membership_growth_rate'].max():.2f}%")
        print(f"  Avg Membership: {growth_subset['membership'].mean():.0f}")

# Save results to CSV
output_path = '/Users/luissari/Desktop/Ecc3479/ECC479-project/outputs/membership_growth_by_ladder_position.csv'
growth_by_position.to_csv(output_path)
print(f"\n\nResults saved to: {output_path}")
