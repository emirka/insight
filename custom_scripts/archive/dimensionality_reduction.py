# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

data_directory='../data/processed'
file_name='Tuesday_processed.pkl'

data_file=os.path.join(data_directory,file_name)
df=pd.read_pickle(data_file)

y=np.array(df['Label'])
y

X=np.array(df.loc[0:1000, df.columns != 'Label'])
X.shape

from sklearn.manifold import TSNE

x_red_tsne = TSNE(n_components=2).fit_transform(X)

fig=plt.figure(figsize=(15,10))
sns.scatterplot(x_red_tsne[:,0],x_red_tsne[:,1],hue=y[0:1000])
plt.xlabel('t-SNE Reduced Dimension 1')
plt.ylabel('t-SNE Reduced Dimension 2')
plt.title('Dataset after Linear Discriminant Analysis Dimensionality Reduction')
plt.show()
