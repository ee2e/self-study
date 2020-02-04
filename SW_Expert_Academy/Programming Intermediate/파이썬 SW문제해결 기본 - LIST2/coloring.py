import sys

sys.stdin = open('coloring.txt','r')

T = int(input())

for tc in range(T):
    N = int(input())
    color_list = [list(map(int,input().split())) for _ in range(N)]
    
    domain = [[0]*10 for _ in range(10)]

    for k in range(N):
        for i in range(color_list[k][0],color_list[k][2]+1):
            for j in range(color_list[k][1],color_list[k][3]+1):
                domain[i][j] += color_list[k][4]
    
    sum = 0
    for i in range(10):
        sum += domain[i].count(3)

    print(f'#{tc+1} {sum}')
