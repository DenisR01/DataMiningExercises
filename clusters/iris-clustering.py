import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

feature = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

data = pd.read_csv("iris.data", names=feature)
print(data.head())

data['class'] = data['class'].replace({'Iris-setosa': 1, 'Iris-versicolor': 2, 'Iris-virginica': 0})
print(data.head())

x = data.iloc[:, [1, 2, 3, 4]].values
print(x)
spd = []

for i in range(1, 9):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(x)
    spd.append(kmeans.inertia_)

# Graficul Elbow pentru a alege numarul de clusteri
plt.plot(range(1, 9), spd)
plt.title('Metoda Elbow')
plt.xlabel('Nr clusteri')
plt.ylabel('Suma patratelor distantelor')
plt.show()

kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=100)
# 3 pt ca am 3 tipuri de Iris
y_kmeans = kmeans.fit_predict(x)

# Vizualizarea clusterilor
plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s=100, c='yellow', label='Cluster 2')
plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s=100, c='blue', label='Cluster 3')

plt.legend()
plt.show()
