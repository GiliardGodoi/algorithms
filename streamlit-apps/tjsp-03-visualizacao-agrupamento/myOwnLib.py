import random

import numpy as np
from sklearn.base import BaseEstimator, ClusterMixin
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.pipeline import Pipeline
from sklearn.datasets import make_blobs
from fcmeans import FCM
from pyclustering.cluster.kmeans import kmeans, kmeans_visualizer
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.cluster.rock import rock
from pyclustering.cluster.somsc import somsc
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import CountVectorizer

def random_color():
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def vec2mat(lst, n):
    m = []
    while lst != []:
        m.append(lst[:n])
        lst = lst[n:]
    return m


def processCluster(df, alg='K-Means', n_groups=3, feature='TFIDF', size=1024, ngram=[2, 3], eps=0.3, ns=10):
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.decomposition import TruncatedSVD
    from sklearn.cluster import KMeans
    from sklearn.pipeline import Pipeline

    # Criar o pipeline TF-IDF + PCA + Clustering
    extractor  = getFeature(feature, size, ngram)
    classifier = getCluster(alg, n_groups, myEps=eps, ns=ns)
    pipeline = Pipeline([
        ('featureExtraction', extractor),  # Passo 1: feature set extraction
        ('pca', TruncatedSVD(n_components=100, n_iter=7, random_state=42)),
        # Passo 2: PCA com 2 componentes (ajuste ao número desejado)
        # ('clustering', KMeans(n_clusters=n_groups))  # Passo 3: Clustering (K-Means com 2 clusters)
        ('clustering', classifier)  # Passo 3: Clustering (K-Means com 2 clusters)
    ])

    X = df['formatado']

    # Processar os documentos e ajustar o pipeline
    pipeline.fit(X)

    # Exibir as etiquetas dos clusters encontrados
    cluster_labels = pipeline.named_steps['clustering'].labels_
    features       = pipeline[:-1].transform(X)
    features       = features[:,:2]

    return cluster_labels, features


def getFeature(featureType, vecSize, ngram):
    if featureType == 'TFIDF':
        return TfidfVectorizer(max_features=vecSize, ngram_range=(min(ngram),max(ngram)))
    if featureType == 'Counting':
        return CountVectorizer(max_features=vecSize, ngram_range=(min(ngram),max(ngram)))
    if featureType == 'Hash':
        return HashingVectorizer(n_features=vecSize, ngram_range=(min(ngram),max(ngram)))


def getCluster(alg, nc=3, myEps=0.3, ns=10):
    if alg == 'K-Means':
        return KMeans(n_clusters=nc)
    if alg == 'K-Medoids':
        return PyClusteringKMedoids(n_clusters=nc)
    if alg == 'SOM':
        return PyClusteringSOMSC(n_clusters=nc)
    if alg == 'Fuzzy':
        return FuzzyCMeans(n_clusters=nc)
    if alg == 'Rock':
        return PyClusteringROCK(n_clusters=nc)
    if alg == 'DBSCAN':
        return DBSCAN(eps=myEps, min_samples = ns, n_jobs=-1)


class PyClusteringROCK(BaseEstimator, ClusterMixin):
    def __init__(self, threshold=2.0, number_clusters=2, number_iterations=10):
        self.threshold = threshold
        self.number_clusters = number_clusters
        self.number_iterations = number_iterations

    def fit(self, X, y=None):
        # Convertendo os dados para um formato aceito pelo pyclustering
        data = np.array(X).tolist()

        # Criando o objeto ROCK do pyclustering
        rock_instance = rock(data, self.number_clusters, self.threshold, self.number_iterations)

        # Executando o algoritmo de clustering
        rock_instance.process()

        # Obtendo as labels dos clusters atribuídas a cada ponto
        self.labels_ = rock_instance.get_clusters()

        return self


class PyClusteringSOMSC(BaseEstimator, ClusterMixin):
    def __init__(self, n_clusters=8, max_iter=10, error=1e-6):
        self.n_clusters = n_clusters
        self.max_iter = max_iter

    def fit(self, X, y=None):
        # Convertendo os dados para um formato aceito pelo pyclustering
        data = np.array(X).tolist()

        # Criando o objeto K-Medoids do pyclustering
        somsc_instance = somsc(data, self.n_clusters)

        # Executando o algoritmo de clustering
        somsc_instance.process()

        # Obtendo as labels dos clusters atribuídas a cada ponto
        self.labels_ = somsc_instance.get_clusters()

        return self


class PyClusteringKMedoids(BaseEstimator, ClusterMixin):
    def __init__(self, n_clusters=8, max_iter=100):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.labels_ = None

    def fit(self, X, y=None):
        # Convertendo os dados para um formato aceito pelo pyclustering
        data = np.array(X).tolist()

        # Criando o objeto K-Medoids do pyclustering
        initial_medoids = np.random.choice(len(data), size=self.n_clusters, replace=False)
        kmedoids_instance = kmedoids(data, initial_medoids)

        # Executando o algoritmo de clustering
        kmedoids_instance.process()

        # Obtendo as labels dos clusters atribuídas a cada ponto
        self.labels_ = kmedoids_instance.predict(data)

        return self

    def fit_predict(self, X, y=None):
        self.fit(X, y)
        return self.labels_




class FuzzyCMeans(BaseEstimator, ClusterMixin):
    def __init__(self, n_clusters=8, m=2, max_iter=50, error=1e-6):
        self.n_clusters = n_clusters
        self.m = m
        self.max_iter = max_iter
        self.error = error

    def fit(self, X, y=None):
        fcm = FCM(n_clusters=self.n_clusters, m=self.m, max_iter=self.max_iter, error=self.error)
        fcm.fit(X)

        self.cluster_centers_ = fcm.centers
        self.labels_ = np.argmax(fcm.u, axis=1)

        return self