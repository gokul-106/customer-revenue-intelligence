import pandas as pd

# load RFM dataset
rfm = pd.read_csv("data/processed/rfm_segmented.csv")

# select only RFM features
rfm_features = rfm[["recency", "frequency", "monetary"]]

print(rfm_features.head())

from sklearn.preprocessing import StandardScaler

# scale the data
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm_features)

print(rfm_scaled[:5])

from sklearn.cluster import KMeans

# apply KMeans
kmeans = KMeans(n_clusters=4, random_state=42)
clusters = kmeans.fit_predict(rfm_scaled)

# add cluster labels to dataframe
rfm["cluster"] = clusters

print(rfm[["recency", "frequency", "monetary", "cluster"]].head())

cluster_summary = rfm.groupby("cluster").agg({
    "recency": "mean",
    "frequency": "mean",
    "monetary": "mean"
}).round(2)

print(cluster_summary)

cluster_labels = {
    0: "Regular Customers",
    1: "Low Value Customers",
    2: "High Value Customers",
    3: "At Risk Customers"
}

rfm["segment_kmeans"] = rfm["cluster"].map(cluster_labels)

print(rfm[["recency", "frequency", "monetary", "segment_kmeans"]].head())

rfm.to_csv("data/processed/kmeans_segmented.csv", index=False)

print(rfm["segment_kmeans"].value_counts())

distribution = rfm["segment_kmeans"].value_counts(normalize=True) * 100
print(distribution.round(2))

cluster_summary.to_csv("data/processed/cluster_summary.csv")
rfm.to_csv("data/processed/kmeans_segmented.csv", index=False)

from sklearn.metrics import silhouette_score

score = silhouette_score(rfm_scaled, clusters)
print("Silhouette Score:", round(score, 4))

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# create target (1 = at risk, 0 = others)
rfm["target"] = (rfm["segment_kmeans"] == "At Risk Customers").astype(int)

# features and target
X = rfm[["recency", "frequency", "monetary"]]
y = rfm["target"]

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# accuracy
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", round(accuracy, 4))

import pandas as pd

importance = pd.Series(model.feature_importances_, index=X.columns)
print("\nFeature Importance:")
print(importance.sort_values(ascending=False))