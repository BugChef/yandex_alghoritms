n, m = [int(x) for x in input().split()]

graph = [[] for i in range(n + 1)]
entry = [0 for _ in range(n + 1)]
leave = [0 for _ in range(n + 1)]
colors = ['white' for _ in range(n + 1)]
time = 0

for _ in range(m):
    u, v = [int(x) for x in input().split()]
    graph[u].append(v)

for g in graph:
    g.sort()


def dfs(u):
    global time
    entry[u] = time
    time += 1
    colors[u] = 'gray'

    for v in graph[u]:
        if colors[v] == 'white':
            dfs(v)

    leave[u] = time
    colors[u] = 'black'
    time += 1


dfs(1)
for i in range(1, n + 1):
    print(str(entry[i]) + " " + str(leave[i]))

