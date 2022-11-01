import pandas as pd
from joblib import dump
from catboost import CatBoostRegressor
from sklearn.utils import shuffle
import numpy as np

data = pd.read_csv('data.csv')
data = shuffle(data, random_state=100)
data['Number of Doors'].fillna(data['Number of Doors'].median(), inplace=True)
data.fillna(0, inplace=True)

X = data.drop(['MSRP'], axis=1)
y = data['MSRP']

categorical_features_indices = np.where(X.dtypes != float)[0]
regressor = CatBoostRegressor(iterations=2, learning_rate=1, depth=2)

regressor.fit(X, y, cat_features=categorical_features_indices, )

dump(regressor, 'vehicle_dt_v1.joblib')
