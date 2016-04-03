import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fmin_bfgs

class logisticRegression :
    def __init__(self,data = np.matrix(''),target = np.matrix('')):
        self.data = data
        self.target = target
        self.theta = np.matrix('')
        self.cov = plt.figure()

    def fit(self,data = np.matrix(''),target = np.matrix('')):
        m,n = np.shape(data)
        self.theta = np.zeros(m,1)


    def _sigmoid(self,x):
        res = 1/(1 + np.exp(-x))
        return res
    def _compute_cost(self,theta):
        J = -1/ m * (y.T * np.log(sigmoid(X * theta)) + (1 - y.T)*np.log(1-))