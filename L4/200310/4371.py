import sys

sys.stdin = open('4371.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    joy = []
    for _ in range(N):
        joy.append(int(input()))

    cnt = 0
    while len(joy) > 1:
        gap = joy[1]-joy[0]
        day = joy[1]
        while day <= joy[-1]:
            if day in joy:
                joy.remove(day)
            day += gap
        cnt += 1

    print(f'#{tc}', cnt)