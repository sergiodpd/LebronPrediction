import pandas as pd
import numpy as np
from scipy import stats
from datetime import datetime
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import xgboost as xgb
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

for n in range(1, 9):
    for m in range(1, 9):
        i = n*0.1
        j =m*0.1
        #I'll change the parameters objective, max_depth, alpha and n_estimators to see which is the best option.
        xg_reg = xgb.XGBRegressor(objective ='reg:squarederror', colsample_bytree = i, learning_rate = j,
                max_depth = 3, alpha = 5, n_estimators = 8)


        xg_reg.fit(X_train, Y_train)
        Y_pred = xg_reg.predict(X_test).ravel()

        print("------------------------------------------------------------------------------------------------")
        print("colsample_bytree=", i, "learning_rate=", j)
        print("The mean absolute error is", mean_absolute_error(Y_test, Y_pred))
        print("The mean absolute percentage error is", mean_absolute_percentage_error(Y_test, Y_pred))
        print("The R^2 score is", r2_score(Y_test, Y_pred))