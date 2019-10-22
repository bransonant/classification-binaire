# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 09:52:28 2019

@author: BRANSON Antoine & CHATELET Robin
"""

from common import *

# Dataset contains 138047 lines
X_train, y_train = X_train.iloc[:138047, :], y_train.iloc[:138047]

# Using the KNN model with 5 neighbors
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

# Model Accuracy
print("Accuracy:", sklearn.metrics.accuracy_score(y_test, y_pred))
