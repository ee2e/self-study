import sys

sys.stdin = open('4579.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    word = input()

    flag = 1
    scope = len(word)//2
    for i in range(len(word)):
        if word[i] == word[-1-i]:
            continue
        elif word[i] == '*' or word[-1-i] == '*':
            break
        else:
            flag = 0
            break

    if flag:
        result = 'Exist'
    else:
        result = 'Not exist'

    print(f'#{tc} {result}')