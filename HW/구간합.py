import sys

sys.stdin = open('구간합.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))

    minV = 10000*N
    maxV = 1
    for i in range(N-M+1):
        part_sum = 0
        for k in range(M):
            part_sum += arr[i+k]
        if part_sum > maxV:
            maxV = part_sum
        if part_sum < minV:
            minV = part_sum

    print(f'#{tc}', maxV-minV)