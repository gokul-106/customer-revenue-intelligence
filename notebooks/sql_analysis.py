import sqlite3
import pandas as pd

connection = sqlite3.connect("customer.db")

rfm = pd.read_csv("data/processed/rfm_segmented.csv")

rfm.to_sql("customers", connection, if_exists="replace", index=False)

print("done")