def split_numbers_by_space(string_with_spaces) -> [int]:
    return list(map(int, string_with_spaces.strip().split()))


matrix = []
n = int(input())
for i in range(n):
    entered_row = split_numbers_by_space(input())
    matrix.append(entered_row)

row_index = n//2
column_index = row_index


def go_round(circle_size):
    global row_index
    global column_index
    print(matrix[row_index][column_index])
    counted_range = range(circle_size - 1)
    for _ in range(1, circle_size - 1):
        column_index += 1
        print(matrix[row_index][column_index])
    for _ in counted_range:
        row_index += 1
        print(matrix[row_index][column_index])
    for _ in counted_range:
        column_index -= 1
        print(matrix[row_index][column_index])
    for _ in counted_range:
        row_index -= 1
        print(matrix[row_index][column_index])


print(matrix[row_index][column_index])
for size in range(3, n + 1, 2):
    row_index -= 1
    go_round(size)
