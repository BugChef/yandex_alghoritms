def split_numbers_by_space(string_with_spaces) -> {str}:
    string_number_list = string_with_spaces.split()
    number_set = set(string_number_list)
    return number_set


n = int(input())
users_id_set = split_numbers_by_space(input())

numbers_left_to_find = 2
missing_users = []

for i in range(1, n + 1):
    i_string = str(i)
    if i_string not in users_id_set:
        missing_users.append(i_string)
        n -= 1
    if n == 0:
        break

print(' '.join(missing_users))