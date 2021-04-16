import sys

n = int(sys.stdin.readline().strip())
factors = list(map(int, sys.stdin.readline().strip().split()))
factors.sort(reverse=True)

m = int(sys.stdin.readline().strip())
sizes = list(map(int, sys.stdin.readline().strip().split()))
sizes.sort(reverse=True)

result = 0
while len(factors) != 0 and len(sizes) != 0:
    if sizes[-1] >= factors[-1]:
        result += 1
        factors.pop()
    sizes.pop()

print(result)
