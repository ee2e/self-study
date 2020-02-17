import sys

sys.stdin = open('5162.txt', 'r')

T = int(input())

for tc in range(T):
    A, B, C = map(int,input().split())

    x = 0; y = 0
    maximum = C // min(A, B) + 1
    minimum = C // max(A, B)
    result = maximum
    for x in range(minimum, maximum):
        for y in range(minimum, maximum):
            if A*x + B*y <= C:
                if A*x+B*y > result:
                    result = x+y+1


    print(f'#{tc+1} {result-1}')