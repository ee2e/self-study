import sys

sys.stdin = open('2001.txt','r')

T = int(input())

for tc in range(T):
    N, M = map(int,input().split())
    data_list = [list(map(int,input().split())) for _ in range(N)]

    total = 0
    total_list = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            for k in range(M):
                for l in range(M):
                    total += data_list[i+k][j+l]
            total_list.append(total)
            total = 0

    print(f'#{tc+1} {max(total_list)}')