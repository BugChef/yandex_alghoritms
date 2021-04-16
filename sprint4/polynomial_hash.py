import sys

a = int(sys.stdin.readline())
m = int(sys.stdin.readline())
string = sys.stdin.readline().strip()


def hsh(string):
    lth = len(string)
    sm = ord(string[0]) if lth > 0 else 0
    for i in range(1, lth):
        sm = sm * a + ord(string[i])
        sm = sm % m
    return sm


print(hsh(string))
