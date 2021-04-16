n, m = list(map(int, input().split()))
flowers = []
for _ in range(n):
    line = [int(x) for x in list(input())]
    flowers.append(line)

field = [[0] * m for _ in range(n)]
field[n - 1][0] = flowers[n - 1][0]  # базовый случай

for i in range(n - 1, -1, -1):
    for j in range(m):
        left = 0 if j - 1 < 0 else field[i][j - 1]
        down = 0 if i + 1 > n - 1 else field[i + 1][j]
        mx = max(left, down)
        field[i][j] = mx + flowers[i][j]

print(field[0][m - 1])