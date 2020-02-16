import sys

sys.stdin = open('2805.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    farm = [[int(x) for x in input()] for _ in range(N)]
    
    crops = 0
    o = 1
    for i in range(N//2+1):
        for j in range(N//2-i,N//2-i+o):
            crops += farm[i][j]
        o += 2

    o -= 4
    for i in range(N//2+1,N):
        for j in range(i-N//2,i-N//2+o):
            crops += farm[i][j]
        o -= 2

    print(f'#{tc+1} {crops}')