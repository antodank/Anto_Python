import numpy as np

a = np.array(
[[2,3],
 [2,3]])

b = np.array(
[[3,4],
 [5,6]])

print("Basic array a:\n", a)
print("Basic array b:\n", b)

# ============================================================================
# BASIC ARITHMETIC OPERATIONS
# ============================================================================
print("\n\n1. BASIC ARITHMETIC OPERATIONS")
print("-" * 80)
print("\nAddition (a + b):\n", a + b)
print("\nSubtraction (a - b):\n", a - b)
print("\nElement-wise multiplication (a * b):\n", a * b)
print("\nElement-wise division (a / b):\n", a / b)
print("\nPower (a ** 2):\n", a ** 2)
print("\nModulo (b % 2):\n", b % 2)


# ============================================================================
# INDEXING AND SLICING
# ============================================================================
print("\n\n 2.INDEXING AND SLICING")
print("-" * 80)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original array:\n", arr)
print("\nElement at [0, 1]:", arr[0, 1])  # Row 0, Column 1
print("First row:", arr[0, :])  # All columns of row 0
print("Second column:", arr[:, 1])  # All rows of column 1
print("Subarray (first 2 rows, last 2 cols):\n", arr[:2, 1:])

# Negative indexing
print("\nLast element:", arr[-1, -1])
print("Last row:", arr[-1, :])

