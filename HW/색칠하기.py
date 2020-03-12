import sys

sys.stdin = open('색칠하기.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    coloring = [list(map(int,input().split())) for _ in range(N)]

    grid = [[0]*10 for _ in range(10)]

    for i in range(N):
        for r in range(coloring[i][0],coloring[i][2]+1):
            for c in range(coloring[i][1],coloring[i][3]+1):
                grid[r][c] += coloring[i][4]

    result = 0
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 3:
                result += 1

    print(f'#{tc}', result)