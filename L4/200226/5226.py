import sys

sys.stdin = open('5226.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, L = map(int,input().split())
    T = []; K = []
    for _ in range(N):
        t, k = map(int,input().split())
        T.append(t); K.append(k)

    A = [0]*N
    result = 0

    def printset(n, sum):
        global result
        score = 0
        for i in range(len(A)):
            if A[i] == 1:
                score += T[i]
        if score > result:
            result = score

    def subset(n, k, sum):
        if sum > L:
            return
        if n == k:
            printset(n, sum)
        else:
            A[k] = 1
            subset(n, k+1, sum + K[k])
            A[k] = 0
            subset(n, k+1, sum)

    subset(N, 0, 0)

    print(f'#{tc} {result}')