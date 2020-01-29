import sys
sys.stdin = open('전기버스.txt', 'r')

T = int(input())

for tc in range(T):
    K, N, M = map(int,input().split())
    data = list(map(int,input().split()))
    bus = 0
    a = 0
    result = 0

    while bus+K < N:
        if a == K:
            result = 0
            break
        elif bus+K-a in data:
            result += 1
            bus = bus+K-a
            a = 0
        else:
            a += 1

    print('#{} {}'.format(tc+1,result))
