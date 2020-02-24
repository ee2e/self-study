import sys

sys.stdin = open('6485.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int,input().split())
        A.append(a)
        B.append(b)
    P = int(input())
    C = []
    for _ in range(P):
        C.append(int(input()))