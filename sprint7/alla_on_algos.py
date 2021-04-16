# https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/
import sys

summ = int(input())
k = int(input())
nom = list(map(int, input().split()))
nom.sort(reverse=True)


def min_nom(nom, summ):
    table = [sys.maxsize for _ in range(summ + 1)]
    table[0] = 0

    for i in range(1, summ + 1):
        for nm in nom:
            if nm <= i:
                sub_res = table[i - nm]
                if sub_res != sys.maxsize and sub_res + 1 < table[i]:
                    table[i] = sub_res + 1

    if table[summ] == sys.maxsize:
        return -1

    return table[summ]


print(min_nom(nom, summ))
