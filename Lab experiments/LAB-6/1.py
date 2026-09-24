import pandas as pd
from sklearn.datasets import load_iris
from statistics import mode
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
print("First 5 rows of the Iris dataset:")
print(df.head())
mean_values = df.mean()
print("\nMean Values:")
print(mean_values)
median_values = df.median()
print("\nMedian Values:")
print(median_values)
mode_values = df.mode().iloc[0]
print("\nMode Values:")
print(mode_values)