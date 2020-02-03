import sys
sys.stdin = open('2070.txt', 'r')

T = int(input())

for tc in range(T):
    a, b = map(int,input().split())
    if a == b:
        result = '='
    elif a < b:
        result = '<'
    else:
        result = '>'

    print(f'#{tc+1} {result}')