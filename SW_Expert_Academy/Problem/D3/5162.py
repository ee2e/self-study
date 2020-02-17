import sys

sys.stdin = open('5162.txt', 'r')

T = int(input())

for tc in range(T):
    A, B, C = map(int,input().split())

    maximum = C // min(A, B)
    if C % min(A, B) == 0:
        pass
    else:
        flag = 0
        for x in range(maximum-1, 0, -1):
            for y in range(maximum-1, 0, -1):
                if x+y < maximum:
                    flag = 1
                    break
                if A*x + B*y <= C:
                    if A*x+B*y > maximum:
                        maximum = x+y
            if flag:
                break

    print(f'#{tc+1} {maximum}')