import numpy as np

# ============================================================================
# 6. LINEAR ALGEBRA
# ============================================================================
print("\n\n6. LINEAR ALGEBRA")
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