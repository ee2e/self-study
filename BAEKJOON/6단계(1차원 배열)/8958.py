import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    string = input()
    i = 0; score = 0; result = 0
    while i < len(string):
        if string[i] == 'O':
            score += 1
            result += score
        else:
            score = 0
        i += 1
    print(result)