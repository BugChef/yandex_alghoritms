import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

smth_changed = False
for i in range(n - 1):
    was_changed = False
    for j in range(n - i - 1):
        if lst[j] > lst[j + 1]:
            buff = lst[j]
            lst[j] = lst[j + 1]
            lst[j + 1] = buff
            was_changed = True
            smth_changed = True
    if was_changed:
        print(' '.join(map(str, lst)))

if not smth_changed:
    print(' '.join(map(str, lst)))