"""

Слияние
Написать генератор-функцию joinseq(seq0, seq1, …), принимающую на вход произвольное количество
(возможно, бесконечных) числовых последовательностей. Порождаемый ею генератор должен всякий раз
возвращать наименьший из начальных элементов этих последовательностей. Если таких несколько,
используется самый первый. Если последовательность закончилась, она больше не учитывается.
Итератор завершается, когда все последовательности иссякли. Условие: использовать обработку
исключений в этой задаче нельзя.

Примеры
Входные данные
print("".join(joinseq("abs", "qr", "azt")))

Результат работы
aabqrszt

"""


def joinseq(*args):
    list_seqs = [list(seq) for seq in args]
    cnt = 0
    for seq in list_seqs:
        cnt += len(seq)
    while cnt:
        # print(list_seqs)
        flag = False
        k = -1
        mn = -1
        for i, seq in enumerate(list_seqs):
            if len(seq) and (not flag or mn > seq[0]):
                flag = True
                k = i
                mn = seq[0]
        yield mn
        list_seqs[k].remove(mn)
        cnt -= 1


# if __name__ == '__main__':
#     print("".join(joinseq("abs", "qr", "azt")))
