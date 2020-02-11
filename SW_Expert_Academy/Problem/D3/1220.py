import sys

sys.stdin = open('1220.txt', 'r')

# 1은 N극 성질 2는 S극 성질
# 위에 N극, 밑에 S극
for tc in range(10):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    result = 0

    flag = True
    for j in range(N):
        for i in range(N):
            if flag:
                if matrix[i][j] == 1:
                    cnt += 1
                    flag = False
            else:
                if matrix[i][j] == 2:
                    cnt += 1
                    flag = True

        result += cnt//2
        cnt = 0
        flag = True

    print(f'#{tc+1} {result}')