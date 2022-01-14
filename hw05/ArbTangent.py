"""
Тангенс
Ввести числа: рациональное A — угол из диапазона от 1 до 99 градов (десятичных градусов),
и натуральное 4 ⩽ E ⩽ 1000 — точность вычисления (в терминах контекста вычислений модуля Decimal — поле perc).
Вычислить значение тангенса с указанной точностью. Число Пи (если оно вам понадобится) тоже надо вычислять!

Примеры

Входные данные
50
7

Результат работы
1.000000
"""

import decimal
from decimal import Decimal
import math


MEMBERS_NUM = 177
PRECISION_NUM = 2017


def get_pi_value():
    """ Алгоритм Чудновского для получения числа пи. """
    my_pi = Decimal(0)
    for k in range(MEMBERS_NUM):
        my_pi += (Decimal(-1) ** k) * Decimal(math.factorial(6 * k)) * (13591409 + 545140134 * k)\
                 / ((math.factorial(k) ** 3) * math.factorial(3 * k) * (640320 ** (3 * k)))
    my_pi = (Decimal(640320).sqrt() ** 3) / 12 / my_pi
    return my_pi


def sin(x):
    my_sin = 0
    for k in range(MEMBERS_NUM):
        my_sin += (Decimal((-1) ** k) * Decimal(x ** (2 * k + 1))) / Decimal(math.factorial(2 * k + 1))
    return my_sin


def cos(x):
    my_cos = 0
    for k in range(MEMBERS_NUM):
        my_cos += (Decimal((-1) ** k) * Decimal(x ** (2 * k))) / Decimal(math.factorial(2 * k))
    return my_cos


def grad_to_radian(alpha):
    my_pi = get_pi_value()
    return Decimal(my_pi) * Decimal(alpha) / Decimal(200)


if __name__ == '__main__':

    alpha = float(input())
    precision = int(input())
    decimal.getcontext().prec = PRECISION_NUM
    x = grad_to_radian(alpha)
    ans = sin(x) / cos(x)
    print(decimal.Context(prec = precision).create_decimal(ans))