import sys

sys.stdin = open('1860.txt', 'r')

T = int(input())

for tc in range(T):
    N, M, K = map(int,input().split())
    data = list(map(int,input().split()))

    t = M-1; n = 0
    result = 'Possible'

    while 0 < len(data):
        num = 0
        idx = []
        for i in range(len(data)):
            if data[i] <= t:
                num += 1
                idx.append(i)
        if num > n:
            result = 'Impossible'
            break
        else:
            for i in range(len(idx)-1,-1,-1):
                data.pop(idx[i])
        t += M; n += K-num
        

    print(f'#{tc+1} {result}')