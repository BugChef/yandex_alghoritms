"""
ID = 47497250

Мое решение работает так:
Сначала считываем документы и заодно заполняем словарь такого вида
{ слово: { номер_документа: кол-во_слов_в_документе  } }

Дальше считываем запросы и заодно сразу находим релевантности.
Из запроса делаем set, чтобы итерироваться только по уникальным словам
В процессе итерации по уникальным словам заполняем вспомогательный словарь такого вида
{ номер_документа: релевантность }
После того, как мы знаем релевантности для всех документов,
- превращаем словарь в массив [(key, value)],
- сортируем массив по value и -key, чтобы получить нужный порядок
- берем первые 5 элементов
- добавляем 1 k key
- печатаем результат

Поисковый индекс заполняется за O(n), так как операции со словарем работают за O(1)
Функция нахождения релевантности find_relevance_for_request вызывается m раз
Внутри функция работает со словарем за О(1)
Так же происходит сортировка массива за O(KlogK), где K - кол-во слов, которые совпали

получается, что алгоритм работает за O(n + m * KlogK)

Дополнительная память используется для хранения search_index, O(n) - в худшем случае
так же для relevance_by_doc внутри find_relevance_for_request, O(K) на каждой итерации

В общем случае O(n) доп памяти
"""

import sys


def fill_search_index(document, search_index, i):
    for word in document:
        if word not in search_index:
            search_index[word] = {i: 1}
        else:
            if i in search_index[word]:
                search_index[word][i] +=1
            else:
                search_index[word][i] = 1


def find_relevance_for_request(words, search_index):
    relevance_by_doc = {}

    for word in words:

        if word in search_index:
            words_count_by_doc = search_index[word]

            for key, value in words_count_by_doc.items():
                if key in relevance_by_doc:
                    relevance_by_doc[key] += value
                else:
                    relevance_by_doc[key] = value

    relevance_by_doc = list(relevance_by_doc.items())
    relevance_by_doc = sorted(relevance_by_doc, key=lambda r: (r[1], -r[0]), reverse=True)[:5]
    relevance_by_doc = list(map(lambda r: str(r[0] + 1), relevance_by_doc))
    if len(relevance_by_doc) > 0:
        print(' '.join(relevance_by_doc))


n = int(sys.stdin.readline().strip())
search_index = {}
for i in range(n):
    document = sys.stdin.readline().strip().split()
    fill_search_index(document, search_index, i)

m = int(sys.stdin.readline().strip())
for _ in range(m):
    request = sys.stdin.readline().strip().split()
    find_relevance_for_request(set(request), search_index)