"""

Строка с делением
Написать класс DivStr, унаследованный от str, который поддерживал бы операцию деления
«//» и остатка от деления «%». Деление на N должно возвращать список из N подстрок
одинаковой наибольшей длины, на которые можно разделить исходную строку, а остаток — оставшуюся
концевую подстроку меньшей длины (возможно, пустую). Дополнительное требование: все пользовательские
(не начинающиеся на "__") методы str, которые возвращают строку, должны возвращать экземпляр DivStr.
Это же требование распространяется на методы __getitem__, __add__, __radd__, __mul__ и __rmul__. См.
советы и комментарии в полном условии задачи.

Примеры
Входные данные
a = DivStr("XcDfQWEasdERTdfgRTY")
print(* a // 4)
print(a % 4)
print(* a % 10 // 3)
print(a.lower() % 3)
print(* a[1:7] // 3)

Результат работы
XcDf QWEa sdER Tdfg
RTY
ERT dfg RTY
y
cD fQ WE


"""


class DivStr(str):
    def __mod__(self, N):
        return self[len(self) - len(self) % N:]

    def __floordiv__(self, N):
        d = len(self) // N
        return [self[i * d: (i + 1) * d] for i in range(N)]

    def __add__(self, other):
        return DivStr(super().__add__(other))

    def __radd__(self, other):
        return DivStr(super().__add__(other))

    def __mul__(self, other):
        return DivStr(super().__mul__(other))

    def __rmul__(self, other):
        return DivStr(super().__mul__(other))

    def __getitem__(self, item):
        return DivStr(super().__str__()[item])

    def center(self, *args, **kwargs):
        return DivStr(super().__str__().center(*args, **kwargs))

    def ljust(self, *args, **kwargs):
        return DivStr(super().__str__().ljust(*args, **kwargs))

    def rjust(self, *args, **kwargs):
        return DivStr(super().__str__().rjust(*args, **kwargs))

    def count(self, *args, **kwargs):
        return super().__str__().count(*args, **kwargs)

    def lower(self):
        return DivStr(super().__str__().lower())

    def capitalize(self):
        return DivStr(super().__str__().capitalize())

    def casefold(self, *args, **kwargs):
        return DivStr(self.__str__().casefold(*args, **kwargs))

    def lower(self):
        return DivStr(self.__str__().lower())

    def lstrip(self, *args, **kwargs):
        return DivStr(self.__str__().lstrip(*args, **kwargs))

    def rstrip(self, *args, **kwargs):
        return DivStr(super().__str__().rstrip(*args, **kwargs))

    def strip(self, *args):
        return DivStr(super().__str__().strip(*args))

    def swapcase(self):
        return DivStr(super().__str__().swapcase())

    def title(self):
        return DivStr(super().__str__().title())

    def upper(self):
        return DivStr(super().__str__().upper())

    def removeprefix(self, *args, **kwargs):
        return DivStr(super().__str__().removeprefix(*args, **kwargs))

    def removesuffix(self, *args, **kwargs):
        return DivStr(super().__str__().removesuffix(*args, **kwargs))

    def join(self, *args, **kwargs):
        return DivStr(super().__str__().join(*args, **kwargs))

    def replace(self, *args, **kwargs):
        return DivStr(super().__str__().replace(*args, **kwargs))