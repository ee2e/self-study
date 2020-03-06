import sys

sys.stdin = open('1949.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, K = map(int,input().split())
    mountain = [list(map(int,input().split())) for _ in range(N)]

    dx_j = [1,0,-1,0]
    dy_i = [0,1,0,-1]

    def hiking(i,j,val,flag):
        global maxV
        d = 0
        while d < 4:
            ni = i+dy_i[d]
            nj = j+dx_j[d]
            if 0 <= ni < N and 0 <= nj < N and [ni,nj] not in V:
                if mountain[ni][nj] < val:
                    V.append([ni,nj])
                    hiking(ni,nj,mountain[ni][nj],flag)
                    V.pop(-1)
                else:
                    if flag == 0:
                        for k in range(1,K+1):
                            if mountain[ni][nj]-k < val:
                                V.append([ni,nj])
                                hiking(ni,nj,mountain[ni][nj]-k,1)
                                V.pop(-1)
            d += 1
        if len(V) > maxV:
            maxV = len(V)

    maximum = 0
    for i in range(N):
        for j in range(N):
            if mountain[i][j] > maximum:
                maximum = mountain[i][j]

    maxV = 0
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == maximum:
                V = [[i,j]]
                hiking(i,j,maximum,0)

    print(f'#{tc}', maxV)