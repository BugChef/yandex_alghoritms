n = int(input())

res = {}
max_count = 0
result = []
for _ in range(n):
    word = input()
    if word not in res:
        res[word] = 1
    else:
        res[word] += 1

    if res[word] > max_count:
        max_count = res[word]
        result = [word]
    elif res[word] == max_count:
        result.append(word)
result.sort()
print(result[0])
