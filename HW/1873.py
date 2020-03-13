import sys

sys.stdin = open('1873.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    H, W = map(int,input().split())
    MAP = [list(input()) for _ in range(H)]
    N = int(input())
    enter = input()

    for i in range(H):
        for j in range(W):
            if MAP[i][j] == '<' or MAP[i][j] == '>' or MAP[i][j] == '^' or MAP[i][j] == 'v':
                start_i, start_j = i, j
                break
    
    dx_j = [0,0,-1,1]
    dy_i = [-1,1,0,0]
    shape = ['^','v','<','>']

    def action(i,j,s):
        if s == 'S':
            if MAP[i][j] == '^': d = 0
            elif MAP[i][j] == 'v': d = 1
            elif MAP[i][j] == '<': d = 2
            else: d = 3
            ni = i + dy_i[d]
            nj = j + dx_j[d]
            while 0 <= ni < H and 0 <= nj < W:
                if MAP[ni][nj] == '*':
                    MAP[ni][nj] = '.'
                    break
                elif MAP[ni][nj] == '#':
                    break
                ni = ni + dy_i[d]
                nj = nj + dx_j[d]
        else:
            if s == 'U': d = 0
            elif s == 'D': d = 1
            elif s == 'L': d = 2
            elif s == 'R': d = 3
            MAP[i][j] = shape[d]
            ni = i + dy_i[d]
            nj = j + dx_j[d]
            if 0 <= ni < H and 0 <= nj < W and MAP[ni][nj] == '.':
                MAP[i][j] = '.'
                MAP[ni][nj] = shape[d]
                i, j = ni, nj
        return i, j


    for i in range(N):
        start_i, start_j = action(start_i,start_j,enter[i])

    print(f'#{tc}', ''.join(MAP[0]))
    for i in range(1,H):
        print(''.join(MAP[i]))