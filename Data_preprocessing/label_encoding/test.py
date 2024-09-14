import pandas as pd;
import sklearn.datasets
import seaborn as sns;
from sklearn.preprocessing import LabelEncoder

dataset = sklearn.datasets.load_breast_cancer();
dataset_pd = pd.DataFrame(dataset.data,columns=dataset.feature_names)
# print(dataset_pd.head())

iris = sns.load_dataset("iris")
# print(iris)
# print(iris['species'].value_counts())

# print(dataset_pd['diagnosis'].value_counts())
# print(dataset_pd['mean radius'].value_counts())

labels = LabelEncoder();
labeled_data = labels.fit_transform(iris.species)
# print(labeled_data)

iris['target'] = labeled_data
print(iris)