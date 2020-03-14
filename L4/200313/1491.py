import sys

sys.stdin = open('1491.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, A, B = map(int,input().split())

    minV = 0xfffffff
    for R in range(1,N):
        for C in range(1,N-R+1):
            if R*C > N:
                break
            result = A*abs(R-C)+B*(N-R*C)
            if result < minV:
                minV = result

    print(f'#{tc}', minV)