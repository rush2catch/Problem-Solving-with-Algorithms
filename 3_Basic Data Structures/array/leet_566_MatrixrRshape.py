# Problem: Reshape the Matrix
# Difficulty: Easy
# Category: Array
# Leetcode 566: https://leetcode.com/problems/reshape-the-matrix/#/description
# Description:
"""
    In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix
    into a new one with different size but keep its original data.
    You're given a matrix represented by a two-dimensional array, and two positive integers
    r and c representing the row number and column number of the wanted reshaped matrix, respectively.
    The reshaped matrix need to be filled with all the elements of the original matrix
    in the same row-traversing order as they were.
    If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix;
    Otherwise, output the original matrix.

    Example 1:
    Input:
    nums =
    [[1,2],
     [3,4]]
    r = 1, c = 4
    Output:
    [[1,2,3,4]]
    Explanation:
    The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix,
    fill it row by row by using the previous list.
    Example 2:
    Input:
    nums =
    [[1,2],
     [3,4]]
    r = 2, c = 4
    Output:
    [[1,2],
     [3,4]]
    Explanation:
    There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
"""


# @Solution 1
"""
Solution 1 contains two steps:
1. convert the original matrix to a one row matrix or a list;
   in this step, two for loops are used, thus the time complexity is O(n*2)
2. convert the list to the new matrix, it takes O(n) in this step
Thus, the time complexity of this solution is 0(n*2), which needs to be improved
"""


def matrix_reshape(matrix, row, column):

    # 0. initialize
    if len(matrix) == 0:
        return matrix
    new_matrix = []
    traverse_matrix = []
    minimal = row * column

    # 1. first convert the input matrix to a list
    for rowNum in range(len(matrix)):
        for colNum in range(len(matrix[rowNum])):
            traverse_matrix.append(matrix[rowNum][colNum])

    # 2. convert the after traversing matrix into the objective matrix
    if (len(traverse_matrix) % minimal is 0) and (len(traverse_matrix) >= minimal):
        for i in range(row):
            new_matrix.append(traverse_matrix[i * column:(i + 1) * column])
        return new_matrix
    else:
        return matrix

print(matrix_reshape([[1, 2], [3, 4]], 1, 4))
print(matrix_reshape([[1, 2], [3, 4]], 2, 4))
print(matrix_reshape([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]], 5, 3))
print(matrix_reshape([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]], 4, 3))
print(matrix_reshape([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]], 15, 1))
print(matrix_reshape([], 1, 1))
