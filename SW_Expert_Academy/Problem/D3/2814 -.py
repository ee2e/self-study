import sys

sys.stdin = open('D3/2814.txt', 'r')

T = int(input())


def DFS(cnt = 0):
    global visited, maxV, stack
    while stack:
        V = stack.pop()
        visited[V] = True; cnt += 1
        flag = False
        for node in adj[V]:
            if not visited[node]:
                stack.append(node)
                flag = True
        if not flag:
            if cnt > maxV:
                maxV = cnt
            cnt -= 1
            

for tc in range(1,T+1):
    # N, M = map(int,input().split())

    # adj = {i:[] for i in range(1,N+1)}
    # for _ in range(M):
    #     x, y = map(int,input().split())
    #     adj[x].append(y)
    #     adj[y].append(x)
    adj = {1: [3], 2: [3], 3: [1, 4, 2], 4: [3]}

    maxV = 0
    for i in range(1,N+1):
        visited = [False]*(N+1)
        stack = [i]
        DFS()

    print(f'#{tc}', maxV)