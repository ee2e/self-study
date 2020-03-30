import sys

sys.stdin = open('4008.txt', 'r')

T = int(input())

def cal(n,k,sum):
    global minV, maxV, operator
    if operator[0] < 0 or operator[1] < 0 or operator[2] < 0 or operator[3] < 0:
        return
    if k == n:
        if sum < minV:
            minV = sum
        if sum > maxV:
            maxV = sum
    else:
        operator[0] -= 1
        cal(n,k+1,sum+number[k])
        operator[0] += 1
        operator[1] -= 1
        cal(n,k+1,sum-number[k])
        operator[1] += 1
        operator[2] -= 1
        cal(n,k+1,sum*number[k])
        operator[2] += 1
        operator[3] -= 1
        if sum < 0:
            cal(n,k+1,-(abs(sum)//number[k]))
        else:
            cal(n,k+1,sum//number[k])
        operator[3] += 1

for tc in range(1,T+1):
    N = int(input())
    operator = list(map(int,input().split()))
    number = list(map(int,input().split()))
    
    minV = 100000000; maxV = -100000000

    cal(N,1,number[0])

    print(f'#{tc} {maxV-minV}')