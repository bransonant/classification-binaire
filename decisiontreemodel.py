# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:30:03 2019

@author: BRANSON Antoine & CHATELET Robin
"""

from common import *

# Dataset contains 138047 lines
X_train, y_train = X_train.iloc[:138047, :], y_train.iloc[:138047]

# Using Decision Tree Model
clf = DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Model accuracy
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
