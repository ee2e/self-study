import sys

sys.stdin = open('1865.txt', 'r')

# T = int(input())

# for tc in range(1,T+1):
#     N = int(input())
#     P = [list(map(int,input().split())) for _ in range(N)]

#     arr = list(range(N))     

#     def perm(n, k, sum):
#         global result
#         if sum <= result:
#             return
#         if n == k:
#             if sum > result:
#                 result = sum
#         else:
#             for i in range(k, n):
#                 arr[k], arr[i] = arr[i], arr[k]
#                 perm(n, k+1, sum*P[k][arr[k]]*0.01)
#                 arr[k], arr[i] = arr[i], arr[k]

#     result = 0
#     perm(N, 0, 1)

#     print(f'#{tc} {result*100:.6f}')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    P = [list(map(int,input().split())) for _ in range(N)]

    V = [0]*N
    minV = 0

    def work(k, sum):
        global minV
        if sum <= minV:
            return
        if k == N:
            if sum > minV:
                minV = sum
        else:
            for i in range(N):
                if V[i] == 0:
                    V[i] = 1
                    work(k+1, sum * P[k][i] * 0.01)
                    V[i] = 0

    work(0, 1)

    print(f'#{tc} {minV*100:.6f}')