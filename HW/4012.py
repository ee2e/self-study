import sys

sys.stdin = open('4012.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    S = [list(map(int,input().split())) for _ in range(N)]

    A = [0]*N
    N2 = N//2
    select = []
    select2 = []

    def subset(n, k):
        if sum(A) > N2:
            return
        if n == k:
            index = []
            index2 = []
            if sum(A) == N2:
                for i in range(len(A)):
                    if A[i] == 1:
                        index.append(i)
                    else:
                        index2.append(i)
                select.append(index)
                select2.append(index2)
        else:
            A[k] = 1
            subset(n, k+1)
            A[k] = 0
            subset(n, k+1)

    subset(N, 0)

    A2 = [0]*N2
    ans = 0xffffffff

    def subset2(n, k):
        global result1, result2
        if sum(A2) > 2:
            return
        if n == k:
            idx = []
            idx2 = []
            if sum(A2) == 2:
                for i in range(len(A2)):
                    if A2[i] == 1:
                        idx.append(temp1[i])
                        idx2.append(temp2[i])
                result1 += S[idx[0]][idx[1]] + S[idx[1]][idx[0]]
                result2 += S[idx2[0]][idx2[1]] + S[idx2[1]][idx2[0]]
        else:
            A2[k] = 1
            subset2(n, k+1)
            A2[k] = 0
            subset2(n, k+1)

    for i in range(len(select)):
        result1 = result2 = 0
        temp1 = select[i]
        temp2 = select2[i]
        subset2(N2, 0)
        if abs(result1-result2) < ans:
            ans = abs(result1-result2)

    print(f'#{tc}', ans)