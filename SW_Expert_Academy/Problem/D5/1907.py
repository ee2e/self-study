import sys
from collections import deque

sys.stdin = open('1907.txt', 'r')

T = int(input())

direction = {(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)}

for tc in range(1,T+1):
    H, W = map(int,input().split())
    sandcastle = [[0 if x == '.' else int(x) for x in input()] for _ in range(H)]

    sand = [[0]*W for _ in range(H)]
    removed = deque()
    
    for i in range(1,H-1):
        for j in range(1,W-1):
            if sandcastle[i][j]:
                s = 0
                for di, dj in direction:
                    ni = i + di
                    nj = j + dj
                    if sandcastle[ni][nj] == 0:
                        s += 1
                sand[i][j] = s
                if sand[i][j] >= sandcastle[i][j]:
                    removed.append((i,j))

    cnt = 0
    while len(removed):
        for _ in range(len(removed)):
            i, j = removed.popleft()
            sandcastle[i][j] = 0
            for di, dj in direction:
                ni = i + di
                nj = j + dj
                if sandcastle[ni][nj] != 0:
                    sand[ni][nj] += 1
                    if sand[ni][nj] == sandcastle[ni][nj]:
                        sandcastle[ni][nj] = 0
                        removed.append((ni,nj))
        cnt += 1

    print(f'#{tc}', cnt)