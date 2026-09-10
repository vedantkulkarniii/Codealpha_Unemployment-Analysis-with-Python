"""
COVID-19 Impact Visualizations
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('data/unemployment_cleaned.csv')
df['date'] = pd.to_datetime(df['date'])

print("Generating COVID-19 impact visualizations...")

# 1. COVID Timeline with phases
fig, ax = plt.subplots(figsize=(14, 7))
daily_avg = df.groupby('date')['estimated_unemployment_rate_pct'].mean().reset_index()

colors = []
for date in daily_avg['date']:
    if date < pd.to_datetime('2020-03-01'):
        colors.append('#18A558')  # Green for Pre-COVID
    elif date <= pd.to_datetime('2020-12-31'):
        colors.append('#E63946')  # Red for COVID
    else:
        colors.append('#2E86AB')  # Blue for Post-COVID

ax.bar(daily_avg['date'], daily_avg['estimated_unemployment_rate_pct'], 
       color=colors, alpha=0.7, edgecolor='black', linewidth=0.5)
ax.axvline(pd.to_datetime('2020-03-01'), color='black', linestyle='--', linewidth=2, alpha=0.7)
ax.set_title('Unemployment Timeline: Pre-COVID vs COVID vs Post-COVID', fontsize=14, fontweight='bold')
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Unemployment Rate (%)', fontsize=12)
ax.grid(True, alpha=0.3, axis='y')
ax.legend(['COVID Start (Mar 2020)', 'Pre-COVID', 'COVID', 'Post-COVID'], loc='upper left')
plt.tight_layout()
plt.savefig('outputs/figures/11_covid_timeline.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Generated: 11_covid_timeline.png")

# 2. Pre-COVID vs COVID comparison
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

periods = ['Pre-COVID', 'COVID']
colors_comp = ['#18A558', '#E63946']

for idx, period in enumerate(periods):
    period_data = df[df['covid_period'] == period]
    state_avg = period_data.groupby('region')['estimated_unemployment_rate_pct'].mean().sort_values()
    
    axes[idx].barh(state_avg.index, state_avg.values, color=colors_comp[idx], alpha=0.8, edgecolor='black')
    axes[idx].set_title(f'{period} Period', fontsize=12, fontweight='bold')
    axes[idx].set_xlabel('Unemployment Rate (%)', fontsize=11)
    axes[idx].grid(True, alpha=0.3, axis='x')
    axes[idx].set_xlim(0, 25)

plt.tight_layout()
plt.savefig('outputs/figures/12_pre_covid_vs_covid_comparison.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Generated: 12_pre_covid_vs_covid_comparison.png")

# 3. State-wise COVID impact
pre_covid = df[df['covid_period'] == 'Pre-COVID']
covid = df[df['covid_period'] == 'COVID']

state_impact = []
for state in df['region'].unique():
    pre_mean = pre_covid[pre_covid['region'] == state]['estimated_unemployment_rate_pct'].mean()
    covid_mean = covid[covid['region'] == state]['estimated_unemployment_rate_pct'].mean()
    impact = covid_mean - pre_mean
    state_impact.append({'state': state, 'impact': impact})

impact_df = pd.DataFrame(state_impact).sort_values('impact', ascending=True)

plt.figure(figsize=(10, 6))
colors_impact = ['#E63946' if x > 0 else '#18A558' for x in impact_df['impact']]
plt.barh(impact_df['state'], impact_df['impact'], color=colors_impact, alpha=0.8, edgecolor='black')
plt.axvline(0, color='black', linestyle='-', linewidth=1)
plt.title('COVID-19 Impact by State\n(Change in Unemployment Rate)', fontsize=14, fontweight='bold')
plt.xlabel('Change in Unemployment Rate (percentage points)', fontsize=12)
plt.ylabel('State', fontsize=12)
plt.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.savefig('outputs/figures/13_state_covid_impact.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Generated: 13_state_covid_impact.png")

# 4. Monthly COVID progression
covid_data = df[df['covid_period'] == 'COVID'].copy()
monthly_covid = covid_data.groupby(covid_data['date'].dt.to_period('M'))['estimated_unemployment_rate_pct'].mean()

plt.figure(figsize=(12, 6))
x_pos = range(len(monthly_covid))
bars = plt.bar(x_pos, monthly_covid.values, color='#E63946', alpha=0.8, edgecolor='black')

# Highlight peak
peak_idx = monthly_covid.values.argmax()
bars[peak_idx].set_color('#8B0000')
bars[peak_idx].set_alpha(1.0)

plt.xticks(x_pos, [str(m) for m in monthly_covid.index], rotation=45)
plt.title('Monthly Unemployment During COVID Period (Mar-Nov 2020)', fontsize=14, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Average Unemployment Rate (%)', fontsize=12)
plt.grid(True, alpha=0.3, axis='y')
plt.axhline(monthly_covid.mean(), color='blue', linestyle='--', label=f'COVID Average: {monthly_covid.mean():.2f}%')
plt.legend()
plt.tight_layout()
plt.savefig('outputs/figures/14_monthly_covid_progression.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Generated: 14_monthly_covid_progression.png")

# 5. Rural vs Urban COVID impact
fig, ax = plt.subplots(figsize=(10, 6))

categories = ['Pre-COVID', 'COVID']
rural_vals = [
    pre_covid[pre_covid['area'] == 'Rural']['estimated_unemployment_rate_pct'].mean(),
    covid[covid['area'] == 'Rural']['estimated_unemployment_rate_pct'].mean()
]
urban_vals = [
    pre_covid[pre_covid['area'] == 'Urban']['estimated_unemployment_rate_pct'].mean(),
    covid[covid['area'] == 'Urban']['estimated_unemployment_rate_pct'].mean()
]

x = np.arange(len(categories))
width = 0.35

bars1 = ax.bar(x - width/2, rural_vals, width, label='Rural', color='#8B4513', alpha=0.8, edgecolor='black')
bars2 = ax.bar(x + width/2, urban_vals, width, label='Urban', color='#4169E1', alpha=0.8, edgecolor='black')

ax.set_ylabel('Unemployment Rate (%)', fontsize=12)
ax.set_title('Rural vs Urban Unemployment: Pre-COVID vs COVID', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
ax.grid(True, alpha=0.3, axis='y')

# Add value labels on bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('outputs/figures/15_rural_urban_covid_impact.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Generated: 15_rural_urban_covid_impact.png")

# 6. Labour participation during COVID
labour_data = df.groupby(['date', 'covid_period']).agg({
    'estimated_unemployment_rate_pct': 'mean',
    'estimated_labour_participation_rate_pct': 'mean'
}).reset_index()

fig, axes = plt.subplots(2, 1, figsize=(14, 10))

# Unemployment
for period, color in [('Pre-COVID', '#18A558'), ('COVID', '#E63946')]:
    period_data = labour_data[labour_data['covid_period'] == period]
    axes[0].plot(period_data['date'], period_data['estimated_unemployment_rate_pct'],
                 label=period, linewidth=2, marker='o', markersize=4, color=color)

axes[0].axvline(pd.to_datetime('2020-03-01'), color='black', linestyle='--', alpha=0.7)
axes[0].set_title('Unemployment Rate by COVID Period', fontsize=13, fontweight='bold')
axes[0].set_ylabel('Unemployment Rate (%)', fontsize=11)
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Labour Participation
for period, color in [('Pre-COVID', '#18A558'), ('COVID', '#E63946')]:
    period_data = labour_data[labour_data['covid_period'] == period]
    axes[1].plot(period_data['date'], period_data['estimated_labour_participation_rate_pct'],
                 label=period, linewidth=2, marker='s', markersize=4, color=color)

axes[1].axvline(pd.to_datetime('2020-03-01'), color='black', linestyle='--', alpha=0.7)
axes[1].set_title('Labour Participation Rate by COVID Period', fontsize=13, fontweight='bold')
axes[1].set_xlabel('Date', fontsize=11)
axes[1].set_ylabel('Labour Participation Rate (%)', fontsize=11)
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('outputs/figures/16_labour_participation_covid.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Generated: 16_labour_participation_covid.png")

print("\n" + "="*60)
print("All COVID-19 visualizations generated successfully!")
print("="*60)
