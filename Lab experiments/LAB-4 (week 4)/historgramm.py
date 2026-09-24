import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv("student.csv")
sns.histplot(df['Age'], bins=20, kde=True)
plt.title("Age Distribution")
plt.show()
