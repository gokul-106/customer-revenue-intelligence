import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# load data
rfm = pd.read_csv("data/processed/rfm_segmented.csv")

# take only required columns
rfm_features = rfm[["recency", "frequency", "monetary"]]

# scale the data
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm_features)

# elbow method
inertia = []

for k in range(1, 10):
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(rfm_scaled)
    inertia.append(model.inertia_)

# plot graph
plt.plot(range(1, 10), inertia, marker='o')
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()

# cluster summary already created earlier
print(cluster_summary)

# distribution (count)
print(rfm["segment_kmeans"].value_counts())

# distribution (%)
distribution = rfm["segment_kmeans"].value_counts(normalize=True) * 100
print(distribution.round(2))

# save outputs
cluster_summary.to_csv("data/processed/cluster_summary.csv")
rfm.to_csv("data/processed/kmeans_segmented.csv", index=False)