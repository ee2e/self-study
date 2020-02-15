import sys

sys.stdin = open('1215.txt', 'r')

for tc in range(10):
    N = int(input())
    matrix = [[x for x in input()] for _ in range(8)]

    result = 0
    s1 = ''
    s2 = ''

    for i in range(8):
        for j in range(8-N+1):
            for k in range(N):
                s1 += matrix[i][j+k]
                s2 += matrix[j+k][i]

            if s1 == s1[::-1]:
                result += 1

            if s2 == s2[::-1]:
                result += 1

            s1 = ''
            s2 = ''

    print(f'#{tc+1} {result}')