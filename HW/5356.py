import sys

sys.stdin = open('5356.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    words = [input() for _ in range(5)]

    maxV = 0
    for i in range(5):
        if len(words[i]) > maxV:
            maxV = len(words[i])

    word = ''
    for j in range(maxV):
        for i in range(5):
            if j < len(words[i]):
                word += words[i][j]

    print(f'#{tc}', word)