import sys

sys.stdin = open('4522.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    s = [x for x in input()]
    t = list(reversed(s))
    for i in range(len(s)):
        if s[i] == t[i] or s[i] == '?' or t[i] == '?':
            pass
        else:
            result = 'Not exist'
            break
        result = 'Exist'

    print(f'#{tc} {result}')