import sys

sys.stdin = open('1979.txt','r')

T = int(input())

for tc in range(T):
    N, K = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    length_list = [0] * (N+1)

    for i in range(N):
        for j in range(N):
            if data[i][j] == 1 :
                if i != 0 and j != 0:
                    if data[i-1][j] == 0:
                        length = 0
                        for k in range(i,N):
                            if data[k][j] == 1 :
                                length += 1
                            else:
                                break
                        length_list[length] += 1
                    if data[i][j-1] == 0:
                        length = 0
                        for k in range(j,N):
                            if data[i][k] == 1 :
                                length += 1
                            else:
                                break
                        length_list[length] += 1
                elif i != 0 and j == 0:
                    if data[i-1][j] == 0:
                        length = 0
                        for k in range(i,N):
                            if data[k][j] == 1 :
                                length += 1
                            else:
                                break
                        length_list[length] += 1
                    length = 0
                    for k in range(j,N):
                        if data[i][k] == 1 :
                            length += 1
                        else:
                            break
                    length_list[length] += 1
                elif i == 0 and j != 0:
                    if data[i][j-1] == 0:
                        length = 0
                        for k in range(j,N):
                            if data[i][k] == 1 :
                                length += 1
                            else:
                                break
                        length_list[length] += 1
                    length = 0
                    for k in range(i,N):
                        if data[k][j] == 1 :
                            length += 1
                        else:
                            break
                    length_list[length] += 1
                else:
                    length = 0
                    for k in range(j,N):
                        if data[i][k] == 1 :
                            length += 1
                        else:
                            break
                    length_list[length] += 1
                    length = 0
                    for k in range(i,N):
                        if data[k][j] == 1 :
                            length += 1
                        else:
                            break
                    length_list[length] += 1

    print(f'#{tc+1} {length_list[K]}')