N, M = map(int,input().split())

graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    u, v = map(int,input().split())
    graph[u][v] = 1
    start = v

def DFS(graph,node):
    stack = [node]
    visited = []
    while stack:
        n = stack.pop(-1)
        for j in range(N+1):
            if graph[n][j] == 1:
                if j not in stack:
                    stack.append(j)
            graph[n][j] = 0
            graph[j][n] = 0
        if n not in visited:
            visited.append(n)
    return visited

print(DFS(graph,u))