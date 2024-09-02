from numpy import zeros, matrix


# brute
def rotate_matrix(matrix1):
    n = len(matrix1)
    nums = zeros((n, n))
    for i in range(n):
        for j in range(n):
            nums[j][n - i - 1] = matrix1[i][j]
    for i in range(n):
        for j in range(n):
            matrix1[i][j] = int(nums[i][j])
    return matrix1


matrix1 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
print(matrix(matrix1))
print(matrix(rotate_matrix(matrix1)))


# better
def rotate_matrix2(matrix1):
    n = len(matrix1)
    nums = [[matrix1[j][i] for j in range(len(matrix1))] for i in range(len(matrix1))]
    for i in range(n):
        for j in range(n):
            matrix1[i][n - j - 1] = nums[i][j]
    return matrix1


print(matrix(rotate_matrix2(matrix1)))
