import numpy as np
a = np.array([10, 20, 30, 40, 50])
indices = np.where(a > 25) # Find indices where values are greater than 25
print("Values:", a[indices])
