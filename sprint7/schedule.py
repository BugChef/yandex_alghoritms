n = int(input())
times = []
for _ in range(n):
    time1, time2 = [float(x) for x in input().split()]
    times.append((time2, time1))

times.sort()

result = []
for time2, time1 in times:
    if not result:
        result.append((time1, time2))
        continue
    last1, last2 = result[-1]
    if time1 >= last2:
        result.append((time1, time2))

print(len(result))
for r in result:
    r1 = r[0] if not r[0].is_integer() else int(r[0])
    r2 = r[1] if not r[1].is_integer() else int(r[1])
    print(r1, r2)
