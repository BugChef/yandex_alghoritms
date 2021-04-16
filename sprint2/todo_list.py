"""
Васе нужно распечатать свой список дел на сегодня.
Помогите ему: напишите функцию, которая печатает все его дела.
Известно, что дел у Васи не больше 5000.
Внимание: в этой задаче не нужно считывать входные данные.
Нужно написать только функцию, которая принимает на вход голову списка и печатает его элементы.
Ниже дано описание структуры, которая задаёт узел списка.
"""


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node) -> None:
    current_node = node
    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next_item
