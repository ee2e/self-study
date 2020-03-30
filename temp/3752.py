import sys

sys.stdin = open('3752.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    score = list(map(int,input().split()))

    scores = [0]

    for i in score:
        temp = len(scores)
        for j in range(temp-1,-1,-1):
            scores.append(i+scores[j])
        scores = set(scores)
        scores = list(scores)

    print(f'#{tc}', len(scores))