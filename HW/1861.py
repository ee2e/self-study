import sys

sys.stdin = open('1861.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    room = [list(map(int,input().split())) for _ in range(N)]
    dx_j = [1,-1,0,0]
    dy_i = [0,0,1,-1]
    maximum = 0; cnt = 1; temp = 0

    def go(room, start, first):
        global maximum, cnt, temp
        d = 0
        while d < 4:
            if 0 <= start[0]+dy_i[d] < N and 0 <= start[1]+dx_j[d] < N:
                if room[start[0]+dy_i[d]][start[1]+dx_j[d]] == room[start[0]][start[1]] + 1:
                    cnt += 1
                    go(room, [start[0]+dy_i[d], start[1]+dx_j[d]], first)
                    cnt -= 1
            d += 1
        if cnt > maximum:
            maximum = cnt
            temp = first
        elif cnt == maximum:
            if temp > first:
                temp = first

    for i in range(N):
        for j in range(N):
            first = room[i][j]
            go(room,[i,j], first)

    print(f'#{tc}', temp, maximum)