import sys

sys.stdin = open('1953.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, M, R, C, L = map(int,input().split())
    manhole = [list(map(int,input().split())) for _ in range(N)]

    V = [[0]*M for _ in range(N)]
    pipe = [[], [0,1,2,3], [1,3], [0,2], [0,3], [0,1], [1,2], [2,3]]

    dx_j = [1,0,-1,0]
    dy_i = [0,1,0,-1]

    t = 1
    V[R][C] = t
    while t < L:
        t += 1
        for i in range(N):
            for j in range(M):
                if V[i][j] == t-1:
                    for k in pipe[manhole[i][j]]:
                        ni = i + dy_i[k]
                        nj = j + dx_j[k]
                        if 0 <= ni < N and 0 <= nj < M and V[ni][nj] == 0:
                            if (k+2)%4 in pipe[manhole[ni][nj]]:
                                V[ni][nj] = t
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if V[i][j] != 0:
                cnt += 1

    print(f'#{tc}', cnt)