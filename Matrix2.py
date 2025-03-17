import numpy as np

# Define two matrices
A = np.array([[3, 5, 7], [2, 6, 4], [8, 1, 9]])
B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Matrix addition
C = A + B
print("Matrix Addition:\n", C)

# Matrix multiplication
D = np.dot(A, B)
print("Matrix Multiplication:\n", D)

# Element-wise division
E = A / (B + 1)  # Adding 1 to avoid division by zero
print("Element-wise Division:\n", E)

# Trace of the matrix
F = np.trace(A)
print("Trace of A:", F)

# Singular Value Decomposition (SVD)
U, S, V = np.linalg.svd(A)
print("Singular Values of A:\n", S)
