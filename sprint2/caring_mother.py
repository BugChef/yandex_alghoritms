"""
Мама Васи хочет знать, что сын планирует делать и когда.
Помогите ей: напишите функцию solution,
определяющую индекс первого вхождения передаваемого ей на вход значения в связном списке,
если значение присутствует.
Внимание: в этой задаче не нужно считывать входные данные.
Нужно написать только функцию, которая принимает на вход голову списка и искомый элемент,
а возвращает целое число — индекс найденного элемента или -1.
Ниже дано описание структуры, которая задаёт вершину списка.
"""


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node, elem) -> int:
    current_node = node
    index = 0
    while current_node is not None:
        if current_node.value == elem:
            return index
        if current_node.next_item is None:
            return -1
        current_node = current_node.next_item
        index += 1
