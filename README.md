# Customer Revenue Intelligence System

An end-to-end data analytics and machine learning system designed to identify high-value customers, uncover revenue concentration, and proactively detect churn risk using behavioral segmentation and predictive modeling.

---

## Problem Statement

Businesses often lack visibility into:
- Which customers drive the majority of revenue
- How customer value is distributed across segments
- Which customers are at risk of churn before it happens

This leads to:
- Inefficient marketing spend
- Missed retention opportunities
- Revenue loss from high-value customers

---

## Solution

Built a data-driven customer intelligence system that:
- Segments customers based on behavioral and monetary patterns
- Identifies high-value and at-risk customers
- Quantifies revenue concentration across segments
- Enables targeted retention and growth strategies

---

## Key Results

- Analyzed ~100,000 transactions across ~11,000 customers  
- Identified that a very small % of customers contribute a disproportionately high share of revenue  
- Discovered ~40%+ of revenue is linked to at-risk customer segments  
- Found **Recency** to be the strongest predictor of churn  

---

## Methodology

- Performed Exploratory Data Analysis (EDA) to understand customer behavior  
- Engineered RFM (Recency, Frequency, Monetary) features  
- Applied K-Means clustering for customer segmentation  
- Used Elbow Method and Silhouette Score for cluster validation  
- Built a Random Forest model for churn prediction  
- Evaluated feature importance to identify key churn drivers  
- Developed an interactive Power BI dashboard for insights  

---

## Key Components

### RFM Segmentation
- Quantified customer value using Recency, Frequency, and Monetary metrics  
- Enabled clear separation of high-value vs low-value customers  

### Customer Segmentation (K-Means)
- Clustered customers into distinct behavioral groups  
- Identified high-value, low-value, and at-risk segments  

### Churn Prediction (Random Forest)
- Predicted churn likelihood using behavioral features  
- Identified Recency as the most important feature  

### Business Intelligence Dashboard (Power BI)
- Segment-wise revenue distribution  
- Customer segmentation breakdown  
- At-risk customer revenue tracking  
- RFM-based insights visualization  

---

## Dashboard Preview

![Dashboard](dashboard.png)

[Download Full Dashboard (PDF)](dashboard.pdf)

---

## Tech Stack

- Python (Pandas, NumPy, Scikit-learn)  
- SQL  
- Power BI  
- Machine Learning (Clustering + Classification)  

---

## Project Structure
