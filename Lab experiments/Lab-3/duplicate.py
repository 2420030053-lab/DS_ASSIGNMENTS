import pandas as pd
df = pd.read_csv("Iris.csv")
print(df.shape)
dup_df = pd.concat([df, df])
print(dup_df.shape)
