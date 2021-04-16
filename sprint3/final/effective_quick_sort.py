"""
ID = 46915431
"""


def border_index(array, start, end):
    pivot = array[(start + end) // 2]
    low = start
    high = end

    while low < high:
        while low < high and array[low] < pivot:
            low = low + 1

        while low < high and array[high] > pivot:
            high = high - 1

        if low < high:
            array[low], array[high] = array[high], array[low]

    return high


def effective_quicksort(array, start, end):
    if end - start < 1:
        return

    border_id = border_index(array, start, end)
    effective_quicksort(array, start, border_id - 1)
    effective_quicksort(array, border_id + 1, end)


n = int(input())
members = []
for _ in range(n):
    params = input().split()
    members.append((-int(params[1]), int(params[2]), params[0]))

effective_quicksort(members, 0, n - 1)

for member in members:
    print(member[2])
