import sys

n = int(sys.stdin.readline().strip())
colors = list(map(int, sys.stdin.readline().split()))
colors.sort()

print(' '.join(map(str, colors)))
