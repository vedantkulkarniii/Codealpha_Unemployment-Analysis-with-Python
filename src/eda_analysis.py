"""
Exploratory Data Analysis - Statistical Analysis
Day 3
"""
import pandas as pd
import numpy as np

# Load cleaned data
df = pd.read_csv('data/unemployment_cleaned.csv')
df['date'] = pd.to_datetime(df['date'])

print("="*70)
print("EXPLORATORY DATA ANALYSIS - STATISTICAL SUMMARY")
print("="*70)

# Overall Unemployment Statistics
print("\n1. OVERALL UNEMPLOYMENT STATISTICS")
print("-" * 70)
print(f"Mean Unemployment Rate: {df['estimated_unemployment_rate_pct'].mean():.2f}%")
print(f"Median Unemployment Rate: {df['estimated_unemployment_rate_pct'].median():.2f}%")
print(f"Minimum Unemployment Rate: {df['estimated_unemployment_rate_pct'].min():.2f}%")
print(f"Maximum Unemployment Rate: {df['estimated_unemployment_rate_pct'].max():.2f}%")
print(f"Standard Deviation: {df['estimated_unemployment_rate_pct'].std():.2f}%")
print(f"25th Percentile: {df['estimated_unemployment_rate_pct'].quantile(0.25):.2f}%")
print(f"75th Percentile: {df['estimated_unemployment_rate_pct'].quantile(0.75):.2f}%")

# State-wise Analysis
print("\n2. STATE-WISE UNEMPLOYMENT ANALYSIS")
print("-" * 70)
state_stats = df.groupby('region')['estimated_unemployment_rate_pct'].agg([
    ('Mean', 'mean'),
    ('Median', 'median'),
    ('Min', 'min'),
    ('Max', 'max'),
    ('Std', 'std')
]).round(2).sort_values('Mean')
print(state_stats)

print("\nHighest Unemployment States:")
top_states = state_stats.nlargest(3, 'Mean')
for idx, (state, row) in enumerate(top_states.iterrows(), 1):
    print(f"  {idx}. {state}: {row['Mean']:.2f}% (Max: {row['Max']:.2f}%)")

print("\nLowest Unemployment States:")
bottom_states = state_stats.nsmallest(3, 'Mean')
for idx, (state, row) in enumerate(bottom_states.iterrows(), 1):
    print(f"  {idx}. {state}: {row['Mean']:.2f}% (Min: {row['Min']:.2f}%)")

# Year-wise Analysis
print("\n3. YEAR-WISE UNEMPLOYMENT ANALYSIS")
print("-" * 70)
year_stats = df.groupby('year')['estimated_unemployment_rate_pct'].agg([
    ('Mean', 'mean'),
    ('Median', 'median'),
    ('Min', 'min'),
    ('Max', 'max')
]).round(2)
print(year_stats)

change_2019_2020 = year_stats.loc[2020, 'Mean'] - year_stats.loc[2019, 'Mean']
print(f"\nYear-over-Year Change (2019 to 2020): {change_2019_2020:+.2f} percentage points")

# Month-wise Analysis
print("\n4. MONTH-WISE UNEMPLOYMENT ANALYSIS")
print("-" * 70)
month_stats = df.groupby('month')['estimated_unemployment_rate_pct'].mean().round(2)
print(month_stats)

print(f"\nHighest Unemployment Month: Month {month_stats.idxmax()} ({month_stats.max():.2f}%)")
print(f"Lowest Unemployment Month: Month {month_stats.idxmin()} ({month_stats.min():.2f}%)")

# Rural vs Urban Analysis
print("\n5. RURAL VS URBAN UNEMPLOYMENT COMPARISON")
print("-" * 70)
area_stats = df.groupby('area')['estimated_unemployment_rate_pct'].agg([
    ('Mean', 'mean'),
    ('Median', 'median'),
    ('Min', 'min'),
    ('Max', 'max')
]).round(2)
print(area_stats)

rural_urban_diff = area_stats.loc['Urban', 'Mean'] - area_stats.loc['Rural', 'Mean']
print(f"\nUrban-Rural Difference: {rural_urban_diff:+.2f} percentage points")
if rural_urban_diff > 0:
    print("→ Urban areas show higher average unemployment")
else:
    print("→ Rural areas show higher average unemployment")

# Labour Participation Analysis
print("\n6. LABOUR PARTICIPATION RATE ANALYSIS")
print("-" * 70)
print(f"Mean Labour Participation: {df['estimated_labour_participation_rate_pct'].mean():.2f}%")
print(f"Median Labour Participation: {df['estimated_labour_participation_rate_pct'].median():.2f}%")
print(f"Range: {df['estimated_labour_participation_rate_pct'].min():.2f}% - {df['estimated_labour_participation_rate_pct'].max():.2f}%")

# COVID Period Analysis
print("\n7. COVID PERIOD COMPARISON")
print("-" * 70)
covid_stats = df.groupby('covid_period')['estimated_unemployment_rate_pct'].agg([
    ('Mean', 'mean'),
    ('Median', 'median'),
    ('Min', 'min'),
    ('Max', 'max')
]).round(2)
print(covid_stats)

pre_covid_mean = covid_stats.loc['Pre-COVID', 'Mean']
covid_mean = covid_stats.loc['COVID', 'Mean']
covid_impact = covid_mean - pre_covid_mean
covid_impact_pct = (covid_impact / pre_covid_mean) * 100

print(f"\nPre-COVID to COVID Change:")
print(f"  Absolute: {covid_impact:+.2f} percentage points")
print(f"  Relative: {covid_impact_pct:+.1f}%")

# Quarterly Analysis
print("\n8. QUARTERLY UNEMPLOYMENT TRENDS")
print("-" * 70)
quarterly_stats = df.groupby('quarter')['estimated_unemployment_rate_pct'].mean().round(2)
print(quarterly_stats)

# State + Area Analysis
print("\n9. STATE AND AREA COMBINATION ANALYSIS")
print("-" * 70)
state_area = df.groupby(['region', 'area'])['estimated_unemployment_rate_pct'].mean().round(2).unstack()
print(state_area)

print("\n" + "="*70)
print("ANALYSIS COMPLETE")
print("="*70)
