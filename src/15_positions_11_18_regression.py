import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import os

# Load merged data
csv_path = '/Users/luissari/Desktop/Ecc3479/ECC479-project/data/clean/merged_data_2012_2025.csv'
df = pd.read_csv(csv_path)

# Filter for positions 11-18
pos_11_18_df = df[df['ladder_position'] >= 11].copy()

# Fit linear regression: membership ~ ladder_position
model = smf.ols('membership ~ ladder_position', data=pos_11_18_df).fit(cov_type='HC3')

# Create output directory
output_dir = '/Users/luissari/Desktop/Ecc3479/ECC479-project/outputs'
os.makedirs(output_dir, exist_ok=True)

# Plot scatter with regression line
plt.figure(figsize=(12, 8))
plt.scatter(pos_11_18_df['ladder_position'], pos_11_18_df['membership'], alpha=0.7, color='steelblue', edgecolor='k', s=80)

# Generate predicted values
x_vals = np.linspace(11, 18, 100)
pred_df = pd.DataFrame({'ladder_position': x_vals})
pred_df['membership'] = model.predict(pred_df)

plt.plot(x_vals, pred_df['membership'], color='red', linewidth=2.5, label='Regression Line')

plt.xlabel('Ladder Position (11-18)')
plt.ylabel('Membership')
plt.title('Linear Regression: Membership vs Ladder Position (Positions 11-18, 2012-2025)')
plt.xticks(range(11, 19))
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()

# Save plot
plot_path = os.path.join(output_dir, 'positions_11_18_regression_plot.png')
plt.savefig(plot_path, dpi=300)
plt.close()

# Save regression summary
summary_path = os.path.join(output_dir, 'positions_11_18_regression_summary.txt')
with open(summary_path, 'w') as f:
    f.write('Linear Regression: Membership ~ Ladder Position (Positions 11-18)\n')
    f.write('=' * 65 + '\n\n')
    f.write(model.summary().as_text())
    f.write('\n\nKey Statistics:\n')
    f.write(f'R-squared: {model.rsquared:.4f}\n')
    f.write(f'Coefficient: {model.params["ladder_position"]:.2f}\n')
    f.write(f'P-value: {model.pvalues["ladder_position"]:.4f}\n')
    f.write(f'Observations: {len(pos_11_18_df)}\n')

print('Regression completed for positions 11-18.')
print(f'Plot saved to: {plot_path}')
print(f'Summary saved to: {summary_path}')
print('\nRegression Summary:')
print(model.summary())
