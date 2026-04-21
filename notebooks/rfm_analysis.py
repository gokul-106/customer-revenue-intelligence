import pandas as pd
transactions = pd.read_csv("data/processed/transactions.csv")
transactions['date'] = pd.to_datetime(transactions['date'])
reference_date = transactions['date'].max()
rfm = transactions.groupby('customer_id').agg({
    'date': lambda x: (reference_date - x.max()).days,
    'customer_id': 'count',
    'amount': 'sum'})
rfm.columns = ['recency', 'frequency', 'monetary']
rfm = rfm.reset_index()
print(rfm.head())
rfm.to_csv("data/processed/rfm.csv", index=False)
print(f"RFM table created for {len(rfm)} customers.")
rfm['r_score'] = pd.qcut(rfm['recency'], 4, labels=[4,3,2,1])
rfm['f_score'] = pd.qcut(rfm['frequency'], 4, labels=[1,2,3,4])
rfm['m_score'] = pd.qcut(rfm['monetary'], 4, labels=[1,2,3,4])
rfm['rfm_score'] = (
    rfm['r_score'].astype(str) +
    rfm['f_score'].astype(str) +
    rfm['m_score'].astype(str)
)
print(rfm.head())
def segment_customer(row):
    if row['rfm_score'] == '444':
        return 'champions'
    elif row['r_score'] >= 3 and row['f_score'] >= 3:
        return 'loyal_customers'
    elif row['r_score'] <= 2 and row['f_score'] >= 3:
        return 'at_risk'
    elif row['r_score'] <= 2 and row['f_score'] <= 2:
        return 'lost'
    else:
        return 'potential'
rfm['segment'] = rfm.apply(segment_customer, axis=1)
print(rfm[['customer_id', 'rfm_score', 'segment']].head())
rfm.to_csv("data/processed/rfm_segmented.csv", index=False)
print(f"Segmentation completed for {len(rfm)} customers.")
rfm.to_csv("data/processed/rfm_segmented.csv", index=False)
print(f"Segmentation completed for {len(rfm)} customers.")
print("\n--- Data Validation ---")
print("\nMissing values:")
print(rfm.isnull().sum())
print("\nDuplicate customers:")
print(rfm['customer_id'].duplicated().sum())
print("\nSummary statistics:")
print(rfm[['recency', 'frequency', 'monetary']].describe())
print("\nSegment distribution:")
print(rfm['segment'].value_counts())