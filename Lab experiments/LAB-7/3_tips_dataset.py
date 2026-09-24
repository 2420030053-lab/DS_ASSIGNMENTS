import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species_name'] = df['species'].map({i:name for i, name in enumerate(iris.target_names)})

plt.figure(figsize=(6,4))
sns.heatmap(df.iloc[:, :-1].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Iris Features")
plt.show()

plt.figure(figsize=(6,4))
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], s = df['petal length (cm)'] * 20, alpha=0.5, c=df['species'], cmap='viridis')
plt.title("Bubble Plot of Sepal Length vs Sepal Width")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.show()

sns.pairplot(df.iloc[:, :4])
plt.suptitle("Pair Plot of Iris Features, y = 1.02")
plt.show()