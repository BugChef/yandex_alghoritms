def dfs(graph, n) -> bool:
    verticies = range(n)
    color = ['white'] * n
    stack = []

    for v in verticies:
        if color[v] == 'black':
            continue
        stack.append((v, 'f'))
        while stack:
            v, stage = stack.pop()
            if stage == 'f':
                stack.append((v, 'r'))
                if color[v] == 'gray':
                    return True
                if color[v] == 'black':
                    continue
                color[v] = 'gray'

                for w in graph[v]:
                    if color[w] == 'gray':
                        return True
                    if color[w] == 'black':
                        continue
                    stack.append((w, 'f'))
            else:
                color[v] = 'black'
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
