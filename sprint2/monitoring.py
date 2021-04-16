"""
Алла получила задание, связанное с мониторингом работы различных серверов.
Требуется понять, сколько времени обрабатываются определённые запросы на конкретных серверах.
Эту информацию нужно хранить в матрице, где номер столбца соответствуют идентификатору запроса,
а номер строки — идентификатору сервера. Алла перепутала строки и столбцы местами.
С каждым бывает. Помогите ей исправить баг.
Есть матрица размера m × n. Нужно написать функцию, которая её транспонирует.
Транспонированная матрица получается из исходной заменой строк на столбцы.
"""

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
matrix = []

for i in range(n):
    line = sys.stdin.readline().strip().split()
    matrix.append(line)

for i in range(m):
    string = ''
    for j in range(n):
        string += matrix[j][i]
        if j != n:
            string += ' '
    print(string)
