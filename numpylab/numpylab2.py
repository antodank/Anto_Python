import numpy as np

# ============================================================================
# 4. RESHAPING AND MANIPULATION
# ============================================================================
print("\n\n4. RESHAPING AND MANIPULATION")
print("-" * 80)

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Original 1D array:", arr1)

# Reshape
reshape1 = arr1.reshape((4, 3))  # 4 rows, 3 columns
reshape2 = arr1.reshape((3, 4))  # 3 rows, 4 columns
print("\nReshape to (4,3):\n", reshape1)
print("\nReshape to (3,4):\n", reshape2)

# Reshape with -1 (auto-calculate dimension)
auto_reshape = arr1.reshape((2, -1))  # 2 rows, auto columns = 6
print("\nReshape to (2,-1) - auto calculate:\n", auto_reshape)

# Flatten and ravel
flat = reshape1.flatten()  # Returns a copy
ravel = reshape1.ravel()  # Returns a view if possible
print("\nFlattened:", flat)
print("Raveled:", ravel)

# Transpose
transposed = reshape1.T
print("\nTransposed (4,3) -> (3,4):\n", transposed)

# Add new axis
new_axis = arr1[:, np.newaxis]  # Convert (12,) to (12,1)
print("\nAdd new axis shape:", new_axis.shape)


