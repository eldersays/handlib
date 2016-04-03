import pandas as pd
import numpy as np
from pandas import DataFrame,Series


def feature_normalize(self, X=np.matrix('')):
    stded_data = X.std(axis=1)
    mean_data = X.mean(axis=1)
    normalized = np.zeros(X.shape)
    print(X.shape)
    for i in range(X.shape[1]):
        normalized[:, i] = ((X[:, i] - mean_data[i]) / stded_data[i]).reshape(X.shape[0])
    return normalized