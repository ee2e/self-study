import sys

sys.stdin = open('1213.txt', 'rt', encoding='UTF8')

for tc in range(10):
    num = int(input())
    str2 = input()
    str1 = input()

    N = len(str1)
    M = len(str2)
    cnt = 0
    result = 0

    for i in range(N-M+1):
        for j in range(M):
            if str1[i+j] == str2[j]:
                cnt += 1
        if cnt == M:
            result += 1
        cnt = 0

    print(f'#{num} {result}')
