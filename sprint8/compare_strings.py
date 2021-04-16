first = list(input())
second = list(input())

new_first = ""
new_second = ""

for i in range(len(first)):
    if ord(first[i]) % 2 == 0:
        new_first += first[i]

for i in range(len(second)):
    if ord(second[i]) % 2 == 0:
        new_second += second[i]

if new_first < new_second:
    print(-1)
elif new_first > new_second:
    print(1)
else:
    print(0)
