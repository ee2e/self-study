import sys

sys.stdin = open('1952.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    d, m, tm, y = map(int,input().split())
    plan = list(map(int,input().split()))

    result = y

    def cost(i, sum):
        global result
        if sum > result:
            return

        if i > 11:
            if sum < result:
                result = sum
        else:
            cost(i+1, sum + min(d*plan[i], m))
            cost(i+3, sum + tm)

    cost(0, 0)

    print(f'#{tc} {result}')