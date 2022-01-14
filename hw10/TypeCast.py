"""

Приведение типов
Написать параметрический декоратор cast(тип), который пытается преобразовать результат декорируемой функции к
заданному типу. Исключения проверять не надо, но надо пользоваться @wraps.

Примеры
Входные данные
@cast(int)
def fun(a, b):
    return a * 2 + b
print(fun(12, 34) * 2)
print(fun("12", "34") * 2)
print(fun(12.765, 34.654) * 2)

Результат работы
116
242468
120

"""


from functools import wraps


def cast(type):
    def wrap(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            return type(f(*args, **kwargs))
        return wrapper
    return wrap