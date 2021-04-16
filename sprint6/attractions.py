n, m = [int(x) for x in input().split()]
graph = [[float('inf') if i != j else 0 for i in range(n)] for j in range(n)]
for _ in range(m):
    u, v, d = [int(x) for x in input().split()]
    if graph[u - 1][v - 1] == float('inf') or graph[u - 1][v - 1] > d:
        graph[u - 1][v - 1] = d
        graph[v - 1][u - 1] = d


def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


floyd_warshall()
for i in graph:
    res = ''
    for j in i:
        d = j
        if j == float('inf'):
            d = -1
        if res == '':
            res += str(d)
        else:
            res += ' ' + str(d)
    print(res)