import sys
sys.stdin = open('1946.txt','r')

T = int(input())

for tc in range(T):
    N = int(input())
    alpha = [list(map(str,input().split())) for _ in range(N)]

    s = ''

    for i in range(len(alpha)):
        s += alpha[i][0] * int(alpha[i][1])

    quotient = len(s) // 10

    result = []

    if quotient == 0:
        result.append(s)
    else:
        for i in range(quotient):
            result.append(s[0+10*i:10+10*i])
        result.append(s[10*quotient:])

    ss = '\n'.join(result)

    print(f'#{tc+1}')
    print(f'{ss}')