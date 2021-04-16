"""
ID = 49709478

Решал так: Если дорога типа 'B' то добавлял путь как есть,
если типа 'R', то инвертировал путь, после этого вся задача свелась
к нахождению цикла в графе.

Сложность алгоритма такая же как итеративный DFS - O(|V| + |E|)

Дополнительная память используется для хранения графа O(n^2) в худшем случае
Для хранения списка вершин, посещенных вершин, стэка и вершин, которые в процессе обработки O(n)
"""


def dfs(graph, n) -> bool:
    verticies = range(n)
    visited = [False for _ in range(n)]
    stack = []
    on_stack = [False for _ in range(n)]

    for v in verticies:
        if visited[v]:
            continue
        stack.append(v)

        while stack:
            s = stack[-1]

            if not visited[s]:
                visited[s] = True
                on_stack[s] = True
            else:
                on_stack[s] = False
                stack.pop()
                continue

            for w in graph[s]:
                if not visited[w]:
                    stack.append(w)
                elif on_stack[w]:
                    return True

    return False


n = int(input())
graph = [[] for _ in range(n)]
for i in range(n - 1):
    symbols_count = n - i - 1
    inp = input().strip()
    railways = list(inp)
    for j in range(i + 1, i + symbols_count + 1):
        symbol = railways[j - i - 1]
        if symbol == 'B':
            graph[i].append(j)
        else:
            graph[j].append(i)

has_cycle = dfs(graph, n)
print('NO' if has_cycle else 'YES')
