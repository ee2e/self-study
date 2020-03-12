import sys

sys.stdin = open('3376.txt', 'r')

T = int(input())

maxV = 101
P = [0]*maxV

for i in range(1,maxV):
    if i <= 3:
        P[i] = 1
    elif i <= 5:
        P[i] = 2
    else:
        P[i] = P[i-1] + P[i-5]

for tc in range(1,T+1):
    N = int(input())

    print(f'#{tc}', P[N])