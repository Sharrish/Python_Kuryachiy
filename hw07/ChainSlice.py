"""

Режем лазанью
Написать Генератор-функцию chainslice(begin, end, seq0, seq1, …),
которая принимает не менее трёх параметров: два целых числа и не менее одной последовательности.
 Рассмотрим последовательность seq, образованную всеми элементами seq0, затем — всеми элементами
 seq1, и т. д. Вернуть эта функция должна итератор, пробегающий элементы этой последовательности
 seq с №begin до №end-1 включительно.

Примеры
Входные данные
print(*(chainslice(17, 33, range(7),  range(8),  range(6),  range(9),  range(5))))

Результат работы
2 3 4 5 0 1 2 3 4 5 6 7 8 0 1 2

"""



def chainslice(begin, end, *args):
    cnt = 0
    slice = []
    for seq in args:
        for i in seq:
            if begin <= cnt and cnt < end:
                slice.append(i)
            elif cnt >= end:
                break
            cnt += 1
    return iter(slice)


# if __name__ == '__main__':
#     print(*(chainslice(17, 33, range(7),  range(8),  range(6),  range(9),  range(5))))