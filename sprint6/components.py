n, m = [int(x) for x in input().split()]
graph = [[] for i in range(n + 1)]
for _ in range(m):
    u, v = [int(x) for x in input().split()]
    graph[u].append(v)
    graph[v].append(u)

components = [-1] * (n + 1)
components_count = 0
result = {}


def dfs_util(v):
    stack = []
    stack.append(v)

    while len(stack):
        s = stack[-1]
        stack.pop()

        if components[s] == -1:
            components[s] = components_count
            if components_count in result:
                result[components_count].append(s)
            else:
                result[components_count] = [s]

        for node in graph[s]:
            if components[node] == -1:
                stack.append(node)


def find_components():
    global components_count
    for i in range(1, n + 1):
        components_count += 1
        if components[i] == -1:
            dfs_util(i)


find_components()
components.pop(0)
print(len(result))
for res in result.values():
    res.sort()
    print(' '.join(map(str, res)))