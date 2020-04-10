import sys

sys.stdin = open('1204.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    scores = list(map(int,input().split()))

    score_num = [0]*101
    max_score = 0
    result = 0

    for score in scores:
        score_num[score] += 1

    for idx in range(101):
        if score_num[idx] >= max_score:
            max_score = score_num[idx]
            result = idx

    print(f'#{tc}', result)