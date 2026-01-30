import numpy as np

a = np.array(
[[2,3],
 [2,3]])

b = np.array(
[[3,4],
 [5,6]])

c = a + b
d = a * b
print("Addition:\n", c)
print("Multiplication:\n", d)


arr = np.array([[1,2,3],[4,5,6]])
print(arr[0, 1])
print(arr[:, 1])


arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
reshape1 = arr1.reshape((4, 3))
reshape2 = arr1.reshape((3, 4))
print("reshape1 :\n", reshape1)
print("reshape2 :\n", reshape2)
