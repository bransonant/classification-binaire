# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 09:52:28 2019

@author: Branson Antoine & Chatelet Robin
"""

import pandas as pd
import sklearn.datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('antivirus_dataset.csv', delimiter='|', header=0)

dataToDrop = ["Name",
              "md5",
              "AddressOfEntryPoint",
              "BaseOfCode",
              "ExportNb",
              "ImportsNbOrdinal",
              "LoaderFlags",
              "MajorImageVersion",
              "MajorOperatingSystemVersion",
              "MinorLinkerVersion",
              "MinorOperatingSystemVersion",
              "Machine",
              "NumberOfRvaAndSizes",
              "ResourcesMeanSize",
              "ResourcesMinSize",
              "SectionAlignment",
              "SectionMaxVirtualsize",
              "SectionsMeanRawsize",
              "SizeOfCode",
              "SectionsMinVirtualsize",
              "SizeOfUninitializedData",
              "Characteristics",
              "CheckSum",
              "DllCharacteristics",
              "ExportNb",
              "LoadConfigurationSize",
              "MinorOperatingSystemVersion",
              "MinorSubsystemVersion"]

# loading dataset and dropping columns unused
for col in dataToDrop:
    try:
        data = data.drop(col, axis=1)
    except:
        print("{} not found".format(col))

X = data.drop('legitimate', axis=1)
Y = data['legitimate']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=1)

# dataset contains 138047 lines
X_train, y_train = X_train.iloc[:138047, :], y_train.iloc[:138047]

# using the knn model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

# Model Accuracy
print("Accuracy:", sklearn.metrics.accuracy_score(y_test, y_pred))
