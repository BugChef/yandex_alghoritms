M = int(input())
heaps_count = int(input())
heaps = []
for _ in range(heaps_count):
    c, m = [int(x) for x in input().split()]
    heaps.append((c, m))
heaps.sort(reverse=True)

mass_count = 0
price_count = 0

for c, m in heaps:
    if mass_count + m > M:
        mass_dif = M - mass_count
        price_count += c * mass_dif
        break
    else:
        price_count += c * m
        mass_count += m

print(price_count)
