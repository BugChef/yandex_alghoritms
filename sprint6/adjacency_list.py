n, m = [int(x) for x in input().split()]

mtrx = [[] for _ in range(n)]

for _ in range(m):
    u, v = [int(x) for x in input().split()]
    mtrx[u - 1].append(v)

for i in range(n):
    res = str(len(mtrx[i]))
    if res != '0':
        res += ' '
        res += ' '.join(map(str, mtrx[i]))
    print(res)