import sys

A = int(input())
B = int(input())
C = int(input())

result = str(A*B*C)

numbers = [0]*10
for num in result:
    numbers[int(num)] += 1

for num in numbers:
    print(num)