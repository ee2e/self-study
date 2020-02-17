import sys

sys.stdin = open('3456.txt', 'r')

T = int(input())

for tc in range(T):
    a, b, c = map(int,input().split())

    if a == b:
        result = c
    elif b == c:
        result = a
    elif a == c:
        result = b

    print(f'#{tc+1} {result}')