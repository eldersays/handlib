import pandas as pd
import numpy as np


class naive_bayesian():
    def __init__(self):
        self.__class__.__doc__ = 'same'
        self.feature_count = 0
        self.types_c = 0
        self.types = []
        self.body = pd.Panel()
        self.data = pd.DataFrame()

    def fit(self,data,target):
        self.data = pd.DataFrame(np.c_[data,target])
        self.types_c = target.shape[0]
        self.types = pd.Series(target).unique().tolist()
        self.feature_count = data.shape[1]


    def predict(self,later_data):
        later_data = pd.DataFrame(later_data)
        rows = later_data.index
        final_results = pd.Series(index = rows)
        for i in range(rows.shape[0]):
            final_results[i] = self.cal_row(later_data.ix[i,:])
        return final_results

    def pos_type(self, s_type,fea, which_col):
        data = self.data
        this_type = data[data[self.feature_count] == s_type]#get the type in last column
        type_num = this_type.shape[0]#sum how many this types
        fea_counts = data[data[which_col] == fea].shape[0]
        P_B_A = fea_counts / this_type.shape[0]
        P_A = this_type.shape[0]/self.types_c
        return P_B_A * P_A


    def cal_row(self,row):
        data = self.data
        result = pd.Series(index = self.types)
        for i in self.types :
            temp = 1
            for j in range(self.feature_count) :
                temp *= self.pos_type(i,row[j],j)
            result[i] = temp
        x_x = result[result == result.max()].index.tolist()#get the max's index
        return x_x[0]#return the index





    '''def fit(self,data = np.matrix(''),target= np.matrix('')):#useless
        combine = np.c_[data,target]
        combine = pd.DataFrame(data = combine)
        self.feature_count = combine.shape[1] - 1
        self.type = combine[self.feature_count].unique()#cant use -1 to get the last column
        all_feature = []
        plus_1 = self.feature_count +1
        for i in plus_1 :
            temp = combine[i].unique().tolist()
            all_feature += temp
        self.body.reindex(items = self.type,major_axis= combine.columns[:-1],minor_axis=all_feature)
        '''