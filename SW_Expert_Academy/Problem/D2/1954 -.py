import sys
sys.stdin = open('1954.txt','r')

T = int(input())

for tc in range(T):
    N = int(input())

    dx_j = [1, 0, -1, 0]
    dy_i = [0, 1, 0, -1]

    result = [[0]*N for _ in range(N)]

    num = list(range(1,N*N+1))
    k = 0

    if N % 2:
        for w in range(N//2+1):
            i = j = w
            if N - 2*w - 1 == 0:
                result[i][j] = N*N
            else:
                for d in range(4):
                    for _ in range(N-2*w-1):
                        result[i][j] = num[k]
                        ni = i + dy_i[d]
                        nj = j + dx_j[d]
                        i, j = ni, nj
                        k += 1
    
    for i in range(N):
        print(result[i])


