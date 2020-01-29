import sys
sys.stdin = open('min_max.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    data = list(map(int,input().split()))
    
    for j in range(N-1,0,-1):
        for i in range(N-1):
            if data[i] > data[i+1]:
                data[i],data[i+1] = data[i+1],data[i]
    
    ans = data[-1] - data[0]

    print('#{} {}'.format(tc+1,ans))