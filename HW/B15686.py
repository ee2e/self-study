import sys

sys.stdin = open('B15686.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    city = [list(map(int,input().split())) for _ in range(N)]

    house = []
    chicken = []
    street = []

    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                house.append([i,j])
            elif city[i][j] == 2:
                chicken.append([i,j])

    CN = len(chicken)
    combi = [0]*M; minV = 0xffffff
    def solve(k,s):
        global minV
        if k == M:
            minS = 0
            for i in range(len(house)):
                minH = 0xfffff
                for j in range(M):
                    if abs(house[i][0]-chicken[combi[j]][0]) + abs(house[i][1]-chicken[combi[j]][1]) < minH:
                        minH = abs(house[i][0]-chicken[combi[j]][0]) + abs(house[i][1]-chicken[combi[j]][1])
                minS += minH
                if minS > minV:
                    return
            if minS < minV:
                minV = minS
        else:
            for i in range(s, CN-M+k+1):
                combi[k] = i
                solve(k+1,i+1)

    solve(0,0)
    print(minV)



    # def solve(k, s):
    # global ans
    # if k == M:
    #     tsum = 0
    #     for h in range(len(home)):
    #         tmin = 1e9
    #         for c in combi:
    #             t = dist[c][h]
    #         # t = abs(home[h][0] - chicken[c][0]) + abs(home[h][1] - chicken[c][1])
    #             tmin = min(tmin, t)
    #         tsum += tmin
    #     ans = min(ans, tsum)
    # else:
    #     for i in range(s, len(chicken) + (k - M) + 1):
    #         combi[k] = i
    #         solve(k + 1, i + 1)
    # N, M = map(int, input().split())
    # mat = [list(map(int, input().split())) for _ in range(N)]
    # home, chicken = [], []
    # for i in range(N):
    #     for j in range(N):
    #         if mat[i][j] == 1:
    #             home.append((i, j))
    #         elif mat[i][j] == 2:
    #             chicken.append((i, j))

    # dist = [[0] * len(home) for _ in range(len(chicken))]
    # for i in range(len(chicken)):
    #     for j in range(len(home)):
    #         dist[i][j] = abs(chicken[i][0] - home[j][0]) + abs(chicken[i][1] - home[j][1])

    # ans = 1e9
    # combi = [0] * M
    # solve(0, 0)
    # print(ans)