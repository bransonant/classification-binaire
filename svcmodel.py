# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:03:00 2019

@author: BRANSON Antoine & CHATELET Robin
"""

from common import *

# Select the 100k first rows
X_train, y_train = X_train.iloc[:100000, :], y_train.iloc[:100000]

# Using SVC algorithm
clf = SVC(gamma='auto')

# Training procedure
clf.fit(X_train, y_train)

# Testing procedure
print(clf.score(X_test, y_test))
