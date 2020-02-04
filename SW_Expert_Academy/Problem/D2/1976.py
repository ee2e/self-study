import sys

sys.stdin = open('1976.txt','r')

T = int(input())

for tc in range(T):
    time_list = list(map(int,input().split()))
    hour = minute = 0

    for i in range(len(time_list)):
        if i % 2 == 0:
            hour += time_list[i]
        else:
            minute += time_list[i]

    if minute >= 60:
        hour += minute//60
        minute = minute%60

    if hour > 12:
        m = hour // 12
        hour -= 12*m

    if hour == 0:
        hour = 12

    print(f'#{tc+1} {hour} {minute}')