import numpy as np
import matplotlib.pyplot as plt

class linear_regression():
    def __init__(self):
        self.theta = np.matrix('')
        self.history = np.matrix('')

    def cost(self,X = np.matrix(''),y = np.matrix(''),theta = np.matrix('')):
        m = X.shape[0]
        J = ((1/(2 * m)) * (X * theta - y).T *(X * theta -y)).sum()
        return J


    def feature_normalize(self,X = np.matrix('')):
        stded_data = X.std(axis= 1)
        mean_data = X.mean(axis = 1)
        normalized = np.zeros(X.shape)
        print(X.shape)
        for i in range(X.shape[1]) :
            normalized[:,i] = ((X[:,i] - mean_data[i]) / stded_data[i]).reshape(X.shape[0])
        return normalized


    def fit(self,data = np.matrix(''),target = np.matrix(''),alpha = 0.01,cycle = 100):
       self.theta = np.ones([data.shape[1],1])
       self.history = np.zeros([cycle,1])
       m = data.shape[0]
       for i in range(cycle):
           self.theta = self.theta - alpha * ( 1 / m) * (data.T *(data * self.theta - target))
           self.history[i] = self.cost(data,target,self.theta)
           i += 1

    def predict(self,data):
        return data * self.theta

