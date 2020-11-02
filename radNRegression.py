import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import neighbors
from datetime import datetime
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt

def percentage_error(actual, predicted):
    res = np.empty(actual.shape)
    for j in range(actual.shape[0]):
        if actual[j] != 0:
            res[j] = (actual[j] - predicted[j]) / actual[j]
        else:
            res[j] = predicted[j] / np.mean(actual)
    return res

def mean_absolute_percentage_error(y_true, y_pred): 
    return np.mean(np.abs(percentage_error(np.asarray(y_true), np.asarray(y_pred)))) * 100
    

path = r'C:\Users\Sergio\Documents\Lebron Prediction\dataset'

df = pd.read_csv(path + "\\LebronPrediction.csv",sep=";", index_col=[0])
df.head()


X = pd.DataFrame(df[["Games", "MPG", "FGA", "FG%", "3PA", "3P%", "eFG%", "PPG"]])
y = pd.DataFrame(df["TotalPoints"]).astype(int)

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=12)

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3, random_state=123)

# ajuste del 1º modelo de regresion

for n_radius in range(5, 10):

    for i, weights in enumerate(['uniform', 'distance']):
        knn = neighbors.RadiusNeighborsRegressor(radius=float(n_radius), weights=weights)
        knn.fit(X_train, Y_train)

        Y_pred = knn.predict(X_test).ravel()

        print("\n", "The scores for",float(n_radius), "radius, and weight", weights)
        print("The mean absolute error is", mean_absolute_error(Y_test, Y_pred))
        print("The mean absolute percentage error is", mean_absolute_percentage_error(Y_test, Y_pred))
        print("The R^2 score is", r2_score(Y_test, Y_pred))