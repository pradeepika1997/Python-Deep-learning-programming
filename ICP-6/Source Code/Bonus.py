import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns
sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")

#Loading CC dataset using pandas
dataset = pd.read_csv('CC.csv')
print(dataset.columns)


#Splitting the dataset
x = dataset.iloc[:,[2, -5,-6]]
y = dataset.iloc[:,-1]
print(x.shape, y.shape)


## Displaying Null values for each feature in the dataset
nulls = pd.DataFrame(x.isnull().sum().sort_values(ascending=False)[:16])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)

## Replacing null values with mean values
x = x.select_dtypes(include=[np.number]).interpolate().dropna()

## Displaying Null value count after replacing with mean
nulls = pd.DataFrame(x.isnull().sum().sort_values(ascending=False)[:16])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)


# Standradising the data features
from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
scaler.fit(x)
X_scaled_array = scaler.transform(x)
X_scaled = pd.DataFrame(X_scaled_array, columns = x.columns)

# Building the model
from sklearn.cluster import KMeans
nclusters = 3 # this is the k in kmeans
km = KMeans(n_clusters=nclusters)
km.fit(X_scaled)

# predict the cluster for each data point
y_cluster_kmeans = km.predict(X_scaled)
from sklearn import metrics
score = metrics.silhouette_score(X_scaled, y_cluster_kmeans)
print("Silhoutte Score without PCA: " + str(score))



# PCA
pca = PCA(2)
x_pca = pca.fit_transform(X_scaled)
df2 = pd.DataFrame(data=x_pca)
finaldf = pd.concat([df2,dataset[['TENURE']]],axis=1)
nclusters = 3 # this is the k in kmeans
km = KMeans(n_clusters=nclusters)
km.fit(df2)

# predict the cluster for each data point after applying PCA.
y_cluster_kmeans = km.predict(df2)
score = metrics.silhouette_score(df2, y_cluster_kmeans)
print("Silhoutte Score with PCA: " + str(score))