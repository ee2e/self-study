import sys

sys.stdin = open('1953.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, M, R, C, L = map(int,input().split())
    manhole = [list(map(int,input().split())) for _ in range(N)]

    dx_j = [0,0,-1,1]
    dy_i = [-1,1,0,0]
    visited = []
    def exodus(manhole, R, C, L, k):
        if manhole[R][C] == 0:
            d = []
        elif manhole[R][C] == 1:
            d = [0,1,2,3]
        elif manhole[R][C] == 2:
            d = [0,1]
        elif manhole[R][C] == 3:
            d = [2,3]
        elif manhole[R][C] == 4:
            d = [0,3]
        elif manhole[R][C] == 5:
            d = [1,3]
        elif manhole[R][C] == 6:
            d = [1,2]
        else:
            d = [0,2]

        if k == L-1:
            return
        else:
            for i in range(len(d)):
                if 0 <= R+dy_i[d[i]] < N and 0 <= C+dx_j[d[i]] < N and room[R+dy_i[d[i]]][C+dx_j[d[i]]] != 0:
                    if manhole[R+dy_i[d[i]]][C+dx_j[d[i]]] not in visited:
                        visited.append([R+dy_i[d[i]],C+dx_j[d[i]]])
                        exodus(manhole, R+dy_i[d[i]], C+dx_j[d[i]], L, k+1)

    exodus(manhole, R, C, L, 0)
    print(len(visited))