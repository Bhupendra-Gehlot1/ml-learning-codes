import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_theme()

# tips = sns.load_dataset("tips")
# print(tips.head());

# sns.relplot(data=tips,x="total_bill",y="tip",col="time",hue="smoker",style="sex",size="size")
# plt.show()

# iris = sns.load_dataset("iris")
# # print(iris.head())

# sns.scatterplot(x="sepal_length",y="petal_length",data=iris,hue="species",style="species",size="species")
# plt.show()


# titanic = sns.load_dataset("titanic")
# print(titanic.head())

# sns.countplot(x="sex",data=titanic)
# sns.countplot(x="class",data=titanic)
# plt.show()

# sns.barplot(x='sex',y='survived',hue="class",data=titanic)
# plt.show()


from sklearn.datasets import fetch_california_housing
housing=fetch_california_housing()
housing_df= pd.DataFrame(housing.data,columns=housing.feature_names)
housing_df['price'] = housing.target
print(housing_df.head())
# sns.displot(housing_df['price'])
# sns.distplot(housing_df['price'])
# plt.show()


correlation=housing_df.corr();
plt.figure(figsize = (10,10))
sns.heatmap(correlation,cbar=True,square=True,fmt='.1f',annot=True,annot_kws={'size':13},cmap="Blues")
plt.show()