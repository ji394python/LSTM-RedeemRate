import numpy as np
import pandas as pd
import seaborn
import matplotlib.pyplot as plt 
import matplotlib.patches as patches
'''
<-> list_useful 範例：
    x = [i for i in range(10)]
    ob = list_userful(x)
    ob

'''

class list_userful():
    def __init__(self,list) -> list:
        self.list = list
    def to_upper(self):
        d = dict()
        for i in self.list:
            d[i] = d.get(i,0) + 1
        self.dict = d
        key = list(self.dict.keys())
        value = list(self.dict.values())
        self.dataframe = pd.DataFrame({'種類':key,'值':value}).sort_values('值',ascending=False)

    def __repr__(self) -> str:
        return(self.__class__.__name__)

class dataframe_useful():
    def __init__(self,data:pd.DataFrame):
        self.data = data
    def general_status(self):
        len_Nums,NA_Nums,ratio_Nums = [],[],[]
        for i in self.data.columns.tolist():
            na = self.data[i].isna().sum()
            le = len(self.data[i])
            NA_Nums.append(na)
            len_Nums.append(le)
            ratio_Nums.append(na/le)
        self.na_ratio = ratio_Nums
        na_col_20,na_col_50,na_col_80,na_col_100 = [],[],[],[]
        for i in range(len(self.na_ratio)):
            x = self.na_ratio[i]
            col =self.data.columns.tolist()[i]
            if x < 0.2:
                na_col_20.append(col)
            elif ( (x>=0.2) & (x<0.5)):
                na_col_50.append(col)
            elif ( (x>=0.5) & (x<0.8) ):
                na_col_80.append(col)
            else:
                na_col_100.append(col)
        self.na_col_20 = na_col_20
        self.na_col_50 = na_col_50
        self.na_col_80 = na_col_80
        self.na_col_100 = na_col_100


