"""
ID = 48710965

Наверно описывать нечего, нам целый параграф теории про это написали
Работает за O(n*log(n)) в худшем случае,
память дополнительную не использует: O(1) по памяти
Трюк с сортировкой тюпла до этого в какой-то задаче финальной уже был
"""


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


n = int(input())
members = []
for _ in range(n):
    params = input().split()
    members.append((-int(params[1]), int(params[2]), params[0]))

heap_sort(members)
for i in range(n):
    print(members[i][2])
