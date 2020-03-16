import sys

sys.stdin = open('4861.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    alphabet = [list(input()) for _ in range(N)]

    K = M//2; word1 = []; word2 = []
    for i in range(N):
        for j in range(N-M+1):
            flag = 1
            for k in range(K):
                if alphabet[i][j+k] != alphabet[i][j+M-1-k] and alphabet[j+k][i] != alphabet[j+M-1-k][i]:
                    flag = 0
                    break
            if flag:
                for l in range(M):
                    word1 += [alphabet[i][j+l]]
                    word2 += [alphabet[j+l][i]]
                break
        if flag:
            break

    if word1 == list(reversed(word1)):
        result = word1
    else:
        result = word2

    print(f'#{tc} {"".join(result)}')