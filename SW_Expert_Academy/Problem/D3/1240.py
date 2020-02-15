import sys

sys.stdin = open('1240.txt', 'r')

T = int(input())

for tc in range(T):
    N, M = map(int,input().split())
    data_list = []
    for _ in range(N):
        data = input()
        data_list.append(list(data))

    code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

    i_idx = []
    for i in range(N):
        for j in range(M-1,-1,-1):
            if data_list[i][j] == '1':
                i_idx = i
                start_j = j-55
                break

    data = ''
    num_list = []
    for j in range(start_j,start_j+55,7):
        for k in range(7):
            data += data_list[i_idx][j+k]
        
        num_list.append(code.index(data))
        data = ''

    odd = []
    even = []
    for i in range(len(num_list)-1):
        if i % 2 == 0:
            odd.append(num_list[i])
        else:
            even.append(num_list[i])

    num = sum(odd)*3 + sum(even) + num_list[-1]

    if num % 10 == 0:
        result = sum(odd) + sum(even) + num_list[-1]
    else:
        result = 0

    print(f'#{tc+1} {result}')
        
    
