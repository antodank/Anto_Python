import numpy as np
# ============================================================================
# 16. ADVANCED INDEXING
# ============================================================================
print("\n\n16. ADVANCED INDEXING")
print("-" * 80)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Array:\n", arr)

# Fancy indexing (using arrays as indices)
rows = np.array([0, 2])
cols = np.array([1, 2])
print("\nElements at (0,1) and (2,2):", arr[rows, cols])

# Integer array indexing
indices = np.array([0, 2, 1])
print("Rows [0, 2, 1]:\n", arr[indices])

# ============================================================================
# 17. COPYING AND VIEWS
# ============================================================================
print("\n\n17. COPYING AND VIEWS")
print("-" * 80)

original = np.array([1, 2, 3, 4, 5])
print("Original:", original)

# View (shares memory)
view = original.view()
view[0] = 999
print("After modifying view - Original:", original)  # Changed!

# Copy (independent)
original = np.array([1, 2, 3, 4, 5])
copy = original.copy()
copy[0] = 888
print("After modifying copy - Original:", original)  # Unchanged

# ============================================================================
# 18. USEFUL UTILITY FUNCTIONS
# ============================================================================
print("\n\n18. USEFUL UTILITY FUNCTIONS")
print("-" * 80)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Array:\n", arr)
print("Shape:", arr.shape)
print("Size (total elements):", arr.size)
print("Ndim (number of dimensions):", arr.ndim)
print("Dtype:", arr.dtype)
print("Item size (bytes):", arr.itemsize)
print("Total bytes:", arr.nbytes)

# Repeating and tiling
print("\nRepeat each element 3 times:", np.repeat(np.array([1, 2, 3]), 3))
print("Tile array 2 times:", np.tile(np.array([1, 2, 3]), 2))