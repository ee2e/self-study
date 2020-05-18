import sys

input = sys.stdin.readline

C = int(input())

for _ in range(C):
    data = list(map(int,input().split()))
    N = data[0]
    scores = data[1:]
    
    average = sum(scores)/N
    above_average = 0

    for score in scores:
        if score > average:
            above_average += 1

    print(f'{round(above_average/N*100, 3):.3f}%')