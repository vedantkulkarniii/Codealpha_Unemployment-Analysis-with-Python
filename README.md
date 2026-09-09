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

### 🔜 Day 3: EDA + Visualization (Upcoming)
### 🔜 Day 4: COVID-19 Impact Analysis (Upcoming)
### 🔜 Day 5: Seasonality + Finalization (Upcoming)

## Key Findings (So Far)

### Overall Statistics:
- Average unemployment rate: ~9.67%
- Highest unemployment: 35.89% (Uttar Pradesh, urban, COVID period)
- Lowest unemployment: 1.45% (Karnataka, urban, Pre-COVID)

### COVID Impact (Initial):
- Pre-COVID average unemployment: ~3.20%
- COVID period average unemployment: ~16.78%
- Observed increase: ~13.58 percentage points
- Note: Full analysis in Day 4

### Regional Patterns:
- Uttar Pradesh: Highest average (10.45%)
- Karnataka: Lowest average (7.15%)
- Urban areas generally showed higher COVID impact

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

1. Navigate to the notebooks directory
2. Open `unemployment_analysis.ipynb` in Jupyter Notebook
3. Run cells sequentially to reproduce the analysis

## Author

**Vedant Kulkarni**

---

*Project Status: Day 2 Complete - In Active Development*

