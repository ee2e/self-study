import sys

sys.stdin = open('5948.txt', 'r')

T = int(input())

def printSet():
    global data, result
    threesum = 0
    if sum(A) == 3:
        for i in range(7):
            if A[i] == 1:
                threesum += data[i]
        result.append(threesum)

def subset(n, k):
    if sum(A) > 3:
        return
    if n == k:
        printSet()
    else:
        A[k] = 1
        subset(n, k+1)
        A[k] = 0
        subset(n, k+1)


for tc in range(T):
    data = list(map(int,input().split()))

    A = [0]*7
    result = []

    subset(7, 0)

    result = list(set(result))
    result.sort()

    print(f'#{tc+1} {result[-5]}')