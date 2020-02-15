import sys

sys.stdin = open('1234.txt', 'r')

for tc in range(10):
    N, S = input().split()
    N = int(N)

    flag = [0,0]
    while flag[1] == 0:
        flag = [0,0]
        for i in range(len(S)-1):
            j = i+1
            while 0 <= i < len(S) and 0 <= j < len(S) and S[i] == S[j]:
                i -= 1
                j += 1
                flag[0] = 1
            
            if flag[0]:
                S = S[:i+1] + S[j:]
                break
            
        if flag[0] == 0:
            flag[1] = 1
    print(f'#{tc+1} {S}')


