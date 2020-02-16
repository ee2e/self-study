import sys

sys.stdin = open('1873.txt', 'r')

T = int(input())

for tc in range(T):
    H, W = map(int,input().split())
    matrix = [[x for x in input()] for _ in range(H)]
    N = int(input())
    enter = input()

    dx_j = [0,0,-1,1]
    dy_i = [-1,1,0,0]

    for s_i in range(H):
        for s_j in range(W):
            if matrix[s_i][s_j] == '^':
                d = 0
                i, j = s_i, s_j
            elif matrix[s_i][s_j] == 'v':
                d = 1
                i, j = s_i, s_j
            elif matrix[s_i][s_j] == '<':
                d = 2
                i, j = s_i, s_j
            elif matrix[s_i][s_j] == '>':
                d = 3
                i, j = s_i, s_j
    
    for e in enter:
        if e == 'U':
            d = 0
            if 0 <= i+dy_i[d] < H and 0 <= j+dx_j[d] < W and matrix[i+dy_i[d]][j+dx_j[d]] == '.':
                matrix[i][j] = '.'
                i += dy_i[d]; j += dx_j[d]
            matrix[i][j] = '^'
        elif e == 'D':
            d = 1
            if 0 <= i+dy_i[d] < H and 0 <= j+dx_j[d] < W and matrix[i+dy_i[d]][j+dx_j[d]] == '.':
                matrix[i][j] = '.'
                i += dy_i[d]; j += dx_j[d]
            matrix[i][j] = 'v'
        elif e == 'L':
            d = 2
            if 0 <= i+dy_i[d] < H and 0 <= j+dx_j[d] < W and matrix[i+dy_i[d]][j+dx_j[d]] == '.':
                matrix[i][j] = '.'
                i += dy_i[d]; j += dx_j[d]
            matrix[i][j] = '<'
        elif e == 'R':
            d = 3
            if 0 <= i+dy_i[d] < H and 0 <= j+dx_j[d] < W and matrix[i+dy_i[d]][j+dx_j[d]] == '.':
                matrix[i][j] = '.'
                i += dy_i[d]; j += dx_j[d]
            matrix[i][j] = '>'
        elif e == 'S':
            shell_i = i; shell_j = j
            while 0 <= shell_i+dy_i[d] < H and 0 <= shell_j+dx_j[d] < W:
                shell_i += dy_i[d]; shell_j += dx_j[d]
                if matrix[shell_i][shell_j] == '*':
                    matrix[shell_i][shell_j] = '.'
                    break
                elif matrix[shell_i][shell_j] == '#':
                    break

    print(f'#{tc+1}', end = ' ')
    for i in range(H):
        print(f'{"".join(matrix[i])}')