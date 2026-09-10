"""
State-wise Detailed Analysis
"""
import pandas as pd

df = pd.read_csv('data/unemployment_cleaned.csv')
df['date'] = pd.to_datetime(df['date'])

print("="*70)
print("STATE-WISE DETAILED ANALYSIS")
print("="*70)

for state in sorted(df['region'].unique()):
    state_data = df[df['region'] == state]
    
    print(f"\n{'='*70}")
    print(f"STATE: {state.upper()}")
    print(f"{'='*70}")
    
    print(f"\nOverall Statistics:")
    print(f"  Records: {len(state_data)}")
    print(f"  Mean Unemployment: {state_data['estimated_unemployment_rate_pct'].mean():.2f}%")
    print(f"  Std Deviation: {state_data['estimated_unemployment_rate_pct'].std():.2f}%")
    print(f"  Range: {state_data['estimated_unemployment_rate_pct'].min():.2f}% - {state_data['estimated_unemployment_rate_pct'].max():.2f}%")
    
    # Area breakdown if both exist
    areas = state_data['area'].unique()
    if len(areas) > 1:
        print(f"\nRural vs Urban:")
        for area in sorted(areas):
            area_data = state_data[state_data['area'] == area]
            print(f"  {area}: {area_data['estimated_unemployment_rate_pct'].mean():.2f}% average")
    
    # COVID impact
    pre_covid = state_data[state_data['covid_period'] == 'Pre-COVID']
    covid = state_data[state_data['covid_period'] == 'COVID']
    
    if len(pre_covid) > 0 and len(covid) > 0:
        pre_mean = pre_covid['estimated_unemployment_rate_pct'].mean()
        covid_mean = covid['estimated_unemployment_rate_pct'].mean()
        change = covid_mean - pre_mean
        pct_change = (change / pre_mean) * 100
        
        print(f"\nCOVID Impact:")
        print(f"  Pre-COVID Average: {pre_mean:.2f}%")
        print(f"  COVID Average: {covid_mean:.2f}%")
        print(f"  Change: {change:+.2f} pp ({pct_change:+.1f}%)")
    
    # Peak unemployment
    peak_row = state_data.loc[state_data['estimated_unemployment_rate_pct'].idxmax()]
    print(f"\nPeak Unemployment:")
    print(f"  Rate: {peak_row['estimated_unemployment_rate_pct']:.2f}%")
    print(f"  Date: {peak_row['date'].strftime('%B %Y')}")
    print(f"  Area: {peak_row['area']}")

print(f"\n{'='*70}")
print("ANALYSIS COMPLETE")
print(f"{'='*70}")
