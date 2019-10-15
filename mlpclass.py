import pandas as pd
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import sklearn

data = pd.read_csv('antivirus_dataset.csv', delimiter='|', header=0)
print(data.head())
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

data = data.drop(dataToDrop,axis=1)
print(data.columns)

X = data.iloc[:,:-1]
y = data['legitimate']

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
print(X_train)
print(y_train)

SVC_model = SVC()

KNN_model = KNeighborsClassifier(n_neighbors=5)
SVC_model.fit(X_train, y_train)
KNN_model.fit(X_train, y_train)

SVC_prediction = SVC_model.predict(X_test)
KNN_prediction = KNN_model.predict(X_test)

print(accuracy_score(SVC_prediction, y_test))
print(accuracy_score(KNN_prediction, y_test))

print(confusion_matrix(SVC_prediction, y_test))
print(classification_report(KNN_prediction, y_test))