import sys

n, k = [int(x) for x in sys.stdin.readline().split()]
houses = list(map(int, sys.stdin.readline().strip().split()))
houses.sort()

result = 0
sm = 0
for house in houses:
    if sm + house > k:
        break
    else:
        sm += house

    result += 1

    if result == n:
        break

print(result)