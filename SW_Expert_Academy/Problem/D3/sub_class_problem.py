# 기지국 문제
import sys

sys.stdin = open('problem.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())

    house_list = [[x for x in input()] for _ in range(N)]

    dx_j = [0, -1, 0, 1]
    dy_i = [-1, 0, 1, 0]

    for i in range(N):
        for j in range(N):
            d = 0
            if house_list[i][j] == 'A' or house_list[i][j] == 'B' or house_list[i][j] == 'C':
                while d < 4:
                    for i in range(ord(house_list[i][j]) - ord('@')):
                        if 0 <= i+dy_i[d]*(i+1) < N and 0 <= j+dx_j[d]*(i+1) < N:
                            house_list[i+dy_i[d]*(i+1)][j+dx_j[d]*(i+1)] = 'X'
                    d += 1

    cnt = 0
    for i in range(N):
        for j in range(N):
            if house_list[i][j] == 'H':
                cnt += 1

    print('#{} {}'.format(tc+1,cnt))