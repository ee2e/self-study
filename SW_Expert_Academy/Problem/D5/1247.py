import sys

sys.stdin = open('1247.txt', 'r')

T = int(input())

def distance(k,last_visit,current_d):
    global minV
    if current_d >= minV:
        return
    if k == N:
        current_d += abs(last_visit[0]-home[0]) + abs(last_visit[1]-home[1])
        if current_d < minV:
            minV = current_d
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                distance(k+1,clients[i],current_d+abs(last_visit[0]-clients[i][0])+abs(last_visit[1]-clients[i][1]))
                visited[i] = False

for tc in range(1,T+1):
    N = int(input())
    coordinates = list(map(int,input().split()))

    company = [coordinates[0],coordinates[1]]
    home = [coordinates[2],coordinates[3]]
    clients = []
    for i in range(2,N+2):
        clients.append([coordinates[2*i],coordinates[2*i+1]])

    minV = 200*(N+1)
    visited = [False]*N

    distance(0,company,0)

    print(f'#{tc}', minV)