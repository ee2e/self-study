import sys

sys.stdin = open('3142.txt', 'r')

T = int(input())

for tc in range(T):
    N, M = map(int,input().split())

    twinhorn = N - M
    unicorn = M - twinhorn

    print(f'#{tc+1} {unicorn} {twinhorn}')