"""
Correlation Analysis - Unemployment vs Labour Participation
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('data/unemployment_cleaned.csv')
df['date'] = pd.to_datetime(df['date'])

print("="*70)
print("CORRELATION ANALYSIS")
print("="*70)

# Calculate correlation
corr = df['estimated_unemployment_rate_pct'].corr(df['estimated_labour_participation_rate_pct'])
print(f"\nCorrelation between Unemployment and Labour Participation: {corr:.4f}")

if corr < -0.5:
    strength = "Strong negative"
elif corr < -0.3:
    strength = "Moderate negative"
elif corr < 0:
    strength = "Weak negative"
elif corr < 0.3:
    strength = "Weak positive"
elif corr < 0.5:
    strength = "Moderate positive"
else:
    strength = "Strong positive"

print(f"Relationship strength: {strength}")

# Create scatter plot
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Overall scatter
axes[0].scatter(df['estimated_labour_participation_rate_pct'], 
                df['estimated_unemployment_rate_pct'],
                alpha=0.6, c='#2E86AB')
axes[0].set_xlabel('Labour Participation Rate (%)', fontsize=11)
axes[0].set_ylabel('Unemployment Rate (%)', fontsize=11)
axes[0].set_title(f'Unemployment vs Labour Participation\n(Correlation: {corr:.3f})', 
                  fontsize=12, fontweight='bold')
axes[0].grid(True, alpha=0.3)

# Add trend line
z = np.polyfit(df['estimated_labour_participation_rate_pct'], 
               df['estimated_unemployment_rate_pct'], 1)
p = np.poly1d(z)
x_line = np.linspace(df['estimated_labour_participation_rate_pct'].min(), 
                     df['estimated_labour_participation_rate_pct'].max(), 100)
axes[0].plot(x_line, p(x_line), "r--", alpha=0.8, linewidth=2, label='Trend')
axes[0].legend()

# By COVID period
for period, color in [('Pre-COVID', '#18A558'), ('COVID', '#E63946')]:
    period_data = df[df['covid_period'] == period]
    axes[1].scatter(period_data['estimated_labour_participation_rate_pct'],
                    period_data['estimated_unemployment_rate_pct'],
                    alpha=0.6, label=period, c=color)

axes[1].set_xlabel('Labour Participation Rate (%)', fontsize=11)
axes[1].set_ylabel('Unemployment Rate (%)', fontsize=11)
axes[1].set_title('Unemployment vs Labour Participation\nby COVID Period', 
                  fontsize=12, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('outputs/figures/09_correlation_analysis.png', dpi=300, bbox_inches='tight')
plt.close()
print("\n✓ Visualization saved: 09_correlation_analysis.png")

# Period-wise correlations
print("\nCorrelation by COVID Period:")
for period in ['Pre-COVID', 'COVID']:
    period_data = df[df['covid_period'] == period]
    if len(period_data) > 0:
        period_corr = period_data['estimated_unemployment_rate_pct'].corr(
            period_data['estimated_labour_participation_rate_pct'])
        print(f"  {period}: {period_corr:.4f}")

# Area-wise correlations
print("\nCorrelation by Area:")
for area in ['Rural', 'Urban']:
    area_data = df[df['area'] == area]
    area_corr = area_data['estimated_unemployment_rate_pct'].corr(
        area_data['estimated_labour_participation_rate_pct'])
    print(f"  {area}: {area_corr:.4f}")

print("\n" + "="*70)
