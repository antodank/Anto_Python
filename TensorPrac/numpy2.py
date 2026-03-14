import numpy as np

print("=" * 20)
print("NUMPY COMPREHENSIVE GUIDE - EXTREMELY USEFUL OPERATIONS")
print("=" * 20)

# ============================================================================
# 1. ARRAY CREATION METHODS
# ============================================================================
print("\n1. ARRAY CREATION METHODS")
print("-" * 20)

# Basic array creation
a = np.array([[2, 3], [2, 3]])
print("Basic array:\n", a)

# Zeros, ones, empty
zeros = np.zeros((3, 4))  # 3x4 array of zeros
ones = np.ones((2, 3))  # 2x3 array of ones
empty = np.empty((2, 2))  # Uninitialized array (faster but random values)
print("\nZeros (3x4):\n", zeros)
print("\nZeros (3x4):\n", zeros)
print("\nOnes (2x3):\n", ones)

# Identity matrix
identity = np.eye(3)  # 3x3 identity matrix
print("\nIdentity matrix (3x3):\n", identity)

# Range and linspace
arange_arr = np.arange(0, 10, 2)  # Start, stop, step (like range())
linspace_arr = np.linspace(0, 10, 5)  # Start, stop, num_points (evenly spaced)
print("\nArange (0 to 10, step 2):", arange_arr)
print("Linspace (0 to 10, 5 points):", linspace_arr)

# Random arrays
np.random.seed(42)  # For reproducibility
random_uniform = np.random.rand(2, 3)  # Uniform [0, 1)
random_normal = np.random.randn(2, 3)  # Standard normal distribution
random_int = np.random.randint(0, 100, size=(3, 3))  # Random integers
print("\nRandom uniform [0,1):\n", random_uniform)
print("\nRandom normal distribution:\n", random_normal)
print("\nRandom integers [0,100):\n", random_int)

# Full (constant value)
full_arr = np.full((2, 3), 7)  # 2x3 array filled with 7
print("\nFull array (filled with 7):\n", full_arr)

# ============================================================================
# 2. BASIC ARITHMETIC OPERATIONS
# ============================================================================
print("\n\n2. BASIC ARITHMETIC OPERATIONS")
print("-" * 80)

a = np.array([[2, 3], [2, 3]])
b = np.array([[3, 4], [5, 6]])

print("Array a:\n", a)
print("\nArray b:\n", b)
print("\nAddition (a + b):\n", a + b)
print("\nSubtraction (a - b):\n", a - b)
print("\nElement-wise multiplication (a * b):\n", a * b)
print("\nElement-wise division (a / b):\n", a / b)
print("\nPower (a ** 2):\n", a ** 2)
print("\nModulo (b % 2):\n", b % 2)

# ============================================================================
# 3. INDEXING AND SLICING
# ============================================================================
print("\n\n3. INDEXING AND SLICING")
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

# ============================================================================
# 5. STATISTICAL OPERATIONS
# ============================================================================
print("\n\n5. STATISTICAL OPERATIONS")
print("-" * 80)

data = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("Data:\n", data)

print("\nMean (all elements):", np.mean(data))
print("Mean (axis=0 - column-wise):", np.mean(data, axis=0))
print("Mean (axis=1 - row-wise):", np.mean(data, axis=1))

print("\nMedian:", np.median(data))
print("Standard deviation:", np.std(data))
print("Variance:", np.var(data))

print("\nMin:", np.min(data))
print("Max:", np.max(data))
print("Sum:", np.sum(data))
print("Product:", np.prod(data))

print("\nArgmin (index of min):", np.argmin(data))
print("Argmax (index of max):", np.argmax(data))

# Percentiles
print("\n25th percentile:", np.percentile(data, 25))
print("75th percentile:", np.percentile(data, 75))

# ============================================================================
# 6. MATHEMATICAL FUNCTIONS
# ============================================================================
print("\n\n6. MATHEMATICAL FUNCTIONS")
print("-" * 80)

nums = np.array([1, 4, 9, 16, 25])
print("Original:", nums)
print("Square root:", np.sqrt(nums))
print("Exponential:", np.exp(np.array([1, 2, 3])))
print("Log (natural):", np.log(nums))
print("Log10:", np.log10(nums))
print("Power (nums^2):", np.power(nums, 2))

# Trigonometric
angles = np.array([0, np.pi/4, np.pi/2, np.pi])
print("\nAngles:", angles)
print("Sin:", np.sin(angles))
print("Cos:", np.cos(angles))
print("Tan:", np.tan(angles))

# Rounding
decimals = np.array([1.234, 5.678, 9.999])
print("\nOriginal:", decimals)
print("Round:", np.round(decimals, 2))
print("Floor:", np.floor(decimals))
print("Ceil:", np.ceil(decimals))

# Absolute value
print("\nAbsolute:", np.abs(np.array([-1, -2, 3, -4])))

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

# ============================================================================
# 11. LINEAR ALGEBRA
# ============================================================================
print("\n\n11. LINEAR ALGEBRA")
print("-" * 80)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Matrix A:\n", A)
print("\nMatrix B:\n", B)

# Matrix multiplication
matmul = np.matmul(A, B)  # or A @ B
print("\nMatrix multiplication (A @ B):\n", matmul)

# Dot product
dot = np.dot(A, B)
print("\nDot product:\n", dot)

# Determinant
det = np.linalg.det(A)
print("\nDeterminant of A:", det)

# Inverse
inv = np.linalg.inv(A)
print("\nInverse of A:\n", inv)

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("\nEigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# Trace (sum of diagonal)
trace = np.trace(A)
print("\nTrace of A:", trace)

# Diagonal
diag = np.diag(A)
print("Diagonal elements:", diag)

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

print("\n" + "=" * 80)
print("END OF NUMPY GUIDE")
print("=" * 80)
