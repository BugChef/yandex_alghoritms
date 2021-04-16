"""
Тимофей спросил у студента Саши, умеет ли тот работать с числами в двоичной системе счисления.
Он ответил, что проходил это на одной из первых лекций по информатике.
Тимофей предложил Саше решить задачку.
Два числа записаны в двоичной системе счисления.
Нужно вывести их сумму, также в двоичной системе.
Встроенную в язык программирования возможность сложения двоичных чисел применять нельзя.
Решение должно работать за O(N) , где N - количество разрядов максимального числа на входе.
"""
import sys

first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()

max_len = max(len(first), len(second))

first = first.zfill(max_len)
second = second.zfill(max_len)

result = ''
carry = 0
for i in range(max_len - 1, -1, -1):
    r = carry
    r += 1 if first[i] == '1' else 0
    r += 1 if second[i] == '1' else 0
    result = ('1' if r % 2 == 1 else '0') + result
    carry = 0 if r < 2 else 1

if carry != 0: result = '1' + result
print(result.zfill(max_len))