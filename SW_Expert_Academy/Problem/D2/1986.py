import sys

sys.stdin = open('1986.txt','r')

T = int(input())

for tc in range(T):
    N = int(input())
    result = 0

    for i in range(1,N+1):
        if i % 2:
            result += i
        else:
            result -= i

    print(f'#{tc+1} {result}')