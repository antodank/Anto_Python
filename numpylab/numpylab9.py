import numpy as np
# ============================================================================
# 12. BROADCASTING
# ============================================================================
print("\n\n12. BROADCASTING")
print("-" * 80)

arr = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 10
print("Array:\n", arr)
print("\nAdd scalar 10:\n", arr + scalar)

# Broadcasting with 1D array
vec = np.array([10, 20, 30])
print("\nAdd 1D array [10, 20, 30] to each row:\n", arr + vec)

# Broadcasting with column vector
col = np.array([[10], [20]])
print("\nAdd column vector [[10], [20]]:\n", arr + col)

# ============================================================================
# 13. AGGREGATION WITH AXIS
# ============================================================================
print("\n\n13. AGGREGATION WITH AXIS")
print("-" * 80)

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Data:\n", data)
print("\nSum (all):", np.sum(data))
print("Sum (axis=0 - column sum):", np.sum(data, axis=0))
print("Sum (axis=1 - row sum):", np.sum(data, axis=1))

# Cumulative sum and product
print("\nCumulative sum:", np.cumsum(data))
print("Cumulative sum (axis=1):\n", np.cumsum(data, axis=1))
print("\nCumulative product:", np.cumprod(np.array([1, 2, 3, 4, 5])))

# ============================================================================
# 14. CLIPPING AND REPLACING
# ============================================================================
print("\n\n14. CLIPPING AND REPLACING")
print("-" * 80)

data = np.array([1, 5, 10, 15, 20, 25, 30])
print("Original:", data)
print("Clip to [10, 20]:", np.clip(data, 10, 20))

# Replace NaN values
data_with_nan = np.array([1.0, 2.0, np.nan, 4.0, np.nan])
print("\nData with NaN:", data_with_nan)
print("Is NaN:", np.isnan(data_with_nan))
data_no_nan = np.nan_to_num(data_with_nan, nan=0.0)
print("Replace NaN with 0:", data_no_nan)

# ============================================================================
# 15. SET OPERATIONS
# ============================================================================
print("\n\n15. SET OPERATIONS")
print("-" * 80)

a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7, 8])
print("Array a:", a)
print("Array b:", b)

print("\nIntersection:", np.intersect1d(a, b))
print("Union:", np.union1d(a, b))
print("Set difference (a - b):", np.setdiff1d(a, b))
print("Set difference (b - a):", np.setdiff1d(b, a))

# Check membership
print("\nIs 3 in a?", np.isin(3, a))
print("Which elements of a are in b?", np.isin(a, b))