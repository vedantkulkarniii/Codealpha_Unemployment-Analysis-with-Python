"""
COVID Impact Heatmap Visualizations
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/unemployment_cleaned.csv')
df['date'] = pd.to_datetime(df['date'])

print("Generating COVID impact heatmaps...")

# 1. State-Month COVID Heatmap
covid = df[df['covid_period'] == 'COVID']
pivot_covid = covid.pivot_table(values='estimated_unemployment_rate_pct', 
                                  index='region', 
                                  columns=covid['date'].dt.to_period('M'), 
                                  aggfunc='mean')

plt.figure(figsize=(12, 6))
sns.heatmap(pivot_covid, annot=True, fmt='.1f', cmap='YlOrRd', cbar_kws={'label': 'Unemployment Rate (%)'})
plt.title('State-Month Unemployment Heatmap During COVID Period', fontsize=14, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('State', fontsize=12)
plt.tight_layout()
plt.savefig('outputs/figures/18_covid_state_month_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Generated: 18_covid_state_month_heatmap.png")

# 2. State-Area COVID Impact Heatmap
impact_data = []
pre_covid = df[df['covid_period'] == 'Pre-COVID']

for state in df['region'].unique():
    for area in df['area'].unique():
        pre_val = pre_covid[(pre_covid['region'] == state) & (pre_covid['area'] == area)]['estimated_unemployment_rate_pct'].mean()
        covid_val = covid[(covid['region'] == state) & (covid['area'] == area)]['estimated_unemployment_rate_pct'].mean()
        
        if not pd.isna(pre_val) and not pd.isna(covid_val):
            impact = covid_val - pre_val
            impact_data.append({'State': state, 'Area': area, 'Impact': impact})

impact_df = pd.DataFrame(impact_data)
impact_pivot = impact_df.pivot(index='State', columns='Area', values='Impact')

plt.figure(figsize=(8, 6))
sns.heatmap(impact_pivot, annot=True, fmt='.2f', cmap='Reds', cbar_kws={'label': 'Impact (pp)'})
plt.title('COVID Impact by State and Area\n(Increase in Unemployment Rate)', fontsize=14, fontweight='bold')
plt.xlabel('Area', fontsize=12)
plt.ylabel('State', fontsize=12)
plt.tight_layout()
plt.savefig('outputs/figures/19_covid_impact_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Generated: 19_covid_impact_heatmap.png")

print("\n" + "="*60)
print("COVID heatmaps generated successfully!")
print("="*60)
