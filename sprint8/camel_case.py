from collections import defaultdict

strings_by_pattern = defaultdict(list)
strings = []
n = int(input())
for _ in range(n):
    string = input()
    strings.append(string)
    ptrn = ""
    for c in list(string):
        if c.isupper():
            ptrn += c
            strings_by_pattern[ptrn].append(string)

for v in strings_by_pattern.values():
    v.sort()

m = int(input())
for _ in range(m):
    pattern = input()
    matched = strings_by_pattern[pattern]
    if len(pattern) == 0:
        strings.sort()
        for s in strings:
            print(s)
        continue
    if len(matched) == 0:
        print()
        continue
    for res in matched:
        print(res)
