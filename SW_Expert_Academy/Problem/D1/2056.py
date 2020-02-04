import sys

sys.stdin = open('2056.txt','r')

T = int(input())

for tc in range(T):
    date = input()
    if not 1 <= int(date[4:6]) <= 12:
        result = '-1'
    elif int(date[4:6]) == 1 or int(date[4:6]) == 3 or int(date[4:6]) == 5 or int(date[4:6]) == 7 or int(date[4:6]) == 8 or int(date[4:6]) == 10 or int(date[4:6]) == 12:
        if not 1 <= int(date[6:]) <= 31:
            result = '-1'
        else:
            result = f'{date[0:4]}/{date[4:6]}/{date[6:]}'
    elif int(date[4:6]) == 2:
        if not 1 <= int(date[6:]) <= 28:
            result = '-1'
        else:
            result = f'{date[0:4]}/{date[4:6]}/{date[6:]}'
    elif int(date[4:6]) == 4 or int(date[4:6]) == 6 or int(date[4:6]) == 9 or int(date[4:6]) == 11:
        if not 1 <= int(date[6:]) <= 30:
            result = '-1'
        else:
            result = f'{date[0:4]}/{date[4:6]}/{date[6:]}'
    print(f'#{tc+1} {result}')