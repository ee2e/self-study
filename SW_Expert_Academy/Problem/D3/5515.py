import sys

sys.stdin = open('5515.txt', 'r')

T = int(input())

for tc in range(T):
    m, d = map(int,input().split())
    week = [3, 4, 5, 6, 0, 1, 2]
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]

    cal = (sum(month[:m]) + d) % 7

    print(f'#{tc+1} {week[cal]}')