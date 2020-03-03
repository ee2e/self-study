import sys

sys.stdin = open('1486.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, B = map(int,input().split())
    H = list(map(int,input().split()))
    top_list = []
    result = 0xffffffff

    A = [0]*len(H)
    def printset():
        global result
        top = 0
        for i in range(len(A)):
            if A[i] == 1:
                top += H[i]
        if top >= B and top < result:
            result = top
        

    def subset(n, k):
        if n == k:
            printset()
        else:
            A[k] = 1
            subset(n, k+1)
            A[k] = 0
            subset(n, k+1)

    subset(len(H), 0)

    print(f'#{tc} {result-B}')