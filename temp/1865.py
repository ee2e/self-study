import sys

sys.stdin = open('1865.txt', 'r')

T = int(input())

def manage(data,n,k,sum):
    global maxV
    if sum <= maxV:
        return
    if n == k:
        if sum > maxV:
            maxV = sum
    else:
        for i in range(k,n):
            data[k], data[i] = data[i], data[k]
            manage(data,n,k+1,sum*staff[k][data[k]]*0.01)
            data[k], data[i] = data[i], data[k]

for tc in range(1,T+1):
    N = int(input())
    staff = [list(map(int,input().split())) for _ in range(N)]
    data = list(range(0,N))

    maxV = 0
    manage(data,N,0,1)

    print(f'#{tc} {maxV*100:.6f}')