import sys
sys.stdin = open('1948.txt','r')

T = int(input())

month_day = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

for tc in range(T):
    data = list(map(int,input().split()))
    result = 0

    if data[0] == data[2]:
        result = data[3] - data[1] + 1
    elif data[0] - data[2] == 1:
        result += month_day[data[0]] - data[1] + 1 + data[3]
    else:
        result += month_day[data[0]] - data[1] + 1 + data[3]
        for i in range(data[0]+1,data[2]):
            result += month_day[i]

    print(f'#{tc+1} {result}')