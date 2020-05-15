import sys

input = sys.stdin.readline

total = 0
for _ in range(5):
    x = int(input())
    if x >= 40: total += x
    else: total += 40

print(total//5)