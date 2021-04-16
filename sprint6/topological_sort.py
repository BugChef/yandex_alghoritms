from collections import deque

n, m = [int(x) for x in input().split()]
graph = [[] for i in range(n + 1)]
for _ in range(m):
    u, v = [int(x) for x in input().split()]
    graph[u].append(v)

deque = deque()
colors = ['white' for _ in range(n + 1)]


def top_sort(v):
    colors[v] = 'gray'

    for w in graph[v]:
        if colors[w] == 'white':
            top_sort(w)

    colors[v] = 'black'
    deque.appendleft(str(v))


def main_top_sort():
    for i in range(1, n + 1):
        if colors[i] == 'white':
            top_sort(i)


main_top_sort()
print(' '.join(deque))