from queue import SimpleQueue

n, m = [int(x) for x in input().split()]

graph = [[] for _ in range(n + 1)]
colors = ['white' for _ in range(n + 1)]
distances = [None for _ in range(n + 1)]
for _ in range(m):
    u, v = [int(x) for x in input().split()]
    graph[u].append(v)
    graph[v].append(u)

start_vertex = int(input())
max_distance = 0


def bfs(s):
    global max_distance
    planned = SimpleQueue()
    planned.put(s)
    colors[s] = 'gray'
    distances[s] = 0
    while planned.qsize() != 0:
        u = planned.get()
        for v in graph[u]:
            if colors[v] == 'white':
                distances[v] = distances[u] + 1
                if max_distance <= distances[u] + 1:
                    max_distance = distances[u] + 1
                colors[v] = 'gray'
                planned.put(v)
        colors[u] = 'black'


bfs(start_vertex)
print(max_distance)