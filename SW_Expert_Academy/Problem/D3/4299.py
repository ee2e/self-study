import sys

sys.stdin = open('4299.txt', 'r')

T = int(input())

for tc in range(T):
    D, H, M = map(int,input().split())
    
    time = (D*1440 + H*60 + M) - (11*1440 + 11*60 + 11)
    if time < 0:
        time = -1

    print(f'#{tc+1} {time}')