import sys

sys.stdin = open('5688.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    N = N**(1/3)

    if abs(N - round(N)) < 0.1**5:
        N = round(N)
    else:
        N = -1

    print(f'#{tc} {N}')