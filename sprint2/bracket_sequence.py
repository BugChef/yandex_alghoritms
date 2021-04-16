"""
Вот какую задачу Тимофей предложил на собеседовании одному из кандидатов.
Если вы с ней ещё не сталкивались, то наверняка столкнётесь –— она довольно популярная.
Дана скобочная последовательность. Нужно определить, правильная ли она.
Будем придерживаться такого определения:
пустая строка —– правильная скобочная последовательность;
правильная скобочная последовательность, взятая в скобки одного типа,
–— правильная скобочная последовательность;
правильная скобочная последовательность
с приписанной слева или справа правильной скобочной последовательностью —– тоже правильная.
На вход подается последовательность из скобок трёх видов: [], (), {}.
Напишите функцию is_correct_bracket_seq,
которая принимает на вход скобочную последовательность и возвращает True,
если последовательность правильная, а иначе False.
"""

import sys


def is_correct_bracket_seq(sequense) -> bool:
    if len(sequense) == 0:
        return True
    elif len(sequense) % 2 == 1:
        return False

    stack = []
    for s in sequense:
        if s == '(' or s == '[' or s == '{':
            stack.append(s)
        else:
            if len(stack) > 0:
                last_elem = stack.pop()
                if last_elem == '(' and s == ')':
                    continue
                elif last_elem == '[' and s == ']':
                    continue
                elif last_elem == '{' and s == '}':
                    continue
                else:
                    return False

    return len(stack) == 0


string = sys.stdin.readline().strip()
sequence = list(string)
print(is_correct_bracket_seq(sequence))