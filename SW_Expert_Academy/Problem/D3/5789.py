import sys

sys.stdin = open('5789.txt', 'r')

T = int(input())

for tc in range(T):
    N, Q = map(int,input().split())
    data = [[int(x) for x in input().split()] for _ in range(Q)]

    box = [0]*N

    for i in range(Q):
        for j in range(data[i][0]-1, data[i][1]):
            box[j] = i+1

    print(f'#{tc+1} {" ".join(map(str,box))}')