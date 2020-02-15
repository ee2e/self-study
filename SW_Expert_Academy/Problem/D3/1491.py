import sys

sys.stdin = open('1491.txt', 'r')

T = int(input())

for tc in range(T):
    N, A, B = map(int,input().split())
 
    R = C = int(N**0.5)

    while N - R*C >= R or N - R*C >= C:
        if N - R*C >= R:
            R += 1
        if N - R*C >= C:
            C += 1

    result = A*abs(R-C)+B*(N-R*C)
    print(result)