import sys

sys.stdin = open('4408.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    room = [0]*201
    for _ in range(N):
        temp = list(map(int,input().split()))
        for i in range(2):
            if temp[i] % 2:
                temp[i] = temp[i]//2+1
            else:
                temp[i] //= 2
        for i in range(min(temp),max(temp)+1):
            room[i] += 1
    
    print(f'#{tc}', max(room))