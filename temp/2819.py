import sys

sys.stdin = open('2819.txt', 'r')

T = int(input())

def num(n,k,word,i,j):
    global numbers, MAP
    if k == n:
        numbers.add(word)
    else:
        for d in range(4):
            ni = i + dy_i[d]
            nj = j + dx_j[d]
            if 0 <= ni < 4 and 0 <= nj < 4:
                num(n,k+1,word + str(MAP[ni][nj]),ni,nj)


for tc in range(1,T+1):
    MAP = [list(map(int,input().split())) for _ in range(4)]

    dx_j = [0,1,0,-1]
    dy_i = [-1,0,1,0]

    numbers = set()

    for i in range(4):
        for j in range(4):
            word = str(MAP[i][j])
            num(7,1,word,i,j)
    
    print(f'#{tc}', len(numbers))