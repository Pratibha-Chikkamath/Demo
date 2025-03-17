import numpy as np

# Define a matrix
A = np.array([[2, 4, 6], [1, 3, 5], [7, 8, 9]])

# Scalar multiplication
B = 3 * A
print("Scalar Multiplication (3 * A):\n", B)

# Matrix subtraction
C = A - np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print("Matrix Subtraction:\n", C)

# Element-wise multiplication
D = A * A
print("Element-wise Multiplication:\n", D)

# Rank of the matrix
E = np.linalg.matrix_rank(A)
print("Rank of A:", E)

# Eigenvalues and Eigenvectors
values, vectors = np.linalg.eig(A)
print("Eigenvalues of A:\n", values)
print("Eigenvectors of A:\n", vectors)
