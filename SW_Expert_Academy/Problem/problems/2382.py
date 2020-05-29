import sys

sys.stdin = open('2382.txt', 'r')

from collections import deque

dj = [0,0,0,-1,1]
di = [0,-1,1,0,0]

for tc in range(1,int(input())+1):
    N, M, K = map(int,input().split())

    cluster = deque([])
    for _ in range(K):
        i, j, microbe, move = map(int,input().split())
        cluster.append([i,j,microbe,move])

    t = 0; result = 0; check2 = {}
    while t < M:
        check = {}
        cluster_length = len(cluster)
        for _ in range(cluster_length):
            microbe = cluster.popleft()
            ni = microbe[0] + di[microbe[3]]
            nj = microbe[1] + dj[microbe[3]]
            if ni == 0 or ni == (N-1) or nj == 0 or nj == (N-1):
                microbe[2] //= 2
                if microbe[3]&1:
                    microbe[3] += 1
                else:
                    microbe[3] -= 1
            if check.get((ni,nj)):
                check[(ni,nj)].append((microbe[2],microbe[3]))
            else:
                check[(ni,nj)] = [(microbe[2],microbe[3])]

        for key, value in check.items():
            if len(value) > 1:
                sumV = 0; maxV = 0; maxM = 0
                for val in value:
                    sumV += val[0]
                    if val[0] > maxV:
                        maxV = val[0]
                        maxM = val[1]
                cluster.append([key[0],key[1],sumV,maxM])
            else:
                cluster.append([key[0],key[1],value[0][0],value[0][1]])
        t += 1

    while cluster:
        result += cluster.pop()[2]

    print(f'#{tc}', result)