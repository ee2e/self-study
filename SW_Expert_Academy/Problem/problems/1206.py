import sys

sys.stdin = open('1206.txt', 'r')

T = 10

for tc in range(1,T+1):
    length = int(input())
    building = list(map(int,input().split()))

    view = 0
    for i in range(length):
        if building[i]:
            if building[i] > building[i-1] and building[i] > building[i-2] and building[i] > building[i+1] and building[i] > building[i+2]:
                maxV = 0
                for j in range(i-2,i+3):
                    if i != j:
                        if building[j] > maxV:
                            maxV = building[j]
                view += building[i] - maxV

    print(f'#{tc}', view)