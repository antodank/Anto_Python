import numpy as np
# ============================================================================
# 10. SORTING AND SEARCHING
# ============================================================================
print("\n\n10. SORTING AND SEARCHING")
print("-" * 80)

unsorted = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print("Unsorted:", unsorted)
print("Sorted:", np.sort(unsorted))
print("Argsort (indices that would sort):", np.argsort(unsorted))

# 2D sorting
arr_2d = np.array([[3, 2, 1], [6, 5, 4]])
print("\n2D array:\n", arr_2d)
print("Sort along axis=1 (rows):\n", np.sort(arr_2d, axis=1))

# Find unique values
duplicates = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
unique_vals = np.unique(duplicates)
unique_counts = np.unique(duplicates, return_counts=True)
print("\nArray with duplicates:", duplicates)
print("Unique values:", unique_vals)
print("Unique with counts:", unique_counts)