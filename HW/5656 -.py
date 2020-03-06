import sys, copy

sys.stdin = open('5656.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, W, H = map(int,input().split())
    brick = [list(map(int,input().split())) for _ in range(H)]
    dx_j = [1,0,-1,0]
    dy_i = [0,1,0,-1]

    def shatter(idx, V, data, flag):
        global cnt
        if data[idx[0]][idx[1]] == 0:
            return
        elif data[idx[0]][idx[1]] == 1:
            data[idx[0]][idx[1]] = 0
            cnt += 1
        else:
            for k in range(1,data[idx[0]][idx[1]]):
                d = 0
                while d < 4:
                    ni = idx[0] + k*dx_j[d]
                    nj = idx[1] + k*dy_i[d]
                    data[idx[0]][idx[1]] = 0
                    if 0 <= ni < H and 0 <= nj < W and [ni,nj] not in V:
                        if data[ni][nj] != 0:
                            V.append([ni,nj])
                            cnt += 1
                            shatter([ni,nj], V, data, flag)
                    d += 1
        if flag:
            temp = data
        else:
            brick = data
        return cnt

    def arrange(data, flag):
        for j in range(W):
            for i in range(H-1,-1,-1):
                if data[i][j] == 0:
                    while 0 <= i-1 < H and data[i-1][j] == 0:
                        i -= 1
                    if 0 <= i-1 < H:
                        data[i][j] = data[i-1][j]
                        data[i-1][j] = 0
        if flag:
            temp = data
        else:
            brick = data


    for k in range(N,0,-1):
        value = [0]*W
        rowcol = []
        for j in range(W):
            check = 0
            for i in range(H):
                temp = copy.deepcopy(brick)
                if temp[i][j] != 0:
                    check += 1
                    if check == 1:
                        rowcol.append([i,j])
                    cnt = 0
                    value[j] += shatter([i,j], [i,j], temp, 1)
                    arrange(temp, 1)
                if check == k:
                    break
        print(value)
        for m in range(len(rowcol)):
            if rowcol[m][1] == value.index(max(value)):
                idx = rowcol[m]
                break
        shatter(idx, idx, brick, 0)
        arrange(brick, 0)
    
    result = 0
    for i in range(H):
        for j in range(W):
            if brick[i][j] != 0:
                result += 1

    print(result)