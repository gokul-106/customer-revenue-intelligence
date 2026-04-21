import pandas as pd
import numpy as np

# Load customer data
df = pd.read_csv("data/raw/bank.csv")

# Create customer_id
df['customer_id'] = range(1, len(df) + 1)

transactions = []

np.random.seed(42)

for _, row in df.iterrows():
    base = max(5, int(abs(row['balance']) / 1000))
    num_transactions = np.random.randint(base, base + 10)

    for _ in range(num_transactions):
        amount = np.random.normal(loc=abs(row['balance']) * 0.05 + 500, scale=500)
        amount = max(50, abs(amount))

        transactions.append({
            "customer_id": row['customer_id'],
            "amount": round(amount, 2),
            "transaction_type": np.random.choice(["debit", "credit"]),
            "date": pd.Timestamp("2024-01-01") + pd.to_timedelta(np.random.randint(0, 365), unit="D")
        })

transactions_df = pd.DataFrame(transactions)

# Save outputs
df.to_csv("data/processed/customers.csv", index=False)
transactions_df.to_csv("data/processed/transactions.csv", index=False)

total_customers = df['customer_id'].nunique()
total_transactions = len(transactions_df)
avg_txn = total_transactions / total_customers

print(f"""
Transaction generation completed.
Total customers: {total_customers}
Total transactions: {total_transactions}
Average transactions per customer: {avg_txn:.2f}
""")