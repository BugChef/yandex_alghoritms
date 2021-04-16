"""
Владелец казино хочет поставить себе новый игровой автомат:
когда дёргаешь за ручку, в автомате генерируются три случайных числа.
Если все три числа одной чётности, то игрок выигрывает.
Напишите программу, которая по трём числам определяет, выиграл игрок или нет.
"""
import sys

line = sys.stdin.readline().strip()
a, b, c = line.split()
a = int(a)
b = int(b)
c = int(c)


def is_even(number) -> bool:
    return number % 2 == 0


a = is_even(a)
b = is_even(b)
c = is_even(c)

win = a and b and c or not (a or b or c)
print("WIN" if win else "FAIL")