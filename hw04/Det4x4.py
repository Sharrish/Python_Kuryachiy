"""

Определитель матрицы 4×4
Матрица 4×4 задаётся кортежем из 4 кортежей по 4 целых числа в каждом.
Посчитать точный определитель этой матрицы. Пользоваться itertools нельзя.

Примеры
Входные данные
(5, -4, 4, -7), (1, -2, 6, 0), (3, -8, -6, -4), (-1, 2, -9, 3)
Результат работы
702

"""


def matrix_without_column(matrix, col: int):
    matrix_new = []
    for row in matrix:
        matrix_new.append((*row[:col], *row[col+1:]))
    return tuple(matrix_new)


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    ans = 0
    mult = 1
    for i in range(len(matrix)):
        ans += mult * matrix[0][i] * determinant(matrix_without_column(matrix[1:], i))
        mult *= -1
    return ans


if __name__ == '__main__':
    matrix = eval(input())
    print(determinant(matrix))