"""
Peak Unemployment Analysis - Identify and analyze peak periods
"""
import pandas as pd

df = pd.read_csv('data/unemployment_cleaned.csv')
df['date'] = pd.to_datetime(df['date'])

print("="*70)
print("PEAK UNEMPLOYMENT ANALYSIS")
print("="*70)

# Find top 10 highest unemployment records
print("\n1. TOP 10 HIGHEST UNEMPLOYMENT RECORDS")
print("-"*70)
top_10 = df.nlargest(10, 'estimated_unemployment_rate_pct')[
    ['date', 'region', 'area', 'estimated_unemployment_rate_pct']
]
for idx, row in top_10.iterrows():
    print(f"{row['date'].strftime('%b %Y'):<12} | {row['region']:<18} | {row['area']:<7} | {row['estimated_unemployment_rate_pct']:>6.2f}%")

# State-wise peak
print("\n2. PEAK UNEMPLOYMENT BY STATE")
print("-"*70)
for state in sorted(df['region'].unique()):
    state_data = df[df['region'] == state]
    peak = state_data.loc[state_data['estimated_unemployment_rate_pct'].idxmax()]
    print(f"{state:<18} | {peak['date'].strftime('%b %Y'):<12} | {peak['area']:<7} | {peak['estimated_unemployment_rate_pct']:>6.2f}%")

# Monthly peaks
print("\n3. MONTHLY PEAK ANALYSIS")
print("-"*70)
monthly_peaks = df.groupby(df['date'].dt.to_period('M')).agg({
    'estimated_unemployment_rate_pct': ['mean', 'max']
}).round(2)
monthly_peaks.columns = ['Average', 'Peak']
print(monthly_peaks)

print("\n" + "="*70)
