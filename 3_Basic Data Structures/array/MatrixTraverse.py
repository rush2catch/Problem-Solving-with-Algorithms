"""
given a matrix, convert it to a one row  matrix or list
@:arg matrix
"""


def matrix_traverse(matrix):
    if len(matrix) == 0:
        return None
    new_matrix = []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            new_matrix.append(matrix[row][column])
    return new_matrix

print(matrix_traverse([[1, 2, 3], [4, 5, 6]]))
print(matrix_traverse([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
