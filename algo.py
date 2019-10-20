# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:03:00 2019

@author: BRANSON Antoine & CHATELET Robin
"""

import sklearn.datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

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

for col in dataToDrop:
    try:
        data = data.drop(col, axis=1)
    except:
        print("{} not found".format(col))

X = data.drop('legitimate', axis=1)
Y = data['legitimate']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=1)

#select the 100k first rows
X_train, y_train = X_train.iloc[:100000,:], y_train.iloc[:100000]

clf = SVC(gamma='auto')

#training procedure
clf.fit(X_train, y_train) 

#testing procedure
print(clf.score(X_test, y_test))
