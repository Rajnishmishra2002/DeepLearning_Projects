# Comparing the Titanic Mean Using CLT

## Overview
This Jupyter Notebook analyzes the Titanic dataset using statistical techniques, particularly focusing on the **Central Limit Theorem (CLT)** to compare sample means. The goal is to explore how sampling affects statistical estimates and derive insights into passenger survival rates.

## Dataset
The notebook utilizes the **Titanic dataset**, which includes information about passengers, such as:
- Passenger class
- Age
- Gender
- Fare paid
- Survival status

## Methodology
1. **Data Loading & Preprocessing:**
   - Reads the Titanic dataset (CSV format) using **Pandas**.
   
2. **Exploratory Data Analysis (EDA):**
   - Descriptive statistics of key features.
   - Data visualization to understand distributions.
   
3. **Applying the Central Limit Theorem (CLT):**
   - Takes multiple random samples from the dataset.
   - Computes the means of those samples.
   - Compares sample means with the population mean to validate CLT.
   
4. **Visualization & Interpretation:**
   - Histograms and plots to visualize sample distributions.
   - Statistical summaries to confirm CLT assumptions.

## Requirements
- Python 3
- Jupyter Notebook
- Libraries: `numpy`, `pandas`, `matplotlib`, `seaborn`

## How to Use
1. Open the notebook in Jupyter.
2. Run each cell sequentially.
3. Analyze the output, particularly the visualizations and statistical summaries.

## Expected Findings
- The sample means should approximate the population mean as the sample size increases.
- The distribution of sample means should be normal, as per CLT principles.

