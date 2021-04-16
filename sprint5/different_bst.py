import sys
from math import factorial as f


def catalan(n):
    cat = f(2 * n) / (f(n) * f(n + 1))
    return int(cat)


n = int(sys.stdin.readline().strip())
print(catalan(n))
