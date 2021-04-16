a = int(input())
m = int(input())
s = input()
t = int(input())

hsh = ord(s[0]) if len(s) > 0 else 0
for i in range(1, len(s)):
    hsh = hsh * a + ord(s[i])

for _ in range(t):
    l, r = map(int, input().split())
    result_hash = hsh

    while l != 0:
        l -= 1
        power = len(s) - l
        l_hash = ord(s[l]) * (a ** power)
        result_hash -= l_hash

    while r < len(s) - 1:
        r += 1
        power = len(s) - r
        r_hash = ord(s[r]) * (a ** power)
        result_hash -= r_hash

    print(result_hash % m)