import pandas as pd

# Load data
df = pd.read_csv("data/raw/bank.csv")

# Handle missing values
df = df.ffill()

# Convert categorical columns
df['job'] = df['job'].astype('category').cat.codes

# Create age groups
df['age_group'] = pd.cut(df['age'], bins=[18,30,45,60,100], labels=[1,2,3,4])

# Create balance categories
df['balance_category'] = pd.cut(df['balance'], bins=[-10000,0,5000,20000,100000], labels=[1,2,3,4])

# Save cleaned data
df.to_csv("data/processed/customers_cleaned.csv", index=False)

print(f"Processed dataset saved with {len(df)} rows.")