import numpy as np
# ============================================================================
# 3. ARRAY CREATION METHODS
# ============================================================================
print("\n3. ARRAY CREATION METHODS")
print("-" * 20)

# Zeros, ones, empty
zeros = np.zeros((3, 4))  # 3x4 array of zeros
ones = np.ones((2, 3))  # 2x3 array of ones
empty = np.empty((2, 2))  # Uninitialized array (faster but random values)
print("\nZeros (3x4):\n", zeros)
print("\nZeros (3x4):\n", zeros)
print("\nOnes (2x3):\n", ones)
print("\nEmpty (2x2):\n", empty)

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

