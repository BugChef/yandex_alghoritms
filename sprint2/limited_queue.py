"""
В первой строке записано одно число — количество команд, оно не превосходит 5000.
Во второй строке задан максимально допустимый размер очереди, он не превосходит 5000.
Далее идут команды по одной на строке. Команды могут быть следующих видов:
push x — добавить число x в очередь
pop — удалить число из очереди и вывести на печать
peek — напечатать первое число в очереди
size — вернуть размер очереди
При превышении допустимого размера очереди нужно вывести «error».
При вызове операции pop для пустой очереди нужно вывести «None».
"""
import sys


class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
            return -1
        else:
            return None

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def peek(self):
        return self.queue[self.head]


PUSH_COMMAND = "push"
POP_COMMAND = "pop"
PEEK_COMMAND = "peek"
SIZE_COMMAND = "size"


def process_command(command, queue):
    com = command.split()
    if com[0] == PUSH_COMMAND:
        number = com[1]
        if queue.push(number) is None:
            print('error')
    elif command == POP_COMMAND:
        print(queue.pop())
    elif command == PEEK_COMMAND:
        print(queue.peek())
    else:
        print(queue.size)


commands_number = int(sys.stdin.readline().strip())
max_queue_size = int(sys.stdin.readline().strip())

queue = Queue(max_queue_size)
for _ in range(commands_number):
    command = sys.stdin.readline().strip()
    process_command(command, queue)