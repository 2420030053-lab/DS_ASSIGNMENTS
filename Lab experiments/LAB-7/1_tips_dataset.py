import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plt.figure(figsize=(6,4))
sns.histplot(tips['total_bill'], bins=20, kde=True)
plt.title("Histogram of Total Bill")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x=tips['total_bill'])
plt.title("Boxplot of Total Bill")
plt.show()

species_counts = tips['smoker'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Smoker Distribution")
plt.show()
