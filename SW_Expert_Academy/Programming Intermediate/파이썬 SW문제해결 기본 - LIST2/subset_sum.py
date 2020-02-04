import sys

sys.stdin = open('subset_sum.txt','r')

T = int(input())

for tc in range(T):
    N, K = map(int,input().split())

    A = [1,2,3,4,5,6,7,8,9,10,11,12]
    subset_list = []
    subset = []
    for i in range(1<<len(A)):
        for j in range(len(A)):
            if i & (1<<j):
                subset.append(A[j])
        subset_list.append(subset)
        subset = []

    result = 0
    for i in range(2**len(A)):
        if N == len(subset_list[i]) and K == sum(subset_list[i]):
            result += 1

    print(f'#{tc+1} {result}')