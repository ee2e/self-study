import sys

sys.stdin = open('2819.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = [list(map(int,input().split())) for _ in range(4)]
    dx_j = [1,-1,0,0]
    dy_i = [0,0,1,-1]
    num_list = []

    def grid(N, k, start, num):
        d = 0
        if k == 6:
            if num not in num_list:
                num_list.append(num)
        else:
            while d < 4:
                if 0 <= start[0]+dy_i[d] < 4 and 0 <= start[1]+dx_j[d] < 4:
                    num += str(N[start[0]+dy_i[d]][start[1]+dx_j[d]])
                    grid(N, k+1, [start[0]+dy_i[d], start[1]+dx_j[d]], num)
                    num = num[:-1]
                d += 1

    for i in range(4):
        for j in range(4):
            grid(N, 0, [i,j], str(N[i][j]))

    print(f'#{tc} {len(num_list)}')