import sys

sys.stdin = open('1244.txt', 'r')

def search(L,cnt):
    global price, result
    if cnt == N:
        if int(''.join(price)) > int(result):
            result = ''.join(price)
    else:
        for i in range(L-1):
            for j in range(i+1,L):
                if i == j: continue
                price[i], price[j] = price[j], price[i]
                now = ''.join(price)
                if now not in check[cnt]:
                    check[cnt].append(now)
                    search(L,cnt+1)
                if result == maxV_price:
                    return
                price[i], price[j] = price[j], price[i]

T = int(input())

for tc in range(1,T+1):
    p, N = map(int,input().split())

    price = [x for x in str(p)]
    maxV_price = ''.join(sorted(price, reverse=True))
    result = 0

    check = [[] for _ in range(N)]

    search(len(price),0)

    print(f'#{tc}', result)