import numpy as np
# ============================================================================
# 9. BOOLEAN INDEXING AND MASKING
# ============================================================================
print("\n\n9. BOOLEAN INDEXING AND MASKING")
print("-" * 80)

data = np.array([10, 25, 30, 45, 50, 65, 70])
print("Data:", data)

# Boolean mask
mask = data > 30
print("\nMask (data > 30):", mask)
print("Elements > 30:", data[mask])

# Multiple conditions
mask2 = (data > 20) & (data < 60)  # Use & (and), | (or), ~ (not)
print("\nElements between 20 and 60:", data[mask2])

# Where function
result = np.where(data > 40, 1, 0)  # If > 40: 1, else: 0
print("\nWhere (>40 -> 1, else -> 0):", result)

# Replace values using mask
data_copy = data.copy()
data_copy[data_copy < 30] = 0
print("Replace values < 30 with 0:", data_copy)