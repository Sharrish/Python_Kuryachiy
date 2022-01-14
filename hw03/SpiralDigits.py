"""

Цифры по спирали
Ввести целые M и N, вывести последовательность 0 1 2 3 4 5 6 7 8 9 0 1 2 3 …
в виде спирально (по часовой стрелке, из верхнего левого угла)
заполненной таблицы N×M (N строк, M столбцов).
Не забываем про то, что M и N могут быть чётными, нечётными и неизвестно, какое больше.

Примеры
Входные данные
6,5

Результат работы
0 1 2 3 4 5
7 8 9 0 1 6
6 7 8 9 2 7
5 6 5 4 3 8
4 3 2 1 0 9

"""



def next_direction(i: int, j: int, direction: int,
                   lim_left: int, lim_right: int, lim_down: int, lim_up: int):

    if direction == 'left':
        if j == lim_left:
            i -= 1
            direction = 'up'
            lim_left += 1
        else:
            j -= 1

    elif direction == 'right':
        if j == lim_right:
            i += 1
            direction = 'down'
            lim_right -= 1;
        else:
            j += 1

    elif direction == 'down':
        if i == lim_down:
            j -= 1
            direction = 'left'
            lim_down -= 1;
        else:
            i += 1

    elif direction == 'up':
        if i == lim_up:
            j += 1
            direction = 'right'
            lim_up += 1;
        else:
            i -= 1

    return (i, j, direction, lim_left, lim_right, lim_down, lim_up)


if __name__ == '__main__':
    m, n = eval(input())
    spiral = [[0] * m for i in range(n)]
    cnt = 0
    i, j = 0, 0
    direction = 'right'
    lim_left, lim_right, lim_down, lim_up = 0, m - 1, n - 1, 1
    while cnt < n * m:
        spiral[i][j] = cnt % 10
        cnt += 1
        i, j, direction, lim_left, lim_right, lim_down, lim_up = next_direction(i, j, direction,
                                                                                lim_left, lim_right, lim_down, lim_up)

    for row in spiral:
        print(*row)