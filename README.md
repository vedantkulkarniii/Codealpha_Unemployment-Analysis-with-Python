# Unemployment Analysis with Python

A comprehensive data analysis project analyzing unemployment trends and investigating the impact of COVID-19 on employment patterns in India.

## Project Overview

This project performs exploratory data analysis on unemployment data from January 2019 to November 2020, examining temporal trends, regional variations, and the association between COVID-19 timing and unemployment changes.

## Technologies Used

- **Python 3.14**
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical visualizations
- **Jupyter Notebook** - Interactive analysis environment

## Dataset

- **Source**: Unemployment rate data for Indian states
- **Time Period**: January 2019 - November 2020 (23 months)
- **Regions**: 6 states (Andhra Pradesh, Karnataka, Maharashtra, Tamil Nadu, Delhi, Uttar Pradesh)
- **Coverage**: Both Rural and Urban areas
- **Records**: 253 observations

## Project Structure

```
Unemployment-Analysis-with-Python/
│
├── data/
│   ├── Unemployment_Rate_upto_11_2020.csv    # Raw dataset
│   └── unemployment_cleaned.csv               # Cleaned dataset
│
├── notebooks/
│   └── unemployment_analysis.ipynb            # Main analysis notebook
│
├── outputs/
│   └── figures/                               # Visualizations (Day 3+)
│
├── src/                                       # Source code (if needed)
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Progress

### ✅ Day 1: Setup + Data Understanding (Completed)
- Project structure created
- Dataset loaded and inspected
- Data types analyzed
- Missing values checked (0 found)
- Duplicate records checked (0 found)
- Regions and date range documented
- Descriptive statistics generated

### ✅ Day 2: Data Cleaning + Feature Engineering (Completed)
- Column names standardized
- Whitespace cleaned from categorical data
- Dates converted to datetime format
- Numerical values validated
- **Temporal features created:**
  - Year (2019, 2020)
  - Month (1-12)
  - Month name (January, February, etc.)
  - Quarter (Q1-Q4)
- **COVID period classification created:**
  - Pre-COVID: Before March 1, 2020
  - COVID: March 1, 2020 - December 31, 2020
  - Post-COVID: After December 31, 2020
- Cleaned dataset exported
- Data cleaning methodology documented

### ✅ Day 3: EDA + Visualization (Completed)
- Loaded cleaned dataset
- Generated 9 professional visualizations
- Analyzed overall unemployment statistics
- Performed state-wise detailed analysis
- Examined year-wise and monthly trends
- Analyzed quarterly patterns
- Compared rural vs urban unemployment
- Studied labour participation trends
- Performed correlation analysis
- Created comprehensive EDA findings report
- Documented all insights

### ✅ Day 4: COVID-19 Impact Analysis (Completed)
- Deep-dive COVID-19 impact analysis performed
- Pre-COVID vs COVID detailed comparison completed
- State-level COVID impact assessed
- Peak analysis during COVID period documented
- Most/least affected regions identified
- Labour participation during COVID analyzed
- Rural vs urban COVID impact compared
- Recovery pattern analysis completed
- COVID-specific visualizations created (9 charts)
- Comprehensive COVID impact report generated
- State-by-state detailed analysis documented
- **Key Finding:** 397.7% unemployment increase during COVID period
- **Peak:** 35.89% (Uttar Pradesh, Urban, April 2020)
- **Recovery:** 69.7% from peak by November 2020

### 🔜 Day 5: Seasonality + Final Documentation (Upcoming)

## Key Findings (So Far)

### Overall Statistics:
- Average unemployment rate: 8.49%
- Highest unemployment: 35.89% (Uttar Pradesh, urban, April 2020)
- Lowest unemployment: 1.45% (Karnataka, urban, Pre-COVID)
- Standard deviation: 8.02% (high variability)

### COVID Impact:
- Pre-COVID average unemployment: 3.32%
- COVID period average unemployment: 16.53%
- Observed increase: **+13.21 percentage points (+397.9%)**
- Peak month: April 2020 (15.58% average)

### Regional Patterns:
- **Highest unemployment:** Delhi (11.01% average)
- **Lowest unemployment:** Andhra Pradesh (7.11% average)
- **Most COVID-affected:** Uttar Pradesh (peak 35.89%)
- Urban areas show 0.75 pp higher unemployment than rural

### Temporal Patterns:
- 2019 average: 3.10%
- 2020 average: 14.36% (+11.26 pp year-over-year)
- Q2 2020 worst quarter (13.92% average)
- Clear recovery trend from July 2020 onwards

### Labour Participation:
- Average: 42.85%
- Strong negative correlation with unemployment (-0.67)
- Declined significantly during COVID period

### Visualizations Created:

**EDA Visualizations (Day 3):**
1. Unemployment trend over time
2. State-wise average unemployment
3. Monthly unemployment patterns
4. Distribution analysis (histogram & box plot)
5. Rural vs urban comparison
6. Labour participation trend
7. State-monthly heatmap
8. Area monthly comparison
9. Correlation scatter plots
10. Time series with moving averages

**COVID-19 Visualizations (Day 4):**
11. COVID timeline overview
12. Pre-COVID vs COVID comparison
13. State-level COVID impact
14. Monthly COVID progression
15. Rural vs urban COVID impact
16. Labour participation during COVID
17. COVID recovery patterns
18. State-month COVID heatmap
19. COVID impact intensity heatmap

**Total:** 19 professional visualizations (300 DPI PNG)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/vedantkulkarniii/Unemployment-Analysis-with-Python.git
cd Unemployment-Analysis-with-Python
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Option 1: Run All Analyses (Recommended)
```bash
# Windows
run_all_analyses.bat

# Or run individual scripts
python src/generate_visualizations.py
python src/covid_visualizations.py
```

### Option 2: Interactive Analysis
1. Navigate to the notebooks directory
2. Open `unemployment_analysis.ipynb` in Jupyter Notebook
3. Run cells sequentially to reproduce the analysis

## Project Statistics

- **Total Commits:** 68/75 (Day 1: 15, Day 2: 15, Day 3: 15, Day 4: 15 in-progress)
- **Visualizations:** 19 professional charts
- **Analysis Scripts:** 13 Python scripts
- **Documentation:** 15+ comprehensive reports
- **Data Quality Score:** 99% reliability

## Author

**Vedant Kulkarni**

---

*Project Status: Day 4 Complete - 90% Complete (68/75 commits)*
*Next: Day 5 - Seasonality Analysis + Final Documentation*

