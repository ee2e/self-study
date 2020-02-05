import sys

sys.stdin = open('2005.txt','r')

T = int(input())

for tc in range(T):
    N = int(input())
    result = []

    for i in range(N):
        if i <= 1:
            result.append([1]*(i+1))
        else:
            temp = [0]*(i+1)
            temp[0] = temp[-1] = 1
            for j in range(1,i):
                temp[j] = result[i-1][j-1] + result[i-1][j]
            result.append(temp)
    
    print(f'#{tc+1}')
    for i in range(N):
        print(f'{" ".join(map(str,result[i]))}')