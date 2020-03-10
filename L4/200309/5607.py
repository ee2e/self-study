import sys

sys.stdin = open('5607.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, R = map(int,input().split())
    if R > N-R:
        R0 = N-R
    else:
        R0 = R

    i = 0
    numerator = denominator = 1
    while i < R:
        numerator *= N
        denominator *= R0
        N -= 1
        R0 -= 1
        i += 1

    fraction = numerator//denominator

    if fraction > 1234567891:
        result = fraction % 1234567891
    else:   
        result = fraction
        
    print(f'#{tc} {result}')