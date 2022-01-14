"""

Три квадрата
Ввести произвольную последовательность
(не обязательно кортеж) натуральных чисел, не превышающих 1000000.
Вывести, сколько среди них различных чисел, являющихся суммой трёх квадратов.
Пояснение. Входная последовательность должна обрабатываться так: seq = list(eval(input()))

Примеры
Входные данные
3, 4, 2, 9, 1, 5, 6, 7, 8, 3, 6
Результат работы
3

"""


from math import sqrt


if __name__ == '__main__':
    seq = set(eval(input()))
    st = set()
    mx = max(seq)
    sqrt_max_num1 = int(sqrt(mx))
    for i in range(1, sqrt_max_num1 + 1):
        sqrt_max_num2 = int(sqrt(mx - i * i))
        for j in range(i, sqrt_max_num2 + 1):
            sqrt_max_num3 = int(sqrt(mx - i * i - j * j))
            for k in range(j, sqrt_max_num3 + 1):
                st.add(i * i + j * j + k * k)
    ans = 0
    for i in seq:
        if i in st:
            ans += 1
    print(ans)
