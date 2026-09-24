import pandas as pd
df = pd.read_csv("Iris.csv")
print(df.shape)  
dup_df = pd.concat([df, df])
dup_df.drop_duplicates(inplace=False)
print(dup_df.shape)
