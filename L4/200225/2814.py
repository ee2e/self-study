import sys

sys.stdin = open('2814.txt', 'r')

T = int(input())

def DFS(graph, start):
    for val in graph[start]:
        if val not in visited:
            if val in graph[visited[-1]]:
                visited.append(val)
                DFS(graph, val)    
            else:
                print(visited)

for tc in range(1,T+1):
    N, M = map(int,input().split())
    graph = {}

    for i in range(1,N+1):
        graph[i] = []

    for _ in range(M):
        a, b = map(int,input().split())
        graph[a] += [b]
        graph[b] += [a]

    result = 0
    for key in graph.keys():
        visited = [key]
        DFS(graph, key)
        print(visited)
        print(graph)
        if len(visited) > result:
            result = len(visited)

    print(f'#{tc} {result}')
