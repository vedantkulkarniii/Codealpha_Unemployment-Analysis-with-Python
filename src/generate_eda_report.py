"""
Generate comprehensive EDA report combining all analyses
"""
import pandas as pd
from datetime import datetime

df = pd.read_csv('data/unemployment_cleaned.csv')
df['date'] = pd.to_datetime(df['date'])

report = []
report.append("="*80)
report.append("UNEMPLOYMENT ANALYSIS - COMPREHENSIVE EDA REPORT")
report.append("="*80)
report.append(f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
report.append(f"Analysis Period: {df['date'].min().strftime('%B %Y')} to {df['date'].max().strftime('%B %Y')}")
report.append(f"Total Records: {len(df)}")
report.append(f"States Analyzed: {len(df['region'].unique())}")

report.append("\n" + "-"*80)
report.append("EXECUTIVE SUMMARY")
report.append("-"*80)

# Key metrics
avg_unemp = df['estimated_unemployment_rate_pct'].mean()
pre_covid = df[df['covid_period'] == 'Pre-COVID']['estimated_unemployment_rate_pct'].mean()
covid = df[df['covid_period'] == 'COVID']['estimated_unemployment_rate_pct'].mean()
increase = covid - pre_covid
pct_increase = (increase / pre_covid) * 100

report.append(f"\n1. OVERALL UNEMPLOYMENT: {avg_unemp:.2f}%")
report.append(f"   - Pre-COVID Average: {pre_covid:.2f}%")
report.append(f"   - COVID Average: {covid:.2f}%")
report.append(f"   - Increase: +{increase:.2f} pp (+{pct_increase:.1f}%)")

report.append(f"\n2. PEAK UNEMPLOYMENT: {df['estimated_unemployment_rate_pct'].max():.2f}%")
peak_row = df.loc[df['estimated_unemployment_rate_pct'].idxmax()]
report.append(f"   - Date: {peak_row['date'].strftime('%B %Y')}")
report.append(f"   - Location: {peak_row['region']}, {peak_row['area']}")

report.append(f"\n3. MOST AFFECTED STATE: {df.groupby('region')['estimated_unemployment_rate_pct'].mean().idxmax()}")
report.append(f"   - Average: {df.groupby('region')['estimated_unemployment_rate_pct'].mean().max():.2f}%")

report.append(f"\n4. LEAST AFFECTED STATE: {df.groupby('region')['estimated_unemployment_rate_pct'].mean().idxmin()}")
report.append(f"   - Average: {df.groupby('region')['estimated_unemployment_rate_pct'].mean().min():.2f}%")

report.append(f"\n5. URBAN VS RURAL:")
urban_avg = df[df['area'] == 'Urban']['estimated_unemployment_rate_pct'].mean()
rural_avg = df[df['area'] == 'Rural']['estimated_unemployment_rate_pct'].mean()
report.append(f"   - Urban: {urban_avg:.2f}%")
report.append(f"   - Rural: {rural_avg:.2f}%")
report.append(f"   - Difference: {urban_avg - rural_avg:+.2f} pp")

report.append("\n" + "-"*80)
report.append("ANALYSIS COMPONENTS COMPLETED")
report.append("-"*80)
report.append("\n✓ Overall statistical analysis")
report.append("✓ State-wise detailed analysis")
report.append("✓ Temporal trend analysis")
report.append("✓ Rural vs urban comparison")
report.append("✓ Correlation analysis")
report.append("✓ Peak unemployment identification")
report.append("✓ Time series analysis with moving averages")
report.append("✓ COVID-19 impact quantification")
report.append("✓ 10 professional visualizations")
report.append("✓ Comprehensive documentation")

report.append("\n" + "-"*80)
report.append("FILES GENERATED")
report.append("-"*80)
report.append("\nAnalysis Scripts:")
report.append("  - src/eda_analysis.py")
report.append("  - src/state_analysis.py")
report.append("  - src/area_comparison.py")
report.append("  - src/correlation_analysis.py")
report.append("  - src/time_series_analysis.py")
report.append("  - src/peak_analysis.py")

report.append("\nDocumentation:")
report.append("  - docs/EDA_FINDINGS.md")
report.append("  - docs/SUMMARY_STATISTICS.md")
report.append("  - docs/DATA_QUALITY_REPORT.md")
report.append("  - docs/VISUALIZATION_INDEX.md")

report.append("\nVisualizations:")
for i in range(1, 11):
    report.append(f"  - outputs/figures/{i:02d}_*.png")

report.append("\n" + "="*80)
report.append("END OF REPORT - DAY 3 COMPLETE")
report.append("="*80)

# Print and save
report_text = "\n".join(report)
print(report_text)

with open('docs/EDA_COMPREHENSIVE_REPORT.txt', 'w', encoding='utf-8') as f:
    f.write(report_text)

print("\n✓ Report saved to: docs/EDA_COMPREHENSIVE_REPORT.txt")
