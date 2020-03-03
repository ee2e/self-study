import sys

sys.stdin = open('1258.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    num = []

    for t in range(N):
        for k in range(N):
            flag = 0
            if data[t][k] != 0:
                i = t; j = k
                flag = 1
            if flag:
                flag2 = 0
                while i < N:
                    while j < N:
                        start_i = i
                        start_j = j
                        while data[i][j+1] != 0:
                            j += 1
                        end_j = j
                        flag2 = 1
                        break
                    if flag2:
                        while data[i+1][end_j] != 0:
                            i += 1
                        end_i = i
                        break
                    else:
                        i += 1             
                num.append([end_i+1-start_i,end_j+1-start_j])
                for i in range(start_i,end_i+1):
                    for j in range(start_j,end_j+1):
                        data[i][j] = 0

    order = []
    for i in range(len(num)):
        order.append(num[i][0]*num[i][1])

    result = []
    while len(num) != 0:
        order_min = 0xfffffff
        order_idx = 0
        for idx, val in enumerate(order):
            if val < order_min :
                order_idx = idx
                order_min = val
            if val == order_min :
                if num[idx][0] <= num[order_idx][0]:
                    order_idx = idx
        result.append(num[order_idx])
        num.pop(order_idx)
        order.pop(order_idx)

    print(f'#{tc} {len(result)}', end = '')
    for i in range(len(result)-1):
        print(f' {result[i][0]} {result[i][1]}', end = '')
    print(f' {result[-1][0]} {result[-1][1]}')