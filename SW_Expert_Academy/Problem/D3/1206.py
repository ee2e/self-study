import sys

sys.stdin = open('1206.txt', 'r')

for tc in range(10):
    N = int(input())
    household = list(map(int,input().split()))

    result = 0
    view_sum = 0
    max_val = 0
    for i in range(2,N-1):
        for j in range(-2,3):
            if household[i] >= household[i+j]:
                if j != 0 and household[i+j] > max_val:
                    max_val = household[i+j]
                flag = True
            else:
                max_val = 0
                flag = False
                break

        if flag:
            result += household[i] - max_val
            max_val = 0

    print(f'#{tc+1} {result}')