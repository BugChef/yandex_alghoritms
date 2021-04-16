"""
Любимый вариант очереди Тимофея — очередь,
написанная с использованием связного списка.
Помогите ему с реализацией. Очередь должна поддерживать выполнение трёх команд:
get — вывести элемент в голове очереди и удалить его. Если очередь пуста, то вывести «error».
put x — добавить число x в очередь
size — вывести текущий размер очереди
"""

import sys


class Node:
    def __init__(self, value, previous_item=None):
        self.value = value
        self.previous_item = previous_item


class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.last_added_node = None

    def put(self, value: int):
        if self.head is None:
            node = Node(value)
            self.head = node
            self.last_added_node = node
        else:
            node = Node(value)
            self.last_added_node.previous_item = node
            self.last_added_node = node

        self.size += 1

    def get(self):
        if self.size == 0:
            return None

        value_to_return = self.head.value
        self.head = self.head.previous_item

        self.size -= 1
        return value_to_return


GET_COMMAND = "get"
PUT_COMMAND = "put"
SIZE_COMMAND = "size"


def process_command(command, queue):
    com = command.split()
    if com[0] == PUT_COMMAND:
        number = com[1]
        queue.put(number)
    elif command == GET_COMMAND:
        elem = queue.get()
        if elem is None:
            print('error')
        else:
            print(elem)
    else:
        print(queue.size)


commands_number = int(sys.stdin.readline().strip())
queue = Queue()
for _ in range(commands_number):
    command = sys.stdin.readline().strip()
    process_command(command, queue)
