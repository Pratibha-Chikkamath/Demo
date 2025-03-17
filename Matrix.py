import numpy as np

# Define two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix addition
C = A + B
print("Matrix Addition:\n", C)

# Matrix multiplication
D = np.dot(A, B)
print("Matrix Multiplication:\n", D)

# Transpose of a matrix
E = A.T
print("Transpose of A:\n", E)

# Determinant of a matrix
F = np.linalg.det(A)
print("Determinant of A:", F)

# Inverse of a matrix
G = np.linalg.inv(A)
print("Inverse of A:\n", G)
