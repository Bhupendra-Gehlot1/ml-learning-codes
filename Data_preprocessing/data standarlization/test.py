import pandas as pd;
import numpy as np;
import sklearn.datasets;
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

dataset = sklearn.datasets.load_breast_cancer()
# print(dataset)

dataset_pd = pd.DataFrame(dataset.data,columns=dataset.feature_names)
print(dataset_pd.head())
# dataset_pd['target']=dataset.target
# print(dataset_pd.head())
# print(dataset_pd.shape)

# print(dataset_pd.notnull().sum())

X=dataset_pd;
Y=dataset.target;

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=3)

# print(X_test.shape,X_train.shape)

# print(dataset.data.std())

scaler = StandardScaler()
scaler.fit(X_train)
X_train_standardized = scaler.transform(X_train)
# print(X_train_standardized) 
X_test_standardized = scaler.transform(X_test)
print(X_test_standardized) 
print(X_test_standardized.std())
print(X_train_standardized.std())