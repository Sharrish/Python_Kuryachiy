"""

https://uneex.org/LecturesCMC/PythonIntro2021/Homework_SemClass

Примеры
Входные данные
@Lock.locked
class A(str):
    pass


a, b = A("a"), A("b")
a.lock = "S"       # Регистрация на семафор S
b.lock = "S"       # Регистрация на семафор S
print(a, a.lock)   # Успешный захват семафора S
print(a, a.lock)   # Семафор S уже захвачен нами
print(b, b.lock)   # Неуспешный захват семафора S
del a.lock         # Освобождение семафора S
print(b, b.lock)   # Успешный захват семафора S
b.lock = "T"       # Регистрация на семафор T, освобождает предыдущий семафор
print(b, b.lock)   # Успешный захват семафора T
del b              # Удаление объекта-носителя освобождает семафор
a.lock = "T"       # Регистрация на семафор T, освобождает предыдущий семафор
print(a, a.lock)   # Успешный захват семафора T

Результат работы
a S
a S
b None
b S
b T
a T

"""



class Lock:

    def __init__(self):
        self.state = {}

    @staticmethod
    def locked(cls):
        cls.lock = Semaphore()
        cls._lock = None

        def del2(self):
            del self.lock

            if "__del__" in dir(super(type(self), self)):
                super(type(self), self).__del__(self)

        cls.__del__ = del2
        return cls


class Semaphore:
    def __init__(self):
        self.resources = Lock()

    def __get__(self, obj, cls):
        lock_cls = self.resources.state.get(obj._lock)
        if lock_cls is None:
            self.resources.state[obj._lock] = id(obj)
            return obj._lock
        else:
            if lock_cls == id(obj):
                return obj._lock
            else:
                return None

    def __set__(self, obj, val):
        if self.resources.state.get(obj._lock) == id(obj):
            self.resources.state[obj._lock] = None
        obj._lock = val

    def __delete__(self, obj):
        if self.resources.state.get(obj._lock) == id(obj):
            self.resources.state[obj._lock] = None
        obj._lock = None