import sys

sys.stdin = open('B17135.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, M, D = map(int,input().split())
    MAP = [list(map(int,input().split())) for _ in range(N)]

    def shoot(k0,k1,k2,cnt):
        if cnt == N:
        else:
            killed = [[0]*M for _ in range(len(MAP_copy))]
            N-cnt

    archer = []
    for k0 in range(0,M-2):
        for k1 in range(1,M-1):
            for k2 in range(2,M)):
                MAP_copy = []
                for m in range(N):
                    MAP_copy.append(MAP[m])
                shoot(k0,k1,k2,0)