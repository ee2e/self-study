import sys

sys.stdin = open('4613.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split()) # N * M
    flag = [input() for _ in range(N)]

    minV = 2500; result = 0
    result += 2*M - flag[0].count('W') - flag[-1].count('R')

    def search(n, k, cnt, check, check2):
        global minV
        if cnt >= minV:
            return
        if k == n-1:
            if cnt < minV and check == 1:
                minV = cnt
        else:
            if check2 <= 1:
                search(n, k+1, cnt+M-flag[k].count('W'), check,1)
            if check2 <= 2:
                search(n, k+1, cnt+M-flag[k].count('B'), 1,2)
            search(n, k+1, cnt+M-flag[k].count('R'), check,3)
    
    search(N,1,result,0,0)
    
    print(f'#{tc}', minV)