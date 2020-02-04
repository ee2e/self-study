import sys
sys.stdin = open('1204.txt','r')

T = int(input())

for tc in range(T):
    N = int(input())
    scores = list(map(int,input().split()))
    score_list = [0] * 101

    for score in scores:
        score_list[score] += 1

    result = 0
    idx = 0
    for i in range(len(score_list)):
        if score_list[i] >= result:
            result = score_list[i]
            idx = i
    
    print(f'#{N} {idx}')