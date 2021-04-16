n, k = list(map(int, input().split()))
module = 10 ** 9 + 7

temp = 0
res = [1]

for i in range(1, n):
    s = i - k - 1
    e = i - 1
    if s >= 0:
        temp -= res[s]
    temp += res[e]
    res.append(temp)

print(res[n - 1] % module)
