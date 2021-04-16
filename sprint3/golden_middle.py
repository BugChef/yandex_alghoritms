import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
north = list(map(int, sys.stdin.readline().split()))
south = list(map(int, sys.stdin.readline().split()))


def median(arr):
    l = len(arr)
    if l % 2 == 0:
        mid = (l - 1) // 2
        return (arr[mid] + arr[mid + 1]) / 2
    else:
        return arr[l // 2]


al = north + south
al.sort()
med = median(al)
print(med)