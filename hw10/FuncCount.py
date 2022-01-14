"""

Счётчик вызовов
Написать декоратор counter, который заводит внутри объекта-функции метод counter().
Этот метод возвращает, сколько раз эта функция была вызвана. Использовать @wraps.
Дополнительное требование: никаких других глобальных объектов (кроме counter и wraps).

Примеры
Входные данные
@counter
def fun(a, b):
    return a * 1 + b

print(fun.counter())
res = sum(fun(i, i + 1) for i in range(5))
print(fun.counter(), res)

Результат работы
0
5 25

"""

from functools import wraps

def counter(f):
  f.k = 0
  f.counter = lambda: f.k

  @wraps(f)
  def wrap(*args, **kwargs):
    f.k += 1
    return f(*args, **kwargs)

  return wrap