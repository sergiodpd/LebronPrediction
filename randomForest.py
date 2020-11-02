import pandas as pd
import numpy as np
from scipy import stats
from datetime import datetime
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
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
    

path = r'C:\Users\Sergio\Documents\LebronPrediction\dataset'

df = pd.read_csv(path + "\\LJPredictionNew.csv",sep=";")
df.head()

X = pd.DataFrame(df['Games'])
y = pd.DataFrame(df['Points']).astype(int)


for n in range(1, 15):
    regr = RandomForestRegressor(max_depth=n, random_state=5)

    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=2)
    regr.fit(X_train, Y_train.values.ravel())
    Y_pred = regr.predict(X_test).ravel()

    print("\n", "The scores for max_depth", n)
    print("The mean absolute error is", mean_absolute_error(Y_test, Y_pred))
    print("The mean absolute percentage error is", mean_absolute_percentage_error(Y_test, Y_pred))
    print("The R^2 score is", r2_score(Y_test, Y_pred))