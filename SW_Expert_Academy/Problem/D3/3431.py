import sys

sys.stdin = open('3431.txt', 'r')

T = int(input())

for tc in range(T):
    L, U, X = map(int,input().split())

    result = 0

    if X > U:
        result = -1
    elif X < L:
        result = L - X

    print(f'#{tc+1} {result}')