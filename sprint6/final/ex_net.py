"""
ID = 49769472

Использовал алгоритм Прима, который работает за O(V^3)
после работы алгоритма проверяю за O(V) является ли граф связным
и еще за O(V) собираю путь (mst)

Дополнительная память используется для хранения посещенных вершин, весов и родителей
Каждая занимает O(V) памяти
"""

import math

n, m = [int(x) for x in input().split()]
graph = [[0 for i in range(n)] for j in range(n)]
for _ in range(m):
    u, v, d = [int(x) for x in input().split()]
    if graph[u - 1][v - 1] < d:
        graph[u - 1][v - 1] = d
        graph[v - 1][u - 1] = d


def find_max_vertex(visited, weights):
    index = -1
    max_weight = 0

    for i in range(n):
        if not visited[i] and weights[i] > max_weight:
            max_weight = weights[i]
            index = i
    return index


def maximum_spanning_tree(graph):
    visited = [False] * n
    weights = [0] * n
    parent = [-1] * n

    weights[0] = math.inf

    for i in range(n - 1):
        max_vertex_index = find_max_vertex(visited, weights)
        visited[max_vertex_index] = True

        for j in range(n):
            if graph[j][max_vertex_index] != 0 and not visited[j]:
                if graph[j][max_vertex_index] > weights[j]:
                    weights[j] = graph[j][max_vertex_index]
                    parent[j] = max_vertex_index

    if -1 in parent[1:]:
        print("Oops! I did it again")
    else:
        mst = 0
        for i in range(1, n):
            mst += graph[i][parent[i]]
        print(mst)


maximum_spanning_tree(graph)

