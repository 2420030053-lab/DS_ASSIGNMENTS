import seaborn as sns
import pandas as pd

# Load Titanic dataset
titanic = sns.load_dataset("titanic")

# 1. Handle missing values with median (numeric only)
for col in titanic.select_dtypes(include="number").columns:
    titanic[col] = titanic[col].fillna(titanic[col].median())

# For categorical variables, we’ll still use mode (most frequent value)
for col in titanic.select_dtypes(include="object").columns:
    titanic[col] = titanic[col].fillna(titanic[col].mode()[0])
titanic = titanic.drop_duplicates()
titanic_encoded = pd.get_dummies(titanic, drop_first=True)
titanic_encoded["family_size"] = titanic["sibsp"] + titanic["parch"] + 1
print(titanic_encoded.head())
