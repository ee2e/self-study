import sys

input = sys.stdin.readline

maxV = 0; index = 0
for i in range(1,10):
    number = int(input())
    if number > maxV:
        maxV = number
        index = i

print(maxV)
print(index)