import sys

sys.stdin = open('1217.txt', 'r')

for tc in range(10):
    n = int(input())
    N, M = map(int,input().split())

    def squ(N,M):
        if M == 1:
            return N
        else:
            M -= 1
        return N * squ(N,M)

    print(f'#{n} {squ(N,M)}')