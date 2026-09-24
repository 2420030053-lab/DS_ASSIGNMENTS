import pandas as pd

data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
df = pd.DataFrame.from_dict(data, orient = 'index', columns=['A','B','C','D'])

print(df)

student roll no, name, age, section, 3 different sub marks, data scence, qc and toc marks, create 10 rows for all thesevalues, create data frame and convert data frame to csv