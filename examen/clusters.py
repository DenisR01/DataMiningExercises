from ucimlrepo import fetch_ucirepo
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

iris = fetch_ucirepo(id=53)

X = iris.data.features
y = iris.data.targets

print(iris.metadata)

print(iris.variables)

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
clusters = kmeans.predict(X)

X_with_clusters = X.copy()
X_with_clusters['Cluster'] = clusters

print(X_with_clusters)

plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_with_clusters.iloc[:, 0], y=X_with_clusters.iloc[:, 1], hue=X_with_clusters['Cluster'], palette='viridis', legend='full')
plt.title('K-Means Clustering of Iris Dataset')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend(title='Cluster')
plt.show()
