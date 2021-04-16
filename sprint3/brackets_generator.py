import sys


def generate_brackets(result, opened_brackets, closed_brackets, pairs):
    if opened_brackets == pairs and closed_brackets == pairs:
        print(result)
    else:
        if opened_brackets < pairs:
            generate_brackets(result + '(', opened_brackets + 1, closed_brackets, pairs)
        if closed_brackets < opened_brackets:
            generate_brackets(result + ')', opened_brackets, closed_brackets + 1, pairs)


n = int(sys.stdin.readline().strip())
generate_brackets("", 0, 0, n)
