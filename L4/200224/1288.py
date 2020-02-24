import sys

sys.stdin = open('1288.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = n = input()
    N = int(N)
    li = [0]*10
    k = 2

    while li [0] < 1 or li[1] < 1 or li[2] < 1 or li[3] < 1 or li[4] < 1 or li[5] < 1 or li[6] < 1 or li[7] < 1 or li[8] < 1 or li[9] < 1:
        for i in n:
            li[int(i)] += 1
        n = str(N*k)
        k += 1

    print(f'#{tc} {N*(k-2)}')