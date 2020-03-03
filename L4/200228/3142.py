import sys

sys.stdin = open('3142.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())

    twinhorn = N-M
    unicorn = M-twinhorn

    print(f'#{tc} {unicorn} {twinhorn}')