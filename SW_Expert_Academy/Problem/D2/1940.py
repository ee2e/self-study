import sys
sys.stdin = open('1940.txt','r')

T = int(input())

for tc in range(T):
    N = int(input())
    command_list = [list(map(int,input().split())) for _ in range(N)]
    d = 0
    v = 0

    for i in range(N):
        if command_list[i][0] == 0:
            d += v
        else:
            if command_list[i][0] == 1:
                v += command_list[i][1]
                d += v
            elif command_list[i][0] == 2:
                if v < command_list[i][1]:
                    v = 0
                else:
                    v -= command_list[i][1]
                    d += v

    print(f'#{tc+1} {d}')