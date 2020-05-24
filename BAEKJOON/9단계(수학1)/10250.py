import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    H, W, N = map(int,input().split())

    Y = str(N%H if N%H else H)
    X = str((N-1)//H+1)
    if len(X) == 1: X = '0' + X

    print(Y+X)