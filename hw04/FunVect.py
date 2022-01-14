"""

Вектор функций
Написать функцию superposition(funmod, funseq), которая принимает два параметра — функцию funmod()
от одного переменного, и последовательность funseq[] функций от одного переменного. superposition()
 возвращает также список функций funres[],
 каждая из которых представляет собой суперпозицию вида funres[i] ::== funmod(funseq[i])

Примеры
Входные данные
from math import *
F = superposition(abs, (sin, cos))
print(F[0](-1), F[1](-1), F[0](2), F[1](2))

Результат работы
0.8414709848078965 0.5403023058681398 0.9092974268256817 0.4161468365471424

"""



def superposition(funmod, funseq):
    """
    :param funmod: функция от одного переменного.
    :param funseq: последовательность функций от одного переменного.
    :return: возвращает список функций funres[], каждая из которых представляет собой суперпозицию вида
                funres[i] == funmod(funseq[i])
    """
    funres = []
    for fun in funseq:
        funres.append(lambda x, f=fun: funmod(f(x)))
    return funres


# if __name__ == '__main__':
#     from math import *
#     F = superposition(abs, (sin, cos))
#     print(F[0](-1), F[1](-1), F[0](2), F[1](2))
