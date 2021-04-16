import sys

s = list(sys.stdin.readline().strip())
t = list(sys.stdin.readline().strip())

it = iter(t)
result = all(x in it for x in s)

print(result)

