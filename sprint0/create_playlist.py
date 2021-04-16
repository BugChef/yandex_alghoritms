import sys


def split_numbers_by_space(string_with_spaces) -> [int]:
    string_number_list = string_with_spaces.split()
    number_list = list(map(int, string_number_list))
    return number_list


n = int(input())
if n < 1:
    print('')
    sys.exit()
russian_id_list = split_numbers_by_space(input())
foreign_id_list = split_numbers_by_space(input())

output = []

for i in range(n):
    russian_id = russian_id_list[i]
    foreign_id = foreign_id_list[i]
    output.append(russian_id)
    output.append(foreign_id)

print(' '.join(map(str, output)))