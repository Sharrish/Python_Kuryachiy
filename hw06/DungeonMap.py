"""

Карта подземелья
Вводится карта проходимых в обе стороны тоннелей подземлья в виде строк, содержащих
разделённые пробелом названия двух пещер, которые соединяет соответствующий тоннель.
Две последние строки не содержат пробелов — это название входа в подземелье и название выхода.
Вывести "YES", если из входа можно попасть в выход, и "NO" в противном случае.
Пары могут повторяться или содержать одинаковые слова.

Примеры
Входные данные
markers jumping
jumping guinea
skiing pre
markers gauge
skiing mpeg
solar jackson
skiing solar
guinea gauge
mpeg honor
pre honor
guinea gauge
pre mpeg
markers guinea
markers gauge
honor mpeg
markers jumping
skiing
jumping

Результат работы
NO

"""


from collections import deque


def bfs(start_v, end_v, edges):
    used = set()
    q = deque()
    q.append(start_v)
    while len(q):
        v = q.popleft()
        if v not in used:
            for u in edges[v]:
                q.append(u)
            used.add(v)
    return end_v in used


if __name__ == '__main__':
    edges = {}
    s = input()
    while ' ' in s:
        v1, v2 = s.split()
        if v1 not in edges.keys():
            edges[v1] = set()
        if v2 not in edges.keys():
            edges[v2] = set()
        edges[v1].add(v2)
        edges[v2].add(v1)
        s = input()
    start_v = s
    end_v = input()
    if bfs(start_v, end_v, edges):
        print("YES")
    else:
        print("NO")
