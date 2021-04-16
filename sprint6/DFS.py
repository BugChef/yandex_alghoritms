from collections import defaultdict


class Graph:
    def __init__(self):
        self.result = ''
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[u].sort()

    def dfs(self, v):
        visited = [False] * (len(self.graph) + 1)
        self.dfs_util(v, visited)

    def dfs_util(self, v, visited):
        visited[v] = True
        if self.result == '':
            self.result = str(v)
        else:
            self.result += ' ' + str(v)

        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited)


n, m = [int(x) for x in input().split()]
g = Graph()
for _ in range(m):
    u, v = [int(x) for x in input().split()]
    g.add_edge(u, v)
    g.add_edge(v, u)

start_vertex = int(input())

g.dfs(start_vertex)
print(g.result)
