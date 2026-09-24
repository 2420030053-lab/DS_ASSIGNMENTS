import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plt.figure(figsize=(6,4))
sns.violinplot(x=tips['day'], y=tips['total_bill'])
plt.title("Violin Plot of Total Bill by Day")
plt.show()
