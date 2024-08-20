from sklearn.ensemble import RandomForestRegressor
import numpy as np

class PricePredictor:
    def __init__(self):
        self.model = RandomForestRegressor()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

