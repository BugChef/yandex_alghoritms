"""
ID = 47712586

Я сделал хэш таблицу с помощью массива и в каждой ячейке массива я храню 2ух связный список, размером массива взял простое число 99971.
В задании про хэш функцию ничего не было сказано, в чатике на всякий случай тоже спросил - сказали можно стандартную юзать, так и сделал.

Не знаю, что можно напиать про работу - стандартная реализация хэш таблицы, в теории описана ее работа, наверно пропущу этот момент.

Все операции данной реализации работают за O(1) в лучшем случае, при отсутствии коллизий.
Если все же коллизии присутствуют, то все операции работают за O(k), где k - кол-во элементов в списке (нужно пройтись по списку)

Дополнительная паммять не используется, потребляемая память будет зависеть от количества элементов, то есть O(n)
"""

import sys


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self.capacity = 99971
        self.buckets = [None] * self.capacity

    def hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self.hash(key)
        node = self.buckets[index]

        if node is None:
            self.buckets[index] = Node(key, value)
            return

        while node is not None and node.key != key:
            node = node.next

        if node is not None:
            node.value = value
            return

        new_node = Node(key, value)
        new_node.next = self.buckets[index]
        self.buckets[index] = new_node

    def get(self, key):
        index = self.hash(key)
        node = self.buckets[index]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value

    def delete(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        prev = None

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            return None
        else:
            result = node.value

            if prev is None:
                self.buckets[index] = None
            else:
                prev.next = prev.next.next
            return result


n = int(sys.stdin.readline().strip())
hash_table = HashTable()
for _ in range(n):
    command = sys.stdin.readline().strip().split()
    com = command[0]
    key = command[1]

    if com == 'get':
        print(hash_table.get(key))
    elif com == 'put':
        value = command[2]
        hash_table.put(key, value)
    else:
        print(hash_table.delete(key))