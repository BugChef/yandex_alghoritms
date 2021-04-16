def merge(arr: list, left: int, mid: int, right: int) -> list:
    left_copy = arr[left: mid + 1]
    right_copy = arr[mid + 1: right + 1]

    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left

    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            arr[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        else:
            arr[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        sorted_index = sorted_index + 1

    while left_copy_index < len(left_copy):
        arr[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        arr[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1

    return arr


def merge_sort(arr: list, left: int, right: int):
    if left >= right:
        return

    middle = (left + right)//2
    merge_sort(arr, left, middle)
    merge_sort(arr, middle + 1, right)
    merge(arr, left, middle, right)


test = [9, 6, 8, 3, 5, 2]
merge_sort(test, 0, len(test))
print(test)

