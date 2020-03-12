import sys

sys.stdin = open('1974.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    sdoku = [list(map(int,input().split())) for _ in range(9)]

    result = 1
    for i in range(9):
        row = [False]*10
        column = [False]*10
        for j in range(9):
            row[sdoku[i][j]] = True
            column[sdoku[j][i]] = True
        if sum(row) != 9 or sum(column) != 9:
            result = 0
            break
            
    if result:
        for i in range(0,9,3):
            for j in range(0,9,3):
                rect = [False]*10
                for k in range(3):
                    for l in range(3):
                        rect[sdoku[i+k][j+l]] = True
                if sum(rect) != 9:
                    result = 0
                    break
            if result == 0:
                break

    print(f'#{tc}', result)