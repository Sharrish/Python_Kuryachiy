"""

В далёкой галактике
Ввести построчно четвёрки вида «число число число слово», где первые
три числа — это координаты галактики по имени «слово» (некоторые галактики могут называться одинаково,
но координаты у всех разные). Последняя строка ввода не содержит пробелов и не учитывается.
Вывести в алфавитном порядке имена любых двух наиболее удалённых друг от друга галактик.
Считается, что одинаковых расстояний в списке нет.

Примеры
Входные данные
35.764 -797.636 -770.320 almost
88.213 -61.688 778.457 gene
-322.270 -248.555 -812.730 trend
721.262 630.355 968.287 dow
-895.519 -970.173 97.282 non
-561.036 -350.840 -723.149 disco
-151.546 -900.962 -658.862 bidder
-716.197 478.576 -695.843 hawaii
-744.664 -173.034 -11.211 sad
-999.968 990.467 650.551 erik
.

Результат работы
almost erik

"""


import math


def dist(x1, y1, z1, x2, y2, z2):
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) + (z1 - z2) * (z1 - z2)


if __name__ == '__main__':
    galaxy_name = []
    galaxy_pos = []
    s = input()
    while ' ' in s:
        x, y, z, name = s.split(' ')
        x, y, z = float(x), float(y), float(z)
        galaxy_name.append(name)
        galaxy_pos.append((x, y, z))
        s = input()
    min_dist = -math.inf
    ans1 = str()
    ans2 = str()
    for i in range(len(galaxy_pos)):
        for j in range(i + 1, len(galaxy_pos)):
            tmp_dist = dist(*galaxy_pos[i], *galaxy_pos[j])
            if (tmp_dist > min_dist):
                min_dist = tmp_dist
                ans1 = galaxy_name[i]
                ans2 = galaxy_name[j]
    if ans1 > ans2:
        ans1, ans2 = ans2, ans1
    print(ans1, ans2)