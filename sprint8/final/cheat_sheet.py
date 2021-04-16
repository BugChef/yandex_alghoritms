"""
ID = 50512295

Написал комменты в коде про работу кода. Если вкратце, то сначала
создаем trie на основе допустимых к использованию слов, дальше
смотрим по бору, куда можем попасть.

Функция построения префиксного дерева работает за O(L),
где L — суммарная длина слов во множестве.
Так же используется память для хранения дерева O(L),
где L — суммарная длина слов во множестве, такое возможно,
если все слова начинаются по разному.
Еще массив терминальных элементов O(K), где K - кол-во
элементов в боре.

Функция нахождения разбиений работает за O(n⋅M),
где n — длина текста, а M = max Mi - длина самого длинного из искомых шаблонов.
Здесь память используется для хранения достижимых позиций O(n) - где
n - длина строки.

Все вместе работает за T*O(L) + O(n⋅M), где T - кол-во допустимых слов
"""


def add_string(trie, terminals, string):
    current_node = trie[0]
    current_node_index = 0

    for char in string:
        if char not in current_node:
            current_node[char] = len(trie)
            trie.append({})
            terminals.append(False)

        next_node_index = current_node[char]
        current_node = trie[next_node_index]
        current_node_index = next_node_index

    terminals[current_node_index] = True


def break_words(trie, terminals, string) -> bool:
    valid = [True] + [False] * len(string)

    for pos in range(len(string)):
        if not valid[pos]:
            continue

        # Начинаем с корня бора
        current_node = trie[0]

        # Перебираем символы шаблона, начиная со стартовой позиции.
        offset = 0

        # Расхождений с шаблоном пока не найдено
        mismatch_not_found = True

        while pos + offset < len(string):
            symbol = string[pos + offset]

            if symbol in current_node:
                # Сдвигаюсь на следующий символ
                next_index = current_node[symbol]
                current_node = trie[next_index]
                # Если это терминальный узел и я могу в него
                # попасть из предыдущей позиции, то отмечаем
                # позицию, как достижимую
                if terminals[next_index]:
                    valid[pos + offset + 1] = True
                offset += 1
            # Подходящее ребро отсутствует
            else:
                break

    # Так как нужно добраться до конца строки,
    # то смотрим на последний элемент
    return valid[len(string)]


trie = [{}]
terminals = [False]

string = input()
n = int(input())
for _ in range(n):
    dict_word = input()
    add_string(trie, terminals, dict_word)

is_valid = break_words(trie, terminals, string)
print("YES" if is_valid else "NO")
