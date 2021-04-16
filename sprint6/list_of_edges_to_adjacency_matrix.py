n, m = [int(x) for x in input().split()]

mtrx = [['0'] * n for _ in range(n)]
for _ in range(m):
    vrtx1, vrtx2 = [int(x) for x in input().split()]
    mtrx[vrtx1 - 1][vrtx2 - 1] = '1'

for i in range(n):
    res = ' '.join(mtrx[i])
    print(res)