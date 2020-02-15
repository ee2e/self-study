import sys

sys.stdin = open('1225.txt', 'r')

for tc in range(10):
    n = int(input())
    data = list(map(int,input().split()))

    while data[-1] > 0:
        d = 1
        while data[-1] > 0 and d < 6:
            data.append(data[0]-d)
            data.pop(0)
            d += 1

    data[-1] = 0

    print(f'#{n} {" ".join(map(str,data))}')