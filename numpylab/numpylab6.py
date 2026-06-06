import numpy as np
# ============================================================================
# 7. ARRAY CONCATENATION AND STACKING
# ============================================================================
print("\n\n7. ARRAY CONCATENATION AND STACKING")
print("-" * 80)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print("Array 1:\n", arr1)
print("\nArray 2:\n", arr2)

# Concatenate (axis=0 is vertical, axis=1 is horizontal)
vstack = np.concatenate([arr1, arr2], axis=0)  # or np.vstack([arr1, arr2])
hstack = np.concatenate([arr1, arr2], axis=1)  # or np.hstack([arr1, arr2])
print("\nVertical stack (concatenate axis=0):\n", vstack)
print("\nHorizontal stack (concatenate axis=1):\n", hstack)

# Stack (adds new dimension)
stacked = np.stack([arr1, arr2], axis=0)  # Shape: (2, 2, 2)
print("\nStack (axis=0) shape:", stacked.shape)
print(stacked)

# ============================================================================
# 8. SPLITTING ARRAYS
# ============================================================================
print("\n\n8. SPLITTING ARRAYS")
print("-" * 80)

arr = np.arange(12).reshape(4, 3)
print("Original array:\n", arr)

# Split vertically (row-wise)
split_rows = np.split(arr, 2, axis=0)  # Split into 2 parts along rows
print("\nSplit into 2 parts (rows):")
for i, part in enumerate(split_rows):
    print(f"Part {i+1}:\n{part}")

# Split horizontally (column-wise)
split_cols = np.split(arr, 3, axis=1)  # Split into 3 parts along columns
print("\nSplit into 3 parts (columns):")
for i, part in enumerate(split_cols):
    print(f"Part {i+1}:\n{part}")