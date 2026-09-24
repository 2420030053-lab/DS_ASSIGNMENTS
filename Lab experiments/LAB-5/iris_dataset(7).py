import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Use the full path to the file
iris = pd.read_csv(r"C:\Data sciences\LAB-5\Iris.csv")
print("Original Data (first 5 rows):")
print(iris.head())

numeric_cols = ['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']

scaler_minmax = MinMaxScaler()
iris_normalized = iris.copy()
iris_normalized[numeric_cols] = scaler_minmax.fit_transform(iris[numeric_cols])
print("\nNormalized Data:")
print(iris_normalized.head())

scaler_standard = StandardScaler()
iris_standardized = iris.copy()
iris_standardized[numeric_cols] = scaler_standard.fit_transform(iris[numeric_cols])
print("\nStandardized Data (first 5 rows):")
print(iris_standardized.head())

iris_onehot = pd.get_dummies(iris, columns=['Species'])
print("\nOne-Hot Encoded Data (first 5 rows):")
print(iris_onehot.head())

pca = PCA(n_components=2)
pca_result = pca.fit_transform(iris_standardized[numeric_cols])
pca_df = pd.DataFrame(data=pca_result, columns=['PC1','PC2'])
print("\nExplained Variance Ratio:", pca.explained_variance_ratio_)
print("\nPCA Result:")
print(pca_df.head())

plt.figure(figsize=(8,6))
plt.scatter(pca_df['PC1'], pca_df['PC2'],
            c=iris['Species'].astype('category').cat.codes,
            cmap='viridis', alpha=0.7)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Projection of Iris Dataset (colored by Species)')
plt.colorbar(label='Species')
plt.show()
