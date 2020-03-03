import sys

sys.stdin = open('5293.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    A, B, C, D = map(int,input().split())
    length = A + B + C + D + 1

    temp = [0]*length
    flag = 0
    result = []

    def printset():
        global flag, result
        comp = [0]*4
        for i in range(length-1):
            if temp[i] == 0:
                if temp[i+1] == 0:
                    comp[0] += 1
                else:
                    comp[1] += 1
            else:
                if temp[i+1] == 0:
                    comp[2] += 1
                else:
                    comp[3] += 1
        if comp[0] == A and comp[1] == B and comp[2] == C and comp[3] == D:
            flag = 1
            result = ''.join(map(str,temp))

    def subset(n, k):
        global flag
        if flag == 1:
            return
        if n == k:
            printset()
        else:
            temp[k] = 1
            subset(n, k+1)
            temp[k] = 0
            subset(n, k+1)

    subset(length, 0)

    ans = result if flag else 'impossible'

    print(f'#{tc} {ans}')