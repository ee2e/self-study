import sys

sys.stdin = open('5521.txt', 'r')

from collections import deque

for tc in range(1,int(input())+1):
    N, M = map(int,input().split())

    friends = {i:[] for i in range(1,N+1)}
    for _ in range(M):
        a, b = map(int,input().split())
        friends[a].append(b)
        friends[b].append(a)

    Q = deque([(1,0)])

    visited = [False]*(N+1); cnt = 0
    visited[1] = True
    while Q:
        friend, time = Q.popleft()
        if time == 3:
            break  
        cnt += 1
        for val in friends[friend]:
            if not visited[val]:
                visited[val] = True
                Q.append((val, time+1))

    print(f'#{tc}', cnt-1)