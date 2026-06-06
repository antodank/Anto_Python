import numpy as np

# ============================================================================
# 5. STATISTICAL OPERATIONS
# ============================================================================
print("\n\n5. STATISTICAL OPERATIONS")
print("-" * 80)

data = np.array([[10, 20, 30], 
                 [40, 50, 60], 
                 [70, 80, 90]])
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