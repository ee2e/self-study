import sys

sys.stdin = open('1983.txt','r')

T = int(input())

for tc in range(T):
    N, K = map(int,input().split())
    scores_list = [list(map(int,input().split())) for _ in range(N)]

    total_scores = []

    for i in range(N):
        score = scores_list[i][0] * 0.35 + scores_list[i][1] * 0.45 + scores_list[i][2] * 0.2
        total_scores.append(score)

    d = N / 10
    
    K_score = total_scores[K-1]

    total_scores.sort()

    K_rank = total_scores.index(K_score) + 1

    def rank(arg, div):
        if arg <= div:
            return 'D0'
        elif arg <= 2*div:
            return 'C-'
        elif arg <= 3*div:
            return 'C0'
        elif arg <= 4*div:
            return 'C+'
        elif arg <= 5*div:
            return 'B-'
        elif arg <= 6*div:
            return 'B0'
        elif arg <= 7*div:
            return 'B+'
        elif arg <= 8*div:
            return 'A-'
        elif arg <= 9*div:
            return 'A0'
        else:
            return 'A+'

    print(f'#{tc+1} {rank(K_rank,d)}')