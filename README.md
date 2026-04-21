# Customer Revenue Intelligence System

An end-to-end data analytics and machine learning project focused on understanding customer behavior, identifying high-value segments, and predicting churn risk.

---

## Project Overview

- Analyzed ~100,000 transactions across ~11,000 customers  
- Designed a system to segment customers based on value and behavior  
- Identified revenue concentration and potential churn risk  

---

## Objectives

- Identify high-value and low-value customer segments  
- Understand revenue contribution across segments  
- Detect customers at risk of churn  
- Provide actionable insights for business decision-making  

---

## Methodology

- Performed Exploratory Data Analysis (EDA) on transaction data  
- Engineered RFM (Recency, Frequency, Monetary) features  
- Applied K-Means clustering for customer segmentation  
- Built a Random Forest model for churn prediction  
- Developed a Power BI dashboard for visualization  

---

## Key Components

- **RFM Segmentation**
  - Categorized customers based on recency, frequency, and monetary value  

- **K-Means Clustering**
  - Grouped customers into distinct behavioral segments  

- **Churn Prediction**
  - Used Random Forest to identify at-risk customers  
  - Analyzed feature importance (recency as key driver)  

- **Dashboard (Power BI)**
  - Customer distribution by segment  
  - Revenue contribution analysis  
  - Customer segment share  
  - RFM-based distribution visualization  

---

## Key Insights

- A very small percentage of customers contributes a significant portion of revenue  
- A large share of revenue is associated with at-risk customers  
- Customer distribution is highly skewed across segments  
- Recency is the strongest indicator of churn risk  

---

## Tech Stack

- Python (Pandas, NumPy, Scikit-learn)  
- SQL  
- Power BI  
- Machine Learning (Clustering and Classification)  

---

## Project Structure

customer-revenue-intelligence/

- notebooks/
  - EDA.ipynb  
  - RFM_analysis.ipynb  
  - clustering.ipynb  
  - churn_model.ipynb  

- dashboard/
  - powerbi_dashboard.pbix  

- README.md  

---

## Business Impact

- Enables targeted marketing for high-value customers  
- Helps identify and retain at-risk customers  
- Supports data-driven revenue optimization strategies  
