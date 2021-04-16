"""
ID = 45683367

-- ПРИНЦИП РАБОТЫ --
В задании уже описан принцип работы)
Для вычисления значения выражения, записанного в обратной польской нотации,
нужно считывать выражение слева направо и придерживаться следующих шагов:
Обработка входного символа:
- Если на вход подан операнд, он помещается на вершину стека.
- Если на вход подан знак операции, то эта операция выполняется над требуемым количеством значений из стека,
взятых в порядке добавления. Результат выполненной операции помещается на вершину стека.
- Если входной набор символов обработан не полностью, перейти к шагу 1.
После полной обработки входного набора символов результат вычисления выражения находится в вершине стека.
Если в стеке осталось несколько чисел, то надо вывести только верхний элемент.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Можно исходить из описания работы польской нотации:
Когда в выражении встречается знак операции,
выполняется соответствующая операция над двумя ближайшими операндами,
находящимися слева от знака операции.
Результат операции заменяет в выражении последовательность её операндов и знак,
после чего выражение вычисляется дальше по тому же правилу.

Числа пушим в стэк, это и будут ближайшие операнды, как только встречаем операцию - достаем их.
Пушим результат в стэк, получается, что я заменил операцию над двумя операндами на их результат,
что и требовалось.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Все операции со стэком будут происходить за O(1), так как вставка и удаление последнего
элемента массива происходит за O(1)
Так как мне нужно перебрать все входные символы, то сложность будет O(n)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
На каждую операцию приходится 2 числа, значит в среднем в стэке будет n/2 элементов
В худшем случае n - 1 элемент
Значит стэк будет занимать O(n) памяти
"""

import sys


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


ADDITION = '+'
SUBSTRACTION = '-'
MULTIPLICATION = '*'
DIVISION = '/'


numbers_and_operations = sys.stdin.readline().strip().split()
stack = Stack()
for symbol in numbers_and_operations:
    if symbol is ADDITION:
        operand1 = stack.pop()
        operand2 = stack.pop()
        result = operand1 + operand2
        stack.push(result)
    elif symbol is SUBSTRACTION:
        operand1 = stack.pop()
        operand2 = stack.pop()
        result = operand2 - operand1
        stack.push(result)
    elif symbol is MULTIPLICATION:
        operand1 = stack.pop()
        operand2 = stack.pop()
        result = operand1 * operand2
        stack.push(result)
    elif symbol is DIVISION:
        operand1 = stack.pop()
        operand2 = stack.pop()
        result = operand2 // operand1
        stack.push(result)
    else:
        operand = int(symbol)
        stack.push(operand)

print(stack.pop())