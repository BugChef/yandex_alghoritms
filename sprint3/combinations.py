import sys

numbers = list(sys.stdin.readline().strip())

letters_by_number = {
                    '2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']
                    }

combinations = []


def generate_combinations(current_number_index, prefix):
    if current_number_index == len(numbers):
        combinations.append(prefix)
        return

    current_number = numbers[current_number_index]
    letters = letters_by_number[current_number]

    for letter in letters:
        new_prefix = prefix + letter
        generate_combinations(current_number_index + 1, new_prefix)


generate_combinations(0, '')
print(' '.join(combinations))
