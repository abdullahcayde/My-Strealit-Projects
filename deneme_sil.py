import pandas as pd
import numpy as np
import seaborn as sns

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = sns.load_dataset('taxis')
df.to_csv('data/taxis.csv')
print(df.head())
print(df.columns)

X = df[['distance']]
y = df['total']

m = 1
n = 100

regr = RandomForestRegressor(max_depth= m, n_estimators= n)

regr.fit(X,y)
prediction = regr.predict(X)