import sys

sys.stdin = open('5431.txt', 'r')

T = int(input())

for tc in range(T):
    N, K = map(int,input().split())
    K_num = list(map(int,input().split()))
    result = []

    for i in range(1,N+1):
        if i not in K_num:
            result.append(i)

    print(f'#{tc+1} {" ".join(map(str,result))}')