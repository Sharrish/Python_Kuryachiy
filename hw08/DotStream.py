"""

Источник точек
Написать класс Dots, генерирующий заданное количество точек на заданном отрезке. Свойства класса:
При создании объекта d типа Dots задаются вещественные границы отрезка.
d[n] — последовательность из n равноудалённых точек от начала до конца отрезка (включая конец).
d[i:n] — i-я точка такой последовательности. d[i:j:n] — последовательность точек, начиная с i-той и
заканчивая j-1-й точкой исходной последовательности. Выход за границы отрезка означает экстраполяцию (см. пример).

Примеры
Входные данные
a = Dots(0,40)
print(*a[5])
print(a[0:5])
print(a[2:5])
print(a[4:5])
print(a[7:5])
print(a[-7:5])
print(*a[1:3:5])
print(*a[:3:5])
print(*a[2::5])
print(*a[::5])
print(*a[-2:6:5])

Результат работы
0.0 10.0 20.0 30.0 40.0
0.0
20.0
40.0
70.0
-70.0
10.0 20.0
0.0 10.0 20.0
20.0 30.0 40.0
0.0 10.0 20.0 30.0 40.0
-20.0 -10.0 0.0 10.0 20.0 30.0 40.0 50.0

"""




class Dots:
    def __init__(self, a, b):
        self.left = a
        self.right = b

    @staticmethod
    def get_step(left, right, sz):
        return (right - left) / sz

    def __getitem__(self, key):
        if not isinstance(key, slice):
            step = self.get_step(self.left, self.right, key - 1)
            return (self.left + i * step for i in range(key))
        elif not key.step is None:
            step = self.get_step(self.left, self.right, key.step - 1)
            start = 0
            end = key.step
            if key.start:
                start = key.start
            if key.stop:
                end = key.stop
            return (self.left + i * step for i in range(start, end))
        else:
            step = self.get_step(self.left, self.right, key.stop - 1)
            if key.start:
                return self.left + key.start * step
            return self.left


# a = Dots(0,40)
# print(*a[5])
# print(a[0:5])
# print(a[2:5])
# print(a[4:5])
# print(a[7:5])
# print(a[-7:5])
# print(*a[1:3:5])
# print(*a[:3:5])
# print(*a[2::5])
# print(*a[::5])
# print(*a[-2:6:5])
