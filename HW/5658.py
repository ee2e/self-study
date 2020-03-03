import sys

sys.stdin = open('5658.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int,input().split())
    num = [x for x in input()]
    treasure = []

    for _ in range(N//4):
        for i in range(0,N,N//4):
            temp = ''
            for j in range(i,i+N//4):
                temp += num[j]
            treasure.append(temp)
        num.insert(0, num.pop(-1))

    treasure = list(set(treasure))

    new_num = []
    for i in range(len(treasure)):
        new_num.append(int(treasure[i], 16))

    new_num = sorted(new_num, reverse=True)

    print(f'#{tc} {new_num[K-1]}')