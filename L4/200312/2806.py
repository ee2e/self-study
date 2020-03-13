import sys

sys.stdin = open('2806.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    queen = list(range(0,N))

    cnt = 0
    def perm(n,k):
        global cnt
        if 2 <= k < N and abs(queen[k-1]-queen[k-2]) == 1:
            return
        if n == k:
            for i in range(N):
                for j in range(N):
                    if i != j:
                        if abs(queen[i] - queen[j]) == abs(i-j):
                            return
            cnt += 1
        else:
            for i in range(k,n):
                queen[i], queen[k] = queen[k], queen[i]
                perm(n,k+1)
                queen[i], queen[k] = queen[k], queen[i]
    
    perm(N,0)

    print(f'#{tc}', cnt)