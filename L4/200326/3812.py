import sys

sys.stdin = open('3812.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    X, Y, Z, A, B, C, N = map(int,input().split())

    if N == 1:
        mod = [X*Y*Z]
    else:
        mod = [0]*N
        for x in range(X):
            for y in range(Y):
                for z in range(Z):
                    mod[(abs(x-A)+abs(y-B)+abs(z-C))%N] += 1

    print(f'#{tc}', *mod)