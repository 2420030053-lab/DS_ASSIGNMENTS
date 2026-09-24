import numpy as np

# 1D array
a = np.array([1, 2, 3, 4])
for i in a:
    print(i)

# 2D array
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
for row in b:
    for val in row:
        print(val)
