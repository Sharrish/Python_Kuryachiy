"""

Вращающееся число
(Жак Арсак. Программирование игр и головоломок.)
Для заданной цифры k найти такое минимальное целое неотрицательное число, оканчивающееся на k,
что, умножая его на k, мы получим новое число, полученное из предыдущего вычеркиванием цифры k на конце и
приписыванием ее в начале. Строки/кортежи и иные последовательности не использовать.

Примеры
Входные данные
4

Результат работы
102564

"""


def reverse_num(num: int) -> int:
    num_reversed = 0
    while num:
        num_reversed *= 10
        num_reversed += num % 10
        num //= 10
    return num_reversed


if __name__ == '__main__':
    k = int(input())
    if k in (0, 1):
        print(k)
    else:
        last_num = (k * k) % 10
        add = (k * k) // 10
        ans = k
        while last_num != 1 or add > 0:
            ans *= 10
            ans += last_num
            last_num = last_num * k + add
            if last_num >= 10:
                add = last_num // 10
                last_num %= 10
            else:
                add = 0
        ans *= 10
        ans += 1
        print(reverse_num(ans))