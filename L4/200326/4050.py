import sys

sys.stdin = open('4050.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    cost = list(map(int,input().split()))

    cost.sort()

    if N >= 3:
        for i in range(N-3,-1,-3):
            cost.pop(i)
    
    print(f'#{tc}', sum(cost))