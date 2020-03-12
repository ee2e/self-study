import sys

sys.stdin = open('2001.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    fly = [list(map(int,input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            flyV = 0
            for k in range(M):
                for l in range(M):
                    flyV += fly[i+k][j+l]
            if flyV > maxV:
                maxV = flyV

    print(f'#{tc}', maxV)