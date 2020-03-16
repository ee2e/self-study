import sys

sys.stdin = open('3143.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    word1, word2 = input().split()

    result = len(word1) - (len(word2)-1)*word1.count(word2)

    print(f'#{tc}', result)