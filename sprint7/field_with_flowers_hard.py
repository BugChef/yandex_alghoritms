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

i = 0
j = m - 1
path = ''
for _ in range(n + m - 2):
    left = -1 if j - 1 < 0 else field[i][j - 1]
    down = -1 if i + 1 > n - 1 else field[i + 1][j]

    if left == -1 :
        if down == -1:
            break
        i += 1
        path = 'U' + path
    elif down == -1:
        if left == -1:
            break
        j -= 1
        path = 'R' + path
    elif down > left:
        i += 1
        path = 'U' + path
    else:
        j -= 1
        path = 'R' + path

print(field[0][m - 1])
print(path)
