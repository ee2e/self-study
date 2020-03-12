import sys

sys.stdin = open('3349.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    W, H, N = map(int,input().split())
    visit = [list(map(int,input().split())) for _ in range(N)]

    result = 0
    for i in range(N-1):
        val = [visit[i+1][0]-visit[i][0],visit[i+1][1]-visit[i][1]]
        if val[0]*val[1] > 0:
            val = [abs(val[0]),abs(val[1])]
            result += max(val)
        else:
            result += max(val)-min(val)

    print(f'#{tc}', result)