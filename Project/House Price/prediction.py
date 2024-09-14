import numpy as np;
import pandas as pd
import seaborn as sns
import sklearn.datasets 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics

house_price_data = pd.read_csv('D:\ML\Project\House Price\housing.csv')
# print(house_price_data)
# print(house_price_data.shape)
# print(house_price_data.info())
# print(house_price_data.describe())
correlation = house_price_data.corr()

# plt.figure(figsize=(10,10))
# sns.heatmap(correlation,cmap="Blues",cbar=True,annot_kws={'size':8},square=True,annot=True,fmt='.1f')
# plt.show()

X = house_price_data.drop(['PRICE'],axis=1) 
Y = house_price_data['PRICE']
print(X)
print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=3)
