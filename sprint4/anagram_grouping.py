n = int(input())
strings = input().strip().split()

indexes_by_string = {}
for i in range(len(strings)):
    string = strings[i]
    sorted_string = str(sorted(string))
    if sorted_string in indexes_by_string:
        indexes_by_string[sorted_string].append(i)
    else:
        indexes_by_string[sorted_string] = [i]

for indexes in indexes_by_string.values():
    print(' '.join(map(str, indexes)))