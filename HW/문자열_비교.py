import sys

sys.stdin = open('문자열_비교.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    str1 = input()
    str2 = input()

    result = 0
    if str1 in str2:
        result = 1

    print(f'#{tc}', result)