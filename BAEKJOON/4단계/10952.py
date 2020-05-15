import sys

input = sys.stdin.readline

A = B = 1
while A+B > 0:
    A, B = map(int,input().split())
    if A+B != 0:
        print(A+B)