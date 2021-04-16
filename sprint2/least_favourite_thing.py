"""
Вася размышляет, что бы такое из списка не делать.
Но, кажется, все пункты очень важные!
Вася решает загадать число и удалить дело, которое идёт под этим номером.
Список дел представлен в виде односвязного списка.
Напишите функцию solution, которая принимает на вход голову списка
и номер удаляемого дела и возвращает голову обновлённого списка.
Внимание: в этой задаче не нужно считывать входные данные.
Нужно написать только функцию, которая принимает на вход голову списка
и номер удаляемого элемента и возвращает голову обновленного списка.
Ниже дано описание структуры, которая задаёт вершину списка.
"""

class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def print_linked_list(vertex):
    while vertex:
        print(vertex.value, end=" -> ")
        vertex = vertex.next_item
    print()


def solution(node, idx) -> Node:
    if idx == 0:
        return node.next_item

    previous_node = None
    next_node = None
    current_node = node
    for i in range(idx):
        previous_node = current_node
        current_node = current_node.next_item
        if i == idx - 1:
            next_node = current_node.next_item if current_node is not None else None

    previous_node.next_item = next_node
    return node


n4 = Node('4')
n3 = Node('3', n4)
n2 = Node('2', n3)
n1 = Node('1', n2)
print_linked_list(n1)
node = solution(n1, 1)
print_linked_list(node)

