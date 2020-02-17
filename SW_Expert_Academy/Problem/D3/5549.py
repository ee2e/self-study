import sys

sys.stdin = open('5549.txt', 'r')

T = int(input())

for tc in range(T):
    num = int(input())

    print(f'#{tc+1}', end = ' ')
    if num % 2:
        print('Odd')
    else:
        print('Even')