"""
ID = 43773810
"""

import sys


def main():
    k = int(sys.stdin.readline().strip())
    k *= 2  # по условию они нажимают вдвоем
    field = []
    for i in range(4):
        line = sys.stdin.readline().strip()
        line = list(line)
        field.append(line)

    # словарь для подсчета сколько раз встречается каждый символ
    char_dict = {str(x): 0 for x in range(1, 10)}
    for line in field:
        for char in line:
            # игнорируем точки, они не используются
            if char == '.':
                continue
            else:
                char_dict[char] += 1

    # считаем кол-во очков
    score = 0
    for i in range(1, 10):
        char_number = char_dict[str(i)]
        # если символ встречается меньше k раз, то игроки смогут нажать нужные кнопки
        if char_number <= k and char_number != 0:
            score += 1

    print(score)


main()