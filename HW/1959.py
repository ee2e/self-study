import sys

sys.stdin = open('1959.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    if N > M:
        N, M = M, N
        A, B = B, A

    maxV = 0
    for i in range(M-N+1):
        sumV = 0
        for j in range(N):
            sumV += A[j]*B[j+i]
        if sumV > maxV:
            maxV = sumV

    print(f'#{tc}', maxV)