import sys

sys.stdin = open('숫자_카드.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    a = input()
    num = [0]*10

    for i in a:
        num[int(i)] += 1

    maxV = idx = 0
    for i in range(10):
        if num[i] >= maxV:
            maxV = num[i]
            idx = i

    print(f'#{tc}', idx, maxV)