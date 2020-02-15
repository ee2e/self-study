import sys

sys.stdin = open('palindrome.txt', 'r')

T = int(input())

for tc in range(T):
    N, M = map(int,input().split())
    str_list = []
    
    for _ in range(N):
        str_list.append(input())

    result = ''

    for s in str_list:
        for i in range(N-M+1):
            word = s[i:i+M]
            if  word == word[::-1]:
                result = word

    s = ''
    flag = False
    for j in range(N):
    
        if result:
            break

        for i in range(N-M+1):
            for k in range(M):
                s += str_list[i+k][j]

            if  s == s[::-1]:
                result = s
                flag = True
                break
            s = ''

        if flag:
            break
    
    print(f'#{tc+1} {result}')