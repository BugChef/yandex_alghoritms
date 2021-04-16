import sys

n = int(sys.stdin.readline().strip())
sides = list(map(int, sys.stdin.readline().split()))
sides.sort()

for i in range(n - 3, -1, -1):
    a = sides[i]
    b = sides[i + 1]
    c = sides[i + 2]

    if c < a + b:
        print(a + b + c)
        break
