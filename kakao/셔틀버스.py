import sys

sys.stdin = open('셔틀버스.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    n, t, m = map(int,input().split())
    timetable = list(input().split())

    # 제일 뒤에 있는 인수부터 계산할 수 있도록 내림차순으로 정렬해준다
    timetable.sort(reverse=True)

    # 계산을 편하게 해주기 위해 HH:MM인 시간 형태를 [HH,MM]으로 각각 시와 분은 정수로 바꿔준다
    for i in range(len(timetable)):
        timetable[i] = [int(timetable[i][:2]), int(timetable[i][3:])]

    # 셔틀버스가 정류장에 도착하는 시간을 bus라는 리스트에 넣어준다
    bus = [[9,0]]
    for _ in range(n-1):
        temp = [bus[-1][0],bus[-1][1]+t]
        if temp[1] >= 60:
            temp[0] += 1
            temp[1] -= 60
        bus.append(temp)
    
    if n == 1:
        if len(timetable) < m:
            result = f'{bus[0][0]:#02}:{bus[0][1]:#02}'
        else: