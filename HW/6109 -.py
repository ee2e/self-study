import sys

sys.stdin = open('6109.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, S = input().split()
    N = int(N)
    MAP = [list(map(int,input().split())) for _ in range(N)]

    dx_j = [1,-1,0,0]
    dy_i = [0,0,1,-1]
    ds_j = [0,3,0,0]
    ds_i = [0,0,0,3]
    # left, right, up, down
    delta = [0,1,2,3]
    k = [1,-1,1,-1]
    S_list = ['left','right','up','down']

    d = S_list.index(S)
    k = k[S_list.index(S)]
    si = ds_i[S_list.index(S)]
    sj = ds_j[S_list.index(S)]

    if d == 0 or d == 1:
        i = si
        while 0 <= i < N:
            j = sj
            while 0 <= j < N:
                ni = i + dy_i[d]
                nj = j + dx_j[d]
                while 0 <= ni < N and 0 <= nj < N:
                    if MAP[i][j] and MAP[i][j] == MAP[ni][nj]:
                        MAP[i][j] = MAP[i][j]*2
                        MAP[ni][nj] = 0
                        i += ni; j += nj
                        break
                    elif MAP[ni][nj]:
                        break
                    ni += dy_i[d]
                    nj += dx_j[d]
                j += k
            i += 1
    else:
        j = sj
        while 0 <= j < N:
            i = si
            while 0 <= i < N:
                ni = i + dy_i[d]
                nj = j + dx_j[d]
                while 0 <= ni < N and 0 <= nj < N:
                    if MAP[i][j] and MAP[i][j] == MAP[ni][nj]:
                        MAP[i][j] = MAP[i][j]*2
                        MAP[ni][nj] = 0
                        i += ni; j += nj
                        break
                    elif MAP[ni][nj]:
                        break
                    ni += dy_i[d]
                    nj += dx_j[d]
                i += k
            j += 1

    print(MAP)