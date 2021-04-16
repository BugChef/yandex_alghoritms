"""
Нужно реализовать класс StackMax,
который поддерживает операцию определения максимума среди всех элементов в стеке.
Класс также должен поддерживать все операции,
реализованные в классе Stack, из урока.
При этом в классе StackMax может быть реализовано не более трёх методов.
Стек может содержать только данные типов,
поддерживающих операцию сравнения.
Иначе операция поиска максимума будет некорректной.
"""

import sys


class StackMax:
    def __init__(self):
        self.main_stack = []
        self.track_stack = []

    def push(self, x):
        self.main_stack.append(x)
        if len(self.main_stack) == 1:
            self.track_stack.append(x)
            return

        if x > self.track_stack[-1]:
            self.track_stack.append(x)
        else:
            self.track_stack.append(self.track_stack[-1])

    def get_max(self):
        if len(self.track_stack) > 0:
            return self.track_stack[-1]
        else:
            return None

    def pop(self):
        if len(self.main_stack) > 0:
            self.track_stack.pop()
            return self.main_stack.pop()
        else:
            return None


GET_MAX_COMMAND = "get_max"
POP_COMMAND = "pop"


def process_command(command, stack):
    if command == GET_MAX_COMMAND:
        print(stack.get_max())
    elif command == POP_COMMAND:
        if stack.pop() is None:
            print('error')
    else:
        number = int(command.strip().split()[1])
        stack.push(number)


n = int(sys.stdin.readline().strip())
stack = StackMax()
for _ in range(n):
    command = sys.stdin.readline().strip()
    process_command(command, stack)