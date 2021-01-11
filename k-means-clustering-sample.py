# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:00:01 2021

@author: Zeno
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
# initally, we need to create features
x1 = np.random.normal(20,5,1000)
y1 = np.random.normal(25,5,1000)
x2 = np.random.normal(32,5,1000)
y2 = np.random.normal(33,5,1000)
x3 = np.random.normal(45,5,1000)
y3 = np.random.normal(53,5,1000)
# and then we can concatenate them before making pandas dataFrame
x = np.concatenate((x1,x2,x3),axis = 0)
y = np.concatenate((y1,y2,y2),axis = 0)
# for making pandas dataframe we need to convert these numpy series into dictionary
dictionary = {"x": x,"y" : y} 
# and now we can create pandas DataFrame
data = pd.DataFrame(dictionary)
# Let's look at how many clusters can be elbow
ssq = []
for each in range(1,15):
    model = KMeans(n_clusters= each).fit(data)
    ssq.append(model.inertia_)
    
"""plt.plot(range(1,15),ssq,color = "purple") # as you can see our elbow is 3
plt.grid()"""
plt.show()
# now we can create our K-means model with 3 clusters
k_means_model = KMeans(n_clusters=3).fit(data)
prediction = k_means_model.predict(data)
data["label"] = prediction
# for the last step, we can visualize how our model clustered our unlabelled data
plt.scatter(data.x[data.label == 0 ],data.y[data.label == 0 ], color = "orange")
plt.scatter(data.x[data.label == 1],data.y[data.label == 1],color ="purple")
plt.scatter(data.x[data.label == 2],data.y[data.label == 2],color = "green")
plt.scatter(k_means_model.cluster_centers_[:,0],k_means_model.cluster_centers_[:,1],color = "black") # to show centers of the clusters