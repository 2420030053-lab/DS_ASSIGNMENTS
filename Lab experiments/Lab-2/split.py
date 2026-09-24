import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
b = np.split(a, 3)   # split into 3 equal parts
print(b)

x = np.array([[1, 2], [3, 4], [5, 6]])
y = np.split(x, 3)   # split rows into 3 parts
print(y)
