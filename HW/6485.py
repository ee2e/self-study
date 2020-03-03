import sys

sys.stdin = open('6485.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    busstop = [0]*5001
    for _ in range(N):
        a, b = map(int,input().split())
        for i in range(a,b+1):
            busstop[i] += 1

    P = int(input())
    result = []
    for _ in range(P):
        result.append(busstop[int(input())])

    print(f'#{tc} {" ".join(map(str,result))}')