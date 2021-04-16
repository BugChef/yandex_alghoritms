import sys
from functools import cmp_to_key

n = int(sys.stdin.readline())
numbers = sys.stdin.readline().split()

numbers = sorted(numbers, key=cmp_to_key(lambda i, j: -1 if j + i < i + j else 1))

print(''.join(numbers))