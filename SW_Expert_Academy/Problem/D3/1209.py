import sys

sys.stdin = open('1209.txt', 'r')

for tc in range(10):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(100)]
    maximum = 0
    sum_row = 0
    sum_column = 0
    sum_diagonal = 0
    sum_dia_reverse = 0

    for i in range(100):
        sum_diagonal += matrix[i][i]
        sum_dia_reverse += matrix[i][99-i]
        for j in range(100):
            sum_row += matrix[i][j]
            sum_column += matrix[j][i]
        if sum_row > maximum:
            maximum = sum_row
        if sum_column > maximum:
            maximum = sum_column
        sum_row = 0
        sum_column = 0
    if sum_diagonal > maximum:
            maximum = sum_diagonal
    if sum_dia_reverse > maximum:
        maximum = sum_dia_reverse

    print(f'#{N} {maximum}')
