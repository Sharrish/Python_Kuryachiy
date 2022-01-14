"""

Объединение отрезков
Вводится кортеж пар натуральных чисел. Это координаты отрезков на прямой.
Рассмотрим объединение этих отрезков и найдём длину этого объединения
(т. е. совокупную длину всех «закрашенных» нашими отрезками отрезков на прямой).

Примеры
Входные данные
(66, 91), (152, 230), (21, 81), (323, 342), (158, 211), (286, 332), (294, 330), (18, 58), (183, 236)

Результат работы
213

"""


if __name__ == '__main__':
    sea_matrix = []
    first_string = str(input())
    sea_matrix.append('.' * len(first_string))
    while (last_string := str(input())) != first_string:
        sea_matrix.append(last_string)

    cnt_rect = 0
    for i in range(1, len(sea_matrix)):
        for j in range(1, len(sea_matrix[i])):
            if sea_matrix[i][j] == '#' and sea_matrix[i][j - 1] == '.' and sea_matrix[i - 1][j] == '.':
                cnt_rect += 1

    print(cnt_rect)

