import seaborn as sns
import pandas as pd
students = sns.load_dataset("student")
# 1. Handle missing values
for col in students.select_dtypes(include="number").columns:
    students[col] = students[col].fillna(students[col].median())

for col in students.select_dtypes(include="object").columns:
    students[col] = students[col].fillna(students[col].mode()[0])

# 2. Drop duplicates
students = students.drop_duplicates()

# 3. Encode categorical variables
students_encoded = pd.get_dummies(students, drop_first=True)

# 4. Feature engineering: Family size
students_encoded["family_size"] = 1  # placeholder, same as Titanic pipeline

print(students_encoded.head()) 
