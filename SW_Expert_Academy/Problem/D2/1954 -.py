import sys
sys.stdin = open('1954.txt','r')

T = int(input())

for tc in range(T):
    N = int(input())

    x = [1, 0, -1, 0]
    y = [0, -1, 0, 1]

    W = 0