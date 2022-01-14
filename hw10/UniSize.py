"""
Унисайз
Написать декоратор класса под названием sizer, который будет добавлять в класс поле size.
При обращении к этому полю возвращается len() объекта, если объёкт имеет длину, иначе же abs()
объекта, если от него вычисляется модуль, и 0 в противном случае.

Примеры
Входные данные
@sizer
class S(str):
    pass

@sizer
class N(complex):
    pass

@sizer
class E(Exception):
    pass

for obj in S("QWER"), N(3+4j), E("Exceptions know no lengths!"):
    print(obj, obj.size)

Результат работы
QWER 4
(3+4j) 5.0
Exceptions know no lengths! 0

"""

def sizer(class_name):
    def wr(*args, **kwargs):
        class_name.size = MyClass()
        return class_name(*args, **kwargs)

    class MyClass:
        def __get__(self, obj, cls):
            try:
                self.size = len(obj)
            except:
                try:
                    self.size = abs(obj)
                except:
                    self.size = 0

            return self.size
    return wr