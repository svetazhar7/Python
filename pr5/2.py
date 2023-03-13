def submatrix(A, i, j):

    if i >= len(A) or j >= len(A[0]):
        raise ValueError("Индексы строки и столбца должны быть меньше размера матрицы")
    # Создаем новую матрицу
    new_A = []
    for row in range(len(A)):
        if row == i:
            continue  # Пропускаем заданную строку
        new_row = []
        for col in range(len(A[row])):
            if col == j:
                continue  # Пропускаем заданный столбец
            new_row.append(A[row][col])
        new_A.append(new_row)

    return new_A

A = [[0, 2, 1], [1, 4, 3], [2, 1, 1]]
print(submatrix(A,0,0))
print(submatrix(A,1,1))
print(submatrix(A,2,1))
