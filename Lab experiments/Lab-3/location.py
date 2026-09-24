import pandas as pd
data = {'apples':[3,2,0,1], 'oranges':[0,3,7,2]}
df = pd.DataFrame(data, index=['Ahmad','Ali','Rashed','Hamza'])
print(df.loc['Ali'])   # Correct way to access Ali's row
print(df)
