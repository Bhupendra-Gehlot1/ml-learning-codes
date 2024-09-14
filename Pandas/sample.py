import pandas as pd;
import numpy as np

from sklearn.datasets import fetch_california_housing

# housing = fetch_california_housing() 

# # print(housing)

# housing_df = pd.DataFrame(housing.data,columns=housing.feature_names) # change to data frame

# print(housing_df.head())      # top 5 entries
# print(housing_df.tail())      # last 5 entries

# print(housing_df.shape)       #dimensions

# csv files PD DF
# diabets_data = pd.read_csv("")    #csv to df

# PD DF from excel file
# data = pd.read_excel("path")      #excel to df

# DF to csv
# housing_df.to_csv('housing.csv')      # df to csv
# housing_df2 = pd.read_csv('D:\ML\Pandas\housing.csv') #path should be passed
# print(housing_df2.head()) 

# DF to excel
# housing_df.to_excel("action.xlsx")   #df to excel

# random_df = pd.DataFrame(np.random.rand(20,10))       # random df generate
# # random_df = pd.DataFrame(np.random.randint(20,50,(20,10))) #random df in range 
# print(random_df.head())


# print(housing_df.info())       # while info gives not null values as well 
# print(housing_df.isnull().sum())      #give null values each col
# print(housing_df.head())      
# print(housing_df.value_counts('HouseAge'))        #individual value count
# print(housing_df.groupby('HouseAge').mean());     #mean of all other col for individual values of group

# print(housing_df.count())
# print(housing_df.mean())
# print(housing_df.std())
# print(housing_df.min())
# print(housing_df.max())
# print(housing_df.describe()) # all at one go



# housing_df['target']= housing.target  #add new col
# print(housing_df.head())

# print(housing_df)
# new_df = housing_df.drop(columns="MedInc", axis=1) #remove col if axis =1 and if axis = 0 give index of row to remove
# print(new_df)
# housing_df.drop(columns='HouseAge',axis=1)
# print(housing_df)

# print(housing_df.iloc[0])     # specific row
# print(housing_df.iloc[:,-1]) # specific col
# print(housing_df.shape)

# print(housing_df.corr())  all correlation - positive negative