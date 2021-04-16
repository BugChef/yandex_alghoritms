from queue import SimpleQueue

n, m = [int(x) for x in input().split()]

graph = [[] for _ in range(n + 1)]
colors = ['white' for _ in range(n + 1)]
for _ in range(m):
    u, v = [int(x) for x in input().split()]
    graph[u].append(v)
    graph[v].append(u)

start_vertex = int(input())

for g in graph:
    g.sort()


def bfs(s):
    planned = SimpleQueue()
    planned.put(s)
    colors[s] = 'gray'
    path = str(s)
    while planned.qsize() != 0:
        u = planned.get()
        for v in graph[u]:
            if colors[v] == 'white':
                colors[v] = 'gray'
                planned.put(v)
                path += ' ' + str(v)
        colors[u] = 'black'
    return path


print(bfs(start_vertex))
