"""
ID = 45681797

Расширил функционал кольцевого буфера из теории.
-- ПРИНЦИП РАБОТЫ --
'max_n' - максимально возможное количество элементов в очереди
'head' - индекс слудующего элемента добавленного в начало очереди
'tail' - индекс слудующего элемента добавленного в конец очереди
'size' - размер очереди

Вся задача сводится к трэкингу индексов.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

-Изначально я говорю, что следующий элемент,
добавленный в начало будет на 1ой позиции в массив, а в конец на нулевой.

- Допустим я сначала добавляю элемент в начало очереди, добавлю я его на позицию 1,
следовательно позиция для следующего элемента добавленного в начало будет 2.

- Допустим я хочу добавить элемент в конец очереди, добавлю я его на позицию 0,
следовательно позиция для следующего элемента добавленного в конец будет 0 - 1 = -1 (что не подходит),
поэтому все индексы взяты по модулю 'max_n', тогда индекс будет равен max_n - 1.

-При извлечении элементов я просто беру значение по индексу до 'head' и после 'tail' (так же беру
по модулю max_n).

- Так же есть проверки на размер очереди при попытке добавления или извлечения элемента

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Так как мы заранее знаем размер массива,
то массив не будет занаво аллоцироваться в памяти, что обеспечит мне добавление
и доступ к элементам за O(1).
Все методы в классе Deque просто обращаются к ячейке массива ,
значит все операции будут выполняться за O(1)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Массив в классе Deque всегда содержит n элементов, значит всегда занимает O(n) памяти
Так же в класс есть 4 вспомогательные переменные, каждая из которых занимает O(1) памяти
Получается что всего Deque занимает 4*O(1) + O(n) = O(n) памяти
"""

import sys


class Deque:
    def __init__(self, n):
        self.deque = [None] * n
        self.max_n = n
        self.head = 1
        self.tail = 0
        self.size = 0

    def push_back(self, x):
        if self.size != self.max_n:
            self.deque[self.tail] = x
            self.tail = (self.tail - 1) % self.max_n
            self.size += 1
            return -1
        else:
            return None

    def push_front(self, x):
        if self.size != self.max_n:
            self.deque[self.head] = x
            self.head = (self.head + 1) % self.max_n
            self.size += 1
            return -1
        else:
            return None

    def pop_back(self):
        if self.size == 0:
            return None
        new_tail_index = (self.tail + 1) % self.max_n
        x = self.deque[new_tail_index]
        self.deque[new_tail_index] = None
        self.tail = new_tail_index
        self.size -= 1
        return x

    def pop_front(self):
        if self.size == 0:
            return None
        new_head_index = (self.head - 1) % self.max_n
        x = self.deque[new_head_index]
        self.deque[new_head_index] = None
        self.head = new_head_index
        self.size -= 1
        return x


PUSH_BACK = 'push_back'
PUSH_FRONT = 'push_front'
POP_FRONT = 'pop_front'
POP_BACK = 'pop_back'


def process_command(command, deque):
    com = command.split()
    if com[0] == PUSH_BACK:
        number = com[1]
        if deque.push_back(number) is None:
            print('error')
    elif com[0] == PUSH_FRONT:
        number = com[1]
        if deque.push_front(number) is None:
            print('error')
    elif command == POP_BACK:
        number = deque.pop_back()
        if number is None:
            print('error')
        else:
            print(number)
    else:
        number = deque.pop_front()
        if number is None:
            print('error')
        else:
            print(number)


commands_number = int(sys.stdin.readline().strip())
max_dequeue_size = int(sys.stdin.readline().strip())
deque = Deque(max_dequeue_size)
for _ in range(commands_number):
    command = sys.stdin.readline().strip()
    process_command(command, deque)
