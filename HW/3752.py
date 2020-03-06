import sys

sys.stdin = open('3752.txt', 'r')

T = int(input())

# for tc in range(1,T+1):
#     N = int(input())
#     scores = list(map(int,input().split()))

#     result = []

#     def subset(N, k, sum):
#         if N == k:
#             if sum not in result:
#                 result.append(sum)
#         else:
#             subset(N, k+1, sum+scores[k])
#             subset(N, k+1, sum)

#     subset(N, 0, 0)
#     print(f'#{tc}', len(result))



# for tc in range(1, T+1):
#     N = int(input())
#     scores = list(map(int,input().split()))

#     result = []
#     for i in range(2**N):
#         score = 0
#         for j in range(N):
#             if (i & (1<<j)) != 0:
#                 score += scores[j]
#         if score not in result:
#             result.append(score)

#     print(f'#{tc}', len(result))


for tc in range(1,T+1):
    N = int(input())
    score = list(map(int,input().split()))

    max_score = sum(score)
    temp = [False] * (max_score+1)
    temp[0] = True

    for i in score:
        for j in range(len(temp)-1,-1,-1):
            if temp[j]:
                temp[i+j] = True

    print(f'#{tc} {sum(temp)}')