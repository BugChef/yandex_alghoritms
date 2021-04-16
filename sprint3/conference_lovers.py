import sys
from functools import cmp_to_key

n = int(sys.stdin.readline())
ids = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())

dict = {}
for id in ids:
    if dict.get(id) is None:
        dict[id] = 1
    else:
        dict[id] += 1


def compare(key_value1, key_value2):
    key1 = key_value1[0]
    value1 = key_value1[1]

    key2 = key_value2[0]
    value2 = key_value2[1]

    if value1 == value2:
        return key1 - key2
    else:
        return value2 - value1

dict = sorted(dict.items(), key=cmp_to_key(compare))[:k]
dict = [str(x[0]) for x in dict]
print(' '.join(dict))