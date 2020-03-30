import sys

sys.stdin = open('1861.txt', 'r')

# T = int(input())

# def move(room,i,j,cnt,i0,j0):
#     global maxV, num
#     for d in range(4):
#         ni = i + dy_i[d]
#         nj = j + dx_j[d]
#         if 0 <= ni < N and 0 <= nj < N and room[ni][nj] == room[i][j] + 1:
#             move(room,ni,nj,cnt+1,i0,j0)
#     if cnt > maxV:
#         maxV = cnt
#         num = room[i0][j0]
#     elif cnt == maxV and num > room[i0][j0]:
#         num = room[i0][j0]

# for tc in range(1,T+1):
#     N = int(input())
#     room = [list(map(int,input().split())) for _ in range(N)]

#     dx_j = [0,1,0,-1]
#     dy_i = [-1,0,1,0]

#     maxV = 0; num = 0
#     for i in range(N):
#         for j in range(N):
#             cnt = 0
#             move(room,i,j,1,i,j)
            
#     print(f'#{tc}', num, maxV)


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    room = [list(map(int,input().split())) for _ in range(N)]

    dx_j = [0,1,0,-1]
    dy_i = [-1,0,1,0]

    num = 0; maxV = 0
    for i in range(N):
        for j in range(N):
            flag = 1; cnt = 1; i0 = i; j0 = j
            while flag:
                for d in range(4):
                    if 0 <= i+dy_i[d] < N and 0 <= j+dx_j[d] < N and room[i+dy_i[d]][j+dx_j[d]] == room[i][j]+1 :
                        i += dy_i[d]
                        j += dx_j[d]
                        cnt += 1
                        break
                else:
                    flag = 0
            if cnt > maxV:
                maxV = cnt
                num = room[i0][j0]
            elif cnt == maxV and room[i0][j0] < num:
                num = room[i0][j0]
    
    print(f'#{tc}', num, maxV)