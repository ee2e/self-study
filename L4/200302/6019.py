import sys

sys.stdin = open('6019.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    D, A, B, F = map(int,input().split())

    time = D / (A+B)

    print(f'#{tc} {time*F}')