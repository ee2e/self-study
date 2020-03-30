import sys

sys.stdin = open('4881.txt', 'r')

T = int(input())

def perm(arr,n,k,sum):
    global minV, data
    if sum >= minV:
        return
    if k == n:
        if sum < minV:
            minV = sum
    else:
        for i in range(k,n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(arr,n,k+1,sum+data[k][arr[k]])
            arr[k], arr[i] = arr[i], arr[k]

for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]

    arr = list(range(0,N))
    minV = 10*N

    perm(arr,N,0,0)
    print(f'#{tc}', minV)