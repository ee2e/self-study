import sys

input = sys.stdin.readline

numbers = [0]*42
for _ in range(10):
    num = int(input())
    if not numbers[num%42]:
        numbers[num%42] = 1

print(sum(numbers))