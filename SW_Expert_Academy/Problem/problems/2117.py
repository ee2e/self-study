import sys

sys.stdin = open('2117.txt', 'r')

for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    home = [list(map(int,input().split())) for _ in range(N)]

    K = 2; maxH = 1 if M-1 >= 0 else 0
    while K < N+2:
        cost = K*K + (K-1)*(K-1)
        for i in range(N):
            for j in range(N):
                home_cnt = 0
                for k in range(-K+1, K):
                    if i+k < 0 or i+k >= N:
                        continue
                    for l in range(-K+1+abs(k), K-abs(k)):
                        if j+l < 0 or j+l >= N:
                            continue
                        if home[i+k][j+l]:
                            home_cnt += 1
                if M*home_cnt-cost >= 0:
                    if home_cnt > maxH:
                        maxH = home_cnt
        K += 1

    print(f'#{tc}', maxH)



# # solved by 묵
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     city = [list(map(int, input().split())) for _ in range(N)]
#     city_copy = [[[] for _ in range(N)] for _ in range(N)]
 
#     cities = []
#     count = 0
#     for row in range(N):
#         for col in range(N):
#             if city[row][col] == 1:
#                 count += 1
#                 cities.append((row, col))
#     result = 0
#     for row in range(N):
#         for col in range(N):
#             k = 1
#             cnt = 1
#             while cnt < count:
#                 cnt = 0
#                 for R, C in cities:
#                     temp = abs(row-R) + abs(col-C)
#                     if temp <= k-1:
#                         cnt += 1
#                 if cnt * M - (k * k + (k - 1) * (k - 1)) >= 0:
#                     if cnt > result:
#                         result = cnt
#                 k += 1
#     print('#{0} {1}'.format(tc, result))