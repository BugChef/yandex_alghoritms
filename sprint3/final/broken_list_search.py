"""
ID = 46692084

Разделил задачу на 2 части, сначала ищу сдвиг, потом делаю бинарный поиск с учетом сдвига.
Сдвиг ищу следующим образом, допустим есть массив [6, 7, 8, 1, 2, 3, 4], сначала нужно найти
low, high, mid для этого массива (похоже на бинарный поиск) [6, 7, 8, 1, 2, 3, 4]
                                                             ^        ^        ^
                                                            low      mid     high
Дальше проверяем, если low > mid и mid < high - это значит, что промежуток от mid до high точно отсортирован
и мы можем избавиться от него и сделать high = mid, массив получается выглядит вот так:
                                                            [6, 7, 8, 1, 2, 3, 4]
                                                             ^  ^      ^
                                                            low mid   high
Либо если low < mid и mid > high - это значит, что промежуток от low до mid точно отсортирован
и мы можем избавиться от него и сделать low = mid
Продолжаем делить массив пополам, пока не окажется, что high - low == 1, это значит, что мы нашли
максимальный и минимальный элемент этой последовательности и следовательно сдвиг - это позиция минимального элемента + 1
Функция reveal_shift будет работать за O(logN), так как массив постоянно делится пополам


Дальше можно легко найти искомый элемент обычным бинарным поиском, с поправкой на сдвиг,
shifted_binary_search будет так же работать за O(logN)

Общеее решение будет работать так же за O(logN), так как O(logN) + O(logN) = O(2 * logN) = O(logN)
Решение не использует дополнительной памяти, поэтому будет О(1) по памяти
"""

import sys


def reveal_shift(arr):
    low = 0
    high = len(arr) - 1

    if arr[0] <= arr[-1]:
        return 0

    while low <= high:
        mid = (low + high) // 2

        if arr[low] > arr[mid] and arr[mid] < arr[high]:
            high = mid
        elif arr[low] < arr[mid] and arr[mid] > arr[high]:
            low = mid
        elif high - low == 1:
            return low + 1


def shifted_binary_search(arr, val, shift):
    length = len(arr)
    low = 0
    high = length - 1

    while low <= high:
        mid = (low + high) // 2
        shifted_middle_elem = arr[(mid + shift) % length]

        if shifted_middle_elem == val:
            return (mid + shift) % length
        elif val > shifted_middle_elem:
            low = mid + 1
        elif val < shifted_middle_elem:
            high = mid - 1

    return -1


n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))

shift_in_array = reveal_shift(numbers)
index = shifted_binary_search(numbers, k, shift_in_array)

print(index)