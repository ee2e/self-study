import sys

sys.stdin = open('5162.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    A, B, C = map(int,input().split())
    result = 0

    if C % min(A,B) == 0:
        result = C // min(A,B)
    else:
        for i in range(0,C//A):
            for j in range(0,C//B):
                if A*i + B*j <= C:
                    ans = i+j
                    if ans > result:
                        result = ans

    print(f'#{tc}', result)