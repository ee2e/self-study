import sys

sys.stdin = open('1211.txt', 'r')

T = 10

directions = {(0,1),(0,-1),(1,0)}

def search(i,j):
    global visited, cnt
    while True:
        visited[i][j] = 1
        for direction in directions:
            ni = i + direction[0]
            nj = j + direction[1]
            if 0 <= ni < 100 and 0 <= nj < 100:
                if ni == 99 and ladder[ni][nj] == 1:
                    return
                elif visited[ni][nj] == 0 and ladder[ni][nj]:
                    cnt += 1
                    i = ni; j = nj
                    break


for tc in range(1,T+1):
    N = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]

    minV = 10000; result = -1
    for j in range(100):
        visited = [[0]*100 for _ in range(100)]
        cnt = 0
        if ladder[0][j] == 1:
            search(0,j)
            if cnt < minV:
                minV = cnt; result = j
    
    print(f'#{tc}', result)