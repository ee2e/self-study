N, M = map(int, input().split())

if N > M:
    for i in range(M,N+1):
        print(i, end = ' ')
else:
    for i in range(N,M+1):
        print(i, end = ' ')