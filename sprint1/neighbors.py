"""
Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его соседей.
Соседним считается элемент, находящийся от текущего на одну ячейку влево, вправо, вверх или вниз.
Диагональные элементы соседними не считаются.
Например, в матрице A:
                        [[1, 2, 3],
                        [0, 2, 6],
                        [7, 4, 1],
                        [2, 7, 0]]
соседними элементами для (0, 0) будут 2 и 0 А для (2, 1) — 1, 2, 7, 7.
"""

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
matrix = []

for i in range(n):
    line = sys.stdin.readline().strip()
    line = [int(x) for x in line.split()]
    matrix.append(line)

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

array = []
if x < n-1:
    array.append(matrix[x+1][y])
if x > 0:
    array.append(matrix[x - 1][y])
if y < m-1:
    array.append(matrix[x][y + 1])
if y > 0:
    array.append(matrix[x][y - 1])

array.sort()
print(' '.join(map(str, array)))
