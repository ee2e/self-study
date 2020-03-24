import sys

sys.stdin = open('B14502.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    lab = [list(map(int,input().split())) for _ in range(N)]

    # 0 : 빈칸, 1 : 벽, 2 : 바이러스가 있는 위치

    visit = [[0]*M for _ in range(N)]
    dx_j = [0,1,0,-1]
    dy_i = [-1,0,1,0]
    cnt = 0

    def DFS(i,j):
        global cnt
        visit[i][j] = 1; cnt += 1
        for d in range(4):
            ni = i + dy_i[d]
            nj = j + dx_j[d]
            if 0 <= ni < N and 0 <= nj < M and visit[ni][nj] == 0 and lab[ni][nj] == 0:
                DFS(ni,nj)

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0 and visit[i][j] == 0:
                DFS(i,j)

    print(cnt)