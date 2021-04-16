n, m = [int(x) for x in input().split()]
graph = [[0 for i in range(n)] for j in range(n)]
for _ in range(m):
    u, v, d = [int(x) for x in input().split()]
    if graph[u - 1][v - 1] < d:
        graph[u - 1][v - 1] = d
        graph[v - 1][u - 1] = d


def add_vertex(v, added, not_added, edges):
    added.add(v)
    not_added.remove(v)
    v_edges = []
    for i in range(n):
        edge = graph[v][i]
        if edge != 0 and i in not_added:
            v_edges.append((edge, v, i))  # dist, from, to
    edges.extend(v_edges)


def find_mst(added, not_added, edges):
    maximum_spanning_tree = 0
    vertices = range(n)
    not_added = set(vertices)
    v = vertices[0]
    add_vertex(v, added, not_added, edges)

    while len(edges) != 0 and len(not_added) != 0:
        e = max(edges)
        edges.remove(e)
        if e[2] in not_added:
            maximum_spanning_tree += e[0]
            add_vertex(e[2], added, not_added, edges)

    if len(not_added) == 0:
        print(maximum_spanning_tree)
    else:
        print('Oops! I did it again')


added = set()
not_added = set()
edges = []

find_mst(added, not_added, edges)
