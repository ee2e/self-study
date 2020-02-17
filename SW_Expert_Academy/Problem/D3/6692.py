import sys

sys.stdin = open('6692.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    data = [[float(x) for x in input().split()] for _ in range(N)]
    pay = 0

    for i in range(N):
        pay += data[i][0] * data[i][1]

    print(f'#{tc+1} {pay}')