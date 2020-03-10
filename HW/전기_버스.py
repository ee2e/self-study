import sys

sys.stdin = open('전기_버스.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    K, N, M = map(int,input().split())
    num = list(map(int,input().split()))

    i = K
    cnt = com = 0
    while i < N:
        if i in num:
            cnt += 1
            i += K
            com = 0
        else:
            if com < K-1:
                i -= 1
                com += 1
            else:
                cnt = 0
                break

    print(f'#{tc}', cnt)