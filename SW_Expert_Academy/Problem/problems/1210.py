import sys

sys.stdin = open('1210.txt', 'r')

T = 10


# # 방법1
# direction = {(0,1),(0,-1),(1,0)}

# def search(fj,i,j,flag):
#     global visited, result
#     visited[i][j] = 1
#     for d in direction:
#         ni = i + d[0]
#         nj = j + d[1]
#         if 0 <= ni < 100 and 0 <= nj < 100:
#             if ladder[ni][nj] == 1 and visited[ni][nj] == 0:
#                 search(fj,ni,nj,0)
#                 flag = 1
#             elif ladder[ni][nj] == 2:
#                 result = fj
#                 return
#         if flag:
#             break

# for tc in range(1,T+1):
#     N = int(input())
#     ladder = [list(map(int,input().split())) for _ in range(100)]

#     result = -1

#     for j in range(100):
#         if ladder[0][j] == 1:
#             visited = [[0]*100 for _ in range(100)]
#             search(j,0,j,0)
#         if result > -1:
#             break
    
#     print(f'#{tc}', result)



# # 방법2
# direction = {(0,-1),(0,1),(-1,0)}

# def search(i,j,flag):
#     global visited, result
#     visited[i][j] = 1
#     for d in direction:
#         ni = i + d[0]
#         nj = j + d[1]
#         if ni == 0:
#             result = nj
#             return
#         elif 0 <= ni < 100 and 0 <= nj < 100:
#             if ladder[ni][nj] == 1 and visited[ni][nj] == 0:
#                 search(ni,nj,0)
#                 flag = 1
#         if flag:
#             break

# for tc in range(1,T+1):
#     N = int(input())
#     ladder = [list(map(int,input().split())) for _ in range(100)]

#     j = ladder[99].index(2)
    
#     visited = [[0]*100 for _ in range(100)]
#     result = 0
#     search(99,j,0)

#     print(f'#{tc}', result)



# 방법3
direction = {(0,-1),(0,1),(-1,0)}

def search(i,j):
    global visited
    while True:
        visited[i][j] = 1
        for d in direction:
            ni = i + d[0]
            nj = j + d[1]
            if ni == 0:
                return nj
            elif 0 <= ni < 100 and 0 <= nj < 100:
                if ladder[ni][nj] == 1 and visited[ni][nj] == 0:
                    i = ni; j = nj
                    break

for tc in range(1,T+1):
    N = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]

    j = ladder[99].index(2)
    visited = [[0]*100 for _ in range(100)]
    result = search(99,j)

    print(f'#{tc}', result)