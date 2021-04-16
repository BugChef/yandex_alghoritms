"""
Вася решил запутать маму —– делать дела в обратном порядке.
Список его дел теперь хранится в двусвязном списке.
Напишите функцию, которая вернёт список в обратном порядке.
Внимание: в этой задаче не нужно считывать входные данные.
Нужно написать только функцию, которая принимает на вход голову двусвязного списка
и возвращает голову перевернутого списка. Ниже дано описание структуры,
которая задаёт вершину списка.
"""


class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def solution(node: DoubleConnectedNode) -> DoubleConnectedNode:
    new_node = None
    while node:
        node.next, node, new_node = new_node, node.next, node
    return new_node
