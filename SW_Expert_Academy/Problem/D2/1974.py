import sys

sys.stdin = open('1974.txt','r')

T = int(input())

for tc in range(T):
    sudoku_list = [list(map(int,input().split())) for _ in range(9)]
    row_sum = 0 # 행
    column_sum = 0 # 열
    squares_sum = 0
    result = 1

    for i in range(9):
        for j in range(9):
            row_sum += sudoku_list[i][j]
            column_sum += sudoku_list[j][i]

        if row_sum != 45 or column_sum != 45:
            result = 0
            break

        row_sum = 0
        column_sum = 0

    for i in range(0,9,3):
        for j in range(0,9,3):
            for k in range(3):
                squares_sum += sudoku_list[i][j+k]
                squares_sum += sudoku_list[i+1][j+k]
                squares_sum += sudoku_list[i+2][j+k]
        
            if squares_sum != 45:
                result = 0
                break

            squares_sum = 0

    print(f'#{tc+1} {result}')
