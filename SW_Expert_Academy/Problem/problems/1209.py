import sys

sys.stdin = open('1209.txt', 'r')

T = 10

for tc in range(1,T+1):
    N = int(input())
    array = [list(map(int,input().split())) for _ in range(100)]

    maxV = 0

    diagonalleft = diagonaright = 0
    for i in range(100):
        rowsum = columnsum = 0
        for j in range(100):
            rowsum += array[i][j]
            columnsum += array[j][i]
        if rowsum > maxV:
            maxV = rowsum
        if columnsum > maxV:
            maxV = columnsum
        diagonalleft += array[i][i]
        diagonaright += array[i][99-i]
    
    if diagonalleft > maxV:
        maxV = diagonalleft
    if diagonaright > maxV:
        maxV = diagonaright

    print(f'#{tc}', maxV)