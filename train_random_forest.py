import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor

x_all = np.load("data/x_all.npy")
y_all = np.load("data/y_all.npy")

regressor = RandomForestRegressor()
regressor.fit(x_all, y_all)
joblib.dump(regressor, "out/trained_model.sav")
