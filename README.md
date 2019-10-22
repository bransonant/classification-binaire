# Classification binaire

## Dataset

Le fichier antivirus_dataset.csv est le fichier contenant les datas pour faire l'apprentissage

## Modélisation

Le fichier observation.py permet de générer le rapport Pandas_profiling_report.html pour modéliser le dataset fourni

## Comparaison

Le fichier comparison.py génère des graphiques permettant de comparer les différents algorithmes qu'il aurait été 
possible d'utiliser dans notre programme

## Apprentissage

Le fichier algo.py contient la partie apprentissage et permet d'obtenir un pourcentage de confiance d'environ 93,5%.
Afin de construire notre programme, nous avons implémenté l'algorithme SVC.

Le fichier knnmodel.py contient une autre implémentation de la partie apprentissage et permet d'obtenir un pourcentage 
de confiance d'environ 98,3%.
Nous utilisons dans ce cas-ci le modèle KNN.

## Requirements

Afin d'exécuter nos deux scripts Python, il est nécessaire d'installer les packages listés dans le requirements.txt
```bash
pip3 install -r requirements.txt
```


