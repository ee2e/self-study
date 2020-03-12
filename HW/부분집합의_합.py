import sys

sys.stdin = open('부분집합의_합.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, K = map(int,input().split())

    A = list(range(1,13))

    temp = [0]*12; result = 0
    def subset(n,k,sumV):
        global result
        if sumV > K:
            return
        if n == k:
            if sum(temp) == N and sumV == K:
                result += 1
        else:
            temp[k] = 1
            subset(n,k+1,sumV+A[k])
            temp[k] = 0
            subset(n,k+1,sumV)

    subset(12,0,0)
    print(f'#{tc}', result)