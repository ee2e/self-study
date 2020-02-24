import sys

sys.stdin = open('5603.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    hay = []

    for i in range(N):
        hay.append(int(input()))

    average = sum(hay)//len(hay)

    value = 0

    for h in hay:
        value += abs(average-h)

    print(f'#{tc+1} {value//2}')