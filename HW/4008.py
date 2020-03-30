import sys

sys.stdin = open('4008.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    operator = list(map(int,input().split()))
    num = list(map(int,input().split()))
    
    minV = 100000000
    maxV = -100000000
    def cal(n, k, sum):
        global minV, maxV
        if operator[0] < 0 or operator[1] < 0 or operator[2] < 0 or operator[3] < 0:
            return
        if (n+1) == k:
            if sum < minV:
                minV = sum
            if sum > maxV:
                maxV = sum 
        else:
            operator[0] -= 1
            cal(n, k+1, sum + num[k])
            operator[0] += 1
            operator[1] -= 1
            cal(n, k+1, sum - num[k])
            operator[1] += 1
            operator[2] -= 1
            cal(n, k+1, sum * num[k])
            operator[2] += 1
            operator[3] -= 1
            if sum < 0:
                cal(n, k+1, -(abs(sum)//num[k]))
            else:
                cal(n, k+1, sum // num[k])
            operator[3] += 1

    cal(N-1, 1, num[0])
    print(f'#{tc} {maxV-minV}')
