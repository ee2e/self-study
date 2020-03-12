import sys

sys.stdin = open('1289.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    bit = [int(x) for x in input()]

    basic = cnt = 0
    for i in bit:
        if i != basic:
            basic = i
            cnt += 1

    print(f'#{tc}',cnt)