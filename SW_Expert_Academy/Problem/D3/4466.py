import sys

sys.stdin = open('4466.txt', 'r')

T = int(input())

for tc in range(T):
    N, K = map(int,input().split())
    scores = list(map(int,input().split()))

    j = len(scores)
    while j > len(scores) - K:
        for i in range(0, j-1):
            if scores[i] > scores[i+1]:
                scores[i], scores[i+1] = scores[i+1], scores[i]
        j -= 1

    print(f'#{tc+1} {sum(scores[-K:])}')