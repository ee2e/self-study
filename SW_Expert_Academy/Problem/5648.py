import sys

sys.stdin = open('5648.txt', 'r')

from collections import deque

# T = int(input())

# # 상 0 하 1 좌 2 우 3

# def BFS(energy):
#     while A:
#         length = len(A)
#         for i in range(length):
#             temp = energy
#             num, x, y, d, K = A.popleft()
#             if abs(x) > 2000 or abs(y) > 2000: continue
#             if checked[num]: continue
#             length = len(A)
#             for j in range(length):
#                 if x == A[j][1] and y == A[j][2]:
#                     energy += A[j][4]; checked[num] = True
#             if energy == temp:
#                 A.append([num,x+direction[d][0],y+direction[d][1],d,K])
#             else:
#                 energy += K
#     return energy

# for tc in range(1,T+1):
#     N = int(input())

#     A = deque([]); checked = [False]*N
#     direction = [(0,1),(0,-1),(-1,0),(1,0)]

#     for num in range(N):
#         x, y, d, K = map(int,input().split())
#         if d == 0:
#             A.append([num, x*2, y*2+1, d, K])
#         elif d == 1:
#             A.append([num, x*2, y*2-1, d, K])
#         elif d == 2:
#             A.append([num, x*2-1, y*2, d, K])
#         else:
#             A.append([num, x*2+1, y*2+1, d, K])

#     print(f'#{tc}', BFS(0))


T = int(input())

# 상 0 하 1 좌 2 우 3

for tc in range(1,T+1):
    N = int(input())

    A = []

    for num in range(N):
        x, y, d, K = map(int,input().split())
        A.append([x*2, y*2, d, K])

    atom = []
    for i in range(N):
        if A[i][2] == 0:
            for j in range(i+1,N):
                if A[j][2] == 1:
                    if A[i][0] == A[j][0] and A[i][1] < A[j][1]:
                        atom.append([(A[j][1]-A[i][1])//2, i, j])
                elif A[j][2] == 2:
                    if A[i][1]-A[i][0] == A[j][1]-A[j][0] and A[j][0] > A[i][0]:
                        atom.append([A[j][0]-A[i][0], i, j])
                elif A[j][2] == 3:
                    if A[i][0]+A[i][1] == A[j][0]+A[j][1] and A[i][0] > A[j][0]:
                        atom.append([A[i][0]-A[j][0], i, j])
        elif A[i][2] == 1:
            for j in range(i+1,N):
                if A[j][2] == 0:
                    if A[i][0] == A[j][0] and A[i][1] > A[j][1]:
                        atom.append([(A[i][1]-A[j][1])//2, i, j])
                elif A[j][2] == 2:
                    if A[i][0]+A[i][1] == A[j][0]+A[j][1] and A[j][0] > A[i][0]:
                        atom.append([A[j][0]-A[i][0], i, j])
                elif A[j][2] == 3:
                    if A[i][1]-A[i][0] == A[j][1]-A[j][0] and A[i][0] > A[j][0]:
                        atom.append([A[i][0]-A[j][0], i, j])
        elif A[i][2] == 2:
            for j in range(i+1,N):
                if A[j][2] == 0:
                    if A[i][1]-A[i][0] == A[j][1]-A[j][0] and A[i][0] > A[j][0]:
                        atom.append([A[i][0]-A[j][0], i, j])
                elif A[j][2] == 1:
                    if A[i][0]+A[i][1] == A[j][0]+A[j][1] and A[i][0] > A[j][0]:
                        atom.append([A[i][0]-A[j][0], i, j])
                elif A[j][2] == 3:
                    if A[i][1] == A[j][1] and A[i][0] > A[j][0]:
                        atom.append([(A[i][0]-A[j][0])//2, i, j])
        else:
            for j in range(i+1,N):
                if A[j][2] == 0:
                    if A[i][0]+A[i][1] == A[j][0]+A[j][1] and A[j][0] > A[i][0]:
                        atom.append([A[j][0]-A[i][0], i, j])
                elif A[j][2] == 1:
                    if A[i][1]-A[i][0] == A[j][1]-A[j][0] and A[j][0] > A[i][0]:
                        atom.append([A[j][0]-A[i][0], i, j])
                elif A[j][2] == 2:
                    if A[i][1] == A[j][1] and A[i][0] < A[j][0]:
                        atom.append([(A[j][0]-A[i][0])//2, i, j])

    visited = [0]*N
    atom.sort(); energy = 0
    for i in range(len(atom)):
        if not visited[atom[i][1]] and not visited[atom[i][2]]:
            visited[atom[i][1]] = atom[i][0]
            visited[atom[i][2]] = atom[i][0]
            energy += A[atom[i][1]][3] + A[atom[i][2]][3]
        elif visited[atom[i][1]] and not visited[atom[i][2]]:
            if visited[atom[i][1]] == atom[i][0]:
                energy += A[atom[i][2]][3]
                visited[atom[i][2]] = atom[i][0]
        elif not visited[atom[i][1]] and visited[atom[i][2]]:
            if visited[atom[i][2]] == atom[i][0]:
                energy += A[atom[i][1]][3]
                visited[atom[i][1]] = atom[i][0]

    print(f'#{tc}', energy)