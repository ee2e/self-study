import sys

sys.stdin = open('1961.txt','r')

T = int(input())

def degree90(arg, N):
    result = [[0]*N for _ in range(N)]   
    for i in range(N):
        for j in range(N):
            result[j][N-1-i] = arg[i][j] 
    return result

def degree180(arg, N):
    result = [[0]*N for _ in range(N)]   
    for i in range(N):
        for j in range(N):
            result[N-1-i][N-1-j] = arg[i][j] 
    return result

def degree270(arg, N):
    result = [[0]*N for _ in range(N)]   
    for i in range(N):
        for j in range(N):
            result[N-1-j][i] = arg[i][j] 
    return result

for tc in range(T):
    N = int(input())
    data_list = [list(map(int,input().split())) for _ in range(N)]

    result90 = degree90(data_list, N)
    result180 = degree180(data_list, N)
    result270 = degree270(data_list, N)
    
    print(f'#{tc+1}')
    for i in range(N):
        print(f'{"".join(map(str,result90[i]))}', end = ' ')
        print(f'{"".join(map(str,result180[i]))}', end = ' ')
        print(f'{"".join(map(str,result270[i]))}')