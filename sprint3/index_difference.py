import sys

n = int(sys.stdin.readline())
areas = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())

difs = []
for i in range(n):
    first = areas[i]
    for j in range(i, n):
        if i == j:
            continue

        second = areas[j]
        dif = abs(first - second)
        difs.append(dif)

print(1)