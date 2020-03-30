import sys

sys.stdin = open('1952.txt', 'r')

T = int(input())

def charge(money,k):
    global plan, minV, d, m, tm
    if minV <= money or k > 15:
        return
    if k >= 12:
        if money < minV:
            minV = money
    else:
        charge(money+min(m,plan[k]*d),k+1)
        charge(money+tm,k+3)


for tc in range(1,T+1):
    d, m, tm, y = map(int,input().split())
    plan = list(map(int,input().split()))

    minV = y

    charge(0,0)

    print(f'#{tc} {minV}')