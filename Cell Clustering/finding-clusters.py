#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 12:47:46 2020

@author: shabnamsahay
"""

import pandas as pd
import numpy as np

file = 'pbmcs.txt'

A_table = pd.read_csv(file, sep='\t', header=0, index_col=0)
A_log=np.log(A_table+1)

from sklearn.decomposition import PCA
PCA = PCA(n_components=50)
PCA.fit(A_log)
A_pca = PCA.transform(A_log)

import matplotlib.pyplot as plt

plt.scatter(A_pca[:,0], A_pca[:,1], alpha=0.5)
plt.title('PCA figure')
plt.xlabel('PC1')
plt.ylabel('PC2')

from sklearn.manifold import TSNE

TSNE = TSNE(random_state=1, early_exaggeration=4, learning_rate=500.0)
A_tsne = TSNE.fit_transform(A_pca)

plt.scatter(A_tsne[:,0], A_tsne[:,1], alpha=0.5)
plt.title('t-SNE figure')
plt.xlabel('t-SNE1')
plt.ylabel('t-SNE2')

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=6, max_iter=1000)
kmeans.fit(A_pca)
cluster_labels = kmeans.predict(A_pca)

plt.scatter(A_tsne[:,0], A_tsne[:,1], c=cluster_labels, cmap='viridis',alpha=0.5)
plt.title('t-SNE figure with clusters')
plt.xlabel('t-SNE1')
plt.ylabel('t-SNE2')