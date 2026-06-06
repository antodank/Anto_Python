import numpy as np

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