s = input()
n = int(input())
result = list(s)
for _ in range(n):
    line = input().split()
    insertion_str, pos = line[0], int(line[1])
    result.insert(pos, insertion_str)

print(result)
