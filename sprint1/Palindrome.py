"""
А теперь помогите Васе понять, будет ли фраза палиндромом.
Учитываются только буквы и цифры, заглавные и строчные буквы считаются одинаковыми.
Решение должно работать за O(N), где N - длина строки на входе.
"""

import sys
import string

inp = sys.stdin.readline().strip().split()
inp = "".join(inp).lower()

s = set(string.ascii_lowercase)
n = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

result = ""
for char in list(inp):
    if char in s or char in n:
        result += char

rev = result[::-1]
print("True" if result == rev else "False")