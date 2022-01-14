"""

Счётчик экземпляров
Написать класс WeAre, экземпляры которого содержат поле count.
В этом поле хранится количество существующих экземпляров этого класса.

Примеры
Входные данные
a = WeAre()
print(a.count)
b, c = WeAre(), WeAre(),
print(a.count, b.count, c.count)
del b
print(a.count)

Результат работы
1
3 3 3
2


"""


class WeAre:
    """
    Класс WeAre, экземпляры которого содержат поле count.
    В этом поле хранится количество существующих экземпляров этого класса.
    """
    count = 0

    def __init__(self):
        WeAre.count += 1

    def __del__(self):
        WeAre.count -= 1


# if __name__ == '__main__':
#     a = WeAre()
#     print(a.count)
#     b, c = WeAre(), WeAre(),
#     print(a.count, b.count, c.count)
#     del b
#     print(a.count)