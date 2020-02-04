import sys
sys.stdin = open('1959.txt','r')

T = int(input())

for tc in range(T):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    sum_list = []
    maximum = []

    if N > M:
        for i in range(N-M+1):
            B0 = [0]*N
            for j in range(M):
                B0[i+j] = B[j]
            for k in range(N):
                sum_list.append(A[k]*B0[k])
            maximum.append(sum(sum_list))
            sum_list = []

    else:
        for i in range(M-N+1):
            A0 = [0]*M
            for j in range(N):
                A0[i+j] = A[j]
            for k in range(M):
                sum_list.append(B[k]*A0[k])
            maximum.append(sum(sum_list))
            sum_list = []
    
    print(f'#{tc+1} {max(maximum)}')