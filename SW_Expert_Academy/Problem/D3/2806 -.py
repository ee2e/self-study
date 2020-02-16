import sys

sys.stdin = open('2806.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())

    matrix = [[1]*N for _ in range(N)]

    dx_j = [-1,1,1,-1]
    dy_i = [-1,-1,1,1]
    d = 0

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                for k in range(N):
                    for l in range(N):
                        if k != i and l != j:
                            matrix[k][l] = 0
                while d < 4:
                    if 0 <= i+dy_i[d] < N and 0 <= j+dx_j[d] < N:
                        matrix[i+dy_i[d]][j+dx_j[d]] = 0
                    d += 1
            break

    print(matrix)