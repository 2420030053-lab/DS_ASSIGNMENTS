import numpy as np
a = np.array([1, 2, 3])                 # 1D array
b = np.array([[1, 2, 3], [4, 5, 6]])    # 2D array
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # 3D array
print(a.shape)
print(b.shape)
print(c.shape)
print(a.ndim)
print(b.ndim)
print(c.ndim)