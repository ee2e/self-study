import sys

sys.stdin = open('number_letters.txt', 'r')

T = int(input())

for tc in range(T):
    str2 = input()
    str1 = input()

    N = len(str1); M = len(str2)

    cnt = 0
    max_val = 0

    for i in range(M):
        for j in range(N):
            if str1[j] == str2[i]:
                cnt += 1

        if cnt > max_val :
            max_val = cnt

        cnt = 0

    print(f'#{tc+1} {max_val}')