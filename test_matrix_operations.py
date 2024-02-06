import numpy as np
from matrix_operations import add_matrices, subtract_matrices, multiply_matrices, find_determinant

# Sample matrices for testing
matrix1_2x2 = [[1, 2], [3, 4]]
matrix2_2x2 = [[5, 6], [7, 8]]

matrix1_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2_3x3 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Test add_matrices
result_add_2x2 = add_matrices(matrix1_2x2, matrix2_2x2)
print("Addition of 2x2 matrices:")
print(result_add_2x2)

result_add_3x3 = add_matrices(matrix1_3x3, matrix2_3x3)
print("Addition of 3x3 matrices:")
print(result_add_3x3)

# Test subtract_matrices, multiply_matrices, and find_determinant similarly
