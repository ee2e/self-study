import sys

sys.stdin = open('4522.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    word = input()
    N = len(word)//2

    flag = 1
    for i in range(N):
        if word[i] != word[-1-i] and (word[i] != '?' and word[-1-i] != '?'):
            flag = 0
            break

    result = 'Exist' if flag else 'Not exist'

    print(f'#{tc}', result)