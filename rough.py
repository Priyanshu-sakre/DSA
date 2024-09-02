matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]
print(matrix)
