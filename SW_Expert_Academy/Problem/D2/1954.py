import sys
sys.stdin = open('1954.txt','r')

T = int(input())

for tc in range(T):
    N = int(input())
    matrix = [[0]*N for _ in range(N)]
    dx_j = [1, 0, -1, 0]
    dy_i = [0, 1, 0, -1]

    W = 0
    d = 0
    num = 1

    while W < N//2:
        i = j = W
        
        while d < 4:
            for _ in range(N-2*W-1):
                matrix[i][j] = num
                i += dy_i[d]; j += dx_j[d]
                num += 1
        
            d += 1

        W += 1
        d = 0

    if N % 2:
        matrix[W][W] = num

    print(f'#{tc+1}')
    for i in range(N):
        print(f'{" ".join(map(str,matrix[i]))}')