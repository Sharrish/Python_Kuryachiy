"""
Прочти это вслух
Написать генератор-функцию LookSay() цифр последовательности Конвея «Look and Say».

Примеры
Входные данные
for i, l in enumerate(LookSay()):
    print(f"{i}: {l}")
    if i > 10:
        break

Результат работы
0: 1
1: 1
2: 1
3: 2
4: 1
5: 1
6: 2
7: 1
8: 1
9: 1
10: 1
11: 1

"""


from itertools import groupby


def LookSay():
    prev_number = 1
    yield prev_number
    prev_number = str(prev_number)
    while True:
        next_number = ""
        for digit, seq in groupby(prev_number):
            next_number += str(len(list(seq))) + str(digit)
        prev_number = next_number
        for i in prev_number:
            yield int(i)


# if __name__ == '__main__':
#     for i, l in enumerate(LookSay()):
#         print(f"{i}: {l}")
#         if i > 10:
#             break
