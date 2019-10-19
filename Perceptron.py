# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 13:23:38 2019

@author: a761217
"""

import sklearn.datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

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
X = data.Name
Y = data.legitimate
dataform = pd.DataFrame(data.legitimate, columns=data.Name)
data['class'] = data.legitimate
data.head()
data.describe()
print(data['class'].value_counts())
print(data.Name)
data.groupby('class').mean()

X = data.drop('class', axis=1)
Y = data['class']
type(X)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=1)
print(X_train.mean(), X_test.mean(), X.mean())
X_train = X_train.values
X_test = X_test.values


class Perceptron:

    def __init__(self):
        self.w = None
        self.b = None

    def model(self, x):
        return 1 if (np.dot(self.w, x) >= self.b) else 0

    def predict(self, X):
        Y = []
        for x in X:
            result = self.model(x)
            Y.append(result)
            return np.array(Y)

    def fit(self, X, Y, epochs=1, lr=1):

        self.w = np.ones(X.shape[1])
        self.b = 0

        accuracy = {}
        max_accuracy = 0

        wt_matrix = []

        for i in range(epochs):
            for x, y in zip(X, Y):
                y_pred = self.model(x)
                if y == 1 and y_pred == 0:
                    self.w = self.w + lr * x
                    self.b = self.b - lr * 1
                elif y == 0 and y_pred == 1:
                    self.w = self.w - lr * x
                    self.b = self.b + lr * 1

            wt_matrix.append(self.w)

            accuracy[i] = pd.accuracy_score(self.predict(X), Y)
            if (accuracy[i] > max_accuracy):
                max_accuracy = accuracy[i]
                j = i
                chkptw = self.w
                chkptb = self.b

        self.w = chkptw
        self.b = chkptb

        print(max_accuracy, j)

        plt.plot(accuracy.values())
        plt.xlabel("Epoch #")
        plt.ylabel("Accuracy")
        plt.ylim([0, 1])
        plt.show()

        return np.array(wt_matrix)


perceptron = Perceptron()
wt_matrix = perceptron.fit(X_train, Y_train, 10000,
                           0.3)  # on peut modifier le 0.3 pour essayer d'obtenir une meilleure précision
