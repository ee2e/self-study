import sys

sys.stdin = open('1208.txt', 'r')

T = 10

for tc in range(1,T+1):
    dump = int(input())
    box = list(map(int,input().split()))

    for _ in range(dump):
        maxV = 0; minV = 100
        maxidx = minidx = 0
        for i in range(100):
            if box[i] > maxV:
                maxV = box[i]
                maxidx = i
            if box[i] < minV:
                minV = box[i]
                minidx = i
        box[minidx] += 1
        box[maxidx] -= 1

    maxV = 0; minV = 100
    for i in range(100):
        if box[i] > maxV:
            maxV = box[i]
        if box[i] < minV:
            minV = box[i]

    print(f'#{tc}', maxV-minV)