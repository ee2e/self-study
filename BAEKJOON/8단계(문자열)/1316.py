import sys

input = sys.stdin.readline

T = int(input())

cnt = 0
for _ in range(T):
    word = input().strip()

    alpha = []
    for w in word:
        if w not in alpha:
            alpha.append(w)
        else:
            if w != alpha[-1]:
                break
    else:
        cnt += 1

print(cnt)