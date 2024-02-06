import numpy as np

def add_matrices(matrix1, matrix2):
    result = np.add(matrix1, matrix2)
    return result.tolist()

def subtract_matrices(matrix1, matrix2):
    result = np.subtract(matrix1, matrix2)
    return result.tolist()

def multiply_matrices(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result.tolist()

def find_determinant(matrix):
    if len(matrix) == 2:
        determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif len(matrix) == 3:
        determinant = np.linalg.det(matrix)
    else:
        raise ValueError("Unsupported matrix size")
    return determinant
