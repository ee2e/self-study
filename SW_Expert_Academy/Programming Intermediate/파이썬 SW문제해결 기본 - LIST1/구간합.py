import sys
sys.stdin = open('구간합.txt', 'r')

T = int(input())

for tc in range(T):
    N, M = map(int,input().split())
    data = list(map(int,input().split()))
    total = 0
    total_list = []

    for i in range(N-M+1):
        for j in range(i,i+M):
            total += data[j]
        total_list.append(total)
        total = 0
    
    for j in range(len(total_list)-1,0,-1):
        for i in range(len(total_list)-1):
            if total_list[i] > total_list[i+1]:
                total_list[i], total_list[i+1] = total_list[i+1], total_list[i]

    ans = total_list[-1] - total_list[0]

    print('#{} {}'.format(tc+1, ans))