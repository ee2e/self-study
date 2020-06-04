import sys

sys.stdin = open('1249.txt', 'r')

from collections import deque

direction = {(-1,0), (0,1), (1,0), (0,-1)}

for tc in range(1,int(input())+1):
    N = int(input())
    data = [[int(x) for x in input()] for _ in range(N)]

    INF = float('inf')
    visited = [[INF]*N for _ in range(N)]; visited[0][0] = 0

    Q = deque([(0,0)])
    while Q:
        i, j = Q.popleft()
        for d in direction:
            ni = i + d[0]
            nj = j + d[1]
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] > visited[i][j] + data[ni][nj]:
                    visited[ni][nj] = visited[i][j] + data[ni][nj]
                    Q.append((ni,nj))

    print(f'#{tc}', visited[N-1][N-1])