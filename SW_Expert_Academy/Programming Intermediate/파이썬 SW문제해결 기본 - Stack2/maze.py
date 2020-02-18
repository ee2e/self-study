import sys

sys.stdin = open('maze.txt', 'r')

T = int(input())

dx_j = [-1, 0, 1, 0]
dy_i = [0, -1, 0, 1]

def DFS(maze,start,visited):
    global flag

    if flag:
        return
        
    visited.append(start)
    i = start[0]; j = start[1]; d = 0

    while d < 4:
        if 0 <= i+dy_i[d] < N and 0 <= j+dx_j[d] < N:
            if maze[i+dy_i[d]][j+dx_j[d]] == 3:
                flag = 1
                return
            if maze[i+dy_i[d]][j+dx_j[d]] == 0:
                if [i+dy_i[d], j+dx_j[d]] not in visited:
                    DFS(maze,[i+dy_i[d], j+dx_j[d]],visited)    
        d += 1
    

for tc in range(T):
    N = int(input())
    maze = [[int(x) for x in input()] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = [i, j]
                break

    flag = 0
    visited = []

    DFS(maze,start,visited)

    print(f'#{tc+1} {flag}')