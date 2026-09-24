import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student.csv")

sns.histplot(df['Attendance'].dropna(), bins=10, kde=True)
plt.title("Attendance Distribution")
plt.show()
