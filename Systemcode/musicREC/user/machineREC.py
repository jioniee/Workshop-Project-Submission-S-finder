from random import uniform
from matplotlib import pyplot as plt
from yellowbrick.cluster import InterclusterDistance, KElbowVisualizer, SilhouetteVisualizer
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import NearestNeighbors
from random import sample
import numpy as np
import pandas as pd

# def pca_trans(data):
#     n_components = 15
#     pca = PCA(n_components).fit(data)
#     PCs = []
#     for l in range(1, n_components + 1):
#         PCs.append("PC" + str(l))
#     eigenvalues = pca.explained_variance_
#     eigenvectors = np.round(pca.components_.transpose(), decimals=3)
#     pd.DataFrame(eigenvectors, index=features, columns=PCs)
#     loadings = eigenvectors * np.sqrt(eigenvalues)
#     pd.DataFrame(np.round(loadings, decimals=4), index=features, columns=PCs)
#     fig = plt.figure(figsize=(8, 5))
#     x_axis = np.arange(n_components) + 1
#
#     plt.plot(x_axis, eigenvalues, 'ro-', linewidth=2)
#     plt.title('Scree Plot')
#     plt.xlabel('Principal Component')
#     plt.ylabel('Eigenvalue')
#     plt.show()
#
#     # no_pc = 6
#     # PC_scores = pca.fit_transform(data)  # PC scores for downstream analytics
#     # scores = pd.DataFrame(PC_scores[:, 0:no_pc], columns=PCs[0:no_pc])
#     return scores, pca

#将歌手名转化为序号
def get_singerid(u_singers):
    singer_ids = []
    for each in u_singers:
        singer_ids.append(df[df.singer==each].index.tolist()[0])
    return singer_ids

#将用户的歌手库转化为标准的特征向量组
def get_u_vector(u_singers):
    temp = []
    for each in u_singers:
        if each in df['singer'].tolist():
            temp.append(each)
    singer_ids = get_singerid(temp)
    # print(singer_ids)
    songlabels = np.zeros(len(data.columns.tolist()))
    for each in singer_ids:
        songlabel = np.array(data.loc[each].tolist())
        songlabels += songlabel

    min_label = min(songlabels)
    max_label = max(songlabels)
    normalized_labels = []
    for each in songlabels:
        normalized_label = (each - min_label)/(max_label - min_label)
        normalized_labels.append(normalized_label)

    u_vector = normalized_labels
    # u_vector = pca.transform([u_vector])[:,0:6]
    return u_vector

#预测10个最近歌手
def prediction(u_vector, data):
    model_knn = NearestNeighbors(n_neighbors=10, algorithm='brute')
    model_knn.fit(data)
    # print(data)
    # data.to_excel('see.xlsx')
    distances, indices = model_knn.kneighbors(u_vector)
    return(indices[0])



df = pd.read_csv("./static/user_singerdata.csv", index_col=[0])
df.index = range(0, len(df.index.tolist()))

singer_names = df['singer'].tolist()
data = df.drop(['singer'], axis=1)
features = data.columns.tolist()
data = MinMaxScaler().fit_transform(data)
data = pd.DataFrame(data)

# scores, pca = pca_trans(data)

#测试单个歌手的最近5个歌手
########################################
u_singers = ['周杰伦']
########################################

u_vector = get_u_vector(u_singers)
# print(u_vector)
indices = prediction([u_vector], data)
# for each in indices:
#     print(df.loc[each, 'singer'])