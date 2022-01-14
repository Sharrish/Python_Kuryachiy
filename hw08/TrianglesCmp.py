"""

Сравниваем треугольники
Написать класс Triangle, моделирующий треугольник:

объект tri типа Triangle создаётся из трёх вещественных чисел — сторон треугольника
tri пуст, если не выполняется строгое неравенство треугольника или хотя бы одна из сторон не положительна
abs(tri) — площадь треугольника (0, если tri пуст)
два объекта tri1 и tri2 типа Triangle равны, только если попарно равны их стороны (в некотором порядке)
сравнение на неравенство двух объектов типа Triangle есть результат сравнения их площадей
в частности A ⩽ B истинно, если их площади равны
строковое представление: a:b:c, где a, b и c — это стороны треугольника в порядке их задания
Примеры
Входные данные
tri = Triangle(3, 4, 5), Triangle(5, 4, 3), Triangle(7, 1, 1), Triangle(5, 5, 5), Tria  ngle(7, 4, 4)
      for a, b in zip(tri[:-1], tri[1:]):
      print(a if a else b)
      print(f"{a}={abs(a):.2f} {b}={abs(b):.2f}")
      print(a == b)
      print(a >= b)
      print(a < b)
Результат работы
3.0:4.0:5.0
      3.0:4.0:5.0=6.00 5.0:4.0:3.0=6.00
      True
      True
      False
      5.0:4.0:3.0
      5.0:4.0:3.0=6.00 7.0:1.0:1.0=0.00
      False
      True
      False
      5.0:5.0:5.0
      7.0:1.0:1.0=0.00 5.0:5.0:5.0=10.83
      False
      False
      True
      5.0:5.0:5.0
      5.0:5.0:5.0=10.83 7.0:4.0:4.0=6.78
      False
      True
      False

"""


class Triangle:
    def __init__(self, a: float, b: float, c: float):
        """ Объект tri типа Triangle создаётся из трёх вещественных чисел — сторон треугольника. """
        self.a, self.b, self.c  = float(a), float(b), float(c)

    def __bool__(self):
        a, b, c = self.a, self.b, self.c
        return ((a + b > c) and (a + c > b) and (b + c > a) and (a > 0) and (b > 0) and (c > 0))

    def __abs__(self):
        if not self.__bool__():
            return 0
        p = (self.a + self.b + self.c) / 2.0
        return (max(p * (p - self.a) * (p - self.b) * (p - self.c), 0.0)) ** 0.5

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __gt__(self, other):
        return abs(other) < abs(self)

    def __eq__(self, other):
        return abs(self) == abs(other)

    def __le__(self, other):
        return abs(self) <= abs(other)

    def __ge__(self, other):
        return abs(other) <= abs(self)

    def __str__(self):
        return '{}:{}:{}'.format(self.a, self.b, self.c)
