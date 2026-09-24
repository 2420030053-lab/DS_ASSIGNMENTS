import numpy as np

n1 = np.array([1,2,3,4])
n2 = np.array([5,6,7,8])
print(np.sum([n1,n2]))   

n3 = np.array([10,11,12,13])
n4 = np.array([15,16,17,18])
print(np.sum([n3,n4], axis=1))  

n5 = np.array([20,21,22,23])
n6 = np.array([26,27,28,29]) 
print(np.sum([n5,n6], axis=0))   

print(np.subtract(n1,n2))
print(np.multiply(n1,n2))
print(np.divide(n1,n2))
print(np.subtract(n3,n4))
print(np.multiply(n3,n4))
print(np.divide(n3,n4))
print(np.subtract(n5,n6))
print(np.multiply(n5,n6))
print(np.divide(n5,n6))
