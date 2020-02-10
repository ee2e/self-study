import sys

sys.stdin = open('string_comparison.txt', 'r')

T = int(input())

for tc in range(T):
    str1 = input()
    str2 = input()

    N = len(str1)
    M = len(str2)

    if M > N:
        N, M = M, N
        str1, str2 = str2, str1

    leng_cnt = 0
    cnt = 0
    for i in range(N-M+1):
        for j in range(M):
            if str1[i+j] == str2[j]:
                leng_cnt += 1
        if leng_cnt == len(str2):
            cnt = 1
            break
        leng_cnt = 0
    
    print(f'#{tc+1} {cnt}')