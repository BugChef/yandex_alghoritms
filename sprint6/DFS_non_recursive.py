class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def add_edge(self, v, w):
        self.adj[v].append(w)

    def sort(self):
        for a in self.adj:
            a.sort(reverse=True)

    def dfs(self, s):
        visited = [False for _ in range(self.V)]
        stack = []
        path = ''
        stack.append(s)

        while len(stack):
            s = stack[-1]
            stack.pop()

            if not visited[s]:
                if path == '':
                    path += str(s)
                else:
                    path += ' ' + str(s)
                visited[s] = True

            for node in self.adj[s]:
                if not visited[node]:
                    stack.append(node)

        return path


n, m = [int(x) for x in input().split()]
g = Graph(n + 1)
for _ in range(m):
    u, v = [int(x) for x in input().split()]
    g.add_edge(u, v)
    g.add_edge(v, u)

start_vertex = int(input())
g.sort()
print(g.dfs(start_vertex))