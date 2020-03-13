import sys

sys.stdin = open('4615.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())

    board = [[0]*(N+1) for _ in range(N+1)]

    idx = N//2
    board[N//2][N//2] = board[N//2+1][N//2+1] = 2
    board[N//2+1][N//2] = board[N//2][N//2+1] = 1

    dx_j = [1,0,-1,0,-1,1,-1,1]
    dy_i = [0,1,0,-1,-1,-1,1,1]

    def othello(i,j,color):
        board[i][j] = color
        if color == 1:
            temp = 2
        else:
            temp = 1
        d = 0
        while d < 8:
            change = []
            ni = i+dy_i[d]
            nj = j+dx_j[d]
            if 0 < ni < N+1 and 0 < nj < N+1 and board[ni][nj] == temp:
                while 0 < ni < N+1 and 0 < nj < N+1 and board[ni][nj] == temp:
                    change.append([ni,nj])
                    ni = ni+dy_i[d]
                    nj = nj+dx_j[d]
                if 0 < ni < N+1 and 0 < nj < N+1 and board[ni][nj] == color:
                    for k in range(len(change)):
                        board[change[k][0]][change[k][1]] = color
            d += 1

    for i in range(M):
        i, j, color = map(int,input().split())
        othello(i,j,color)

    black = white = 0
    for i in range(N+1):
        for j in range(N+1):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1
    print(f'#{tc}', black, white)