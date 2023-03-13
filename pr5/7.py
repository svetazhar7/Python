def inv(A):
    n = len(A)
    det_A = det(A)
    if det_A == 0:
        raise ValueError("Матрица вырожденная, обратной не существует")
    alg_A_T = [[alg(A, j, i) for i in range(n)] for j in range(n)]
    inv_A = [[alg_A_T[i][j] / det_A for j in range(n)] for i in range(n)]
    return inv_A


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

def det(A, i=0):
    n = len(A)
    if n == 2:
        return smalldet(A)
    else:
        determinant = 0
        for j in range(n):
            submat = submatrix(A, i, j)
            sign = (-1) ** (i + j)
            coeff = A[i][j]
            determinant += sign * coeff * det(submat, i+1)
        return determinant

def minor(A, i, j):
    submat = submatrix(A, i, j)
    return det(submat)
def smalldet(matrix):

    # Вычисляем определитель
    determinant = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    return determinant


def alg(A, i=1, j=1):
    return (-1) ** (i+j) * minor(A, i, j)

def algmatrix(A):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = alg(A, i, j)
    return result

def transpose(A):
    n = len(A)
    m = len(A[0])
    # Создаем новую матрицу
    new_A = []
    for j in range(m):
        new_row = []
        for i in range(n):
            new_row.append(A[i][j])
        new_A.append(new_row)
    return new_A



def inv(A):
    n = len(A)
    det_A = det(A)
    if det_A == 0:
        raise ValueError("Матрица вырожденная, обратной не существует")
    algmatrix_A_T = algmatrix(transpose(A))
    inv_A = [[algmatrix_A_T[i][j] / det_A for j in range(n)] for i in range(n)]
    return inv_A



A =[[0,2,1,4],[1,0,3,2],[0,1,4,0],[1,2,1,1]]
print(inv(A))
