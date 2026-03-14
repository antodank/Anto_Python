import numpy as np

a = np.array(
[[2,3],
 [2,3]])

b = np.array(
[[3,4],
 [5,6]])

print("\nAddition (a + b):\n", a + b)
print("\nSubtraction (a - b):\n", a - b)
print("\nElement-wise multiplication (a * b):\n", a * b)
print("\nElement-wise division (a / b):\n", a / b)
print("\nPower (a ** 2):\n", a ** 2)
print("\nModulo (b % 2):\n", b % 2)


arr = np.array([[1,2,3],[4,5,6]])
print(arr[0, 1]) # 0th row, 1st column
print(arr[:, 1]) # : means all rows, 1 means 1st column. So this will print the 1st column of the array.


arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

# reshape1 will have 4 rows and 3 columns. The total number of elements (4*3=12) must match the number of elements in arr1 (which is 12). If the total number of elements does not match, it will raise an error.
reshape1 = arr1.reshape((4, 3))

#
reshape2 = arr1.reshape((3, 4))
print("reshape1 :\n", reshape1)
print("reshape2 :\n", reshape2)
