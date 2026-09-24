import pandas as pd
data = {'apples': [3, 2, 0, 1], 'oranges': [0, 3, 7, 2]}
df = pd.DataFrame(data, index=['Ahmad', 'Ali', 'Rashed', 'Hamza'])
df.to_csv("abcd.csv", index=True)
print("CSV file 'abcd.csv' is created")
