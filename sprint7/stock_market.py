n = int(input())
numbers = list(map(int, input().split()))

profit = 0

for i in range(1, n):
    dif = numbers[i] - numbers[i - 1]
    if dif > 0:
        profit += dif

print(profit)
