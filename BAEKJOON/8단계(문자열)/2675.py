import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    R, S = input().split()
    
    i = 0; result = ''
    while i < len(S):
        for _ in range(int(R)):
            result += S[i]
        i += 1

    print(result)