def smalldet(matrix):

    # Вычисляем определитель
    determinant = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    return determinant


matrix = [[4, 3], [1, 1]]
print(smalldet(matrix))