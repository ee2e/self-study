# import sys

# sys.stdin = open('2819.txt', 'r')

# T = int(input())

# for tc in range(1,T+1):
#     data = [list(input().split()) for _ in range(4)]

#     dx_j = [1,0,-1,0]
#     dy_i = [0,1,0,-1]

#     numbers = []

#     def num(k, start):
#         global number
#         if k == 6:
#             if number not in numbers:
#                 numbers.append(number)
#         else:
#             d = 0
#             while d < 4:
#                 ni = start[0] + dy_i[d]
#                 nj = start[1] + dx_j[d]
#                 if 0 <= ni < 4 and 0 <= nj < 4:
#                     number += data[ni][nj]
#                     num(k+1,[ni, nj])
#                     number = number[:-1]
#                 d += 1

#     for i in range(4):
#         for j in range(4):
#             number = data[i][j]
#             num(0, [i,j])

#     print(f'#{tc} {len(numbers)}')




import sys
sys.stdin = open('2819.txt', 'r')

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(A, B, ans, cnt):
    if cnt == 6:
        if ans not in line:
            line.append(ans)
            return
    else:
        for k in range(4):
            new_i = A + di[k]
            new_j = B + dj[k]
            if 0 <= new_i < 4 and 0 <= new_j < 4:
                dfs(new_i, new_j, ans + data[new_i][new_j], cnt + 1)

T = int(input())

for tc in range(T):
    data = [[x for x in map(str, input().split())] for _ in range(4)]
    line = []
    for i in range(4):
        for j in range(4):
            dfs(i, j, data[i][j], 0)
    print("#{} {}".format(tc+1, len(line)))