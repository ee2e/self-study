import sys

sys.stdin = open('6190.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    numlist = []

    result = -1
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if i == j:
                continue
            else:
                num = str(arr[i]*arr[j])
                flag = 1
                for k in range(len(num)-1):
                    if num[k] > num[k+1]:
                        flag = 0
                        break
                if flag:
                    if int(num) > result:
                        result = int(num)
    
    print(f'#{tc}', result)