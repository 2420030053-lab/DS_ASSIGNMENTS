import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
parts = np.split(a, 3)
print("First part:", parts[0])
print("Second part:", parts[1])
print("Third part:", parts[2])
