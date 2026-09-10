"""
Rural vs Urban Detailed Comparison
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/unemployment_cleaned.csv')
df['date'] = pd.to_datetime(df['date'])

print("="*70)
print("RURAL VS URBAN DETAILED COMPARISON")
print("="*70)

# Overall comparison
print("\n1. OVERALL COMPARISON")
print("-"*70)
for area in ['Rural', 'Urban']:
    area_data = df[df['area'] == area]
    print(f"\n{area}:")
    print(f"  Records: {len(area_data)}")
    print(f"  Mean: {area_data['estimated_unemployment_rate_pct'].mean():.2f}%")
    print(f"  Median: {area_data['estimated_unemployment_rate_pct'].median():.2f}%")
    print(f"  Min: {area_data['estimated_unemployment_rate_pct'].min():.2f}%")
    print(f"  Max: {area_data['estimated_unemployment_rate_pct'].max():.2f}%")
    print(f"  Labour Participation: {area_data['estimated_labour_participation_rate_pct'].mean():.2f}%")

# COVID period comparison
print("\n2. COVID PERIOD COMPARISON")
print("-"*70)
for period in ['Pre-COVID', 'COVID']:
    print(f"\n{period}:")
    for area in ['Rural', 'Urban']:
        area_period = df[(df['area'] == area) & (df['covid_period'] == period)]
        if len(area_period) > 0:
            print(f"  {area}: {area_period['estimated_unemployment_rate_pct'].mean():.2f}%")

# Monthly trends
print("\n3. MONTHLY TRENDS")
print("-"*70)
monthly = df.groupby(['month', 'area'])['estimated_unemployment_rate_pct'].mean().unstack()
print(monthly.round(2))

# Create visualization
plt.figure(figsize=(12, 6))
for area in ['Rural', 'Urban']:
    area_monthly = df[df['area'] == area].groupby('month')['estimated_unemployment_rate_pct'].mean()
    plt.plot(area_monthly.index, area_monthly.values, marker='o', label=area, linewidth=2)

plt.title('Rural vs Urban Monthly Unemployment Patterns', fontsize=14, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Average Unemployment Rate (%)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(range(1, 12))
plt.tight_layout()
plt.savefig('outputs/figures/08_area_monthly_comparison.png', dpi=300, bbox_inches='tight')
plt.close()
print("\n✓ Visualization saved: 08_area_monthly_comparison.png")

print("\n" + "="*70)
