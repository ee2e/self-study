import sys

sys.stdin = open('pasting_paper.txt', 'r')

T = int(input())

def exp(arg):
    if arg == 0 or arg == 1:
        return 1
    else:
        return exp(arg-1) + 2*exp(arg-2)

for tc in range(T):
    N = int(input())
    N = N // 10

    print(f'#{tc+1} {exp(N)}')