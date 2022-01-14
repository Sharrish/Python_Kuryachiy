"""

Случайные диапазоны
Написать генератор-функцию randomes(seq), которой передаётся на вход последовательность пар
seq — диапазоны для функции random.randint(). На выходе должен быть генератор, который
бесконечно возвращает случайные числа по одному из каждого диапазона. Сами пары тоже могут оказаться итераторами.

Примеры
Входные данные
for e in zip(randomes([(1, 3), (100, 200), (-10, 10)]), range(7)):
    print(e[0])

Результат работы
1
123
-3
3
177
7
2

"""



import random


def randomes(seq):
    segments = []
    for i in seq:
        segment = [j for j in i]
        segments.append(segment)
        yield random.randint(segment[0], segment[1])
    while True:
        for left, right in segments:
            yield random.randint(left, right)


# if __name__ == '__main__':
#     for e in zip(randomes([(1, 3), (100, 200), (-10, 10)]), range(7)):
#         print(e[0])