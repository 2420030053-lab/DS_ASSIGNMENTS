import pandas as pd
import seaborn as sns
from statistics import mode
tips=sns.load_dataset("tips")
df=pd.DataFrame(data=tips)
print("First 5 rows of the Tips dataset:")
print(df.head())
range_values=df.max(numeric_only=True)-df.min(numeric_only=True)
print("\nRange Values:")
print(range_values)
variance_values=df.var(numeric_only=True)
print("\nVariance Values:")
print(variance_values)
std_values=df.std(numeric_only=True)
print("\nStandard Deviation Values:")
print(std_values)
Q1=df.quantile(0.25,numeric_only=True)
Q3=df.quantile(0.75,numeric_only=True)
IQR=Q3-Q1
print("\nInterquartile Range (IQR) Values:")
print(IQR)
