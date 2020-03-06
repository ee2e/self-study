import sys

sys.stdin = open('1233.txt', 'r')

T = 10

for tc in range(1,T+1):
    N = int(input())
    data = []
    for i in range(N):
        data.append(list(input().split()))

    result = 1
    for i in range(N-1,-1,-1):
        if len(data[i]) == 2:
            if data[i][1].isdecimal() == False:
                result = 0
                break
        else:
            if data[i][1].isdecimal() == True:
                result = 0
                break

    print(f'#{tc}', result)