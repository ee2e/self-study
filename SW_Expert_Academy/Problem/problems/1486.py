import sys

sys.stdin = open('1486.txt', 'r')

def selected(k,height):
    global result
    # N이 20이기 때문에 가지치기 안해줘도 됨
    # if height >= result:
    #     return
    # if height >= B:
    #     result = height
    #     return
    if k == N:
        if B <= height < result:
            result = height
    else:
        selected(k+1,height+H[k])
        selected(k+1,height)

for tc in range(1,int(input())+1):
    N, B = map(int,input().split())
    H = list(map(int,input().split()))

    result = float('inf')
    selected(0,0)

    print(f'#{tc}', result-B)