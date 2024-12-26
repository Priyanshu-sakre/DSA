import numpy


# brute
def rows(matrix, j):
    for i in range(len(matrix)):
        if matrix[i][j] != 0:
            matrix[i][j] = float("-inf")
    return matrix


def columns(matrix, i):
    for j in range(len(matrix[0])):
        if matrix[i][j] != 0:
            matrix[i][j] = float("-inf")
    return matrix


def set_zeros(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                rows(matrix, j)
                columns(matrix, i)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == float("-inf"):
                matrix[i][j] = 0
    return matrix


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
# print(numpy.matrix(set_zeros(matrix)))


# better
def set_zeros2(matrix):
    rows = [0] * len(matrix)
    columns = [0] * len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                rows[i] = 1
                columns[j] = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if rows[i] == 1 or columns[j] == 1:
                matrix[i][j] = 0
    return matrix


print(numpy.matrix(set_zeros2(matrix)))
