import pandas as pd
import seaborn as sns
from statistics import mode
tips=sns.load_dataset("tips")
df=pd.DataFrame(data=tips)
print("First 5 rows of the Tips dataset:")
print(df.head())
mean_values=df.mean(numeric_only=True)
print("\nMean Values:")
print(mean_values)
median_values=df.median(numeric_only=True)
print("\nMedian Values:")
print(median_values)
mode_values=df.mode().iloc[0]
print("\nMode Values:")
print(mode_values)
