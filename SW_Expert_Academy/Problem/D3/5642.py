import sys

sys.stdin = open('5642.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    num_list = list(map(int,input().split()))
    result = 0
    sum = 0

    for i in range(N):
        for j in range(1,N-i):
            for k in range(j):
                sum += num_list[i+k]
                
            if sum > result:
                result = sum

            sum = 0

    print(f'#{tc+1} {result}')