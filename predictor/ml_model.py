import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay


data = pd.read_csv("predictor/Heart Prediction Quantum Dataset.csv")
data = data.drop(labels="QuantumPatternFeature", axis=1)
X = data.drop("HeartDisease", axis=1)
y = data["HeartDisease"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1410)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
accuracies = []
n = [i for i in range(1,15)]
p = [1, 2]
for n_value in n:
    for p_value in p:
        knn_temp = KNeighborsClassifier(n_neighbors=n_value, p=p_value)
        knn_temp.fit(X_train_scaled, y_train)
        y_pred_temp = knn_temp.predict(X_test_scaled)
        accuracies.append(accuracy_score(y_test, y_pred_temp))
optimal_k = accuracies.index(max(accuracies)) + 1
knn = KNeighborsClassifier(n_neighbors=optimal_k)
knn.fit(X_train_scaled, y_train)
y_pred = knn.predict(X_test_scaled)
print(classification_report(y_test, y_pred))
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()

