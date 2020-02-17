import sys

sys.stdin = open('5601.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())

    print(f'#{tc+1}', end = '')

    for _ in range(N):
        print(f' 1/{N}', end = '')
    print()