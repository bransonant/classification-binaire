# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:03:00 2019

@author: BRANSON Antoine & CHATELET Robin
"""

from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pandas as pd
import pandas_profiling
import sklearn.datasets


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

# Loading dataset and dropping columns unused
for col in dataToDrop:
    try:
        data = data.drop(col, axis=1)
    except:
        print("{} not found".format(col))

X = data.drop('legitimate', axis=1)
Y = data['legitimate']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=1)