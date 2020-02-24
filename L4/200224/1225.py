import sys

sys.stdin = open('1225.txt', 'r')

T = 10

for tc in range(1,T+1):
    N = int(input())
    data = list(map(int,input().split()))

    while data[-1] != 0:
        d = 1

        while d < 6:
            num = data.pop(0) - d
            if num < 0:
                num = 0

            data.append(num)
            
            if data[-1] == 0:
                break

            d += 1

    print(f'#{N} {" ".join(map(str,data))}')