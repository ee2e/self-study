import sys

sys.stdin = open('9611.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    YES = []
    NO = []

    for _ in range(N):
        temp = list(input().split())
        if temp[4] == 'YES':
            for i in range(4):
                YES.append(int(temp[i]))
        else:
            for i in range(4):
                NO.append(int(temp[i]))
    
    for i in range(len(NO)):
        if NO[i] in YES:
            for j in range(YES.count(NO[i])):
                YES.remove(NO[i])

    print(f'#{tc} {YES.pop()}')