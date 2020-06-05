import sys

sys.stdin = open('1251.txt', 'r')

from heapq import heappush, heappop

for tc in range(1,int(input())+1):
    N = int(input())
    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))
    E = float(input())
    
    INF = float('inf')
    key = [INF]*N
    mst = [False]*N
    pq = []

    key[0] = 0

    heappush(pq,(0,0))
    minV = 0
    while pq:
        k, node = heappop(pq)
        
        if mst[node]: continue

        mst[node] = True
        minV += k

        for i in range(N):
            if i == node: continue
            wt = (X[node]-X[i])**2 + (Y[node]-Y[i])**2
            if not mst[i] and key[i] > wt:
                key[i] = wt
                heappush(pq,(key[i], i))

    print(f'#{tc}', round(E*minV))