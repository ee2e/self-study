import sys

sys.stdin = open('5653.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, M, K = map(int,input().split())

    container = [[0]*(300+M) for _ in range(300+N)]
    [list(map(int,input().split())) for _ in range(N)]

    print(container)