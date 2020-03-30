import sys, copy

sys.stdin = open('B14502.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    lab = [list(map(int,input().split())) for _ in range(N)]

    # 0 : 빈칸, 1 : 벽, 2 : 바이러스가 있는 위치

    safearea = []
    dx_j = [0,1,0,-1]
    dy_i = [-1,0,1,0]

    def safe(i,j):
        global cnt, visit
        visit[i][j] = 1; cnt += 1
        for d in range(4):
            ni = i + dy_i[d]
            nj = j + dx_j[d]
            if 0 <= ni < N and 0 <= nj < M and visit[ni][nj] == 0 and virus[ni][nj] == 0:
                safe(ni,nj)

    def infection(i,j):
        global visited, virusnum, flag
        if check - virusnum < maxV:
            flag = 0
            return
        visited[i][j] = 1; virusnum += 1
        for d in range(4):
            ni = i + dy_i[d]
            nj = j + dx_j[d]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and virus[ni][nj] == 0:
                virus[ni][nj] = 2
                infection(ni,nj)

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                safearea.append([i,j])
    check = len(safearea)

    maxV = 0
    for k in range(check):
        lab[safearea[k][0]][safearea[k][1]] = 1
        for l in range(check):
            if k == l:
                continue
            lab[safearea[l][0]][safearea[l][1]] = 1
            for m in range(check):
                if k == m or l == m:
                    continue
                lab[safearea[m][0]][safearea[m][1]] = 1
                
                visited = [[0]*M for _ in range(N)]
                virus = copy.deepcopy(lab)
                virusnum = 0; flag = 1
                for i in range(N):
                    for j in range(M):
                        if virus[i][j] == 2 and visited[i][j] == 0:
                            infection(i,j)

                if flag:
                    visit = [[0]*M for _ in range(N)]
                    cnt = 0
                    for i in range(N):
                        for j in range(M):
                            if virus[i][j] == 0 and visit[i][j] == 0:
                                safe(i,j)
                            if cnt > maxV:
                                maxV = cnt
                
                lab[safearea[m][0]][safearea[m][1]] = 0
            lab[safearea[l][0]][safearea[l][1]] = 0
        lab[safearea[k][0]][safearea[k][1]] = 0

    print(maxV)










# def dfs(area):
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
# stack = list()
# visited = [[0]*M for _ in range(N)]
# for i in range(N):
#     for j in range(M):
#         if area[i][j] == 2:
#             stack.append((i,j))

#     while len(stack):
#         cr, cc = stack.pop()
#         visited[cr][cc] = 1
#         for i in range(4):
#             nr = cr + dr[i]
#             nc = cc + dc[i]
#             if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and area[nr][nc] == 0:
#                 area[nr][nc] = 2
#                 stack.append((nr, nc))

# def comb(arr,idx,cnt): # 1차원 배열의 조합을 구하기 위한 함수
#     global max_area
#     if cnt == 3: # 모든 경우의 수를 구했으니, 더 이상 진행 할 필요 없음
#          # tmpboard = board.copy()  얕은 복사이기 때문에 안됨>> 깊은 복사
#         tmp_board = list()
#         for b in board: # 원본 board 복사
#              tmp_board.append([l for l in b])
#         for i in range(len(arr)):
#             if arr[i] == 1:
#                 r = i // M
#                 c = i % M
#                 tmp_board[r][c] = 1
#         # 반복문이 끝이나면 임의의 세개의 벽을 세운 상황

#         # 바이러스 퍼뜨리기(Dfs로 진행할 수있는 모든 빈칸에 바이러스 만들기)
#         dfs(tmp_board)

#         # 남아 있는 칸의 개수 세기
#         remain = 0
#         for i in range(N):
#             for j in range(M):
#                 if tmp_board[i][j] == 0:
#                     remain += 1
#         if remain > max_area:
#             max_area = remain
#         return

#     if idx == len(arr): # 세개를 고르지 못하고, 마지막 인덱스까지 모두 검사함
#         return
#     # 위 두가지 경우에 부합하지 않은다면, 아직 세 위치를 정하지 못한 것이다. 다음으로 진행
#     # 이번 인덱스의 요소를 사용할지 안할지를 결정 해서 다음 단계로 진행
#     # 경우의수를 줄여 줍시다!
#     tmpr = idx // M
#     tmpc = idx % M
#     if board[tmpr][tmpc] == 0:
#         arr[idx] = 1
#         comb(arr,idx + 1,cnt+1)
#     arr[idx] = 0
#     comb(arr, idx + 1, cnt)

# # 7 7
# # 2 0 0 0 1 1 0
# # 0 0 1 0 1 2 0
# # 0 1 1 0 1 0 0
# # 0 1 0 0 0 0 0
# # 0 0 0 0 0 1 1
# # 0 1 0 0 0 0 0
# # 0 1 0 0 0 0 0

# N,M = map(int,input().split())
# board = [list(map(int,input().split())) for _ in range(N)]
# # print(board)
# # 조합을 구해서 해당 조합이 의미하는 칸에 벽을 세울건데...
# arr = [0]*(N*M)
# max_area = 0
# comb(arr,0,0)
# print(max_area)